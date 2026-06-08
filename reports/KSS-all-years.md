# Kohl's (KSS) — FY2018–FY2024 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2018 | 2019-02-02 | No change |
| 2019 | 2020-02-01 | [ANOMALY] Income statement formula inconsistency — SEC verification needed |
| 2020 | 2021-01-30 | [ANOMALY] Income statement formula inconsistency — SEC verification needed |
| 2021 | 2022-01-29 | [ANOMALY] Income statement formula inconsistency — SEC verification needed |
| 2022 | 2023-01-28 | No change |
| 2023 | 2024-02-03 | No change |
| 2024 | 2025-02-01 | No change |

---

## Notes

- **Kohl's fiscal year** ends in late January/early February. DB year label corresponds to the fiscal year ending in that label's following Jan/Feb.
- **SGA treatment:** Kohl's reports SGA and D&A as separate lines on the income statement. Yahoo confirms for FY2022–FY2024 that SGA excludes D&A. COGS includes buying, occupancy (operating lease cost), and distribution costs.
- **Yahoo Finance coverage:** FY2022–FY2024 fully confirmed. FY2021 (column 2022-01-31) is NaN for income statement items. FY2018–FY2021 not available from Yahoo.
- **ASC 842 adoption (FY2019):** Total Assets jumped from 12,469,000K (FY2018) to 14,555,000K (FY2019); Liabilities jumped from 6,942,000K to 9,105,000K. ROU assets added ~2.1B. All balance sheet identities remain satisfied.
- **[ANOMALY] Income statement formula inconsistency FY2019–FY2021:** For FY2022–FY2024, the formula GM − SGA − D&A = Operating Profit holds exactly (Yahoo confirms D&A ~743–808K for those years). Applying the same formula to FY2019–FY2021 yields impossible negative implied D&A values (FY2021: −124K; FY2020: −88K; FY2019: −59K). FY2018 gives plausible D&A of 1,068K (pre-ASC 842). This indicates one or more income statement values are incorrect for FY2019–FY2021. Possible causes: COGS overstated, SGA overstated, or Operating Profit overstated. **SEC 10-K verification required for all income statement fields (Revenue, COGS, SGA, Operating Profit) for FY2019–FY2021 before corrections can be recommended.**
- **Gross margins:** FY2018 39.7%, FY2019 35.7%, FY2020 31.1% (COVID), FY2021 38.1%, FY2022 36.7%, FY2023 39.9%, FY2024 40.5%. Reasonable range for a department store.
- **Operating margins FY2023–FY2024:** 4.1% and 2.7% — consistent with department store sector under pressure from off-price competition.

---

## FY2018

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 20,229,000 | 20,229,000 |
| Cost of Goods | N/A | 12,199,000 | 12,199,000 |
| Gross Margin | N/A | 8,030,000 | 8,030,000 |
| SGA | N/A | 5,601,000 | 5,601,000 |
| Operating Profit | N/A | 1,361,000 | 1,361,000 |
| Net Profit | N/A | 801,000 | 801,000 |
| Inventory | N/A | 3,475,000 | 3,475,000 |
| Current Assets | N/A | 4,835,000 | 4,835,000 |
| Total Assets | N/A | 12,469,000 | 12,469,000 |
| Current Liabilities | N/A | 2,730,000 | 2,730,000 |
| Liabilities | N/A | 6,942,000 | 6,942,000 |
| Total Shareholder Equity | N/A | 5,527,000 | 5,527,000 |
| Total Liabilities and SE | N/A | 12,469,000 | 12,469,000 |

**Balance sheet check:** 12,469,000 = 6,942,000 + 5,527,000 ✓
**Gross margin %:** 39.7%
**Implied D&A:** 8,030 − 5,601 − 1,361 = 1,068K (plausible for pre-ASC 842)
**Action:** No change

---

## FY2019

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 18,885,000 | ❓ SEC needed |
| Cost of Goods | N/A | 12,140,000 | ❓ SEC needed |
| Gross Margin | N/A | 6,745,000 | ❓ SEC needed |
| SGA | N/A | 5,705,000 | ❓ SEC needed |
| Operating Profit | N/A | 1,099,000 | ❓ SEC needed |
| Net Profit | N/A | 691,000 | ❓ SEC needed |
| Inventory | N/A | 3,537,000 | 3,537,000 |
| Current Assets | N/A | 4,649,000 | 4,649,000 |
| Total Assets | N/A | 14,555,000 | 14,555,000 |
| Current Liabilities | N/A | 2,769,000 | 2,769,000 |
| Liabilities | N/A | 9,105,000 | 9,105,000 |
| Total Shareholder Equity | N/A | 5,450,000 | 5,450,000 |
| Total Liabilities and SE | N/A | 14,555,000 | 14,555,000 |

**Balance sheet check:** 14,555,000 = 9,105,000 + 5,450,000 ✓
**[INFO] Total Assets jump (+2.1B) due to ASC 842 adoption.**
**Implied D&A:** 6,745 − 5,705 − 1,099 = **−59K (IMPOSSIBLE — anomaly)**
**Action: [ANOMALY] Income statement values require SEC verification. Balance sheet accepted as correct.**

---

## FY2020

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 15,031,000 | ❓ SEC needed |
| Cost of Goods | N/A | 10,360,000 | ❓ SEC needed |
| Gross Margin | N/A | 4,671,000 | ❓ SEC needed |
| SGA | N/A | 5,021,000 | ❓ SEC needed |
| Operating Profit | N/A | -262,000 | ❓ SEC needed |
| Net Profit | N/A | -163,000 | ❓ SEC needed |
| Inventory | N/A | 2,590,000 | 2,590,000 |
| Current Assets | N/A | 5,835,000 | 5,835,000 |
| Total Assets | N/A | 15,337,000 | 15,337,000 |
| Current Liabilities | N/A | 3,022,000 | 3,022,000 |
| Liabilities | N/A | 10,141,000 | 10,141,000 |
| Total Shareholder Equity | N/A | 5,196,000 | 5,196,000 |
| Total Liabilities and SE | N/A | 15,337,000 | 15,337,000 |

**Balance sheet check:** 15,337,000 = 10,141,000 + 5,196,000 ✓
**Implied D&A:** 4,671 − 5,021 − (−262) = **−88K (IMPOSSIBLE — anomaly)**
**Action: [ANOMALY] Income statement values require SEC verification. Balance sheet accepted as correct.**

---

## FY2021

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 18,471,000 | ❓ SEC needed |
| Cost of Goods | N/A | 11,437,000 | ❓ SEC needed |
| Gross Margin | N/A | 7,034,000 | ❓ SEC needed |
| SGA | N/A | 5,478,000 | ❓ SEC needed |
| Operating Profit | N/A | 1,680,000 | ❓ SEC needed |
| Net Profit | N/A | 938,000 | ❓ SEC needed |
| Inventory | N/A | 3,067,000 | 3,067,000 |
| Current Assets | N/A | 5,023,000 | 5,023,000 |
| Total Assets | N/A | 15,054,000 | 15,054,000 |
| Current Liabilities | N/A | 3,286,000 | 3,286,000 |
| Liabilities | N/A | 10,393,000 | 10,393,000 |
| Total Shareholder Equity | N/A | 4,661,000 | 4,661,000 |
| Total Liabilities and SE | N/A | 15,054,000 | 15,054,000 |

**Balance sheet check:** 15,054,000 = 10,393,000 + 4,661,000 ✓
**Implied D&A:** 7,034 − 5,478 − 1,680 = **−124K (IMPOSSIBLE — anomaly)**
**Action: [ANOMALY] Income statement values require SEC verification. Balance sheet accepted as correct.**

---

## FY2022

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | 18,098,000 | 18,098,000 | 18,098,000 |
| Cost of Goods | 11,457,000 | 11,457,000 | 11,457,000 |
| Gross Margin | 6,641,000 | 6,641,000 | 6,641,000 |
| SGA | 5,587,000 | 5,587,000 | 5,587,000 |
| Operating Profit | 246,000 | 246,000 | 246,000 |
| Net Profit | -19,000 | -19,000 | -19,000 |
| Inventory | 3,189,000 | 3,189,000 | 3,189,000 |
| Current Assets | 3,736,000 | 3,736,000 | 3,736,000 |
| Total Assets | 14,345,000 | 14,345,000 | 14,345,000 |
| Current Liabilities | 3,115,000 | 3,115,000 | 3,115,000 |
| Liabilities | 10,582,000 | 10,582,000 | 10,582,000 |
| Total Shareholder Equity | 3,763,000 | 3,763,000 | 3,763,000 |
| Total Liabilities and SE | 14,345,000 | 14,345,000 | 14,345,000 |

**Balance sheet check:** 14,345,000 = 10,582,000 + 3,763,000 ✓
**Yahoo D&A (confirmed):** 808,000K; formula: 6,641 − 5,587 − 808 = 246 ✓
**Action:** No change

---

## FY2023

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | 17,476,000 | 17,476,000 | 17,476,000 |
| Cost of Goods | 10,498,000 | 10,498,000 | 10,498,000 |
| Gross Margin | 6,978,000 | 6,978,000 | 6,978,000 |
| SGA | 5,512,000 | 5,512,000 | 5,512,000 |
| Operating Profit | 717,000 | 717,000 | 717,000 |
| Net Profit | 317,000 | 317,000 | 317,000 |
| Inventory | 2,880,000 | 2,880,000 | 2,880,000 |
| Current Assets | 3,410,000 | 3,410,000 | 3,410,000 |
| Total Assets | 14,009,000 | 14,009,000 | 14,009,000 |
| Current Liabilities | 2,612,000 | 2,612,000 | 2,612,000 |
| Liabilities | 10,116,000 | 10,116,000 | 10,116,000 |
| Total Shareholder Equity | 3,893,000 | 3,893,000 | 3,893,000 |
| Total Liabilities and SE | 14,009,000 | 14,009,000 | 14,009,000 |

**Balance sheet check:** 14,009,000 = 10,116,000 + 3,893,000 ✓
**Yahoo D&A (confirmed):** 749,000K; formula: 6,978 − 5,512 − 749 = 717 ✓
**Action:** No change

---

## FY2024

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | 16,221,000 | 16,221,000 | 16,221,000 |
| Cost of Goods | 9,661,000 | 9,661,000 | 9,661,000 |
| Gross Margin | 6,560,000 | 6,560,000 | 6,560,000 |
| SGA | 5,308,000 | 5,308,000 | 5,308,000 |
| Operating Profit | 433,000* | 433,000 | 433,000 |
| Net Profit | 109,000 | 109,000 | 109,000 |
| Inventory | 2,945,000 | 2,945,000 | 2,945,000 |
| Current Assets | 3,388,000 | 3,388,000 | 3,388,000 |
| Total Assets | 13,559,000 | 13,559,000 | 13,559,000 |
| Current Liabilities | 3,131,000 | 3,131,000 | 3,131,000 |
| Liabilities | 9,757,000 | 9,757,000 | 9,757,000 |
| Total Shareholder Equity | 3,802,000 | 3,802,000 | 3,802,000 |
| Total Liabilities and SE | 13,559,000 | 13,559,000 | 13,559,000 |

*Yahoo "Operating Income" = 509,000K (normalized, excl. special items); "Total Operating Income As Reported" = 433,000K ✓ (Dolt uses as-reported). Special charges: −76K (restructuring + impairment).

**Balance sheet check:** 13,559,000 = 9,757,000 + 3,802,000 ✓
**Yahoo D&A (confirmed):** 743,000K; formula: 6,560 − 5,308 − 743 − 76 = 433 ✓
**Action:** No change

---

**Analysis complete for KSS.** FY2022–FY2024 verified correct by Yahoo. FY2019–FY2021 have income statement anomaly (impossible implied D&A) requiring SEC 10-K verification. Balance sheet identities satisfied for all 7 years. No corrections applied pending SEC review.
