# Academy Sports (ASO) — FY2020–FY2025 Financial Analysis

**Generated:** 2026-05-29
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2020 | 2021-01-30 | No change (cannot verify — no Yahoo/SEC data) |
| 2021 | 2022-01-29 | No change (cannot verify — no Yahoo/SEC data) |
| 2022 | 2023-01-28 | No change (all fields confirmed against Yahoo) |
| 2023 | 2024-02-03 | No change (all fields confirmed against Yahoo) |
| 2024 | 2025-02-03 | No change (all fields confirmed against Yahoo) |
| 2025 | 2026-01-31 | New insert |

---

## Notes

- **US company:** CIK = 1817358. SEC MCP was unavailable this session — SEC 10-K cross-check not performed. Yahoo Finance only for FY2022–FY2025.
- **Fiscal year end:** Late January / early February each year.
- **Currency:** All values in $thousands (USD).
- **Segment:** Sporting goods specialty retail. Gross margins consistently 30–35%, below the 35–55% specialty benchmark but expected for this segment.
- **Net Revenue:** Dolt uses Yahoo "Total Revenue" (not "Operating Revenue"). Total Revenue includes gift card breakage and other non-merchandise revenue (~$34–38M above Operating Revenue each year). Confirmed against FY2022–FY2024 existing rows.
- **SGA:** Yahoo reports a single combined "Selling General And Administration" line — no sub-lines to construct or exclude.
- **FY2020/2021:** No external validation possible. Internal consistency checks pass (Gross Margin − SGA = Operating Profit, balance sheet identities hold).
- **FY2025:** New insert from Yahoo (2026-01-31). All checks pass.

---

## FY2020

**Sources:** Dolt only (no Yahoo/SEC data)

### Anomaly Detection
- `[WARNING]` Cannot verify against any external source.
- Gross margin: 1,734,045 / 5,689,233 = 30.5% — below Specialty range; expected for sporting goods.
- Internal consistency: Gross Margin − SGA = 1,734,045 − 1,313,647 = 420,398 = Operating Profit ✓
- Balance sheet: 3,272,499 + 1,111,983 = 4,384,482 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | — | 5,689,233 | 5,689,233 |
| Cost of Goods | N/A | — | 3,955,188 | 3,955,188 |
| Gross Margin | N/A | — | 1,734,045 | 1,734,045 |
| SGA | N/A | — | 1,313,647 | 1,313,647 |
| Operating Profit | N/A | — | 420,398 | 420,398 |
| Net Profit | N/A | — | 308,764 | 308,764 |
| Inventory | N/A | — | 990,034 | 990,034 |
| Current Assets | N/A | — | 1,415,020 | 1,415,020 |
| Total Assets | N/A | — | 4,384,482 | 4,384,482 |
| Current Liabilities | N/A | — | 1,167,093 | 1,167,093 |
| Liabilities | N/A | — | 3,272,499 | 3,272,499 |
| Total SE | N/A | — | 1,111,983 | 1,111,983 |
| Total L+SE | N/A | — | 4,384,482 | 4,384,482 |

**Action: No change.**

---

## FY2021

**Sources:** Dolt only (Yahoo 2022-01-31 column is NaN for all material fields)

### Anomaly Detection
- `[WARNING]` Cannot verify against any external source.
- Gross margin: 2,351,095 / 6,773,128 = 34.7% — near Specialty lower bound; expected for sporting goods.
- Internal consistency: Gross Margin − SGA = 2,351,095 − 1,443,148 = 907,947 = Operating Profit ✓
- Balance sheet: 3,117,994 + 1,466,946 = 4,584,940 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | NaN | 6,773,128 | 6,773,128 |
| Cost of Goods | N/A | NaN | 4,422,033 | 4,422,033 |
| Gross Margin | N/A | NaN | 2,351,095 | 2,351,095 |
| SGA | N/A | NaN | 1,443,148 | 1,443,148 |
| Operating Profit | N/A | NaN | 907,947 | 907,947 |
| Net Profit | N/A | NaN | 671,381 | 671,381 |
| Inventory | N/A | NaN | 1,171,808 | 1,171,808 |
| Current Assets | N/A | NaN | 1,715,747 | 1,715,747 |
| Total Assets | N/A | NaN | 4,584,940 | 4,584,940 |
| Current Liabilities | N/A | NaN | 1,127,110 | 1,127,110 |
| Liabilities | N/A | NaN | 3,117,994 | 3,117,994 |
| Total SE | N/A | NaN | 1,466,946 | 1,466,946 |
| Total L+SE | N/A | NaN | 4,584,940 | 4,584,940 |

**Action: No change.**

---

## FY2022

**Sources:** Yahoo Finance (2023-01-31 column) + Dolt

### Anomaly Detection
- All 13 fields match Yahoo (within rounding). ✓
- Gross margin: 2,212,502 / 6,395,073 = 34.6% — expected for sporting goods ✓
- Balance sheet: 2,967,133 + 1,628,306 = 4,595,439 = Total Assets ✓
- Yahoo SGA Rule 3: SGA (1,365,950K) vs Total Expenses (5,548,520K) — 24.6%. Rule 3 N/A ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | 6,395,070 | 6,395,073 | 6,395,073 |
| Cost of Goods | N/A | 4,182,570 | 4,182,571 | 4,182,571 |
| Gross Margin | N/A | 2,212,500 | 2,212,502 | 2,212,502 |
| SGA | N/A | 1,365,950 | 1,365,953 | 1,365,953 |
| Operating Profit | N/A | 846,549 | 846,549 | 846,549 |
| Net Profit | N/A | 628,001 | 628,001 | 628,001 |
| Inventory | N/A | 1,283,520 | 1,283,517 | 1,283,517 |
| Current Assets | N/A | 1,686,680 | 1,686,675 | 1,686,675 |
| Total Assets | N/A | 4,595,440 | 4,595,439 | 4,595,439 |
| Current Liabilities | N/A | 1,038,720 | 1,038,716 | 1,038,716 |
| Liabilities | N/A | 2,967,130 | 2,967,133 | 2,967,133 |
| Total SE | N/A | 1,628,310 | 1,628,306 | 1,628,306 |
| Total L+SE | N/A | 4,595,440 | 4,595,439 | 4,595,439 |

**Action: No change.**

---

## FY2023

**Sources:** Yahoo Finance (2024-01-31 column) + Dolt

### Anomaly Detection
- All 13 fields match Yahoo (within rounding). ✓
- Gross margin: 2,110,211 / 6,159,291 = 34.3% — expected for sporting goods ✓
- Balance sheet: 2,722,063 + 1,954,650 = 4,676,713 = Total Assets ✓
- Yahoo SGA Rule 3: SGA (1,432,360K) vs Total Expenses (5,481,440K) — 26.1%. Rule 3 N/A ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | 6,159,290 | 6,159,291 | 6,159,291 |
| Cost of Goods | N/A | 4,049,080 | 4,049,080 | 4,049,080 |
| Gross Margin | N/A | 2,110,210 | 2,110,211 | 2,110,211 |
| SGA | N/A | 1,432,360 | 1,432,356 | 1,432,356 |
| Operating Profit | N/A | 677,855 | 677,855 | 677,855 |
| Net Profit | N/A | 519,190 | 519,190 | 519,190 |
| Inventory | N/A | 1,194,160 | 1,194,159 | 1,194,159 |
| Current Assets | N/A | 1,644,900 | 1,644,900 | 1,644,900 |
| Total Assets | N/A | 4,676,710 | 4,676,713 | 4,676,713 |
| Current Liabilities | N/A | 879,858 | 879,858 | 879,858 |
| Liabilities | N/A | 2,722,060 | 2,722,063 | 2,722,063 |
| Total SE | N/A | 1,954,650 | 1,954,650 | 1,954,650 |
| Total L+SE | N/A | 4,676,710 | 4,676,713 | 4,676,713 |

**Action: No change.**

---

## FY2024

**Sources:** Yahoo Finance (2025-01-31 column) + Dolt

### Anomaly Detection
- All 13 fields match Yahoo (within rounding). ✓
- Gross margin: 2,011,460 / 5,933,450 = 33.9% — expected for sporting goods ✓
- Balance sheet: 2,896,928 + 2,004,035 = 4,900,963 = Total Assets ✓
- Yahoo SGA Rule 3: SGA (1,472,820K) vs Total Expenses (5,394,810K) — 27.3%. Rule 3 N/A ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | 5,933,450 | 5,933,450 | 5,933,450 |
| Cost of Goods | N/A | 3,921,990 | 3,921,990 | 3,921,990 |
| Gross Margin | N/A | 2,011,460 | 2,011,460 | 2,011,460 |
| SGA | N/A | 1,472,820 | 1,472,821 | 1,472,821 |
| Operating Profit | N/A | 538,639 | 538,639 | 538,639 |
| Net Profit | N/A | 418,447 | 418,447 | 418,447 |
| Inventory | N/A | 1,308,840 | 1,308,840 | 1,308,840 |
| Current Assets | N/A | 1,710,150 | 1,710,149 | 1,710,149 |
| Total Assets | N/A | 4,900,960 | 4,900,963 | 4,900,963 |
| Current Liabilities | N/A | 960,881 | 960,881 | 960,881 |
| Liabilities | N/A | 2,896,920 | 2,896,928 | 2,896,928 |
| Total SE | N/A | 2,004,040 | 2,004,035 | 2,004,035 |
| Total L+SE | N/A | 4,900,960 | 4,900,963 | 4,900,963 |

**Action: No change.**

---

## FY2025

**Sources:** Yahoo Finance (2026-01-31 column) only — new year not yet in Dolt

### Anomaly Detection
- Gross margin: 2,105,610 / 6,053,410 = 34.8% — expected for sporting goods ✓
- Balance sheet: 3,105,660 + 2,171,380 = 5,277,040 = Total Assets ✓
- Yahoo SGA Rule 3: SGA (1,593,430K) vs Total Expenses (5,541,230K) — 28.8%. Rule 3 N/A ✓
- Operating Income = Total Operating Income As Reported = 512,184K (no special charges FY2025) ✓
- Net Revenue uses Yahoo Total Revenue = 6,053,410K (consistent with FY2022–2024 treatment) ✓
- No minority interest — TSE = Common Stock Equity = Total Equity Gross Minority Interest ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | 6,053,410 | — | 6,053,410 |
| Cost of Goods | N/A | 3,947,800 | — | 3,947,800 |
| Gross Margin | N/A | 2,105,610 | — | 2,105,610 |
| SGA | N/A | 1,593,430 | — | 1,593,430 |
| Operating Profit | N/A | 512,184 | — | 512,184 |
| Net Profit | N/A | 376,768 | — | 376,768 |
| Inventory | N/A | 1,503,760 | — | 1,503,760 |
| Current Assets | N/A | 1,954,240 | — | 1,954,240 |
| Total Assets | N/A | 5,277,040 | — | 5,277,040 |
| Current Liabilities | N/A | 1,032,250 | — | 1,032,250 |
| Liabilities | N/A | 3,105,660 | — | 3,105,660 |
| Total SE | N/A | 2,171,380 | — | 2,171,380 |
| Total L+SE | N/A | 5,277,040 | — | 5,277,040 |

**Action: New insert.**

---

## Step 7 — Unresolved Flags

1. `[WARNING]` SEC MCP unavailable — no SEC 10-K cross-check performed for any year.
2. `[WARNING]` FY2020 and FY2021 cannot be verified against external sources.

**Analysis complete.** Run `/insert-financials ASO` to write all changed years to the database.
