# Walgreens (WBA) — FY2019–FY2024 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2019 | 2019-08-31 | No change |
| 2020 | 2020-08-31 | No change |
| 2021 | 2021-08-31 | No change (SEC unavailable — unverified) |
| 2022 | 2022-08-31 | Correction: NetProfit $4,065,000K → $4,337,000K (wrong line item) |
| 2023 | 2023-08-31 | Correction: NetProfit −$3,528,000K → −$3,080,000K (wrong line item) |
| 2024 | 2024-08-31 | Correction: Liab $68,992,000K → $69,032,000K (balance identity failure) |

---

## Company Notes

**Segment:** Health & Pharmacy (drug store chain with international operations — Boots UK, wholesale)

**Fiscal year:** Ends August 31 each year. FY2024 = fiscal year ending 2024-08-31.

**Went private:** Sycamore Partners acquisition closed March 2025. No Yahoo Finance data available for WBA. FY2025 (ending Aug 31, 2025) data status unknown.

**SGA construction:** Single combined `us-gaap_SellingGeneralAndAdministrativeExpense` line. No separate marketing or ops-tech split. Use directly. Note: FY2023 SGA ($34.2B) includes opioid litigation settlement reserves (~$6.9B jump from FY2022). FY2024 has a SEPARATE `us-gaap_GoodwillImpairmentLoss` line ($12.7B) that is NOT in SGA.

**Minority interest (CRITICAL):** WBA has substantial noncontrolling interests (Boots UK minority, VillageMD/CityMD in FY2022–FY2024). DB convention:
- **TSE = `us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest`** (total equity including NCI)
- **Liabilities = Total Assets − TSE** (excludes NCI from "liabilities")
- This is the OPPOSITE of VSCO's convention

**Net Income:** Always use `us-gaap_NetIncomeLoss` (attributable to parent). Do NOT use `us-gaap_ProfitLoss` (consolidated). NCI entities (VillageMD, CityMD) had massive losses in FY2022–FY2024 that must be excluded from the parent's Net Profit. The NCI loss is absorbed by minority investors, raising the parent's net income above consolidated profit.

**Gross margin:** 18–25% expected (Health & Pharmacy segment). Declining trend (22% in FY2019 → 18% in FY2024) reflects pharmacy mix shift and reimbursement pressure — expected, not an anomaly.

**SEC data availability:** FY2021, FY2022, FY2023 10-K filings return `'NoneType' object has no attribute 'to_dataframe'` from the SEC MCP. Income data for FY2022 and FY2023 is available from the FY2024 10-K comparative (per restatement rule). Balance sheet data for FY2021–FY2023 is unverifiable.

---

## FY2019 (ends 2019-08-31)

### Anomaly Detection

- Gross margin: $30,076K / $136,866K = 22.0% — within Health & Pharmacy range ✓
- Balance identity: $43,446,000 + $24,152,000 = $67,598,000 ✓
- TSE = StockholdersEquityIncludingNCI: $23,512K (common) + $641K (minority) = $24,152K ✓
- NetIncomeLoss = $3,982K = NetIncomeLoss (to parent) ✓. ProfitLoss = $3,962K + NCI loss $20K = NetIncomeLoss $3,982K ✓
- SGA: single line $25,242K, no composite needed ✓

### Side-by-Side Comparison

| Field | SEC (FY2019 10-K) | Yahoo | Dolt (current) | Recommended |
|-------|-------------------|-------|----------------|-------------|
| reportDate | 2019-08-31 | — | 2019-08-31 | 2019-08-31 |
| Net Revenue | 136,866,000 | — | 136,866,000 | 136,866,000 |
| Cost of Goods | 106,790,000 | — | 106,790,000 | 106,790,000 |
| Gross Margin | 30,076,000 | — | 30,076,000 | 30,076,000 |
| SGA | 25,242,000 | — | 25,242,000 | 25,242,000 |
| Operating Profit | 4,998,000 | — | 4,998,000 | 4,998,000 |
| Net Profit | 3,982,000 | — | 3,982,000 | 3,982,000 |
| Inventory | 9,333,000 | — | 9,333,000 | 9,333,000 |
| Current Assets | 18,700,000 | — | 18,700,000 | 18,700,000 |
| Total Assets | 67,598,000 | — | 67,598,000 | 67,598,000 |
| Current Liabilities | 25,769,000 | — | 25,769,000 | 25,769,000 |
| Liabilities | 43,446,000 | — | 43,446,000 | 43,446,000 |
| Total Shareholder Equity | 24,152,000 | — | 24,152,000 | 24,152,000 |
| Total Liab and SE | 67,598,000 | — | 67,598,000 | 67,598,000 |

### Reconciled Recommendation

All fields match SEC. **No change needed.**

---

## FY2020 (ends 2020-08-31)

### Anomaly Detection

- Gross margin: $28,017K / $139,537K = 20.1% — within Health & Pharmacy range ✓
- Balance identity: $66,038,000 + $21,136,000 = $87,174,000 ✓
- TSE = StockholdersEquityIncludingNCI: $20,637K (common) + $498K (minority) = $21,136K ✓
- NetIncomeLoss = $456K = NetIncomeLoss (to parent) ✓. ProfitLoss = $424K + NCI loss $32K = $456K ✓
- ASC 842 operating lease ROU assets added: $21,724K in non-current assets. Total Assets jumped from $67,598K (FY2019) to $87,174K (FY2020). Expected — lease accounting change.

### Side-by-Side Comparison

| Field | SEC (FY2020 10-K) | Yahoo | Dolt (current) | Recommended |
|-------|-------------------|-------|----------------|-------------|
| reportDate | 2020-08-31 | — | 2020-08-31 | 2020-08-31 |
| Net Revenue | 139,537,000 | — | 139,537,000 | 139,537,000 |
| Cost of Goods | 111,520,000 | — | 111,520,000 | 111,520,000 |
| Gross Margin | 28,017,000 | — | 28,017,000 | 28,017,000 |
| SGA | 27,045,000 | — | 27,045,000 | 27,045,000 |
| Operating Profit | 1,312,000 | — | 1,312,000 | 1,312,000 |
| Net Profit | 456,000 | — | 456,000 | 456,000 |
| Inventory | 9,451,000 | — | 9,451,000 | 9,451,000 |
| Current Assets | 18,073,000 | — | 18,073,000 | 18,073,000 |
| Total Assets | 87,174,000 | — | 87,174,000 | 87,174,000 |
| Current Liabilities | 27,070,000 | — | 27,070,000 | 27,070,000 |
| Liabilities | 66,038,000 | — | 66,038,000 | 66,038,000 |
| Total Shareholder Equity | 21,136,000 | — | 21,136,000 | 21,136,000 |
| Total Liab and SE | 87,174,000 | — | 87,174,000 | 87,174,000 |

### Reconciled Recommendation

All fields match SEC. **No change needed.**

---

## FY2021 (ends 2021-08-31)

### Anomaly Detection

- **[WARNING] SEC data unavailable:** The SEC MCP cannot parse the WBA FY2021 10-K filing (returns NoneType error). Income statement and balance sheet unverifiable.
- Gross margin: $28,067K / $132,509K = 21.2% — within range ✓
- Balance identity: $57,463,000 + $23,822,000 = $81,285,000 ✓
- TSE convention: cannot verify from SEC, but $23,822K is plausible between FY2020 ($21,136K) and FY2022 ($25,275K).
- NetProfit $2,512K > OpInc $2,342K: attributable to equity earnings in AmerisourceBergen/Cencora and other equity method investments. Plausible. VillageMD acquisition closed Oct 2021 (after FY2021 fiscal year end) — minimal NCI impact in FY2021.

### Side-by-Side Comparison

| Field | SEC (FY2021 10-K) | Yahoo | Dolt (current) | Recommended |
|-------|-------------------|-------|----------------|-------------|
| reportDate | (unavailable) | — | 2021-08-31 | 2021-08-31 |
| Net Revenue | (unavailable) | — | 132,509,000 | 132,509,000 |
| Cost of Goods | (unavailable) | — | 104,442,000 | 104,442,000 |
| Gross Margin | (unavailable) | — | 28,067,000 | 28,067,000 |
| SGA | (unavailable) | — | 24,586,000 | 24,586,000 |
| Operating Profit | (unavailable) | — | 2,342,000 | 2,342,000 |
| Net Profit | (unavailable) | — | 2,512,000 | 2,512,000 |
| Inventory | (unavailable) | — | 8,159,000 | 8,159,000 |
| Current Assets | (unavailable) | — | 15,814,000 | 15,814,000 |
| Total Assets | (unavailable) | — | 81,285,000 | 81,285,000 |
| Current Liabilities | (unavailable) | — | 22,054,000 | 22,054,000 |
| Liabilities | (unavailable) | — | 57,463,000 | 57,463,000 |
| Total Shareholder Equity | (unavailable) | — | 23,822,000 | 23,822,000 |
| Total Liab and SE | (unavailable) | — | 81,285,000 | 81,285,000 |

### Reconciled Recommendation

SEC data unavailable. Balance identity holds. All values accepted as-is. **No change.**

---

## FY2022 (ends 2022-08-31)

### Anomaly Detection

- **[ERROR] NetProfit $4,065,000K in Dolt — wrong line item:** Dolt used `us-gaap_ProfitLoss` ($4,065M, consolidated including NCI) instead of `us-gaap_NetIncomeLoss` ($4,337M, attributable to parent). NCI entities (VillageMD, CityMD, Shields Health) had net losses of $271M in FY2022, absorbed by minority investors. Parent net income is HIGHER than consolidated. Confirmed from FY2024 10-K comparative.
- **[WARNING] Balance sheet unverifiable:** SEC MCP cannot parse FY2022 10-K. Balance sheet values accepted as-is from Dolt.
- Gross margin: $28,266K / $132,703K = 21.3% — within range ✓
- Balance identity: $64,849,000 + $25,275,000 = $90,124,000 ✓
- SGA $27,295K within normal range for WBA (vs FY2019 $25,242K). No anomaly.
- Source: FY2024 10-K income statement comparative (2022-08-31 column) per restatement rule.

### Side-by-Side Comparison

| Field | SEC (FY2024 10-K comparative) | Yahoo | Dolt (current) | Recommended |
|-------|-------------------------------|-------|----------------|-------------|
| reportDate | 2022-08-31 | — | 2022-08-31 | 2022-08-31 |
| Net Revenue | 132,703,000 | — | 132,703,000 | 132,703,000 |
| Cost of Goods | 104,437,000 | — | 104,437,000 | 104,437,000 |
| Gross Margin | 28,266,000 | — | 28,266,000 | 28,266,000 |
| SGA | 27,295,000 | — | 27,295,000 | 27,295,000 |
| Operating Profit | 1,387,000 | — | 1,387,000 | 1,387,000 |
| Net Profit | **4,337,000** | — | **4,065,000*** | **4,337,000** |
| Inventory | (unavailable) | — | 8,353,000 | 8,353,000 |
| Current Assets | (unavailable) | — | 16,902,000 | 16,902,000 |
| Total Assets | (unavailable) | — | 90,124,000 | 90,124,000 |
| Current Liabilities | (unavailable) | — | 22,583,000 | 22,583,000 |
| Liabilities | (unavailable) | — | 64,849,000 | 64,849,000 |
| Total Shareholder Equity | (unavailable) | — | 25,275,000 | 25,275,000 |
| Total Liab and SE | (unavailable) | — | 90,124,000 | 90,124,000 |

*Dolt NetProfit = $4,065,000K = us-gaap_ProfitLoss (consolidated). Correct = $4,337,000K = us-gaap_NetIncomeLoss (to parent). NCI had net loss of $271,000K; $4,065K + $271K = $4,336K ≈ $4,337K (rounding).

### Reconciled Recommendation

- **Net Profit:** $4,337,000K. **Overwrite** (was $4,065,000K — wrong line item).
- Balance sheet: accepted as-is (unverifiable, but identity holds).

---

## FY2023 (ends 2023-08-31)

### Anomaly Detection

- **[ERROR] NetProfit −$3,528,000K in Dolt — wrong line item:** Dolt used `us-gaap_ProfitLoss` (−$3,528M, consolidated) instead of `us-gaap_NetIncomeLoss` (−$3,080M, to parent). NCI entities absorbed losses of $448M in FY2023. Parent's net loss is SMALLER than consolidated. Confirmed from FY2024 10-K comparative.
- **[WARNING] Balance sheet unverifiable:** SEC MCP cannot parse FY2023 10-K.
- **[WARNING] SGA large jump:** $34,205K vs $27,295K in FY2022 (+$6.9B). Includes opioid litigation settlement reserves classified within `us-gaap_SellingGeneralAndAdministrativeExpense` per WBA's income statement. This is correctly recorded per SEC reporting — not a data entry error.
- Gross margin: $27,072K / $139,081K = 19.5% — within Health & Pharmacy range ✓
- Balance identity: $68,306,000 + $28,322,000 = $96,628,000 ✓
- Note: TSE = $28,322K is elevated due to large NCI equity from VillageMD/CityMD. This collapses in FY2024 when VillageMD goodwill was impaired.

### Side-by-Side Comparison

| Field | SEC (FY2024 10-K comparative) | Yahoo | Dolt (current) | Recommended |
|-------|-------------------------------|-------|----------------|-------------|
| reportDate | 2023-08-31 | — | 2023-08-31 | 2023-08-31 |
| Net Revenue | 139,081,000 | — | 139,081,000 | 139,081,000 |
| Cost of Goods | 112,009,000 | — | 112,009,000 | 112,009,000 |
| Gross Margin | 27,072,000 | — | 27,072,000 | 27,072,000 |
| SGA | 34,205,000 | — | 34,205,000 | 34,205,000 |
| Operating Profit | −6,882,000 | — | −6,882,000 | −6,882,000 |
| Net Profit | **−3,080,000** | — | **−3,528,000*** | **−3,080,000** |
| Inventory | (unavailable) | — | 8,257,000 | 8,257,000 |
| Current Assets | (unavailable) | — | 15,503,000 | 15,503,000 |
| Total Assets | (unavailable) | — | 96,628,000 | 96,628,000 |
| Current Liabilities | (unavailable) | — | 24,535,000 | 24,535,000 |
| Liabilities | (unavailable) | — | 68,306,000 | 68,306,000 |
| Total Shareholder Equity | (unavailable) | — | 28,322,000 | 28,322,000 |
| Total Liab and SE | (unavailable) | — | 96,628,000 | 96,628,000 |

*Dolt NetProfit = −$3,528,000K = us-gaap_ProfitLoss (consolidated). Correct = −$3,080,000K = us-gaap_NetIncomeLoss (to parent). NCI absorbed $448,000K losses; −$3,528K + $448K = −$3,080K ✓.

### Reconciled Recommendation

- **Net Profit:** −$3,080,000K. **Overwrite** (was −$3,528,000K — wrong line item).
- Balance sheet: accepted as-is (unverifiable, but identity holds).

---

## FY2024 (ends 2024-08-31)

### Anomaly Detection

- **[ERROR] Balance sheet identity failure:** Dolt Liab $68,992,000 + TSE $12,005,000 = $80,997,000 ≠ TA $81,037,000 (off by $40,000K = $40M). This violates the balance sheet identity rule. Correct Liab = TA − TSE = $81,037,000 − $12,005,000 = **$69,032,000**.
  - SEC breakdown: Total Liabilities $68,858K + Redeemable NCI $174K = $69,032K = TA − TSE ✓ (Redeemable NCI is absorbed into DB "Liabilities" per convention).
  - Dolt's $68,992K corresponds to no clean balance sheet line item.
- **[WARNING] Very large goodwill impairment:** $12,701M for VillageMD (U.S. Healthcare) — reported as separate `us-gaap_GoodwillImpairmentLoss` line, NOT in SGA. SGA = $28,113M is correctly net of this impairment.
- **[WARNING] NCI collapse:** TSE dropped from $28,322K (FY2023) to $12,005K (FY2024), a decline of $16,317K in one year, driven by VillageMD impairment and NCI ($6,812M NCI net loss absorbed in FY2024).
- Gross margin: $26,524K / $147,658K = 18.0% — within Health & Pharmacy range (lower bound) ✓
- TSE = StockholdersEquityIncludingNCI: $10,445K (common) + $1,561K (minority) = $12,006K ≈ $12,005K (rounding) ✓
- NetIncomeLoss = −$8,636K ✓. ProfitLoss = −$15,448K. NCI loss absorbed = $6,812K. −$15,448K + $6,812K = −$8,636K ✓

### Side-by-Side Comparison

| Field | SEC (FY2024 10-K) | Yahoo | Dolt (current) | Recommended |
|-------|-------------------|-------|----------------|-------------|
| reportDate | 2024-08-31 | — | 2024-08-31 | 2024-08-31 |
| Net Revenue | 147,658,000 | — | 147,658,000 | 147,658,000 |
| Cost of Goods | 121,134,000 | — | 121,134,000 | 121,134,000 |
| Gross Margin | 26,524,000 | — | 26,524,000 | 26,524,000 |
| SGA | 28,113,000 | — | 28,113,000 | 28,113,000 |
| Operating Profit | −14,076,000 | — | −14,076,000 | −14,076,000 |
| Net Profit | −8,636,000 | — | −8,636,000 | −8,636,000 |
| Inventory | 8,320,000 | — | 8,320,000 | 8,320,000 |
| Current Assets | 18,335,000 | — | 18,335,000 | 18,335,000 |
| Total Assets | 81,037,000 | — | 81,037,000 | 81,037,000 |
| Current Liabilities | 26,953,000 | — | 26,953,000 | 26,953,000 |
| Liabilities | **69,032,000** | — | **68,992,000*** | **69,032,000** |
| Total Shareholder Equity | 12,005,000 | — | 12,005,000 | 12,005,000 |
| Total Liab and SE | 81,037,000 | — | 81,037,000 | 81,037,000 |

*Dolt Liab $68,992K: Liab + TSE = $80,997K ≠ TA $81,037K (identity fails). Correct = $81,037K − $12,005K = $69,032K (= SEC Total Liabilities $68,858K + Redeemable NCI $174K).

### Reconciled Recommendation

- **Liabilities:** $69,032,000K (= TA − TSE). **Overwrite** (was $68,992,000K — balance identity violated).
- All other fields: unchanged.

---

## Analysis Complete

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql WBA` to write all changed years to the database.

**Changes to apply:**
- FY2022 correction: NetProfit $4,065,000K → $4,337,000K (was ProfitLoss not NetIncomeLoss; NCI entities had $271M losses)
- FY2023 correction: NetProfit −$3,528,000K → −$3,080,000K (was ProfitLoss not NetIncomeLoss; NCI entities had $448M losses)
- FY2024 correction: Liab $68,992,000K → $69,032,000K (balance identity failure; TA − TSE = $69,032K)

**Flags for review:**
- [WARNING] FY2021 income statement and balance sheet unverifiable — SEC MCP cannot parse WBA's FY2021, FY2022, FY2023 10-K filings. Values accepted as-is (balance identities hold for all three years).
- [WARNING] FY2022 and FY2023 balance sheets unverifiable from SEC. Income statement data confirmed from FY2024 10-K comparative.
- [WARNING] FY2023 SGA $34,205M includes opioid litigation settlement reserves — large but correctly classified per WBA's SEC filings.
- [WARNING] No FY2025 data available. WBA went private March 2025 (Sycamore Partners); Yahoo Finance unavailable; FY2025 10-K filing status uncertain.
