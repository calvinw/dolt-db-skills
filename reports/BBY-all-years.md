# Best Buy (BBY) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-06
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2018 | 2019-02-02 | No change |
| 2019 | 2020-02-01 | No change |
| 2020 | 2021-01-30 | No change |
| 2021 | 2022-01-29 | No change |
| 2022 | 2023-01-28 | No change |
| 2023 | 2024-02-03 | No change |
| 2024 | 2025-02-01 | Correction: reportDate (2025-02-03 → 2025-02-01) |
| 2025 | 2026-01-31 | New insert |

---

## Company Metadata

- **company_name:** Best Buy
- **CIK:** 764478
- **display_name:** Best Buy
- **ticker_symbol:** BBY
- **Segment:** Specialty electronics retailer
- **Fiscal year:** Ends late January/early February

---

## FY2018 — No Change

All values in Dolt match SEC. No action required.

---

## FY2019 — No Change

All values in Dolt match SEC. No action required.

---

## FY2020 — No Change

All values in Dolt match SEC. No action required.

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

**reportDate:** 2025-02-01 (SEC) vs 2025-02-03 (current Dolt) — minor 2-day correction required.
All 13 financial fields verified correct against SEC. No financial changes needed.

### Anomaly Flags
- None. All financial values confirmed match SEC 10-K.

### Comparison Table (FY2024, values in $thousands)

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| reportDate | 2025-02-01 | — | 2025-02-03 | **2025-02-01** |
| Net Revenue | 41,528,000 | 41,528,000 | 41,528,000 | **41,528,000** |
| Cost of Goods | 32,143,000 | 32,143,000 | 32,143,000 | **32,143,000** |
| Gross Margin | 9,385,000 | 9,385,000 | 9,385,000 | **9,385,000** |
| SGA | 7,651,000 | 7,651,000 | 7,651,000 | **7,651,000** |
| Operating Profit | 1,262,000 | 1,262,000 | 1,262,000 | **1,262,000** |
| Net Profit | 927,000 | 927,000 | 927,000 | **927,000** |
| Inventory | 5,085,000 | 5,085,000 | 5,085,000 | **5,085,000** |
| Current Assets | 8,224,000 | 8,224,000 | 8,224,000 | **8,224,000** |
| Total Assets | 14,782,000 | 14,782,000 | 14,782,000 | **14,782,000** |
| Current Liabilities | 8,016,000 | 8,016,000 | 8,016,000 | **8,016,000** |
| Liabilities | 11,974,000 | 11,974,000 | 11,974,000 | **11,974,000** |
| Total Shareholder Equity | 2,808,000 | 2,808,000 | 2,808,000 | **2,808,000** |
| Total Liabilities and SE | 14,782,000 | 14,782,000 | 14,782,000 | **14,782,000** |

### Balance Sheet Check
- Total Assets (14,782,000) = Total L&SE (14,782,000) ✓
- Liabilities (11,974,000) = Total Assets − TSE (14,782,000 − 2,808,000 = 11,974,000) ✓

### Reconciled Recommendation (FY2024)
- **Action:** Update reportDate from 2025-02-03 to 2025-02-01. All financial values unchanged.
- **Source:** SEC 10-K (CIK 764478)

---

## FY2025 Analysis

**Status:** New year — not yet in Dolt DB. Insert required.
**reportDate:** 2026-01-31

### Anomaly Flags
- [WARNING] Gross margin 22.5% — slightly below 22–28% benchmark floor, consistent with BBY's known thin electronics margins. Not a data error.
- SGA: Single combined `SellingGeneralAndAdministrativeExpense` tag. Restructuring charges excluded (separate line). ✓
- Balance sheet check: 14,670,000 = 14,670,000 ✓

### Comparison Table (FY2025, values in $thousands)

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| reportDate | 2026-01-31 | 2026-01-31 | — | **2026-01-31** |
| Net Revenue | 41,691,000 | 41,691,000 | — | **41,691,000** |
| Cost of Goods | 32,318,000 | 32,318,000 | — | **32,318,000** |
| Gross Margin | 9,373,000 | 9,373,000 | — | **9,373,000** |
| SGA | 7,623,000 | 7,623,000 | — | **7,623,000** |
| Operating Profit | 1,389,000 | 1,750,000 * | — | **1,389,000** |
| Net Profit | 1,069,000 | 1,069,000 | — | **1,069,000** |
| Inventory | 5,230,000 | 5,230,000 | — | **5,230,000** |
| Current Assets | 8,504,000 | 8,504,000 | — | **8,504,000** |
| Total Assets | 14,670,000 | 14,670,000 | — | **14,670,000** |
| Current Liabilities | 7,679,000 | 7,679,000 | — | **7,679,000** |
| Liabilities | 11,706,000 | 11,706,000 | — | **11,706,000** |
| Total Shareholder Equity | 2,964,000 | 2,964,000 | — | **2,964,000** |
| Total Liabilities and SE | 14,670,000 | 14,670,000 | — | **14,670,000** |

\* Yahoo Operating Profit 1,750,000 differs from SEC 1,389,000 — Yahoo excludes restructuring/impairment charges. Use SEC value.

### Balance Sheet Check
- Total Assets (14,670,000) = Total L&SE (14,670,000) ✓
- Liabilities (11,706,000) = Total Assets − TSE (14,670,000 − 2,964,000 = 11,706,000) ✓
- Gross margin: 9,373,000 / 41,691,000 = 22.5% — slightly below 22–28% range, consistent with electronics retail

### Reconciled Recommendation (FY2025)
- **Action:** New insert. All values from SEC 10-K.
- **Source:** SEC 10-K (CIK 764478, FY2025 ending 2026-01-31)

---

## Final Summary

**Analysis complete.** Run `/insert-financials BBY` to write all changed years to the database.

**Changed years:** FY2024 (reportDate fix), FY2025 (new insert)
**Unchanged years:** FY2018–FY2023

**No unresolved [ERROR] flags.** One [WARNING] on FY2025 gross margin — confirmed valid for electronics retail.
