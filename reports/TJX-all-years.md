# TJ Maxx (TJX) — FY2018–FY2024 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2019-02-02 | No change — all sources match |
| 2019 | 2020-02-01 | No change — all sources match |
| 2020 | 2021-01-30 | No change — all sources match (COVID year) |
| 2021 | 2022-01-29 | No change — all sources match (rounding only) |
| 2022 | 2023-01-28 | No change — values consistent |
| 2023 | 2024-02-03 | No change — values consistent |
| 2024 | 2025-02-01 | Correction: Operating Profit |

---

## FY2024 (reportDate: 2025-02-01)

### Anomaly Detection

**SGA check:** SEC and Yahoo both report SGA = 10,946,000. No separate marketing line. Single combined SGA — clean.

**SGA Rule 3 check:** Yahoo SGA (10,946,000) ≈ Total Operating Expenses from SEC (10,946,000). SGA = Total Operating Expenses for TJX, which is normal for a traditional retailer with no other operating expense lines.

**Gross margin:** 17,248,000 / 56,360,000 = 30.6% — within off-price benchmark (28–32%). ✓

**Balance sheet identity:** Total Assets (31,749,000) = Total Liabilities and SE (31,749,000). ✓

**Liabilities check:** 31,749,000 − 8,393,000 = 23,356,000 = Dolt Liabilities. ✓

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 56,360,000 | 56,360,000 | 56,360,000 | 56,360,000 |
| Cost of Goods | 39,112,000 | 39,112,000 | 39,112,000 | 39,112,000 |
| Gross Margin | 17,248,000 | 17,248,000 | 17,248,000 | 17,248,000 |
| SGA | 10,946,000 | 10,946,000 | 10,946,000 | 10,946,000 |
| Operating Profit | *no direct tag* | 6,302,000* | 6,483,000* | **6,302,000** |
| Net Profit | 4,864,000 | 4,864,000 | 4,864,000 | 4,864,000 |
| Inventory | 6,421,000 | 6,421,000 | 6,421,000 | 6,421,000 |
| Current Assets | 12,991,000 | 12,991,000 | 12,991,000 | 12,991,000 |
| Total Assets | 31,749,000 | 31,749,000 | 31,749,000 | 31,749,000 |
| Current Liabilities | 11,008,000 | 11,008,000 | 11,008,000 | 11,008,000 |
| Liabilities | 23,356,000 | 23,356,000 | 23,356,000 | 23,356,000 |
| Total SE | 8,393,000 | 8,393,000 | 8,393,000 | 8,393,000 |
| Total Liab & SE | 31,749,000 | 31,749,000 | 31,749,000 | 31,749,000 |

*\* Yahoo Operating Income = Revenue − COGS − SGA = 6,302,000*
*\* Dolt Operating Profit (6,483,000) = Revenue − COGS − SGA + Interest Income (181,000)*

### Reconcile

**Operating Profit [WARNING]:** Dolt FY2024 Operating Profit (6,483,000) equals Income Before Tax (includes $181,000 interest income). However, in FY2022 and FY2023, Dolt Operating Profit equals pure operating income (Revenue − COGS − SGA, no interest). This is inconsistent. **Recommended value: 6,302,000** — matching Yahoo Operating Income and consistent with the treatment used in FY2022–FY2023.

All other fields match SEC and Yahoo. No other adjustments needed.

---

## FY2023 (reportDate: 2024-02-03)

### Anomaly Detection

**SGA check:** Single combined SGA line — clean.

**Gross margin:** 16,266,000 / 54,217,000 = 30.0% — within off-price benchmark. ✓

**Balance sheet identity:** Total Assets (29,747,000) = Total Liabilities and SE (29,747,000). ✓

**Liabilities check:** 29,747,000 − 7,302,000 = 22,445,000 = Dolt Liabilities. ✓

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 54,217,000 | 54,217,000 | 54,217,000 | 54,217,000 |
| Cost of Goods | 37,951,000 | 37,951,000 | 37,951,000 | 37,951,000 |
| Gross Margin | 16,266,000 | 16,266,000 | 16,266,000 | 16,266,000 |
| SGA | 10,469,000 | 10,469,000 | 10,469,000 | 10,469,000 |
| Operating Profit | *no direct tag* | 5,797,000 | 5,797,000 | 5,797,000 |
| Net Profit | 4,474,000 | 4,474,000 | 4,474,000 | 4,474,000 |
| Inventory | 5,965,000 | 5,965,000 | 5,965,000 | 5,965,000 |
| Current Assets | 12,664,000 | 12,664,000 | 12,664,000 | 12,664,000 |
| Total Assets | 29,747,000 | 29,747,000 | 29,747,000 | 29,747,000 |
| Current Liabilities | 10,451,000 | 10,451,000 | 10,451,000 | 10,451,000 |
| Liabilities | 22,445,000 | 22,445,000 | 22,445,000 | 22,445,000 |
| Total SE | 7,302,000 | 7,302,000 | 7,302,000 | 7,302,000 |
| Total Liab & SE | 29,747,000 | 29,747,000 | 29,747,000 | 29,747,000 |

### Reconcile

All fields match across all three sources. No adjustments needed (see FY2024 note about Operating Profit consistency — FY2023 is consistent with pure operating income treatment).

---

## FY2022 (reportDate: 2023-01-28)

### Anomaly Detection

**SGA check:** Single combined SGA line — clean.

**Gross margin:** 13,787,000 / 49,936,000 = 27.6% — **slightly below** the off-price benchmark (28–32%). [WARNING] — may reflect inventory markdown pressure or category mix shift.

**Balance sheet identity:** Total Assets (28,349,000) = Total Liabilities and SE (28,349,000). ✓

**Liabilities check:** 28,349,000 − 6,364,000 = 21,985,000 = Dolt Liabilities. ✓

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 49,936,000 | 49,936,000 | 49,936,000 | 49,936,000 |
| Cost of Goods | 36,149,000 | 36,149,000 | 36,149,000 | 36,149,000 |
| Gross Margin | 13,787,000 | 13,787,000 | 13,787,000 | 13,787,000 |
| SGA | 8,927,000 | 8,927,000 | 8,927,000 | 8,927,000 |
| Operating Profit | *no direct tag* | 4,860,000 | 4,860,000 | 4,860,000 |
| Net Profit | 3,498,000 | 3,498,000 | 3,498,000 | 3,498,000 |
| Inventory | 5,819,000 | 5,819,000 | 5,819,000 | 5,819,000 |
| Current Assets | 12,456,000 | 12,456,000 | 12,456,000 | 12,456,000 |
| Total Assets | 28,349,000 | 28,349,000 | 28,349,000 | 28,349,000 |
| Current Liabilities | 10,305,000 | 10,305,000 | 10,305,000 | 10,305,000 |
| Liabilities | 21,985,000 | 21,985,000 | 21,985,000 | 21,985,000 |
| Total SE | 6,364,000 | 6,364,000 | 6,364,000 | 6,364,000 |
| Total Liab & SE | 28,349,000 | 28,349,000 | 28,349,000 | 28,349,000 |

### Reconcile

All fields match across sources. No adjustments needed.

---

## FY2021 (reportDate: 2022-01-29)

### Anomaly Detection

**SGA check:** Single combined SGA line — clean.

**Gross margin:** 13,836,170 / 48,549,982 = 28.5% — within off-price benchmark. ✓

**Balance sheet identity:** Total Assets (28,461,458) = Total Liabilities and SE (28,461,458). ✓

**Liabilities check:** 28,461,458 − 6,002,992 = 22,458,466 = Dolt Liabilities. ✓

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 48,550,000 | N/A | 48,549,982 | 48,549,982 |
| Cost of Goods | 34,713,800 | N/A | 34,713,812 | 34,713,812 |
| Gross Margin | 13,836,200 | N/A | 13,836,170 | 13,836,170 |
| SGA | 9,081,240 | N/A | 9,081,238 | 9,081,238 |
| Operating Profit | *no direct tag* | N/A | 4,397,608 | 4,397,608 |
| Net Profit | 3,282,820 | N/A | 3,282,815 | 3,282,815 |
| Inventory | 5,961,573 | N/A | 5,961,573 | 5,961,573 |
| Current Assets | 13,258,597 | N/A | 13,258,597 | 13,258,597 |
| Total Assets | 28,461,458 | N/A | 28,461,458 | 28,461,458 |
| Current Liabilities | 10,468,140 | N/A | 10,468,140 | 10,468,140 |
| Liabilities | 22,458,466 | N/A | 22,458,466 | 22,458,466 |
| Total SE | 6,002,992 | N/A | 6,002,992 | 6,002,992 |
| Total Liab & SE | 28,461,458 | N/A | 28,461,458 | 28,461,458 |

### Reconcile

Dolt values match SEC within minor rounding ($1K–$30K differences). No adjustments needed.

---

## FY2020 (reportDate: 2021-01-30)

### Anomaly Detection

**Gross margin:** 7,603,147 / 32,136,962 = 23.7% — **below** the off-price benchmark (28–32%). [WARNING] — COVID-19 impact. Stores were closed for portions of the fiscal year, revenue dropped 23% YoY (from $41.7B to $32.1B), and SGA remained relatively flat, compressing margins.

**Balance sheet identity:** Total Assets (30,813,555) = Total Liabilities and SE (30,813,555). ✓

**Liabilities check:** 30,813,555 − 5,832,684 = 24,980,871 = Dolt Liabilities. ✓

**Inventory:** 4,337,389 — down from prior year's 4,872,592. Less inventory due to store closures, expected.

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 32,137,000 | N/A | 32,136,962 | 32,136,962 |
| Cost of Goods | 24,533,800 | N/A | 24,533,815 | 24,533,815 |
| Gross Margin | 7,603,200 | N/A | 7,603,147 | 7,603,147 |
| SGA | 7,020,920 | N/A | 7,020,917 | 7,020,917 |
| Operating Profit | *no direct tag* | N/A | 89,263 | 89,263 |
| Net Profit | 90,470 | N/A | 90,470 | 90,470 |
| Inventory | 4,337,389 | N/A | 4,337,389 | 4,337,389 |
| Current Assets | 15,739,337 | N/A | 15,739,337 | 15,739,337 |
| Total Assets | 30,813,555 | N/A | 30,813,555 | 30,813,555 |
| Current Liabilities | 10,803,668 | N/A | 10,803,668 | 10,803,668 |
| Liabilities | 24,980,871 | N/A | 24,980,871 | 24,980,871 |
| Total SE | 5,832,684 | N/A | 5,832,684 | 5,832,684 |
| Total Liab & SE | 30,813,555 | N/A | 30,813,555 | 30,813,555 |

### Reconcile

All values match. The low gross margin is a COVID artifact — no correction needed.

---

## FY2019 (reportDate: 2020-02-01)

### Anomaly Detection

**Gross margin:** 11,871,197 / 41,716,977 = 28.5% — within off-price benchmark. ✓

**Balance sheet identity:** Total Assets (24,145,003) = Total Liabilities and SE (24,145,003). ✓

**Liabilities check:** 24,145,003 − 5,948,212 = 18,196,791 = Dolt Liabilities. ✓

**Total Assets jump:** 24,145,003 vs 14,326,029 in FY2018 (+69%). This reflects ASC 842 lease accounting adoption (operating lease ROU assets and liabilities added to the balance sheet) effective FY2019. [WARNING — expected, no correction needed.]

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 41,717,000 | N/A | 41,716,977 | 41,716,977 |
| Cost of Goods | 29,845,800 | N/A | 29,845,780 | 29,845,780 |
| Gross Margin | 11,871,200 | N/A | 11,871,197 | 11,871,197 |
| SGA | 7,454,990 | N/A | 7,454,988 | 7,454,988 |
| Operating Profit | *no direct tag* | N/A | 4,406,183 | 4,406,183 |
| Net Profit | 3,272,190 | N/A | 3,272,193 | 3,272,193 |
| Inventory | 4,872,592 | N/A | 4,872,592 | 4,872,592 |
| Current Assets | 8,890,622 | N/A | 8,890,622 | 8,890,622 |
| Total Assets | 24,145,003 | N/A | 24,145,003 | 24,145,003 |
| Current Liabilities | 7,150,247 | N/A | 7,150,247 | 7,150,247 |
| Liabilities | 18,196,791 | N/A | 18,196,791 | 18,196,791 |
| Total SE | 5,948,212 | N/A | 5,948,212 | 5,948,212 |
| Total Liab & SE | 24,145,003 | N/A | 24,145,003 | 24,145,003 |

### Reconcile

All values match within minor rounding. No adjustments needed.

---

## FY2018 (reportDate: 2019-02-02)

### Anomaly Detection

**Gross margin:** 11,141,757 / 38,972,934 = 28.6% — within off-price benchmark. ✓

**Balance sheet identity:** Total Assets (14,326,029) = Total Liabilities and SE (14,326,029). ✓

**Liabilities check:** 14,326,029 − 5,048,606 = 9,277,423 = Dolt Liabilities. ✓

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 38,972,934 | N/A | 38,972,934 | 38,972,934 |
| Cost of Goods | 27,831,177 | N/A | 27,831,177 | 27,831,177 |
| Gross Margin | 11,141,757 | N/A | 11,141,757 | 11,141,757 |
| SGA | 6,923,564 | N/A | 6,923,564 | 6,923,564 |
| Operating Profit | *no direct tag* | N/A | 4,173,211 | 4,173,211 |
| Net Profit | 3,059,798 | N/A | 3,059,798 | 3,059,798 |
| Inventory | 4,579,033 | N/A | 4,579,033 | 4,579,033 |
| Current Assets | 8,469,222 | N/A | 8,469,222 | 8,469,222 |
| Total Assets | 14,326,029 | N/A | 14,326,029 | 14,326,029 |
| Current Liabilities | 5,531,374 | N/A | 5,531,374 | 5,531,374 |
| Liabilities | 9,277,423 | N/A | 9,277,423 | 9,277,423 |
| Total SE | 5,048,606 | N/A | 5,048,606 | 5,048,606 |
| Total Liab & SE | 14,326,029 | N/A | 14,326,029 | 14,326,029 |

### Reconcile

All values match SEC exactly. No adjustments needed.

---

## Consolidated Findings

### Flags

| Year | Severity | Issue |
|------|----------|-------|
| 2024 | [WARNING] | **Operating Profit inconsistency:** Dolt FY2024 Operating Profit (6,483,000) includes interest income (181,000), while FY2022–FY2023 use pure operating income (Revenue − COGS − SGA). Recommended: correct FY2024 to 6,302,000 for consistency. |
| 2020 | [WARNING] | **Gross margin 23.7%** — below off-price benchmark due to COVID-19. Expected anomaly, no correction. |
| 2022 | [WARNING] | **Gross margin 27.6%** — slightly below 28–32% off-price benchmark. May reflect markdown pressure. |
| 2019 | [WARNING] | **Total Assets jump +69%** from FY2018 due to ASC 842 lease accounting adoption. Expected — no correction. |

### Data Quality

TJ Maxx data is well-maintained. All 13 standard fields match SEC source data across all 7 years (2018–2024) within rounding. Yahoo Finance cross-checks (FY2022–FY2024) confirm consistency. The only substantive issue is the Operating Profit treatment inconsistency in FY2024.

### Recommended Values (for SQL generation)

If running `/create-verified-dolt-db-financials-sql TJX 2024`, correct Operating Profit to **6,302,000**. All other years use current Dolt values.

---

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql TJX` to write all changed years to the database.

### Unresolved Flags for Review

1. **FY2024 Operating Profit (6,483,000 vs recommended 6,302,000)** — confirm whether to align with FY2022–FY2023 treatment (pure operating income) before inserting.
2. **FY2022 gross margin (27.6%)** — slightly below benchmark range. Verify against segment reporting if needed.
