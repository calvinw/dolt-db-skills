# Petco Health & Wellness Company (WOOF) — New Company Data (FY2021–FY2025)

**Generated:** 2026-06-01
**Source:** /create-new-company-sql skill
**Action:** New company setup

---

## Company Info

| Field | Value |
|-------|-------|
| company | Petco |
| CIK | 1826470 |
| display_name | Petco Health & Wellness Company |
| ticker_symbol | WOOF |
| segment | Health & Pharmacy |
| subsegment | NULL |
| currency | USD |
| units | thousands |

## Data Coverage

| Year | reportDate | SEC | Yahoo | Status |
|------|-----------|-----|-------|--------|
| 2021 | 2022-01-29 | ✓ | — | New insert |
| 2022 | 2023-01-28 | ✓ | ✓ | New insert |
| 2023 | 2024-02-03 | ✓ | ✓ | New insert |
| 2024 | 2025-02-01 | ✓ | ✓ | New insert |
| 2025 | 2026-01-31 | ✓ | ✓ | New insert |

**Years with no data (skipped):** 2018, 2019, 2020 — Petco (formerly PET Acquisition LLC) had no public SEC filings before FY2021.

## Reconciled Values (in $000s)

All values sourced from SEC 10-K filings (the authoritative source). Yahoo Finance values were cross-checked and matched within rounding for all available years.

| Field | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|-------|--------|--------|--------|--------|--------|
| reportDate | 2022-01-29 | 2023-01-28 | 2024-02-03 | 2025-02-01 | 2026-01-31 |
| Net Revenue | 5,807,149 | 6,035,967 | 6,255,284 | 6,116,462 | 5,961,467 |
| Cost of Goods | 3,380,539 | 3,608,860 | 3,901,449 | 3,792,060 | 3,656,395 |
| Gross Margin | 2,426,610 | 2,427,107 | 2,353,835 | 2,324,402 | 2,305,072 |
| SGA | 2,160,539 | 2,201,548 | 2,311,625 | 2,317,351 | 2,184,639 |
| Operating Profit | 266,071 | 225,559 | -1,180,314 | 7,051 | 120,433 |
| Net Profit | 164,417 | 90,801 | -1,280,210 | -101,816 | 9,066 |
| Inventory | 675,111 | 652,430 | 684,502 | 653,329 | 590,210 |
| Current Assets | 1,070,777 | 1,015,994 | 951,744 | 973,619 | 1,019,786 |
| Total Assets | 6,497,941 | 6,612,829 | 5,363,152 | 5,194,430 | 5,173,425 |
| Current Liabilities | 1,053,139 | 1,021,258 | 1,113,143 | 1,139,163 | 1,134,141 |
| Liabilities | 4,242,122 | 4,231,352 | 4,178,723 | 4,080,800 | 4,009,171 |
| Total SE | 2,255,819 | 2,381,477 | 1,184,429 | 1,113,630 | 1,164,254 |
| Total LSE | 6,497,941 | 6,612,829 | 5,363,152 | 5,194,430 | 5,173,425 |

## Anomaly Checks

| Check | Result |
|------|--------|
| Balance Sheet Identity | ✓ All years: Total Assets = Total LSE |
| Gross Margin | ~38–42% (above Health & Pharmacy benchmark of 18–25%, but reasonable for pet specialty retailer with services mix) |
| SGA | Single combined line — no composite issue |
| Inventory | Large positive values — correct for physical retailer |
| Negative Equity | None detected |

## Files Written

| File | Path |
|------|------|
| SQL | `extract/2026/create_company/WOOF_create.sql` |
| Report | `reports/WOOF-create.md` |

**SQL covers:**
- `company_info` — 1 INSERT
- `financials` — 5 REPLACE statements (years: 2021, 2022, 2023, 2024, 2025)

---

*No existing Dolt data was overwritten — this is a new company.*
