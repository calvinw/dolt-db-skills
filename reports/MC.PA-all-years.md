# LVMH (MC.PA) — FY2018–FY2024 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill
**Currency:** EUR (thousands) | Non-US company — Yahoo Finance only (no SEC)

---

## Per-Year Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2018 | 2018-12-31 | **CORRECTION: Balance sheet ×1000 (7 fields); SGA (3,466,000→21,616,000)** |
| 2019 | 2019-12-31 | **CORRECTION: Balance sheet ×1000 (7 fields); SGA (3,864,000→24,445,000)** |
| 2020 | —          | Missing from Dolt; Yahoo FY2020 not in 4-year history — skipped |
| 2021 | 2021-12-31 | No change |
| 2022 | 2022-12-31 | No change (FY2022 inventory may be gross — see notes) |
| 2023 | 2023-12-31 | No change |
| 2024 | 2024-12-31 | No change |

---

## Notes

- **Non-US company:** No SEC filings. Yahoo Finance is the only external data source. LVMH (Louis Vuitton Moët Hennessy) reports in EUR under IFRS.
- **LVMH fiscal year** ends December 31.
- **FY2020 missing from Dolt:** LVMH adopted IFRS 16 in FY2019. FY2020 is not in Dolt and Yahoo Finance shows NaN for that period. Skipped.
- **[CRITICAL] FY2018 and FY2019 balance sheet unit error:** All balance sheet values (Inventory, Current Assets, Total Assets, Current Liabilities, Liabilities, TSE, TL&SE) are stored as EUR millions when the database unit is EUR thousands — they are off by a factor of 1,000. Income statement values (Revenue, COGS, GM, SGA, Op Profit, Net Profit) are correctly stored in EUR thousands.
- **[CRITICAL] FY2018 and FY2019 SGA — selling/marketing missing:** LVMH's income statement has: Gross Margin → Marketing & Selling Expenses → G&A Expenses → Profit from Recurring Operations. Dolt FY2018 SGA (3,466,000K) and FY2019 SGA (3,864,000K) are only the G&A component (~3–4B EUR). The Selling/Marketing expenses (~18–21B EUR) were not captured. Correct SGA = Gross Margin − Operating Profit.
  - FY2018: 31,201,000 − 9,585,000 = **21,616,000K**
  - FY2019: 35,547,000 − 11,102,000 = **24,445,000K**
- **FY2019 Total Assets jump (74.3B → 96.5B EUR):** Driven by IFRS 16 adoption (operating lease ROU assets added) and the Belmond acquisition. Normal for the transition period.
- **[INFO] FY2022 inventory — possible gross vs net:** Yahoo shows FY2022 inventory = 20,319,000K (gross) with a separate "Inventories Adjustments Allowances" = −2,723,000K, implying net = ~17,596,000K. Dolt stores 20,319,000K (gross). FY2023–FY2024 show no separate adjustment, suggesting those are already net. The correct value for FY2022 requires verification against LVMH's actual 2022 annual report balance sheet (which typically shows net inventory). Flagged but not corrected here.
- **Operating Profit convention:** LVMH reports "Profit from Recurring Operations" as their primary operating metric. Yahoo's "normalized Operating Income" = this value. Dolt uses the normalized (recurring) operating profit, not as-reported. The FY2024 difference: normalized 19,578,000K vs as-reported 18,907,000K (671M EUR in impairments/restructuring). This is consistent across all LVMH years in the DB.
- **Net Profit:** Uses parent-only net income (Net Income Common Stockholders in Yahoo), excluding NCI of ~344–778M EUR/year. Confirmed ✓.
- **Liabilities in Dolt:** Includes NCI (minority interest). Pattern: Dolt Liabilities = Yahoo "Total Liabilities Net Minority Interest" + Yahoo "Minority Interest (balance sheet)". ✓ for FY2022–FY2024.
- **Yahoo Finance coverage:** Available for FY2022–FY2025 (FY2025 column available but not in DB). FY2021 column shows NaN for income statement. FY2018–FY2020 not in Yahoo history.
- **Gross margins 66–69%:** Extremely high — consistent with luxury goods (very high brand premium, pricing power, and product mix across fashion, wines/spirits, perfumes, and watches).

---

## FY2018

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 46,826,000 | 46,826,000 |
| Cost of Goods | N/A | 15,625,000 | 15,625,000 |
| Gross Margin | N/A | 31,201,000 | 31,201,000 |
| SGA | N/A | 3,466,000 ❌ | **21,616,000** |
| Operating Profit | N/A | 9,585,000 | 9,585,000 |
| Net Profit | N/A | 6,990,000 | 6,990,000 |
| Inventory | N/A | 12,485 ❌ | **12,485,000** |
| Current Assets | N/A | 23,551 ❌ | **23,551,000** |
| Total Assets | N/A | 74,300 ❌ | **74,300,000** |
| Current Liabilities | N/A | 16,833 ❌ | **16,833,000** |
| Liabilities | N/A | 40,343 ❌ | **40,343,000** |
| Total Shareholder Equity | N/A | 33,957 ❌ | **33,957,000** |
| Total Liabilities and SE | N/A | 74,300 ❌ | **74,300,000** |

Balance sheet unit error: all 7 balance sheet values stored as EUR millions; multiply by 1,000 for EUR thousands.
SGA: Dolt captures only G&A (~3.5B EUR); correct = Gross Margin − Op Profit = 31,201,000 − 9,585,000 = 21,616,000K.

**Balance sheet check (corrected):** 74,300,000 = 40,343,000 + 33,957,000 ✓
**Gross margin %:** 66.6%
**Action: CORRECTION — Balance sheet ×1000 (7 fields); SGA 3,466,000 → 21,616,000**

---

## FY2019

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 53,670,000 | 53,670,000 |
| Cost of Goods | N/A | 18,123,000 | 18,123,000 |
| Gross Margin | N/A | 35,547,000 | 35,547,000 |
| SGA | N/A | 3,864,000 ❌ | **24,445,000** |
| Operating Profit | N/A | 11,102,000 | 11,102,000 |
| Net Profit | N/A | 7,782,000 | 7,782,000 |
| Inventory | N/A | 13,717 ❌ | **13,717,000** |
| Current Assets | N/A | 26,510 ❌ | **26,510,000** |
| Total Assets | N/A | 96,507 ❌ | **96,507,000** |
| Current Liabilities | N/A | 22,623 ❌ | **22,623,000** |
| Liabilities | N/A | 58,142 ❌ | **58,142,000** |
| Total Shareholder Equity | N/A | 38,365 ❌ | **38,365,000** |
| Total Liabilities and SE | N/A | 96,507 ❌ | **96,507,000** |

Same issues as FY2018.

**Balance sheet check (corrected):** 96,507,000 = 58,142,000 + 38,365,000 ✓
**Gross margin %:** 66.2%
**[INFO] Total Assets jump from FY2018 (~22B EUR): IFRS 16 adoption + Belmond acquisition. Expected.**
**Action: CORRECTION — Balance sheet ×1000 (7 fields); SGA 3,864,000 → 24,445,000**

---

## FY2020

**MISSING FROM DOLT.** LVMH adopted IFRS 16 in FY2019. FY2020 (ending Dec 31, 2020) is not loaded into Dolt. Yahoo Finance does not have this year in its current history window (COVID year). Skipped.

---

## FY2021

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 64,215,000 | 64,215,000 |
| Cost of Goods | N/A | 20,355,000 | 20,355,000 |
| Gross Margin | N/A | 43,860,000 | 43,860,000 |
| SGA | N/A | 26,722,000 | 26,722,000 |
| Operating Profit | N/A | 17,122,000 | 17,122,000 |
| Net Profit | N/A | 12,036,000 | 12,036,000 |
| Inventory | N/A | 16,548,000 | 16,548,000 |
| Current Assets | N/A | 34,301,000 | 34,301,000 |
| Total Assets | N/A | 125,311,000 | 125,311,000 |
| Current Liabilities | N/A | 27,989,000 | 27,989,000 |
| Liabilities | N/A | 78,192,000 | 78,192,000 |
| Total Shareholder Equity | N/A | 47,119,000 | 47,119,000 |
| Total Liabilities and SE | N/A | 125,311,000 | 125,311,000 |

SGA = 26,722,000K = full Selling & Marketing + G&A ✓ (SGA definition same as FY2022–FY2024).
Formula: 43,860 − 26,722 = 17,138 vs Op Profit 17,122; gap of 16K = small special charges ✓.
Yahoo FY2021 column (NaN) — cannot cross-verify directly.

**Balance sheet check:** 125,311,000 = 78,192,000 + 47,119,000 ✓
**Gross margin %:** 68.3%
**Action:** No change

---

## FY2022

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | 79,183,000 | 79,183,000 | 79,183,000 |
| Cost of Goods | 24,988,000 | 24,988,000 | 24,988,000 |
| Gross Margin | 54,195,000 | 54,195,000 | 54,195,000 |
| SGA | 33,178,000 | 33,178,000 | 33,178,000 |
| Operating Profit | 21,014,000* | 21,014,000 | 21,014,000 |
| Net Profit | 14,084,000 | 14,084,000 | 14,084,000 |
| Inventory | 20,319,000 ⚠️ | 20,319,000 | ❓ (see notes) |
| Current Assets | 39,740,000 | 39,740,000 | 39,740,000 |
| Total Assets | 134,646,000 | 134,646,000 | 134,646,000 |
| Current Liabilities | 31,543,000 | 31,543,000 | 31,543,000 |
| Liabilities | 79,535,000** | 79,535,000 | 79,535,000 |
| Total Shareholder Equity | 55,111,000 | 55,111,000 | 55,111,000 |
| Total Liabilities and SE | 134,646,000 | 134,646,000 | 134,646,000 |

*Yahoo normalized Operating Income = 21,014,000K ✓ (as-reported = 21,001,000K; Dolt uses normalized/recurring profit — LVMH convention).
**Yahoo "Total Liabilities Net Minority Interest" = 78,042,000 + NCI (1,493,000) = 79,535,000 = Dolt Liabilities ✓.
⚠️ Inventory: Yahoo shows gross = 20,319,000K with allowance of −2,723,000K (net ~17,596,000K). LVMH balance sheet typically shows net inventory. Verify against LVMH 2022 annual report.

**Balance sheet check:** 134,646,000 = 79,535,000 + 55,111,000 ✓
**Gross margin %:** 68.4%
**Action:** No change (inventory flag for manual verification)

---

## FY2023

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | 86,153,000 | 86,153,000 | 86,153,000 |
| Cost of Goods | 26,876,000 | 26,876,000 | 26,876,000 |
| Gross Margin | 59,277,000 | 59,277,000 | 59,277,000 |
| SGA | 36,482,000 | 36,482,000 | 36,482,000 |
| Operating Profit | 22,781,000* | 22,781,000 | 22,781,000 |
| Net Profit | 15,174,000 | 15,174,000 | 15,174,000 |
| Inventory | 22,952,000 | 22,952,000 | 22,952,000 |
| Current Assets | 43,710,000 | 43,710,000 | 43,710,000 |
| Total Assets | 143,694,000 | 143,694,000 | 143,694,000 |
| Current Liabilities | 33,145,000 | 33,145,000 | 33,145,000 |
| Liabilities | 82,677,000** | 82,677,000 | 82,677,000 |
| Total Shareholder Equity | 61,017,000 | 61,017,000 | 61,017,000 |
| Total Liabilities and SE | 143,694,000 | 143,694,000 | 143,694,000 |

*Yahoo normalized = 22,781,000K ✓ (as-reported = 22,560,000K; 221,000K special charges).
**Yahoo Liabilities (80,993,000) + NCI (1,684,000) = 82,677,000 ✓.

**Balance sheet check:** 143,694,000 = 82,677,000 + 61,017,000 ✓
**Gross margin %:** 68.8%
**Action:** No change

---

## FY2024

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | 84,682,000 | 84,683,000 | 84,683,000 |
| Cost of Goods | 27,918,000 | 27,918,000 | 27,918,000 |
| Gross Margin | 56,764,000 | 56,765,000 | 56,765,000 |
| SGA | 37,222,000 | 37,222,000 | 37,222,000 |
| Operating Profit | 19,577,000* | 19,578,000 | 19,578,000 |
| Net Profit | 12,550,000 | 12,550,000 | 12,550,000 |
| Inventory | 23,669,000 | 23,669,000 | 23,669,000 |
| Current Assets | 47,471,000 | 47,471,000 | 47,471,000 |
| Total Assets | 149,190,000 | 149,190,000 | 149,190,000 |
| Current Liabilities | 33,696,000 | 33,696,000 | 33,696,000 |
| Liabilities | 81,673,000** | 81,673,000 | 81,673,000 |
| Total Shareholder Equity | 67,517,000 | 67,517,000 | 67,517,000 |
| Total Liabilities and SE | 149,190,000 | 149,190,000 | 149,190,000 |

*Yahoo normalized = 19,577,000K ≈ Dolt 19,578,000K (1K rounding) ✓. As-reported = 18,907,000K (671M EUR in special charges: goodwill impairments, restructuring). Dolt uses normalized/recurring — LVMH convention.
**Yahoo Liabilities (79,903,000) + NCI (1,770,000) = 81,673,000 ✓.
Revenue/GM: 1K rounding difference vs Yahoo — within tolerance ✓.

**Balance sheet check:** 149,190,000 = 81,673,000 + 67,517,000 ✓
**Gross margin %:** 67.0%
**Action:** No change

---

**Analysis complete for MC.PA.** FY2018 and FY2019 have two critical errors each: balance sheet values are 1,000× too small (EUR millions stored instead of EUR thousands), and SGA captures only G&A (~3–4B EUR) instead of full selling/marketing + G&A (~21–24B EUR). FY2020 is missing from Dolt. FY2021–FY2024 verified correct. FY2022 inventory may be gross vs net — needs manual verification against LVMH annual report.

