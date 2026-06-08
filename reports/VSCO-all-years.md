# Victoria's Secret (VSCO) — FY2020–FY2025 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2020 | 2021-01-30 | Correction: reportDate '2021-01-31' → '2021-01-30' |
| 2021 | 2022-01-29 | No change |
| 2022 | 2023-01-28 | No change |
| 2023 | 2024-02-03 | Correction: NetInc $116,000K → $109,000K (wrong line item) |
| 2024 | 2025-02-01 | Correction: TSE $664,000K → $640,000K; Liab $3,868,000K → $3,892,000K (minority interest misclassification) |
| 2025 | 2026-01-31 | New insert |

---

## Company Notes

**Segment:** Specialty (lingerie/intimate apparel) — brands: Victoria's Secret, PINK, Adore Me

**Fiscal year:** Ends late January/early February. FY2025 = fiscal year ending 2026-01-31.

**History:** Spun off from L Brands on August 2, 2021 (CIK 1856437). FY2020 data is carved-out from L Brands historical financials; no standalone 10-K exists for FY2020.

**SGA construction:** Single combined `us-gaap_SellingGeneralAndAdministrativeExpense` line. No separate marketing or ops split. Use directly.

**Minority interest (CRITICAL):** VSCO has a Chinese JV with a noncontrolling interest starting FY2022. The DB convention for this company is:
- **TSE = `us-gaap_StockholdersEquity`** (common shareholders only, excluding minority interest)
- **Liabilities = Total Assets − TSE** (implicitly includes minority interest in "liabilities")
- Do NOT use `us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest` for TSE

**Net Income:** Always use `us-gaap_NetIncomeLoss` (attributable to common shareholders). Do NOT use `us-gaap_ProfitLoss` (consolidated including NCI). These differ by the NCI's income/loss for the period.

---

## FY2020 (ends 2021-01-30)

### Anomaly Detection

- **[WARNING] reportDate '2021-01-31' in Dolt vs '2021-01-30' per SEC:** L Brands FY2020 fiscal year ended January 30, 2021. The VSCO FY2020 carved-out financials use this date. Dolt has '2021-01-31' (off by 1 day).
- **[WARNING] Balance sheet unverifiable from standalone 10-K:** VSCO CIK 1856437 has no FY2020 10-K (spinoff occurred August 2021). Balance sheet likely sourced from VSCO's S-1/registration statement carved-out financials. Cannot cross-check via SEC MCP.
- Income statement data confirmed from FY2021 10-K comparative (2021-01-30 column).
- Gross margin: $1,571K / $5,413K = 29.0% — below specialty range (35–55%), expected for COVID-impacted year. [WARNING — COVID year]
- Balance identity check (from Dolt): $3,338,000 + $891,000 = $4,229,000 ✓
- No minority interest in FY2020 (pre-spinoff carve-out).

### Side-by-Side Comparison

| Field | SEC (FY2021 10-K comparative) | Yahoo | Dolt (current) | Recommended |
|-------|-------------------------------|-------|----------------|-------------|
| reportDate | **2021-01-30** | — | **2021-01-31*** | **2021-01-30** |
| Net Revenue | 5,413,000 | — | 5,413,000 | 5,413,000 |
| Cost of Goods | 3,842,000 | — | 3,842,000 | 3,842,000 |
| Gross Margin | 1,571,000 | — | 1,571,000 | 1,571,000 |
| SGA | 1,672,000 | — | 1,672,000 | 1,672,000 |
| Operating Profit | −101,000 | — | −101,000 | −101,000 |
| Net Profit | −72,000 | — | −72,000 | −72,000 |
| Inventory | (unverifiable) | — | 701,000 | 701,000 |
| Current Assets | (unverifiable) | — | 1,239,000 | 1,239,000 |
| Total Assets | (unverifiable) | — | 4,229,000 | 4,229,000 |
| Current Liabilities | (unverifiable) | — | 1,556,000 | 1,556,000 |
| Liabilities | (unverifiable) | — | 3,338,000 | 3,338,000 |
| Total Shareholder Equity | (unverifiable) | — | 891,000 | 891,000 |
| Total Liab and SE | (unverifiable) | — | 4,229,000 | 4,229,000 |

*reportDate in Dolt = 2021-01-31; SEC shows 2021-01-30 as the actual L Brands fiscal year end.

### Reconciled Recommendation

- **reportDate:** '2021-01-30' (from SEC). Dolt has '2021-01-31'. **Overwrite.**
- All financial values: Income statement confirmed correct. Balance sheet accepted as-is (source unverifiable but balance identity holds).

---

## FY2021 (ends 2022-01-29)

### Anomaly Detection

- Gross margin: $2,760K / $6,785K = 40.7% — within specialty range ✓
- Balance identity: $4,087,000 + $257,000 = $4,344,000 ✓
- No minority interest in FY2021 balance sheet.
- Strong recovery year post-COVID; OpInc $870M vs −$101M prior year.

### Side-by-Side Comparison

| Field | SEC (FY2021 10-K) | Yahoo | Dolt (current) | Recommended |
|-------|-------------------|-------|----------------|-------------|
| reportDate | 2022-01-29 | — | 2022-01-29 | 2022-01-29 |
| Net Revenue | 6,785,000 | — | 6,785,000 | 6,785,000 |
| Cost of Goods | 4,025,000 | — | 4,025,000 | 4,025,000 |
| Gross Margin | 2,760,000 | — | 2,760,000 | 2,760,000 |
| SGA | 1,890,000 | — | 1,890,000 | 1,890,000 |
| Operating Profit | 870,000 | — | 870,000 | 870,000 |
| Net Profit | 646,000 | — | 646,000 | 646,000 |
| Inventory | 949,000 | — | 949,000 | 949,000 |
| Current Assets | 1,691,000 | — | 1,691,000 | 1,691,000 |
| Total Assets | 4,344,000 | — | 4,344,000 | 4,344,000 |
| Current Liabilities | 1,698,000 | — | 1,698,000 | 1,698,000 |
| Liabilities | 4,087,000 | — | 4,087,000 | 4,087,000 |
| Total Shareholder Equity | 257,000 | — | 257,000 | 257,000 |
| Total Liab and SE | 4,344,000 | — | 4,344,000 | 4,344,000 |

### Reconciled Recommendation

All 14 fields match SEC exactly. **No change needed.**

---

## FY2022 (ends 2023-01-28)

### Anomaly Detection

- Gross margin: $2,258K / $6,344K = 35.6% — at the lower bound of specialty range. [WARNING — monitor trend]
- Balance identity: $4,328,000 + $383,000 = $4,711,000 ✓
- Minority interest: $18M (Chinese JV). Dolt TSE = $383K (common only, correct per DB convention).
- DB Liab = $4,711K − $383K = $4,328K. SEC Total Liabilities = $4,310K. Difference = $18K = minority interest (included in DB Liab field by convention). ✓

### Side-by-Side Comparison

| Field | SEC (FY2022 10-K) | Yahoo (FY2022) | Dolt (current) | Recommended |
|-------|-------------------|----------------|----------------|-------------|
| reportDate | 2023-01-28 | — | 2023-01-28 | 2023-01-28 |
| Net Revenue | 6,344,000 | 6,344,000 | 6,344,000 | 6,344,000 |
| Cost of Goods | 4,086,000 | 4,086,000 | 4,086,000 | 4,086,000 |
| Gross Margin | 2,258,000 | — | 2,258,000 | 2,258,000 |
| SGA | 1,780,000 | 1,780,000 | 1,780,000 | 1,780,000 |
| Operating Profit | 478,000 | 478,000 | 478,000 | 478,000 |
| Net Profit | 348,000 | 348,000 | 348,000 | 348,000 |
| Inventory | 1,052,000 | 1,052,000 | 1,052,000 | 1,052,000 |
| Current Assets | 1,737,000 | 1,737,000 | 1,737,000 | 1,737,000 |
| Total Assets | 4,711,000 | 4,711,000 | 4,711,000 | 4,711,000 |
| Current Liabilities | 1,579,000 | 1,579,000 | 1,579,000 | 1,579,000 |
| Liabilities | 4,328,000 | — | 4,328,000 | 4,328,000 |
| Total Shareholder Equity | 383,000 | 383,000 | 383,000 | 383,000 |
| Total Liab and SE | 4,711,000 | 4,711,000 | 4,711,000 | 4,711,000 |

### Reconciled Recommendation

All fields match SEC. **No change needed.**

---

## FY2023 (ends 2024-02-03)

### Anomaly Detection

- **[ERROR] NetInc $116,000K in Dolt — wrong line item:** Dolt used `us-gaap_ProfitLoss` ($116M, consolidated including NCI) instead of `us-gaap_NetIncomeLoss` ($109M, attributable to common shareholders). Noncontrolling interest had income of $7M in FY2023, reducing parent's share. Confirmed by Yahoo ($109K) and EPS × shares (Basic EPS $1.41 × ~78M shares ≈ $110M).
- Gross margin: $2,242K / $6,182K = 36.3% — within range ✓
- Balance identity: $4,183,000 + $417,000 = $4,600,000 ✓
- Minority interest: $21M. Dolt TSE = $417K (common only, correct).
- Asset impairment: $6,404K (Nuuly Thrift) — wait, that's URBN not VSCO. No impairment noted for VSCO FY2023.

### Side-by-Side Comparison

| Field | SEC (FY2023 10-K) | Yahoo (FY2023) | Dolt (current) | Recommended |
|-------|-------------------|----------------|----------------|-------------|
| reportDate | 2024-02-03 | — | 2024-02-03 | 2024-02-03 |
| Net Revenue | 6,182,000 | 6,182,000 | 6,182,000 | 6,182,000 |
| Cost of Goods | 3,940,000 | 3,940,000 | 3,940,000 | 3,940,000 |
| Gross Margin | 2,242,000 | — | 2,242,000 | 2,242,000 |
| SGA | 1,996,000 | 1,996,000 | 1,996,000 | 1,996,000 |
| Operating Profit | 246,000 | 246,000 | 246,000 | 246,000 |
| Net Profit | **109,000** | **109,000** | **116,000*** | **109,000** |
| Inventory | 985,000 | 985,000 | 985,000 | 985,000 |
| Current Assets | 1,533,000 | 1,533,000 | 1,533,000 | 1,533,000 |
| Total Assets | 4,600,000 | 4,600,000 | 4,600,000 | 4,600,000 |
| Current Liabilities | 1,614,000 | 1,614,000 | 1,614,000 | 1,614,000 |
| Liabilities | 4,183,000 | — | 4,183,000 | 4,183,000 |
| Total Shareholder Equity | 417,000 | 417,000 | 417,000 | 417,000 |
| Total Liab and SE | 4,600,000 | 4,600,000 | 4,600,000 | 4,600,000 |

*Dolt NetInc = $116,000K = us-gaap_ProfitLoss (consolidated). Correct = $109,000K = us-gaap_NetIncomeLoss (to common). NCI income = $7,000K; $116K − $7K = $109K.

### Reconciled Recommendation

- **Net Profit:** $109,000K. **Overwrite** (was $116,000K — wrong line item).
- All other fields: unchanged.

---

## FY2024 (ends 2025-02-01)

### Anomaly Detection

- **[WARNING] TSE $664,000K in Dolt uses total equity including minority interest:** Inconsistent with FY2022 ($383K, common only) and FY2023 ($417K, common only). FY2024 Dolt TSE = $664K = `us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest` (common $640K + minority $24K). Correct value per DB convention = $640K (common only). Yahoo also shows Common Stock Equity = $640K.
- **[WARNING] Liab $3,868,000K in Dolt = SEC Total Liabilities (excludes minority).** Per DB convention (Liab = TA − TSE_common), should be $4,532K − $640K = $3,892K (includes $24K minority in "liabilities").
- Gross margin: $2,284K / $6,230K = 36.7% — within range ✓
- Balance identity (corrected): $3,892,000 + $640,000 = $4,532,000 ✓

### Side-by-Side Comparison

| Field | SEC (FY2024 10-K) | Yahoo (FY2024) | Dolt (current) | Recommended |
|-------|-------------------|----------------|----------------|-------------|
| reportDate | 2025-02-01 | — | 2025-02-01 | 2025-02-01 |
| Net Revenue | 6,230,000 | 6,230,000 | 6,230,000 | 6,230,000 |
| Cost of Goods | 3,946,000 | 3,946,000 | 3,946,000 | 3,946,000 |
| Gross Margin | 2,284,000 | — | 2,284,000 | 2,284,000 |
| SGA | 1,974,000 | 1,974,000 | 1,974,000 | 1,974,000 |
| Operating Profit | 310,000 | 310,000 | 310,000 | 310,000 |
| Net Profit | 165,000 | 165,000 | 165,000 | 165,000 |
| Inventory | 955,000 | 955,000 | 955,000 | 955,000 |
| Current Assets | 1,441,000 | 1,441,000 | 1,441,000 | 1,441,000 |
| Total Assets | 4,532,000 | 4,532,000 | 4,532,000 | 4,532,000 |
| Current Liabilities | 1,375,000 | 1,375,000 | 1,375,000 | 1,375,000 |
| Liabilities | **3,892,000** | — | **3,868,000*** | **3,892,000** |
| Total Shareholder Equity | **640,000** | **640,000** | **664,000*** | **640,000** |
| Total Liab and SE | 4,532,000 | 4,532,000 | 4,532,000 | 4,532,000 |

*Dolt TSE = $664K = total equity incl. minority $24K. Correct = $640K (common only per DB convention).
*Dolt Liab = $3,868K = TA − $664K. Correct = $3,892K = TA − $640K.

### Reconciled Recommendation

- **Total Shareholder Equity:** $640,000K (common only). **Overwrite** (was $664K including minority).
- **Liabilities:** $3,892,000K (= TA − TSE = $4,532K − $640K). **Overwrite** (was $3,868K).
- All other fields: unchanged.

---

## FY2025 (ends 2026-01-31) — NEW INSERT

### Anomaly Detection

- Gross margin: $2,384K / $6,553K = 36.4% — within specialty range ✓
- Balance identity: $4,157,000 + $856,000 = $5,013,000 ✓
- Minority interest: $54M. TSE = $856K (common only, per DB convention).
  DB Liab = TA ($5,013K) − TSE ($856K) = $4,157K. SEC Total Liabilities = $4,103K. Difference = $54K = minority interest (included in DB Liab). ✓
- Yahoo and SEC agree on all fields exactly.
- NetInc: SEC NetIncomeLoss = $161K (to common). ProfitLoss = $189K (consolidated). NCI income = $28K. $189K − $28K = $161K ✓. Yahoo confirms $161K.
- No impairment charges in FY2025.

### Side-by-Side Comparison

| Field | SEC (FY2025 10-K) | Yahoo (FY2025) | Dolt (current) | Recommended |
|-------|-------------------|----------------|----------------|-------------|
| reportDate | 2026-01-31 | 2026-01-31 | (not in DB) | 2026-01-31 |
| Net Revenue | 6,553,000 | 6,553,000 | — | 6,553,000 |
| Cost of Goods | 4,169,000 | 4,169,000 | — | 4,169,000 |
| Gross Margin | 2,384,000 | — | — | 2,384,000 |
| SGA | 2,113,000 | 2,113,000 | — | 2,113,000 |
| Operating Profit | 271,000 | 271,000 | — | 271,000 |
| Net Profit | 161,000 | 161,000 | — | 161,000 |
| Inventory | 1,071,000 | 1,071,000 | — | 1,071,000 |
| Current Assets | 1,883,000 | 1,883,000 | — | 1,883,000 |
| Total Assets | 5,013,000 | 5,013,000 | — | 5,013,000 |
| Current Liabilities | 1,507,000 | 1,507,000 | — | 1,507,000 |
| Liabilities | 4,157,000 | — | — | 4,157,000 |
| Total Shareholder Equity | 856,000 | 856,000 | — | 856,000 |
| Total Liab and SE | 5,013,000 | 5,013,000 | — | 5,013,000 |

Gross Margin: $6,553,000 − $4,169,000 = $2,384,000 ✓
OpInc check: $2,384,000 − $2,113,000 = $271,000 ✓
Liab: $5,013,000 − $856,000 = $4,157,000 (includes $54K minority) ✓

---

## Analysis Complete

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql VSCO` to write all changed years to the database.

**Changes to apply:**
- FY2020 correction: reportDate '2021-01-31' → '2021-01-30'
- FY2023 correction: NetInc $116,000K → $109,000K (wrong line item — was consolidated ProfitLoss)
- FY2024 correction: TSE $664,000K → $640,000K; Liab $3,868,000K → $3,892,000K (minority interest misclassification)
- FY2025 new insert (reportDate 2026-01-31)

**Flags for review:**
- [WARNING] FY2020 balance sheet unverifiable from standalone 10-K (pre-spinoff carve-out data). Values accepted as-is since balance identity holds.
- [WARNING] FY2020 gross margin 29.0% below specialty range — COVID-impacted year, expected.
- [WARNING] FY2025 minority interest ($54M) is significantly larger than prior years ($18–24M), reflecting growth of Chinese JV. This affects the DB Liab field (includes $54M) but TSE correctly uses common-only equity.
