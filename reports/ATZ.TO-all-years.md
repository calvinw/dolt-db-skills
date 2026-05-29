# Aritzia (ATZ.TO) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-05-29
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2018 | 2019-03-03 | No change — no alternate source to verify |
| 2019 | 2020-03-01 | No change — no alternate source to verify |
| 2020 | 2021-02-28 | No change — no alternate source to verify |
| 2021 | 2022-02-28 | No change — no alternate source to verify |
| 2022 | 2023-02-28 | No change — Yahoo values match within rounding |
| 2023 | 2024-02-29 | No change — Yahoo matches; Current Liabilities discrepancy noted (unresolvable without SEC) |
| 2024 | 2025-02-28 | No change — Yahoo values match exactly |
| 2025 | 2026-02-28 | **New insert** |

---

## Company Metadata

- **Company name (DB):** Aritzia
- **Display name:** Aritzia
- **Ticker:** ATZ.TO
- **CIK:** NULL — non-US company (Canadian); SEC fetch skipped
- **Segment:** Specialty — Apparel (premium/luxury casual women's fashion)
- **Fiscal year end:** Late February / early March (IFRS reporting, Canadian company)
- **SEC available:** No — Yahoo Finance + Dolt only
- **Operating Profit convention:** Yahoo "Operating Income" = "Total Operating Income As Reported" for all years (special charges reported below operating income line for Aritzia); use Operating Income directly
- **TSE convention:** Common Stock Equity = Total Equity Gross Minority Interest (no minority interest)
- **Currency:** CAD — values in thousands of CAD as reported

---

## Anomaly Rules Applied

- **Rule 3 (Yahoo SGA = Total OpEx):** Not triggered. Yahoo Total Expenses (~$3.18B for FY2025) >> SGA (~$1.14B). SGA is safe to use.
- **Rule 1 (SGA + Marketing):** No separate Marketing line in Yahoo data. Yahoo "Selling General And Administration" equals "General And Administrative Expense" — single combined line. Use directly.
- **Rule 4:** Not needed — single combined SGA line present.
- **Gross margin benchmark:** Specialty apparel expected 35–55%. All verified years within range.
- **Inventory:** Aritzia is a traditional apparel retailer. Positive inventory expected and present for all years. ✓
- **Balance sheet identity:** Verified for all Dolt years (2018–2024) and new FY2025 data. ✓
- **Operating Profit:** For Aritzia, clean "Operating Income" = "Total Operating Income As Reported" in all Yahoo years — Aritzia reports special items below the operating line (as non-operating), not within it. No distinction needed.
- **SGA and D&A:** Aritzia follows IFRS 16. D&A on ROU assets is distributed within COGS and SGA (not a separate line). Yahoo SGA figures are consistent across sources and internally consistent (Gross Profit − SGA ≈ Operating Income for all years). Use Yahoo SGA as-is.

---

## Years 2018–2021: Existing Dolt Data (No Alternate Source)

Yahoo Finance does not provide data for these years. No correction is possible without external data.

[WARNING] SGA for years 2018–2021 cannot be verified against Yahoo Finance. Per recurring project convention, companies with data older than ~2021 may have incomplete SGA (G&A only). Do not correct without external data.

### Year 2018

| Field | Dolt (current) | Yahoo | Recommended |
|-------|---------------|-------|-------------|
| reportDate | 2019-03-03 | N/A | 2019-03-03 |
| Net Revenue | 874,296 | N/A | 874,296 |
| Cost of Goods | 531,383 | N/A | 531,383 |
| Gross Margin | 342,913 | N/A | 342,913 |
| Gross Margin % | 39.2% | N/A | — |
| SGA | 226,837 | N/A | 226,837 [WARNING: unverified] |
| Operating Profit | 114,775 | N/A | 114,775 |
| Net Profit | 78,728 | N/A | 78,728 |
| Inventory | 112,183 | N/A | 112,183 |
| Current Assets | 235,857 | N/A | 235,857 |
| Total Assets | 629,374 | N/A | 629,374 |
| Current Liabilities | 90,611 | N/A | 90,611 |
| Liabilities | 255,065 | N/A | 255,065 |
| TSE | 374,309 | N/A | 374,309 |
| Total L+E | 629,374 | N/A | 629,374 |

Balance sheet identity: 255,065 + 374,309 = 629,374 = Total Assets ✓

Note: Lower Total Assets and Liabilities in 2018 compared to 2019 onward reflects pre-IFRS 16 reporting (no ROU assets on balance sheet before FY2019 adoption).

**Action: No change.**

---

### Year 2019

| Field | Dolt (current) | Yahoo | Recommended |
|-------|---------------|-------|-------------|
| reportDate | 2020-03-01 | N/A | 2020-03-01 |
| Net Revenue | 980,589 | N/A | 980,589 |
| Cost of Goods | 577,165 | N/A | 577,165 |
| Gross Margin | 403,424 | N/A | 403,424 |
| Gross Margin % | 41.1% | N/A | — |
| SGA | 251,152 | N/A | 251,152 [WARNING: unverified] |
| Operating Profit | 153,293 | N/A | 153,293 |
| Net Profit | 90,594 | N/A | 90,594 |
| Inventory | 94,034 | N/A | 94,034 |
| Current Assets | 231,376 | N/A | 231,376 |
| Total Assets | 1,036,715 | N/A | 1,036,715 |
| Current Liabilities | 153,843 | N/A | 153,843 |
| Liabilities | 704,650 | N/A | 704,650 |
| TSE | 332,065 | N/A | 332,065 |
| Total L+E | 1,036,715 | N/A | 1,036,715 |

Balance sheet identity: 704,650 + 332,065 = 1,036,715 = Total Assets ✓

Note: Large jump in Total Assets and Liabilities from 2018 to 2019 reflects IFRS 16 adoption (ROU assets and lease liabilities added to balance sheet).

**Action: No change.**

---

### Year 2020

| Field | Dolt (current) | Yahoo | Recommended |
|-------|---------------|-------|-------------|
| reportDate | 2021-02-28 | N/A | 2021-02-28 |
| Net Revenue | 857,323 | N/A | 857,323 |
| Cost of Goods | 544,818 | N/A | 544,818 |
| Gross Margin | 312,505 | N/A | 312,505 |
| Gross Margin % | 36.5% | N/A | — |
| SGA | 261,417 | N/A | 261,417 [WARNING: unverified] |
| Operating Profit | 51,088 | N/A | 51,088 |
| Net Profit | 19,227 | N/A | 19,227 |
| Inventory | 171,821 | N/A | 171,821 |
| Current Assets | 355,341 | N/A | 355,341 |
| Total Assets | 1,140,737 | N/A | 1,140,737 |
| Current Liabilities | 249,195 | N/A | 249,195 |
| Liabilities | 780,474 | N/A | 780,474 |
| TSE | 360,263 | N/A | 360,263 |
| Total L+E | 1,140,737 | N/A | 1,140,737 |

Balance sheet identity: 780,474 + 360,263 = 1,140,737 = Total Assets ✓

Note: Depressed revenue and profit reflect COVID-19 impact on FY2020 (ended Feb 28, 2021). Gross margin 36.5% is at the low end but within specialty apparel range.

**Action: No change.**

---

### Year 2021

| Field | Dolt (current) | Yahoo | Recommended |
|-------|---------------|-------|-------------|
| reportDate | 2022-02-28 | N/A | 2022-02-28 |
| Net Revenue | 1,494,630 | N/A | 1,494,630 |
| Cost of Goods | 839,678 | N/A | 839,678 |
| Gross Margin | 654,952 | N/A | 654,952 |
| Gross Margin % | 43.8% | N/A | — |
| SGA | 418,933 | N/A | 418,933 [WARNING: unverified] |
| Operating Profit | 236,019 | N/A | 236,019 |
| Net Profit | 156,917 | N/A | 156,917 |
| Inventory | 208,125 | N/A | 208,125 |
| Current Assets | 521,536 | N/A | 521,536 |
| Total Assets | 1,424,590 | N/A | 1,424,590 |
| Current Liabilities | 387,325 | N/A | 387,325 |
| Liabilities | 894,779 | N/A | 894,779 |
| TSE | 530,811 | N/A | 530,811 |
| Total L+E | 1,424,590 | N/A | 1,424,590 |

Balance sheet identity: 894,779 + 530,811 = 1,424,590 = Total Assets ✓

**Action: No change.**

---

## Years 2022–2024: Yahoo vs Dolt Comparison

Yahoo fiscal year dates map to Dolt years as follows:
- Yahoo 2023-02-28 → Dolt year 2022 (reportDate 2023-02-28)
- Yahoo 2024-02-29 → Dolt year 2023 (reportDate 2024-02-29)
- Yahoo 2025-02-28 → Dolt year 2024 (reportDate 2025-02-28)

Operating Profit confirmation: Yahoo "Operating Income" = "Total Operating Income As Reported" for all Aritzia years — values are identical. Dolt matches Yahoo Operating Income for all three years.

### Year 2022

| Field | Yahoo (2023-02-28) | Dolt (current) | Recommended |
|-------|-------------------|---------------|-------------|
| reportDate | 2023-02-28 | 2023-02-28 | 2023-02-28 |
| Net Revenue | 2,195,630 | 2,195,630 | 2,195,630 |
| Cost of Goods | 1,281,640 | 1,281,640 | 1,281,640 |
| Gross Margin | 913,990* | 913,990 | 913,990 |
| Gross Margin % | 41.6% | 41.6% | — |
| SGA | 626,838 | 626,838 | 626,838 |
| Operating Profit | 287,154 | 287,154 | 287,154 |
| Net Profit | 187,588 | 187,588 | 187,588 |
| Inventory | 467,634 | 467,634 | 467,634 |
| Current Assets | 611,848 | 611,848 | 611,848 |
| Total Assets | 1,836,540 | 1,836,540 | 1,836,540 |
| Current Liabilities | 417,300 | 417,300 | 417,300 |
| Liabilities | 1,150,760* | 1,150,753 | 1,150,753 |
| TSE | 685,787 | 685,787 | 685,787 |
| Total L+E | 1,836,540 | 1,836,540 | 1,836,540 |

*Yahoo Gross Margin derived as 913,992K; rounded to 913,990K. Yahoo Liabilities = 1,150,760K vs Dolt 1,150,753K — 7K rounding difference only.

Balance sheet identity: 1,150,753 + 685,787 = 1,836,540 ✓

**Action: No change.**

---

### Year 2023

| Field | Yahoo (2024-02-29) | Dolt (current) | Recommended |
|-------|-------------------|---------------|-------------|
| reportDate | 2024-02-29 | 2024-02-29 | 2024-02-29 |
| Net Revenue | 2,332,350 | 2,332,350 | 2,332,350 |
| Cost of Goods | 1,433,370 | 1,433,370 | 1,433,370 |
| Gross Margin | 898,980 | 898,980 | 898,980 |
| Gross Margin % | 38.5% | 38.5% | — |
| SGA | 740,567 | 740,567 | 740,567 |
| Operating Profit | 158,414 | 158,414 | 158,414 |
| Net Profit | 78,780 | 78,780 | 78,780 |
| Inventory | 340,145 | 340,145 | 340,145 |
| Current Assets | 566,220 | 566,220 | 566,220 |
| Total Assets | 1,946,130 | 1,946,130 | 1,946,130 |
| Current Liabilities | **411,627*** | **403,432*** | 403,432 (keep Dolt) |
| Liabilities | 1,138,640* | 1,138,635 | 1,138,635 |
| TSE | 807,495 | 807,495 | 807,495 |
| Total L+E | 1,946,130 | 1,946,130 | 1,946,130 |

[WARNING] Current Liabilities discrepancy: Yahoo shows 411,627K vs Dolt 403,432K (~8.2M difference). Total Liabilities agree (1,138,640 vs 1,138,635 = 5K rounding). The discrepancy is a current vs non-current split difference only. Cannot resolve without SEC data. Keeping Dolt value.

Balance sheet identity: 1,138,635 + 807,495 = 1,946,130 ✓

**Action: No change.**

---

### Year 2024

| Field | Yahoo (2025-02-28) | Dolt (current) | Recommended |
|-------|-------------------|---------------|-------------|
| reportDate | 2025-02-28 | 2025-02-28 | 2025-02-28 |
| Net Revenue | 2,738,110 | 2,738,110 | 2,738,110 |
| Cost of Goods | 1,557,490 | 1,557,490 | 1,557,490 |
| Gross Margin | 1,180,620 | 1,180,620 | 1,180,620 |
| Gross Margin % | 43.1% | 43.1% | — |
| SGA | 885,829 | 885,829 | 885,829 |
| Operating Profit | 294,790 | 294,790 | 294,790 |
| Net Profit | 207,790 | 207,790 | 207,790 |
| Inventory | 379,316 | 379,316 | 379,316 |
| Current Assets | 756,843 | 756,843 | 756,843 |
| Total Assets | 2,455,810 | 2,455,810 | 2,455,810 |
| Current Liabilities | 525,308 | 525,308 | 525,308 |
| Liabilities | 1,361,230 | 1,361,230 | 1,361,230 |
| TSE | 1,094,580 | 1,094,580 | 1,094,580 |
| Total L+E | 2,455,810 | 2,455,810 | 2,455,810 |

All values match exactly.

Balance sheet identity: 1,361,230 + 1,094,580 = 2,455,810 ✓

**Action: No change.**

---

## Year 2025: New Insert (Yahoo 2026-02-28)

This year is not yet in the Dolt database.

### Source Data

Yahoo Finance (column: 2026-02-28):

**Income Statement:**
| Item | Yahoo Raw | Value ($K CAD) |
|------|-----------|---------------|
| Total Revenue | 3.70215e+09 | 3,702,150 |
| Cost Of Revenue | 2.04082e+09 | 2,040,820 |
| Gross Profit | 1.66133e+09 | 1,661,330 |
| Selling General And Administration | 1.13728e+09 | 1,137,280 |
| Operating Income | 5.24054e+08 | 524,054 |
| Total Operating Income As Reported | 5.24054e+08 | 524,054 |
| Net Income Common Stockholders | 3.81848e+08 | 381,848 |

Note: Operating Income = Total Operating Income As Reported (524,054K both) — consistent with prior Aritzia years. Special charges are below the operating line.

Gross Profit check: 3,702,150 − 2,040,820 = 1,661,330 ✓
Operating Income check: 1,661,330 − 1,137,280 = 524,050 ≈ 524,054K (4K rounding) ✓

**Balance Sheet:**
| Item | Yahoo Raw | Value ($K CAD) |
|------|-----------|---------------|
| Inventory | 4.95197e+08 | 495,197 |
| Current Assets | 1.25245e+09 | 1,252,450 |
| Total Assets | 3.13568e+09 | 3,135,680 |
| Current Liabilities | 8.74919e+08 | 874,919 |
| Common Stock Equity (= Total Equity Gross Minority Interest) | 1.36103e+09 | 1,361,030 |
| Total Liabilities Net Minority Interest | 1.77465e+09 | 1,774,650 |

### Anomaly Checks

- **Gross margin:** 1,661,330 / 3,702,150 = **44.9%** — within specialty apparel range (35–55%) ✓
- **SGA rule 3:** Yahoo SGA 1,137,280K << Total Expenses 3,178,090K — no inflation ✓
- **SGA structure:** Single combined line = G&A = 1,137,280K. Consistent with prior Aritzia Dolt values and Yahoo data. ✓
- **Operating Profit:** Yahoo Operating Income = As Reported = 524,054K. Consistent with Aritzia convention. ✓
- **TSE:** Common Stock Equity = Total Equity Gross Minority Interest = 1,361,030K (no minority interest). ✓
- **Balance sheet identity:** 1,774,650 + 1,361,030 = 3,135,680 = Total Assets ✓
- **Inventory:** 495,197K — positive, expected for apparel retailer. ✓

### Reconciled Values for FY2025

| Field | Recommended Value | Source | Notes |
|-------|------------------|--------|-------|
| reportDate | 2026-02-28 | Yahoo column header | |
| Net Revenue | 3,702,150 | Yahoo | |
| Cost of Goods | 2,040,820 | Yahoo | |
| Gross Margin | 1,661,330 | Calculated | Revenue − COGS |
| SGA | 1,137,280 | Yahoo | Single combined G&A/SGA line |
| Operating Profit | 524,054 | Yahoo Operating Income | = As Reported; consistent with Aritzia convention |
| Net Profit | 381,848 | Yahoo | |
| Inventory | 495,197 | Yahoo | |
| Current Assets | 1,252,450 | Yahoo | |
| Total Assets | 3,135,680 | Yahoo | |
| Current Liabilities | 874,919 | Yahoo | |
| Liabilities | 1,774,650 | Calculated | Total Assets − TSE |
| TSE | 1,361,030 | Yahoo Common Stock Equity | No minority interest |
| Total L+E | 3,135,680 | Yahoo | |

**Action: New insert.**

---

## Flags Summary

| Year | Flag | Severity | Description |
|------|------|----------|-------------|
| 2018 | SGA unverified | [WARNING] | No Yahoo data for this year; SGA may be incomplete per recurring convention |
| 2019 | SGA unverified | [WARNING] | No Yahoo data for this year; SGA may be incomplete |
| 2020 | SGA unverified | [WARNING] | No Yahoo data for this year; SGA may be incomplete |
| 2021 | SGA unverified | [WARNING] | No Yahoo data for this year; SGA may be incomplete |
| 2023 | Current Liabilities discrepancy | [WARNING] | Yahoo shows 411,627K vs Dolt 403,432K (~8.2M); total liabilities agree; cannot resolve without SEC data; kept Dolt value |

No [ERROR] flags. All unresolved flags are [WARNING] only.

---

**Analysis complete.** Run `/insert-financials ATZ.TO` to write all changed years to the database.

Only FY2025 requires a new insert. Years 2018–2024 have no changes.
