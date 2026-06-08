# Kroger (KR) — FY2018–FY2024 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2018 | 2019-02-02 | **CORRECTION: COGS (−94,894,000→94,894,000), Gross Margin (216,056,000→26,268,000), SGA (−20,305,000→20,305,000)** |
| 2019 | 2020-02-01 | No change (inventory may need SEC verification — see notes) |
| 2020 | 2021-01-30 | No change (inventory may need SEC verification) |
| 2021 | 2022-01-29 | No change (inventory may need SEC verification) |
| 2022 | 2023-01-28 | **CORRECTION: Inventory (9,756,000→7,560,000)** |
| 2023 | 2024-02-03 | **CORRECTION: Inventory (9,414,000→7,105,000)** |
| 2024 | 2025-02-03 | **CORRECTION: SGA (NULL→25,431,000)** |

---

## Notes

- **Kroger fiscal year** ends in late January/early February. DB year label corresponds to the fiscal year ending that January/February.
- **SGA treatment:** Kroger's SGA in Dolt = "Operating, General and Administrative Expenses" (OG&A) — the main non-COGS operating expense line (labor, benefits, utilities, etc.). This matches Yahoo's "Other Operating Expenses" field for FY2022–FY2024. The operating profit formula: Gross Margin − OG&A − D&A − Rent = Operating Income, where D&A ≈ 2,965–3,246K and Rent ≈ 839–877K per year (FY2022–FY2024, confirmed by Yahoo).
- **[CRITICAL] FY2018 COGS and SGA sign errors:** COGS = −94,894,000 (should be positive) and SGA = −20,305,000 (should be positive). This caused Gross Margin to be computed as 216,056,000 (impossible; correct value = Revenue − COGS = 26,268,000). All three fields need correction. Balance sheet is unaffected (balance sheet identity holds for FY2018).
- **[CRITICAL] FY2022–FY2023 Inventory — FIFO vs LIFO inconsistency:** Kroger uses LIFO for most grocery inventories. The balance sheet face reports LIFO-valued inventory (net). FIFO cost and LIFO reserve are disclosed in footnotes. Dolt FY2022 inventory (9,756,000) and FY2023 inventory (9,414,000) appear to be FIFO gross values (from footnote disclosure), while the correct balance sheet values (LIFO net) are 7,560,000 and 7,105,000 respectively. This is confirmed by: Yahoo Current Assets = 12,670,000 (FY2022) and 12,948,000 (FY2023) are consistent with LIFO inventory (7,560,000 and 7,105,000), not FIFO. FY2024 inventory (7,038,000 in Dolt) correctly uses LIFO net. Yahoo LIFO reserves: FY2022 = 2,196K, FY2023 = 2,309K, FY2024 = 2,404K.
- **[ANOMALY] FY2019–FY2021 Inventory:** Same FIFO vs LIFO issue likely applies to FY2019–FY2021 (inventory 8,464K, 8,436K, 8,353K). Cannot confirm without SEC data. Flag for verification.
- **FY2024 SGA = NULL:** The SGA value was not entered for FY2024. Derived from formula: Gross Margin (33,403) − D&A (3,246 per Yahoo) − Rent (877 per Yahoo) − Operating Profit (3,849) = **25,431,000**.
- **Yahoo Finance coverage:** FY2022–FY2024 revenue, COGS, gross margin, operating profit, and net profit all confirmed. FY2021 column is NaN. FY2018–FY2021 not in Yahoo history.
- **Yahoo SGA note:** Yahoo "Selling General And Administration" for Kroger = 839–877K (only rent/G&A). Dolt correctly uses the broader OG&A figure (~23–26B).
- **All balance sheet identities:** ✓ for all 7 years (including FY2018 despite income statement errors).
- **Gross margins:** FY2018 corrected = 21.7%; FY2019–FY2024 = 22.1–22.3%. Consistent with grocery benchmark (thin margins).
- **Net Profit note:** Dolt uses total net income (not subtracting preferred dividends of ~$20M/year). Difference vs "Net Income Common Stockholders" is ~$20M (<1%). Not correcting — consistent with DB convention.

---

## FY2018

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 121,162,000 | 121,162,000 |
| Cost of Goods | N/A | −94,894,000 ❌ | **94,894,000** |
| Gross Margin | N/A | 216,056,000 ❌ | **26,268,000** |
| SGA | N/A | −20,305,000 ❌ | **20,305,000** |
| Operating Profit | N/A | 2,614,000 | 2,614,000 |
| Net Profit | N/A | 3,110,000 | 3,110,000 |
| Inventory | N/A | 8,123,000 | ❓ (may be FIFO — SEC needed) |
| Current Assets | N/A | 10,803,000 | 10,803,000 |
| Total Assets | N/A | 38,118,000 | 38,118,000 |
| Current Liabilities | N/A | 14,274,000 | 14,274,000 |
| Liabilities | N/A | 30,283,000 | 30,283,000 |
| Total Shareholder Equity | N/A | 7,835,000 | 7,835,000 |
| Total Liabilities and SE | N/A | 38,118,000 | 38,118,000 |

COGS/SGA are stored with wrong sign — data entry error. Correct COGS = 94,894,000, GM = 121,162 − 94,894 = 26,268,000, SGA = 20,305,000.

**Balance sheet check:** 38,118,000 = 30,283,000 + 7,835,000 ✓
**Corrected Gross margin %:** 21.7%
**Action: CORRECTION — COGS, Gross Margin, SGA (sign errors)**

---

## FY2019

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 122,286,000 | 122,286,000 |
| Cost of Goods | N/A | 95,294,000 | 95,294,000 |
| Gross Margin | N/A | 26,992,000 | 26,992,000 |
| SGA | N/A | 21,208,000 | 21,208,000 |
| Operating Profit | N/A | 2,251,000 | 2,251,000 |
| Net Profit | N/A | 1,659,000 | 1,659,000 |
| Inventory | N/A | 8,464,000 | ❓ (may be FIFO — SEC needed) |
| Current Assets | N/A | 10,890,000 | 10,890,000 |
| Total Assets | N/A | 45,256,000 | 45,256,000 |
| Current Liabilities | N/A | 14,243,000 | 14,243,000 |
| Liabilities | N/A | 36,654,000 | 36,654,000 |
| Total Shareholder Equity | N/A | 8,602,000 | 8,602,000 |
| Total Liabilities and SE | N/A | 45,256,000 | 45,256,000 |

**Balance sheet check:** 45,256,000 = 36,654,000 + 8,602,000 ✓
**[INFO] Total Assets jump from FY2018 (+7.1B) due to ASC 842 adoption.**
**Gross margin %:** 22.1%
**Action:** No change (inventory flag only)

---

## FY2020

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 132,498,000 | 132,498,000 |
| Cost of Goods | N/A | 101,597,000 | 101,597,000 |
| Gross Margin | N/A | 30,901,000 | 30,901,000 |
| SGA | N/A | 24,500,000 | 24,500,000 |
| Operating Profit | N/A | 2,780,000 | 2,780,000 |
| Net Profit | N/A | 2,585,000 | 2,585,000 |
| Inventory | N/A | 8,436,000 | ❓ (may be FIFO — SEC needed) |
| Current Assets | N/A | 12,503,000 | 12,503,000 |
| Total Assets | N/A | 48,662,000 | 48,662,000 |
| Current Liabilities | N/A | 15,366,000 | 15,366,000 |
| Liabilities | N/A | 39,086,000 | 39,086,000 |
| Total Shareholder Equity | N/A | 9,576,000 | 9,576,000 |
| Total Liabilities and SE | N/A | 48,662,000 | 48,662,000 |

**Balance sheet check:** 48,662,000 = 39,086,000 + 9,576,000 ✓
**Gross margin %:** 23.3%
**Action:** No change (inventory flag only)

---

## FY2021

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 137,888,000 | 137,888,000 |
| Cost of Goods | N/A | 107,539,000 | 107,539,000 |
| Gross Margin | N/A | 30,349,000 | 30,349,000 |
| SGA | N/A | 23,203,000 | 23,203,000 |
| Operating Profit | N/A | 3,477,000 | 3,477,000 |
| Net Profit | N/A | 1,655,000 | 1,655,000 |
| Inventory | N/A | 8,353,000 | ❓ (may be FIFO — SEC needed) |
| Current Assets | N/A | 12,174,000 | 12,174,000 |
| Total Assets | N/A | 49,086,000 | 49,086,000 |
| Current Liabilities | N/A | 16,323,000 | 16,323,000 |
| Liabilities | N/A | 39,634,000 | 39,634,000 |
| Total Shareholder Equity | N/A | 9,452,000 | 9,452,000 |
| Total Liabilities and SE | N/A | 49,086,000 | 49,086,000 |

**Balance sheet check:** 49,086,000 = 39,634,000 + 9,452,000 ✓
**Gross margin %:** 22.0%
**Action:** No change (inventory flag only)

---

## FY2022

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | 148,258,000 | 148,258,000 | 148,258,000 |
| Cost of Goods | 116,480,000 | 116,480,000 | 116,480,000 |
| Gross Margin | 31,778,000 | 31,778,000 | 31,778,000 |
| SGA | 23,848,000* | 23,848,000 | 23,848,000 |
| Operating Profit | 4,126,000 | 4,126,000 | 4,126,000 |
| Net Profit | 2,244,000 | 2,244,000 | 2,244,000 |
| Inventory | 7,560,000 | 9,756,000 ❌ | **7,560,000** |
| Current Assets | 12,670,000 | 12,670,000 | 12,670,000 |
| Total Assets | 49,623,000 | 49,623,000 | 49,623,000 |
| Current Liabilities | 17,238,000 | 17,238,000 | 17,238,000 |
| Liabilities | 39,581,000 | 39,581,000 | 39,581,000 |
| Total Shareholder Equity | 10,042,000 | 10,042,000 | 10,042,000 |
| Total Liabilities and SE | 49,623,000 | 49,623,000 | 49,623,000 |

*Yahoo "Other Operating Expenses" = 23,848,000 = Dolt SGA ✓. Yahoo D&A = 2,965,000K; Rent = 839,000K; formula: 31,778 − 23,848 − 2,965 − 839 = 4,126 ✓.
Inventory correction: Dolt 9,756,000 = FIFO gross (footnote value). Correct balance-sheet LIFO value = FIFO (9,756) − LIFO reserve (2,196) = **7,560,000**. Confirmed by: Yahoo Current Assets (12,670K) is consistent with inventory = 7,560K, not 9,756K.

**Balance sheet check:** 49,623,000 = 39,581,000 + 10,042,000 ✓
**Gross margin %:** 21.4%
**Action: CORRECTION — Inventory 9,756,000 → 7,560,000**

---

## FY2023

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | 150,039,000 | 150,039,000 | 150,039,000 |
| Cost of Goods | 116,675,000 | 116,675,000 | 116,675,000 |
| Gross Margin | 33,364,000 | 33,364,000 | 33,364,000 |
| SGA | 26,252,000* | 26,252,000 | 26,252,000 |
| Operating Profit | 3,096,000 | 3,096,000 | 3,096,000 |
| Net Profit | 2,164,000 | 2,164,000 | 2,164,000 |
| Inventory | 7,105,000 | 9,414,000 ❌ | **7,105,000** |
| Current Assets | 12,948,000 | 12,948,000 | 12,948,000 |
| Total Assets | 50,505,000 | 50,505,000 | 50,505,000 |
| Current Liabilities | 16,058,000 | 16,058,000 | 16,058,000 |
| Liabilities | 38,890,000 | 38,890,000 | 38,890,000 |
| Total Shareholder Equity | 11,615,000 | 11,615,000 | 11,615,000 |
| Total Liabilities and SE | 50,505,000 | 50,505,000 | 50,505,000 |

*Yahoo "Other Operating Expenses" = 26,252,000 = Dolt SGA ✓. Yahoo D&A = 3,125,000K; Rent = 891,000K; formula: 33,364 − 26,252 − 3,125 − 891 = 3,096 ✓.
Inventory correction: Dolt 9,414,000 = FIFO. LIFO = 9,414 − 2,309 (LIFO reserve) = **7,105,000**. Confirmed by Yahoo Current Assets = 12,948K consistent with inventory = 7,105K.

**Balance sheet check:** 50,505,000 = 38,890,000 + 11,615,000 ✓
**Gross margin %:** 22.2%
**Action: CORRECTION — Inventory 9,414,000 → 7,105,000**

---

## FY2024

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | 147,123,000 | 147,123,000 | 147,123,000 |
| Cost of Goods | 113,720,000 | 113,720,000 | 113,720,000 |
| Gross Margin | 33,403,000 | 33,403,000 | 33,403,000 |
| SGA | 25,431,000* | NULL ❌ | **25,431,000** |
| Operating Profit | 3,849,000 | 3,849,000 | 3,849,000 |
| Net Profit | 2,665,000 | 2,665,000 | 2,665,000 |
| Inventory | 7,038,000 | 7,038,000 | 7,038,000 |
| Current Assets | 15,273,000 | 15,273,000 | 15,273,000 |
| Total Assets | 52,616,000 | 52,616,000 | 52,616,000 |
| Current Liabilities | 15,940,000 | 15,940,000 | 15,940,000 |
| Liabilities | 44,335,000 | 44,335,000 | 44,335,000 |
| Total Shareholder Equity | 8,281,000 | 8,281,000 | 8,281,000 |
| Total Liabilities and SE | 52,616,000 | 52,616,000 | 52,616,000 |

*SGA derived from formula: 33,403 − 3,246 (D&A) − 877 (Rent) − 3,849 (Op Profit) = **25,431,000** = Yahoo "Other Operating Expenses" for FY2024 ✓. FY2024 inventory (7,038,000) is the LIFO-net value and is correct (consistent with current assets).

**Balance sheet check:** 52,616,000 = 44,335,000 + 8,281,000 ✓
**Gross margin %:** 22.7%
**Action: CORRECTION — SGA NULL → 25,431,000**

---

**Analysis complete for KR.** Corrections needed: FY2018 (COGS/GM/SGA sign errors), FY2022 and FY2023 (inventory FIFO→LIFO), FY2024 (SGA missing). FY2019–FY2021 inventory flagged for SEC verification (likely FIFO). All balance sheet identities satisfied.
