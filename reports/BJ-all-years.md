# BJ's Wholesale Club (BJ) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-03
**Source:** /verify-dolt-db-financials skill

---

## Company Background

- **CIK:** 1531152 (BJ's Wholesale Club Holdings, Inc.)
- **Segment:** Warehouse Club
- **Fiscal year end:** Late January / early February
- **Currency:** All values in $thousands (USD)
- **Gross margin benchmark:** Warehouse Clubs 10–15%. BJ's consistently runs ~17–19% due to membership fee revenue (pure margin) being included in Net Revenue. Flag as [WARNING] per benchmark rules but this is a known BJ's pattern.
- **SGA:** Single `us-gaap_SellingGeneralAndAdministrativeExpense` line. No separate marketing split.
- **Pre-opening costs:** Filed as `us-gaap_PreOpeningCosts` — a separate line that reduces Operating Income but is NOT included in SGA. DB convention is to use SEC Operating Income (after pre-opening deduction), NOT Yahoo's "Operating Income" which excludes pre-opening. Use Yahoo's "Total Operating Income As Reported" field when cross-checking.
- **Discontinued ops:** Very small amounts (< $1.2M in any year). Negligible impact on Net Income.

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2019-02-02 | No change — unverifiable from SEC (no older fetch); income statement plausible |
| 2019 | 2020-02-01 | No change — unverifiable from SEC (no older fetch); income statement plausible |
| 2020 | 2021-01-30 | Correction: Operating Profit 652,201 → 642,392 (pre-opening 9,809K missing); reportDate 2021-01-31 → 2021-01-30 |
| 2021 | 2022-01-29 | No change — income statement confirmed by SEC ✓; balance sheet unverified |
| 2022 | 2023-01-28 | No change — SEC confirmed ✓ (full balance sheet) |
| 2023 | 2024-02-03 | No change — SEC confirmed ✓ (full balance sheet) |
| 2024 | 2025-02-01 | No change — SEC confirmed ✓ (full balance sheet) |
| 2025 | 2026-01-31 | New insert |

---

## FY2018

**Sources:** Dolt only — no SEC fetch for this year; plausibility check only

### Anomaly Detection
- `[WARNING]` Cannot verify against SEC or Yahoo (5-year Yahoo window starts at FY2022; no year=2018 SEC fetch performed).
- Gross margin: 2,360,895 / 13,007,347 = 18.2% — above 10–15% Warehouse Club benchmark. Consistent with BJ's membership-fee-inclusive revenue model ✓
- Operating Profit math: Revenue 13,007,347 − COGS 10,646,452 − SGA 2,051,324 = 309,571 ≠ Dolt 303,453 → difference 6,118K consistent with pre-opening costs ✓
- Net Profit / Total Assets ratio looks reasonable for BJ's early post-IPO period.
- Balance sheet identity: 3,441,369 + (−202,084) = 3,239,285 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | — | 13,007,347 | 13,007,347 |
| Cost of Goods | — | — | 10,646,452 | 10,646,452 |
| Gross Margin | — | — | 2,360,895 | 2,360,895 |
| SGA | — | — | 2,051,324 | 2,051,324 |
| Operating Profit | — | — | 303,453 | 303,453 |
| Net Profit | — | — | 127,261 | 127,261 |
| Inventory | — | — | 1,052,306 | 1,052,306 |
| Current Assets | — | — | 1,337,206 | 1,337,206 |
| Total Assets | — | — | 3,239,285 | 3,239,285 |
| Current Liabilities | — | — | 1,577,688 | 1,577,688 |
| Liabilities | — | — | 3,441,369 | 3,441,369 |
| Total Shareholder Equity | — | — | -202,084 | -202,084 |
| TL&SE | — | — | 3,239,285 | 3,239,285 |
| reportDate | — | — | 2019-02-02 | 2019-02-02 |

---

## FY2019

**Sources:** Dolt only — no SEC fetch for this year; plausibility check only

### Anomaly Detection
- `[WARNING]` Cannot verify against SEC or Yahoo.
- Gross margin: 2,426,781 / 13,190,707 = 18.4% — above benchmark; consistent BJ's pattern ✓
- Operating Profit math: 13,190,707 − 10,763,926 − 2,059,430 = 367,351 ≠ Dolt 352,199 → difference 15,152K consistent with pre-opening costs ✓
- Balance sheet identity: 5,324,124 + (−54,344) = 5,269,780 = Total Assets ✓
- TSE went from −202,084K (FY2018) to −54,344K (FY2019) as equity recovered. Trend consistent.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | — | 13,190,707 | 13,190,707 |
| Cost of Goods | — | — | 10,763,926 | 10,763,926 |
| Gross Margin | — | — | 2,426,781 | 2,426,781 |
| SGA | — | — | 2,059,430 | 2,059,430 |
| Operating Profit | — | — | 352,199 | 352,199 |
| Net Profit | — | — | 187,176 | 187,176 |
| Inventory | — | — | 1,081,502 | 1,081,502 |
| Current Assets | — | — | 1,360,020 | 1,360,020 |
| Total Assets | — | — | 5,269,780 | 5,269,780 |
| Current Liabilities | — | — | 1,801,416 | 1,801,416 |
| Liabilities | — | — | 5,324,124 | 5,324,124 |
| Total Shareholder Equity | — | — | -54,344 | -54,344 |
| TL&SE | — | — | 5,269,780 | 5,269,780 |
| reportDate | — | — | 2020-02-01 | 2020-02-01 |

---

## FY2020

**Sources:** SEC 10-K comparative (from FY2022 10-K, column 2021-01-30) for income statement; balance sheet unverified

### Anomaly Detection
- `[ERROR]` Operating Profit: Dolt has 652,201K. SEC comparative (FY2022 10-K, column 2021-01-30) shows Operating Income = 642,392K. Discrepancy = 9,809K = pre-opening costs for FY2020 not deducted in Dolt. Correcting to 642,392K.
- `[WARNING]` reportDate: Dolt has 2021-01-31. SEC comparative column header is 2021-01-30. Correcting to 2021-01-30.
- `[WARNING]` Balance sheet: cannot verify from available SEC data (year=2020 10-K not fetched). Identity check: 5,092,203 + 319,327 = 5,411,530 = Total Assets ✓
- Net Profit confirmed: SEC comparative shows 421,030K = Dolt ✓
- Gross margin: 2,978,956 / 15,430,017 = 19.3% — above benchmark; consistent BJ's pattern (COVID-year revenue boost) ✓

### Side-by-Side

| Field | SEC (comparative) | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 15,430,017 | — | 15,430,017 | 15,430,017 |
| Cost of Goods | 12,451,061 | — | 12,451,061 | 12,451,061 |
| Gross Margin | 2,978,956 | — | 2,978,956 | 2,978,956 |
| SGA | 2,326,755 | — | 2,326,755 | 2,326,755 |
| Operating Profit | **642,392** | — | 652,201* | **642,392** |
| Net Profit | 421,030 | — | 421,030 | 421,030 |
| Inventory | — | — | 1,205,695 | 1,205,695 |
| Current Assets | — | — | 1,470,581 | 1,470,581 |
| Total Assets | — | — | 5,411,530 | 5,411,530 |
| Current Liabilities | — | — | 2,031,212 | 2,031,212 |
| Liabilities | — | — | 5,092,203 | 5,092,203 |
| Total Shareholder Equity | — | — | 319,327 | 319,327 |
| TL&SE | — | — | 5,411,530 | 5,411,530 |
| reportDate | **2021-01-30** | — | 2021-01-31* | **2021-01-30** |

*Operating Profit missing 9,809K pre-opening deduction; reportDate 1 day off.

### Reconciled Values

Correct Operating Profit to 642,392K (SEC). Correct reportDate to 2021-01-30. Balance sheet fields retained as-is (identity passes; full balance sheet unverified). All other values unchanged.

---

## FY2021

**Sources:** SEC 10-K comparative (from FY2022 10-K, column 2022-01-29) for income statement; balance sheet unverified from SEC

### Anomaly Detection
- Income statement confirmed: all fields match SEC comparative ✓
- Gross margin: 3,078,690 / 16,667,302 = 18.5% — above benchmark; consistent BJ's pattern ✓
- Operating Profit math check: 16,667,302 − 13,588,612 − 2,446,465 − 14,902 (pre-opening) = 617,323K = Dolt ✓
- Net Profit: 426,652K = SEC ✓ (includes −108K discontinued, total = 426,652K) ✓
- Balance sheet identity: 5,020,786 + 648,108 = 5,668,894 = Total Assets ✓

### Side-by-Side

| Field | SEC (comparative) | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 16,667,302 | — | 16,667,302 | 16,667,302 |
| Cost of Goods | 13,588,612 | — | 13,588,612 | 13,588,612 |
| Gross Margin | 3,078,690 | — | 3,078,690 | 3,078,690 |
| SGA | 2,446,465 | — | 2,446,465 | 2,446,465 |
| Operating Profit | 617,323 | — | 617,323 | 617,323 |
| Net Profit | 426,652 | — | 426,652 | 426,652 |
| Inventory | — | — | 1,242,935 | 1,242,935 |
| Current Assets | — | — | 1,517,056 | 1,517,056 |
| Total Assets | — | — | 5,668,894 | 5,668,894 |
| Current Liabilities | — | — | 2,002,481 | 2,002,481 |
| Liabilities | — | — | 5,020,786 | 5,020,786 |
| Total Shareholder Equity | — | — | 648,108 | 648,108 |
| TL&SE | — | — | 5,668,894 | 5,668,894 |
| reportDate | 2022-01-29 | — | 2022-01-29 | 2022-01-29 |

---

## FY2022

**Sources:** SEC 10-K (CIK 1531152, FY2022, period ending 2023-01-28) + Yahoo Finance (column 2023-01-31) + Dolt

### Anomaly Detection
- All income statement fields confirmed: SEC = Yahoo = Dolt ✓
- All balance sheet fields confirmed: SEC = Dolt ✓
- Gross margin: 3,431,488 / 19,315,165 = 17.8% — above benchmark; consistent BJ's pattern ✓
- Operating Profit: 737,986K = SEC (after deducting 24,933K pre-opening) ✓
- Yahoo "Total Operating Income As Reported" = 737,986K ✓ (matches; Yahoo's plain "Operating Income" = 762,919K does NOT deduct pre-opening — do not use)
- Balance sheet identity: 5,303,119 + 1,046,837 = 6,349,956 ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 19,315,165 | 19,315,165 | 19,315,165 | 19,315,165 |
| Cost of Goods | 15,883,677 | 15,883,677 | 15,883,677 | 15,883,677 |
| Gross Margin | 3,431,488 | 3,431,488 | 3,431,488 | 3,431,488 |
| SGA | 2,668,569 | 2,668,569 | 2,668,569 | 2,668,569 |
| Operating Profit | 737,986 | 737,986 | 737,986 | 737,986 |
| Net Profit | 513,177 | 513,177 | 513,177 | 513,177 |
| Inventory | 1,378,551 | 1,378,551 | 1,378,551 | 1,378,551 |
| Current Assets | 1,703,245 | 1,703,245 | 1,703,245 | 1,703,245 |
| Total Assets | 6,349,956 | 6,349,956 | 6,349,956 | 6,349,956 |
| Current Liabilities | 2,545,341 | 2,545,341 | 2,545,341 | 2,545,341 |
| Liabilities | 5,303,119 | 5,303,119 | 5,303,119 | 5,303,119 |
| Total Shareholder Equity | 1,046,837 | 1,046,837 | 1,046,837 | 1,046,837 |
| TL&SE | 6,349,956 | 6,349,956 | 6,349,956 | 6,349,956 |
| reportDate | 2023-01-28 | (2023-01-31)* | 2023-01-28 | 2023-01-28 |

*Yahoo approximates reportDate; Dolt uses correct SEC date.

---

## FY2023

**Sources:** SEC 10-K (CIK 1531152, FY2023, period ending 2024-02-03) + Yahoo Finance (column 2024-01-31) + Dolt

### Anomaly Detection
- All income statement fields confirmed: SEC = Yahoo = Dolt ✓
- All balance sheet fields confirmed: SEC = Dolt ✓
- Gross margin: 3,642,560 / 19,968,689 = 18.2% — above benchmark; consistent BJ's pattern ✓
- Operating Profit: 800,419K = SEC (after deducting 19,628K pre-opening) ✓
- Balance sheet identity: 5,218,771 + 1,458,851 = 6,677,622 ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 19,968,689 | 19,968,689 | 19,968,689 | 19,968,689 |
| Cost of Goods | 16,326,129 | 16,326,129 | 16,326,129 | 16,326,129 |
| Gross Margin | 3,642,560 | 3,642,560 | 3,642,560 | 3,642,560 |
| SGA | 2,822,513 | 2,822,513 | 2,822,513 | 2,822,513 |
| Operating Profit | 800,419 | 800,419 | 800,419 | 800,419 |
| Net Profit | 523,741 | 523,741 | 523,741 | 523,741 |
| Inventory | 1,454,822 | 1,454,822 | 1,454,822 | 1,454,822 |
| Current Assets | 1,794,006 | 1,794,006 | 1,794,006 | 1,794,006 |
| Total Assets | 6,677,622 | 6,677,622 | 6,677,622 | 6,677,622 |
| Current Liabilities | 2,468,048 | 2,468,048 | 2,468,048 | 2,468,048 |
| Liabilities | 5,218,771 | 5,218,771 | 5,218,771 | 5,218,771 |
| Total Shareholder Equity | 1,458,851 | 1,458,851 | 1,458,851 | 1,458,851 |
| TL&SE | 6,677,622 | 6,677,622 | 6,677,622 | 6,677,622 |
| reportDate | 2024-02-03 | (2024-01-31)* | 2024-02-03 | 2024-02-03 |

---

## FY2024

**Sources:** SEC 10-K (CIK 1531152, FY2024, period ending 2025-02-01) + Yahoo Finance (column 2025-01-31) + Dolt

### Anomaly Detection
- All income statement fields confirmed: SEC = Yahoo = Dolt ✓
- All balance sheet fields confirmed: SEC = Dolt ✓
- Gross margin: 3,764,426 / 20,501,804 = 18.4% — above benchmark; consistent BJ's pattern ✓
- Operating Profit: 772,206K = SEC (after deducting 28,337K pre-opening) ✓
- Yahoo "Total Operating Income As Reported" = 772,206K ✓
- Balance sheet identity: 5,217,851 + 1,847,454 = 7,065,305 ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 20,501,804 | 20,501,804 | 20,501,804 | 20,501,804 |
| Cost of Goods | 16,737,378 | 16,737,378 | 16,737,378 | 16,737,378 |
| Gross Margin | 3,764,426 | 3,764,426 | 3,764,426 | 3,764,426 |
| SGA | 2,963,883 | 2,963,883 | 2,963,883 | 2,963,883 |
| Operating Profit | 772,206 | 772,206 | 772,206 | 772,206 |
| Net Profit | 534,417 | 534,417 | 534,417 | 534,417 |
| Inventory | 1,508,988 | 1,508,988 | 1,508,988 | 1,508,988 |
| Current Assets | 1,878,960 | 1,878,960 | 1,878,960 | 1,878,960 |
| Total Assets | 7,065,305 | 7,065,305 | 7,065,305 | 7,065,305 |
| Current Liabilities | 2,534,082 | 2,534,082 | 2,534,082 | 2,534,082 |
| Liabilities | 5,217,851 | 5,217,851 | 5,217,851 | 5,217,851 |
| Total Shareholder Equity | 1,847,454 | 1,847,454 | 1,847,454 | 1,847,454 |
| TL&SE | 7,065,305 | 7,065,305 | 7,065,305 | 7,065,305 |
| reportDate | 2025-02-01 | (2025-01-31)* | 2025-02-01 | 2025-02-01 |

---

## FY2025

**Sources:** SEC 10-K (CIK 1531152, FY2025, period ending 2026-01-31) + Yahoo Finance (column 2026-01-31) — New insert

### Anomaly Detection
- No Dolt row exists for year 2025.
- All income statement values confirmed: SEC = Yahoo ✓ (minor rounding in Yahoo)
- All balance sheet values confirmed: SEC = Yahoo ✓
- Gross margin: 3,999,622 / 21,457,274 = 18.6% — above 10–15% Warehouse Club benchmark. `[WARNING]` per rules, but consistent BJ's pattern across all years (membership fee revenue boosts gross margin) ✓
- Operating Profit: 816,604K = SEC (after deducting 29,441K pre-opening). Yahoo "Operating Income" = 846,045K (pre-opening NOT deducted — do NOT use); Yahoo "Total Operating Income As Reported" = 816,604K ✓
- Balance sheet identity: 5,312,816 + 2,197,659 = 7,510,475 ✓
- Net Revenue = Net sales (20,957,502K) + Membership fee income (499,772K) = 21,457,274K ✓
- TSE growing steadily ($319K FY2020 → $2,198M FY2025) as earnings accumulate. Healthy trend ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 21,457,274 | 21,457,274* | — | **21,457,274** |
| Cost of Goods | 17,457,652 | 17,457,652* | — | **17,457,652** |
| Gross Margin | 3,999,622 | 3,999,622* | — | **3,999,622** |
| SGA | 3,153,577 | 3,153,580* | — | **3,153,577** |
| Operating Profit | 816,604 | 816,604† | — | **816,604** |
| Net Profit | 578,377 | 578,377 | — | **578,377** |
| Inventory | 1,555,471 | 1,555,471* | — | **1,555,471** |
| Current Assets | 1,990,089 | 1,990,089* | — | **1,990,089** |
| Total Assets | 7,510,475 | 7,510,475* | — | **7,510,475** |
| Current Liabilities | 2,670,233 | 2,670,233* | — | **2,670,233** |
| Liabilities | 5,312,816 | 5,312,816* | — | **5,312,816** |
| Total Shareholder Equity | 2,197,659 | 2,197,659* | — | **2,197,659** |
| TL&SE | 7,510,475 | 7,510,475* | — | **7,510,475** |
| reportDate | 2026-01-31 | 2026-01-31 | — | **2026-01-31** |

*Minor Yahoo rounding (≤5K); use SEC values. †Yahoo "Total Operating Income As Reported" = 816,604K; Yahoo plain "Operating Income" = 846,045K (excludes pre-opening — do not use).

### Reconciled Values

New insert. Balance sheet identity: 5,312,816 + 2,197,659 = 7,510,475 ✓

---

**Analysis complete.** Run `/insert-financials BJ` to write all changed years to the database.

Unresolved flags:
- **FY2020**: Balance sheet not verified from SEC (year=2020 10-K not fetched). Identity check passes; values retained as-is. Only Operating Profit and reportDate corrected.
- **FY2018–2019**: Not verifiable from available SEC data. Values appear plausible; no corrections made.
- **Gross margin warnings**: BJ's consistently runs above the 10–15% Warehouse Club benchmark (~17–19%). This is a known, expected pattern for BJ's due to membership fee revenue inclusion — not an error.
