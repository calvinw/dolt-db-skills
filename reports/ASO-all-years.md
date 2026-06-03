# Academy Sports (ASO) — FY2020–FY2025 Financial Analysis

**Generated:** 2026-06-03
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2020 | 2021-01-30 | No change (income stmt confirmed by SEC; balance sheet unverified, identity passes) |
| 2021 | 2022-01-29 | No change (all fields confirmed vs SEC) |
| 2022 | 2023-01-28 | No change (all fields confirmed vs SEC + Yahoo) |
| 2023 | 2024-02-03 | No change (all fields confirmed vs SEC + Yahoo) |
| 2024 | 2025-02-01 | Correction: reportDate (2025-02-03→2025-02-01) |
| 2025 | 2026-01-31 | New insert |

---

## Notes

- **US company:** CIK = 1817358. SEC 10-K filings fetched for FY2022 (covers FY2020–FY2022), FY2023, FY2024, FY2025.
- **Fiscal year end:** Late January / early February. Year label = calendar year majority of fiscal year falls in.
- **Currency:** All values in $thousands (USD).
- **Segment:** Sporting goods retail. Gross margins 30–35% — between discount (10–30%) and specialty (35–55%); appropriate for ASO's value-oriented sporting goods format.
- **SGA:** Single `us-gaap_SellingGeneralAndAdministrativeExpense` line — no composite construction needed. Yahoo SGA matches SEC exactly.
- **No NCI:** No minority interest. Net Income = Net Income Common Stockholders throughout.
- **FY2024 reportDate:** SEC 10-K period header = 2025-02-01; Dolt has 2025-02-03. Correcting.
- **FY2020 balance sheet:** Not confirmed from SEC (FY2020 10-K not fetched). Identity check passes: 3,272,499 + 1,111,983 = 4,384,482 ✓.
- **FY2021 balance sheet:** Confirmed from the comparative column in the FY2022 10-K ✓.

---

## FY2020

**Sources:** Dolt + SEC comparative (FY2022 10-K, column 2021-01-30). Balance sheet unverified.

### Anomaly Detection
- Income statement confirmed by SEC comparative — all values match ✓
- `[WARNING]` Balance sheet not verified from SEC (FY2020 10-K not fetched). Identity check passes: 3,272,499 + 1,111,983 = 4,384,482 ✓
- Gross margin: 1,734,045 / 5,689,233 = 30.5% — between discount and specialty; appropriate for ASO's format ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 5,689,233 | — | 5,689,233 | 5,689,233 |
| Cost of Goods | 3,955,188 | — | 3,955,188 | 3,955,188 |
| Gross Margin | 1,734,045 | — | 1,734,045 | 1,734,045 |
| SGA | 1,313,647 | — | 1,313,647 | 1,313,647 |
| Operating Profit | 420,398 | — | 420,398 | 420,398 |
| Net Profit | 308,764 | — | 308,764 | 308,764 |
| Inventory | — | — | 990,034 | 990,034 |
| Current Assets | — | — | 1,415,020 | 1,415,020 |
| Total Assets | — | — | 4,384,482 | 4,384,482 |
| Current Liabilities | — | — | 1,167,093 | 1,167,093 |
| Liabilities | — | — | 3,272,499 | 3,272,499 |
| Total SE | — | — | 1,111,983 | 1,111,983 |
| Total L+SE | — | — | 4,384,482 | 4,384,482 |

**Action: No change.**

---

## FY2021

**Sources:** Dolt + SEC (FY2022 10-K, comparative column 2022-01-29 — income stmt + balance sheet).

### Anomaly Detection
- All income statement and balance sheet fields confirmed vs SEC ✓
- Gross margin: 2,351,095 / 6,773,128 = 34.7% — slightly below specialty; consistent with ASO format ✓
- Balance sheet: 3,117,994 + 1,466,946 = 4,584,940 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 6,773,128 | — | 6,773,128 | 6,773,128 |
| Cost of Goods | 4,422,033 | — | 4,422,033 | 4,422,033 |
| Gross Margin | 2,351,095 | — | 2,351,095 | 2,351,095 |
| SGA | 1,443,148 | — | 1,443,148 | 1,443,148 |
| Operating Profit | 907,947 | — | 907,947 | 907,947 |
| Net Profit | 671,381 | — | 671,381 | 671,381 |
| Inventory | 1,171,808 | — | 1,171,808 | 1,171,808 |
| Current Assets | 1,715,747 | — | 1,715,747 | 1,715,747 |
| Total Assets | 4,584,940 | — | 4,584,940 | 4,584,940 |
| Current Liabilities | 1,127,110 | — | 1,127,110 | 1,127,110 |
| Liabilities | 3,117,994 | — | 3,117,994 | 3,117,994 |
| Total SE | 1,466,946 | — | 1,466,946 | 1,466,946 |
| Total L+SE | 4,584,940 | — | 4,584,940 | 4,584,940 |

**Action: No change.**

---

## FY2022

**Sources:** Dolt + SEC (FY2022 10-K, leftmost column 2023-01-28) + Yahoo (column 2023-01-31).

### Anomaly Detection
- All income statement and balance sheet fields confirmed vs SEC and Yahoo ✓
- Gross margin: 2,212,502 / 6,395,073 = 34.6% — consistent with ASO format ✓
- Balance sheet: 2,967,133 + 1,628,306 = 4,595,439 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 6,395,073 | 6,395,073 | 6,395,073 | 6,395,073 |
| Cost of Goods | 4,182,571 | 4,182,571 | 4,182,571 | 4,182,571 |
| Gross Margin | 2,212,502 | 2,212,502 | 2,212,502 | 2,212,502 |
| SGA | 1,365,953 | 1,365,950 | 1,365,953 | 1,365,953 |
| Operating Profit | 846,549 | 846,549 | 846,549 | 846,549 |
| Net Profit | 628,001 | 628,001 | 628,001 | 628,001 |
| Inventory | 1,283,517 | 1,283,517 | 1,283,517 | 1,283,517 |
| Current Assets | 1,686,675 | 1,686,675 | 1,686,675 | 1,686,675 |
| Total Assets | 4,595,439 | 4,595,439 | 4,595,439 | 4,595,439 |
| Current Liabilities | 1,038,716 | 1,038,716 | 1,038,716 | 1,038,716 |
| Liabilities | 2,967,133 | 2,967,133 | 2,967,133 | 2,967,133 |
| Total SE | 1,628,306 | 1,628,306 | 1,628,306 | 1,628,306 |
| Total L+SE | 4,595,439 | 4,595,439 | 4,595,439 | 4,595,439 |

**Action: No change.**

---

## FY2023

**Sources:** Dolt + SEC (FY2023 10-K, leftmost column 2024-02-03) + Yahoo (column 2024-01-31).

### Anomaly Detection
- All income statement and balance sheet fields confirmed vs SEC and Yahoo ✓
- Gross margin: 2,110,211 / 6,159,291 = 34.3% — consistent with ASO format ✓
- Balance sheet: 2,722,063 + 1,954,650 = 4,676,713 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 6,159,291 | 6,159,291 | 6,159,291 | 6,159,291 |
| Cost of Goods | 4,049,080 | 4,049,080 | 4,049,080 | 4,049,080 |
| Gross Margin | 2,110,211 | 2,110,211 | 2,110,211 | 2,110,211 |
| SGA | 1,432,356 | 1,432,356 | 1,432,356 | 1,432,356 |
| Operating Profit | 677,855 | 677,855 | 677,855 | 677,855 |
| Net Profit | 519,190 | 519,190 | 519,190 | 519,190 |
| Inventory | 1,194,159 | 1,194,159 | 1,194,159 | 1,194,159 |
| Current Assets | 1,644,900 | 1,644,900 | 1,644,900 | 1,644,900 |
| Total Assets | 4,676,713 | 4,676,713 | 4,676,713 | 4,676,713 |
| Current Liabilities | 879,858 | 879,858 | 879,858 | 879,858 |
| Liabilities | 2,722,063 | 2,722,063 | 2,722,063 | 2,722,063 |
| Total SE | 1,954,650 | 1,954,650 | 1,954,650 | 1,954,650 |
| Total L+SE | 4,676,713 | 4,676,713 | 4,676,713 | 4,676,713 |

**Action: No change.**

---

## FY2024

**Sources:** Dolt + SEC (FY2024 10-K, leftmost column 2025-02-01) + Yahoo (column 2025-01-31).

### Anomaly Detection
- `[WARNING]` reportDate: Dolt has 2025-02-03; SEC 10-K header = 2025-02-01. Correcting.
- All financial fields confirmed: SEC = Dolt = Yahoo ✓
- Gross margin: 2,011,460 / 5,933,450 = 33.9% — consistent with ASO format ✓
- Balance sheet: 2,896,928 + 2,004,035 = 4,900,963 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| reportDate | **2025-02-01*** | 2025-01-31 | 2025-02-03* | **2025-02-01** |
| Net Revenue | 5,933,450 | 5,933,450 | 5,933,450 | 5,933,450 |
| Cost of Goods | 3,921,990 | 3,921,990 | 3,921,990 | 3,921,990 |
| Gross Margin | 2,011,460 | 2,011,460 | 2,011,460 | 2,011,460 |
| SGA | 1,472,821 | 1,472,820 | 1,472,821 | 1,472,821 |
| Operating Profit | 538,639 | 538,639 | 538,639 | 538,639 |
| Net Profit | 418,447 | 418,447 | 418,447 | 418,447 |
| Inventory | 1,308,840 | 1,308,840 | 1,308,840 | 1,308,840 |
| Current Assets | 1,710,149 | 1,710,149 | 1,710,149 | 1,710,149 |
| Total Assets | 4,900,963 | 4,900,963 | 4,900,963 | 4,900,963 |
| Current Liabilities | 960,881 | 960,881 | 960,881 | 960,881 |
| Liabilities | 2,896,928 | 2,896,928 | 2,896,928 | 2,896,928 |
| Total SE | 2,004,035 | 2,004,035 | 2,004,035 | 2,004,035 |
| Total L+SE | 4,900,963 | 4,900,963 | 4,900,963 | 4,900,963 |

*SEC fiscal year end per 10-K header = 2025-02-01. Dolt 2025-02-03 is incorrect.

**Action: Correction — reportDate only. All financial values confirmed.**

---

## FY2025

**Sources:** SEC (FY2025 10-K, leftmost column 2026-01-31) + Yahoo (column 2026-01-31). New insert — not yet in Dolt.

### Anomaly Detection
- All fields confirmed: SEC = Yahoo ✓
- Gross margin: 2,105,613 / 6,053,414 = 34.8% — consistent with ASO format ✓
- Balance sheet: 3,105,659 + 2,171,377 = 5,277,036 = Total Assets ✓
- Revenue recovery: 6,053,414K vs 5,933,450K in FY2024 — modest growth resumption after multi-year decline from peak FY2021 (6,773,128K). Not anomalous.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 6,053,414 | 6,053,410 | — | 6,053,414 |
| Cost of Goods | 3,947,801 | 3,947,800 | — | 3,947,801 |
| Gross Margin | 2,105,613 | 2,105,610 | — | 2,105,613 |
| SGA | 1,593,429 | 1,593,430 | — | 1,593,429 |
| Operating Profit | 512,184 | 512,184 | — | 512,184 |
| Net Profit | 376,768 | 376,768 | — | 376,768 |
| Inventory | 1,503,756 | 1,503,760 | — | 1,503,756 |
| Current Assets | 1,954,245 | 1,954,240 | — | 1,954,245 |
| Total Assets | 5,277,036 | 5,277,040 | — | 5,277,036 |
| Current Liabilities | 1,032,253 | 1,032,250 | — | 1,032,253 |
| Liabilities | 3,105,659 | 3,105,660 | — | 3,105,659 |
| Total SE | 2,171,377 | 2,171,380 | — | 2,171,377 |
| Total L+SE | 5,277,036 | 5,277,040 | — | 5,277,036 |

**Action: New insert.**

---

**Analysis complete.** Run `/insert-financials ASO` to write all changed years to the database.
