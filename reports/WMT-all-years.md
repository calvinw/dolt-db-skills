# Walmart (WMT) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2019-01-31 | Correction: TSE $79,634K → $72,496K; Liab $139,661K → $146,799K |
| 2019 | 2020-01-31 | Correction: Revenue $519,926K → $523,964K; Gross $125,321K → $129,359K; TSE $81,552K → $74,669K; Liab $154,943K → $161,826K |
| 2020 | 2021-01-31 | No change |
| 2021 | 2022-01-31 | No change |
| 2022 | 2023-01-31 | No change |
| 2023 | 2024-01-31 | No change |
| 2024 | 2025-01-31 | Correction: TSE $97,421K → $91,013K; Liab $163,402K → $169,810K |
| 2025 | 2026-01-31 | New insert |

---

## Key Findings

### TSE Convention (CRITICAL)
DB convention for WMT is **TSE = us-gaap_StockholdersEquity (common shareholders only, excluding minority interest)**. This is confirmed by years 2020–2023 all matching common-only SE. The minority interest (NCI) is absorbed into DB "Liabilities" = TA − TSE.

Three years incorrectly used `us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest` (total equity including NCI):
- Year 2018: NCI = $7,138K difference
- Year 2019: NCI = $6,883K difference
- Year 2024: NCI = $6,408K difference

NCI amounts by year (non-redeemable minority interest in SEC balance sheet):
- 2019-01-31: $7,138K | 2020-01-31: $6,883K | 2021-01-31: $6,606K | 2022-01-31: $8,638K | 2025-01-31: $6,408K | 2026-01-31: $6,270K

Redeemable NCI (first appeared FY2024): 2025-01-31: $271K; 2026-01-31: $293K → absorbed into DB Liabilities along with non-redeemable NCI.

### Revenue Convention (Year 2019 only)
WMT reports two revenue lines:
- `us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax` = product/service contract revenue only
- `us-gaap_OtherIncome` = membership fees and other income
- `us-gaap_Revenues` = TOTAL revenue (contract + membership) ← **DB uses this**

Year 2019 in Dolt incorrectly used the contract-only revenue ($519,926K), missing $4,038K in membership income. All other years correctly use `us-gaap_Revenues` total.

### Net Income — All Years Correct
All years in Dolt correctly use `us-gaap_NetIncomeLoss` (attributable to common shareholders), not `us-gaap_ProfitLoss`. NCI entities (international JVs) have had net income each year, so ProfitLoss > NetIncomeLoss each year.

---

## Detailed Year-by-Year Analysis

---

### FY2018 (reportDate: 2019-01-31, Dolt year: 2018)

**Anomaly flags:**
- [ERROR] TSE uses total equity (incl. NCI $7,138K) instead of common-only equity. Must correct.

**Sources:**
- SEC: year=2018 10-K (most recent column 2019-01-31)
- Yahoo: available (2022-01-31 is Yahoo's oldest column; 2019-01-31 not in Yahoo)
- Dolt: existing row

**Side-by-side comparison (thousands):**

| Field | SEC | Dolt (current) | Recommended |
|-------|-----|----------------|-------------|
| reportDate | 2019-01-31 | 2019-01-31 | 2019-01-31 |
| Revenue | 514,405 | 514,405 | **514,405** |
| COGS | 385,301 | 385,301 | **385,301** |
| Gross | 129,104 | 129,104 | **129,104** |
| SGA | 107,147 | 107,147 | **107,147** |
| OpInc | 21,957 | 21,957 | **21,957** |
| NetInc | 6,670 | 6,670 | **6,670** |
| Inv | 44,269 | 44,269 | **44,269** |
| CA | 61,897 | 61,897 | **61,897** |
| TA | 219,295 | 219,295 | **219,295** |
| CL | 77,477 | 77,477 | **77,477** |
| Liab | 146,799* | 139,661 | **146,799** |
| TSE | 72,496* | 79,634 | **72,496** |
| TL+SE | 219,295 | 219,295 | **219,295** |

*SEC common-only SE = 72,496K; SEC total SE incl. NCI = 79,634K; Recommended = common-only.
Liab = TA − TSE = 219,295 − 72,496 = 146,799K (= SEC total liabilities $139,661K + NCI $7,138K).

**Net Income check:** ProfitLoss $7,179K − NCI income $509K = NetIncomeLoss $6,670K ✓

**Reconciled values:**
- Revenue: 514,405K (no change)
- COGS: 385,301K (no change)
- Gross: 129,104K (no change)
- SGA: 107,147K (no change)
- OpInc: 21,957K (no change)
- NetInc: 6,670K (no change)
- Inv: 44,269K, CA: 61,897K, TA: 219,295K, CL: 77,477K
- **TSE: 72,496K** (corrected from 79,634K)
- **Liab: 146,799K** (corrected from 139,661K)
- TL+SE: 219,295K

---

### FY2019 (reportDate: 2020-01-31, Dolt year: 2019)

**Anomaly flags:**
- [ERROR] Revenue uses contract-only revenue ($519,926K), missing membership income ($4,038K). Correct total = $523,964K.
- [ERROR] Gross is therefore also wrong: $125,321K → $129,359K.
- [ERROR] TSE uses total equity (incl. NCI $6,883K) instead of common-only equity. Must correct.

**Sources:**
- SEC: year=2019 10-K (most recent column 2020-01-31); also confirmed in year=2020 10-K comparative
- Yahoo: 2020-01-31 not in Yahoo's available columns (oldest = 2022-01-31)
- Dolt: existing row

**Side-by-side comparison (thousands):**

| Field | SEC | Dolt (current) | Recommended |
|-------|-----|----------------|-------------|
| reportDate | 2020-01-31 | 2020-01-31 | 2020-01-31 |
| Revenue | 523,964* | 519,926 | **523,964** |
| COGS | 394,605 | 394,605 | **394,605** |
| Gross | 129,359* | 125,321 | **129,359** |
| SGA | 108,791 | 108,791 | **108,791** |
| OpInc | 20,568 | 20,568 | **20,568** |
| NetInc | 14,881 | 14,881 | **14,881** |
| Inv | 44,435 | 44,435 | **44,435** |
| CA | 61,806 | 61,806 | **61,806** |
| TA | 236,495 | 236,495 | **236,495** |
| CL | 77,790 | 77,790 | **77,790** |
| Liab | 161,826** | 154,943 | **161,826** |
| TSE | 74,669** | 81,552 | **74,669** |
| TL+SE | 236,495 | 236,495 | **236,495** |

*us-gaap_Revenues = 519,926K (contract) + 4,038K (membership) = 523,964K. Dolt incorrectly used contract-only.
**SEC common-only SE = 74,669K; SEC total SE incl. NCI = 81,552K; Recommended = common-only.
Liab = TA − TSE = 236,495 − 74,669 = 161,826K (= SEC total liabilities $154,943K + NCI $6,883K).

**Revenue consistency check:** OpInc = Revenue − COGS − SGA = 523,964 − 394,605 − 108,791 = 20,568K ✓. (Dolt's incorrect revenue of 519,926 would produce OpInc = 16,530K ≠ 20,568K, proving the Dolt revenue is wrong.)

**Net Income check:** ProfitLoss $15,201K − NCI income $320K = NetIncomeLoss $14,881K ✓

**Reconciled values:**
- **Revenue: 523,964K** (corrected from 519,926K)
- COGS: 394,605K (no change)
- **Gross: 129,359K** (corrected from 125,321K)
- SGA: 108,791K (no change)
- OpInc: 20,568K (no change)
- NetInc: 14,881K (no change)
- Inv: 44,435K, CA: 61,806K, TA: 236,495K, CL: 77,790K
- **TSE: 74,669K** (corrected from 81,552K)
- **Liab: 161,826K** (corrected from 154,943K)
- TL+SE: 236,495K

---

### FY2020 (reportDate: 2021-01-31, Dolt year: 2020)

**Anomaly flags:** None — all values verified from SEC year=2020 10-K.

**Sources:**
- SEC: year=2020 10-K (most recent column 2021-01-31) ✓
- Yahoo: 2021-01-31 not in Yahoo's available columns
- Dolt: existing row

**Side-by-side comparison (thousands):**

| Field | SEC | Dolt (current) | Recommended |
|-------|-----|----------------|-------------|
| reportDate | 2021-01-31 | 2021-01-31 | 2021-01-31 |
| Revenue | 559,151 | 559,151 | **559,151** ✓ |
| COGS | 420,315 | 420,315 | **420,315** ✓ |
| Gross | 138,836 | 138,836 | **138,836** ✓ |
| SGA | 116,288 | 116,288 | **116,288** ✓ |
| OpInc | 22,548 | 22,548 | **22,548** ✓ |
| NetInc | 13,510 | 13,510 | **13,510** ✓ |
| Inv | 44,949 | 44,949 | **44,949** ✓ |
| CA | 90,067 | 90,067 | **90,067** ✓ |
| TA | 252,496 | 252,496 | **252,496** ✓ |
| CL | 92,645 | 92,645 | **92,645** ✓ |
| Liab | 171,571 | 171,571 | **171,571** ✓ |
| TSE | 80,925 | 80,925 | **80,925** ✓ |
| TL+SE | 252,496 | 252,496 | **252,496** ✓ |

TSE check: SEC StockholdersEquity (common) = 80,925K = Dolt ✓ (correct convention). SEC MinorityInterest = $6,606K absorbed into Liab.
Liab = 252,496 − 80,925 = 171,571K ✓

**Net Income check:** ProfitLoss $13,706K − NCI income $196K = NetIncomeLoss $13,510K ✓

**Decision: No change.**

---

### FY2021 (reportDate: 2022-01-31, Dolt year: 2021)

**Anomaly flags:** None — all values verified from SEC year=2021 10-K.

**Sources:**
- SEC: year=2021 10-K (most recent column 2022-01-31) ✓
- Yahoo: oldest Yahoo column is 2022-01-31 (partial data)
- Dolt: existing row

**Side-by-side comparison (thousands):**

| Field | SEC | Dolt (current) | Recommended |
|-------|-----|----------------|-------------|
| reportDate | 2022-01-31 | 2022-01-31 | 2022-01-31 |
| Revenue | 572,754 | 572,754 | **572,754** ✓ |
| COGS | 429,000 | 429,000 | **429,000** ✓ |
| Gross | 143,754 | 143,754 | **143,754** ✓ |
| SGA | 117,812 | 117,812 | **117,812** ✓ |
| OpInc | 25,942 | 25,942 | **25,942** ✓ |
| NetInc | 13,673 | 13,673 | **13,673** ✓ |
| Inv | 56,511 | 56,511 | **56,511** ✓ |
| CA | 81,070 | 81,070 | **81,070** ✓ |
| TA | 244,860 | 244,860 | **244,860** ✓ |
| CL | 87,379 | 87,379 | **87,379** ✓ |
| Liab | 161,607 | 161,607 | **161,607** ✓ |
| TSE | 83,253 | 83,253 | **83,253** ✓ |
| TL+SE | 244,860 | 244,860 | **244,860** ✓ |

TSE check: SEC StockholdersEquity (common) = 83,253K = Dolt ✓. SEC MinorityInterest = $8,638K absorbed into Liab.
Liab = 244,860 − 83,253 = 161,607K ✓

**Net Income check:** ProfitLoss $13,940K − NCI income $267K = NetIncomeLoss $13,673K ✓

**Decision: No change.**

---

### FY2022 (reportDate: 2023-01-31, Dolt year: 2022)

**Anomaly flags:** None — verified from SEC FY2024 10-K comparative (2023-01-31 column) and Yahoo Finance.

**Side-by-side comparison (thousands):**

| Field | SEC (FY2024 comparative) | Yahoo | Dolt (current) | Recommended |
|-------|--------------------------|-------|----------------|-------------|
| reportDate | 2023-01-31 | 2023-01-31 | 2023-01-31 | 2023-01-31 |
| Revenue | 611,289 | 611,289 | 611,289 | **611,289** ✓ |
| COGS | 463,721 | 463,721 | 463,721 | **463,721** ✓ |
| Gross | 147,568 | 147,568 | 147,568 | **147,568** ✓ |
| SGA | 127,140 | 127,140 | 127,140 | **127,140** ✓ |
| OpInc | 20,428 | 20,428 | 20,428 | **20,428** ✓ |
| NetInc | 11,680 | 11,680 | 11,680 | **11,680** ✓ |
| Inv | — | 56,576 | 56,576 | **56,576** ✓ |
| CA | — | 75,655 | 75,655 | **75,655** ✓ |
| TA | — | 243,197 | 243,197 | **243,197** ✓ |
| CL | — | 92,198 | 92,198 | **92,198** ✓ |
| Liab | — | — | 166,504 | **166,504** ✓ |
| TSE | — | 76,693 | 76,693 | **76,693** ✓ |
| TL+SE | — | 243,197 | 243,197 | **243,197** ✓ |

TSE check: Yahoo Common Stock Equity = 76,693K = Dolt ✓ (common-only convention). TA − TSE = 243,197 − 76,693 = 166,504K ✓

**Decision: No change.**

---

### FY2023 (reportDate: 2024-01-31, Dolt year: 2023)

**Anomaly flags:** None — verified from SEC FY2024 10-K comparative (2024-01-31 column) and Yahoo Finance.

**Side-by-side comparison (thousands):**

| Field | SEC (FY2024 comparative) | Yahoo | Dolt (current) | Recommended |
|-------|--------------------------|-------|----------------|-------------|
| reportDate | 2024-01-31 | 2024-01-31 | 2024-01-31 | 2024-01-31 |
| Revenue | 648,125 | 648,125 | 648,125 | **648,125** ✓ |
| COGS | 490,142 | 490,142 | 490,142 | **490,142** ✓ |
| Gross | 157,983 | 157,983 | 157,983 | **157,983** ✓ |
| SGA | 130,971 | 130,971 | 130,971 | **130,971** ✓ |
| OpInc | 27,012 | 27,012 | 27,012 | **27,012** ✓ |
| NetInc | 15,511 | 15,511 | 15,511 | **15,511** ✓ |
| Inv | — | 54,892 | 54,892 | **54,892** ✓ |
| CA | — | 76,877 | 76,877 | **76,877** ✓ |
| TA | — | 252,399 | 252,399 | **252,399** ✓ |
| CL | — | 92,415 | 92,415 | **92,415** ✓ |
| Liab | — | — | 168,538 | **168,538** ✓ |
| TSE | — | 83,861 | 83,861 | **83,861** ✓ |
| TL+SE | — | 252,399 | 252,399 | **252,399** ✓ |

TSE check: Yahoo Common Stock Equity = 83,861K = Dolt ✓ (common-only convention). TA − TSE = 252,399 − 83,861 = 168,538K ✓

**Decision: No change.**

---

### FY2024 (reportDate: 2025-01-31, Dolt year: 2024)

**Anomaly flags:**
- [ERROR] TSE uses total equity incl. NCI ($97,421K) instead of common-only ($91,013K). Inconsistent with years 2020–2023.

**Sources:**
- SEC: year=2024 10-K (most recent column 2025-01-31) ✓
- Yahoo: 2025-01-31 column available ✓
- Dolt: existing row

**Side-by-side comparison (thousands):**

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| reportDate | 2025-01-31 | 2025-01-31 | 2025-01-31 | 2025-01-31 |
| Revenue | 680,985 | 680,985 | 680,985 | **680,985** ✓ |
| COGS | 511,753 | 511,753 | 511,753 | **511,753** ✓ |
| Gross | 169,232 | 169,232 | 169,232 | **169,232** ✓ |
| SGA | 139,884 | 139,884 | 139,884 | **139,884** ✓ |
| OpInc | 29,348 | 29,348 | 29,348 | **29,348** ✓ |
| NetInc | 19,436 | 19,436 | 19,436 | **19,436** ✓ |
| Inv | 56,435 | 56,435 | 56,435 | **56,435** ✓ |
| CA | 79,458 | 79,458 | 79,458 | **79,458** ✓ |
| TA | 260,823 | 260,823 | 260,823 | **260,823** ✓ |
| CL | 96,584 | 96,584 | 96,584 | **96,584** ✓ |
| Liab | 169,810* | — | 163,402 | **169,810** |
| TSE | 91,013* | 91,013 | 97,421 | **91,013** |
| TL+SE | 260,823 | — | 260,823 | **260,823** ✓ |

*SEC StockholdersEquity (common only) = 91,013K; SEC StockholdersEquityIncludingNCI = 97,421K (what Dolt currently has). Yahoo Common Stock Equity = 91,013K confirms correct value.
Liab = TA − TSE = 260,823 − 91,013 = 169,810K (= SEC total liabilities $163,131K + Redeemable NCI $271K + Non-redeemable NCI $6,408K).

**Net Income check:** ProfitLoss $20,157K − NCI income $721K = NetIncomeLoss $19,436K ✓

**Reconciled values:**
- Revenue: 680,985K (no change)
- COGS: 511,753K (no change)
- Gross: 169,232K (no change)
- SGA: 139,884K (no change)
- OpInc: 29,348K (no change)
- NetInc: 19,436K (no change)
- Inv: 56,435K, CA: 79,458K, TA: 260,823K, CL: 96,584K
- **TSE: 91,013K** (corrected from 97,421K)
- **Liab: 169,810K** (corrected from 163,402K)
- TL+SE: 260,823K

---

### FY2025 (reportDate: 2026-01-31, Dolt year: 2025) — NEW INSERT

**Sources:**
- SEC: year=2025 10-K (most recent column 2026-01-31) ✓ — SGA confirmed ($147,943K; Yahoo showed NaN)
- Yahoo: 2026-01-31 column available — all fields match SEC except SGA (Yahoo NaN for this year)
- Dolt: no existing row (new year)

**Data (thousands):**

| Field | SEC | Yahoo | Recommended |
|-------|-----|-------|-------------|
| reportDate | 2026-01-31 | 2026-01-31 | **2026-01-31** |
| Revenue | 713,163 | 713,163 | **713,163** |
| COGS | 535,395 | 535,395 | **535,395** |
| Gross | 177,768 | 177,768 | **177,768** |
| SGA | 147,943 | NaN | **147,943** (SEC) |
| OpInc | 29,825 | 29,825 | **29,825** |
| NetInc | 21,893 | 21,893 | **21,893** |
| Inv | 58,851 | 58,851 | **58,851** |
| CA | 84,874 | 84,874 | **84,874** |
| TA | 284,668 | 284,668 | **284,668** |
| CL | 107,469 | 107,469 | **107,469** |
| Liab | 185,051* | — | **185,051** |
| TSE | 99,617* | 99,617 | **99,617** |
| TL+SE | 284,668 | 284,668 | **284,668** |

*SEC StockholdersEquity (common only) = 99,617K. Yahoo Common Stock Equity = 99,617K ✓. SEC MinorityInterest = 6,270K; RedeemableNCI = 293K. Liab = TA − TSE = 284,668 − 99,617 = 185,051K (= SEC total liabilities $178,488K + Redeemable NCI $293K + Non-redeemable NCI $6,270K = 185,051K ✓).

**Revenue check:** Contract revenue 706,413K + Membership income 6,750K = 713,163K ✓
**Income check:** Revenue − COGS − SGA = 713,163 − 535,395 − 147,943 = 29,825K = OpInc ✓
**Net Income check:** ProfitLoss $22,270K − NCI income $377K = NetIncomeLoss $21,893K ✓
**Balance sheet:** Liab + TSE = 185,051 + 99,617 = 284,668K = TA ✓

---

## Reconciled Values — All Changed Years

### year=2018 (2019-01-31)
Revenue: 514,405 | COGS: 385,301 | Gross: 129,104 | SGA: 107,147 | OpInc: 21,957 | NetInc: 6,670 | Inv: 44,269 | CA: 61,897 | TA: 219,295 | CL: 77,477 | Liab: **146,799** | TSE: **72,496** | TL+SE: 219,295

### year=2019 (2020-01-31)
Revenue: **523,964** | COGS: 394,605 | Gross: **129,359** | SGA: 108,791 | OpInc: 20,568 | NetInc: 14,881 | Inv: 44,435 | CA: 61,806 | TA: 236,495 | CL: 77,790 | Liab: **161,826** | TSE: **74,669** | TL+SE: 236,495

### year=2024 (2025-01-31)
Revenue: 680,985 | COGS: 511,753 | Gross: 169,232 | SGA: 139,884 | OpInc: 29,348 | NetInc: 19,436 | Inv: 56,435 | CA: 79,458 | TA: 260,823 | CL: 96,584 | Liab: **169,810** | TSE: **91,013** | TL+SE: 260,823

### year=2025 (2026-01-31) — NEW
Revenue: 713,163 | COGS: 535,395 | Gross: 177,768 | SGA: 147,943 | OpInc: 29,825 | NetInc: 21,893 | Inv: 58,851 | CA: 84,874 | TA: 284,668 | CL: 107,469 | Liab: 185,051 | TSE: 99,617 | TL+SE: 284,668

---

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql WMT` to write all changed years to the database.

**Unresolved flags:** None — all [ERROR] flags resolved above.
