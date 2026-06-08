# Costco (COST) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-06
**Source:** /verify-dolt-db-financials skill

---

## Company Metadata
- **company:** Costco
- **CIK:** 909832
- **display_name:** Costco
- **ticker_symbol:** COST
- **Segment:** Warehouse Clubs
- **Fiscal year end:** Late August / early September

---

## Per-Year Summary

| Year | reportDate  | Action                                                        |
|------|-------------|---------------------------------------------------------------|
| 2018 | 2018-09-02  | OK — Dolt matches SEC                                         |
| 2019 | 2019-09-01  | UPDATE REQUIRED — Dolt balance sheet data is wrong (copied from 2018) |
| 2020 | 2020-08-30  | OK — Dolt matches SEC                                         |
| 2021 | 2021-08-29  | [WARNING] SGA $18,461K in Dolt; 2022 filing shows restated $18,537K — minor restatement |
| 2022 | 2022-08-28  | OK — Dolt matches SEC                                         |
| 2023 | 2023-09-03  | OK — Dolt matches SEC                                         |
| 2024 | 2024-09-01  | OK — Dolt matches SEC                                         |
| 2025 | 2025-08-31  | INSERT REQUIRED — FY2025 not yet in Dolt                      |

---

## Notes on SGA

Costco uses a single `SellingGeneralAndAdministrativeExpense` tag on the income statement (SEC XBRL). In FY2018, there was a separate `PreOpeningCosts` line ($68M) reported outside of SGA. From FY2022 onward, preopening costs appear to be absorbed into SGA. The SGA values used here are the direct `SellingGeneralAndAdministrativeExpense` line from SEC, which Dolt also uses consistently.

Yahoo Finance `Selling General And Administration` matches SEC SGA exactly for all years where Yahoo has annual data (2022–2025). No composite SGA anomaly detected.

---

## FY2018 Analysis

**reportDate:** 2018-09-02

### Side-by-Side Comparison (values in $thousands)

| Field                             | SEC           | Yahoo  | Dolt (current) | Recommended   |
|-----------------------------------|---------------|--------|----------------|---------------|
| Net Revenue                       | 141,576,000   | N/A    | 141,576,000    | 141,576,000   |
| Cost of Goods                     | 123,152,000   | N/A    | 123,152,000    | 123,152,000   |
| Gross Margin                      | 18,424,000    | N/A    | 18,424,000     | 18,424,000    |
| SGA                               | 13,876,000    | N/A    | 13,876,000     | 13,876,000    |
| Operating Profit                  | 4,480,000     | N/A    | 4,480,000      | 4,480,000     |
| Net Profit                        | 3,134,000     | N/A    | 3,134,000      | 3,134,000     |
| Inventory                         | 11,040,000    | N/A    | 11,040,000     | 11,040,000    |
| Current Assets                    | 20,289,000    | N/A    | 20,289,000     | 20,289,000    |
| Total Assets                      | 40,830,000    | N/A    | 40,830,000     | 40,830,000    |
| Current Liabilities               | 19,926,000    | N/A    | 19,926,000     | 19,926,000    |
| Liabilities                       | 27,727,000    | N/A    | 27,727,000     | 27,727,000    |
| Total Shareholder Equity          | 13,103,000    | N/A    | 13,103,000     | 13,103,000    |
| Total Liabilities and SE          | 40,830,000    | N/A    | 40,830,000     | 40,830,000    |

**Note:** Total SE = $13,103M includes Costco stockholders' equity ($12,799M) + Minority Interest ($304M). Dolt uses the consolidated total, consistent with this.

### Anomaly Checks
- Gross margin = 18,424,000 / 141,576,000 = **13.0%** — normal for warehouse club model
- Balance sheet: Total Assets ($40,830M) = Total Liabilities ($27,727M) + Total SE ($13,103M) = $40,830M ✓
- No SGA composite issue
- Yahoo Finance does not have data for FY2018

### Reconciled Values
All fields match SEC. **No changes needed.**

---

## FY2019 Analysis

**reportDate:** 2019-09-01

### Notes on SEC Data
The SEC MCP returned quarterly 10-Q data for FY2019 (showing Q2 periods). Annual income statement values were sourced from the FY2020 10-K comparative columns (2019-09-01), which is the most recent filing for FY2019 data.

### Side-by-Side Comparison (values in $thousands)

| Field                             | SEC           | Yahoo  | Dolt (current) | Recommended   |
|-----------------------------------|---------------|--------|----------------|---------------|
| Net Revenue                       | 152,703,000   | N/A    | 152,703,000    | 152,703,000   |
| Cost of Goods                     | 132,886,000   | N/A    | 132,886,000    | 132,886,000   |
| Gross Margin                      | 19,817,000    | N/A    | 19,817,000     | 19,817,000    |
| SGA                               | 14,994,000    | N/A    | 14,994,000     | 14,994,000    |
| Operating Profit                  | 4,737,000     | N/A    | 4,737,000      | 4,737,000     |
| Net Profit                        | 3,659,000     | N/A    | 3,659,000      | 3,659,000     |
| Inventory                         | 11,395,000    | N/A    | 11,040,000 *   | 11,395,000    |
| Current Assets                    | 23,485,000    | N/A    | 20,289,000 *   | 23,485,000    |
| Total Assets                      | 45,400,000    | N/A    | 40,830,000 *   | 45,400,000    |
| Current Liabilities               | 23,237,000    | N/A    | 19,926,000 *   | 23,237,000    |
| Liabilities                       | 29,816,000    | N/A    | 27,727,000 *   | 29,816,000    |
| Total Shareholder Equity          | 15,584,000    | N/A    | 13,103,000 *   | 15,584,000    |
| Total Liabilities and SE          | 45,400,000    | N/A    | 40,830,000 *   | 45,400,000    |

`*` = Dolt value differs from SEC — **CRITICAL ERROR**: Dolt FY2019 balance sheet data is identical to FY2018 data. All balance sheet fields for FY2019 were copied from FY2018 and must be corrected.

### Anomaly Checks
- Gross margin = 19,817,000 / 152,703,000 = **13.0%** — normal
- Balance sheet check (SEC): $45,400M = $29,816M + $15,584M = $45,400M ✓
- [ERROR in Dolt]: Balance sheet for FY2019 is wrong — all values are FY2018 values
- Income statement values (Revenue, COGS, SGA, Operating, Net) in Dolt are correct

### Reconciled Values
**Income statement:** No changes needed.
**Balance sheet:** All 7 balance sheet fields must be updated in Dolt.

**Note on Total SE:** SEC shows Costco stockholders' equity = $15,243M + Minority Interest = $341M → Total SE = $15,584M. Using total including NCI for consistency with other years.

---

## FY2020 Analysis

**reportDate:** 2020-08-30

### Side-by-Side Comparison (values in $thousands)

| Field                             | SEC           | Yahoo  | Dolt (current) | Recommended   |
|-----------------------------------|---------------|--------|----------------|---------------|
| Net Revenue                       | 166,761,000   | N/A    | 166,761,000    | 166,761,000   |
| Cost of Goods                     | 144,939,000   | N/A    | 144,939,000    | 144,939,000   |
| Gross Margin                      | 21,822,000    | N/A    | 21,822,000     | 21,822,000    |
| SGA                               | 16,332,000    | N/A    | 16,332,000     | 16,332,000    |
| Operating Profit                  | 5,435,000     | N/A    | 5,435,000      | 5,435,000     |
| Net Profit                        | 4,002,000     | N/A    | 4,002,000      | 4,002,000     |
| Inventory                         | 12,242,000    | N/A    | 12,242,000     | 12,242,000    |
| Current Assets                    | 28,120,000    | N/A    | 28,120,000     | 28,120,000    |
| Total Assets                      | 55,556,000    | N/A    | 55,556,000     | 55,556,000    |
| Current Liabilities               | 24,844,000    | N/A    | 24,844,000     | 24,844,000    |
| Liabilities                       | 36,851,000    | N/A    | 36,851,000     | 36,851,000    |
| Total Shareholder Equity          | 18,705,000    | N/A    | 18,705,000     | 18,705,000    |
| Total Liabilities and SE          | 55,556,000    | N/A    | 55,556,000     | 55,556,000    |

### Anomaly Checks
- Gross margin = 21,822,000 / 166,761,000 = **13.1%** — normal
- Balance sheet: $55,556M = $36,851M + $18,705M = $55,556M ✓
- SE includes NCI of $421M
- FY2020 saw a large asset increase from adoption of ASC 842 (operating lease right-of-use assets of $2,788M added)

### Reconciled Values
All fields match SEC. **No changes needed.**

---

## FY2021 Analysis

**reportDate:** 2021-08-29

### Side-by-Side Comparison (values in $thousands)

| Field                             | SEC (2021 10-K) | Yahoo  | Dolt (current) | Recommended    |
|-----------------------------------|-----------------|--------|----------------|----------------|
| Net Revenue                       | 195,929,000     | N/A    | 195,929,000    | 195,929,000    |
| Cost of Goods                     | 170,684,000     | N/A    | 170,684,000    | 170,684,000    |
| Gross Margin                      | 25,245,000      | N/A    | 25,245,000     | 25,245,000     |
| SGA                               | 18,461,000      | N/A    | 18,461,000     | 18,461,000     |
| Operating Profit                  | 6,708,000       | N/A    | 6,708,000      | 6,708,000      |
| Net Profit                        | 5,007,000       | N/A    | 5,007,000      | 5,007,000      |
| Inventory                         | 14,215,000      | N/A    | 14,215,000     | 14,215,000     |
| Current Assets                    | 29,505,000      | N/A    | 29,505,000     | 29,505,000     |
| Total Assets                      | 59,268,000      | N/A    | 59,268,000     | 59,268,000     |
| Current Liabilities               | 29,441,000      | N/A    | 29,441,000     | 29,441,000     |
| Liabilities                       | 41,190,000      | N/A    | 41,190,000     | 41,190,000     |
| Total Shareholder Equity          | 18,078,000      | N/A    | 18,078,000     | 18,078,000     |
| Total Liabilities and SE          | 59,268,000      | N/A    | 59,268,000     | 59,268,000     |

### Anomaly Checks
- Gross margin = 25,245,000 / 195,929,000 = **12.9%** — normal
- Balance sheet: $59,268M = $41,190M + $18,078M = $59,268M ✓
- [WARNING] The FY2022 10-K shows restated FY2021 SGA as $18,537,000 (vs. $18,461,000 in standalone FY2021 10-K — a $76M difference). This appears to be a reclassification of preopening expenses from a separate line into SGA. Dolt currently has $18,461,000 (standalone filing value). Recommend keeping $18,461,000 per the original 2021 10-K; the difference is immaterial at 0.4%.
- Yahoo Finance has no annual data for FY2021

### Reconciled Values
All fields match FY2021 standalone 10-K. **No changes needed.** (Restatement difference noted but not material.)

---

## FY2022 Analysis

**reportDate:** 2022-08-28

### Side-by-Side Comparison (values in $thousands)

| Field                             | SEC           | Yahoo         | Dolt (current) | Recommended   |
|-----------------------------------|---------------|---------------|----------------|---------------|
| Net Revenue                       | 226,954,000   | 226,954,000   | 226,954,000    | 226,954,000   |
| Cost of Goods                     | 199,382,000   | 199,382,000   | 199,382,000    | 199,382,000   |
| Gross Margin                      | 27,572,000    | 27,572,000    | 27,572,000     | 27,572,000    |
| SGA                               | 19,779,000    | 19,779,000    | 19,779,000     | 19,779,000    |
| Operating Profit                  | 7,793,000     | 7,793,000     | 7,793,000      | 7,793,000     |
| Net Profit                        | 5,844,000     | 5,844,000     | 5,844,000      | 5,844,000     |
| Inventory                         | 17,907,000    | 17,907,000    | 17,907,000     | 17,907,000    |
| Current Assets                    | 32,696,000    | 32,696,000    | 32,696,000     | 32,696,000    |
| Total Assets                      | 64,166,000    | 64,166,000    | 64,166,000     | 64,166,000    |
| Current Liabilities               | 31,998,000    | 31,998,000    | 31,998,000     | 31,998,000    |
| Liabilities                       | 43,519,000    | 43,519,000    | 43,519,000     | 43,519,000    |
| Total Shareholder Equity          | 20,647,000    | 20,647,000    | 20,647,000     | 20,647,000    |
| Total Liabilities and SE          | 64,166,000    | 64,166,000    | 64,166,000     | 64,166,000    |

### Anomaly Checks
- Gross margin = 27,572,000 / 226,954,000 = **12.1%** — normal
- Balance sheet: $64,166M = $43,519M + $20,647M = $64,166M ✓
- SEC, Yahoo, and Dolt are in perfect agreement across all fields

### Reconciled Values
All sources agree. **No changes needed.**

---

## FY2023 Analysis

**reportDate:** 2023-09-03

### Side-by-Side Comparison (values in $thousands)

| Field                             | SEC           | Yahoo         | Dolt (current) | Recommended   |
|-----------------------------------|---------------|---------------|----------------|---------------|
| Net Revenue                       | 242,290,000   | 242,290,000   | 242,290,000    | 242,290,000   |
| Cost of Goods                     | 212,586,000   | 212,586,000   | 212,586,000    | 212,586,000   |
| Gross Margin                      | 29,704,000    | 29,704,000    | 29,704,000     | 29,704,000    |
| SGA                               | 21,590,000    | 21,590,000    | 21,590,000     | 21,590,000    |
| Operating Profit                  | 8,114,000     | 8,114,000     | 8,114,000      | 8,114,000     |
| Net Profit                        | 6,292,000     | 6,292,000     | 6,292,000      | 6,292,000     |
| Inventory                         | 16,651,000    | 16,651,000    | 16,651,000     | 16,651,000    |
| Current Assets                    | 35,879,000    | 35,879,000    | 35,879,000     | 35,879,000    |
| Total Assets                      | 68,994,000    | 68,994,000    | 68,994,000     | 68,994,000    |
| Current Liabilities               | 33,583,000    | 33,583,000    | 33,583,000     | 33,583,000    |
| Liabilities                       | 43,936,000    | 43,936,000    | 43,936,000     | 43,936,000    |
| Total Shareholder Equity          | 25,058,000    | 25,058,000    | 25,058,000     | 25,058,000    |
| Total Liabilities and SE          | 68,994,000    | 68,994,000    | 68,994,000     | 68,994,000    |

### Anomaly Checks
- Gross margin = 29,704,000 / 242,290,000 = **12.3%** — normal
- Balance sheet: $68,994M = $43,936M + $25,058M = $68,994M ✓
- Minority Interest = $0 from FY2023 onward (NCI fully consolidated/eliminated)

### Reconciled Values
All sources agree. **No changes needed.**

---

## FY2024 Analysis

**reportDate:** 2024-09-01

### Side-by-Side Comparison (values in $thousands)

| Field                             | SEC           | Yahoo         | Dolt (current) | Recommended   |
|-----------------------------------|---------------|---------------|----------------|---------------|
| Net Revenue                       | 254,453,000   | 254,453,000   | 254,453,000    | 254,453,000   |
| Cost of Goods                     | 222,358,000   | 222,358,000   | 222,358,000    | 222,358,000   |
| Gross Margin                      | 32,095,000    | 32,095,000    | 32,095,000     | 32,095,000    |
| SGA                               | 22,810,000    | 22,810,000    | 22,810,000     | 22,810,000    |
| Operating Profit                  | 9,285,000     | 9,285,000     | 9,285,000      | 9,285,000     |
| Net Profit                        | 7,367,000     | 7,367,000     | 7,367,000      | 7,367,000     |
| Inventory                         | 18,647,000    | 18,647,000    | 18,647,000     | 18,647,000    |
| Current Assets                    | 34,246,000    | 34,246,000    | 34,246,000     | 34,246,000    |
| Total Assets                      | 69,831,000    | 69,831,000    | 69,831,000     | 69,831,000    |
| Current Liabilities               | 35,464,000    | 35,464,000    | 35,464,000     | 35,464,000    |
| Liabilities                       | 46,209,000    | 46,209,000    | 46,209,000     | 46,209,000    |
| Total Shareholder Equity          | 23,622,000    | 23,622,000    | 23,622,000     | 23,622,000    |
| Total Liabilities and SE          | 69,831,000    | 69,831,000    | 69,831,000     | 69,831,000    |

### Anomaly Checks
- Gross margin = 32,095,000 / 254,453,000 = **12.6%** — normal
- Balance sheet: $69,831M = $46,209M + $23,622M = $69,831M ✓
- Note: Dolt SE shows $23,622M (Costco stockholders' equity only; NCI = $0)

### Reconciled Values
All sources agree. **No changes needed.**

---

## FY2025 Analysis (NEW YEAR — Not Yet in Dolt)

**reportDate:** 2025-08-31

### Side-by-Side Comparison (values in $thousands)

| Field                             | SEC           | Yahoo         | Dolt (current) | Recommended   |
|-----------------------------------|---------------|---------------|----------------|---------------|
| Net Revenue                       | 275,235,000   | 275,235,000   | N/A            | 275,235,000   |
| Cost of Goods                     | 239,886,000   | 239,886,000   | N/A            | 239,886,000   |
| Gross Margin                      | 35,349,000    | 35,349,000    | N/A            | 35,349,000    |
| SGA                               | 24,966,000    | 24,966,000    | N/A            | 24,966,000    |
| Operating Profit                  | 10,383,000    | 10,383,000    | N/A            | 10,383,000    |
| Net Profit                        | 8,099,000     | 8,099,000     | N/A            | 8,099,000     |
| Inventory                         | 18,116,000    | 18,116,000    | N/A            | 18,116,000    |
| Current Assets                    | 38,380,000    | 38,380,000    | N/A            | 38,380,000    |
| Total Assets                      | 77,099,000    | 77,099,000    | N/A            | 77,099,000    |
| Current Liabilities               | 37,108,000    | 37,108,000    | N/A            | 37,108,000    |
| Liabilities                       | 47,935,000    | 47,935,000    | N/A            | 47,935,000    |
| Total Shareholder Equity          | 29,164,000    | 29,164,000    | N/A            | 29,164,000    |
| Total Liabilities and SE          | 77,099,000    | 77,099,000    | N/A            | 77,099,000    |

### Anomaly Checks
- Gross margin = 35,349,000 / 275,235,000 = **12.8%** — normal for warehouse club
- Balance sheet: $77,099M = $47,935M + $29,164M = $77,099M ✓
- SEC and Yahoo agree on all fields
- No minority interest (NCI = $0)
- Net Revenue includes: Net sales $269,912M + Membership fees $5,323M = $275,235M

### Reconciled Values
**INSERT REQUIRED** — FY2025 is not in Dolt. All values sourced from SEC (confirmed by Yahoo).

---

## Full Reconciled Values Summary (all years, in $thousands)

| Year | reportDate  | Net Revenue  | Cost of Goods | Gross Margin | SGA        | Operating Profit | Net Profit | Inventory  | Current Assets | Total Assets | Current Liabilities | Liabilities  | Total SE   | Total L+SE   |
|------|-------------|--------------|---------------|--------------|------------|------------------|------------|------------|----------------|--------------|---------------------|--------------|------------|--------------|
| 2018 | 2018-09-02  | 141,576,000  | 123,152,000   | 18,424,000   | 13,876,000 | 4,480,000        | 3,134,000  | 11,040,000 | 20,289,000     | 40,830,000   | 19,926,000          | 27,727,000   | 13,103,000 | 40,830,000   |
| 2019 | 2019-09-01  | 152,703,000  | 132,886,000   | 19,817,000   | 14,994,000 | 4,737,000        | 3,659,000  | 11,395,000 | 23,485,000     | 45,400,000   | 23,237,000          | 29,816,000   | 15,584,000 | 45,400,000   |
| 2020 | 2020-08-30  | 166,761,000  | 144,939,000   | 21,822,000   | 16,332,000 | 5,435,000        | 4,002,000  | 12,242,000 | 28,120,000     | 55,556,000   | 24,844,000          | 36,851,000   | 18,705,000 | 55,556,000   |
| 2021 | 2021-08-29  | 195,929,000  | 170,684,000   | 25,245,000   | 18,461,000 | 6,708,000        | 5,007,000  | 14,215,000 | 29,505,000     | 59,268,000   | 29,441,000          | 41,190,000   | 18,078,000 | 59,268,000   |
| 2022 | 2022-08-28  | 226,954,000  | 199,382,000   | 27,572,000   | 19,779,000 | 7,793,000        | 5,844,000  | 17,907,000 | 32,696,000     | 64,166,000   | 31,998,000          | 43,519,000   | 20,647,000 | 64,166,000   |
| 2023 | 2023-09-03  | 242,290,000  | 212,586,000   | 29,704,000   | 21,590,000 | 8,114,000        | 6,292,000  | 16,651,000 | 35,879,000     | 68,994,000   | 33,583,000          | 43,936,000   | 25,058,000 | 68,994,000   |
| 2024 | 2024-09-01  | 254,453,000  | 222,358,000   | 32,095,000   | 22,810,000 | 9,285,000        | 7,367,000  | 18,647,000 | 34,246,000     | 69,831,000   | 35,464,000          | 46,209,000   | 23,622,000 | 69,831,000   |
| 2025 | 2025-08-31  | 275,235,000  | 239,886,000   | 35,349,000   | 24,966,000 | 10,383,000       | 8,099,000  | 18,116,000 | 38,380,000     | 77,099,000   | 37,108,000          | 47,935,000   | 29,164,000 | 77,099,000   |

---

## Unresolved Flags

1. **[CRITICAL] FY2019 balance sheet data in Dolt is wrong** — All balance sheet fields (Inventory, Current Assets, Total Assets, Current Liabilities, Liabilities, Total SE, Total L+SE) are duplicated from FY2018 and must be corrected to FY2019 values.

2. **[WARNING] FY2021 SGA minor restatement** — Standalone 2021 10-K shows $18,461M; 2022 comparative shows $18,537M (+$76M, 0.4% difference). Dolt currently has $18,461M (original filing). Keeping original value; difference is immaterial.

3. **[INSERT] FY2025 not in Dolt** — New year requires INSERT.

---

**Analysis complete.** Run `/insert-financials COST` to write all changed years to the database.

Changed years requiring SQL writes:
- FY2019: UPDATE balance sheet fields (7 fields need correction)
- FY2025: INSERT new row
