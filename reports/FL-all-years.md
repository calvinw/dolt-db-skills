# Foot Locker (FL) — FY2018–FY2024 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2018 | 2019-02-02 | No change |
| 2019 | 2020-02-01 | No change |
| 2020 | 2021-01-30 | No change |
| 2021 | 2022-01-29 | Correction: Net Revenue (8,958,000→8,968,000), Gross Margin (3,080,000→3,090,000), Operating Profit (860,000→870,000), Net Profit (892,000→893,000) |
| 2022 | 2023-01-28 | Correction: Net Profit (341,000→342,000) |
| 2023 | 2024-02-03 | No change |
| 2024 | 2025-02-01 | No change |

---

## Notes

- **Yahoo Finance unavailable:** MCP returned "No financial data found for ticker symbol: FL" for all years. Analysis based on SEC 10-K and Dolt only.
- **Foot Locker fiscal year** ends in late January/early February. DB year label refers to the fiscal year that ended in the following January/February (e.g., "year 2021" = fiscal year ending 2022-01-29).
- **SGA treatment:** FL reports SGA (Selling, General and Administrative Expense) as a single line item, with D&A listed separately. No SGA composite rules needed. Values are clean across all years.
- **FY2021 restatement (Revenue + Operating Profit):** The FY2022 10-K restates FY2021 (2022-01-29) revenue from 8,958,000K to 8,968,000K by separately disclosing 10,000K in licensing revenue. Operating Income increases by the same 10,000K (860,000→870,000) because licensing has near-zero direct cost. The FY2023 10-K confirms these restated values. Per the restatement rule, the corrected values should be used.
- **FY2021 & FY2022 Net Profit (NCI issue):** FL had a noncontrolling interest (NCI) of ~1,000K in FY2021 and FY2022. Dolt values appear to use total ProfitLoss (including NCI) rather than NetIncomeLoss attributable to Foot Locker. The correct value is NetIncomeLoss (parent-only). FY2021: 892,000→893,000; FY2022: 341,000→342,000. FY2023 and FY2024 Dolt values correctly use NetIncomeLoss (NCI = 0 in those years).
- **FY2019 Total Assets jump:** Total Assets jumped from 3,820,000K (FY2018) to 6,589,000K (FY2019) due to ASC 842 adoption — operating lease right-of-use assets (~2,899,000K) added to the balance sheet for the first time. Expected, not an error.
- **Gross margins 27–34%:** Consistent with specialty footwear retail. Slightly below the specialty benchmark (35–55%) but reasonable for footwear, which carries lower margins than apparel.

---

## FY2018

| Field | SEC | Dolt (current) | Recommended |
|-------|-----|----------------|-------------|
| Net Revenue | 7,939,000 | 7,939,000 | 7,939,000 |
| Cost of Goods | 5,411,000 | 5,411,000 | 5,411,000 |
| Gross Margin | 2,528,000 | 2,528,000 | 2,528,000 |
| SGA | 1,614,000 | 1,614,000 | 1,614,000 |
| Operating Profit | 699,000 | 699,000 | 699,000 |
| Net Profit | 541,000 | 541,000 | 541,000 |
| Inventory | 1,269,000 | 1,269,000 | 1,269,000 |
| Current Assets | 2,518,000 | 2,518,000 | 2,518,000 |
| Total Assets | 3,820,000 | 3,820,000 | 3,820,000 |
| Current Liabilities | 764,000 | 764,000 | 764,000 |
| Liabilities | 1,314,000 | 1,314,000 | 1,314,000 |
| Total Shareholder Equity | 2,506,000 | 2,506,000 | 2,506,000 |
| Total Liabilities and SE | 3,820,000 | 3,820,000 | 3,820,000 |

**Balance sheet check:** 3,820,000 = 1,314,000 + 2,506,000 ✓
**Gross margin %:** 31.8%
**Action:** No change

---

## FY2019

| Field | SEC | Dolt (current) | Recommended |
|-------|-----|----------------|-------------|
| Net Revenue | 8,005,000 | 8,005,000 | 8,005,000 |
| Cost of Goods | 5,462,000 | 5,462,000 | 5,462,000 |
| Gross Margin | 2,543,000 | 2,543,000 | 2,543,000 |
| SGA | 1,650,000 | 1,650,000 | 1,650,000 |
| Operating Profit | 649,000 | 649,000 | 649,000 |
| Net Profit | 491,000 | 491,000 | 491,000 |
| Inventory | 1,208,000 | 1,208,000 | 1,208,000 |
| Current Assets | 2,386,000 | 2,386,000 | 2,386,000 |
| Total Assets | 6,589,000 | 6,589,000 | 6,589,000 |
| Current Liabilities | 1,194,000 | 1,194,000 | 1,194,000 |
| Liabilities | 4,116,000 | 4,116,000 | 4,116,000 |
| Total Shareholder Equity | 2,473,000 | 2,473,000 | 2,473,000 |
| Total Liabilities and SE | 6,589,000 | 6,589,000 | 6,589,000 |

**Balance sheet check:** 6,589,000 = 4,116,000 + 2,473,000 ✓
**Gross margin %:** 31.8%
**[INFO] Total Assets jump due to ASC 842 adoption (ROU assets ~2,899,000K added). Expected.**
**Action:** No change

---

## FY2020

| Field | SEC | Dolt (current) | Recommended |
|-------|-----|----------------|-------------|
| Net Revenue | 7,548,000 | 7,548,000 | 7,548,000 |
| Cost of Goods | 5,365,000 | 5,365,000 | 5,365,000 |
| Gross Margin | 2,183,000 | 2,183,000 | 2,183,000 |
| SGA | 1,587,000 | 1,587,000 | 1,587,000 |
| Operating Profit | 303,000 | 303,000 | 303,000 |
| Net Profit | 323,000 | 323,000 | 323,000 |
| Inventory | 923,000 | 923,000 | 923,000 |
| Current Assets | 2,835,000 | 2,835,000 | 2,835,000 |
| Total Assets | 7,043,000 | 7,043,000 | 7,043,000 |
| Current Liabilities | 1,644,000 | 1,644,000 | 1,644,000 |
| Liabilities | 4,267,000 | 4,267,000 | 4,267,000 |
| Total Shareholder Equity | 2,776,000 | 2,776,000 | 2,776,000 |
| Total Liabilities and SE | 7,043,000 | 7,043,000 | 7,043,000 |

**Balance sheet check:** 7,043,000 = 4,267,000 + 2,776,000 ✓
**Gross margin %:** 28.9%
**Action:** No change

---

## FY2021

| Field | SEC (FY2021 10-K) | SEC (FY2022+ 10-K restated) | Dolt (current) | Recommended |
|-------|-------------------|----------------------------|----------------|-------------|
| Net Revenue | 8,958,000 | **8,968,000** | 8,958,000 | **8,968,000** |
| Cost of Goods | 5,878,000 | 5,878,000 | 5,878,000 | 5,878,000 |
| Gross Margin | 3,080,000 | **3,090,000** | 3,080,000 | **3,090,000** |
| SGA | 1,851,000 | 1,851,000 | 1,851,000 | 1,851,000 |
| Operating Profit | 860,000 | **870,000** | 860,000 | **870,000** |
| Net Profit | 893,000 (NetIncomeLoss) | 893,000 | 892,000* | **893,000** |
| Inventory | 1,266,000 | 1,266,000 | 1,266,000 | 1,266,000 |
| Current Assets | 2,363,000 | 2,363,000 | 2,363,000 | 2,363,000 |
| Total Assets | 8,135,000 | 8,135,000 | 8,135,000 | 8,135,000 |
| Current Liabilities | 1,735,000 | 1,735,000 | 1,735,000 | 1,735,000 |
| Liabilities | 4,892,000 | 4,892,000 | 4,892,000 | 4,892,000 |
| Total Shareholder Equity | 3,243,000 | 3,243,000 | 3,243,000 | 3,243,000 |
| Total Liabilities and SE | 8,135,000 | 8,135,000 | 8,135,000 | 8,135,000 |

*Dolt 892,000 = total ProfitLoss (including NCI of 1,000K). Correct value is NetIncomeLoss = 893,000K (parent-attributable).

FY2022 10-K restates FY2021 to add 10,000K licensing revenue (previously embedded or omitted). Operating Income increases by same 10,000K. Restated values confirmed in FY2023 10-K.

**Balance sheet check:** 8,135,000 = 4,892,000 + 3,243,000 ✓
**Gross margin %:** 34.4% (using restated revenue)
**Action: Correction — Net Revenue 8,958,000→8,968,000; Gross Margin 3,080,000→3,090,000; Operating Profit 860,000→870,000; Net Profit 892,000→893,000**

---

## FY2022

| Field | SEC | Dolt (current) | Recommended |
|-------|-----|----------------|-------------|
| Net Revenue | 8,759,000 | 8,759,000 | 8,759,000 |
| Cost of Goods | 5,955,000 | 5,955,000 | 5,955,000 |
| Gross Margin | 2,804,000 | 2,804,000 | 2,804,000 |
| SGA | 1,903,000 | 1,903,000 | 1,903,000 |
| Operating Profit | 581,000 | 581,000 | 581,000 |
| Net Profit | 342,000 (NetIncomeLoss) | 341,000* | **342,000** |
| Inventory | 1,643,000 | 1,643,000 | 1,643,000 |
| Current Assets | 2,521,000 | 2,521,000 | 2,521,000 |
| Total Assets | 7,907,000 | 7,907,000 | 7,907,000 |
| Current Liabilities | 1,610,000 | 1,610,000 | 1,610,000 |
| Liabilities | 4,614,000 | 4,614,000 | 4,614,000 |
| Total Shareholder Equity | 3,293,000 | 3,293,000 | 3,293,000 |
| Total Liabilities and SE | 7,907,000 | 7,907,000 | 7,907,000 |

*Dolt 341,000 = total ProfitLoss (including NCI of 1,000K). Correct value is NetIncomeLoss = 342,000K (parent-attributable).

**Balance sheet check:** 7,907,000 = 4,614,000 + 3,293,000 ✓
**Gross margin %:** 32.0%
**Action: Correction — Net Profit 341,000→342,000**

---

## FY2023

| Field | SEC | Dolt (current) | Recommended |
|-------|-----|----------------|-------------|
| Net Revenue | 8,168,000 | 8,168,000 | 8,168,000 |
| Cost of Goods | 5,895,000 | 5,895,000 | 5,895,000 |
| Gross Margin | 2,273,000 | 2,273,000 | 2,273,000 |
| SGA | 1,852,000 | 1,852,000 | 1,852,000 |
| Operating Profit | 142,000 | 142,000 | 142,000 |
| Net Profit | -330,000 | -330,000 | -330,000 |
| Inventory | 1,509,000 | 1,509,000 | 1,509,000 |
| Current Assets | 2,225,000 | 2,225,000 | 2,225,000 |
| Total Assets | 6,868,000 | 6,868,000 | 6,868,000 |
| Current Liabilities | 1,291,000 | 1,291,000 | 1,291,000 |
| Liabilities | 3,978,000 | 3,978,000 | 3,978,000 |
| Total Shareholder Equity | 2,890,000 | 2,890,000 | 2,890,000 |
| Total Liabilities and SE | 6,868,000 | 6,868,000 | 6,868,000 |

**Balance sheet check:** 6,868,000 = 3,978,000 + 2,890,000 ✓
**Gross margin %:** 27.8%
**[INFO] Net loss of -330,000K driven by large nonoperating loss (-556,000K) in FY2023, primarily from writing down the Sidestep brand divestiture and impairment charges.**
**Action:** No change

---

## FY2024

| Field | SEC | Dolt (current) | Recommended |
|-------|-----|----------------|-------------|
| Net Revenue | 7,988,000 | 7,988,000 | 7,988,000 |
| Cost of Goods | 5,666,000 | 5,666,000 | 5,666,000 |
| Gross Margin | 2,322,000 | 2,322,000 | 2,322,000 |
| SGA | 1,920,000 | 1,920,000 | 1,920,000 |
| Operating Profit | 103,000 | 103,000 | 103,000 |
| Net Profit | 12,000 | 12,000 | 12,000 |
| Inventory | 1,525,000 | 1,525,000 | 1,525,000 |
| Current Assets | 2,259,000 | 2,259,000 | 2,259,000 |
| Total Assets | 6,748,000 | 6,748,000 | 6,748,000 |
| Current Liabilities | 1,330,000 | 1,330,000 | 1,330,000 |
| Liabilities | 3,839,000 | 3,839,000 | 3,839,000 |
| Total Shareholder Equity | 2,909,000 | 2,909,000 | 2,909,000 |
| Total Liabilities and SE | 6,748,000 | 6,748,000 | 6,748,000 |

**Balance sheet check:** 6,748,000 = 3,839,000 + 2,909,000 ✓
**Gross margin %:** 29.1%
**Action:** No change

---

**Analysis complete for FL.** Corrections needed for FY2021 (revenue restatement + NCI Net Profit) and FY2022 (NCI Net Profit). Run `/create-verified-dolt-db-financials-sql FL` to generate SQL.
