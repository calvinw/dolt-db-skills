# CVS (CVS) — FY2018–FY2024 Financial Analysis

**Generated:** 2026-06-06
**Source:** /verify-dolt-db-financials skill

---

## Company Info

- **Company name in DB:** CVS
- **CIK:** 64803
- **Display name:** CVS
- **Ticker:** CVS
- **Fiscal year end:** December 31
- **Sector:** Health/pharmacy retailer (also PBM and insurance via Aetna)

---

## Per-Year Summary Table

| Year | reportDate | Dolt Action Needed |
|------|------------|--------------------|
| 2018 | 2018-12-31 | OK — no changes needed |
| 2019 | 2019-12-31 | UPDATE — Current Assets, Liabilities, Total SE are wrong |
| 2020 | 2020-12-31 | OK — no changes needed |
| 2021 | 2021-12-31 | OK — no changes needed |
| 2022 | 2022-12-31 | REVIEW — Net Profit discrepancy (restatement); other fields match |
| 2023 | 2023-12-31 | OK — no changes needed |
| 2024 | 2024-12-31 | OK — no changes needed |

---

## Notes on CVS Financial Statement Structure

CVS is a highly complex company with three major segments:
1. **Health Services** (formerly Pharmacy Services / Caremark PBM)
2. **Health Care Benefits** (Aetna insurance, acquired Nov 2018)
3. **Pharmacy & Consumer Wellness** (formerly Retail/LTC)

**SGA note:** CVS labels its SGA as "Operating expenses" on the income statement, using XBRL tags `us-gaap_OtherCostAndExpenseOperating` or `cvs_OperatingExpensesExcluding...`. This is consistently used across all years and excludes: goodwill impairments, store impairments, restructuring charges, opioid litigation charges, and loss on assets held for sale. This is the correct SGA figure throughout.

**COGS note:** CVS's COGS (`us-gaap_CostOfGoodsAndServicesSold`) includes pharmacy dispensing costs and PBM drug costs but NOT insurance benefit costs. The health care costs line (`us-gaap_PolicyholderBenefitsAndClaimsIncurredHealthCare`) is a separate line item. CVS reports COGS and health care costs separately on the income statement. The Dolt DB uses the COGS line as "Cost of Goods" which is appropriate.

**Gross margin benchmark:** With pharmacy/PBM dominating, CVS's gross margin (Revenue - COGS only, not including health care costs) is in the 13–17% range, which is consistent with a pharmacy-heavy business. [NOTE: This understates true economics since health care costs are also a cost of revenue — total cost including health care costs would give a much lower "true" margin.]

---

## FY2018 Analysis

### Data Sources

| Field | SEC 10-K | Yahoo Finance | Dolt (current) | Recommended |
|-------|----------|---------------|-----------------|-------------|
| reportDate | 2018-12-31 | — | 2018-12-31 | 2018-12-31 |
| Net Revenue | 194,579,000 | — | 194,579,000 | 194,579,000 |
| Cost of Goods | 156,447,000 | — | 156,447,000 | 156,447,000 |
| Gross Margin | 38,132,000 | — | 38,132,000 | 38,132,000 |
| SGA | 21,368,000 | — | 21,368,000 | 21,368,000 |
| Operating Profit | 4,021,000 | — | 4,021,000 | 4,021,000 |
| Net Profit | -594,000 | — | -594,000 | -594,000 |
| Inventory | 16,450,000 | — | 16,450,000 | 16,450,000 |
| Current Assets | 45,243,000 | — | 45,243,000 | 45,243,000 |
| Total Assets | 196,456,000 | — | 196,456,000 | 196,456,000 |
| Current Liabilities | 44,009,000 | — | 44,009,000 | 44,009,000 |
| Liabilities | 137,913,000 | — | 137,913,000 | 137,913,000 |
| Total SE | 58,543,000 | — | 58,543,000 | 58,543,000 |
| Total L&SE | 196,456,000 | — | 196,456,000 | 196,456,000 |

### Anomaly Checks

- Balance sheet check: 137,913 + 58,543 = 196,456 = Total Assets. [OK]
- Gross margin %: 38,132 / 194,579 = 19.6% — within expected range for CVS [OK]
- Net Profit is negative (-594M) due to the $6,149M goodwill impairment charge in the Retail/LTC segment. The SGA of 21,368M correctly excludes this impairment. [NOTE: 2018 was the year CVS acquired Aetna (closed Nov 2018)]
- SGA source: `us-gaap_OtherCostAndExpenseOperating` = 21,368M. Correctly excludes goodwill impairment of 6,149M.

### Reconciled Recommendation

**Action: No changes needed.** All Dolt values match SEC 10-K exactly.

---

## FY2019 Analysis

### Data Sources

| Field | SEC 10-K | Yahoo Finance | Dolt (current) | Recommended |
|-------|----------|---------------|-----------------|-------------|
| reportDate | 2019-12-31 | — | 2019-12-31 | 2019-12-31 |
| Net Revenue | 256,776,000 | — | 256,776,000 | 256,776,000 |
| Cost of Goods | 158,719,000 | — | 158,719,000 | 158,719,000 |
| Gross Margin | 98,057,000 | — | 98,057,000 | 98,057,000 |
| SGA | 33,541,000 | — | 33,541,000 | 33,541,000 |
| Operating Profit | 11,987,000 | — | 11,987,000 | 11,987,000 |
| Net Profit | 6,634,000 | — | 6,634,000 | 6,634,000 |
| Inventory | 17,516,000 | — | 17,516,000 | 17,516,000 |
| Current Assets | **50,302,000** | — | **45,195,000** * | **50,302,000** |
| Total Assets | 222,449,000 | — | 222,449,000 | 222,449,000 |
| Current Liabilities | **53,303,000** | — | **45,762,000** * | **53,303,000** |
| Liabilities | **158,279,000** | — | **163,728,000** * | **158,279,000** |
| Total SE | **64,170,000** | — | **58,721,000** * | **64,170,000** |
| Total L&SE | 222,449,000 | — | 222,449,000 | 222,449,000 |

*Fields marked with asterisk differ from SEC; `*` = discrepancy

### Anomaly Checks

- Balance sheet check (SEC): 158,279 + 64,170 = 222,449 = Total Assets. [OK]
- Balance sheet check (Dolt): 163,728 + 58,721 = 222,449 = Total Assets. [Dolt adds up but values are wrong]
- [WARNING] Dolt Current Assets (45,195M) does not match SEC (50,302M). The Dolt value is very close to the 2018 Current Assets (45,243M), suggesting the balance sheet data may have been pulled from the wrong column.
- [WARNING] Dolt Current Liabilities (45,762M) does not match SEC (53,303M). The Dolt value is very close to the 2018 Current Liabilities (44,009M).
- [WARNING] Dolt Liabilities (163,728M) does not match SEC (158,279M). SEC Total Liabilities per balance sheet = 158,279M.
- [WARNING] Dolt Total SE (58,721M) does not match SEC (64,170M). SEC Total SE (including minority interest) = 64,170M (StockholdersEquity=63,864M + MinorityInterest=306M).
- Income statement values (Revenue, COGS, SGA, Operating Profit, Net Profit, Inventory) all match correctly.
- Gross margin %: 98,057 / 256,776 = 38.2% — [WARNING] This is unusually HIGH for CVS pharmacy operations. The large increase from 2018 (19.6%) is explained by the Aetna acquisition: starting 2019, the Aetna health care costs (~$52.5B) appear as a SEPARATE line ("Benefit costs") rather than in COGS. The 2019 "COGS" line (158,719M) excludes benefit costs, making gross margin appear higher. This is a presentation/structural change, not an error.
- SGA source: `us-gaap_OperatingExpenses` = 33,541M. This correctly excludes goodwill impairments (0 in 2019).

### Reconciled Recommendation

**Action: UPDATE required.** The balance sheet fields (Current Assets, Current Liabilities, Liabilities, Total SE) in Dolt appear to have been sourced from the wrong year or wrong column. Income statement and Total Assets/Total L&SE are correct.

Correct values from SEC 2019 10-K:
- Current Assets: **50,302,000**
- Current Liabilities: **53,303,000**
- Liabilities: **158,279,000**
- Total SE: **64,170,000**
- Total L&SE: **222,449,000** (already correct)

---

## FY2020 Analysis

### Data Sources

| Field | SEC 10-K | Yahoo Finance | Dolt (current) | Recommended |
|-------|----------|---------------|-----------------|-------------|
| reportDate | 2020-12-31 | — | 2020-12-31 | 2020-12-31 |
| Net Revenue | 268,706,000 | — | 268,706,000 | 268,706,000 |
| Cost of Goods | 163,981,000 | — | 163,981,000 | 163,981,000 |
| Gross Margin | 104,725,000 | — | 104,725,000 | 104,725,000 |
| SGA | 35,135,000 | — | 35,135,000 | 35,135,000 |
| Operating Profit | 13,911,000 | — | 13,911,000 | 13,911,000 |
| Net Profit | 7,192,000 | — | 7,192,000 | 7,192,000 |
| Inventory | 18,496,000 | — | 18,496,000 | 18,496,000 |
| Current Assets | 56,369,000 | — | 56,369,000 | 56,369,000 |
| Total Assets | 230,715,000 | — | 230,715,000 | 230,715,000 |
| Current Liabilities | 62,017,000 | — | 62,017,000 | 62,017,000 |
| Liabilities | 161,014,000 | — | 161,014,000 | 161,014,000 |
| Total SE | 69,701,000 | — | 69,701,000 | 69,701,000 |
| Total L&SE | 230,715,000 | — | 230,715,000 | 230,715,000 |

### Anomaly Checks

- Balance sheet check: 161,014 + 69,701 = 230,715 = Total Assets. [OK]
- Gross margin %: 104,725 / 268,706 = 39.0% — same structural explanation as 2019 (benefit costs separate from COGS). [OK given structure]
- Net Profit (7,192M) verified: ProfitLoss = 7,192M (CVS Shareholders = 7,179M + NCI 13M = 7,192M). Dolt has 7,192M. [OK]
- SGA source: `cvs_OperatingExpensesExcludingGoodwillImpairments` = 35,135M. Correctly excludes goodwill impairments (0 in 2020).

### Reconciled Recommendation

**Action: No changes needed.** All Dolt values match SEC 10-K exactly.

---

## FY2021 Analysis

### Data Sources

| Field | SEC 10-K | Yahoo Finance | Dolt (current) | Recommended |
|-------|----------|---------------|-----------------|-------------|
| reportDate | 2021-12-31 | — | 2021-12-31 | 2021-12-31 |
| Net Revenue | 292,111,000 | — | 292,111,000 | 292,111,000 |
| Cost of Goods | 175,803,000 | — | 175,803,000 | 175,803,000 |
| Gross Margin | 116,308,000 | — | 116,308,000 | 116,308,000 |
| SGA | 37,066,000 | — | 37,066,000 | 37,066,000 |
| Operating Profit | 13,193,000 | — | 13,193,000 | 13,193,000 |
| Net Profit | 7,910,000 | — | 7,910,000 | 7,910,000 |
| Inventory | 17,760,000 | — | 17,760,000 | 17,760,000 |
| Current Assets | 60,008,000 | — | 60,008,000 | 60,008,000 |
| Total Assets | 232,999,000 | — | 232,999,000 | 232,999,000 |
| Current Liabilities | 67,807,000 | — | 67,807,000 | 67,807,000 |
| Liabilities | 157,618,000 | — | 157,618,000 | 157,618,000 |
| Total SE | 75,381,000 | — | 75,381,000 | 75,381,000 |
| Total L&SE | 232,999,000 | — | 232,999,000 | 232,999,000 |

### Anomaly Checks

- Balance sheet check: 157,618 + 75,381 = 232,999 = Total Assets. [OK]
- Gross margin %: 116,308 / 292,111 = 39.8% — consistent with post-Aetna structure. [OK given structure]
- SGA source: `cvs_OperatingExpensesExcludingStoreImpairmentsAndGoodwillImpairments` = 37,066M. Correctly excludes store impairments (1,358M), goodwill impairment (431M) from 2021.
- Net Profit: 7,910M verified — matches NetIncomeLoss in filing. [OK]
- Note: 2021 had $1,358M store impairments and $431M goodwill impairment in Retail/LTC segment — correctly excluded from SGA.

### Reconciled Recommendation

**Action: No changes needed.** All Dolt values match SEC 10-K exactly.

---

## FY2022 Analysis

### Data Sources

| Field | SEC 10-K (2022 filing) | SEC 10-K (2023 restated) | Yahoo Finance | Dolt (current) | Recommended |
|-------|------------------------|--------------------------|---------------|-----------------|-------------|
| reportDate | 2022-12-31 | 2022-12-31 | 2022-12-31 | 2022-12-31 | 2022-12-31 |
| Net Revenue | 322,467,000 | 322,467,000 | 322,467,000 | 322,467,000 | 322,467,000 |
| Cost of Goods | 196,892,000 | 196,892,000 | 267,965,000 * | 196,892,000 | 196,892,000 |
| Gross Margin | 125,575,000 | 125,575,000 | 54,502,000 * | 125,575,000 | 125,575,000 |
| SGA | 38,212,000 | 38,212,000 | 38,212,000 | 38,212,000 | 38,212,000 |
| Operating Profit | 7,746,000 | 7,954,000 * | 7,954,000 | 7,746,000 * | **7,954,000** |
| Net Profit | 4,149,000 | 4,311,000 * | 4,311,000 | 4,165,000 * | **4,311,000** |
| Inventory | 19,090,000 | 19,090,000 | 19,090,000 | 19,090,000 | 19,090,000 |
| Current Assets | 65,682,000 | 65,682,000 | 65,633,000 ~ | 65,682,000 | 65,682,000 |
| Total Assets | 228,275,000 | 228,275,000 | 228,275,000 | 228,275,000 | 228,275,000 |
| Current Liabilities | 69,736,000 | 69,736,000 | 69,421,000 ~ | 69,736,000 | 69,736,000 |
| Liabilities | 156,960,000 | 156,960,000 | 156,960,000 | 156,960,000 | 156,960,000 |
| Total SE | 71,315,000 | 71,315,000 | 71,469,000 ~ | 71,315,000 | 71,315,000 |
| Total L&SE | 228,275,000 | 228,275,000 | 228,275,000 | 228,275,000 | 228,275,000 |

`*` = differs; `~` = minor difference (Yahoo rounding)

### Anomaly Checks

- Balance sheet check: 156,960 + 71,315 = 228,275 = Total Assets. [OK]
- Gross margin %: 125,575 / 322,467 = 38.9%. Consistent with prior years. [OK]
- [WARNING] Yahoo Cost of Goods (267,965M) appears to include health care benefit costs (71,281M) in addition to COGS (196,892M) — do NOT use Yahoo for COGS or Gross Margin for CVS.
- [WARNING] **Restatement detected**: The 2023 10-K restated 2022 figures due to adoption of a new accounting standard (ASU). Changes:
  - Operating Profit: 7,746M (original) → 7,954M (restated, +208M)
  - Net Income: 4,149M (original) → 4,311M (restated, +162M)
  - Benefit costs also restated downward by 208M in 2022
- Dolt has Operating Profit = 7,746M (original filing value) and Net Profit = 4,165M (unclear source — not matching either original 4,149M or restated 4,311M; the 4,165M appears to be ProfitLoss total including NCI from the original 2022 filing).
- Per restatement rule: Use most recent filing → recommended values are the restated figures from the 2023 10-K.
- SGA: Both original and restated = 38,212M. [No change]

### Reconciled Recommendation

**Action: REVIEW — recommend updating to restated values.**

The 2023 10-K restated 2022 comparatives due to a new accounting standard adoption. The correct current values are:
- Operating Profit: **7,954,000** (restated; Dolt has 7,746,000)
- Net Profit: **4,311,000** (restated; Dolt has 4,165,000)

All other fields match. The balance sheet was not restated (same values in both filings).

---

## FY2023 Analysis

### Data Sources

| Field | SEC 10-K | Yahoo Finance | Dolt (current) | Recommended |
|-------|----------|---------------|-----------------|-------------|
| reportDate | 2023-12-31 | 2023-12-31 | 2023-12-31 | 2023-12-31 |
| Net Revenue | 357,776,000 | 357,776,000 | 357,776,000 | 357,776,000 |
| Cost of Goods | 217,098,000 | 303,345,000 * | 217,098,000 | 217,098,000 |
| Gross Margin | 140,678,000 | 54,431,000 * | 140,678,000 | 140,678,000 |
| SGA | 39,832,000 | 39,832,000 | 39,832,000 | 39,832,000 |
| Operating Profit | 13,743,000 | 13,743,000 | 13,743,000 | 13,743,000 |
| Net Profit | 8,344,000 | 8,344,000 | 8,344,000 | 8,344,000 |
| Inventory | 18,025,000 | 18,025,000 | 18,025,000 | 18,025,000 |
| Current Assets | 67,858,000 | 67,858,000 | 67,858,000 | 67,858,000 |
| Total Assets | 249,728,000 | 249,728,000 | 249,728,000 | 249,728,000 |
| Current Liabilities | 79,189,000 | 79,189,000 | 79,189,000 | 79,189,000 |
| Liabilities | 173,092,000 | 173,092,000 | 173,092,000 | 173,092,000 |
| Total SE | 76,636,000 | 76,636,000 | 76,636,000 | 76,636,000 |
| Total L&SE | 249,728,000 | 249,728,000 | 249,728,000 | 249,728,000 |

### Anomaly Checks

- Balance sheet check: 173,092 + 76,636 = 249,728 = Total Assets. [OK]
- Gross margin %: 140,678 / 357,776 = 39.3%. Consistent. [OK]
- [WARNING] Yahoo COGS (303,345M) includes health care costs — do NOT use Yahoo COGS for CVS.
- SGA source: `us-gaap_OtherCostAndExpenseOperating` = 39,832M. Excludes restructuring charges (507M), goodwill impairment (0), store impairment (0), opioid litigation (0), loss on assets held for sale (349M). [OK]
- 2023 10-K includes "Loss on assets held for sale" = 349M related to Omnicare LTC business divestiture — correctly excluded from SGA.

### Reconciled Recommendation

**Action: No changes needed.** All Dolt values match SEC 10-K exactly.

---

## FY2024 Analysis

### Data Sources

| Field | SEC 10-K | Yahoo Finance | Dolt (current) | Recommended |
|-------|----------|---------------|-----------------|-------------|
| reportDate | 2024-12-31 | 2024-12-31 | 2024-12-31 | 2024-12-31 |
| Net Revenue | 372,809,000 | 372,809,000 | 372,809,000 | 372,809,000 |
| Cost of Goods | 206,287,000 | 321,408,000 * | 206,287,000 | 206,287,000 |
| Gross Margin | 166,522,000 | 51,401,000 * | 166,522,000 | 166,522,000 |
| SGA | 41,606,000 | 41,706,000 ~ | 41,606,000 | 41,606,000 |
| Operating Profit | 8,516,000 | 9,695,000 * | 8,516,000 | 8,516,000 |
| Net Profit | 4,614,000 | 4,614,000 | 4,614,000 | 4,614,000 |
| Inventory | 18,107,000 | 18,107,000 | 18,107,000 | 18,107,000 |
| Current Assets | 68,645,000 | 68,645,000 | 68,645,000 | 68,645,000 |
| Total Assets | 253,215,000 | 253,215,000 | 253,215,000 | 253,215,000 |
| Current Liabilities | 84,609,000 | 84,609,000 | 84,609,000 | 84,609,000 |
| Liabilities | 177,485,000 | 177,485,000 | 177,485,000 | 177,485,000 |
| Total SE | 75,730,000 | 75,560,000 ~ | 75,730,000 | 75,730,000 |
| Total L&SE | 253,215,000 | 253,215,000 | 253,215,000 | 253,215,000 |

`*` = differs significantly; `~` = minor rounding difference

### Anomaly Checks

- Balance sheet check: 177,485 + 75,730 = 253,215 = Total Assets. [OK]
- Gross margin %: 166,522 / 372,809 = 44.7% — [NOTE] Higher than prior years due to structural change: In 2024, CVS restructured segments. The COGS line (206,287M) is lower relative to revenue (372,809M) partly because more costs shifted to the "health care costs" line (115,121M). This is a presentation change, not an error.
- [WARNING] Yahoo COGS (321,408M) clearly includes health care costs — do NOT use Yahoo COGS for CVS in any year.
- [WARNING] Yahoo Operating Profit (9,695M) differs from SEC (8,516M). The SEC value includes restructuring charges (-1,179M) and goodwill impairment. Yahoo appears to use a "Total Operating Income As Reported" that may differ. Use SEC value.
- SGA source: `us-gaap_OtherCostAndExpenseOperating` = 41,606M. Excludes restructuring charges (1,179M). [OK]
- 2024 had significant restructuring ($1,179M) and a large goodwill impairment ($5,725M per Yahoo data) — these are correctly excluded from SGA and Operating Profit via the reported SEC operating income line.
- Yahoo SE (75,560M) = Common Stock Equity only; Dolt correctly uses total including minority interest (75,730M). [OK]

### Reconciled Recommendation

**Action: No changes needed.** All Dolt values match SEC 10-K exactly.

---

## Overall Summary

### Fields Requiring Updates

| Year | Field | Current Dolt Value | Recommended Value | Source |
|------|-------|-------------------|-------------------|--------|
| 2019 | Current Assets | 45,195,000 | 50,302,000 | SEC 2019 10-K |
| 2019 | Current Liabilities | 45,762,000 | 53,303,000 | SEC 2019 10-K |
| 2019 | Liabilities | 163,728,000 | 158,279,000 | SEC 2019 10-K |
| 2019 | Total SE | 58,721,000 | 64,170,000 | SEC 2019 10-K |
| 2022 | Operating Profit | 7,746,000 | 7,954,000 | SEC 2023 10-K (restated) |
| 2022 | Net Profit | 4,165,000 | 4,311,000 | SEC 2023 10-K (restated) |

### Fields Confirmed Correct (No Changes)

All other fields for 2018, 2019 (income stmt), 2020, 2021, 2023, 2024 match SEC exactly.

### Persistent Warnings

1. **Yahoo COGS for CVS**: Yahoo Finance systematically includes health care benefit costs in its Cost of Revenue figure for CVS, making COGS appear much higher (~$100B–$115B more) and gross margin appear much lower than the SEC-reported figures. **Never use Yahoo COGS or Gross Margin for CVS.**
2. **2022 restatement**: The 2022 Operating Profit and Net Profit were restated in the 2023 10-K due to a new accounting standard adoption. Updated Dolt to use most recent (restated) values is recommended.
3. **2019 balance sheet errors**: The Dolt balance sheet fields for 2019 appear to have been pulled from an incorrect source (possibly the 2018 ending balance sheet). Income statement fields for 2019 are correct.

---

**Analysis complete.** Run `/insert-financials CVS` to write all changed years to the database.

**Unresolved flags:**
- 2019: Balance sheet fields (Current Assets, Current Liabilities, Liabilities, Total SE) need correction
- 2022: Operating Profit and Net Profit need update to restated values from 2023 10-K
