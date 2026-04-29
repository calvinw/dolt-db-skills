# YETI (YETI) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-04-29
**Source:** /analyze-financials skill

---

## Step 4 — Anomaly Detection

**Company context:** YETI is a premium specialty outdoor/lifestyle brand (coolers, drinkware, gear). Single combined `us-gaap_SellingGeneralAndAdministrativeExpense` tag — no separate marketing or ops-tech lines. Physical goods company — inventory expected in all years.

**No entry in company-notes.md for YETI.** Notes added at end.

### SGA Rules
- Rule 1: No separate marketing expense line — SGA is a single combined line. ✓
- Rule 2: No platform/ops-tech line (physical goods brand, not a marketplace). ✓
- Rule 3: Yahoo SGA vs. Total Expenses — 2022: 43%, 2023: 50%, 2024: 52%, 2025: 52% — none ≈ 100%. ✓
- Rule 4: N/A — combined SGA tag exists in all years. ✓

### Balance Sheet Identity Checks

| Year | Total Assets | Total L&SE | Diff | Pass? |
|------|-------------|-----------|------|-------|
| 2018 | 514,213 | 514,213 | 0 | ✓ |
| 2019 | 629,539 | 629,539 | 0 | ✓ |
| 2020 | 737,067 | 737,067 | 0 | ✓ |
| 2021 | 1,096,364 | 1,096,364 | 0 | ✓ |
| 2022 | 1,076,765 | 1,076,765 | 0 | ✓ |
| 2023 | 1,297,192 | 1,297,192 | 0 | ✓ |
| 2024 | 1,286,120 | 1,286,120 | 0 | ✓ |
| 2025 | 1,235,418 | 1,235,418 | 0 | ✓ |

### Gross Margin Sanity Check (Specialty benchmark: 35–55%)

| Year | GM% | Flag |
|------|-----|------|
| 2018 | 49.2% | ✓ within range |
| 2019 | 52.0% | ✓ within range |
| 2020 | 57.6% | [WARNING] above 55% ceiling |
| 2021 | 57.8% | [WARNING] above 55% ceiling |
| 2022 | 47.9% | ✓ (product recall impacted COGS) |
| 2023 | 56.8% | [WARNING] above 55% ceiling |
| 2024 | 58.1% | [WARNING] above 55% ceiling |
| 2025 | 57.4% | [WARNING] above 55% ceiling |

Assessment: Consistent with YETI's premium brand positioning — not a data error. 2022 dip explained by product recall costs in COGS.

### reportDate Discrepancy — FY2024
[WARNING] Dolt has 2024-12-31, but SEC fiscal year actually ended 2024-12-28 (last Saturday of December). Yahoo normalizes to 12-31, which is how the wrong date entered Dolt. All financial values are correct; only reportDate needs correcting.

### FY2025 — New Year
No Dolt row exists. SEC and Yahoo agree on all financial values (Yahoo rounding differences ≤4K, within noise). Ready to insert.

---

## Step 5 — Side-by-Side Comparison (values in $thousands)

### FY2018–2021 (SEC vs Dolt; Yahoo N/A)

| Field | 2018 SEC | 2018 Dolt | 2019 SEC | 2019 Dolt | 2020 SEC | 2020 Dolt | 2021 SEC | 2021 Dolt |
|---|---|---|---|---|---|---|---|---|
| reportDate | 2018-12-29 | 2018-12-29 | 2019-12-28 | 2019-12-28 | 2021-01-02 | 2021-01-02 | 2022-01-01 | 2022-01-01 |
| Net Revenue | 778,833 | 778,833 | 913,734 | 913,734 | 1,091,721 | 1,091,721 | 1,410,989 | 1,410,989 |
| Cost of Goods | 395,705 | 395,705 | 438,420 | 438,420 | 462,918 | 462,918 | 594,876 | 594,876 |
| Gross Margin | 383,128 | 383,128 | 475,314 | 475,314 | 628,803 | 628,803 | 816,113 | 816,113 |
| SGA | 280,972 | 280,972 | 385,543 | 385,543 | 414,570 | 414,570 | 541,175 | 541,175 |
| Operating Profit | 102,156 | 102,156 | 89,771 | 89,771 | 214,233 | 214,233 | 274,938 | 274,938 |
| Net Profit | 57,763 | 57,763 | 50,434 | 50,434 | 155,801 | 155,801 | 212,602 | 212,602 |
| Inventory | 145,423 | 145,423 | 185,700 | 185,700 | 140,111 | 140,111 | 318,864 | 318,864 |
| Current Assets | 297,013 | 297,013 | 360,547 | 360,547 | 476,497 | 476,497 | 770,167 | 770,167 |
| Total Assets | 514,213 | 514,213 | 629,539 | 629,539 | 737,067 | 737,067 | 1,096,364 | 1,096,364 |
| Current Liabilities | 187,338 | 187,338 | 170,312 | 170,312 | 287,759 | 287,759 | 403,713 | 403,713 |
| Liabilities | 485,242 | 485,242 | 507,534 | 507,534 | 448,649 | 448,649 | 578,541 | 578,541 |
| Total SE | 28,971 | 28,971 | 122,005 | 122,005 | 288,418 | 288,418 | 517,823 | 517,823 |
| Total L&SE | 514,213 | 514,213 | 629,539 | 629,539 | 737,067 | 737,067 | 1,096,364 | 1,096,364 |

All match perfectly.

### FY2022–2025 (SEC | Yahoo | Dolt; * = disagreement)

| Field | 2022 SEC | 2022 Yahoo | 2022 Dolt | 2023 SEC | 2023 Yahoo | 2023 Dolt | 2024 SEC | 2024 Yahoo | 2024 Dolt | 2025 SEC | 2025 Yahoo | 2025 Dolt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reportDate | 2022-12-31 | 2022-12-31 | 2022-12-31 | 2023-12-30 | 2023-12-31 | 2023-12-30 | 2024-12-28 | 2024-12-31 | 2024-12-31 * | 2026-01-03 | 2025-12-31 | N/A |
| Net Revenue | 1,595,222 | ~1,595,220 | 1,595,222 | 1,658,713 | ~1,658,710 | 1,658,713 | 1,829,873 | ~1,829,870 | 1,829,873 | 1,868,494 | ~1,868,490 | — |
| Cost of Goods | 831,821 | 831,821 | 831,821 | 715,527 | 715,527 | 715,527 | 766,589 | 766,589 | 766,589 | 795,810 | 795,810 | — |
| Gross Margin | 763,401 | 763,401 | 763,401 | 943,186 | 943,186 | 943,186 | 1,063,284 | ~1,063,280 | 1,063,284 | 1,072,684 | ~1,072,680 | — |
| SGA | 637,040 | 637,040 | 637,040 | 717,728 | 717,728 | 717,728 | 817,908 | 817,908 | 817,908 | 859,127 | 859,127 | — |
| Operating Profit | 126,361 | 126,361 | 126,361 | 225,458 | 225,458 | 225,458 | 245,376 | 245,376 | 245,376 | 213,557 | 213,557 | — |
| Net Profit | 89,693 | 89,693 | 89,693 | 169,885 | 169,885 | 169,885 | 175,689 | 175,689 | 175,689 | 165,387 | 165,387 | — |
| Inventory | 371,412 | 371,412 | 371,412 | 337,208 | 337,208 | 337,208 | 310,058 | 310,058 | 310,058 | 290,611 | 290,611 | — |
| Current Assets | 718,920 | 718,920 | 718,920 | 914,405 | 914,405 | 914,405 | 826,766 | 826,766 | 826,766 | 660,326 | 660,326 | — |
| Total Assets | 1,076,765 | ~1,076,760 | 1,076,765 | 1,297,192 | ~1,297,190 | 1,297,192 | 1,286,120 | 1,286,120 | 1,286,120 | 1,235,418 | ~1,235,420 | — |
| Current Liabilities | 409,040 | 409,040 | 409,040 | 398,353 | 398,353 | 398,353 | 379,504 | 379,504 | 379,504 | 334,339 | 334,339 | — |
| Liabilities | 550,288 | — | 550,288 | 573,582 | — | 573,582 | 546,013 | — | 546,013 | 585,142 | — | — |
| Total SE | 526,477 | 526,477 | 526,477 | 723,610 | 723,610 | 723,610 | 740,107 | 740,107 | 740,107 | 650,276 | 650,276 | — |
| Total L&SE | 1,076,765 | ~1,076,760 | 1,076,765 | 1,297,192 | ~1,297,190 | 1,297,192 | 1,286,120 | 1,286,120 | 1,286,120 | 1,235,418 | ~1,235,420 | — |

Yahoo differences of ≤5K are rounding artifacts only, not real discrepancies.

---

## Step 6 — Reconciled Recommendations

| Year | Action | Notes |
|------|--------|-------|
| 2018 | No change | All fields match SEC exactly |
| 2019 | No change | All fields match SEC exactly |
| 2020 | No change | All fields match SEC exactly |
| 2021 | No change | All fields match SEC exactly |
| 2022 | No change | All fields match SEC exactly |
| 2023 | No change | All fields match SEC exactly |
| 2024 | Correct reportDate only | Change 2024-12-31 → 2024-12-28 (SEC fiscal year end). All financial values correct. |
| 2025 | New insert | Not yet in Dolt. All values from SEC 10-K; Yahoo confirms within rounding. |

### FY2025 Recommended Values

| Field | Value | Source |
|-------|-------|--------|
| company_name | YETI | — |
| year | 2025 | — |
| reportDate | 2026-01-03 | SEC (52/53-week FY ending Jan 3, 2026) |
| Net Revenue | 1,868,494 | SEC |
| Cost of Goods | 795,810 | SEC |
| Gross Margin | 1,072,684 | Calculated (1,868,494 − 795,810) |
| SGA | 859,127 | SEC (single combined line) |
| Operating Profit | 213,557 | SEC |
| Net Profit | 165,387 | SEC |
| Inventory | 290,611 | SEC |
| Current Assets | 660,326 | SEC |
| Total Assets | 1,235,418 | SEC |
| Current Liabilities | 334,339 | SEC |
| Liabilities | 585,142 | Calculated (1,235,418 − 650,276) |
| Total SE | 650,276 | SEC |
| Total L&SE | 1,235,418 | SEC |

### FY2024 Recommended Correction
Only `reportDate`: `2024-12-31` → `2024-12-28`. All other values remain unchanged.

---

## Step 7 — Readiness

**Analysis complete.** Run `/insert-financials YETI` to write the 2024 correction and 2025 new insert to SQL files.

**Unresolved flags for review before inserting:**
- [WARNING] Gross Margin above 55% specialty ceiling in FY2020, 2021, 2023, 2024, 2025 (range: 56.8–58.1%). Consistent with YETI's premium positioning — data is correct, not a data error. No action required.
- [WARNING] FY2024 reportDate correction (2024-12-31 → 2024-12-28). Minor but should be corrected for accuracy.

---

## New Company Notes for YETI

- Segment: Specialty outdoor/lifestyle (coolers, drinkware, gear)
- SGA: Single combined line — no separate marketing or ops-tech split
- Fiscal year: 52/53-week year ending last Saturday of December (may push into early January — e.g., FY2025 ended 2026-01-03)
- Gross margin: Consistently 55–58% due to premium pricing — slightly above generic specialty benchmark; treat as normal for YETI
- Inventory: Physical goods manufacturer; positive inventory expected every year
- Product recalls: In 2022–2024, product recall adjustments appear as line-item breakdowns within revenue, COGS, and SGA. The top-level totals already include recall impacts — use the total lines, not the subtotals.
