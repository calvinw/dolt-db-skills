# Amazon (AMZN) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-05-29
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2018-12-31 | No change (cannot verify — no Yahoo data) |
| 2019 | 2019-12-31 | No change (cannot verify — no Yahoo data) |
| 2020 | 2020-12-31 | Correction: Liabilities (101,408,000→227,791,000) |
| 2021 | 2021-12-31 | No change (cannot verify — no Yahoo data) |
| 2022 | 2022-12-31 | No change (SGA minor discrepancy vs Yahoo — flagged, no correction without SEC) |
| 2023 | 2023-12-31 | No change (all fields confirmed against Yahoo) |
| 2024 | 2024-12-31 | No change (all fields confirmed against Yahoo) |
| 2025 | 2025-12-31 | New insert |

---

## Notes

- **US company:** CIK = 1018724. SEC MCP unavailable this session — no SEC cross-check. Yahoo Finance only for FY2022–FY2025.
- **Fiscal year end:** December 31 (calendar year).
- **Currency:** All values in $thousands (USD).
- **Segment:** Online/Marketplace + Cloud (AWS). Gross margins 40–50% exceed the 25–35% online benchmark — AWS high-margin cloud revenue inflates blended GM%. Expected and consistent.
- **SGA:** Yahoo "Selling General And Administration" (Selling & Marketing + G&A). Technology & content, fulfillment, and other operating expenses are NOT included — per company-notes. ✓
- **FY2020 Liabilities error:** Dolt shows 101,408,000K but correct Total Liabilities = Total Assets − TSE = 321,195,000 − 93,404,000 = 227,791,000K. The Dolt value captured only non-current liabilities (Total Assets − TSE − Current Liabilities = 101,406,000K). This is a data entry error.
- **FY2022 SGA note:** Dolt has 55,392,000K vs Yahoo 54,129,000K (difference: 1,263,000K). All other fields match. Operating Profit agrees with Yahoo (12,248,000K), so the extra SGA is offset by something else. Cannot resolve without SEC data. Flagged only.
- **TSE:** Common Stock Equity = Total Equity (no minority interest for Amazon).

---

## FY2018

**Sources:** Dolt only (no Yahoo data)

### Anomaly Detection
- `[WARNING]` Cannot verify against any external source.
- Gross margin: 93,731,000 / 232,887,000 = 40.2% — above Online range; expected with AWS ✓
- Balance sheet: 119,099,000 + 43,549,000 = 162,648,000 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | — | 232,887,000 | 232,887,000 |
| Cost of Goods | N/A | — | 139,156,000 | 139,156,000 |
| Gross Margin | N/A | — | 93,731,000 | 93,731,000 |
| SGA | N/A | — | 18,150,000 | 18,150,000 |
| Operating Profit | N/A | — | 12,421,000 | 12,421,000 |
| Net Profit | N/A | — | 10,073,000 | 10,073,000 |
| Inventory | N/A | — | 17,174,000 | 17,174,000 |
| Current Assets | N/A | — | 75,101,000 | 75,101,000 |
| Total Assets | N/A | — | 162,648,000 | 162,648,000 |
| Current Liabilities | N/A | — | 68,391,000 | 68,391,000 |
| Liabilities | N/A | — | 119,099,000 | 119,099,000 |
| Total SE | N/A | — | 43,549,000 | 43,549,000 |
| Total L+SE | N/A | — | 162,648,000 | 162,648,000 |

**Action: No change.**

---

## FY2019

**Sources:** Dolt only (no Yahoo data)

### Anomaly Detection
- `[WARNING]` Cannot verify against any external source.
- Gross margin: 114,986,000 / 280,522,000 = 41.0% — above Online range; expected ✓
- Balance sheet: 163,188,000 + 62,060,000 = 225,248,000 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | — | 280,522,000 | 280,522,000 |
| Cost of Goods | N/A | — | 165,536,000 | 165,536,000 |
| Gross Margin | N/A | — | 114,986,000 | 114,986,000 |
| SGA | N/A | — | 24,290,000 | 24,290,000 |
| Operating Profit | N/A | — | 14,541,000 | 14,541,000 |
| Net Profit | N/A | — | 11,588,000 | 11,588,000 |
| Inventory | N/A | — | 20,497,000 | 20,497,000 |
| Current Assets | N/A | — | 96,334,000 | 96,334,000 |
| Total Assets | N/A | — | 225,248,000 | 225,248,000 |
| Current Liabilities | N/A | — | 87,812,000 | 87,812,000 |
| Liabilities | N/A | — | 163,188,000 | 163,188,000 |
| Total SE | N/A | — | 62,060,000 | 62,060,000 |
| Total L+SE | N/A | — | 225,248,000 | 225,248,000 |

**Action: No change.**

---

## FY2020

**Sources:** Dolt only (no Yahoo data)

### Anomaly Detection
- `[ERROR]` **Liabilities field is wrong.** Dolt shows 101,408,000K — this equals Non-current Liabilities only (Total Assets − TSE − Current Liabilities = 321,195,000 − 93,404,000 − 126,385,000 = 101,406,000K). The correct Total Liabilities = Total Assets − TSE = 321,195,000 − 93,404,000 = **227,791,000K**.
- `[WARNING]` Other fields cannot be externally verified (no Yahoo data).
- Gross margin: 152,757,000 / 386,064,000 = 39.6% — above Online range; expected ✓
- Balance sheet after correction: 227,791,000 + 93,404,000 = 321,195,000 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | — | 386,064,000 | 386,064,000 |
| Cost of Goods | N/A | — | 233,307,000 | 233,307,000 |
| Gross Margin | N/A | — | 152,757,000 | 152,757,000 |
| SGA | N/A | — | 28,676,000 | 28,676,000 |
| Operating Profit | N/A | — | 22,899,000 | 22,899,000 |
| Net Profit | N/A | — | 21,331,000 | 21,331,000 |
| Inventory | N/A | — | 23,795,000 | 23,795,000 |
| Current Assets | N/A | — | 132,733,000 | 132,733,000 |
| Total Assets | N/A | — | 321,195,000 | 321,195,000 |
| Current Liabilities | N/A | — | 126,385,000 | 126,385,000 |
| Liabilities | N/A | — | **101,408,000 \*** | **227,791,000** |
| Total SE | N/A | — | 93,404,000 | 93,404,000 |
| Total L+SE | N/A | — | 321,195,000 | 321,195,000 |

**Action: Correction: Liabilities (101,408,000→227,791,000).**

---

## FY2021

**Sources:** Dolt only (no Yahoo data)

### Anomaly Detection
- `[WARNING]` Cannot verify against any external source.
- Gross margin: 197,478,000 / 469,822,000 = 42.0% — above Online range; expected ✓
- Balance sheet: 282,304,000 + 138,245,000 = 420,549,000 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | — | 469,822,000 | 469,822,000 |
| Cost of Goods | N/A | — | 272,344,000 | 272,344,000 |
| Gross Margin | N/A | — | 197,478,000 | 197,478,000 |
| SGA | N/A | — | 41,436,000 | 41,436,000 |
| Operating Profit | N/A | — | 24,879,000 | 24,879,000 |
| Net Profit | N/A | — | 33,364,000 | 33,364,000 |
| Inventory | N/A | — | 32,640,000 | 32,640,000 |
| Current Assets | N/A | — | 161,580,000 | 161,580,000 |
| Total Assets | N/A | — | 420,549,000 | 420,549,000 |
| Current Liabilities | N/A | — | 142,266,000 | 142,266,000 |
| Liabilities | N/A | — | 282,304,000 | 282,304,000 |
| Total SE | N/A | — | 138,245,000 | 138,245,000 |
| Total L+SE | N/A | — | 420,549,000 | 420,549,000 |

**Action: No change.**

---

## FY2022

**Sources:** Yahoo Finance (2022-12-31 column) + Dolt

### Anomaly Detection
- `[WARNING]` **SGA minor discrepancy.** Dolt SGA = 55,392,000K, Yahoo SGA = 54,129,000K (Selling 42,238K + G&A 11,891K). Difference = 1,263,000K. All other fields match Yahoo exactly. Operating Profit agrees (12,248,000K). Cannot identify source of 1,263K gap without SEC data. Not correcting.
- Gross margin: 225,152,000 / 513,983,000 = 43.8% — above Online range; expected ✓
- Balance sheet: 316,632,000 + 146,043,000 = 462,675,000 = Total Assets ✓
- Yahoo SGA Rule 3: SGA (54,129,000K) vs Total Expenses (501,735,000K) — 10.8%. Rule 3 N/A ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | 513,983,000 | 513,983,000 | 513,983,000 |
| Cost of Goods | N/A | 288,831,000 | 288,831,000 | 288,831,000 |
| Gross Margin | N/A | 225,152,000 | 225,152,000 | 225,152,000 |
| SGA | N/A | 54,129,000 | **55,392,000 \*** | 55,392,000 (no change — flagged) |
| Operating Profit | N/A | 12,248,000 | 12,248,000 | 12,248,000 |
| Net Profit | N/A | -2,722,000 | -2,722,000 | -2,722,000 |
| Inventory | N/A | 34,405,000 | 34,405,000 | 34,405,000 |
| Current Assets | N/A | 146,791,000 | 146,791,000 | 146,791,000 |
| Total Assets | N/A | 462,675,000 | 462,675,000 | 462,675,000 |
| Current Liabilities | N/A | 155,393,000 | 155,393,000 | 155,393,000 |
| Liabilities | N/A | 316,632,000 | 316,632,000 | 316,632,000 |
| Total SE | N/A | 146,043,000 | 146,043,000 | 146,043,000 |
| Total L+SE | N/A | 462,675,000 | 462,675,000 | 462,675,000 |

**Action: No change (SGA discrepancy flagged for future SEC verification).**

---

## FY2023

**Sources:** Yahoo Finance (2023-12-31 column) + Dolt

### Anomaly Detection
- All 13 fields match Yahoo exactly. ✓
- Gross margin: 270,046,000 / 574,785,000 = 47.0% — above Online range; expected ✓
- Balance sheet: 325,979,000 + 201,875,000 = 527,854,000 = Total Assets ✓
- Yahoo SGA Rule 3: SGA (56,186,000K) vs Total Expenses (537,933,000K) — 10.4%. Rule 3 N/A ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | 574,785,000 | 574,785,000 | 574,785,000 |
| Cost of Goods | N/A | 304,739,000 | 304,739,000 | 304,739,000 |
| Gross Margin | N/A | 270,046,000 | 270,046,000 | 270,046,000 |
| SGA | N/A | 56,186,000 | 56,186,000 | 56,186,000 |
| Operating Profit | N/A | 36,852,000 | 36,852,000 | 36,852,000 |
| Net Profit | N/A | 30,425,000 | 30,425,000 | 30,425,000 |
| Inventory | N/A | 33,318,000 | 33,318,000 | 33,318,000 |
| Current Assets | N/A | 172,351,000 | 172,351,000 | 172,351,000 |
| Total Assets | N/A | 527,854,000 | 527,854,000 | 527,854,000 |
| Current Liabilities | N/A | 164,917,000 | 164,917,000 | 164,917,000 |
| Liabilities | N/A | 325,979,000 | 325,979,000 | 325,979,000 |
| Total SE | N/A | 201,875,000 | 201,875,000 | 201,875,000 |
| Total L+SE | N/A | 527,854,000 | 527,854,000 | 527,854,000 |

**Action: No change.**

---

## FY2024

**Sources:** Yahoo Finance (2024-12-31 column) + Dolt

### Anomaly Detection
- All 13 fields match Yahoo exactly. ✓
- Gross margin: 311,671,000 / 637,959,000 = 48.9% — above Online range; expected ✓
- Balance sheet: 338,924,000 + 285,970,000 = 624,894,000 = Total Assets ✓
- Yahoo SGA Rule 3: SGA (55,266,000K) vs Total Expenses (569,366,000K) — 9.7%. Rule 3 N/A ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | 637,959,000 | 637,959,000 | 637,959,000 |
| Cost of Goods | N/A | 326,288,000 | 326,288,000 | 326,288,000 |
| Gross Margin | N/A | 311,671,000 | 311,671,000 | 311,671,000 |
| SGA | N/A | 55,266,000 | 55,266,000 | 55,266,000 |
| Operating Profit | N/A | 68,593,000 | 68,593,000 | 68,593,000 |
| Net Profit | N/A | 59,248,000 | 59,248,000 | 59,248,000 |
| Inventory | N/A | 34,214,000 | 34,214,000 | 34,214,000 |
| Current Assets | N/A | 190,867,000 | 190,867,000 | 190,867,000 |
| Total Assets | N/A | 624,894,000 | 624,894,000 | 624,894,000 |
| Current Liabilities | N/A | 179,431,000 | 179,431,000 | 179,431,000 |
| Liabilities | N/A | 338,924,000 | 338,924,000 | 338,924,000 |
| Total SE | N/A | 285,970,000 | 285,970,000 | 285,970,000 |
| Total L+SE | N/A | 624,894,000 | 624,894,000 | 624,894,000 |

**Action: No change.**

---

## FY2025

**Sources:** Yahoo Finance (2025-12-31 column) only — new year not yet in Dolt

### Anomaly Detection
- Gross margin: 360,510,000 / 716,924,000 = 50.3% — above Online range; expected with AWS growth ✓
- Balance sheet: 406,977,000 + 411,065,000 = 818,042,000 = Total Assets ✓
- Yahoo SGA Rule 3: SGA (58,301,000K) vs Total Expenses (636,949,000K) — 9.2%. Rule 3 N/A ✓
- SGA = Selling (47,129,000K) + G&A (11,172,000K) = 58,301,000K; Technology & Content excluded ✓
- Operating Income = Total Operating Income As Reported = 79,975,000K (no special charges) ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | 716,924,000 | — | 716,924,000 |
| Cost of Goods | N/A | 356,414,000 | — | 356,414,000 |
| Gross Margin | N/A | 360,510,000 | — | 360,510,000 |
| SGA | N/A | 58,301,000 | — | 58,301,000 |
| Operating Profit | N/A | 79,975,000 | — | 79,975,000 |
| Net Profit | N/A | 77,670,000 | — | 77,670,000 |
| Inventory | N/A | 38,325,000 | — | 38,325,000 |
| Current Assets | N/A | 229,083,000 | — | 229,083,000 |
| Total Assets | N/A | 818,042,000 | — | 818,042,000 |
| Current Liabilities | N/A | 218,005,000 | — | 218,005,000 |
| Liabilities | N/A | 406,977,000 | — | 406,977,000 |
| Total SE | N/A | 411,065,000 | — | 411,065,000 |
| Total L+SE | N/A | 818,042,000 | — | 818,042,000 |

**Action: New insert.**

---

## Step 7 — Unresolved Flags

1. `[WARNING]` SEC MCP unavailable — no SEC 10-K cross-check performed.
2. `[WARNING]` FY2018, 2019, 2021 cannot be externally verified.
3. `[ERROR → RESOLVED]` FY2020 Liabilities corrected (101,408,000→227,791,000K).
4. `[WARNING]` FY2022 SGA discrepancy (Dolt 55,392K vs Yahoo 54,129K, +1,263K) — not corrected pending SEC verification.

**Analysis complete.** Run `/insert-financials AMZN` to write all changed years to the database.
