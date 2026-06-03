# Bath & Body Works (BBWI) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-03
**Source:** /verify-dolt-db-financials skill

---

## Critical Findings

### 1. Wrong CIK in company_info
The Dolt `company_info` table has `CIK = 886158` for BBWI. **CIK 886158 is Bed Bath & Beyond (BBBY)**, not Bath & Body Works. The correct CIK for Bath & Body Works / L Brands is **701985**.

The insert SQL must include: `UPDATE company_info SET CIK = 701985 WHERE ticker_symbol = 'BBWI'`

### 2. Dolt years 2018–2022 contain Bed Bath & Beyond data
Because the wrong CIK was used in prior analysis, all five pre-2023 rows in Dolt for BBWI actually contain BBBY financial data. All reportDates in those rows end in late February / early March — BBBY's fiscal year end — not BBWI's late January / early February end.

- Dolt year 2022 (reportDate 2023-02-25): Revenue 5,344,685K with $1.3B impairment charges → BBBY going-bankrupt year
- Dolt year 2021 (reportDate 2022-02-26): Revenue 7,867,778K → matches BBBY FY2021, not BBWI
- Dolt years 2018–2020: Revenue $9–12B range → all match BBBY revenue, not BBWI

### 4. FY2018–FY2020: L Brands combined (pre-spinoff)
SEC data fetched for years 2018–2020 using the correct CIK 701985. These filings are **L Brands combined** — including both the Bath & Body Works segment and the Victoria's Secret segment, which was not spun off until August 2021. Revenues ($11.8–13.2B) are therefore much larger than BBWI standalone ($7.9B FY2021+) and include VS assets/liabilities on the balance sheet.

This is the only available data for CIK 701985 for those years. It is used to replace the completely wrong BBBY data. The report clearly labels all three years as L Brands combined.

### 3. BBWI background
- **CIK:** 701985 (formerly L Brands, Inc.)
- **Spinoff:** Victoria's Secret (VSCO) was spun off on August 2, 2021. The remaining L Brands entity was renamed Bath & Body Works, Inc. CIK 701985 was retained by BBWI.
- **Fiscal year end:** Late January / early February (e.g., Jan 28, Jan 29, Feb 1, Feb 3)
- **Segment:** Specialty (beauty / personal care). Expected gross margin: 35–55%.
- **Equity:** Negative TSE is expected — company carries significant long-term debt.
- **Discontinued operations:** VS appears as discontinued ops in FY2021 10-K (and prior comparatives). For FY2021, $258M gain from VS spinoff is included in total Net Income. FY2022+ have no material discontinued ops.
- **SGA:** Single `us-gaap_SellingGeneralAndAdministrativeExpense` line — no separate marketing split. Use directly.
- **Currency:** All values in $thousands (USD).

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2019-02-02 | Correction: ALL fields — was BBBY data; replacing with L Brands combined (B&BW + VS pre-spinoff) |
| 2019 | 2020-02-01 | Correction: ALL fields — was BBBY data; replacing with L Brands combined (includes $720M VS goodwill impairment) |
| 2020 | 2021-01-30 | Correction: ALL fields — was BBBY data; replacing with L Brands combined (final pre-spinoff year) |
| 2021 | 2022-01-29 | Correction: ALL fields — replacing BBBY data with BBWI standalone |
| 2022 | 2023-01-28 | Correction: ALL fields — replacing BBBY data with BBWI standalone |
| 2023 | 2024-02-03 | Correction: reportDate only (was 2024-01-31, should be 2024-02-03); financials ✓ |
| 2024 | 2025-02-01 | New insert |
| 2025 | 2026-01-31 | New insert |

---

## FY2018

**Sources:** SEC 10-K (CIK 701985, L Brands FY2018, period ending 2019-02-02) — **L Brands combined (B&BW + Victoria's Secret)**

### Anomaly Detection
- `[WARNING]` This is **L Brands combined** data — includes both Bath & Body Works and Victoria's Secret segments. Revenue ($13,237,000K) is much larger than BBWI standalone ($7.9B in FY2021) because it includes VS. Flag for awareness.
- `[ERROR]` Current Dolt row contains BBBY data (Revenue $12,028,797K, reportDate 2019-03-02). All fields replaced.
- Gross margin: 4,899,000 / 13,237,000 = 37.0% — within Specialty benchmark (35–55%) ✓
- Operating Profit includes −99,000K loss on La Senza divestiture; already embedded in the 1,237,000K total.
- Balance sheet identity: 8,959,000 + (−869,000) = 8,090,000 ✓
- Note: Goodwill of 1,348,000K includes both B&BW and VS goodwill; VS goodwill was later impaired in FY2019.

### Side-by-Side

| Field | SEC (L Brands combined) | Yahoo | Dolt (WRONG — BBBY) | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 13,237,000 | — | 12,028,797 | **13,237,000** |
| Cost of Goods | 8,338,000 | — | 7,924,817 | **8,338,000** |
| Gross Margin | 4,899,000 | — | 4,103,980 | **4,899,000** |
| SGA | 3,563,000 | — | 3,681,210 | **3,563,000** |
| Operating Profit | 1,237,000 | — | -87,135 | **1,237,000** |
| Net Profit | 644,000 | — | -137,224 | **644,000** |
| Inventory | 1,248,000 | — | 2,618,922 | **1,248,000** |
| Current Assets | 3,260,000 | — | 3,909,972 | **3,260,000** |
| Total Assets | 8,090,000 | — | 6,570,541 | **8,090,000** |
| Current Liabilities | 1,986,000 | — | 2,077,632 | **1,986,000** |
| Liabilities | 8,959,000 | — | 4,010,210 | **8,959,000** |
| Total Shareholder Equity | -869,000 | — | 2,560,331 | **-869,000** |
| TL&SE | 8,090,000 | — | 6,570,541 | **8,090,000** |
| reportDate | 2019-02-02 | — | 2019-03-02 | **2019-02-02** |

### Reconciled Values
All values from SEC 10-K (CIK 701985, L Brands combined). Balance sheet identity: 8,959,000 + (−869,000) = 8,090,000 ✓

---

## FY2019

**Sources:** SEC 10-K (CIK 701985, L Brands FY2019, period ending 2020-02-01) — **L Brands combined (B&BW + Victoria's Secret)**

### Anomaly Detection
- `[WARNING]` This is **L Brands combined** data — includes both Bath & Body Works and Victoria's Secret segments.
- `[ERROR]` Current Dolt row contains BBBY data (Revenue $11,158,580K, reportDate 2020-02-29). All fields replaced.
- `[WARNING]` FY2019 includes a **$720,000K goodwill impairment** (Victoria's Secret brand write-down). This sharply reduces Operating Profit to 258,000K and drives Net Income to −366,000K. This is a one-time VS impairment, not a B&BW issue.
- Gross margin: 4,450,000 / 12,914,000 = 34.5% — slightly below Specialty benchmark (VS declining drag) ✓
- Balance sheet identity: 11,624,000 + (−1,499,000) = 10,125,000 ✓

### Side-by-Side

| Field | SEC (L Brands combined) | Yahoo | Dolt (WRONG — BBBY) | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 12,914,000 | — | 11,158,580 | **12,914,000** |
| Cost of Goods | 8,464,000 | — | 7,616,920 | **8,464,000** |
| Gross Margin | 4,450,000 | — | 3,541,660 | **4,450,000** |
| SGA | 3,472,000 | — | 3,732,498 | **3,472,000** |
| Operating Profit | 258,000 | — | -700,064 | **258,000** |
| Net Profit | -366,000 | — | -613,816 | **-366,000** |
| Inventory | 1,287,000 | — | 2,093,869 | **1,287,000** |
| Current Assets | 3,245,000 | — | 3,826,285 | **3,245,000** |
| Total Assets | 10,125,000 | — | 7,790,515 | **10,125,000** |
| Current Liabilities | 2,372,000 | — | 2,466,526 | **2,372,000** |
| Liabilities | 11,624,000 | — | 6,025,580 | **11,624,000** |
| Total Shareholder Equity | -1,499,000 | — | 1,764,935 | **-1,499,000** |
| TL&SE | 10,125,000 | — | 7,790,515 | **10,125,000** |
| reportDate | 2020-02-01 | — | 2020-02-29 | **2020-02-01** |

### Reconciled Values
All values from SEC 10-K (CIK 701985, L Brands combined). Balance sheet identity: 11,624,000 + (−1,499,000) = 10,125,000 ✓

---

## FY2020

**Sources:** SEC 10-K (CIK 701985, L Brands FY2020, period ending 2021-01-30) — **L Brands combined (final pre-spinoff year)**

### Anomaly Detection
- `[WARNING]` This is **L Brands combined** data — final year before Victoria's Secret was spun off (August 2021). Includes both B&BW and VS for the full fiscal year.
- `[ERROR]` Current Dolt row contains BBBY data (Revenue $9,233,028K, reportDate 2021-02-27). All fields replaced.
- Gross margin: 4,667,000 / 11,847,000 = 39.4% — within Specialty benchmark ✓ (B&BW's strong COVID year lifted margins)
- Balance sheet identity: 12,233,000 + (−662,000) = 11,571,000 ✓
- Note: Current Assets ($5,579,000K) are very high due to $3,903,000K in cash (L Brands built cash reserves during COVID)

### Side-by-Side

| Field | SEC (L Brands combined) | Yahoo | Dolt (WRONG — BBBY) | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 11,847,000 | — | 9,233,028 | **11,847,000** |
| Cost of Goods | 7,180,000 | — | 6,114,947 | **7,180,000** |
| Gross Margin | 4,667,000 | — | 3,118,081 | **4,667,000** |
| SGA | 3,087,000 | — | 3,224,363 | **3,087,000** |
| Operating Profit | 1,580,000 | — | -336,887 | **1,580,000** |
| Net Profit | 844,000 | — | -150,773 | **844,000** |
| Inventory | 1,273,000 | — | 1,671,909 | **1,273,000** |
| Current Assets | 5,579,000 | — | 3,620,045 | **5,579,000** |
| Total Assets | 11,571,000 | — | 6,456,930 | **11,571,000** |
| Current Liabilities | 2,826,000 | — | 2,294,921 | **2,826,000** |
| Liabilities | 12,233,000 | — | 5,179,994 | **12,233,000** |
| Total Shareholder Equity | -662,000 | — | 1,276,936 | **-662,000** |
| TL&SE | 11,571,000 | — | 6,456,930 | **11,571,000** |
| reportDate | 2021-01-30 | — | 2021-02-27 | **2021-01-30** |

### Reconciled Values
All values from SEC 10-K (CIK 701985, L Brands combined). Balance sheet identity: 12,233,000 + (−662,000) = 11,571,000 ✓

---

## FY2021

**Sources:** SEC 10-K (CIK 701985, FY2021, period ending 2022-01-29) — first BBWI standalone year

### Anomaly Detection
- `[ERROR]` Current Dolt row contains BBBY data (Revenue 7,867,778K with BBBY reportDate 2022-02-26). All fields must be replaced.
- `[WARNING]` Net Profit: FY2021 includes $258,000K from discontinued operations (Victoria's Secret spinoff gain). Total `us-gaap_NetIncomeLoss` = 1,333,000K; continuing operations only = 1,075,000K. Using total NetIncomeLoss per DB convention, but flag for awareness — the 258M is a one-time spinoff event.
- Gross margin: 3,855,000 / 7,882,000 = 48.9% — within Specialty benchmark (35–55%) ✓
- Balance sheet identity: 6,026,000 + (-1,518,000) = 4,508,000 ✗ — wait, this checks differently: Liabilities + TSE = TL&SE → 7,544,000 + (-1,518,000) = 6,026,000 ✓
- Negative TSE (-1,518,000K) is expected — highly leveraged company.
- Yahoo does not have FY2021 data (5-year window starts at FY2022).

### Side-by-Side

| Field | SEC | Yahoo | Dolt (WRONG — BBBY) | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 7,882,000 | — | 7,867,778 | **7,882,000** |
| Cost of Goods | 4,027,000 | — | 5,384,287 | **4,027,000** |
| Gross Margin | 3,855,000 | — | 2,483,491 | **3,855,000** |
| SGA | 1,846,000 | — | 2,692,292 | **1,846,000** |
| Operating Profit | 2,009,000 | — | -407,578 | **2,009,000** |
| Net Profit | 1,333,000 | — | -559,623 | **1,333,000** |
| Inventory | 709,000 | — | 1,725,410 | **709,000** |
| Current Assets | 3,009,000 | — | 2,363,154 | **3,009,000** |
| Total Assets | 6,026,000 | — | 5,130,572 | **6,026,000** |
| Current Liabilities | 1,290,000 | — | 2,074,787 | **1,290,000** |
| Liabilities | 7,544,000 | — | 4,956,427 | **7,544,000** |
| Total Shareholder Equity | -1,518,000 | — | 174,145 | **-1,518,000** |
| TL&SE | 6,026,000 | — | 5,130,572 | **6,026,000** |
| reportDate | 2022-01-29 | — | 2022-02-26 | **2022-01-29** |

### Reconciled Values

All values from SEC 10-K (CIK 701985). Balance sheet identity: 7,544,000 + (-1,518,000) = 6,026,000 ✓

---

## FY2022

**Sources:** SEC 10-K (CIK 701985, FY2022, period ending 2023-01-28) + Yahoo Finance (column 2023-01-31)

### Anomaly Detection
- `[ERROR]` Current Dolt row contains BBBY data (Revenue 5,344,685K with huge impairment charges — BBBY's bankruptcy year). All fields must be replaced.
- Income statement confirmed: SEC = Yahoo for all fields ✓
- Balance sheet confirmed: SEC = Yahoo (within 1K rounding on Liabilities) ✓
- Gross margin: 3,255,000 / 7,560,000 = 43.1% — within Specialty benchmark ✓
- Negative TSE (-2,206,000K) — normal for BBWI's capital structure.
- Net Profit: $6,000K from discontinued operations included in total 800,000K; continuing ops = 794,000K. Using total.
- Balance sheet identity: 7,700,000 + (-2,206,000) = 5,494,000 ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt (WRONG — BBBY) | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 7,560,000 | 7,560,000 | 5,344,685 | **7,560,000** |
| Cost of Goods | 4,305,000 | 4,305,000 | 4,129,802 | **4,305,000** |
| Gross Margin | 3,255,000 | 3,255,000 | 1,214,883 | **3,255,000** |
| SGA | 1,879,000 | 1,879,000 | 2,372,969 | **1,879,000** |
| Operating Profit | 1,376,000 | 1,376,000 | -2,775,639 | **1,376,000** |
| Net Profit | 800,000 | 800,000 | -3,498,801 | **800,000** |
| Inventory | 709,000 | 709,000 | 817,553 | **709,000** |
| Current Assets | 2,266,000 | 2,266,000 | 1,096,909 | **2,266,000** |
| Total Assets | 5,494,000 | 5,494,000 | 2,225,217 | **5,494,000** |
| Current Liabilities | 1,379,000 | 1,379,000 | 2,495,884 | **1,379,000** |
| Liabilities | 7,700,000 | 7,699,000* | 5,025,225 | **7,700,000** |
| Total Shareholder Equity | -2,206,000 | -2,206,000 | -2,800,008 | **-2,206,000** |
| TL&SE | 5,494,000 | 5,494,000 | 2,225,217 | **5,494,000** |
| reportDate | 2023-01-28 | (2023-01-31)* | 2023-02-25 | **2023-01-28** |

*Yahoo rounds the fiscal period end to month-end (2023-01-31); actual end is 2023-01-28 per SEC. Liabilities 1K rounding difference.

### Reconciled Values

All values from SEC 10-K, confirmed by Yahoo. Balance sheet identity: 7,700,000 + (-2,206,000) = 5,494,000 ✓

---

## FY2023

**Sources:** SEC 10-K (CIK 701985, FY2023, period ending 2024-02-03) + Yahoo Finance (column 2024-01-31) + Dolt (existing row)

### Anomaly Detection
- `[WARNING]` reportDate discrepancy: Dolt has 2024-01-31 (Yahoo's approximation), SEC shows actual period end 2024-02-03. Correcting.
- All income statement values confirmed: SEC = Yahoo = Dolt ✓
- All balance sheet values confirmed: SEC = Dolt ✓
- Gross margin: 3,236,000 / 7,429,000 = 43.6% — within Specialty benchmark ✓
- Balance sheet identity: 7,090,000 + (-1,627,000) = 5,463,000 ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 7,429,000 | 7,429,000 | 7,429,000 | 7,429,000 |
| Cost of Goods | 4,193,000 | 4,193,000 | 4,193,000 | 4,193,000 |
| Gross Margin | 3,236,000 | 3,236,000 | 3,236,000 | 3,236,000 |
| SGA | 1,951,000 | 1,951,000 | 1,951,000 | 1,951,000 |
| Operating Profit | 1,285,000 | 1,285,000 | 1,285,000 | 1,285,000 |
| Net Profit | 878,000 | 878,000 | 878,000 | 878,000 |
| Inventory | 710,000 | 710,000 | 710,000 | 710,000 |
| Current Assets | 2,115,000 | 2,115,000 | 2,115,000 | 2,115,000 |
| Total Assets | 5,463,000 | 5,463,000 | 5,463,000 | 5,463,000 |
| Current Liabilities | 1,289,000 | 1,289,000 | 1,289,000 | 1,289,000 |
| Liabilities | 7,090,000 | 7,089,000* | 7,090,000 | 7,090,000 |
| Total Shareholder Equity | -1,627,000 | -1,627,000 | -1,627,000 | -1,627,000 |
| TL&SE | 5,463,000 | 5,463,000 | 5,463,000 | 5,463,000 |
| reportDate | **2024-02-03** | (2024-01-31)* | 2024-01-31* | **2024-02-03** |

*1K rounding on Liabilities; Yahoo/Dolt reportDate approximation corrected to SEC actual.

### Reconciled Values

No financial value changes. Only correction: reportDate 2024-01-31 → **2024-02-03**.

---

## FY2024

**Sources:** SEC 10-K (CIK 701985, FY2024, period ending 2025-02-01) + Yahoo Finance (column 2025-01-31) — New insert

### Anomaly Detection
- No Dolt row exists for year 2024.
- All income statement values confirmed: SEC = Yahoo ✓
- All balance sheet values confirmed: SEC = Yahoo ✓
- Gross margin: 3,234,000 / 7,307,000 = 44.3% — within Specialty benchmark ✓
- Negative TSE (-1,385,000K) continues the BBWI pattern ✓
- Balance sheet identity: 6,257,000 + (-1,385,000) = 4,872,000 ✓
- Yahoo approximates reportDate as 2025-01-31; actual is 2025-02-01 per SEC.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 7,307,000 | 7,307,000 | — | **7,307,000** |
| Cost of Goods | 4,073,000 | 4,073,000 | — | **4,073,000** |
| Gross Margin | 3,234,000 | 3,234,000 | — | **3,234,000** |
| SGA | 1,968,000 | 1,968,000 | — | **1,968,000** |
| Operating Profit | 1,266,000 | 1,266,000 | — | **1,266,000** |
| Net Profit | 798,000 | 798,000 | — | **798,000** |
| Inventory | 734,000 | 734,000 | — | **734,000** |
| Current Assets | 1,823,000 | 1,823,000 | — | **1,823,000** |
| Total Assets | 4,872,000 | 4,872,000 | — | **4,872,000** |
| Current Liabilities | 1,231,000 | 1,231,000 | — | **1,231,000** |
| Liabilities | 6,257,000 | 6,255,000* | — | **6,257,000** |
| Total Shareholder Equity | -1,385,000 | -1,385,000 | — | **-1,385,000** |
| TL&SE | 4,872,000 | 4,872,000 | — | **4,872,000** |
| reportDate | 2025-02-01 | (2025-01-31)* | — | **2025-02-01** |

*2K rounding on Liabilities; Yahoo reportDate approximation.

### Reconciled Values

New insert. Balance sheet identity: 6,257,000 + (-1,385,000) = 4,872,000 ✓

---

## FY2025

**Sources:** SEC 10-K (CIK 701985, FY2025, period ending 2026-01-31) + Yahoo Finance (column 2026-01-31) — New insert

### Anomaly Detection
- No Dolt row exists for year 2025.
- All income statement values confirmed: SEC = Yahoo ✓
- All balance sheet values confirmed: SEC = Yahoo ✓
- Gross margin: 3,189,000 / 7,291,000 = 43.7% — within Specialty benchmark ✓
- Negative TSE (-1,281,000K) continues BBWI pattern ✓
- Balance sheet identity: 6,350,000 + (-1,281,000) = 5,069,000 ✓
- SGA increased to 2,063,000K (28.3% of revenue) — higher than prior years (~26%); worth monitoring but within acceptable range.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 7,291,000 | 7,291,000 | — | **7,291,000** |
| Cost of Goods | 4,102,000 | 4,102,000 | — | **4,102,000** |
| Gross Margin | 3,189,000 | 3,189,000 | — | **3,189,000** |
| SGA | 2,063,000 | 2,063,000 | — | **2,063,000** |
| Operating Profit | 1,126,000 | 1,126,000 | — | **1,126,000** |
| Net Profit | 649,000 | 649,000 | — | **649,000** |
| Inventory | 699,000 | 699,000 | — | **699,000** |
| Current Assets | 2,019,000 | 2,019,000 | — | **2,019,000** |
| Total Assets | 5,069,000 | 5,069,000 | — | **5,069,000** |
| Current Liabilities | 1,591,000 | 1,591,000 | — | **1,591,000** |
| Liabilities | 6,350,000 | 6,348,000* | — | **6,350,000** |
| Total Shareholder Equity | -1,281,000 | -1,281,000 | — | **-1,281,000** |
| TL&SE | 5,069,000 | 5,069,000 | — | **5,069,000** |
| reportDate | 2026-01-31 | 2026-01-31 | — | **2026-01-31** |

*2K rounding on Liabilities.

### Reconciled Values

New insert. Balance sheet identity: 6,350,000 + (-1,281,000) = 5,069,000 ✓

---

## Unresolved Issues

1. **company_info CIK must be corrected**: 886158 → 701985 (prerequisite — included in SQL file)
2. **FY2018–FY2020 are L Brands combined** (not BBWI standalone): Revenue/balance sheet for those years includes Victoria's Secret. Revenue drops sharply from $11.8B (FY2020 L Brands) to $7.9B (FY2021 BBWI standalone), which reflects the VS spinoff — not a real revenue decline. Flag for users comparing across years.
3. **FY2021 Net Profit warning**: $258M VS spinoff gain included in 1,333,000K total Net Income. Continuing ops = 1,075,000K. If comparability with FY2022+ is preferred, use 1,075,000K instead.

---

**Analysis complete.** Run `/insert-financials BBWI` to write all changed years (2021–2025) and the CIK fix to the database.
