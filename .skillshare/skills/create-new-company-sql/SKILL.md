---
name: create-new-company-sql
version: 0.1
description: Fetch financial data from SEC 10-K filings and Yahoo Finance for a NEW company (2018 through current year), reconcile values, and generate SQL files to insert the company_info row and all financials rows. Does NOT write to the database directly. Triggered by "/create-new-company-sql TICKER [CIK]".
---

# create-new-company-sql

Generate SQL files to add a new company to the BusMgmtBenchmarks Dolt database, spanning 2018 through the current year. **No database connection is made for writes — this skill writes files only.**

Use this for brand-new companies not yet in the Dolt DB. If the company already exists, use `/verify-dolt-db-financials` instead.

## Inputs

`/create-new-company-sql TICKER [CIK]`

- `TICKER` — stock ticker symbol (e.g. WSM, BBW, GPS)
- `CIK` — (optional) SEC Central Index Key number. If omitted, the skill will look it up from Yahoo or prompt the user.

## Step 1 — Verify company does not already exist

Query the Dolt database to check if this company already exists:

```sql
SELECT company, ticker_symbol FROM company_info WHERE ticker_symbol = '{TICKER}'
```

If a row is returned, stop and tell the user:
> **{display_name} ({TICKER}) already exists in the Dolt database. Use `/verify-dolt-db-financials {TICKER}` to update or verify its data.**

If no row is returned, proceed.

## Step 2 — Determine CIK and company name

**If CIK was provided:**
- Use it directly.
- Fetch the company name via SEC: `mcp__mcp-sec-10ks__process_financial_data_from_sec(company_name='Company', year=2024, cik=CIK)` — the response will contain the legal company name. Extract it.

**If CIK was NOT provided:**
- Fetch Yahoo Finance data to get company metadata:
  ```
  mcp__mcp-yfinance-10ks__process_financial_data_from_yahoo(company_name='Company', ticker_symbol=TICKER)
  ```
  The response headers usually contain the company name. Extract `display_name` from the results.
- Search the web for the company's CIK number: `"{display_name} SEC CIK number"` or use `"{display_name} CIK sec.gov"`.
- If CIK cannot be found, set `CIK = NULL` (non-US company or no SEC filing) and skip **Step 3** (SEC fetches). Use Yahoo as the sole source.

## Step 3 — Gather company metadata

Collect or confirm these fields. Prompt the user for any that cannot be auto-detected:

| Field | How to determine |
|-------|-----------------|
| `company` | The company name used as the `company_name` key in `financials`. Use the legal name from SEC/Yahoo, shortened if needed (e.g. "Williams-Sonoma" not "Williams-Sonoma, Inc."). |
| `display_name` | Full display name (e.g. "Williams-Sonoma") |
| `CIK` | From Step 2 (or NULL) |
| `ticker_symbol` | From user input |
| `segment` | Retail segment from the list: Online, Specialty, Grocery, Warehouse Clubs, Off Price, Department Store, Discount Store, Fast Fashion, Home Improvement, Health & Pharmacy, Resale. Look up the company's business description if unsure. **Prompt the user.** |
| `subsegment` | Optional subsegment (e.g. Apparel, Category Killer, Accessories and Shoes, Beauty, Home). Can be NULL. **Prompt the user.** |
| `currency` | Reporting currency (e.g. USD, EUR, GBP). Usually USD for US SEC filers. |
| `units` | Always `thousands` for BusMgmtBenchmarks (all values stored in thousands). |

Show the user the proposed metadata and ask for confirmation before proceeding.

## Step 4 — Fetch all data sources

**4a. Determine the year range.**
Current year is 2026. The range is 2018 through 2026 inclusive.

**4b. Fetch Yahoo Finance data (one call covers all years):**
```
mcp__mcp-yfinance-10ks__process_financial_data_from_yahoo(company_name=display_name, ticker_symbol=TICKER)
```
Inspect the column headers to identify which fiscal years Yahoo provides data for. Note any years in the 2018–2026 range that Yahoo is missing.

**4c. Fetch SEC data (one call per year, if CIK is available).**
For each year from 2018 to 2026:
```
mcp__mcp-sec-10ks__process_financial_data_from_sec(company_name=display_name, year=YEAR, cik=CIK)
```
Note any years where SEC data is unavailable (e.g. company wasn't public yet).

**4d. Display the coverage summary:**
> Data coverage for {display_name} ({TICKER}):
> | Year | SEC | Yahoo |
> |------|-----|-------|
> | 2018 | ✓ | ✓ |
> | ...  |   |   |
> | 2026 | ✓ | ✓ |

## Step 5 — Extract and reconcile values (per year, 2018 → current)

For each available year, process independently (oldest first):

**5a. Extract the 13 standard fields from each source.**

All values in **thousands of dollars**:

| Field | Notes |
|-------|-------|
| Net Revenue | |
| Cost of Goods | Positive value |
| Gross Margin | Revenue − COGS (calculate; don't trust source directly) |
| SGA | Most error-prone — see anomaly rules in references |
| Operating Profit | Can be negative |
| Net Profit | Can be negative |
| Inventory | NULL for pure marketplace companies |
| Current Assets | |
| Total Assets | |
| Current Liabilities | |
| Liabilities | Total Assets − Total SE (calculate) |
| Total Shareholder Equity | Can be negative |
| Total Liabilities and Shareholder Equity | Must equal Total Assets |

Also extract `reportDate` (fiscal year-end date, e.g. `2024-12-31`).

**5b. Apply anomaly detection rules.**

Read the **anomaly-rules.md** file from the verify-dolt-db-financials references:
- `references/anomaly-rules.md` (accessible via the existing skill's references)
- Apply all SGA composite rules (Rules 1–4)
- Apply balance sheet identity check
- Apply gross margin sanity check
- Apply inventory rules

If the company has no SEC data (CIK is NULL), use Yahoo values directly but flag a `[WARNING] that SEC data was unavailable`.

**5c. For each year, determine the action:**

- If this year has data (from SEC, Yahoo, or both): mark as **New insert**
- If no data source has this year: mark as **No data — skip**

## Step 6 — Build the SQL file

**6a. Create the `extract/2026/create_company/` directory if it does not exist.**

**6b. Build a single SQL file:** `extract/2026/create_company/{TICKER}_create.sql`

The file contains two sections, in order:

**Section A — Company info:**

```sql
-- ============================================================
-- {TICKER} — New company setup
-- Generated by /create-new-company-sql on YYYY-MM-DD
-- ============================================================

INSERT INTO company_info (
  company, CIK, display_name, ticker_symbol,
  segment, subsegment, currency, units
) VALUES (
  '{company}', {CIK_OR_NULL}, '{display_name}', '{TICKER}',
  '{segment}', {subsegment_OR_NULL}, '{currency}', 'thousands'
);
```

**Section B — Financials (one REPLACE INTO per year, oldest first):**

```sql
-- ============================================================
-- Financials: {display_name} ({TICKER}) — FY2018 to FY{current_year}
-- ============================================================

-- {display_name} FY{year} — New insert
REPLACE INTO financials (
  company_name, year, reportDate,
  `Net Revenue`, `Cost of Goods`, `Gross Margin`, `SGA`,
  `Operating Profit`, `Net Profit`, `Inventory`,
  `Current Assets`, `Total Assets`, `Current Liabilities`,
  `Liabilities`, `Total Shareholder Equity`,
  `Total Liabilities and Shareholder Equity`
) VALUES (
  '{company}', {year}, '{reportDate}',
  {Net_Revenue}, {Cost_of_Goods}, {Gross_Margin}, {SGA},
  {Operating_Profit}, {Net_Profit}, {Inventory_OR_NULL},
  {Current_Assets}, {Total_Assets}, {Current_Liabilities},
  {Liabilities}, {Total_SE},
  {Total_LSE}
);
```

**6c. Show the full SQL file contents to the user.**

## Step 7 — Write the report file

Write a report to `reports/{TICKER}-create.md` summarizing:

1. Company metadata (what was inserted into `company_info`)
2. Per-year data coverage table (which years had SEC, Yahoo, or both)
3. Per-year reconciled values table
4. Any anomalies or warnings found
5. A note that no existing Dolt data was overwritten (new company)

Start the report with:

```
# {display_name} ({TICKER}) — New Company Data (FY2018–FY{current_year})

**Generated:** {today's date}
**Source:** /create-new-company-sql skill
**Action:** New company setup

---
```

## Step 8 — Print summary and apply instructions

After writing the files, display:

---

**Files written:**

| File | Path |
|------|------|
| SQL | `extract/2026/create_company/{TICKER}_create.sql` |
| Report | `reports/{TICKER}-create.md` |

**SQL covers:**
- `company_info` — 1 INSERT
- `financials` — {N} REPLACE statements (years: {year_list})

To apply this to your local Dolt database clone:

```bash
# 1. Navigate to your local Dolt repo
cd /path/to/your/dolt/BusMgmtBenchmarks

# 2. Run the SQL
dolt sql < /path/to/BusMgmtBenchmarks/extract/2026/create_company/{TICKER}_create.sql

# 3. Review what changed
dolt diff

# 4. Commit locally when satisfied
dolt commit -am "Add {display_name} ({TICKER}) — new company (FY2018–FY{current_year})"

# 5. Push to DoltHub when ready
dolt push
```

---

That's it. The skill's job is done once the files are written.
