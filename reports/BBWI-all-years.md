# Bath & Body Works (BBWI) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-05-29
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2018 | 2019-03-02 | No change — pre-spinoff L Brands data; no alternate source |
| 2019 | 2020-02-29 | No change — pre-spinoff L Brands data; no alternate source |
| 2020 | 2021-02-27 | No change — pre-spinoff L Brands data; no alternate source |
| 2021 | 2022-02-26 | No change — L Brands transition year; no alternate source |
| 2022 | 2023-01-31 | **Correction: All fields** — Dolt data is incorrect; replacing with Yahoo FY2022 values |
| 2023 | 2024-01-31 | No change — Yahoo values match exactly |
| 2024 | 2025-01-31 | **New insert** |
| 2025 | 2026-01-31 | **New insert** |

---

## Company Metadata

- **Company name (DB):** Bath & Body Works
- **Display name:** Bath & Body Works
- **Ticker:** BBWI
- **CIK:** 886158
- **Segment:** Specialty — Personal Care / Home Fragrance
- **Fiscal year end:** Late January
- **SEC available:** Yes (CIK present), but SEC MCP unavailable this session — Yahoo Finance + Dolt only
- **Spinoff note:** BBWI was spun off from L Brands (CIK 886158) on August 2, 2021. The CIK 886158 was retained by BBWI. Dolt years 2018–2021 contain L Brands combined data (included Victoria's Secret segment). Years 2022+ are BBWI standalone.
- **Operating Profit convention:** Yahoo "Operating Income" = "Total Operating Income As Reported" for all years — no special charges in the operating line; use directly
- **TSE convention:** Common Stock Equity (negative for all post-spinoff years due to leveraged capital structure and accumulated losses — valid)

---

## Anomaly Rules Applied

- **Rule 3 (Yahoo SGA = Total OpEx):** Not triggered. Yahoo Total Expenses (~$6.2B for FY2022) >> SGA (~$1.9B). SGA is safe to use.
- **Rule 1 (SGA + Marketing):** No separate Marketing line in Yahoo for BBWI. Single combined G&A/SGA line. Use directly.
- **Rule 4:** Not needed — combined SGA line present.
- **SGA verification (years 2022–2025):** Gross Profit − SGA = Operating Income for all years ✓ (2022: 3,255,000−1,879,000=1,376,000 ✓; 2023: 3,236,000−1,951,000=1,285,000 ✓; 2024: 3,234,000−1,968,000=1,266,000 ✓; 2025: 3,189,000−2,063,000=1,126,000 ✓)
- **Gross margin benchmark:** Specialty expected 35–55%. All post-spinoff years: 43–44% ✓
- **Negative TSE:** All post-spinoff years have negative TSE. Valid — BBWI carries significant lease and long-term debt with accumulated losses.
- **Balance sheet identity:** Verified for all years. ✓
- **Year 2022 ERROR:** Existing Dolt data (Revenue 5.3B, Op Profit −2.8B) is completely inconsistent with Yahoo FY2022 data (Revenue 7.56B, Op Profit +1.4B). The Dolt year 2022 reportDate (2023-02-25) also doesn't match BBWI's FY2022 fiscal year end (Jan 28, 2023). Dolt data appears to be from a wrong source. Correcting to Yahoo values.

---

## Years 2018–2021: L Brands Era Data (Pre-Spinoff / Transition)

[WARNING] Years 2018–2021 in Dolt contain L Brands combined company data, which included the Victoria's Secret segment before the August 2021 spinoff. Revenue figures ($7.9–$12B) and large inventory/SGA values reflect the combined entity. This data is not directly comparable to post-spinoff BBWI financials. No correction is possible without proper L Brands historical data.

No Yahoo Finance data available for these years. No changes recommended.

### Year 2018

| Field | Dolt (current) | Yahoo | Recommended |
|-------|---------------|-------|-------------|
| reportDate | 2019-03-02 | N/A | 2019-03-02 |
| Net Revenue | 12,028,797 | N/A | 12,028,797 |
| Cost of Goods | 7,924,817 | N/A | 7,924,817 |
| Gross Margin | 4,103,980 | N/A | 4,103,980 |
| Gross Margin % | 34.1% | N/A | — |
| SGA | 3,681,210 | N/A | 3,681,210 [WARNING: unverified; L Brands era] |
| Operating Profit | -87,135 | N/A | -87,135 |
| Net Profit | -137,224 | N/A | -137,224 |
| Inventory | 2,618,922 | N/A | 2,618,922 |
| Current Assets | 3,909,972 | N/A | 3,909,972 |
| Total Assets | 6,570,541 | N/A | 6,570,541 |
| Current Liabilities | 2,077,632 | N/A | 2,077,632 |
| Liabilities | 4,010,210 | N/A | 4,010,210 |
| TSE | 2,560,331 | N/A | 2,560,331 |
| Total L+E | 6,570,541 | N/A | 6,570,541 |

Balance sheet identity: 4,010,210 + 2,560,331 = 6,570,541 ✓

**Action: No change.**

---

### Year 2019

| Field | Dolt (current) | Yahoo | Recommended |
|-------|---------------|-------|-------------|
| reportDate | 2020-02-29 | N/A | 2020-02-29 |
| Net Revenue | 11,158,580 | N/A | 11,158,580 |
| Cost of Goods | 7,616,920 | N/A | 7,616,920 |
| Gross Margin | 3,541,660 | N/A | 3,541,660 |
| Gross Margin % | 31.7% | N/A | — |
| SGA | 3,732,498 | N/A | 3,732,498 [WARNING: unverified; L Brands era] |
| Operating Profit | -700,064 | N/A | -700,064 |
| Net Profit | -613,816 | N/A | -613,816 |
| Inventory | 2,093,869 | N/A | 2,093,869 |
| Current Assets | 3,826,285 | N/A | 3,826,285 |
| Total Assets | 7,790,515 | N/A | 7,790,515 |
| Current Liabilities | 2,466,526 | N/A | 2,466,526 |
| Liabilities | 6,025,580 | N/A | 6,025,580 |
| TSE | 1,764,935 | N/A | 1,764,935 |
| Total L+E | 7,790,515 | N/A | 7,790,515 |

Balance sheet identity: 6,025,580 + 1,764,935 = 7,790,515 ✓

Note: Large jump in Total Assets from 2018 to 2019 reflects FASB ASC 842 adoption (ROU assets and lease liabilities added to balance sheet).

**Action: No change.**

---

### Year 2020

| Field | Dolt (current) | Yahoo | Recommended |
|-------|---------------|-------|-------------|
| reportDate | 2021-02-27 | N/A | 2021-02-27 |
| Net Revenue | 9,233,028 | N/A | 9,233,028 |
| Cost of Goods | 6,114,947 | N/A | 6,114,947 |
| Gross Margin | 3,118,081 | N/A | 3,118,081 |
| Gross Margin % | 33.8% | N/A | — |
| SGA | 3,224,363 | N/A | 3,224,363 [WARNING: unverified; L Brands era] |
| Operating Profit | -336,887 | N/A | -336,887 |
| Net Profit | -150,773 | N/A | -150,773 |
| Inventory | 1,671,909 | N/A | 1,671,909 |
| Current Assets | 3,620,045 | N/A | 3,620,045 |
| Total Assets | 6,456,930 | N/A | 6,456,930 |
| Current Liabilities | 2,294,921 | N/A | 2,294,921 |
| Liabilities | 5,179,994 | N/A | 5,179,994 |
| TSE | 1,276,936 | N/A | 1,276,936 |
| Total L+E | 6,456,930 | N/A | 6,456,930 |

Balance sheet identity: 5,179,994 + 1,276,936 = 6,456,930 ✓

**Action: No change.**

---

### Year 2021

| Field | Dolt (current) | Yahoo | Recommended |
|-------|---------------|-------|-------------|
| reportDate | 2022-02-26 | N/A | 2022-02-26 |
| Net Revenue | 7,867,778 | N/A | 7,867,778 |
| Cost of Goods | 5,384,287 | N/A | 5,384,287 |
| Gross Margin | 2,483,491 | N/A | 2,483,491 |
| Gross Margin % | 31.6% | N/A | — |
| SGA | 2,692,292 | N/A | 2,692,292 [WARNING: unverified; L Brands transition year] |
| Operating Profit | -407,578 | N/A | -407,578 |
| Net Profit | -559,623 | N/A | -559,623 |
| Inventory | 1,725,410 | N/A | 1,725,410 |
| Current Assets | 2,363,154 | N/A | 2,363,154 |
| Total Assets | 5,130,572 | N/A | 5,130,572 |
| Current Liabilities | 2,074,787 | N/A | 2,074,787 |
| Liabilities | 4,956,427 | N/A | 4,956,427 |
| TSE | 174,145 | N/A | 174,145 |
| Total L+E | 5,130,572 | N/A | 5,130,572 |

Balance sheet identity: 4,956,427 + 174,145 = 5,130,572 ✓

Note: Year 2021 covers the L Brands transition year including partial-year Victoria's Secret operations (spinoff completed Aug 2021). Negative operating and net profits include spinoff-related charges.

**Action: No change.**

---

## Year 2022: Correction Required

[ERROR] The existing Dolt year 2022 data is incorrect and must be replaced.

**Problem:**
- Dolt reportDate is 2023-02-25 — not a valid BBWI fiscal year-end date (FY2022 ended Jan 28, 2023)
- Dolt Revenue = 5,344,685K vs Yahoo FY2022 = 7,560,000K — a ~2.2B discrepancy
- Dolt Operating Profit = −2,775,639K vs Yahoo FY2022 = +1,376,000K — a ~4.2B discrepancy
- Current Liabilities (2,495,884K) > Total Assets (2,225,217K) — structurally impossible
- All fields appear to be from an incorrect source (possibly Victoria's Secret & Co VSCO data or transition-period L Brands data incorrectly mapped to this period)

**Correct FY2022 values (BBWI standalone, from Yahoo column 2023-01-31):**

| Field | Yahoo (2023-01-31) | Dolt (current — WRONG) | Recommended |
|-------|-------------------|----------------------|-------------|
| reportDate | 2023-01-31 | 2023-02-25* | **2023-01-31** |
| Net Revenue | 7,560,000 | 5,344,685* | **7,560,000** |
| Cost of Goods | 4,305,000 | 4,129,802* | **4,305,000** |
| Gross Margin | 3,255,000 | 1,214,883* | **3,255,000** |
| Gross Margin % | 43.1% | 22.7% | — |
| SGA | 1,879,000 | 2,372,969* | **1,879,000** |
| Operating Profit | 1,376,000 | −2,775,639* | **1,376,000** |
| Net Profit | 800,000 | −3,498,801* | **800,000** |
| Inventory | 709,000 | 817,553* | **709,000** |
| Current Assets | 2,266,000 | 1,096,909* | **2,266,000** |
| Total Assets | 5,494,000 | 2,225,217* | **5,494,000** |
| Current Liabilities | 1,379,000 | 2,495,884* | **1,379,000** |
| Liabilities | 7,700,000 | 5,025,225* | **7,700,000** |
| TSE | −2,206,000 | −2,800,008* | **−2,206,000** |
| Total L+E | 5,494,000 | 2,225,217 | **5,494,000** |

*Asterisk = incorrect/incorrect source

Gross Margin check: 7,560,000 − 4,305,000 = 3,255,000 ✓
Balance sheet: 7,700,000 + (−2,206,000) = 5,494,000 ✓
Gross margin %: 3,255,000/7,560,000 = 43.1% — within specialty range (35–55%) ✓
[WARNING] TSE = −2,206,000K (negative equity). Valid — BBWI leveraged structure.

TSE note: Using Common Stock Equity (−2,206,000K) consistent with Dolt year 2023 convention. Yahoo Total Equity Gross Minority Interest = −2,205,000K (difference of 1,000K = minority interest). Yahoo Total Liabilities = 7,699,000K; calculated Liabilities (5,494,000 − (−2,206,000)) = 7,700,000K; 1K diff from minority interest.

**Action: Correction — all fields.**

---

## Year 2023: Yahoo vs Dolt Comparison

Yahoo 2024-01-31 → Dolt year 2023 (reportDate 2024-01-31).

| Field | Yahoo (2024-01-31) | Dolt (current) | Recommended |
|-------|-------------------|---------------|-------------|
| reportDate | 2024-01-31 | 2024-01-31 | 2024-01-31 |
| Net Revenue | 7,429,000 | 7,429,000 | 7,429,000 |
| Cost of Goods | 4,193,000 | 4,193,000 | 4,193,000 |
| Gross Margin | 3,236,000 | 3,236,000 | 3,236,000 |
| Gross Margin % | 43.6% | 43.6% | — |
| SGA | 1,951,000 | 1,951,000 | 1,951,000 |
| Operating Profit | 1,285,000 | 1,285,000 | 1,285,000 |
| Net Profit | 878,000 | 878,000 | 878,000 |
| Inventory | 710,000 | 710,000 | 710,000 |
| Current Assets | 2,115,000 | 2,115,000 | 2,115,000 |
| Total Assets | 5,463,000 | 5,463,000 | 5,463,000 |
| Current Liabilities | 1,289,000 | 1,289,000 | 1,289,000 |
| Liabilities | 7,090,000* | 7,090,000 | 7,090,000 |
| TSE | −1,627,000 | −1,627,000 | −1,627,000 |
| Total L+E | 5,463,000 | 5,463,000 | 5,463,000 |

*Yahoo Total Liabilities shown as 7,089,000K; Dolt Liabilities = Total Assets − TSE = 5,463,000 − (−1,627,000) = 7,090,000K (1K diff from rounding only).

All values match exactly.

Balance sheet identity: 7,090,000 + (−1,627,000) = 5,463,000 ✓

**Action: No change.**

---

## Year 2024: New Insert (Yahoo 2025-01-31)

This year is not yet in the Dolt database.

### Source Data (Yahoo 2025-01-31)

**Income Statement:**
| Item | Yahoo Raw | Value ($K) |
|------|-----------|-----------|
| Total Revenue | 7.307e+09 | 7,307,000 |
| Cost Of Revenue | 4.073e+09 | 4,073,000 |
| Gross Profit | 3.234e+09 | 3,234,000 |
| Selling General And Administration | 1.968e+09 | 1,968,000 |
| Operating Income | 1.266e+09 | 1,266,000 |
| Total Operating Income As Reported | 1.266e+09 | 1,266,000 |
| Net Income Common Stockholders | 7.98e+08 | 798,000 |

Gross Margin check: 7,307,000 − 4,073,000 = 3,234,000 ✓
Operating check: 3,234,000 − 1,968,000 = 1,266,000 ✓

**Balance Sheet:**
| Item | Yahoo Raw | Value ($K) |
|------|-----------|-----------|
| Inventory | 7.34e+08 | 734,000 |
| Current Assets | 1.823e+09 | 1,823,000 |
| Total Assets | 4.872e+09 | 4,872,000 |
| Current Liabilities | 1.231e+09 | 1,231,000 |
| Common Stock Equity | −1.385e+09 | −1,385,000 |
| Total Equity Gross Minority Interest | −1.383e+09 | −1,383,000 |
| Total Liabilities Net Minority Interest | 6.255e+09 | 6,255,000 |

TSE = Common Stock Equity = −1,385,000K (consistent with Dolt convention)
Liabilities = 4,872,000 − (−1,385,000) = 6,257,000K
Yahoo Total Liabilities = 6,255,000K (2K diff from minority interest of 2,000K)

Balance sheet: 6,257,000 + (−1,385,000) = 4,872,000 ✓

### Anomaly Checks

- **Gross margin:** 3,234,000/7,307,000 = **44.3%** — within specialty range (35–55%) ✓
- **SGA rule 3:** Yahoo SGA 1,968,000K << Total Expenses ~6,041,000K ✓
- **Operating Profit:** Operating Income = As Reported (1,266,000K) — consistent with BBWI convention ✓
- **TSE:** Negative (−1,385,000K) — valid, consistent with BBWI post-spinoff structure ✓
- **Balance sheet identity:** 6,257,000 + (−1,385,000) = 4,872,000 ✓
- **Inventory:** 734,000K — positive, expected ✓

### Reconciled Values for FY2024

| Field | Recommended Value | Notes |
|-------|------------------|-------|
| reportDate | 2025-01-31 | Yahoo column header |
| Net Revenue | 7,307,000 | Yahoo |
| Cost of Goods | 4,073,000 | Yahoo |
| Gross Margin | 3,234,000 | Calculated |
| SGA | 1,968,000 | Yahoo |
| Operating Profit | 1,266,000 | Yahoo Operating Income = As Reported |
| Net Profit | 798,000 | Yahoo |
| Inventory | 734,000 | Yahoo |
| Current Assets | 1,823,000 | Yahoo |
| Total Assets | 4,872,000 | Yahoo |
| Current Liabilities | 1,231,000 | Yahoo |
| Liabilities | 6,257,000 | Calculated (Total Assets − TSE) |
| TSE | −1,385,000 | Yahoo Common Stock Equity |
| Total L+E | 4,872,000 | Yahoo |

**Action: New insert.**

---

## Year 2025: New Insert (Yahoo 2026-01-31)

This year is not yet in the Dolt database.

### Source Data (Yahoo 2026-01-31)

**Income Statement:**
| Item | Yahoo Raw | Value ($K) |
|------|-----------|-----------|
| Total Revenue | 7.291e+09 | 7,291,000 |
| Cost Of Revenue | 4.102e+09 | 4,102,000 |
| Gross Profit | 3.189e+09 | 3,189,000 |
| Selling General And Administration | 2.063e+09 | 2,063,000 |
| Operating Income | 1.126e+09 | 1,126,000 |
| Total Operating Income As Reported | 1.126e+09 | 1,126,000 |
| Net Income Common Stockholders | 6.49e+08 | 649,000 |

Gross Margin check: 7,291,000 − 4,102,000 = 3,189,000 ✓
Operating check: 3,189,000 − 2,063,000 = 1,126,000 ✓

**Balance Sheet:**
| Item | Yahoo Raw | Value ($K) |
|------|-----------|-----------|
| Inventory | 6.99e+08 | 699,000 |
| Current Assets | 2.019e+09 | 2,019,000 |
| Total Assets | 5.069e+09 | 5,069,000 |
| Current Liabilities | 1.591e+09 | 1,591,000 |
| Common Stock Equity | −1.281e+09 | −1,281,000 |
| Total Equity Gross Minority Interest | −1.279e+09 | −1,279,000 |
| Total Liabilities Net Minority Interest | 6.348e+09 | 6,348,000 |

TSE = Common Stock Equity = −1,281,000K (consistent with Dolt convention)
Liabilities = 5,069,000 − (−1,281,000) = 6,350,000K
Yahoo Total Liabilities = 6,348,000K (2K diff from minority interest of 2,000K)

Balance sheet: 6,350,000 + (−1,281,000) = 5,069,000 ✓

### Anomaly Checks

- **Gross margin:** 3,189,000/7,291,000 = **43.7%** — within specialty range (35–55%) ✓
- **SGA rule 3:** Yahoo SGA 2,063,000K << Total Expenses ~6,165,000K ✓
- **Operating Profit:** Operating Income = As Reported (1,126,000K) — consistent with BBWI convention ✓
- **TSE:** Negative (−1,281,000K) — valid, consistent with BBWI post-spinoff structure ✓
- **Balance sheet identity:** 6,350,000 + (−1,281,000) = 5,069,000 ✓
- **Inventory:** 699,000K — positive, expected ✓

### Reconciled Values for FY2025

| Field | Recommended Value | Notes |
|-------|------------------|-------|
| reportDate | 2026-01-31 | Yahoo column header |
| Net Revenue | 7,291,000 | Yahoo |
| Cost of Goods | 4,102,000 | Yahoo |
| Gross Margin | 3,189,000 | Calculated |
| SGA | 2,063,000 | Yahoo |
| Operating Profit | 1,126,000 | Yahoo Operating Income = As Reported |
| Net Profit | 649,000 | Yahoo |
| Inventory | 699,000 | Yahoo |
| Current Assets | 2,019,000 | Yahoo |
| Total Assets | 5,069,000 | Yahoo |
| Current Liabilities | 1,591,000 | Yahoo |
| Liabilities | 6,350,000 | Calculated (Total Assets − TSE) |
| TSE | −1,281,000 | Yahoo Common Stock Equity |
| Total L+E | 5,069,000 | Yahoo |

**Action: New insert.**

---

## Flags Summary

| Year | Flag | Severity | Description |
|------|------|----------|-------------|
| 2018–2021 | L Brands pre-spinoff data | [WARNING] | Data reflects combined L Brands entity (included Victoria's Secret). Not comparable to post-spinoff BBWI. Cannot correct without proper source data. |
| 2018–2021 | SGA unverified | [WARNING] | No Yahoo data for these years; SGA may be incomplete per recurring convention |
| 2022 | Incorrect Dolt data | [ERROR] | All fields wrong — Revenue 5.3B (Dolt) vs 7.56B (Yahoo), Op Profit −2.8B vs +1.4B. reportDate also inconsistent. Correcting to Yahoo FY2022 values. |
| 2022–2025 | Negative TSE | [WARNING] | TSE is negative for all post-spinoff years. Valid — BBWI leveraged capital structure (long-term debt + accumulated losses). |

---

**Analysis complete.** Run `/insert-financials BBWI` to write all changed years to the database.

Years requiring changes: 2022 (correction), 2024 (new insert), 2025 (new insert). Years 2018–2021 and 2023 have no changes.
