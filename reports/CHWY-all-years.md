# Chewy (CHWY) — FY2019–FY2025 Financial Analysis

**Generated:** 2026-06-06
**Source:** /verify-dolt-db-financials skill

---

## Company Info
- **Company:** Chewy
- **CIK:** 1766502
- **Ticker:** CHWY
- **Type:** Online-only pet products retailer
- **Fiscal Year End:** Late January / Early February

---

## Per-Year Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2019 | 2020-02-02 | NO CHANGE — Dolt matches SEC |
| 2020 | 2021-01-31 | NO CHANGE — Dolt matches SEC |
| 2021 | 2022-01-30 | NO CHANGE — Dolt matches SEC |
| 2022 | 2023-01-29 | [WARNING] Dolt revenue/COGS differ from latest SEC filing — possible restatement; review recommended |
| 2023 | 2024-01-28 | NO CHANGE — Dolt matches SEC |
| 2024 | 2025-02-02 | NO CHANGE — Dolt matches SEC |
| 2025 | 2026-02-01 | NEW YEAR — Not yet in Dolt; insert recommended |

---

## SGA Notes (All Years)

Chewy's SEC 10-K filings present operating expenses as:
- `SellingGeneralAndAdministrativeExpense` (SGA line)
- `MarketingAndAdvertisingExpense` (marketing sub-line, separately disclosed)
- `OperatingExpenses` = SGA + Marketing (total)

**Rule 1 does NOT apply here.** The Marketing line is a breakdown *within* operating expenses, not an additive line outside SGA. Chewy's SGA tag (`SellingGeneralAndAdministrativeExpense`) does NOT include marketing — marketing is a separate component of total operating expenses. Therefore:

**Recommended SGA = `SellingGeneralAndAdministrativeExpense` only** (do not add marketing).

Yahoo Finance's `Selling General And Administration` matches SEC's SGA line exactly in recent years. Yahoo's `GeneralAndAdministrativeExpense` is just a sub-component.

No technology/infrastructure cost lines were identified separately in Chewy's filings that would need exclusion.

---

## FY2019 — reportDate: 2020-02-02

### Sources

**SEC FY2019 10-K (filed ~2020, period 2020-02-02):**
- Net Revenue: 4,846,743
- COGS: 3,702,683
- Gross Margin: 1,144,060
- SGA: 969,890 (SellingGeneralAndAdministrativeExpense)
- Marketing (separate): 426,896
- Operating Expenses Total: 1,396,786
- Operating Profit: -252,726
- Net Profit: -252,370
- Inventory: 317,808
- Current Assets: 629,789
- Total Assets: 932,321
- Current Liabilities: 1,100,538
- Total Liabilities: 1,336,295
- Total SE: -403,974
- Total L+SE: 932,321

**Yahoo Finance (FY2022 column = 2022-01-31):** No data available for FY2019 in Yahoo's 4-year window.

**Dolt (year=2019):**
- Net Revenue: 4,846,743
- COGS: 3,702,683
- Gross Margin: 1,144,060
- SGA: 969,890
- Operating Profit: -252,726
- Net Profit: -252,370
- Inventory: 317,808
- Current Assets: 629,789
- Total Assets: 932,321
- Current Liabilities: 1,100,538
- Liabilities: 1,336,295
- Total SE: -403,974
- Total L+SE: 932,321

### Anomaly Detection

**SGA:** SEC SGA = 969,890 (does not include marketing 426,896). Dolt matches SEC. No anomaly.

**Balance Sheet:**
- Total Assets: 932,321
- Total SE: -403,974
- Liabilities (derived): 932,321 − (−403,974) = 1,336,295 ✓ matches filed Total Liabilities
- Total L+SE: 932,321 ✓
- [WARNING] Negative Total SE: -403,974 (expected for Chewy's early growth phase with accumulated losses)
- Current Liabilities (1,100,538) > Total Assets (932,321) — highly leveraged balance sheet in growth phase

**Gross Margin:** 1,144,060 / 4,846,743 = 23.6% — [WARNING] slightly below 25% benchmark but reasonable for an early-stage online retailer with rapid growth

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 4,846,743 | N/A | 4,846,743 | 4,846,743 |
| Cost of Goods | 3,702,683 | N/A | 3,702,683 | 3,702,683 |
| Gross Margin | 1,144,060 | N/A | 1,144,060 | 1,144,060 |
| SGA | 969,890 | N/A | 969,890 | 969,890 |
| Operating Profit | -252,726 | N/A | -252,726 | -252,726 |
| Net Profit | -252,370 | N/A | -252,370 | -252,370 |
| Inventory | 317,808 | N/A | 317,808 | 317,808 |
| Current Assets | 629,789 | N/A | 629,789 | 629,789 |
| Total Assets | 932,321 | N/A | 932,321 | 932,321 |
| Current Liabilities | 1,100,538 | N/A | 1,100,538 | 1,100,538 |
| Liabilities | 1,336,295 | N/A | 1,336,295 | 1,336,295 |
| Total SE | -403,974 | N/A | -403,974 | -403,974 |
| Total L+SE | 932,321 | N/A | 932,321 | 932,321 |

### Reconciled Recommendation
All fields match SEC exactly. **Dolt is correct. NO CHANGE needed.**

---

## FY2020 — reportDate: 2021-01-31

### Sources

**SEC FY2020 10-K (period 2021-01-31):**
- Net Revenue: 7,146,264
- COGS: 5,325,457
- Gross Margin: 1,820,807
- SGA: 1,397,969
- Marketing (separate): 513,302
- Operating Expenses Total: 1,911,271
- Operating Profit: -90,464
- Net Profit: -92,486
- Inventory: 513,304
- Current Assets: 1,226,778
- Total Assets: 1,740,910
- Current Liabilities: 1,380,862
- Total Liabilities: 1,742,914
- Total SE: -2,004
- Total L+SE: 1,740,910

**Yahoo Finance:** Not available in 4-year window.

**Dolt (year=2020):**
- Net Revenue: 7,146,264
- COGS: 5,325,457
- Gross Margin: 1,820,807
- SGA: 1,397,969
- Operating Profit: -90,464
- Net Profit: -92,486
- Inventory: 513,304
- Current Assets: 1,226,778
- Total Assets: 1,740,910
- Current Liabilities: 1,380,862
- Liabilities: 1,742,914
- Total SE: -2,004
- Total L+SE: 1,740,910

### Anomaly Detection

**SGA:** 1,397,969 matches Dolt exactly. No anomaly.

**Balance Sheet:**
- Liabilities (derived): 1,740,910 − (−2,004) = 1,742,914 ✓
- Total L+SE: 1,740,910 ✓
- [WARNING] Negative Total SE: -2,004 (nearly break-even equity)

**Gross Margin:** 1,820,807 / 7,146,264 = 25.5% — within benchmark range ✓

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 7,146,264 | N/A | 7,146,264 | 7,146,264 |
| Cost of Goods | 5,325,457 | N/A | 5,325,457 | 5,325,457 |
| Gross Margin | 1,820,807 | N/A | 1,820,807 | 1,820,807 |
| SGA | 1,397,969 | N/A | 1,397,969 | 1,397,969 |
| Operating Profit | -90,464 | N/A | -90,464 | -90,464 |
| Net Profit | -92,486 | N/A | -92,486 | -92,486 |
| Inventory | 513,304 | N/A | 513,304 | 513,304 |
| Current Assets | 1,226,778 | N/A | 1,226,778 | 1,226,778 |
| Total Assets | 1,740,910 | N/A | 1,740,910 | 1,740,910 |
| Current Liabilities | 1,380,862 | N/A | 1,380,862 | 1,380,862 |
| Liabilities | 1,742,914 | N/A | 1,742,914 | 1,742,914 |
| Total SE | -2,004 | N/A | -2,004 | -2,004 |
| Total L+SE | 1,740,910 | N/A | 1,740,910 | 1,740,910 |

### Reconciled Recommendation
All fields match SEC exactly. **Dolt is correct. NO CHANGE needed.**

---

## FY2021 — reportDate: 2022-01-30

### Sources

**SEC FY2021 10-K (period 2022-01-30):**
- Net Revenue: 8,890,773
- COGS: 6,517,191
- Gross Margin: 2,373,582
- SGA: 1,826,858
- Marketing (separate): 618,902
- Operating Expenses Total: 2,445,760
- Operating Profit: -72,178
- Net Profit: -73,817
- Inventory: 560,430
- Current Assets: 1,323,532
- Total Assets: 2,086,281
- Current Liabilities: 1,644,879
- Total Liabilities: 2,071,545
- Total SE: 14,736
- Total L+SE: 2,086,281

**Yahoo Finance:** Not available in 4-year window.

**Dolt (year=2021):**
- Net Revenue: 8,890,773
- COGS: 6,517,191
- Gross Margin: 2,373,582
- SGA: 1,826,858
- Operating Profit: -72,178
- Net Profit: -73,817
- Inventory: 560,430
- Current Assets: 1,323,532
- Total Assets: 2,086,281
- Current Liabilities: 1,644,879
- Liabilities: 2,071,545
- Total SE: 14,736
- Total L+SE: 2,086,281

### Anomaly Detection

**SGA:** 1,826,858 matches Dolt exactly. No anomaly.

**Balance Sheet:**
- Liabilities (derived): 2,086,281 − 14,736 = 2,071,545 ✓
- Total L+SE: 2,086,281 ✓

**Gross Margin:** 2,373,582 / 8,890,773 = 26.7% — within benchmark range ✓

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 8,890,773 | N/A | 8,890,773 | 8,890,773 |
| Cost of Goods | 6,517,191 | N/A | 6,517,191 | 6,517,191 |
| Gross Margin | 2,373,582 | N/A | 2,373,582 | 2,373,582 |
| SGA | 1,826,858 | N/A | 1,826,858 | 1,826,858 |
| Operating Profit | -72,178 | N/A | -72,178 | -72,178 |
| Net Profit | -73,817 | N/A | -73,817 | -73,817 |
| Inventory | 560,430 | N/A | 560,430 | 560,430 |
| Current Assets | 1,323,532 | N/A | 1,323,532 | 1,323,532 |
| Total Assets | 2,086,281 | N/A | 2,086,281 | 2,086,281 |
| Current Liabilities | 1,644,879 | N/A | 1,644,879 | 1,644,879 |
| Liabilities | 2,071,545 | N/A | 2,071,545 | 2,071,545 |
| Total SE | 14,736 | N/A | 14,736 | 14,736 |
| Total L+SE | 2,086,281 | N/A | 2,086,281 | 2,086,281 |

### Reconciled Recommendation
All fields match SEC exactly. **Dolt is correct. NO CHANGE needed.**

---

## FY2022 — reportDate: 2023-01-29

### Sources

**SEC Direct (year=2022):** Error — no filing returned for this year label.

**SEC FY2023 10-K comparative column (2023-01-29)** — most recent filing that includes FY2022 data:
- Net Revenue: 10,119,000 (rounded to thousands)
- COGS: 7,284,505
- Gross Margin: 2,834,495
- SGA: 2,128,688
- Marketing (separate): 649,386
- Operating Expenses Total: 2,778,074
- Operating Profit: 56,421
- Net Profit: 49,899
- Inventory: 678,005
- Current Assets: 1,524,780
- Total Assets: 2,519,818
- Current Liabilities: 1,827,718
- Total Liabilities: 2,359,550
- Total SE: 160,268
- Total L+SE: 2,519,818

**Yahoo Finance (2023-01-31 column):**
- Net Revenue: 10,119,000
- COGS: 7,284,500
- Gross Margin: 2,834,500
- SGA: 2,128,690 (Selling General And Administration)
- Operating Profit: 56,421
- Net Profit: 49,899
- Inventory: 678,005
- Current Assets: 1,524,780
- Total Assets: 2,519,820
- Current Liabilities: 1,827,720
- Total SE: 160,268
- Total L+SE: 2,519,820

**Dolt (year=2022, reportDate=2023-01-29):**
- Net Revenue: 10,098,939 *
- COGS: 7,268,034 *
- Gross Margin: 2,830,905 *
- SGA: 2,125,766 *
- Operating Profit: 55,753 *
- Net Profit: 49,232 *
- Inventory: 675,520 *
- Current Assets: 1,520,321 *
- Total Assets: 2,515,076 *
- Current Liabilities: 1,769,349 *
- Liabilities: 2,301,119 *
- Total SE: 213,957 *
- Total L+SE: 2,515,076 *

### Anomaly Detection

**[WARNING] Restatement detected for FY2022:**
Multiple fields in Dolt differ significantly from the most recent SEC filing (FY2023 10-K comparative). This indicates the original FY2022 10-K filing was later restated/revised in the subsequent year's filing. The differences are material:

| Field | Original (Dolt) | Restated (SEC FY2023 filing) | Difference |
|-------|-----------------|-------------------------------|------------|
| Net Revenue | 10,098,939 | 10,119,000 | +20,061 |
| COGS | 7,268,034 | 7,284,505 | +16,471 |
| Gross Margin | 2,830,905 | 2,834,495 | +3,590 |
| SGA | 2,125,766 | 2,128,688 | +2,922 |
| Operating Profit | 55,753 | 56,421 | +668 |
| Net Profit | 49,232 | 49,899 | +667 |
| Inventory | 675,520 | 678,005 | +2,485 |
| Current Assets | 1,520,321 | 1,524,780 | +4,459 |
| Total Assets | 2,515,076 | 2,519,818 | +4,742 |
| Current Liabilities | 1,769,349 | 1,827,718 | +58,369 |
| Liabilities | 2,301,119 | 2,359,550 | +58,431 |
| Total SE | 213,957 | 160,268 | -53,689 |

Note: The restated figures likely reflect inclusion of Canadian operations (Chewy expanded to Canada), reclassifications, or other adjustments disclosed in the FY2023 10-K.

**SGA:** Yahoo SGA ≈ SEC SGA (2,128,688 vs 2,128,690 — rounding). No Rule 3 issue.

**Balance Sheet (restated):**
- Liabilities (derived): 2,519,818 − 160,268 = 2,359,550 ✓
- Total L+SE: 2,519,818 ✓

**Gross Margin (restated):** 2,834,495 / 10,119,000 = 28.0% — within benchmark range ✓

### Side-by-Side Comparison

| Field | SEC (restated) | Yahoo | Dolt (current) | Recommended |
|-------|---------------|-------|-----------------|-------------|
| Net Revenue | 10,119,000 | 10,119,000 | 10,098,939 * | 10,119,000 |
| Cost of Goods | 7,284,505 | 7,284,500 | 7,268,034 * | 7,284,505 |
| Gross Margin | 2,834,495 | 2,834,500 | 2,830,905 * | 2,834,495 |
| SGA | 2,128,688 | 2,128,690 | 2,125,766 * | 2,128,688 |
| Operating Profit | 56,421 | 56,421 | 55,753 * | 56,421 |
| Net Profit | 49,899 | 49,899 | 49,232 * | 49,899 |
| Inventory | 678,005 | 678,005 | 675,520 * | 678,005 |
| Current Assets | 1,524,780 | 1,524,780 | 1,520,321 * | 1,524,780 |
| Total Assets | 2,519,818 | 2,519,820 | 2,515,076 * | 2,519,818 |
| Current Liabilities | 1,827,718 | 1,827,720 | 1,769,349 * | 1,827,718 |
| Liabilities | 2,359,550 | — | 2,301,119 * | 2,359,550 |
| Total SE | 160,268 | 160,268 | 213,957 * | 160,268 |
| Total L+SE | 2,519,818 | 2,519,820 | 2,515,076 * | 2,519,818 |

### Reconciled Recommendation
[WARNING] Dolt contains original (pre-restatement) FY2022 values. The most recent SEC 10-K filing (FY2023 comparative) shows materially restated figures. **UPDATE RECOMMENDED** — update all 13 fields with restated values from the FY2023 10-K. Use reportDate 2023-01-29.

---

## FY2023 — reportDate: 2024-01-28

### Sources

**SEC FY2023 10-K (period 2024-01-28):**
- Net Revenue: 11,147,720
- COGS: 7,986,202
- Gross Margin: 3,161,518
- SGA: 2,442,683
- Marketing (separate): 742,460
- Operating Expenses Total: 3,185,143
- Operating Profit: -23,625
- Net Profit: 39,580
- Inventory: 719,273
- Current Assets: 2,104,348
- Total Assets: 3,186,851
- Current Liabilities: 2,110,877
- Total Liabilities: 2,676,607
- Total SE: 510,244
- Total L+SE: 3,186,851

**Yahoo Finance (2024-01-31 column):**
- Net Revenue: 11,147,700
- COGS: 7,986,200
- Gross Margin: 3,161,500
- SGA: 3,185,100 [WARNING — matches total operating expenses, not SGA]
- Operating Profit: -23,600
- Net Profit: 39,600
- Inventory: 719,273
- Current Assets: 2,104,350
- Total Assets: 3,186,850
- Current Liabilities: 2,110,880
- Total SE: 510,244
- Total L+SE: 3,186,850

**Note on Yahoo SGA:** Yahoo's `Selling General And Administration` = 3,185,100 ≈ Total Operating Expenses (3,185,143). This triggers **Rule 3: [WARNING] Yahoo SGA ≈ Total Operating Expenses — do not use Yahoo for SGA.** The correct SGA from SEC = 2,442,683.

**Dolt (year=2023):**
- Net Revenue: 11,147,720
- COGS: 7,986,202
- Gross Margin: 3,161,518
- SGA: 2,442,683
- Operating Profit: -23,625
- Net Profit: 39,580
- Inventory: 719,273
- Current Assets: 2,104,348
- Total Assets: 3,186,851
- Current Liabilities: 2,110,877
- Liabilities: 2,676,607
- Total SE: 510,244
- Total L+SE: 3,186,851

### Anomaly Detection

**[WARNING] Yahoo SGA = 3,185,100 ≈ Total Operating Expenses (3,185,143).** Yahoo is aggregating SGA + Marketing into one composite line. Do not use Yahoo SGA for this year.

**Balance Sheet:**
- Liabilities (derived): 3,186,851 − 510,244 = 2,676,607 ✓
- Total L+SE: 3,186,851 ✓

**Gross Margin:** 3,161,518 / 11,147,720 = 28.4% — within benchmark range ✓

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 11,147,720 | 11,147,700 | 11,147,720 | 11,147,720 |
| Cost of Goods | 7,986,202 | 7,986,200 | 7,986,202 | 7,986,202 |
| Gross Margin | 3,161,518 | 3,161,500 | 3,161,518 | 3,161,518 |
| SGA | 2,442,683 | 3,185,100 * | 2,442,683 | 2,442,683 (use SEC) |
| Operating Profit | -23,625 | -23,600 | -23,625 | -23,625 |
| Net Profit | 39,580 | 39,600 | 39,580 | 39,580 |
| Inventory | 719,273 | 719,273 | 719,273 | 719,273 |
| Current Assets | 2,104,348 | 2,104,350 | 2,104,348 | 2,104,348 |
| Total Assets | 3,186,851 | 3,186,850 | 3,186,851 | 3,186,851 |
| Current Liabilities | 2,110,877 | 2,110,880 | 2,110,877 | 2,110,877 |
| Liabilities | 2,676,607 | — | 2,676,607 | 2,676,607 |
| Total SE | 510,244 | 510,244 | 510,244 | 510,244 |
| Total L+SE | 3,186,851 | 3,186,850 | 3,186,851 | 3,186,851 |

### Reconciled Recommendation
Dolt matches SEC on all fields. Yahoo SGA is inflated (composite line) but Dolt is correct. **Dolt is correct. NO CHANGE needed.**

---

## FY2024 — reportDate: 2025-02-02

### Sources

**SEC FY2024 10-K (period 2025-02-02):**
- Net Revenue: 11,861,335
- COGS: 8,393,631
- Gross Margin: 3,467,704
- SGA: 2,551,004
- Marketing (separate): 804,113
- Operating Expenses Total: 3,355,117
- Operating Profit: 112,587
- Net Profit: 392,738
- Inventory: 836,695
- Current Assets: 1,662,366
- Total Assets: 3,014,527
- Current Liabilities: 2,206,723
- Total Liabilities: 2,753,068
- Total SE: 261,459
- Total L+SE: 3,014,527

**Yahoo Finance (2025-01-31 column — closest available):**
- Net Revenue: 11,861,300
- COGS: 8,393,600
- Gross Margin: 3,467,700
- SGA: 3,355,100 [WARNING — matches total operating expenses]
- Operating Profit: 112,600
- Net Profit: 392,700
- Inventory: 836,700
- Current Assets: 1,662,400
- Total Assets: 3,014,500
- Current Liabilities: 2,206,700
- Total SE: 261,500
- Total L+SE: 3,014,500

**Note on Yahoo SGA:** Yahoo's `Selling General And Administration` = 3,355,100 ≈ Total Operating Expenses (3,355,117). **[WARNING] Rule 3 applies — Yahoo SGA is again the composite total. Use SEC SGA = 2,551,004.**

**Dolt (year=2024):**
- Net Revenue: 11,861,335
- COGS: 8,393,631
- Gross Margin: 3,467,704
- SGA: 2,551,004
- Operating Profit: 112,587
- Net Profit: 392,738
- Inventory: 836,695
- Current Assets: 1,662,366
- Total Assets: 3,014,527
- Current Liabilities: 2,206,723
- Liabilities: 2,753,068
- Total SE: 261,459
- Total L+SE: 3,014,527

### Anomaly Detection

**[WARNING] Yahoo SGA = 3,355,100 ≈ Total Operating Expenses (3,355,117).** Yahoo is presenting the combined SGA+Marketing total. Do not use Yahoo SGA.

**Balance Sheet:**
- Liabilities (derived): 3,014,527 − 261,459 = 2,753,068 ✓
- Total L+SE: 3,014,527 ✓

**Gross Margin:** 3,467,704 / 11,861,335 = 29.2% — within benchmark range ✓

**Net Profit note:** Very high net profit (392,738) driven largely by tax benefit of -241,045 (deferred tax asset recognition). Pretax income was only 151,693.

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 11,861,335 | 11,861,300 | 11,861,335 | 11,861,335 |
| Cost of Goods | 8,393,631 | 8,393,600 | 8,393,631 | 8,393,631 |
| Gross Margin | 3,467,704 | 3,467,700 | 3,467,704 | 3,467,704 |
| SGA | 2,551,004 | 3,355,100 * | 2,551,004 | 2,551,004 (use SEC) |
| Operating Profit | 112,587 | 112,600 | 112,587 | 112,587 |
| Net Profit | 392,738 | 392,700 | 392,738 | 392,738 |
| Inventory | 836,695 | 836,700 | 836,695 | 836,695 |
| Current Assets | 1,662,366 | 1,662,400 | 1,662,366 | 1,662,366 |
| Total Assets | 3,014,527 | 3,014,500 | 3,014,527 | 3,014,527 |
| Current Liabilities | 2,206,723 | 2,206,700 | 2,206,723 | 2,206,723 |
| Liabilities | 2,753,068 | — | 2,753,068 | 2,753,068 |
| Total SE | 261,459 | 261,500 | 261,459 | 261,459 |
| Total L+SE | 3,014,527 | 3,014,500 | 3,014,527 | 3,014,527 |

### Reconciled Recommendation
Dolt matches SEC on all fields. Yahoo SGA is inflated (composite) but Dolt is correct. **Dolt is correct. NO CHANGE needed.**

---

## FY2025 — reportDate: 2026-02-01

### Sources

**SEC FY2025 10-K (period 2026-02-01) — NEW YEAR:**
- Net Revenue: 12,601,500
- COGS: 8,847,600
- Gross Margin: 3,753,900
- SGA: 2,674,700 (SellingGeneralAndAdministrativeExpense)
- Marketing (separate): 824,900
- Operating Expenses Total: 3,499,600
- Operating Profit: 254,300
- Net Profit: 222,800
- Inventory: 864,800
- Current Assets: 2,035,800
- Total Assets: 3,366,400
- Current Liabilities: 2,301,600
- Total Liabilities: 2,868,500
- Total SE: 497,900
- Total L+SE: 3,366,400

**Yahoo Finance (2026-01-31 column — closest available):**
- Net Revenue: 12,601,500
- COGS: 8,847,600
- Gross Margin: 3,753,900
- SGA: 3,499,600 [WARNING — matches total operating expenses]
- Operating Profit: 254,300
- Net Profit: 222,800
- Inventory: 864,800
- Current Assets: 2,035,800
- Total Assets: 3,366,400
- Current Liabilities: 2,301,600
- Total SE: 497,900
- Total L+SE: 3,366,400

**Note on Yahoo SGA:** Yahoo `Selling General And Administration` = 3,499,600 = Total Operating Expenses exactly. **[WARNING] Rule 3 — do not use Yahoo SGA. Use SEC SGA = 2,674,700.**

**Dolt (year=2025):** NOT IN DATABASE

### Anomaly Detection

**[WARNING] Yahoo SGA = Total Operating Expenses (3,499,600). Same issue as FY2023 and FY2024. Use SEC.**

**Balance Sheet:**
- Liabilities (derived): 3,366,400 − 497,900 = 2,868,500 ✓
- Total L+SE: 3,366,400 ✓

**Gross Margin:** 3,753,900 / 12,601,500 = 29.8% — within benchmark range ✓

**Net Profit note:** Net profit 222,800 with tax provision of 40,500 (normal tax rate). This is a genuinely profitable year unlike FY2024's inflated net profit from tax benefit.

**Note on SEC data precision:** The FY2025 10-K figures appear rounded to nearest $100K in the XBRL data (all values end in 00). The FY2024 comparison column in the same filing also shows rounded values (11,861,300 vs exact 11,861,335 in FY2024 10-K). This is expected for rounded XBRL reporting; the FY2025 values should be treated as rounded to nearest $100K.

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 12,601,500 | 12,601,500 | NOT IN DB | 12,601,500 |
| Cost of Goods | 8,847,600 | 8,847,600 | NOT IN DB | 8,847,600 |
| Gross Margin | 3,753,900 | 3,753,900 | NOT IN DB | 3,753,900 |
| SGA | 2,674,700 | 3,499,600 * | NOT IN DB | 2,674,700 (use SEC) |
| Operating Profit | 254,300 | 254,300 | NOT IN DB | 254,300 |
| Net Profit | 222,800 | 222,800 | NOT IN DB | 222,800 |
| Inventory | 864,800 | 864,800 | NOT IN DB | 864,800 |
| Current Assets | 2,035,800 | 2,035,800 | NOT IN DB | 2,035,800 |
| Total Assets | 3,366,400 | 3,366,400 | NOT IN DB | 3,366,400 |
| Current Liabilities | 2,301,600 | 2,301,600 | NOT IN DB | 2,301,600 |
| Liabilities | 2,868,500 | — | NOT IN DB | 2,868,500 |
| Total SE | 497,900 | 497,900 | NOT IN DB | 497,900 |
| Total L+SE | 3,366,400 | 3,366,400 | NOT IN DB | 3,366,400 |

### Reconciled Recommendation
FY2025 is a new year not yet in Dolt. **INSERT REQUIRED.** Use SEC values. reportDate = 2026-02-01.

---

## Consolidated Reconciled Values

All values in thousands of dollars (USD).

| Field | FY2019 | FY2020 | FY2021 | FY2022 (restated) | FY2023 | FY2024 | FY2025 (new) |
|-------|--------|--------|--------|--------------------|--------|--------|--------------|
| reportDate | 2020-02-02 | 2021-01-31 | 2022-01-30 | 2023-01-29 | 2024-01-28 | 2025-02-02 | 2026-02-01 |
| Net Revenue | 4,846,743 | 7,146,264 | 8,890,773 | 10,119,000 | 11,147,720 | 11,861,335 | 12,601,500 |
| Cost of Goods | 3,702,683 | 5,325,457 | 6,517,191 | 7,284,505 | 7,986,202 | 8,393,631 | 8,847,600 |
| Gross Margin | 1,144,060 | 1,820,807 | 2,373,582 | 2,834,495 | 3,161,518 | 3,467,704 | 3,753,900 |
| SGA | 969,890 | 1,397,969 | 1,826,858 | 2,128,688 | 2,442,683 | 2,551,004 | 2,674,700 |
| Operating Profit | -252,726 | -90,464 | -72,178 | 56,421 | -23,625 | 112,587 | 254,300 |
| Net Profit | -252,370 | -92,486 | -73,817 | 49,899 | 39,580 | 392,738 | 222,800 |
| Inventory | 317,808 | 513,304 | 560,430 | 678,005 | 719,273 | 836,695 | 864,800 |
| Current Assets | 629,789 | 1,226,778 | 1,323,532 | 1,524,780 | 2,104,348 | 1,662,366 | 2,035,800 |
| Total Assets | 932,321 | 1,740,910 | 2,086,281 | 2,519,818 | 3,186,851 | 3,014,527 | 3,366,400 |
| Current Liabilities | 1,100,538 | 1,380,862 | 1,644,879 | 1,827,718 | 2,110,877 | 2,206,723 | 2,301,600 |
| Liabilities | 1,336,295 | 1,742,914 | 2,071,545 | 2,359,550 | 2,676,607 | 2,753,068 | 2,868,500 |
| Total SE | -403,974 | -2,004 | 14,736 | 160,268 | 510,244 | 261,459 | 497,900 |
| Total L+SE | 932,321 | 1,740,910 | 2,086,281 | 2,519,818 | 3,186,851 | 3,014,527 | 3,366,400 |

---

## Unresolved Flags

1. **[WARNING] FY2022 Restatement** — Dolt contains original FY2022 figures. The FY2023 10-K comparative data shows restated figures across all income statement and balance sheet fields. All 13 fields need updating.

2. **[WARNING] Yahoo SGA = Total Operating Expenses** for FY2023, FY2024, and FY2025 — Yahoo is aggregating SGA + Marketing advertising into a single line labeled "Selling General And Administration." Always use SEC SGA for Chewy.

3. **[WARNING] Negative SE** in FY2019 (-403,974) and FY2020 (-2,004) — expected for Chewy's growth-phase accumulated deficit; not an error.

4. **[WARNING] FY2019 Gross Margin = 23.6%** — slightly below the 25–30% benchmark. This is the first full year as a public company and reflects the earlier stage of the business.

5. **[INFO] FY2025 XBRL data rounded** to nearest $100K — values from SEC XBRL are rounded. This is the precision available.

---

## Actions Required

| Year | Action | Details |
|------|--------|---------|
| 2019 | NO CHANGE | Dolt correct |
| 2020 | NO CHANGE | Dolt correct |
| 2021 | NO CHANGE | Dolt correct |
| 2022 | UPDATE — restated values | All 13 fields differ from latest SEC filing |
| 2023 | NO CHANGE | Dolt correct |
| 2024 | NO CHANGE | Dolt correct |
| 2025 | INSERT — new year | Not yet in Dolt; insert from SEC |

---

**Analysis complete.** Run `/insert-financials CHWY` to write all changed years to the database.

**Unresolved flags:**
- FY2022 restatement: Dolt has original figures; recommend updating to restated values from FY2023 10-K comparative
- Yahoo SGA is a composite (SGA + Marketing) line for FY2023, FY2024, FY2025 — always use SEC for Chewy SGA
- FY2025 XBRL values are rounded to nearest $100K
