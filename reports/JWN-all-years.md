# Nordstrom (JWN) — FY2018–FY2024 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

**Sources:** SEC 10-K filings. Yahoo Finance unavailable (Nordstrom went private — no longer on Yahoo).

---

## Per-Year Summary

| Year | reportDate | Action | Notes |
|------|-----------|--------|-------|
| 2018 | 2019-02-02 | No change | All values match SEC |
| 2019 | 2020-02-01 | Correction: Net Revenue, Gross Margin | Dolt used Net Sales (15,132,000K) instead of total Revenue (15,524,000K) |
| 2020 | 2021-01-30 | No change | All values match SEC |
| 2021 | 2022-01-29 | No change | All values match SEC |
| 2022 | 2023-01-28 | No change | All values match SEC |
| 2023 | 2024-02-03 | No change | All values match SEC |
| 2024 | 2025-02-01 | No change | All values match SEC |

---

## FY2018 — Analysis

**reportDate:** 2019-02-02

### Side-by-Side Comparison

| Field | SEC | Dolt (current) | Recommended |
|-------|-----|---------------|-------------|
| Net Revenue | 15,860,000 | 15,860,000 | 15,860,000 |
| Cost of Goods | 10,155,000 | 10,155,000 | 10,155,000 |
| Gross Margin | 5,705,000 | 5,705,000 | 5,705,000 |
| SGA | 4,868,000 | 4,868,000 | 4,868,000 |
| Operating Profit | 837,000 | 837,000 | 837,000 |
| Net Profit | 564,000 | 564,000 | 564,000 |
| Inventory | 1,978,000 | 1,978,000 | 1,978,000 |
| Current Assets | 3,374,000 | 3,374,000 | 3,374,000 |
| Total Assets | 7,886,000 | 7,886,000 | 7,886,000 |
| Current Liabilities | 3,381,000 | 3,381,000 | 3,381,000 |
| Liabilities | 7,013,000 | 7,013,000 | 7,013,000 |
| Total SE | 873,000 | 873,000 | 873,000 |
| Total L+SE | 7,886,000 | 7,886,000 | 7,886,000 |

### Anomaly Checks

- **Balance sheet identity:** Total Assets (7,886,000) = Total L+SE (7,886,000) ✓
- **Gross margin:** 36.0% — within department store range (35–45%) ✓
- **Inventory:** $1,978,000K — present and consistent for a traditional retailer ✓

### Verdict

**No changes needed.** All Dolt values match SEC.

---

## FY2019 — Analysis

**reportDate:** 2020-02-01

### Side-by-Side Comparison

| Field | SEC | Dolt (current) | Recommended |
|-------|-----|---------------|-------------|
| Net Revenue* | 15,524,000 | 15,132,000 | 15,524,000 |
| Cost of Goods | 9,932,000 | 9,932,000 | 9,932,000 |
| Gross Margin* | 5,592,000 | 5,200,000 | 5,592,000 |
| SGA | 4,808,000 | 4,808,000 | 4,808,000 |
| Operating Profit | 784,000 | 784,000 | 784,000 |
| Net Profit | 496,000 | 496,000 | 496,000 |
| Inventory | 1,920,000 | 1,920,000 | 1,920,000 |
| Current Assets | 3,230,000 | 3,230,000 | 3,230,000 |
| Total Assets | 9,737,000 | 9,737,000 | 9,737,000 |
| Current Liabilities | 3,520,000 | 3,520,000 | 3,520,000 |
| Liabilities | 8,758,000 | 8,758,000 | 8,758,000 |
| Total SE | 979,000 | 979,000 | 979,000 |
| Total L+SE | 9,737,000 | 9,737,000 | 9,737,000 |

`*` denotes fields with disagreement

### Anomaly Detection

**`[WARNING]` — Net Revenue mismatch:** Dolt stores 15,132,000K, which equals `jwn_NetSalesRevenue` (Net Sales only). The SEC total Revenue (`us-gaap_Revenues`) is 15,524,000K, which includes $392,000K in Credit Card revenues. All other years in the Dolt DB correctly use total Revenue. This appears to be a data entry error for FY2019 only.

**Balance sheet identity:** Total Assets (9,737,000) = Total L+SE (9,737,000) ✓

**Gross margin (corrected):** 5,592/15,524 = 36.0% — within department store range ✓

**Inventory:** $1,920,000K — present and consistent ✓

### Reconciled Recommendation

| Field | Recommended Value | Source | Notes |
|-------|------------------|--------|-------|
| Net Revenue | 15,524,000 | SEC | Dolt incorrectly used Net Sales (excludes credit card revenue) |
| Gross Margin | 5,592,000 | Computed | 15,524,000 − 9,932,000 |

All other fields match SEC and require no change.

---

## FY2020 — Analysis

**reportDate:** 2021-01-30

### Side-by-Side Comparison

| Field | SEC | Dolt (current) | Recommended |
|-------|-----|---------------|-------------|
| Net Revenue | 10,715,000 | 10,715,000 | 10,715,000 |
| Cost of Goods | 7,600,000 | 7,600,000 | 7,600,000 |
| Gross Margin | 3,115,000 | 3,115,000 | 3,115,000 |
| SGA | 4,162,000 | 4,162,000 | 4,162,000 |
| Operating Profit | -1,047,000 | -1,047,000 | -1,047,000 |
| Net Profit | -690,000 | -690,000 | -690,000 |
| Inventory | 1,863,000 | 1,863,000 | 1,863,000 |
| Current Assets | 3,642,000 | 3,642,000 | 3,642,000 |
| Total Assets | 9,538,000 | 9,538,000 | 9,538,000 |
| Current Liabilities | 4,120,000 | 4,120,000 | 4,120,000 |
| Liabilities | 9,233,000 | 9,233,000 | 9,233,000 |
| Total SE | 305,000 | 305,000 | 305,000 |
| Total L+SE | 9,538,000 | 9,538,000 | 9,538,000 |

### Anomaly Checks

- **Balance sheet identity:** Total Assets (9,538,000) = Total L+SE (9,538,000) ✓
- **Gross margin:** `[WARNING]` 3,115/10,715 = 29.1% — below department store range (35–45%). This is a COVID-impacted year (fiscal 2020 ended Jan 30, 2021); the low margin is expected and consistent with the pandemic's effect on retail.
- **Inventory:** $1,863,000K — present ✓
- **Negative equity:** Total SE is $305,000K — low but positive ✓
- **Operating Loss:** -$1,047,000K — consistent with COVID impact ✓

### Verdict

**No changes needed.** All values match SEC. The low gross margin is flagged but expected for a COVID year.

---

## FY2021 — Analysis

**reportDate:** 2022-01-29

### Side-by-Side Comparison

| Field | SEC | Dolt (current) | Recommended |
|-------|-----|---------------|-------------|
| Net Revenue | 14,789,000 | 14,789,000 | 14,789,000 |
| Cost of Goods | 9,344,000 | 9,344,000 | 9,344,000 |
| Gross Margin | 5,445,000 | 5,445,000 | 5,445,000 |
| SGA | 4,953,000 | 4,953,000 | 4,953,000 |
| Operating Profit | 492,000 | 492,000 | 492,000 |
| Net Profit | 178,000 | 178,000 | 178,000 |
| Inventory | 2,289,000 | 2,289,000 | 2,289,000 |
| Current Assets | 3,172,000 | 3,172,000 | 3,172,000 |
| Total Assets | 8,869,000 | 8,869,000 | 8,869,000 |
| Current Liabilities | 3,314,000 | 3,314,000 | 3,314,000 |
| Liabilities | 8,288,000 | 8,288,000 | 8,288,000 |
| Total SE | 581,000 | 581,000 | 581,000 |
| Total L+SE | 8,869,000 | 8,869,000 | 8,869,000 |

### Anomaly Checks

- **Balance sheet identity:** Total Assets (8,869,000) = Total L+SE (8,869,000) ✓
- **Gross margin:** 5,445/14,789 = 36.8% — within department store range ✓
- **Inventory:** $2,289,000K — present ✓

### Verdict

**No changes needed.** All values match SEC.

---

## FY2022 — Analysis

**reportDate:** 2023-01-28

### Side-by-Side Comparison

| Field | SEC | Dolt (current) | Recommended |
|-------|-----|---------------|-------------|
| Net Revenue | 15,530,000 | 15,530,000 | 15,530,000 |
| Cost of Goods | 10,019,000 | 10,019,000 | 10,019,000 |
| Gross Margin | 5,511,000 | 5,511,000 | 5,511,000 |
| SGA | 5,046,000 | 5,046,000 | 5,046,000 |
| Operating Profit | 465,000 | 465,000 | 465,000 |
| Net Profit | 245,000 | 245,000 | 245,000 |
| Inventory | 1,941,000 | 1,941,000 | 1,941,000 |
| Current Assets | 3,209,000 | 3,209,000 | 3,209,000 |
| Total Assets | 8,745,000 | 8,745,000 | 8,745,000 |
| Current Liabilities | 2,990,000 | 2,990,000 | 2,990,000 |
| Liabilities | 8,006,000 | 8,006,000 | 8,006,000 |
| Total SE | 739,000 | 739,000 | 739,000 |
| Total L+SE | 8,745,000 | 8,745,000 | 8,745,000 |

### Anomaly Checks

- **Balance sheet identity:** Total Assets (8,745,000) = Total L+SE (8,745,000) ✓
- **Gross margin:** 5,511/15,530 = 35.5% — within department store range ✓
- **Inventory:** $1,941,000K — present ✓

### Verdict

**No changes needed.** All values match SEC.

---

## FY2023 — Analysis

**reportDate:** 2024-02-03

### Side-by-Side Comparison

| Field | SEC | Dolt (current) | Recommended |
|-------|-----|---------------|-------------|
| Net Revenue | 14,693,000 | 14,693,000 | 14,693,000 |
| Cost of Goods | 9,303,000 | 9,303,000 | 9,303,000 |
| Gross Margin | 5,390,000 | 5,390,000 | 5,390,000 |
| SGA | 4,855,000 | 4,855,000 | 4,855,000 |
| Operating Profit | 251,000 | 251,000 | 251,000 |
| Net Profit | 134,000 | 134,000 | 134,000 |
| Inventory | 1,888,000 | 1,888,000 | 1,888,000 |
| Current Assets | 3,136,000 | 3,136,000 | 3,136,000 |
| Total Assets | 8,444,000 | 8,444,000 | 8,444,000 |
| Current Liabilities | 3,072,000 | 3,072,000 | 3,072,000 |
| Liabilities | 7,596,000 | 7,596,000 | 7,596,000 |
| Total SE | 848,000 | 848,000 | 848,000 |
| Total L+SE | 8,444,000 | 8,444,000 | 8,444,000 |

### Anomaly Checks

- **Balance sheet identity:** Total Assets (8,444,000) = Total L+SE (8,444,000) ✓
- **Gross margin:** 5,390/14,693 = 36.7% — within department store range ✓
- **Inventory:** $1,888,000K — present ✓
- **Restructuring:** SEC shows $284,000K in Canada wind-down costs as a separate line (`us-gaap_RestructuringCosts`). This is correctly excluded from SGA and flows through Operating Profit. Dolt correctly reflects all values. ✓

### Verdict

**No changes needed.** All values match SEC.

---

## FY2024 — Analysis

**reportDate:** 2025-02-01

### Side-by-Side Comparison

| Field | SEC | Dolt (current) | Recommended |
|-------|-----|---------------|-------------|
| Net Revenue | 15,016,000 | 15,016,000 | 15,016,000 |
| Cost of Goods | 9,396,000 | 9,396,000 | 9,396,000 |
| Gross Margin | 5,620,000 | 5,620,000 | 5,620,000 |
| SGA | 5,125,000 | 5,125,000 | 5,125,000 |
| Operating Profit | 495,000 | 495,000 | 495,000 |
| Net Profit | 294,000 | 294,000 | 294,000 |
| Inventory | 2,104,000 | 2,104,000 | 2,104,000 |
| Current Assets | 3,689,000 | 3,689,000 | 3,689,000 |
| Total Assets | 8,966,000 | 8,966,000 | 8,966,000 |
| Current Liabilities | 3,088,000 | 3,088,000 | 3,088,000 |
| Liabilities | 7,826,000 | 7,826,000 | 7,826,000 |
| Total SE | 1,140,000 | 1,140,000 | 1,140,000 |
| Total L+SE | 8,966,000 | 8,966,000 | 8,966,000 |

### Anomaly Checks

- **Balance sheet identity:** Total Assets (8,966,000) = Total L+SE (8,966,000) ✓
- **Gross margin:** 5,620/15,016 = 37.4% — within department store range ✓
- **Inventory:** $2,104,000K — present ✓
- **Restatement check:** No restated prior-year figures in this filing compared to what's already in Dolt. ✓

### Verdict

**No changes needed.** All values match SEC.

---

## Summary of Findings

| Year | Status | Fields to Fix |
|------|--------|---------------|
| 2018 | ✓ Matches SEC | None |
| 2019 | ⚠️ Net Revenue mismatch | Net Revenue (15,132,000 → 15,524,000), Gross Margin (5,200,000 → 5,592,000) |
| 2020 | ✓ Matches SEC (COVID year — low GM flagged as WARNING) | None |
| 2021 | ✓ Matches SEC | None |
| 2022 | ✓ Matches SEC | None |
| 2023 | ✓ Matches SEC | None |
| 2024 | ✓ Matches SEC | None |

**Only one issue found:** FY2019 Net Revenue was stored as Net Sales only ($15,132,000K) instead of total Revenue ($15,524,000K). All other years and all other fields match SEC perfectly.

**Unresolved flags:**
- FY2019: Net Revenue correction needed (+$392,000K to include Credit Card revenues)
- FY2020: Gross margin at 29.1% is below the department store benchmark but expected due to COVID

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql JWN` to write all changed years to the database.
