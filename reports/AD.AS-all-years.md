# Ahold Delhaize (AD.AS) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-05-29
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2018-12-30 | No change (cannot verify — no Yahoo/SEC data; SGA likely incomplete: 2,139,000K) |
| 2019 | 2019-12-29 | No change (cannot verify — no Yahoo/SEC data; SGA likely incomplete: 2,210,000K) |
| 2020 | — | Missing from both Dolt and Yahoo — skipped |
| 2021 | 2021-12-31 | No change (cannot verify — Yahoo income statement NaN) |
| 2022 | 2022-12-31 | No change (all fields confirmed against Yahoo) |
| 2023 | 2023-12-31 | No change (all fields confirmed against Yahoo) |
| 2024 | 2024-12-31 | No change (all fields confirmed against Yahoo) |
| 2025 | 2025-12-31 | New insert |

---

## Notes

- **Non-US company:** CIK = NULL. Dutch grocery/retail conglomerate (Albert Heijn, Stop & Shop, Food Lion, etc.). No SEC filings. Sources: Yahoo Finance + Dolt DB only.
- **Fiscal year end:** Late December / early January each year.
- **Currency:** All values in thousands of euros (€).
- **Segment:** Grocery. Gross margins 26.5–27.4% are within Grocery benchmark (22–28%) ✓.
- **FY2020:** Missing from both Dolt and Yahoo — not analyzed.
- **SGA pattern issue (FY2018–FY2019):** Dolt SGA = 2,139,000K (2018) and 2,210,000K (2019) — far below the ~20B SGA seen in FY2022. These values likely capture G&A only. Cannot correct without external data.
- **Operating Profit:** Dolt uses Yahoo "Operating Income" (clean). "Total Operating Income As Reported" includes "Other Non-Operating Income Expenses" (a non-operating item) and is therefore not used.
- **TSE:** No minority interest for Ahold Delhaize — Common Stock Equity = Total Equity Gross Minority Interest.

---

## FY2018

**Sources:** Dolt only (no Yahoo/SEC data)

### Anomaly Detection
- `[WARNING]` Cannot verify against any external source.
- `[WARNING]` SGA = 2,139,000K likely captures G&A only. Full SGA for FY2018 likely ~14–16B.
- Gross margin: 16,953,000 / 62,791,000 = 27.0% — within Grocery range ✓
- Balance sheet: 25,625,000 + 14,205,000 = 39,830,000 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | — | 62,791,000 | 62,791,000 |
| Cost of Goods | N/A | — | 45,838,000 | 45,838,000 |
| Gross Margin | N/A | — | 16,953,000 | 16,953,000 |
| SGA | N/A | — | 2,139,000 | 2,139,000 |
| Operating Profit | N/A | — | 2,651,000 | 2,651,000 |
| Net Profit | N/A | — | 1,780,000 | 1,780,000 |
| Inventory | N/A | — | 3,196,000 | 3,196,000 |
| Current Assets | N/A | — | 8,918,000 | 8,918,000 |
| Total Assets | N/A | — | 39,830,000 | 39,830,000 |
| Current Liabilities | N/A | — | 10,943,000 | 10,943,000 |
| Liabilities | N/A | — | 25,625,000 | 25,625,000 |
| Total SE | N/A | — | 14,205,000 | 14,205,000 |
| Total L+SE | N/A | — | 39,830,000 | 39,830,000 |

**Action: No change.**

---

## FY2019

**Sources:** Dolt only (no Yahoo/SEC data)

### Anomaly Detection
- `[WARNING]` Cannot verify against any external source.
- `[WARNING]` SGA = 2,210,000K likely captures G&A only. Full SGA for FY2019 likely ~15–17B.
- Gross margin: 18,060,000 / 66,260,000 = 27.3% — within Grocery range ✓
- Balance sheet: 27,407,000 + 14,083,000 = 41,490,000 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | — | 66,260,000 | 66,260,000 |
| Cost of Goods | N/A | — | 48,200,000 | 48,200,000 |
| Gross Margin | N/A | — | 18,060,000 | 18,060,000 |
| SGA | N/A | — | 2,210,000 | 2,210,000 |
| Operating Profit | N/A | — | 2,660,000 | 2,660,000 |
| Net Profit | N/A | — | 1,766,000 | 1,766,000 |
| Inventory | N/A | — | 3,347,000 | 3,347,000 |
| Current Assets | N/A | — | 9,570,000 | 9,570,000 |
| Total Assets | N/A | — | 41,490,000 | 41,490,000 |
| Current Liabilities | N/A | — | 12,590,000 | 12,590,000 |
| Liabilities | N/A | — | 27,407,000 | 27,407,000 |
| Total SE | N/A | — | 14,083,000 | 14,083,000 |
| Total L+SE | N/A | — | 41,490,000 | 41,490,000 |

**Action: No change.**

---

## FY2021

**Sources:** Dolt only (Yahoo income statement NaN for FY2021)

### Anomaly Detection
- `[WARNING]` Cannot verify against any external source.
- Gross margin: 20,684,000 / 75,600,000 = 27.4% — within Grocery range ✓
- Balance sheet: 31,992,000 + 13,720,000 = 45,712,000 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | NaN | 75,600,000 | 75,600,000 |
| Cost of Goods | N/A | NaN | 54,916,000 | 54,916,000 |
| Gross Margin | N/A | NaN | 20,684,000 | 20,684,000 |
| SGA | N/A | NaN | 17,896,000 | 17,896,000 |
| Operating Profit | N/A | NaN | 2,789,000 | 2,789,000 |
| Net Profit | N/A | NaN | 2,246,000 | 2,246,000 |
| Inventory | N/A | NaN | 3,727,000 | 3,727,000 |
| Current Assets | N/A | NaN | 9,584,000 | 9,584,000 |
| Total Assets | N/A | NaN | 45,712,000 | 45,712,000 |
| Current Liabilities | N/A | NaN | 14,179,000 | 14,179,000 |
| Liabilities | N/A | NaN | 31,992,000 | 31,992,000 |
| Total SE | N/A | NaN | 13,720,000 | 13,720,000 |
| Total L+SE | N/A | NaN | 45,712,000 | 45,712,000 |

**Action: No change.**

---

## FY2022

**Sources:** Yahoo Finance (2022-12-31 column) + Dolt

### Anomaly Detection
- All 13 fields match Yahoo exactly. ✓
- Gross margin: 23,295,000 / 86,984,000 = 26.8% — within Grocery range ✓
- Balance sheet: 33,150,000 + 15,405,000 = 48,555,000 = Total Assets ✓
- Yahoo SGA Rule 3: SGA (20,190,000K) vs Total Expenses (83,879,000K) — 24.1%. Rule 3 N/A ✓
- Operating Profit uses Yahoo "Operating Income" (3,105,000K), not "Total Operating Income As Reported" (3,768,000K which adds other non-operating income) ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | 86,984,000 | 86,984,000 | 86,984,000 |
| Cost of Goods | N/A | 63,689,000 | 63,689,000 | 63,689,000 |
| Gross Margin | N/A | 23,295,000 | 23,295,000 | 23,295,000 |
| SGA | N/A | 20,190,000 | 20,190,000 | 20,190,000 |
| Operating Profit | N/A | 3,105,000 | 3,105,000 | 3,105,000 |
| Net Profit | N/A | 2,546,000 | 2,546,000 | 2,546,000 |
| Inventory | N/A | 4,612,000 | 4,612,000 | 4,612,000 |
| Current Assets | N/A | 10,818,000 | 10,818,000 | 10,818,000 |
| Total Assets | N/A | 48,555,000 | 48,555,000 | 48,555,000 |
| Current Liabilities | N/A | 15,082,000 | 15,082,000 | 15,082,000 |
| Liabilities | N/A | 33,150,000 | 33,150,000 | 33,150,000 |
| Total SE | N/A | 15,405,000 | 15,405,000 | 15,405,000 |
| Total L+SE | N/A | 48,555,000 | 48,555,000 | 48,555,000 |

**Action: No change.**

---

## FY2023

**Sources:** Yahoo Finance (2023-12-31 column) + Dolt

### Anomaly Detection
- All 13 fields match Yahoo exactly. ✓
- Gross margin: 23,854,000 / 88,734,000 = 26.9% — within Grocery range ✓
- Balance sheet: 33,066,000 + 14,755,000 = 47,821,000 = Total Assets ✓
- Yahoo SGA Rule 3: SGA (21,422,000K) vs Total Expenses (86,302,000K) — 24.8%. Rule 3 N/A ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | 88,734,000 | 88,734,000 | 88,734,000 |
| Cost of Goods | N/A | 64,880,000 | 64,880,000 | 64,880,000 |
| Gross Margin | N/A | 23,854,000 | 23,854,000 | 23,854,000 |
| SGA | N/A | 21,422,000 | 21,422,000 | 21,422,000 |
| Operating Profit | N/A | 2,432,000 | 2,432,000 | 2,432,000 |
| Net Profit | N/A | 1,874,000 | 1,874,000 | 1,874,000 |
| Inventory | N/A | 4,584,000 | 4,584,000 | 4,584,000 |
| Current Assets | N/A | 11,463,000 | 11,463,000 | 11,463,000 |
| Total Assets | N/A | 47,821,000 | 47,821,000 | 47,821,000 |
| Current Liabilities | N/A | 15,610,000 | 15,610,000 | 15,610,000 |
| Liabilities | N/A | 33,066,000 | 33,066,000 | 33,066,000 |
| Total SE | N/A | 14,755,000 | 14,755,000 | 14,755,000 |
| Total L+SE | N/A | 47,821,000 | 47,821,000 | 47,821,000 |

**Action: No change.**

---

## FY2024

**Sources:** Yahoo Finance (2024-12-31 column) + Dolt

### Anomaly Detection
- All 13 fields match Yahoo (within 1K rounding on Gross Margin). ✓
- Gross margin: 23,806,000 / 89,357,000 = 26.6% — within Grocery range ✓
- Balance sheet: 36,388,000 + 15,454,000 = 51,842,000 = Total Assets ✓
- Yahoo SGA Rule 3: SGA (21,453,000K) vs Total Expenses (87,004,000K) — 24.7%. Rule 3 N/A ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | 89,357,000 | 89,357,000 | 89,357,000 |
| Cost of Goods | N/A | 65,551,000 | 65,551,000 | 65,551,000 |
| Gross Margin | N/A | 23,805,000 | 23,806,000 | 23,806,000 |
| SGA | N/A | 21,453,000 | 21,453,000 | 21,453,000 |
| Operating Profit | N/A | 2,352,000 | 2,352,000 | 2,352,000 |
| Net Profit | N/A | 1,764,000 | 1,764,000 | 1,764,000 |
| Inventory | N/A | 4,796,000 | 4,796,000 | 4,796,000 |
| Current Assets | N/A | 14,526,000 | 14,526,000 | 14,526,000 |
| Total Assets | N/A | 51,842,000 | 51,842,000 | 51,842,000 |
| Current Liabilities | N/A | 17,396,000 | 17,396,000 | 17,396,000 |
| Liabilities | N/A | 36,388,000 | 36,388,000 | 36,388,000 |
| Total SE | N/A | 15,454,000 | 15,454,000 | 15,454,000 |
| Total L+SE | N/A | 51,842,000 | 51,842,000 | 51,842,000 |

**Action: No change.**

---

## FY2025

**Sources:** Yahoo Finance (2025-12-31 column) only — new year not yet in Dolt

### Anomaly Detection
- Gross margin: 24,514,000 / 92,352,000 = 26.5% — within Grocery range ✓
- Balance sheet: 34,894,000 + 14,195,000 = 49,089,000 = Total Assets ✓
- Yahoo SGA Rule 3: SGA (21,432,000K) vs Total Expenses (89,270,000K) — 24.0%. Rule 3 N/A ✓
- SGA = Selling & Marketing (17,722,000K) + G&A (3,710,000K) = 21,432,000K ✓
- Operating Profit uses Yahoo "Operating Income" = 3,082,000K (clean). "Total Operating Income As Reported" = 3,542,000K includes 460,000K of other non-operating income — excluded per pattern ✓
- No minority interest — TSE = Common Stock Equity ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | 92,352,000 | — | 92,352,000 |
| Cost of Goods | N/A | 67,838,000 | — | 67,838,000 |
| Gross Margin | N/A | 24,514,000 | — | 24,514,000 |
| SGA | N/A | 21,432,000 | — | 21,432,000 |
| Operating Profit | N/A | 3,082,000 | — | 3,082,000 |
| Net Profit | N/A | 2,264,000 | — | 2,264,000 |
| Inventory | N/A | 4,795,000 | — | 4,795,000 |
| Current Assets | N/A | 11,923,000 | — | 11,923,000 |
| Total Assets | N/A | 49,089,000 | — | 49,089,000 |
| Current Liabilities | N/A | 16,794,000 | — | 16,794,000 |
| Liabilities | N/A | 34,894,000 | — | 34,894,000 |
| Total SE | N/A | 14,195,000 | — | 14,195,000 |
| Total L+SE | N/A | 49,089,000 | — | 49,089,000 |

**Action: New insert.**

---

## Step 7 — Unresolved Flags

1. `[WARNING]` FY2018 and FY2019 SGA values are likely G&A-only (incomplete). Cannot correct without external data.
2. `[WARNING]` FY2021 cannot be verified (Yahoo NaN).
3. `[WARNING]` FY2020 is missing from both Dolt and Yahoo — no data available.

**Analysis complete.** Run `/insert-financials AD.AS` to write all changed years to the database.
