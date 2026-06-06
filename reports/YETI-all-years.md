# YETI (YETI) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-06
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2018-12-29 | No change |
| 2019 | 2019-12-28 | No change |
| 2020 | 2021-01-02 | No change |
| 2021 | 2022-01-01 | No change |
| 2022 | 2022-12-31 | No change |
| 2023 | 2023-12-30 | No change |
| 2024 | 2024-12-28 | Correction: reportDate |
| 2025 | 2026-01-03 | New insert |

## FY2018–FY2023

All values match perfectly between SEC and Dolt. No changes needed.

| Field | 2018 SEC | 2018 Dolt | 2019 SEC | 2019 Dolt | 2020 SEC | 2020 Dolt | 2021 SEC | 2021 Dolt | 2022 SEC | 2022 Dolt | 2023 SEC | 2023 Dolt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reportDate | 2018-12-29 | 2018-12-29 | 2019-12-28 | 2019-12-28 | 2021-01-02 | 2021-01-02 | 2022-01-01 | 2022-01-01 | 2022-12-31 | 2022-12-31 | 2023-12-30 | 2023-12-30 |
| Net Revenue | 778,833 | 778,833 | 913,734 | 913,734 | 1,091,721 | 1,091,721 | 1,410,989 | 1,410,989 | 1,595,222 | 1,595,222 | 1,658,713 | 1,658,713 |
| Cost of Goods | 395,705 | 395,705 | 438,420 | 438,420 | 462,918 | 462,918 | 594,876 | 594,876 | 831,821 | 831,821 | 715,527 | 715,527 |
| Gross Margin | 383,128 | 383,128 | 475,314 | 475,314 | 628,803 | 628,803 | 816,113 | 816,113 | 763,401 | 763,401 | 943,186 | 943,186 |
| SGA | 280,972 | 280,972 | 385,543 | 385,543 | 414,570 | 414,570 | 541,175 | 541,175 | 637,040 | 637,040 | 717,728 | 717,728 |
| Operating Profit | 102,156 | 102,156 | 89,771 | 89,771 | 214,233 | 214,233 | 274,938 | 274,938 | 126,361 | 126,361 | 225,458 | 225,458 |
| Net Profit | 57,763 | 57,763 | 50,434 | 50,434 | 155,801 | 155,801 | 212,602 | 212,602 | 89,693 | 89,693 | 169,885 | 169,885 |
| Inventory | 145,423 | 145,423 | 185,700 | 185,700 | 140,111 | 140,111 | 318,864 | 318,864 | 371,412 | 371,412 | 337,208 | 337,208 |
| Current Assets | 297,013 | 297,013 | 360,547 | 360,547 | 476,497 | 476,497 | 770,167 | 770,167 | 718,920 | 718,920 | 914,405 | 914,405 |
| Total Assets | 514,213 | 514,213 | 629,539 | 629,539 | 737,067 | 737,067 | 1,096,364 | 1,096,364 | 1,076,765 | 1,076,765 | 1,297,192 | 1,297,192 |
| Current Liabilities | 187,338 | 187,338 | 170,312 | 170,312 | 287,759 | 287,759 | 403,713 | 403,713 | 409,040 | 409,040 | 398,353 | 398,353 |
| Liabilities | 485,242 | 485,242 | 507,534 | 507,534 | 448,649 | 448,649 | 578,541 | 578,541 | 550,288 | 550,288 | 573,582 | 573,582 |
| Total SE | 28,971 | 28,971 | 122,005 | 122,005 | 288,418 | 288,418 | 517,823 | 517,823 | 526,477 | 526,477 | 723,610 | 723,610 |
| Total L&SE | 514,213 | 514,213 | 629,539 | 629,539 | 737,067 | 737,067 | 1,096,364 | 1,096,364 | 1,076,765 | 1,076,765 | 1,297,192 | 1,297,192 |

## FY2024 — ReportDate Correction

Dolt has `2024-12-31` but SEC fiscal year actually ended **2024-12-28** (52/53-week calendar, last Saturday of December). All financial values are identical between SEC and Dolt.

| Field | SEC | Dolt | Recommended |
|-------|-----|------|-------------|
| reportDate | 2024-12-28 | 2024-12-31 * | 2024-12-28 |
| Net Revenue | 1,829,873 | 1,829,873 | 1,829,873 |
| Cost of Goods | 766,589 | 766,589 | 766,589 |
| Gross Margin | 1,063,284 | 1,063,284 | 1,063,284 |
| SGA | 817,908 | 817,908 | 817,908 |
| Operating Profit | 245,376 | 245,376 | 245,376 |
| Net Profit | 175,689 | 175,689 | 175,689 |
| Inventory | 310,058 | 310,058 | 310,058 |
| Current Assets | 826,766 | 826,766 | 826,766 |
| Total Assets | 1,286,120 | 1,286,120 | 1,286,120 |
| Current Liabilities | 379,504 | 379,504 | 379,504 |
| Liabilities | 546,013 | 546,013 | 546,013 |
| Total SE | 740,107 | 740,107 | 740,107 |
| Total L&SE | 1,286,120 | 1,286,120 | 1,286,120 |

Yahoo confirms all financial values (rounding ≤5K).

## FY2025 — New Insert

Not yet in Dolt. SEC and Yahoo agree on all values (Yahoo rounding ≤4K).

| Field | SEC | Yahoo | Recommended |
|-------|-----|-------|-------------|
| reportDate | 2026-01-03 | 2025-12-31 | **2026-01-03** (SEC) |
| Net Revenue | 1,868,494 | 1,868,490 | 1,868,494 |
| Cost of Goods | 795,810 | 795,810 | 795,810 |
| Gross Margin | 1,072,684 | 1,072,680 | 1,072,684 |
| SGA | 859,127 | 859,127 | 859,127 |
| Operating Profit | 213,557 | 213,557 | 213,557 |
| Net Profit | 165,387 | 165,387 | 165,387 |
| Inventory | 290,611 | 290,611 | 290,611 |
| Current Assets | 660,326 | 660,326 | 660,326 |
| Total Assets | 1,235,418 | 1,235,420 | 1,235,418 |
| Current Liabilities | 334,339 | 334,339 | 334,339 |
| Liabilities | 585,142 | — | 585,142 |
| Total SE | 650,276 | 650,276 | 650,276 |
| Total L&SE | 1,235,418 | 1,235,420 | 1,235,418 |

## Anomaly Detection

### SGA Rules
- Rule 1: No separate marketing line — combined SGA ✓
- Rule 2: Not a marketplace company ✓
- Rule 3: Yahoo SGA ≠ Total OpEx (52% max) ✓
- Rule 4: Combined SGA tag exists ✓

### Balance Sheet Identity
All years pass (Total Assets = Total L&SE, diff = 0).

### Gross Margin Sanity Check (Specialty: 35–55%)
| Year | GM% | Flag |
|------|-----|------|
| 2018 | 49.2% | ✓ |
| 2019 | 52.0% | ✓ |
| 2020 | 57.6% | ⚠ Above range |
| 2021 | 57.8% | ⚠ Above range |
| 2022 | 47.9% | ✓ (recall impact) |
| 2023 | 56.8% | ⚠ Above range |
| 2024 | 58.1% | ⚠ Above range |
| 2025 | 57.4% | ⚠ Above range |

Consistent with YETI's premium brand positioning — not a data error.

### Inventory
Positive values all years — physical goods manufacturer, as expected.

## Summary of Changes

| Year | Action | Details |
|------|--------|---------|
| 2018 | No change | — |
| 2019 | No change | — |
| 2020 | No change | — |
| 2021 | No change | — |
| 2022 | No change | — |
| 2023 | No change | — |
| 2024 | Correction: reportDate | `2024-12-31` → `2024-12-28` |
| 2025 | New insert | Full 13-field row from SEC 10-K |

---

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql YETI` to write these changes to SQL files.

**Flags for review:**
- [WARNING] Gross margin 56–58% above specialty benchmark (35–55%) — consistent with YETI's premium positioning, data is correct
- [WARNING] FY2024 reportDate correction (2024-12-31 → 2024-12-28) — minor but improves accuracy
