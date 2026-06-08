# Boot Barn (BOOT) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-06
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2018 | 2018-03-31 | No change |
| 2019 | 2019-03-30 | No change |
| 2020 | 2020-03-28 | No change |
| 2021 | 2021-04-03 | No change |
| 2022 | 2022-04-02 | No change |
| 2023 | 2023-04-01 | No change |
| 2024 | 2025-03-29 | Correction: reportDate (2025-03-31 → 2025-03-29) |
| 2025 | 2026-03-28 | New insert |

---

## Company Metadata

- **company_name:** Boot Barn
- **CIK:** 1610250
- **display_name:** Boot Barn
- **ticker_symbol:** BOOT
- **Segment:** Specialty western/work lifestyle apparel
- **Fiscal year:** Ends late March/early April

---

## FY2018 — No Change

All values in Dolt match SEC. No action required.

---

## FY2019 — No Change

All values in Dolt match SEC. No action required.

---

## FY2020 — No Change

All values in Dolt match SEC. No action required. (FY2020 GM% ~32–33% — below 35–40% benchmark, valid for early growth phase + COVID impacts.)

---

## FY2021 — No Change

All values in Dolt match SEC. No action required.

---

## FY2022 — No Change

All values in Dolt match SEC. No action required.

---

## FY2023 — No Change

All values in Dolt match SEC. No action required.

---

## FY2024 Analysis

**reportDate:** 2025-03-29 (SEC) vs 2025-03-31 (current Dolt) — minor 2-day correction required.
All 13 financial fields verified correct against SEC. No financial changes needed.

### Anomaly Flags
- None. All financial values confirmed match SEC 10-K.

### Comparison Table (FY2024, values in $thousands)

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| reportDate | 2025-03-29 | — | 2025-03-31 | **2025-03-29** |
| Net Revenue | 1,911,104 | 1,911,104 | 1,911,104 | **1,911,104** |
| Cost of Goods | 1,194,066 | 1,194,066 | 1,194,066 | **1,194,066** |
| Gross Margin | 717,038 | 717,038 | 717,038 | **717,038** |
| SGA | 477,686 | 477,686 | 477,686 | **477,686** |
| Operating Profit | 239,352 | 239,352 | 239,352 | **239,352** |
| Net Profit | 180,942 | 180,942 | 180,942 | **180,942** |
| Inventory | 747,191 | 747,191 | 747,191 | **747,191** |
| Current Assets | 863,960 | 863,960 | 863,960 | **863,960** |
| Total Assets | 2,018,021 | 2,018,021 | 2,018,021 | **2,018,021** |
| Current Liabilities | 353,349 | 353,349 | 353,349 | **353,349** |
| Liabilities | 886,964 | 886,964 | 886,964 | **886,964** |
| Total Shareholder Equity | 1,131,057 | 1,131,057 | 1,131,057 | **1,131,057** |
| Total Liabilities and SE | 2,018,021 | 2,018,021 | 2,018,021 | **2,018,021** |

### Balance Sheet Check
- Total Assets (2,018,021) = Total L&SE (2,018,021) ✓
- Liabilities (886,964) = Total Assets − TSE (2,018,021 − 1,131,057 = 886,964) ✓

### Reconciled Recommendation (FY2024)
- **Action:** Update reportDate from 2025-03-31 to 2025-03-29. All financial values unchanged.
- **Source:** SEC 10-K (CIK 1610250)

---

## FY2025 Analysis

**Status:** New year — not yet in Dolt DB. Insert required.
**reportDate:** 2026-03-28

### Anomaly Flags
- None. Gross margin 38.1% within expected 35–40% range. ✓
- SGA: Single combined `SellingGeneralAndAdministrativeExpense` tag. ✓
- Balance sheet: 2,450,075 = 2,450,075 ✓

### Comparison Table (FY2025, values in $thousands)

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| reportDate | 2026-03-28 | 2026-03-28 | — | **2026-03-28** |
| Net Revenue | 2,253,859 | 2,253,859 | — | **2,253,859** |
| Cost of Goods | 1,395,504 | 1,395,504 | — | **1,395,504** |
| Gross Margin | 858,355 | 858,355 | — | **858,355** |
| SGA | 559,210 | 559,210 | — | **559,210** |
| Operating Profit | 299,145 | 299,145 | — | **299,145** |
| Net Profit | 225,880 | 225,880 | — | **225,880** |
| Inventory | 844,637 | 844,637 | — | **844,637** |
| Current Assets | 1,034,399 | 1,034,399 | — | **1,034,399** |
| Total Assets | 2,450,075 | 2,450,075 | — | **2,450,075** |
| Current Liabilities | 390,972 | 390,972 | — | **390,972** |
| Liabilities | 1,131,419 | 1,131,419 | — | **1,131,419** |
| Total Shareholder Equity | 1,318,656 | 1,318,656 | — | **1,318,656** |
| Total Liabilities and SE | 2,450,075 | 2,450,075 | — | **2,450,075** |

### Balance Sheet Check
- Total Assets (2,450,075) = Total L&SE (2,450,075) ✓
- Liabilities (1,131,419) = Total Assets − TSE (2,450,075 − 1,318,656 = 1,131,419) ✓
- Gross margin: 858,355 / 2,253,859 = 38.1% — within 35–40% expected range ✓

### Reconciled Recommendation (FY2025)
- **Action:** New insert. All values from SEC 10-K.
- **Source:** SEC 10-K (CIK 1610250, FY2025 ending 2026-03-28)

---

## Final Summary

**Analysis complete.** Run `/insert-financials BOOT` to write all changed years to the database.

**Changed years:** FY2024 (reportDate fix), FY2025 (new insert)
**Unchanged years:** FY2018–FY2023

**No unresolved [ERROR] flags.**
