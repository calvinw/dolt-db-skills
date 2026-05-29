# ASOS (ASOMF) — FY2019–FY2025 Financial Analysis

**Generated:** 2026-05-29
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2019 | 2019-08-31 | No change (cannot verify — no Yahoo/SEC data) |
| 2020 | 2020-08-31 | No change (cannot verify — no Yahoo/SEC data) |
| 2021 | 2021-08-31 | No change (cannot verify — no Yahoo/SEC data) |
| 2022 | 2022-08-31 | No change (all fields confirmed against Yahoo) |
| 2023 | 2023-08-31 | No change (all fields confirmed against Yahoo) |
| 2024 | 2024-08-31 | Correction: SGA (1,496,400→1,340,800), Operating Profit (-331,900→-187,000) |
| 2025 | 2025-08-31 | New insert |

---

## Notes

- **Non-US company:** ASOS is UK-listed (ASOS.L / ASOMF OTC). CIK = NULL. No SEC 10-K filings available. Sources: Yahoo Finance + Dolt DB only.
- **Fiscal year end:** August 31 each year.
- **Currency:** All values in thousands of GBP (£).
- **FY2019/2020/2021:** No Yahoo Finance data available for these years. Cannot cross-validate. Existing Dolt values retained.
- **FY2024 SGA issue:** Dolt SGA (1,496,400K) incorrectly includes restructuring charges (144,900K) and D&A amortization (10,700K). Per anomaly rules, both must be excluded. Corrected value: 1,340,800K. Operating Profit corrected accordingly from -331,900K to -187,000K (Yahoo "Operating Income" clean figure, consistent with FY2022 treatment).
- **Inventory:** ASOS carries owned physical inventory. Declining trend (FY2022: 1,078,400K → FY2025: 402,300K) reflects ASOS's known inventory reduction program. Not an anomaly.

---

## FY2019

**Sources:** Dolt only (no Yahoo/SEC data)

### Anomaly Detection
- `[WARNING]` Cannot verify against any external source. Values retained as found in Dolt.
- Gross margin: 1,334,300 / 2,733,500 = 48.8% — within Specialty range (35–55%) ✓
- Balance sheet: 791,900 + 453,600 = 1,245,500 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | — | 2,733,500 | 2,733,500 |
| Cost of Goods | — | — | 1,399,200 | 1,399,200 |
| Gross Margin | — | — | 1,334,300 | 1,334,300 |
| SGA | — | — | 761,800 | 761,800 |
| Operating Profit | — | — | 35,100 | 35,100 |
| Net Profit | — | — | 24,600 | 24,600 |
| Inventory | — | — | 536,800 | 536,800 |
| Current Assets | — | — | 623,200 | 623,200 |
| Total Assets | — | — | 1,245,500 | 1,245,500 |
| Current Liabilities | — | — | 772,200 | 772,200 |
| Liabilities | — | — | 791,900 | 791,900 |
| Total SE | — | — | 453,600 | 453,600 |
| Total L+SE | — | — | 1,245,500 | 1,245,500 |

**Action: No change.**

---

## FY2020

**Sources:** Dolt only (no Yahoo/SEC data)

### Anomaly Detection
- `[WARNING]` Cannot verify against any external source. Values retained as found in Dolt.
- Gross margin: 1,547,400 / 3,263,500 = 47.4% — within Specialty range ✓
- Balance sheet: 1,179,100 + 810,300 = 1,989,400 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | — | 3,263,500 | 3,263,500 |
| Cost of Goods | — | — | 1,716,100 | 1,716,100 |
| Gross Margin | — | — | 1,547,400 | 1,547,400 |
| SGA | — | — | 832,300 | 832,300 |
| Operating Profit | — | — | 151,100 | 151,100 |
| Net Profit | — | — | 113,300 | 113,300 |
| Inventory | — | — | 532,400 | 532,400 |
| Current Assets | — | — | 1,019,800 | 1,019,800 |
| Total Assets | — | — | 1,989,400 | 1,989,400 |
| Current Liabilities | — | — | 817,800 | 817,800 |
| Liabilities | — | — | 1,179,100 | 1,179,100 |
| Total SE | — | — | 810,300 | 810,300 |
| Total L+SE | — | — | 1,989,400 | 1,989,400 |

**Action: No change.**

---

## FY2021

**Sources:** Dolt only (Yahoo 2021 column is NaN for all income statement and balance sheet fields)

### Anomaly Detection
- `[WARNING]` Yahoo Finance has no usable data for FY2021. Cannot cross-validate.
- Gross margin: 1,776,400 / 3,910,500 = 45.4% — within Specialty range ✓
- Balance sheet: 1,850,500 + 1,034,000 = 2,884,500 = Total Assets ✓
- Internal consistency: Gross Margin − SGA = 1,776,400 − 1,586,300 = 190,100 = Operating Profit ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | NaN | 3,910,500 | 3,910,500 |
| Cost of Goods | — | NaN | 2,134,100 | 2,134,100 |
| Gross Margin | — | NaN | 1,776,400 | 1,776,400 |
| SGA | — | NaN | 1,586,300 | 1,586,300 |
| Operating Profit | — | NaN | 190,100 | 190,100 |
| Net Profit | — | NaN | 128,400 | 128,400 |
| Inventory | — | NaN | 807,100 | 807,100 |
| Current Assets | — | NaN | 1,559,700 | 1,559,700 |
| Total Assets | — | NaN | 2,884,500 | 2,884,500 |
| Current Liabilities | — | NaN | 998,000 | 998,000 |
| Liabilities | — | NaN | 1,850,500 | 1,850,500 |
| Total SE | — | NaN | 1,034,000 | 1,034,000 |
| Total L+SE | — | NaN | 2,884,500 | 2,884,500 |

**Action: No change.**

---

## FY2022

**Sources:** Yahoo Finance (2022-08-31 column) + Dolt

### Anomaly Detection
- Gross margin: 1,717,500 / 3,936,500 = 43.6% — within Specialty range ✓
- Balance sheet: 1,982,000 + 1,014,900 = 2,996,900 = Total Assets ✓
- Yahoo SGA Rule 3 check: Yahoo SGA (1,694,000K) vs Yahoo Total Expenses (3,903,100K) — 43.4%, not close. Rule 3 N/A ✓
- All 13 fields match Yahoo exactly.
- Note: Yahoo "Operating Income" (33,400K) used — matches Dolt. Yahoo "Total Operating Income As Reported" (-9,800K) excluded; that value includes special charges of 43,200K. Dolt correctly uses the clean Operating Income figure.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | 3,936,500 | 3,936,500 | 3,936,500 |
| Cost of Goods | — | 2,219,000 | 2,219,000 | 2,219,000 |
| Gross Margin | — | 1,717,500 | 1,717,500 | 1,717,500 |
| SGA | — | 1,694,000 | 1,694,000 | 1,694,000 |
| Operating Profit | — | 33,400 | 33,400 | 33,400 |
| Net Profit | — | -30,800 | -30,800 | -30,800 |
| Inventory | — | 1,078,400 | 1,078,400 | 1,078,400 |
| Current Assets | — | 1,554,000 | 1,554,000 | 1,554,000 |
| Total Assets | — | 2,996,900 | 2,996,900 | 2,996,900 |
| Current Liabilities | — | 1,040,000 | 1,040,000 | 1,040,000 |
| Liabilities | — | 1,982,000 | 1,982,000 | 1,982,000 |
| Total SE | — | 1,014,900 | 1,014,900 | 1,014,900 |
| Total L+SE | — | 2,996,900 | 2,996,900 | 2,996,900 |

**Action: No change.**

---

## FY2023

**Sources:** Yahoo Finance (2023-08-31 column) + Dolt

### Anomaly Detection
- Gross margin: 1,459,000 / 3,549,500 = 41.1% — within Specialty range ✓
- Balance sheet: 1,758,900 + 866,700 = 2,625,600 = Total Assets ✓
- Yahoo SGA Rule 3 check: Yahoo SGA (1,709,500K) vs Yahoo Total Expenses (3,798,000K) — 45.0%. Rule 3 N/A ✓
- All 13 fields match Yahoo exactly.
- Yahoo "Operating Income" = "Total Operating Income As Reported" = -248,500K (same value — no separate exceptional items for this year).

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | 3,549,500 | 3,549,500 | 3,549,500 |
| Cost of Goods | — | 2,090,500 | 2,090,500 | 2,090,500 |
| Gross Margin | — | 1,459,000 | 1,459,000 | 1,459,000 |
| SGA | — | 1,709,500 | 1,709,500 | 1,709,500 |
| Operating Profit | — | -248,500 | -248,500 | -248,500 |
| Net Profit | — | -223,100 | -223,100 | -223,100 |
| Inventory | — | 768,000 | 768,000 | 768,000 |
| Current Assets | — | 1,234,500 | 1,234,500 | 1,234,500 |
| Total Assets | — | 2,625,600 | 2,625,600 | 2,625,600 |
| Current Liabilities | — | 715,200 | 715,200 | 715,200 |
| Liabilities | — | 1,758,900 | 1,758,900 | 1,758,900 |
| Total SE | — | 866,700 | 866,700 | 866,700 |
| Total L+SE | — | 2,625,600 | 2,625,600 | 2,625,600 |

**Action: No change.**

---

## FY2024

**Sources:** Yahoo Finance (2024-08-31 column) + Dolt

### Anomaly Detection

`[ERROR]` **SGA inflated in Dolt.** Dolt SGA = 1,496,400K. Yahoo clean SGA = 1,340,800K (Selling & Marketing 326,100K + G&A 1,014,700K). Difference = 155,600K, which maps exactly to:
- Yahoo D&A (Amortization in Income Statement): 10,700K
- Yahoo Restructuring/Special Charges: 144,900K
- Total inflation: 155,600K → 1,340,800 + 155,600 = 1,496,400K ✓

Per anomaly-rules.md: restructuring charges are one-time and must always be excluded. D&A reported separately must be excluded. **Corrected SGA = 1,340,800K.**

`[ERROR]` **Operating Profit cascades from SGA error.** Dolt Operating Profit = -331,900K = Yahoo "Total Operating Income As Reported" (includes restructuring). Yahoo "Operating Income" (clean) = -187,000K. FY2022 precedent: Dolt correctly used the clean Operating Income (33,400K), not the as-reported figure (-9,800K). **Corrected Operating Profit = -187,000K.**

- Yahoo SGA Rule 3 check: Yahoo SGA (1,340,800K) vs Yahoo Total Expenses (3,092,800K) — 43.4%. Rule 3 N/A ✓
- Gross margin: 1,162,500 / 2,905,800 = 40.0% — within Specialty range ✓
- Balance sheet: 1,749,900 + 521,300 = 2,271,200 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | 2,905,800 | 2,905,800 | 2,905,800 |
| Cost of Goods | — | 1,743,300 | 1,743,300 | 1,743,300 |
| Gross Margin | — | 1,162,500 | 1,162,500 | 1,162,500 |
| SGA | — | 1,340,800 | **1,496,400 \*** | **1,340,800** |
| Operating Profit | — | -187,000 | **-331,900 \*** | **-187,000** |
| Net Profit | — | -338,700 | -338,700 | -338,700 |
| Inventory | — | 520,300 | 520,300 | 520,300 |
| Current Assets | — | 1,146,400 | 1,146,400 | 1,146,400 |
| Total Assets | — | 2,271,200 | 2,271,200 | 2,271,200 |
| Current Liabilities | — | 714,000 | 714,000 | 714,000 |
| Liabilities | — | 1,749,900 | 1,749,900 | 1,749,900 |
| Total SE | — | 521,300 | 521,300 | 521,300 |
| Total L+SE | — | 2,271,200 | 2,271,200 | 2,271,200 |

### Reconciled Values (changes only)
- SGA: 1,340,800K (was 1,496,400K — removed restructuring 144,900K + D&A 10,700K)
- Operating Profit: -187,000K (was -331,900K — corrected to Yahoo clean Operating Income)

**Action: Correction: SGA, Operating Profit.**

---

## FY2025

**Sources:** Yahoo Finance (2025-08-31 column) only — new year not yet in Dolt

### Anomaly Detection
- Gross margin: 1,166,700 / 2,477,800 = 47.1% — within Specialty range ✓
- Balance sheet: 1,459,700 + 212,400 = 1,672,100 = Total Assets ✓
- Yahoo SGA Rule 3 check: Yahoo SGA (1,199,900K) vs Yahoo Total Expenses (2,512,800K) — 47.7%. Rule 3 N/A ✓
- SGA = Selling & Marketing (262,300K) + G&A (937,600K) = 1,199,900K ✓
- Operating Profit uses Yahoo "Operating Income" = -35,000K (clean, pre-exceptional). Yahoo "Total Operating Income As Reported" = -212,300K includes exceptional/restructuring charges of 177,300K (excluded per anomaly rules).
- TSE (212,400K) is positive. No negative equity concern.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | 2,477,800 | — | 2,477,800 |
| Cost of Goods | — | 1,311,100 | — | 1,311,100 |
| Gross Margin | — | 1,166,700 | — | 1,166,700 |
| SGA | — | 1,199,900 | — | 1,199,900 |
| Operating Profit | — | -35,000 | — | -35,000 |
| Net Profit | — | -298,400 | — | -298,400 |
| Inventory | — | 402,300 | — | 402,300 |
| Current Assets | — | 775,300 | — | 775,300 |
| Total Assets | — | 1,672,100 | — | 1,672,100 |
| Current Liabilities | — | 757,400 | — | 757,400 |
| Liabilities | — | 1,459,700 | — | 1,459,700 |
| Total SE | — | 212,400 | — | 212,400 |
| Total L+SE | — | 1,672,100 | — | 1,672,100 |

**Action: New insert.**

---

## Step 7 — Unresolved Flags

Before inserting, review:

1. `[WARNING]` FY2019, FY2020, FY2021 values cannot be verified against any external source. Values in Dolt are retained as-is. If a source for these years is discovered later (e.g., ASOS UK annual reports), revalidation is recommended.
2. `[ERROR → RESOLVED]` FY2024 SGA and Operating Profit corrected in this report. Corrections must be applied before use.

**Analysis complete.** Run `/insert-financials ASOMF` to write all changed years to the database.
