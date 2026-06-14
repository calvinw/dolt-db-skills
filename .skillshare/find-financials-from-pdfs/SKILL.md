---
name: find-financials-from-pdfs
description: Extract financial data from PDF annual reports for private companies not listed on public exchanges, standardize the data to match the BusMgmtBenchmarks schema, and generate SQL files for insertion into the company_info and financials tables. Use when adding a private company (e.g. ACE Hardware) from PDF sources. Triggered by "/find-financials-from-pdfs COMPANY NAME".
---

# find-financials-from-pdfs

Extract financial data from PDF annual reports for private companies and generate SQL files ready for insertion into the BusMgmtBenchmarks Dolt database.

## Inputs

`/find-financials-from-pdfs COMPANY NAME`

- `COMPANY NAME` — the full company name (e.g. `ACE Hardware`)

## Step 0 — Locate PDFs and confirm years

Scan the `references/` folder inside `.skillshare/find-financials-from-pdfs/references/` for all `.pdf` files.

Display what was found:

> Found {N} PDF file(s): file1.pdf, file2.pdf, …

For each PDF, try to infer the fiscal year(s) it covers from the filename (e.g. `ace-hardware-2023.pdf` → 2023). If unclear, note it as "year unknown."

Ask the user to confirm:

> These PDFs appear to cover the following years: {year1}, {year2}, …
> Is this correct, or would you like to specify which years to process?

Wait for confirmation before proceeding.

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

## Step 2 — Infer and confirm company metadata

Read the first available PDF to infer the following fields:

| Field | What to look for |
|---|---|
| `display_name` | The company's full name as it appears in the document |
| `segment` | Broad category (e.g. "Retail", "Wholesale") |
| `subsegment` | More specific category (e.g. "Home Improvement", "Grocery") |
| `currency` | Currency used in the financials (e.g. "USD") |
| `units` | Scale of numbers (e.g. "thousands", "millions") — convert to thousands for DB |

Note: `CIK` and `ticker_symbol` are left as NULL for private companies — do not attempt to fill these.

While reading the PDFs, scan the financial statement headers in **all PDFs** to identify the actual fiscal years covered inside each one. Build a complete mapping of PDF → actual years found.

Then identify **all overlapping years** across all PDFs — not just between consecutive PDFs. For every year that appears in more than one PDF, the **earliest PDF is the primary source** and all others serve as **verification**.

Present your best guess to the user for confirmation:

> Based on the PDFs, here is what I found for **{Company Name}**:
> - display_name: {value}
> - segment: {value}
> - subsegment: {value}
> - currency: {value}
> - units: {value} (will be stored as thousands)
>
> Here are the actual years found inside each PDF:
> - `{pdf1}` → {year1}, {year2}, {year3}
> - `{pdf2}` → {year1} *(overlap with pdf1 — verify)*, {year2}, {year3} *(overlap with pdf3 — verify)*
> - `{pdf3}` → {year1}, {year2}
>
> Overlap summary:
> | Year | Primary | Verified by |
> |---|---|---|
> | {yearX} | {pdf1} | {pdf2} |
> | {yearY} | {pdf2} | {pdf3} |
>
> Combined unique years to process: {all unique years}. Are there any years you'd like to add or exclude before I proceed?

Wait for confirmation or corrections before proceeding. Use the confirmed year list (not the Step 0 estimate) going forward.

## Step 3 — Read PDFs and extract financial data

For each year confirmed, read the corresponding PDF using the Read tool.

Extract the following 13 fields per year. All values must be in **thousands of dollars** (convert if the PDF uses millions: multiply by 1,000).

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

Write a single SQL file to `extract/2026/inserts/{COMPANY_SLUG}-{YEARS}.sql`.

- `COMPANY_SLUG` = company name lowercased with hyphens (e.g. `ace-hardware`)
- `YEARS` = year range (e.g. `2021-2024` or single year `2023`)

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

> SQL file saved to `extract/2026/inserts/{filename}.sql`.
>
> Review the file, then apply it manually to the database when ready.

List any `[WARNING]` flags for the user to review before inserting.

## References

- PDF files are stored in `.skillshare/find-financials-from-pdfs/references/`
- Target tables: `company_info` and `financials` on `calvinw/BusMgmtBenchmarks/main`
- All numeric values stored in **thousands**
- Private companies: `CIK` and `ticker_symbol` are left as NULL
