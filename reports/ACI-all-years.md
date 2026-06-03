# Albertsons (ACI) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-03
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2019-02-23 | No change (Dolt only — no external source; balance sheet identity passes) |
| 2019 | 2020-02-29 | No change (income stmt confirmed by SEC; balance sheet unverified but identity passes) |
| 2020 | 2021-02-27 | No change (income stmt confirmed by SEC; balance sheet unverified but identity passes) |
| 2021 | 2022-02-26 | No change (all fields confirmed vs SEC + Yahoo) |
| 2022 | 2023-02-25 | No change (all fields confirmed vs SEC + Yahoo) |
| 2023 | 2024-02-24 | No change (all fields confirmed vs SEC + Yahoo) |
| 2024 | 2025-02-22 | Correction: reportDate (2025-02-24 → 2025-02-22) |
| 2025 | 2026-02-28 | New insert |

---

## Notes

- **US company:** CIK = 1646972. SEC 10-K filings available FY2018–FY2025.
- **Fiscal year end:** Late February each year (e.g. FY2024 ended 2025-02-22). Year label = calendar year in which majority of the fiscal year falls.
- **Currency:** All values in $thousands (USD).
- **Segment:** Grocery. Expected gross margin 22–28%; Albertsons' pharmacy and specialty mix occasionally pushes to 28–29%.
- **SGA:** Single combined `us-gaap_SellingGeneralAndAdministrativeExpense` line — no composite construction needed. Yahoo SGA matches SEC SGA exactly across all verified years.
- **Net Profit consistency:** Dolt uses `us-gaap_NetIncomeLoss` (Net Income) consistently. For FY2022, Yahoo shows "Net Income Common Stockholders" of 1,210,300K (after $303.2M preferred dividends); correct Dolt value using Net Income = 1,513,500K. This is consistent with SEC and all other years.
- **FY2024 reportDate:** SEC 10-K header shows 2025-02-22; Dolt has 2025-02-24. Correcting to match SEC.
- **FY2018–FY2020 balance sheets:** Not directly verifiable from available SEC filings (older filings not fetched). Income statements for FY2019 and FY2020 confirmed via comparative columns in the FY2021 10-K. FY2018 income statement not cross-checked. Balance sheet identity checks pass for all three years.
- **FY2025:** New insert. SEC fiscal year ended 2026-02-28 confirmed by Yahoo column header.

---

## FY2018

**Sources:** Dolt only (no SEC/Yahoo data available)

### Anomaly Detection
- `[WARNING]` Cannot verify income statement or balance sheet against any external source.
- Gross margin: 16,894,600 / 60,534,500 = 27.9% — at upper edge of Grocery benchmark (22–28%); acceptable for Albertsons' pharmacy/specialty mix.
- Balance sheet: 19,325,900 + 1,450,700 = 20,776,600 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | — | 60,534,500 | 60,534,500 |
| Cost of Goods | — | — | 43,639,900 | 43,639,900 |
| Gross Margin | — | — | 16,894,600 | 16,894,600 |
| SGA | — | — | 16,107,300 | 16,107,300 |
| Operating Profit | — | — | 787,300 | 787,300 |
| Net Profit | — | — | 131,100 | 131,100 |
| Inventory | — | — | 4,332,800 | 4,332,800 |
| Current Assets | — | — | 6,250,000 | 6,250,000 |
| Total Assets | — | — | 20,776,600 | 20,776,600 |
| Current Liabilities | — | — | 5,152,700 | 5,152,700 |
| Liabilities | — | — | 19,325,900 | 19,325,900 |
| Total SE | — | — | 1,450,700 | 1,450,700 |
| Total L+SE | — | — | 20,776,600 | 20,776,600 |

**Action: No change.**

---

## FY2019

**Sources:** Dolt + SEC comparative (from FY2021 10-K, column 2020-02-29)

### Anomaly Detection
- Income statement confirmed by SEC comparative columns — all values match.
- `[WARNING]` Balance sheet not independently verified (older filing not fetched); identity check passes.
- Gross margin: 17,594,200 / 62,455,100 = 28.2% — slightly above Grocery benchmark; within acceptable range for Albertsons.
- Balance sheet: 22,457,000 + 2,278,100 = 24,735,100 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 62,455,100 | — | 62,455,100 | 62,455,100 |
| Cost of Goods | 44,860,900 | — | 44,860,900 | 44,860,900 |
| Gross Margin | 17,594,200 | — | 17,594,200 | 17,594,200 |
| SGA | 16,641,900 | — | 16,641,900 | 16,641,900 |
| Operating Profit | 1,437,100 | — | 1,437,100 | 1,437,100 |
| Net Profit | 466,400 | — | 466,400 | 466,400 |
| Inventory | — | — | 4,352,500 | 4,352,500 |
| Current Assets | — | — | 5,731,300 | 5,731,300 |
| Total Assets | — | — | 24,735,100 | 24,735,100 |
| Current Liabilities | — | — | 5,904,300 | 5,904,300 |
| Liabilities | — | — | 22,457,000 | 22,457,000 |
| Total SE | — | — | 2,278,100 | 2,278,100 |
| Total L+SE | — | — | 24,735,100 | 24,735,100 |

**Action: No change.**

---

## FY2020

**Sources:** Dolt + SEC comparative (from FY2021 10-K, column 2021-02-27)

### Anomaly Detection
- Income statement confirmed by SEC comparative columns — all values match.
- `[WARNING]` Balance sheet not independently verified (older filing not fetched); identity check passes.
- Gross margin: 20,414,500 / 69,690,400 = 29.3% — above Grocery benchmark; COVID-era sales mix shift (more pharmacy/fresh, less fuel) explains elevated margin.
- Balance sheet: 25,273,700 + 1,324,300 = 26,598,000 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 69,690,400 | — | 69,690,400 | 69,690,400 |
| Cost of Goods | 49,275,900 | — | 49,275,900 | 49,275,900 |
| Gross Margin | 20,414,500 | — | 20,414,500 | 20,414,500 |
| SGA | 18,835,800 | — | 18,835,800 | 18,835,800 |
| Operating Profit | 1,617,500 | — | 1,617,500 | 1,617,500 |
| Net Profit | 850,200 | — | 850,200 | 850,200 |
| Inventory | — | — | 4,301,300 | 4,301,300 |
| Current Assets | — | — | 6,988,000 | 6,988,000 |
| Total Assets | — | — | 26,598,000 | 26,598,000 |
| Current Liabilities | — | — | 6,832,200 | 6,832,200 |
| Liabilities | — | — | 25,273,700 | 25,273,700 |
| Total SE | — | — | 1,324,300 | 1,324,300 |
| Total L+SE | — | — | 26,598,000 | 26,598,000 |

**Action: No change.**

---

## FY2021

**Sources:** Dolt + SEC (10-K filed 2022, period ending 2022-02-26) + Yahoo (column 2022-02-28)

### Anomaly Detection
- All income statement fields confirmed: SEC = Dolt = Yahoo (minor date rounding in Yahoo header).
- All balance sheet fields confirmed: SEC = Dolt.
- Gross margin: 20,722,400 / 71,887,000 = 28.8% — slightly above benchmark; fuel recovery and pharmacy growth contribute.
- Balance sheet: 25,098,400 + 3,024,600 = 28,123,000 = Total Assets ✓
- No SGA composite issues — single SGA line in SEC, matches Yahoo exactly.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 71,887,000 | 71,887,000 | 71,887,000 | 71,887,000 |
| Cost of Goods | 51,164,600 | 51,164,600 | 51,164,600 | 51,164,600 |
| Gross Margin | 20,722,400 | 20,722,400 | 20,722,400 | 20,722,400 |
| SGA | 18,300,500 | 18,300,500 | 18,300,500 | 18,300,500 |
| Operating Profit | 2,436,900 | 2,436,900 | 2,436,900 | 2,436,900 |
| Net Profit | 1,619,600 | 1,619,600 | 1,619,600 | 1,619,600 |
| Inventory | 4,500,800 | 4,500,800 | 4,500,800 | 4,500,800 |
| Current Assets | 8,366,400 | 8,366,400 | 8,366,400 | 8,366,400 |
| Total Assets | 28,123,000 | 28,123,000 | 28,123,000 | 28,123,000 |
| Current Liabilities | 8,348,500 | 8,348,500 | 8,348,500 | 8,348,500 |
| Liabilities | 25,098,400 | 25,098,400 | 25,098,400 | 25,098,400 |
| Total SE | 3,024,600 | 3,024,600 | 3,024,600 | 3,024,600 |
| Total L+SE | 28,123,000 | 28,123,000 | 28,123,000 | 28,123,000 |

**Action: No change.**

---

## FY2022

**Sources:** Dolt + SEC (10-K filed 2023, period ending 2023-02-25) + Yahoo (column 2023-02-28)

### Anomaly Detection
- All income statement fields confirmed: SEC = Dolt = Yahoo (minor date rounding in Yahoo header).
- All balance sheet fields confirmed: SEC = Dolt.
- Gross margin: 21,755,600 / 77,649,700 = 28.0% — at upper edge of Grocery benchmark; acceptable.
- Balance sheet: 24,557,500 + 1,610,700 = 26,168,200 = Total Assets ✓
- Net Profit: Yahoo "Net Income Common Stockholders" = 1,210,300K (excludes $303.2M preferred dividends). Dolt correctly uses Net Income = 1,513,500K per SEC `us-gaap_NetIncomeLoss`. No change needed.
- No SGA composite issues.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 77,649,700 | 77,649,700 | 77,649,700 | 77,649,700 |
| Cost of Goods | 55,894,100 | 55,894,100 | 55,894,100 | 55,894,100 |
| Gross Margin | 21,755,600 | 21,755,600 | 21,755,600 | 21,755,600 |
| SGA | 19,596,000 | 19,596,000 | 19,596,000 | 19,596,000 |
| Operating Profit | 2,307,100 | 2,307,100 | 2,307,100 | 2,307,100 |
| Net Profit | 1,513,500 | 1,513,500* | 1,513,500 | 1,513,500 |
| Inventory | 4,782,000 | 4,782,000 | 4,782,000 | 4,782,000 |
| Current Assets | 6,270,400 | 6,270,400 | 6,270,400 | 6,270,400 |
| Total Assets | 26,168,200 | 26,168,200 | 26,168,200 | 26,168,200 |
| Current Liabilities | 8,428,800 | 8,428,800 | 8,428,800 | 8,428,800 |
| Liabilities | 24,557,500 | 24,557,500 | 24,557,500 | 24,557,500 |
| Total SE | 1,610,700 | 1,610,700 | 1,610,700 | 1,610,700 |
| Total L+SE | 26,168,200 | 26,168,200 | 26,168,200 | 26,168,200 |

*Yahoo "Net Income Common Stockholders" = 1,210,300K; "Net Income" = 1,513,500K. Using Net Income per SEC.

**Action: No change.**

---

## FY2023

**Sources:** Dolt + SEC (10-K filed 2024, period ending 2024-02-24) + Yahoo (column 2024-02-29)

### Anomaly Detection
- All income statement fields confirmed: SEC = Dolt = Yahoo (minor date rounding in Yahoo header).
- All balance sheet fields confirmed: SEC = Dolt.
- Gross margin: 22,045,700 / 79,237,700 = 27.8% — within Grocery benchmark ✓
- Balance sheet: 23,473,600 + 2,747,500 = 26,221,100 = Total Assets ✓
- No SGA composite issues.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 79,237,700 | 79,237,700 | 79,237,700 | 79,237,700 |
| Cost of Goods | 57,192,000 | 57,192,000 | 57,192,000 | 57,192,000 |
| Gross Margin | 22,045,700 | 22,045,700 | 22,045,700 | 22,045,700 |
| SGA | 19,932,900 | 19,932,900 | 19,932,900 | 19,932,900 |
| Operating Profit | 2,068,900 | 2,068,900 | 2,068,900 | 2,068,900 |
| Net Profit | 1,296,000 | 1,295,000* | 1,296,000 | 1,296,000 |
| Inventory | 4,945,200 | 4,945,200 | 4,945,200 | 4,945,200 |
| Current Assets | 6,287,500 | 6,287,500 | 6,287,500 | 6,287,500 |
| Total Assets | 26,221,100 | 26,221,100 | 26,221,100 | 26,221,100 |
| Current Liabilities | 7,457,700 | 7,457,700 | 7,457,700 | 7,457,700 |
| Liabilities | 23,473,600 | 23,473,600 | 23,473,600 | 23,473,600 |
| Total SE | 2,747,500 | 2,747,500 | 2,747,500 | 2,747,500 |
| Total L+SE | 26,221,100 | 26,221,100 | 26,221,100 | 26,221,100 |

*Yahoo Net Income Common Stockholders = 1,295,000K vs SEC Net Income = 1,296,000K; $1M rounding. Using SEC.

**Action: No change.**

---

## FY2024

**Sources:** Dolt + SEC (10-K filed 2025, period ending 2025-02-22) + Yahoo (column 2025-02-28)

### Anomaly Detection
- `[WARNING]` reportDate discrepancy: Dolt has 2025-02-24; SEC 10-K header shows 2025-02-22; Yahoo column header 2025-02-28. SEC is authoritative — correcting to 2025-02-22.
- All financial fields confirmed: SEC = Dolt = Yahoo.
- Gross margin: 22,255,600 / 80,390,900 = 27.7% — within Grocery benchmark ✓
- Balance sheet: 23,369,800 + 3,385,900 = 26,755,700 = Total Assets ✓
- No SGA composite issues.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| reportDate | **2025-02-22*** | 2025-02-28 | 2025-02-24* | **2025-02-22** |
| Net Revenue | 80,390,900 | 80,390,900 | 80,390,900 | 80,390,900 |
| Cost of Goods | 58,135,300 | 58,135,300 | 58,135,300 | 58,135,300 |
| Gross Margin | 22,255,600 | 22,255,600 | 22,255,600 | 22,255,600 |
| SGA | 20,613,700 | 20,613,700 | 20,613,700 | 20,613,700 |
| Operating Profit | 1,546,100 | 1,546,100 | 1,546,100 | 1,546,100 |
| Net Profit | 958,600 | 958,600 | 958,600 | 958,600 |
| Inventory | 4,989,000 | 4,989,000 | 4,989,000 | 4,989,000 |
| Current Assets | 6,559,000 | 6,559,000 | 6,559,000 | 6,559,000 |
| Total Assets | 26,755,700 | 26,755,700 | 26,755,700 | 26,755,700 |
| Current Liabilities | 7,251,000 | 7,251,000 | 7,251,000 | 7,251,000 |
| Liabilities | 23,369,800 | 23,369,800 | 23,369,800 | 23,369,800 |
| Total SE | 3,385,900 | 3,385,900 | 3,385,900 | 3,385,900 |
| Total L+SE | 26,755,700 | 26,755,700 | 26,755,700 | 26,755,700 |

*SEC fiscal year end date from 10-K period header = 2025-02-22. Dolt's 2025-02-24 is incorrect.

**Action: Correction — reportDate 2025-02-24 → 2025-02-22. All financial values unchanged.**

---

## FY2025

**Sources:** SEC (10-K filed 2026, period ending 2026-02-28) + Yahoo (column 2026-02-28). New insert — not yet in Dolt.

### Anomaly Detection
- All fields confirmed: SEC = Yahoo.
- Gross margin: 22,606,700 / 83,172,500 = 27.2% — within Grocery benchmark ✓
- Balance sheet: 24,929,700 + 1,836,200 = 26,765,900 = Total Assets ✓
- Net Profit 217,400K and Operating Profit 727,600K are significantly lower than FY2024 (958,600K / 1,546,100K). This reflects real margin compression reported in FY2025 — not a data anomaly.
- SGA increased to 21,891,300K from 20,613,700K — consistent with higher operating costs, merger-related expenses, and fuel price changes.
- No SGA composite issues — single line in SEC, matches Yahoo exactly.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 83,172,500 | 83,172,500 | — | 83,172,500 |
| Cost of Goods | 60,565,800 | 60,565,800 | — | 60,565,800 |
| Gross Margin | 22,606,700 | 22,606,700 | — | 22,606,700 |
| SGA | 21,891,300 | 21,891,300 | — | 21,891,300 |
| Operating Profit | 727,600 | 727,600 | — | 727,600 |
| Net Profit | 217,400 | 217,400 | — | 217,400 |
| Inventory | 5,173,900 | 5,173,900 | — | 5,173,900 |
| Current Assets | 6,715,700 | 6,715,700 | — | 6,715,700 |
| Total Assets | 26,765,900 | 26,765,900 | — | 26,765,900 |
| Current Liabilities | 7,824,000 | 7,824,000 | — | 7,824,000 |
| Liabilities | 24,929,700 | 24,929,700 | — | 24,929,700 |
| Total SE | 1,836,200 | 1,836,200 | — | 1,836,200 |
| Total L+SE | 26,765,900 | 26,765,900 | — | 26,765,900 |

**Action: New insert.**

---

## Unresolved Flags

1. `[WARNING]` FY2018 income statement not cross-checked (no SEC fetch; oldest filing, pre-IPO era). Balance sheet identity passes. Values retained as-is.
2. `[WARNING]` FY2019 and FY2020 balance sheets not independently verified from SEC (income statements confirmed via FY2021 10-K comparative columns). Balance sheet identity checks pass.

**Analysis complete.** Run `/insert-financials ACI` to write all changed years to the database.
