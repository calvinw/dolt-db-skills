---
name: find-financials-from-pdfs
description: Extract financial data from PDF annual reports for private companies not listed on public exchanges, standardize the data to match the BusMgmtBenchmarks schema, and generate SQL files for insertion into the company_info and financials tables. Use when adding a private company (e.g. ACE Hardware) from PDF sources. Triggered by "/find-financials-from-pdfs COMPANY NAME".
---

# find-financials-from-pdfs

Extract financial data from PDF annual reports for private companies and generate SQL files ready for insertion into the BusMgmtBenchmarks Dolt database.

## Inputs

`/find-financials-from-pdfs COMPANY NAME`

- `COMPANY NAME` — the full company name (e.g. `ACE Hardware`)

## Step 1 — Check if company already exists

Query the Dolt database:

```sql
SELECT * FROM company_info WHERE company = '{company_name}'
```

Use `db_string: calvinw/BusMgmtBenchmarks/main`.

- **If the row exists** — note the existing metadata. Also fetch the existing financials rows for this company:

  ```sql
  SELECT * FROM financials WHERE company_name = '{company_name}' ORDER BY year
  ```

  Store these values — after extracting from PDFs in Step 3, you will compare them side by side in Step 5 and flag any differences. Skip to Step 3.

- **If no row exists** — proceed to Step 2 to collect metadata.

## Step 2 — Scan PDFs, infer metadata, and confirm years

Scan the `references/` folder inside `.skillshare/find-financials-from-pdfs/references/` for all `.pdf` files. Read all PDFs to:

1. Infer company metadata from the first PDF:

| Field | What to look for |
|---|---|
| `display_name` | The company's full name as it appears in the document |
| `segment` | Broad category (e.g. "Retail", "Wholesale") |
| `subsegment` | More specific category (e.g. "Home Improvement", "Grocery") |
| `currency` | Currency used in the financials (e.g. "USD") |
| `units` | Scale of numbers (e.g. "thousands", "millions") — convert to thousands for DB |

Note: `CIK` and `ticker_symbol` are left as NULL for private companies — do not attempt to fill these.

2. Scan financial statement headers in **all PDFs** to identify the actual fiscal years covered. Build a complete mapping of PDF → actual years found.

3. Identify **all overlapping years** across all PDFs. For every year that appears in more than one PDF, the **earliest PDF is the primary source** and all others serve as **verification**.

Present findings to the user for confirmation:

> Based on the PDFs, here is what I found for **{Company Name}**:
> - display_name: {value}
> - segment: {value}
> - subsegment: {value}
> - currency: {value}
> - units: {value} (will be stored as thousands)
>
> | Year | Primary Source | Verified by |
> |---|---|---|
> | FY{year1} | {pdf} | — |
> | FY{year2} | {pdf} | {pdf} |
> | FY{year3} | {pdf} | {pdf} |
> | … | | |
>
> Are there any years you'd like to exclude before I proceed?

Wait for confirmation or corrections before proceeding.

## Step 3 — Extract financial data

For each confirmed year, read the corresponding PDF and extract the following 13 fields. All values must be in **thousands of dollars** (convert if the PDF uses millions: multiply by 1,000).

| Field | Notes |
|---|---|
| `Net Revenue` | Total sales / revenue |
| `Cost of Goods` | COGS — positive value |
| `Gross Margin` | Net Revenue − Cost of Goods |
| `SGA` | Selling, General & Administrative expenses |
| `Operating Profit` | Can be negative |
| `Net Profit` | Can be negative |
| `Inventory` | Use NULL if not applicable |
| `Current Assets` | |
| `Total Assets` | |
| `Current Liabilities` | |
| `Liabilities` | Total Assets − Total Shareholder Equity |
| `Total Shareholder Equity` | Can be negative |
| `Total Liabilities and Shareholder Equity` | Must equal Total Assets |

Also extract `reportDate` — the fiscal year-end date (e.g. `2023-12-31`).

If a field cannot be found in the PDF, set it to `NULL`. **Never guess or estimate values.**

Track which PDF filename each year's data came from — this will be stored in `source_pdf`.

For overlapping years, extract values from both PDFs and compare:
- If values match → use the primary PDF value, set `source_pdf` to `"{pdf1}, {pdf2} (verified)"`
- If values differ → flag `[WARNING] overlap mismatch: {pdf1} shows {value}, {pdf2} shows {value}` and ask the user which to use before generating SQL

## Step 4 — Validate the extracted data

Run these basic checks for each year:

1. **Balance sheet check**: `Total Assets` = `Total Liabilities and Shareholder Equity` → if not, flag `[WARNING]`
2. **Gross margin check**: `Gross Margin` = `Net Revenue` − `Cost of Goods` → if not, flag `[WARNING]`
3. **NULL check**: If more than 5 of the 13 fields are NULL, flag `[WARNING] — many fields missing, verify PDF quality`

Do not block SQL generation for warnings — just display them so the user can review.

## Step 5 — Display side-by-side summary

Show a table of extracted values per year. If the company already existed in the DB (Step 1), add a column for the current DB value and mark differences with `*`:

| Field | PDF ({Year}) | DB (current) |
|---|---|---|
| Net Revenue | | |
| … | | |

If the company is new, just show the PDF values:

| Field | {Year1} | {Year2} | … |
|---|---|---|---|
| Net Revenue | | | |
| … | | | |

Mark any `[WARNING]` fields and any `*` differences clearly. For each difference, note:
> `[DIFF]` {Field}: DB has {old value}, PDF has {new value} — will be overwritten by REPLACE INTO.

## Step 6 — Generate SQL file

Write a single SQL file to `extract/2026/inserts/private/{COMPANY_SLUG}_{FIRST_YEAR}-{LAST_YEAR}.sql`.

- `COMPANY_SLUG` = company name lowercased with hyphens (e.g. `ace-hardware`)
- `FIRST_YEAR` and `LAST_YEAR` = first and last year processed (e.g. `ace-hardware_2021-2025.sql`). If only one year, use `ace-hardware_2023.sql`.

The file should contain:

**If company is new** (not found in Step 1):

```sql
REPLACE INTO company_info
  (company, display_name, segment, subsegment, currency, units)
VALUES
  ('{company}', '{display_name}', '{segment}', '{subsegment}', '{currency}', 'thousands');
```

**For each year:**

```sql
REPLACE INTO financials
  (company_name, year, reportDate, `Net Revenue`, `Cost of Goods`, `Gross Margin`,
   SGA, `Operating Profit`, `Net Profit`, Inventory, `Current Assets`, `Total Assets`,
   `Current Liabilities`, Liabilities, `Total Shareholder Equity`,
   `Total Liabilities and Shareholder Equity`, source_pdf)
VALUES
  ('{company}', {year}, '{reportDate}', {Net Revenue}, {Cost of Goods}, {Gross Margin},
   {SGA}, {Operating Profit}, {Net Profit}, {Inventory}, {Current Assets}, {Total Assets},
   {Current Liabilities}, {Liabilities}, {Total Shareholder Equity},
   {Total Liabilities and Shareholder Equity}, '{source_pdf}');
```

Use `NULL` (without quotes) for any missing numeric fields.

## Step 7 — Signal completion

Tell the user:

> SQL file saved to `extract/2026/inserts/private/{filename}.sql`.
>
> Review the file, then apply it manually to the database when ready.

List any `[WARNING]` flags for the user to review before inserting.

## References

- PDF files are stored in `.skillshare/find-financials-from-pdfs/references/`
- Target tables: `company_info` and `financials` on `calvinw/BusMgmtBenchmarks/main`
- All numeric values stored in **thousands**
- Private companies: `CIK` and `ticker_symbol` are left as NULL
