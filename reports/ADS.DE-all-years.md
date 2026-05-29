# Adidas (ADS.DE) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-05-29
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2018-12-31 | No change (cannot verify — no Yahoo/SEC data; SGA likely incomplete: only 1,576,000K) |
| 2019 | 2019-12-31 | No change (cannot verify — no Yahoo/SEC data; SGA likely incomplete: only 1,652,000K) |
| 2020 | 2020-12-31 | No change (cannot verify — no Yahoo/SEC data) |
| 2021 | 2021-12-31 | No change (cannot verify — Yahoo income statement NaN) |
| 2022 | 2022-12-31 | No change (all fields confirmed against Yahoo) |
| 2023 | 2023-12-31 | No change (all fields confirmed against Yahoo) |
| 2024 | 2024-12-31 | No change (all fields confirmed against Yahoo) |
| 2025 | 2025-12-31 | New insert |

---

## Notes

- **Non-US company:** CIK = NULL. No SEC filings. Sources: Yahoo Finance + Dolt DB only.
- **Fiscal year end:** December 31 (calendar year).
- **Currency:** All values in thousands of euros (€).
- **Segment:** Specialty — athletic/sportswear (Adidas, Reebok). Gross margins 47–52% are within Specialty benchmark (35–55%) ✓.
- **SGA pattern issue (FY2018–FY2019):** Dolt SGA = 1,576,000K (2018) and 1,652,000K (2019) — far below the ~10B SGA seen in FY2022. The FY2019 value of 1,652,000K matches Adidas's G&A-only line for FY2022 (1,651,000K) almost exactly, confirming only G&A was captured. Full SGA for those years would be ~9–10B. Cannot correct without external data.
- **Operating Profit:** Dolt uses Yahoo "Operating Income" (clean, pre-special charges). Confirmed for FY2022 (729,000K), FY2023 (279,000K), FY2024 (1,291,000K).
- **TSE:** Dolt uses Yahoo "Common Stock Equity" (excludes minority interest). Confirmed against FY2022–2024.
- **Net Profit:** Dolt uses "Net Income Common Stockholders" (excludes minority). Confirmed against FY2022–2024.

---

## FY2018

**Sources:** Dolt only (no Yahoo/SEC data)

### Anomaly Detection
- `[WARNING]` Cannot verify against any external source.
- `[WARNING]` SGA = 1,576,000K likely captures G&A only (consistent with ~1.65B G&A seen in later years). Full SGA for FY2018 likely ~9B. Cannot correct without external data.
- Gross margin: 11,363,000 / 21,915,000 = 51.9% — within Specialty range ✓
- Balance sheet: 9,248,000 + 6,364,000 = 15,612,000 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | — | 21,915,000 | 21,915,000 |
| Cost of Goods | N/A | — | 10,552,000 | 10,552,000 |
| Gross Margin | N/A | — | 11,363,000 | 11,363,000 |
| SGA | N/A | — | 1,576,000 | 1,576,000 |
| Operating Profit | N/A | — | 2,421,000 | 2,421,000 |
| Net Profit | N/A | — | 1,705,000 | 1,705,000 |
| Inventory | N/A | — | 3,445,000 | 3,445,000 |
| Current Assets | N/A | — | 9,813,000 | 9,813,000 |
| Total Assets | N/A | — | 15,612,000 | 15,612,000 |
| Current Liabilities | N/A | — | 6,834,000 | 6,834,000 |
| Liabilities | N/A | — | 9,248,000 | 9,248,000 |
| Total SE | N/A | — | 6,364,000 | 6,364,000 |
| Total L+SE | N/A | — | 15,612,000 | 15,612,000 |

**Action: No change.**

---

## FY2019

**Sources:** Dolt only (no Yahoo/SEC data)

### Anomaly Detection
- `[WARNING]` Cannot verify against any external source.
- `[WARNING]` SGA = 1,652,000K likely captures G&A only. Full SGA for FY2019 likely ~9–10B.
- Gross margin: 12,293,000 / 23,640,000 = 52.0% — within Specialty range ✓
- Balance sheet: 13,623,000 + 7,057,000 = 20,680,000 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | — | 23,640,000 | 23,640,000 |
| Cost of Goods | N/A | — | 11,347,000 | 11,347,000 |
| Gross Margin | N/A | — | 12,293,000 | 12,293,000 |
| SGA | N/A | — | 1,652,000 | 1,652,000 |
| Operating Profit | N/A | — | 2,669,000 | 2,669,000 |
| Net Profit | N/A | — | 1,978,000 | 1,978,000 |
| Inventory | N/A | — | 4,085,000 | 4,085,000 |
| Current Assets | N/A | — | 10,934,000 | 10,934,000 |
| Total Assets | N/A | — | 20,680,000 | 20,680,000 |
| Current Liabilities | N/A | — | 8,754,000 | 8,754,000 |
| Liabilities | N/A | — | 13,623,000 | 13,623,000 |
| Total SE | N/A | — | 7,057,000 | 7,057,000 |
| Total L+SE | N/A | — | 20,680,000 | 20,680,000 |

**Action: No change.**

---

## FY2020

**Sources:** Dolt only (no Yahoo/SEC data)

### Anomaly Detection
- `[WARNING]` Cannot verify against any external source.
- Gross margin: 9,222,000 / 18,435,000 = 50.0% — within Specialty range ✓
- Balance sheet: 14,599,000 + 6,454,000 = 21,053,000 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | — | 18,435,000 | 18,435,000 |
| Cost of Goods | N/A | — | 9,213,000 | 9,213,000 |
| Gross Margin | N/A | — | 9,222,000 | 9,222,000 |
| SGA | N/A | — | 8,353,000 | 8,353,000 |
| Operating Profit | N/A | — | 746,000 | 746,000 |
| Net Profit | N/A | — | 432,000 | 432,000 |
| Inventory | N/A | — | 4,397,000 | 4,397,000 |
| Current Assets | N/A | — | 12,154,000 | 12,154,000 |
| Total Assets | N/A | — | 21,053,000 | 21,053,000 |
| Current Liabilities | N/A | — | 8,827,000 | 8,827,000 |
| Liabilities | N/A | — | 14,599,000 | 14,599,000 |
| Total SE | N/A | — | 6,454,000 | 6,454,000 |
| Total L+SE | N/A | — | 21,053,000 | 21,053,000 |

**Action: No change.**

---

## FY2021

**Sources:** Dolt only (Yahoo 2021-12-31 balance sheet data is NaN; income statement not available)

### Anomaly Detection
- `[WARNING]` Cannot verify against any external source.
- Gross margin: 10,765,000 / 21,234,000 = 50.7% — within Specialty range ✓
- Balance sheet: 14,618,000 + 7,519,000 = 22,137,000 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | NaN | 21,234,000 | 21,234,000 |
| Cost of Goods | N/A | NaN | 10,469,000 | 10,469,000 |
| Gross Margin | N/A | NaN | 10,765,000 | 10,765,000 |
| SGA | N/A | NaN | 8,810,000 | 8,810,000 |
| Operating Profit | N/A | NaN | 1,989,000 | 1,989,000 |
| Net Profit | N/A | NaN | 2,116,000 | 2,116,000 |
| Inventory | N/A | NaN | 4,009,000 | 4,009,000 |
| Current Assets | N/A | NaN | 13,944,000 | 13,944,000 |
| Total Assets | N/A | NaN | 22,137,000 | 22,137,000 |
| Current Liabilities | N/A | NaN | 8,965,000 | 8,965,000 |
| Liabilities | N/A | NaN | 14,618,000 | 14,618,000 |
| Total SE | N/A | NaN | 7,519,000 | 7,519,000 |
| Total L+SE | N/A | NaN | 22,137,000 | 22,137,000 |

**Action: No change.**

---

## FY2022

**Sources:** Yahoo Finance (2022-12-31 column) + Dolt

### Anomaly Detection
- All 13 fields match Yahoo exactly. ✓
- Gross margin: 10,644,000 / 22,511,000 = 47.3% — within Specialty range ✓
- Balance sheet: 15,305,000 + 4,991,000 = 20,296,000 = Total Assets ✓
- Yahoo SGA Rule 3: SGA (10,015,000K) vs Total Expenses (21,782,000K) — 46.0%. Rule 3 N/A ✓
- Operating Profit uses Yahoo "Operating Income" (729,000K), not "Total Operating Income As Reported" (669,000K which includes -60,000K special charges) ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | 22,511,000 | 22,511,000 | 22,511,000 |
| Cost of Goods | N/A | 11,867,000 | 11,867,000 | 11,867,000 |
| Gross Margin | N/A | 10,644,000 | 10,644,000 | 10,644,000 |
| SGA | N/A | 10,015,000 | 10,015,000 | 10,015,000 |
| Operating Profit | N/A | 729,000 | 729,000 | 729,000 |
| Net Profit | N/A | 612,000 | 612,000 | 612,000 |
| Inventory | N/A | 5,973,000 | 5,973,000 | 5,973,000 |
| Current Assets | N/A | 11,732,000 | 11,732,000 | 11,732,000 |
| Total Assets | N/A | 20,296,000 | 20,296,000 | 20,296,000 |
| Current Liabilities | N/A | 9,257,000 | 9,257,000 | 9,257,000 |
| Liabilities | N/A | 15,305,000 | 15,305,000 | 15,305,000 |
| Total SE | N/A | 4,991,000 | 4,991,000 | 4,991,000 |
| Total L+SE | N/A | 20,296,000 | 20,296,000 | 20,296,000 |

**Action: No change.**

---

## FY2023

**Sources:** Yahoo Finance (2023-12-31 column) + Dolt

### Anomaly Detection
- All 13 fields match Yahoo exactly. ✓
- Gross margin: 10,183,000 / 21,427,000 = 47.5% — within Specialty range ✓
- Balance sheet: 13,440,000 + 4,580,000 = 18,020,000 = Total Assets ✓
- Yahoo SGA Rule 3: SGA (9,914,000K) vs Total Expenses (21,148,000K) — 46.9%. Rule 3 N/A ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | 21,427,000 | 21,427,000 | 21,427,000 |
| Cost of Goods | N/A | 11,244,000 | 11,244,000 | 11,244,000 |
| Gross Margin | N/A | 10,183,000 | 10,183,000 | 10,183,000 |
| SGA | N/A | 9,914,000 | 9,914,000 | 9,914,000 |
| Operating Profit | N/A | 279,000 | 279,000 | 279,000 |
| Net Profit | N/A | -75,000 | -75,000 | -75,000 |
| Inventory | N/A | 4,525,000 | 4,525,000 | 4,525,000 |
| Current Assets | N/A | 9,809,000 | 9,809,000 | 9,809,000 |
| Total Assets | N/A | 18,020,000 | 18,020,000 | 18,020,000 |
| Current Liabilities | N/A | 8,043,000 | 8,043,000 | 8,043,000 |
| Liabilities | N/A | 13,440,000 | 13,440,000 | 13,440,000 |
| Total SE | N/A | 4,580,000 | 4,580,000 | 4,580,000 |
| Total L+SE | N/A | 18,020,000 | 18,020,000 | 18,020,000 |

**Action: No change.**

---

## FY2024

**Sources:** Yahoo Finance (2024-12-31 column) + Dolt

### Anomaly Detection
- All 13 fields match Yahoo exactly. ✓
- Gross margin: 12,025,000 / 23,683,000 = 50.8% — within Specialty range ✓
- Balance sheet: 15,179,000 + 5,476,000 = 20,655,000 = Total Assets ✓
- Yahoo SGA Rule 3: SGA (10,915,000K) vs Total Expenses (22,392,000K) — 48.7%. Rule 3 N/A ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | 23,683,000 | 23,683,000 | 23,683,000 |
| Cost of Goods | N/A | 11,658,000 | 11,658,000 | 11,658,000 |
| Gross Margin | N/A | 12,025,000 | 12,025,000 | 12,025,000 |
| SGA | N/A | 10,915,000 | 10,915,000 | 10,915,000 |
| Operating Profit | N/A | 1,291,000 | 1,291,000 | 1,291,000 |
| Net Profit | N/A | 764,000 | 764,000 | 764,000 |
| Inventory | N/A | 4,989,000 | 4,989,000 | 4,989,000 |
| Current Assets | N/A | 11,904,000 | 11,904,000 | 11,904,000 |
| Total Assets | N/A | 20,655,000 | 20,655,000 | 20,655,000 |
| Current Liabilities | N/A | 9,593,000 | 9,593,000 | 9,593,000 |
| Liabilities | N/A | 15,179,000 | 15,179,000 | 15,179,000 |
| Total SE | N/A | 5,476,000 | 5,476,000 | 5,476,000 |
| Total L+SE | N/A | 20,655,000 | 20,655,000 | 20,655,000 |

**Action: No change.**

---

## FY2025

**Sources:** Yahoo Finance (2025-12-31 column) only — new year not yet in Dolt

### Anomaly Detection
- Gross margin: 12,805,000 / 24,811,000 = 51.6% — within Specialty range ✓
- Balance sheet: 14,486,000 + 5,776,000 = 20,262,000 = Total Assets ✓
- Yahoo SGA Rule 3: SGA (10,841,000K) vs Total Expenses (22,750,000K) — 47.6%. Rule 3 N/A ✓
- SGA = Selling & Marketing (8,956,000K) + G&A (1,885,000K) = 10,841,000K ✓
- Operating Profit uses Yahoo "Operating Income" = 2,061,000K (clean, pre-special charges of -5,000K) ✓
- Net Profit uses Net Income Common Stockholders = 1,340,000K (excludes minority interest 45,000K) ✓
- TSE uses Common Stock Equity = 5,776,000K (excludes minority interest 349,000K) ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | 24,811,000 | — | 24,811,000 |
| Cost of Goods | N/A | 12,006,000 | — | 12,006,000 |
| Gross Margin | N/A | 12,805,000 | — | 12,805,000 |
| SGA | N/A | 10,841,000 | — | 10,841,000 |
| Operating Profit | N/A | 2,061,000 | — | 2,061,000 |
| Net Profit | N/A | 1,340,000 | — | 1,340,000 |
| Inventory | N/A | 5,832,000 | — | 5,832,000 |
| Current Assets | N/A | 11,977,000 | — | 11,977,000 |
| Total Assets | N/A | 20,262,000 | — | 20,262,000 |
| Current Liabilities | N/A | 9,094,000 | — | 9,094,000 |
| Liabilities | N/A | 14,486,000 | — | 14,486,000 |
| Total SE | N/A | 5,776,000 | — | 5,776,000 |
| Total L+SE | N/A | 20,262,000 | — | 20,262,000 |

**Action: New insert.**

---

## Step 7 — Unresolved Flags

1. `[WARNING]` FY2018 and FY2019 SGA values are likely G&A-only (incomplete). Cannot correct without external data for those years.
2. `[WARNING]` FY2020 and FY2021 cannot be verified against external sources.

**Analysis complete.** Run `/insert-financials ADS.DE` to write all changed years to the database.
