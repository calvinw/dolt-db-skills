# ASOS (ASOMF) — FY2019–FY2025 Financial Analysis

**Generated:** 2026-06-03
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2019 | 2019-08-31 | No change (Dolt only, no external source available) |
| 2020 | 2020-08-31 | No change (Dolt only, no external source available) |
| 2021 | 2021-08-31 | No change (Dolt only, no external source available) |
| 2022 | 2022-08-31 | Correction: Operating Profit (33,400→-9,800) |
| 2023 | 2023-08-31 | No change (all fields confirmed vs Yahoo) |
| 2024 | 2024-08-31 | Correction: SGA (1,496,400→1,340,800) |
| 2025 | 2025-08-31 | New insert |

---

## Notes

- **Non-US company:** ASOS is UK-listed (ASOS.L / ASOMF OTC). CIK = NULL. No SEC 10-K filings available. Sources: Yahoo Finance + Dolt DB only.
- **Fiscal year end:** August 31 each year.
- **Currency:** All values in thousands (consistent with Yahoo Finance USD-equivalent figures).
- **FY2019/2020/2021:** No Yahoo Finance data available for these years. Cannot cross-validate. Balance sheet checks pass; existing Dolt values retained.
- **FY2022 Operating Profit:** Dolt has 33,400 (Yahoo's adjusted/underlying figure, excludes ~43,200 in special charges). GAAP reported is -9,800 (Yahoo "Total Operating Income As Reported"). Correcting to GAAP basis for consistency.
- **FY2024 SGA:** Dolt has 1,496,400 which includes special charges/impairments (~155,600). Yahoo's "Selling General And Administration" line is 1,340,800. Per anomaly rules, restructuring and impairment charges must be excluded from SGA. Correcting to 1,340,800.
- **Operating Profit approach:** Using Yahoo "Total Operating Income As Reported" (GAAP basis) consistently across all years.
- **Inventory:** ASOS carries owned physical inventory. Declining trend (FY2022: 1,078,400 → FY2025: 402,300) reflects ASOS's known inventory reduction program — not an anomaly.

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
- Gross margin: 1,547,400 / 3,263,500 = 47.4% — within Specialty range (35–55%) ✓
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

**Sources:** Dolt only (Yahoo FY2021 column is all NaN — no usable data)

### Anomaly Detection
- `[WARNING]` Cannot verify against any external source. Values retained as found in Dolt.
- Gross margin: 1,776,400 / 3,910,500 = 45.4% — within Specialty range (35–55%) ✓
- Balance sheet: 1,850,500 + 1,034,000 = 2,884,500 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | — | 3,910,500 | 3,910,500 |
| Cost of Goods | — | — | 2,134,100 | 2,134,100 |
| Gross Margin | — | — | 1,776,400 | 1,776,400 |
| SGA | — | — | 1,586,300 | 1,586,300 |
| Operating Profit | — | — | 190,100 | 190,100 |
| Net Profit | — | — | 128,400 | 128,400 |
| Inventory | — | — | 807,100 | 807,100 |
| Current Assets | — | — | 1,559,700 | 1,559,700 |
| Total Assets | — | — | 2,884,500 | 2,884,500 |
| Current Liabilities | — | — | 998,000 | 998,000 |
| Liabilities | — | — | 1,850,500 | 1,850,500 |
| Total SE | — | — | 1,034,000 | 1,034,000 |
| Total L+SE | — | — | 2,884,500 | 2,884,500 |

**Action: No change.**

---

## FY2022

**Sources:** Yahoo Finance + Dolt

### Anomaly Detection
- Gross margin: 1,717,500 / 3,936,500 = 43.6% — within Specialty range (35–55%) ✓
- Balance sheet: 1,982,000 + 1,014,900 = 2,996,900 = Total Assets ✓
- `[ERROR]` Operating Profit discrepancy: Dolt has 33,400 (Yahoo adjusted/underlying), but Yahoo "Total Operating Income As Reported" = -9,800 (GAAP, includes 43,200 in special charges). Dolt value does NOT reconcile with Net Profit: if Op Profit = 33,400, then after interest (−22,100) = 11,300 pretax → Net ≈ +12,400, but actual Net Profit = −30,800. GAAP basis (−9,800) reconciles correctly: −9,800 − 22,100 = −31,900 → with tax credit +1,100 → Net = −30,800 ✓. Must correct.
- All other fields confirmed against Yahoo ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | 3,936,500 | 3,936,500 | 3,936,500 |
| Cost of Goods | — | 2,219,000 | 2,219,000 | 2,219,000 |
| Gross Margin | — | 1,717,500 | 1,717,500 | 1,717,500 |
| SGA | — | 1,694,000 | 1,694,000 | 1,694,000 |
| Operating Profit | — | -9,800* | 33,400* | **-9,800** |
| Net Profit | — | -30,800 | -30,800 | -30,800 |
| Inventory | — | 1,078,400 | 1,078,400 | 1,078,400 |
| Current Assets | — | 1,554,000 | 1,554,000 | 1,554,000 |
| Total Assets | — | 2,996,900 | 2,996,900 | 2,996,900 |
| Current Liabilities | — | 1,040,000 | 1,040,000 | 1,040,000 |
| Liabilities | — | 1,982,000 | 1,982,000 | 1,982,000 |
| Total SE | — | 1,014,900 | 1,014,900 | 1,014,900 |
| Total L+SE | — | 2,996,900 | 2,996,900 | 2,996,900 |

*Yahoo "Operating Income" (adjusted, excl special charges) = 33,400; Yahoo "Total Operating Income As Reported" (GAAP) = -9,800. Dolt stored the adjusted figure. Correcting to GAAP.

**Action: Correction — Operating Profit: 33,400 → -9,800**

---

## FY2023

**Sources:** Yahoo Finance + Dolt

### Anomaly Detection
- Gross margin: 1,459,000 / 3,549,500 = 41.1% — within Specialty range (35–55%) ✓
- Balance sheet: 1,758,900 + 866,700 = 2,625,600 = Total Assets ✓
- Yahoo "Operating Income" and "Total Operating Income As Reported" both = -248,500 (no special charges this year) ✓
- All fields confirmed against Yahoo ✓

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

**Sources:** Yahoo Finance + Dolt

### Anomaly Detection
- Gross margin: 1,162,500 / 2,905,800 = 40.0% — within Specialty range (35–55%) ✓
- Balance sheet: 1,749,900 + 521,300 = 2,271,200 = Total Assets ✓
- `[ERROR]` SGA discrepancy: Dolt has 1,496,400 which includes special charges/impairments (~144,900) not captured in Yahoo's SGA line. Yahoo "Selling General And Administration" = 1,340,800 (Selling & Marketing 326,100 + G&A 1,014,700). Per anomaly rules, impairment/restructuring must be excluded from SGA. Correcting to 1,340,800.
- Operating Profit: Dolt -331,900 = Yahoo "Total Operating Income As Reported" (GAAP) ✓ — no change.
- All balance sheet fields confirmed ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | 2,905,800 | 2,905,800 | 2,905,800 |
| Cost of Goods | — | 1,743,300 | 1,743,300 | 1,743,300 |
| Gross Margin | — | 1,162,500 | 1,162,500 | 1,162,500 |
| SGA | — | 1,340,800* | 1,496,400* | **1,340,800** |
| Operating Profit | — | -331,900 | -331,900 | -331,900 |
| Net Profit | — | -338,700 | -338,700 | -338,700 |
| Inventory | — | 520,300 | 520,300 | 520,300 |
| Current Assets | — | 1,146,400 | 1,146,400 | 1,146,400 |
| Total Assets | — | 2,271,200 | 2,271,200 | 2,271,200 |
| Current Liabilities | — | 714,000 | 714,000 | 714,000 |
| Liabilities | — | 1,749,900 | 1,749,900 | 1,749,900 |
| Total SE | — | 521,300 | 521,300 | 521,300 |
| Total L+SE | — | 2,271,200 | 2,271,200 | 2,271,200 |

*Yahoo SGA line (excl special charges) = 1,340,800; Dolt 1,496,400 incorrectly included ~155,600 of special charges. Note: Operating Profit (-331,900) includes special charges per GAAP — the gap between Gross−SGA and Operating Profit is explained by impairment charges not recorded in SGA.

**Action: Correction — SGA: 1,496,400 → 1,340,800**

---

## FY2025

**Sources:** Yahoo Finance only (new insert — no existing Dolt row)

### Anomaly Detection
- Gross margin: 1,166,700 / 2,477,800 = 47.1% — within Specialty range (35–55%) ✓
- Balance sheet: 1,459,700 + 212,400 = 1,672,100 = Total Assets ✓
- Operating Profit: -212,300 = Yahoo "Total Operating Income As Reported" (GAAP, includes 177,300 special charges). Adjusted/underlying = -35,000.
- SGA: 1,199,900 = Selling & Marketing (262,300) + G&A (937,600) ✓
- Continued declining trend in revenue and inventory consistent with ASOS's ongoing restructuring program.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | 2,477,800 | — | 2,477,800 |
| Cost of Goods | — | 1,311,100 | — | 1,311,100 |
| Gross Margin | — | 1,166,700 | — | 1,166,700 |
| SGA | — | 1,199,900 | — | 1,199,900 |
| Operating Profit | — | -212,300 | — | -212,300 |
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

**Analysis complete.** Run `/insert-financials ASOMF` to write all changed years to the database.

**Unresolved flags to review before inserting:**
- FY2019/2020/2021: Cannot be verified (no external source). Values retained as-is.
- FY2022: Operating Profit corrected from adjusted (33,400) to GAAP reported (-9,800). Confirms ASOS had a reported operating loss in FY2022 despite "underlying" profitability.
- FY2024: SGA corrected to exclude impairment charges. Note that Operating Profit (-331,900) will not reconcile to Gross−SGA due to impairment charges sitting between the two lines.
