---
name: download-new-year-data
version: 0.1
description: Check a specific company in the BusMgmtBenchmarks Dolt database for newly available fiscal year data not yet in the database, validate it for consistency, and generate a SQL INSERT file. For American companies, cross-checks SEC and Yahoo Finance. For non-American companies, uses Yahoo Finance only. Triggered by "/download-new-year-data TICKER".
---

# download-new-year-data

Scan for new fiscal year data not yet in the BusMgmtBenchmarks Dolt database for a specific company, validate it, and generate a SQL INSERT statement. **No database writes — this skill writes a SQL file only.**

## Inputs

`/download-new-year-data TICKER`

- `TICKER` — (required) stock ticker symbol (e.g. `WMT`, `ADS.DE`).

If TICKER is missing, stop and tell the user:
> Please provide a ticker symbol. Usage: `/download-new-year-data TICKER`

---

## Step 1 — Get company info and latest year from Dolt

**1a.** Query `company_info` for the specified company:

```sql
SELECT company, display_name, ticker_symbol, CIK, currency
FROM company_info
WHERE ticker_symbol = '{TICKER}'
```

Use `db_string: calvinw/BusMgmtBenchmarks/main`.

If no row is returned, stop and tell the user:
> **{TICKER} not found in company_info.** Check the ticker or add the company first with `/create-new-company-sql`.

**1b.** Query the latest fiscal year on record for this company:

```sql
SELECT MAX(year) AS latest_year
FROM financials
WHERE company_name = '{company}'
```

**1c.** Display a status line to the user:

> **{display_name} ({TICKER})** — Latest year in DB: {latest_year} | American: {yes/no} | Currency: {currency}

- `american = true` when CIK is not NULL; `american = false` when CIK is NULL.

---

## Step 2 — Fetch data sources to find new years

Fetch external data to identify any fiscal year more recent than `latest_year`.

**Non-American company** (CIK is NULL):

Fetch Yahoo Finance:
```
mcp__yfinance-10ks__process_financial_data_from_yahoo(company_name=display_name, ticker_symbol=TICKER)
```

Inspect the **column headers** of the returned income statement. Each header is a fiscal year-end date (e.g. `2025-12-31`). Derive the DB year label:
- Calendar year of the fiscal year-end date → DB `year` (e.g. `2025-12-31` → `2025`).
- Exception: if the fiscal year end falls in **January or February**, the DB year label is the **prior** calendar year (e.g. `2025-02-01` → `2024`). This matches how US retailers' fiscal years are labeled in the database.

Identify any derived year label > `latest_year`. Those are **candidate new years**.

**American company** (CIK is not NULL):

Fetch Yahoo Finance (same call as above) **and** fetch SEC for each candidate year (`latest_year + 1`, and `+2` if that also looks available):

```
mcp__sec-10ks__process_financial_data_from_sec(company_name=display_name, year=CANDIDATE_YEAR, cik=CIK)
```

Run Yahoo and SEC fetches in parallel where possible. A candidate year is **confirmed available** if SEC returns data for it.

---

## Step 3 — Report what was found

Tell the user which new years were identified:

> **{display_name} ({TICKER})** — Latest in DB: {latest_year} | New years found: {list or "none"}

- If no new year is found:
  > **{display_name} ({TICKER}) is up to date. No new fiscal year data available.**

  Then stop.

- If one or more new years are found, list them and proceed. Process each new year independently, oldest first.

---

## Step 4 — Cross-check SEC vs Yahoo (American companies only)

For each new year, compare SEC and Yahoo values for the **13 standard fields**:

| Field | SEC | Yahoo | Match? |
|-------|-----|-------|--------|
| Net Revenue | … | … | ✓ / ✗ |
| Cost of Goods | … | … | ✓ / ✗ |
| Gross Margin | … | … | ✓ / ✗ |
| SGA | … | … | ✓ / ✗ |
| Operating Profit | … | … | ✓ / ✗ |
| Net Profit | … | … | ✓ / ✗ |
| Inventory | … | … | ✓ / ✗ |
| Current Assets | … | … | ✓ / ✗ |
| Total Assets | … | … | ✓ / ✗ |
| Current Liabilities | … | … | ✓ / ✗ |
| Liabilities | … | … | ✓ / ✗ |
| Total Shareholder Equity | … | … | ✓ / ✗ |
| Total Liab. & SE | … | … | ✓ / ✗ |

Tolerance for "match": within 1% for revenue/assets; exact or within rounding for derived fields.

Apply the anomaly detection rules from `.skillshare/skills/verify-dolt-db-financials/references/anomaly-rules.md`:
- SGA composite rules (Rules 1–4)
- Balance sheet identity check
- Gross margin sanity check

Also check `.skillshare/skills/verify-dolt-db-financials/references/company-notes.md` for any per-company quirks.

Flag issues as `[WARNING]` (investigate) or `[ERROR]` (must resolve before inserting).

**If SEC and Yahoo disagree on a field (>1% difference):**
- Prefer SEC as the authoritative source for that field.
- Flag `[WARNING] Yahoo vs SEC discrepancy on {field}: SEC={x}, Yahoo={y}`.

**For non-American companies:** skip this step. Use Yahoo values directly and flag:
> `[WARNING] No SEC cross-check available — Yahoo Finance only.`

---

## Step 5 — Trend consistency check

Pull all prior years from Dolt for this company:

```sql
SELECT year, `Net Revenue`, `Gross Margin`, `SGA`, `Operating Profit`, `Net Profit`,
       `Total Assets`, `Total Shareholder Equity`
FROM financials
WHERE company_name = '{company}'
ORDER BY year
```

Compute trailing averages from the **3 most recent prior years**:
- Gross margin % = Gross Margin / Net Revenue
- SGA % = SGA / Net Revenue
- Revenue YoY change (from the prior 2 periods)

Check the **new year's candidate values** against these benchmarks:

| Check | Flag level | Condition |
|-------|-----------|-----------|
| Revenue YoY change | `[WARNING]` | > +50% or < −50% vs prior year |
| Gross margin % | `[WARNING]` | More than 5 pp outside the 3-year trailing average |
| SGA % of revenue | `[WARNING]` | More than 5 pp outside the 3-year trailing average |
| Net profit direction | `[WARNING]` | Flips from consistently positive to deeply negative (> −20% of revenue), or vice versa, without a known reason |
| Balance sheet identity | `[ERROR]` | Total Assets ≠ Total Liabilities + Total SE |

Display a trend table showing all prior years plus the new year:

| Year | Revenue | Gross% | SGA% | Op.Profit | Net Profit |
|------|---------|--------|------|-----------|------------|
| 2022 | … | … | … | … | … |
| 2023 | … | … | … | … | … |
| 2024 | … | … | … | … | … |
| **2025 (new)** | … | … | … | … | … |

If an `[ERROR]` is raised, do **not** generate a SQL INSERT for that year — tell the user to resolve it manually before inserting.

---

## Step 6 — Build the SQL INSERT

For each new year that passed Steps 4–5 without `[ERROR]`, build a `REPLACE INTO` statement.

**Determine the value for each field:**
- American company: prefer SEC; use Yahoo as fallback for any field SEC didn't return.
- Non-American company: use Yahoo values.
- Apply any SGA construction adjustments identified in Step 4.
- Always compute: `Gross Margin = Net Revenue − Cost of Goods` and `Liabilities = Total Assets − Total Shareholder Equity`.

```sql
-- {TICKER} FY{YEAR} — new insert
-- Generated by /download-new-year-data on {today's date}
-- Source: {SEC + Yahoo / Yahoo only}
-- currency: {currency}, units: thousands

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
  {Liabilities}, {Total_SE}, {Total_LSE}
);
```

If multiple new years were found, concatenate all statements in one file, oldest year first.

---

## Step 7 — Write the SQL file

Write to: `extract/2026/inserts/new-year-data/new_year_{TICKER}_{today's date}.sql`

Example: `extract/2026/inserts/new-year-data/new_year_WMT_2026-06-05.sql`

Show the full file contents to the user.

---

## Step 8 — Print summary and apply instructions

After writing the file, display:

---

**Download-new-year-data complete — {display_name} ({TICKER})**

| New Year(s) Inserted | Warnings | Skipped (errors) |
|----------------------|----------|------------------|
| {year list}          | {N}      | {year list or —} |

**SQL file written to:** `extract/2026/inserts/new-year-data/{FILENAME}`

To apply this to your local Dolt database clone:

```bash
# 1. Navigate to your local Dolt repo
cd /path/to/your/dolt/BusMgmtBenchmarks

# 2. Run the SQL
dolt sql < /path/to/BusMgmtBenchmarks/extract/2026/inserts/new-year-data/{FILENAME}

# 3. Review what changed
dolt diff

# 4. Commit locally when satisfied
dolt commit -am "Add {display_name} ({TICKER}) FY{year_list}"

# 5. Push to DoltHub when ready
dolt push
```

---

## References

- **`anomaly-rules.md`** — SGA composite rules, balance sheet checks, gross margin benchmarks. Read in Step 4.
- **`company-notes.md`** — Per-company quirks. Check in Step 4.

Both files live at `.skillshare/skills/verify-dolt-db-financials/references/`.
