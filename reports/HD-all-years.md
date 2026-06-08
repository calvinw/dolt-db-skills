# Home Depot (HD) — FY2018–FY2024 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2018 | 2019-02-03 | No change |
| 2019 | 2020-02-02 | No change |
| 2020 | 2021-01-31 | No change |
| 2021 | 2022-01-30 | No change |
| 2022 | 2023-01-29 | No change |
| 2023 | 2024-01-28 | No change |
| 2024 | 2025-02-02 | No change |

---

## Notes

- **Home Depot fiscal year** ends on the Sunday nearest January 31. DB year label corresponds to the fiscal year ending in the following January/February.
- **SGA treatment:** HD reports SGA (Selling, General and Administrative) separately from D&A. The Dolt SGA values are SGA only (D&A excluded). D&A is an additional line between SGA and Operating Income: Operating Income = Gross Margin − SGA − D&A. This is consistent across all 7 years (implicit D&A ranges from ~2.1B FY2018 to ~3.0B FY2024, confirmed by Yahoo FY2022–FY2024).
- **Gross margins 33–34%:** Extremely consistent with Home Improvement benchmark (30–35%). Expected.
- **[INFO] Negative/near-zero TSE in FY2018, FY2019, FY2021:** Due to HD's aggressive share buyback program and dividends paid in excess of net income. TSE ranges from −3.1B to +3.3B. Balance sheet identities hold in all cases.
- **FY2024 Total Assets jump:** 76,530K (FY2023) → 96,119K (FY2024) — driven by HD's ~$18.25B acquisition of SRS Distribution (completed June 2024), adding ~16B in goodwill and intangibles.
- **Yahoo Finance coverage:** Available for FY2022–FY2024 only (FY2018–FY2021 return NaN for FY2021 and are not in the 4-year history for earlier years). FY2022–FY2024 confirmed against Yahoo. FY2018–FY2021 verified by internal consistency (balance sheet identity, SGA formula, gross margin trends).

---

## FY2018

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 108,203,000 | 108,203,000 |
| Cost of Goods | N/A | 71,043,000 | 71,043,000 |
| Gross Margin | N/A | 37,160,000 | 37,160,000 |
| SGA | N/A | 19,513,000 | 19,513,000 |
| Operating Profit | N/A | 15,530,000 | 15,530,000 |
| Net Profit | N/A | 11,121,000 | 11,121,000 |
| Inventory | N/A | 13,925,000 | 13,925,000 |
| Current Assets | N/A | 18,529,000 | 18,529,000 |
| Total Assets | N/A | 44,003,000 | 44,003,000 |
| Current Liabilities | N/A | 16,716,000 | 16,716,000 |
| Liabilities | N/A | 45,881,000 | 45,881,000 |
| Total Shareholder Equity | N/A | -1,878,000 | -1,878,000 |
| Total Liabilities and SE | N/A | 44,003,000 | 44,003,000 |

**Balance sheet check:** 44,003,000 = 45,881,000 + (−1,878,000) ✓
**Gross margin %:** 34.3%
**Implied D&A:** 37,160 − 19,513 − 15,530 = 2,117K
**Action:** No change

---

## FY2019

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 110,225,000 | 110,225,000 |
| Cost of Goods | N/A | 72,653,000 | 72,653,000 |
| Gross Margin | N/A | 37,572,000 | 37,572,000 |
| SGA | N/A | 19,740,000 | 19,740,000 |
| Operating Profit | N/A | 15,843,000 | 15,843,000 |
| Net Profit | N/A | 11,242,000 | 11,242,000 |
| Inventory | N/A | 14,531,000 | 14,531,000 |
| Current Assets | N/A | 19,810,000 | 19,810,000 |
| Total Assets | N/A | 51,236,000 | 51,236,000 |
| Current Liabilities | N/A | 18,375,000 | 18,375,000 |
| Liabilities | N/A | 54,352,000 | 54,352,000 |
| Total Shareholder Equity | N/A | -3,116,000 | -3,116,000 |
| Total Liabilities and SE | N/A | 51,236,000 | 51,236,000 |

**Balance sheet check:** 51,236,000 = 54,352,000 + (−3,116,000) ✓
**Gross margin %:** 34.1%
**Implied D&A:** 37,572 − 19,740 − 15,843 = 1,989K
**[INFO] Total Assets jump from FY2018 (44,003K) due to ASC 842 adoption (operating lease ROU assets added ~7B). Expected.**
**Action:** No change

---

## FY2020

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 132,110,000 | 132,110,000 |
| Cost of Goods | N/A | 87,257,000 | 87,257,000 |
| Gross Margin | N/A | 44,853,000 | 44,853,000 |
| SGA | N/A | 24,447,000 | 24,447,000 |
| Operating Profit | N/A | 18,278,000 | 18,278,000 |
| Net Profit | N/A | 12,866,000 | 12,866,000 |
| Inventory | N/A | 16,627,000 | 16,627,000 |
| Current Assets | N/A | 28,477,000 | 28,477,000 |
| Total Assets | N/A | 70,581,000 | 70,581,000 |
| Current Liabilities | N/A | 23,166,000 | 23,166,000 |
| Liabilities | N/A | 67,282,000 | 67,282,000 |
| Total Shareholder Equity | N/A | 3,299,000 | 3,299,000 |
| Total Liabilities and SE | N/A | 70,581,000 | 70,581,000 |

**Balance sheet check:** 70,581,000 = 67,282,000 + 3,299,000 ✓
**Gross margin %:** 34.0%
**Implied D&A:** 44,853 − 24,447 − 18,278 = 2,128K
**Action:** No change

---

## FY2021

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 151,157,000 | 151,157,000 |
| Cost of Goods | N/A | 100,325,000 | 100,325,000 |
| Gross Margin | N/A | 50,832,000 | 50,832,000 |
| SGA | N/A | 25,406,000 | 25,406,000 |
| Operating Profit | N/A | 23,040,000 | 23,040,000 |
| Net Profit | N/A | 16,433,000 | 16,433,000 |
| Inventory | N/A | 22,068,000 | 22,068,000 |
| Current Assets | N/A | 29,055,000 | 29,055,000 |
| Total Assets | N/A | 71,876,000 | 71,876,000 |
| Current Liabilities | N/A | 28,693,000 | 28,693,000 |
| Liabilities | N/A | 73,572,000 | 73,572,000 |
| Total Shareholder Equity | N/A | -1,696,000 | -1,696,000 |
| Total Liabilities and SE | N/A | 71,876,000 | 71,876,000 |

**Balance sheet check:** 71,876,000 = 73,572,000 + (−1,696,000) ✓
**Gross margin %:** 33.6%
**Implied D&A:** 50,832 − 25,406 − 23,040 = 2,386K
**Action:** No change

---

## FY2022

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | 157,403,000 | 157,403,000 | 157,403,000 |
| Cost of Goods | 104,625,000 | 104,625,000 | 104,625,000 |
| Gross Margin | 52,778,000 | 52,778,000 | 52,778,000 |
| SGA | 26,284,000 | 26,284,000 | 26,284,000 |
| Operating Profit | 24,039,000 | 24,039,000 | 24,039,000 |
| Net Profit | 17,105,000 | 17,105,000 | 17,105,000 |
| Inventory | 24,886,000 | 24,886,000 | 24,886,000 |
| Current Assets | 32,471,000 | 32,471,000 | 32,471,000 |
| Total Assets | 76,445,000 | 76,445,000 | 76,445,000 |
| Current Liabilities | 23,110,000 | 23,110,000 | 23,110,000 |
| Liabilities | 74,883,000 | 74,883,000 | 74,883,000 |
| Total Shareholder Equity | 1,562,000 | 1,562,000 | 1,562,000 |
| Total Liabilities and SE | 76,445,000 | 76,445,000 | 76,445,000 |

**Balance sheet check:** 76,445,000 = 74,883,000 + 1,562,000 ✓
**Gross margin %:** 33.5%
**Yahoo D&A (confirmed):** 2,455,000K
**Action:** No change

---

## FY2023

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | 152,669,000 | 152,669,000 | 152,669,000 |
| Cost of Goods | 101,709,000 | 101,709,000 | 101,709,000 |
| Gross Margin | 50,960,000 | 50,960,000 | 50,960,000 |
| SGA | 26,598,000 | 26,598,000 | 26,598,000 |
| Operating Profit | 21,689,000 | 21,689,000 | 21,689,000 |
| Net Profit | 15,143,000 | 15,143,000 | 15,143,000 |
| Inventory | 20,976,000 | 20,976,000 | 20,976,000 |
| Current Assets | 29,775,000 | 29,775,000 | 29,775,000 |
| Total Assets | 76,530,000 | 76,530,000 | 76,530,000 |
| Current Liabilities | 22,015,000 | 22,015,000 | 22,015,000 |
| Liabilities | 75,486,000 | 75,486,000 | 75,486,000 |
| Total Shareholder Equity | 1,044,000 | 1,044,000 | 1,044,000 |
| Total Liabilities and SE | 76,530,000 | 76,530,000 | 76,530,000 |

**Balance sheet check:** 76,530,000 = 75,486,000 + 1,044,000 ✓
**Gross margin %:** 33.4%
**Yahoo D&A (confirmed):** 2,673,000K
**Action:** No change

---

## FY2024

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | 159,514,000 | 159,514,000 | 159,514,000 |
| Cost of Goods | 106,206,000 | 106,206,000 | 106,206,000 |
| Gross Margin | 53,308,000 | 53,308,000 | 53,308,000 |
| SGA | 28,748,000 | 28,748,000 | 28,748,000 |
| Operating Profit | 21,526,000 | 21,526,000 | 21,526,000 |
| Net Profit | 14,806,000 | 14,806,000 | 14,806,000 |
| Inventory | 23,451,000 | 23,451,000 | 23,451,000 |
| Current Assets | 31,683,000 | 31,683,000 | 31,683,000 |
| Total Assets | 96,119,000 | 96,119,000 | 96,119,000 |
| Current Liabilities | 28,661,000 | 28,661,000 | 28,661,000 |
| Liabilities | 89,479,000 | 89,479,000 | 89,479,000 |
| Total Shareholder Equity | 6,640,000 | 6,640,000 | 6,640,000 |
| Total Liabilities and SE | 96,119,000 | 96,119,000 | 96,119,000 |

**Balance sheet check:** 96,119,000 = 89,479,000 + 6,640,000 ✓
**Gross margin %:** 33.4%
**Yahoo D&A (confirmed):** 3,034,000K
**[INFO] Total Assets jumped ~19.6B from FY2023 due to SRS Distribution acquisition (~$18.25B, closed June 2024). Goodwill+intangibles grew from 12.1B to 28.5B.**
**Action:** No change

---

**Analysis complete for HD.** All 7 years verified. No corrections needed. Data is clean across all fields.
