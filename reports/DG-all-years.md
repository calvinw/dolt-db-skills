# Dollar General (DG) — FY2018–FY2024 Financial Analysis

**Generated:** 2026-06-06
**Source:** /verify-dolt-db-financials skill

---

## Company Info

- **Company:** Dollar General
- **Ticker:** DG
- **CIK:** 29534
- **Display Name:** Dollar General
- **Type:** Discount variety retailer
- **Fiscal Year:** Ends late January / early February

---

## Summary Table

| Year | reportDate   | Gross Margin % | Action         |
|------|-------------|----------------|----------------|
| 2018 | 2019-02-01  | 30.5%          | OK — no changes needed |
| 2019 | 2020-01-31  | 30.6%          | OK — no changes needed |
| 2020 | 2021-01-29  | 31.8%          | OK — no changes needed |
| 2021 | 2022-01-28  | 31.6%          | OK — no changes needed |
| 2022 | 2023-02-03  | 31.2%          | OK — no changes needed |
| 2023 | 2024-02-02  | 30.3%          | OK — no changes needed |
| 2024 | 2025-01-31  | 29.6%          | [WARNING] GM% slightly below 30% threshold — values confirmed correct |

---

## Notes on Data Sources

- **SEC:** All 7 years have clean single-line `SellingGeneralAndAdministrativeExpense` — no composite SGA issue. No MarketingExpense separate line.
- **Yahoo Finance:** Available for FY2022, FY2023, FY2024 only (Yahoo reports 4 years: 2022–2025, but 2025 is out of scope for this verification run). For FY2018–FY2021, only SEC and Dolt are compared.
- **SGA Rule 1 check:** No separate MarketingExpense tag found in any year — single SGA line used throughout.
- **Balance sheet:** All years balance (Total Assets = Total Liabilities + SE) to within $0.
- **Restatement check:** Most recent SEC filing figures match Dolt for all years.

---

## FY2018 — Detailed Analysis

**reportDate:** 2019-02-01  
**Fiscal year end from SEC income statement header:** 2019-02-01

### SGA Anomaly Check
- Single `SellingGeneralAndAdministrativeExpense` line: $5,687,564K — no separate marketing expense. Clean.

### Balance Sheet Check
- Total Assets: $13,204,038K
- Total SE: $6,417,393K
- Liabilities (derived): $6,786,645K
- TL&SE: $13,204,038K
- [OK] Balance sheet balances exactly.

### Gross Margin Check
- Net Revenue: $25,625,043K
- COGS: $17,821,173K
- Gross Margin: $7,803,870K = **30.5%** — within expected 30–35% range. [OK]

### Side-by-Side Comparison

| Field                        | SEC           | Yahoo  | Dolt (current) | Recommended    |
|------------------------------|---------------|--------|----------------|----------------|
| reportDate                   | 2019-02-01    | N/A    | 2019-02-01     | 2019-02-01     |
| Net Revenue                  | 25,625,043    | N/A    | 25,625,043     | 25,625,043     |
| Cost of Goods                | 17,821,173    | N/A    | 17,821,173     | 17,821,173     |
| Gross Margin                 | 7,803,870     | N/A    | 7,803,870      | 7,803,870      |
| SGA                          | 5,687,564     | N/A    | 5,687,564      | 5,687,564      |
| Operating Profit             | 2,116,306     | N/A    | 2,116,306      | 2,116,306      |
| Net Profit                   | 1,589,472     | N/A    | 1,589,472      | 1,589,472      |
| Inventory                    | 4,097,004     | N/A    | 4,097,004      | 4,097,004      |
| Current Assets               | 4,663,020     | N/A    | 4,663,020      | 4,663,020      |
| Total Assets                 | 13,204,038    | N/A    | 13,204,038     | 13,204,038     |
| Current Liabilities          | 3,015,857     | N/A    | 3,015,857      | 3,015,857      |
| Liabilities                  | 6,786,645     | N/A    | 6,786,645      | 6,786,645      |
| Total Shareholder Equity     | 6,417,393     | N/A    | 6,417,393      | 6,417,393      |
| Total Liabilities and SE     | 13,204,038    | N/A    | 13,204,038     | 13,204,038     |

### Reconciliation
All fields match exactly between SEC and Dolt. No changes needed.

**Verdict: NO UPDATE REQUIRED**

---

## FY2019 — Detailed Analysis

**reportDate:** 2020-01-31  
**Fiscal year end from SEC income statement header:** 2020-01-31

### SGA Anomaly Check
- Single `SellingGeneralAndAdministrativeExpense` line: $6,186,757K — no separate marketing expense. Clean.

### Balance Sheet Check
- Total Assets: $22,825,084K
- Total SE: $6,702,500K
- Liabilities (derived): $16,122,584K
- TL&SE: $22,825,084K
- [OK] Balance sheet balances exactly.
- NOTE: Large jump in Total Assets from $13.2B (2018) to $22.8B (2019) due to adoption of ASC 842 (operating lease right-of-use assets added to balance sheet). This is expected and correct.

### Gross Margin Check
- Net Revenue: $27,753,973K
- COGS: $19,264,912K
- Gross Margin: $8,489,061K = **30.6%** — within expected 30–35% range. [OK]

### Side-by-Side Comparison

| Field                        | SEC           | Yahoo  | Dolt (current) | Recommended    |
|------------------------------|---------------|--------|----------------|----------------|
| reportDate                   | 2020-01-31    | N/A    | 2020-01-31     | 2020-01-31     |
| Net Revenue                  | 27,753,973    | N/A    | 27,753,973     | 27,753,973     |
| Cost of Goods                | 19,264,912    | N/A    | 19,264,912     | 19,264,912     |
| Gross Margin                 | 8,489,061     | N/A    | 8,489,061      | 8,489,061      |
| SGA                          | 6,186,757     | N/A    | 6,186,757      | 6,186,757      |
| Operating Profit             | 2,302,304     | N/A    | 2,302,304      | 2,302,304      |
| Net Profit                   | 1,712,555     | N/A    | 1,712,555      | 1,712,555      |
| Inventory                    | 4,676,848     | N/A    | 4,676,848      | 4,676,848      |
| Current Assets               | 5,177,868     | N/A    | 5,177,868      | 5,177,868      |
| Total Assets                 | 22,825,084    | N/A    | 22,825,084     | 22,825,084     |
| Current Liabilities          | 4,543,560     | N/A    | 4,543,560      | 4,543,560      |
| Liabilities                  | 16,122,584    | N/A    | 16,122,584     | 16,122,584     |
| Total Shareholder Equity     | 6,702,500     | N/A    | 6,702,500      | 6,702,500      |
| Total Liabilities and SE     | 22,825,084    | N/A    | 22,825,084     | 22,825,084     |

### Reconciliation
All fields match exactly between SEC and Dolt. No changes needed.

**Verdict: NO UPDATE REQUIRED**

---

## FY2020 — Detailed Analysis

**reportDate:** 2021-01-29  
**Fiscal year end from SEC income statement header:** 2021-01-29

### SGA Anomaly Check
- Single `SellingGeneralAndAdministrativeExpense` line: $7,164,097K — no separate marketing expense. Clean.

### Balance Sheet Check
- Total Assets: $25,862,624K
- Total SE: $6,661,238K
- Liabilities (derived): $19,201,386K
- TL&SE: $25,862,624K
- [OK] Balance sheet balances exactly.

### Gross Margin Check
- Net Revenue: $33,746,839K
- COGS: $23,027,977K
- Gross Margin: $10,718,862K = **31.8%** — within expected 30–35% range. [OK]
- NOTE: Revenue jumped significantly from $27.8B (2019) to $33.7B (2020) — COVID-19 pandemic boost for essential/discount retailers is expected.

### Side-by-Side Comparison

| Field                        | SEC           | Yahoo  | Dolt (current) | Recommended    |
|------------------------------|---------------|--------|----------------|----------------|
| reportDate                   | 2021-01-29    | N/A    | 2021-01-29     | 2021-01-29     |
| Net Revenue                  | 33,746,839    | N/A    | 33,746,839     | 33,746,839     |
| Cost of Goods                | 23,027,977    | N/A    | 23,027,977     | 23,027,977     |
| Gross Margin                 | 10,718,862    | N/A    | 10,718,862     | 10,718,862     |
| SGA                          | 7,164,097     | N/A    | 7,164,097      | 7,164,097      |
| Operating Profit             | 3,554,765     | N/A    | 3,554,765      | 3,554,765      |
| Net Profit                   | 2,655,050     | N/A    | 2,655,050      | 2,655,050      |
| Inventory                    | 5,247,477     | N/A    | 5,247,477      | 5,247,477      |
| Current Assets               | 6,914,219     | N/A    | 6,914,219      | 6,914,219      |
| Total Assets                 | 25,862,624    | N/A    | 25,862,624     | 25,862,624     |
| Current Liabilities          | 5,710,783     | N/A    | 5,710,783      | 5,710,783      |
| Liabilities                  | 19,201,386    | N/A    | 19,201,386     | 19,201,386     |
| Total Shareholder Equity     | 6,661,238     | N/A    | 6,661,238      | 6,661,238      |
| Total Liabilities and SE     | 25,862,624    | N/A    | 25,862,624     | 25,862,624     |

### Reconciliation
All fields match exactly between SEC and Dolt. No changes needed.

**Verdict: NO UPDATE REQUIRED**

---

## FY2021 — Detailed Analysis

**reportDate:** 2022-01-28  
**Fiscal year end from SEC income statement header:** 2022-01-28

### SGA Anomaly Check
- Single `SellingGeneralAndAdministrativeExpense` line: $7,592,331K — no separate marketing expense. Clean.

### Balance Sheet Check
- Total Assets: $26,327,371K
- Total SE: $6,261,986K
- Liabilities (derived): $20,065,385K
- TL&SE: $26,327,371K
- [OK] Balance sheet balances exactly.

### Gross Margin Check
- Net Revenue: $34,220,449K
- COGS: $23,407,443K
- Gross Margin: $10,813,006K = **31.6%** — within expected 30–35% range. [OK]

### Side-by-Side Comparison

| Field                        | SEC           | Yahoo  | Dolt (current) | Recommended    |
|------------------------------|---------------|--------|----------------|----------------|
| reportDate                   | 2022-01-28    | N/A    | 2022-01-28     | 2022-01-28     |
| Net Revenue                  | 34,220,449    | N/A    | 34,220,449     | 34,220,449     |
| Cost of Goods                | 23,407,443    | N/A    | 23,407,443     | 23,407,443     |
| Gross Margin                 | 10,813,006    | N/A    | 10,813,006     | 10,813,006     |
| SGA                          | 7,592,331     | N/A    | 7,592,331      | 7,592,331      |
| Operating Profit             | 3,220,675     | N/A    | 3,220,675      | 3,220,675      |
| Net Profit                   | 2,399,232     | N/A    | 2,399,232      | 2,399,232      |
| Inventory                    | 5,614,325     | N/A    | 5,614,325      | 5,614,325      |
| Current Assets               | 6,303,843     | N/A    | 6,303,843      | 6,303,843      |
| Total Assets                 | 26,327,371    | N/A    | 26,327,371     | 26,327,371     |
| Current Liabilities          | 5,979,357     | N/A    | 5,979,357      | 5,979,357      |
| Liabilities                  | 20,065,385    | N/A    | 20,065,385     | 20,065,385     |
| Total Shareholder Equity     | 6,261,986     | N/A    | 6,261,986      | 6,261,986      |
| Total Liabilities and SE     | 26,327,371    | N/A    | 26,327,371     | 26,327,371     |

### Reconciliation
All fields match exactly between SEC and Dolt. No changes needed.

**Verdict: NO UPDATE REQUIRED**

---

## FY2022 — Detailed Analysis

**reportDate:** 2023-02-03  
**Fiscal year end from SEC income statement header:** 2023-02-03

### SGA Anomaly Check
- Single `SellingGeneralAndAdministrativeExpense` line: $8,491,796K — no separate marketing expense. Clean.
- Yahoo SGA: $8,491,800K (rounding difference of $4K — no issue).
- Yahoo SGA vs Total Operating Expenses check: Yahoo Total Expenses = ~$34,516,600K vs SGA = $8,491,800K — SGA is NOT close to total operating expenses. [OK — Rule 3 passes]

### Balance Sheet Check
- Total Assets: $29,083,367K
- Total SE: $5,541,772K
- Liabilities (derived): $23,541,595K
- TL&SE: $29,083,367K
- [OK] Balance sheet balances exactly.

### Gross Margin Check
- Net Revenue: $37,844,863K
- COGS: $26,024,765K
- Gross Margin: $11,820,098K = **31.2%** — within expected 30–35% range. [OK]

### Side-by-Side Comparison

| Field                        | SEC           | Yahoo         | Dolt (current) | Match? | Recommended    |
|------------------------------|---------------|---------------|----------------|--------|----------------|
| reportDate                   | 2023-02-03    | 2023-01-31*   | 2023-02-03     | ~      | 2023-02-03     |
| Net Revenue                  | 37,844,863    | 37,844,900    | 37,844,863     | ~      | 37,844,863     |
| Cost of Goods                | 26,024,765    | 26,024,800    | 26,024,765     | ~      | 26,024,765     |
| Gross Margin                 | 11,820,098    | 11,820,100    | 11,820,098     | ~      | 11,820,098     |
| SGA                          | 8,491,796     | 8,491,800     | 8,491,796      | ~      | 8,491,796      |
| Operating Profit             | 3,328,302     | 3,328,300     | 3,328,302      | ~      | 3,328,302      |
| Net Profit                   | 2,415,989     | 2,415,990     | 2,415,989      | ~      | 2,415,989      |
| Inventory                    | 6,760,733     | 6,760,730     | 6,760,733      | ~      | 6,760,733      |
| Current Assets               | 7,581,009     | 7,581,010     | 7,581,009      | ~      | 7,581,009      |
| Total Assets                 | 29,083,367    | 29,083,400    | 29,083,367     | ~      | 29,083,367     |
| Current Liabilities          | 5,887,768     | 5,887,770     | 5,887,768      | ~      | 5,887,768      |
| Liabilities                  | 23,541,595    | 23,541,630    | 23,541,595     | ~      | 23,541,595     |
| Total Shareholder Equity     | 5,541,772     | 5,541,770     | 5,541,772      | ~      | 5,541,772      |
| Total Liabilities and SE     | 29,083,367    | 29,083,370    | 29,083,367     | ~      | 29,083,367     |

Note: Yahoo date shown as 2023-01-31 in column header (Yahoo uses calendar year-end approximation); actual SEC fiscal year end is 2023-02-03. All value differences are pure rounding ($4K max). SEC/Dolt values used as authoritative.

### Reconciliation
All fields match between SEC and Dolt. Yahoo minor rounding only. No changes needed.

**Verdict: NO UPDATE REQUIRED**

---

## FY2023 — Detailed Analysis

**reportDate:** 2024-02-02  
**Fiscal year end from SEC income statement header:** 2024-02-02

### SGA Anomaly Check
- Single `SellingGeneralAndAdministrativeExpense` line: $9,272,724K — no separate marketing expense. Clean.
- Yahoo SGA: $9,272,724K — exact match. [OK]
- Yahoo SGA vs Total Operating Expenses: Yahoo Total Expenses = ~$36,245,300K vs SGA = $9,272,724K — SGA is NOT close to total operating expenses. [OK — Rule 3 passes]

### Balance Sheet Check
- Total Assets: $30,795,591K
- Total SE: $6,749,119K
- Liabilities (derived): $24,046,472K
- TL&SE: $30,795,591K
- [OK] Balance sheet balances exactly.

### Gross Margin Check
- Net Revenue: $38,691,609K
- COGS: $26,972,585K
- Gross Margin: $11,719,024K = **30.3%** — within expected 30–35% range. [OK]

### Side-by-Side Comparison

| Field                        | SEC           | Yahoo         | Dolt (current) | Match? | Recommended    |
|------------------------------|---------------|---------------|----------------|--------|----------------|
| reportDate                   | 2024-02-02    | 2024-01-31*   | 2024-02-02     | ~      | 2024-02-02     |
| Net Revenue                  | 38,691,609    | 38,691,609    | 38,691,609     | OK     | 38,691,609     |
| Cost of Goods                | 26,972,585    | 26,972,585    | 26,972,585     | OK     | 26,972,585     |
| Gross Margin                 | 11,719,024    | 11,719,024    | 11,719,024     | OK     | 11,719,024     |
| SGA                          | 9,272,724     | 9,272,724     | 9,272,724      | OK     | 9,272,724      |
| Operating Profit             | 2,446,300     | 2,446,300     | 2,446,300      | OK     | 2,446,300      |
| Net Profit                   | 1,661,274     | 1,661,274     | 1,661,274      | OK     | 1,661,274      |
| Inventory                    | 6,994,266     | 6,994,266     | 6,994,266      | OK     | 6,994,266      |
| Current Assets               | 8,010,724     | 8,010,724     | 8,010,724      | OK     | 8,010,724      |
| Total Assets                 | 30,795,591    | 30,795,591    | 30,795,591     | OK     | 30,795,591     |
| Current Liabilities          | 6,725,701     | 6,725,701     | 6,725,701      | OK     | 6,725,701      |
| Liabilities                  | 24,046,472    | 24,046,472    | 24,046,472     | OK     | 24,046,472     |
| Total Shareholder Equity     | 6,749,119     | 6,749,119     | 6,749,119      | OK     | 6,749,119      |
| Total Liabilities and SE     | 30,795,591    | 30,795,591    | 30,795,591     | OK     | 30,795,591     |

Note: Yahoo date shown as 2024-01-31 (column header approximation); actual SEC fiscal year end is 2024-02-02. All values are exact matches.

### Reconciliation
All fields match exactly across SEC, Yahoo, and Dolt. No changes needed.

**Verdict: NO UPDATE REQUIRED**

---

## FY2024 — Detailed Analysis

**reportDate:** 2025-01-31  
**Fiscal year end from SEC income statement header:** 2025-01-31

### SGA Anomaly Check
- Single `SellingGeneralAndAdministrativeExpense` line: $10,303,423K — no separate marketing expense. Clean.
- Yahoo SGA: $10,303,423K — exact match. [OK]
- Yahoo SGA vs Total Operating Expenses: Yahoo Total Expenses = ~$38,898,200K vs SGA = $10,303,423K — SGA is NOT close to total operating expenses. [OK — Rule 3 passes]

### Balance Sheet Check
- Total Assets: $31,132,733K
- Total SE: $7,413,707K
- Liabilities (derived): $23,719,026K
- TL&SE: $31,132,733K
- [OK] Balance sheet balances exactly.

### Gross Margin Check
- Net Revenue: $40,612,308K
- COGS: $28,594,811K
- Gross Margin: $12,017,497K = **29.6%** — [WARNING] slightly below the 30–35% expected range for a discount retailer. However, this reflects margin compression that Dollar General disclosed publicly (higher markdowns, shrink/theft costs, consumables mix shift). Values are confirmed correct per SEC 10-K.

### Side-by-Side Comparison

| Field                        | SEC           | Yahoo         | Dolt (current) | Match? | Recommended    |
|------------------------------|---------------|---------------|----------------|--------|----------------|
| reportDate                   | 2025-01-31    | 2025-01-31    | 2025-01-31     | OK     | 2025-01-31     |
| Net Revenue                  | 40,612,308    | 40,612,308    | 40,612,308     | OK     | 40,612,308     |
| Cost of Goods                | 28,594,811    | 28,594,811    | 28,594,811     | OK     | 28,594,811     |
| Gross Margin                 | 12,017,497    | 12,017,497    | 12,017,497     | OK     | 12,017,497     |
| SGA                          | 10,303,423    | 10,303,423    | 10,303,423     | OK     | 10,303,423     |
| Operating Profit             | 1,714,074     | 1,714,074     | 1,714,074      | OK     | 1,714,074      |
| Net Profit                   | 1,125,253     | 1,125,253     | 1,125,253      | OK     | 1,125,253      |
| Inventory                    | 6,711,242     | 6,711,242     | 6,711,242      | OK     | 6,711,242      |
| Current Assets               | 8,163,925     | 8,163,925     | 8,163,925      | OK     | 8,163,925      |
| Total Assets                 | 31,132,733    | 31,132,733    | 31,132,733     | OK     | 31,132,733     |
| Current Liabilities          | 6,868,702     | 6,868,702     | 6,868,702      | OK     | 6,868,702      |
| Liabilities                  | 23,719,026    | 23,719,026    | 23,719,026     | OK     | 23,719,026     |
| Total Shareholder Equity     | 7,413,707     | 7,413,707     | 7,413,707      | OK     | 7,413,707      |
| Total Liabilities and SE     | 31,132,733    | 31,132,733    | 31,132,733     | OK     | 31,132,733     |

### Reconciliation
All fields match exactly across SEC, Yahoo, and Dolt. No changes needed.
GM% of 29.6% is confirmed correct — reflects publicly-disclosed margin compression, not a data error.

**Verdict: NO UPDATE REQUIRED**

---

## Overall Reconciliation Summary

| Year | Any Dolt Discrepancy? | Action Required |
|------|-----------------------|-----------------|
| 2018 | No                    | None            |
| 2019 | No                    | None            |
| 2020 | No                    | None            |
| 2021 | No                    | None            |
| 2022 | No                    | None            |
| 2023 | No                    | None            |
| 2024 | No                    | None            |

---

## Unresolved Flags

- [WARNING] FY2024 Gross Margin = 29.6% (slightly below 30% threshold). Values confirmed correct per SEC 10-K — reflects business-level margin compression, not a data error. No corrective action needed.

---

**Analysis complete.** Run `/insert-financials DG` to write all changed years to the database.

No changed years were identified — all Dolt values match SEC filings exactly across all 7 years. No inserts required.
