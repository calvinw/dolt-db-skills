# Amazon (AMZN) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-03
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2018-12-31 | No change (unverified — no SEC fetch for this year; balance sheet identity passes) |
| 2019 | 2019-12-31 | No change (unverified — no SEC fetch for this year; balance sheet identity passes) |
| 2020 | 2020-12-31 | Correction: Liabilities (101,408,000→227,791,000) |
| 2021 | 2021-12-31 | Correction: SGA (41,436,000→41,374,000) |
| 2022 | 2022-12-31 | Correction: SGA (55,392,000→54,129,000) |
| 2023 | 2023-12-31 | No change (all fields confirmed vs SEC + Yahoo) |
| 2024 | 2024-12-31 | No change (all fields confirmed vs SEC + Yahoo) |
| 2025 | 2025-12-31 | New insert |

---

## Notes

- **US company:** CIK = 1018724. SEC 10-K filings fetched for FY2022 (covers FY2020–FY2022), FY2023, FY2024, FY2025.
- **Fiscal year end:** December 31 (calendar year).
- **Currency:** All values in $thousands (USD). Note: Amazon's figures are very large (hundreds of billions). All Dolt values correctly stored in thousands.
- **Segment:** Online/marketplace + AWS + advertising. Gross margin rising rapidly (FY2022: 43.8% → FY2025: 50.3%) due to AWS and advertising growth. The 25–35% Online benchmark does not apply to Amazon's mixed business model.
- **SGA construction (critical):** Amazon does NOT have a labeled "SGA" line in its SEC filing. Operating expenses are split into: COGS, Fulfillment, Technology and Infrastructure, Marketing, G&A, Other. Per company-notes, Technology and Infrastructure is a product/platform cost — EXCLUDE from SGA. Correct SGA = Marketing + G&A only. Fulfillment is also excluded (analogous to COGS for a logistics company). "Other operating expense/income" is excluded (restructuring-type charges per anomaly rules).
- **SGA inconsistency fixed:** Dolt FY2021 and FY2022 incorrectly included "Other operating expense" in SGA (62,000K and 1,263,000K respectively). FY2020, FY2023, FY2024 correctly excluded it. Correcting FY2021 and FY2022.
- **FY2020 Liabilities error:** Dolt has 101,408,000K which is LESS than Current Liabilities (126,385,000K) — impossible. Correct value = Total Assets − Total SE = 321,195,000 − 93,404,000 = 227,791,000K.
- **No NCI:** No minority interest throughout all years.
- **FY2018–FY2019:** Not verified from SEC (older 10-Ks not fetched). Balance sheet identities pass for both years.

---

## FY2018

**Sources:** Dolt only (no SEC/Yahoo for this year).

### Anomaly Detection
- `[WARNING]` Cannot verify from SEC or Yahoo.
- Gross margin: 93,731,000 / 232,887,000 = 40.2% — above Online benchmark (25–35%); consistent with Amazon's mixed model including AWS/advertising.
- Balance sheet: 119,099,000 + 43,549,000 = 162,648,000 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | — | 232,887,000 | 232,887,000 |
| Cost of Goods | — | — | 139,156,000 | 139,156,000 |
| Gross Margin | — | — | 93,731,000 | 93,731,000 |
| SGA | — | — | 18,150,000 | 18,150,000 |
| Operating Profit | — | — | 12,421,000 | 12,421,000 |
| Net Profit | — | — | 10,073,000 | 10,073,000 |
| Inventory | — | — | 17,174,000 | 17,174,000 |
| Current Assets | — | — | 75,101,000 | 75,101,000 |
| Total Assets | — | — | 162,648,000 | 162,648,000 |
| Current Liabilities | — | — | 68,391,000 | 68,391,000 |
| Liabilities | — | — | 119,099,000 | 119,099,000 |
| Total SE | — | — | 43,549,000 | 43,549,000 |
| Total L+SE | — | — | 162,648,000 | 162,648,000 |

**Action: No change.**

---

## FY2019

**Sources:** Dolt only (no SEC/Yahoo for this year).

### Anomaly Detection
- `[WARNING]` Cannot verify from SEC or Yahoo.
- Gross margin: 114,986,000 / 280,522,000 = 41.0% — above Online benchmark; consistent with Amazon's model.
- Balance sheet: 163,188,000 + 62,060,000 = 225,248,000 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | — | 280,522,000 | 280,522,000 |
| Cost of Goods | — | — | 165,536,000 | 165,536,000 |
| Gross Margin | — | — | 114,986,000 | 114,986,000 |
| SGA | — | — | 24,290,000 | 24,290,000 |
| Operating Profit | — | — | 14,541,000 | 14,541,000 |
| Net Profit | — | — | 11,588,000 | 11,588,000 |
| Inventory | — | — | 20,497,000 | 20,497,000 |
| Current Assets | — | — | 96,334,000 | 96,334,000 |
| Total Assets | — | — | 225,248,000 | 225,248,000 |
| Current Liabilities | — | — | 87,812,000 | 87,812,000 |
| Liabilities | — | — | 163,188,000 | 163,188,000 |
| Total SE | — | — | 62,060,000 | 62,060,000 |
| Total L+SE | — | — | 225,248,000 | 225,248,000 |

**Action: No change.**

---

## FY2020

**Sources:** Dolt + SEC comparative (FY2022 10-K, column 2020-12-31). Balance sheet identity fails in Dolt — correcting.

### Anomaly Detection
- `[ERROR]` Liabilities field in Dolt (101,408,000K) is LESS than Current Liabilities (126,385,000K) — mathematically impossible. Balance sheet identity fails: 101,408,000 + 93,404,000 = 194,812,000 ≠ 321,195,000 (Total Assets). Correcting to Total Assets − TSE = 227,791,000K.
- Income statement confirmed by SEC FY2022 10-K comparative ✓
- Gross margin: 152,757,000 / 386,064,000 = 39.6% — consistent with Amazon's model.
- Balance sheet after correction: 227,791,000 + 93,404,000 = 321,195,000 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 386,064,000 | — | 386,064,000 | 386,064,000 |
| Cost of Goods | 233,307,000 | — | 233,307,000 | 233,307,000 |
| Gross Margin | 152,757,000 | — | 152,757,000 | 152,757,000 |
| SGA | 28,676,000* | — | 28,676,000 | 28,676,000 |
| Operating Profit | 22,899,000 | — | 22,899,000 | 22,899,000 |
| Net Profit | 21,331,000 | — | 21,331,000 | 21,331,000 |
| Inventory | — | — | 23,795,000 | 23,795,000 |
| Current Assets | — | — | 132,733,000 | 132,733,000 |
| Total Assets | — | — | 321,195,000 | 321,195,000 |
| Current Liabilities | — | — | 126,385,000 | 126,385,000 |
| Liabilities | — | — | **101,408,000*** | **227,791,000** |
| Total SE | — | — | 93,404,000 | 93,404,000 |
| Total L+SE | — | — | 321,195,000 | 321,195,000 |

*SGA (Marketing 22,008 + G&A 6,668 = 28,676K) confirms Dolt; Other op income (-75K) correctly excluded.
*Dolt Liabilities of 101,408,000K is invalid (< Current Liabilities). Correct = 321,195,000 - 93,404,000 = 227,791,000K.

**Action: Correction — Liabilities only. All other fields confirmed.**

---

## FY2021

**Sources:** Dolt + SEC comparative (FY2022 10-K, column 2021-12-31). Balance sheet unverified.

### Anomaly Detection
- `[WARNING]` SGA: Dolt 41,436,000K includes "Other operating expense" (62,000K = small restructuring). Per anomaly rules, exclude one-time charges. Correcting to Marketing (32,551) + G&A (8,823) = 41,374,000K.
- Income statement confirmed by SEC FY2022 10-K comparative (operating income, net income, revenue all match) ✓
- `[WARNING]` Balance sheet not verified from SEC (FY2021 10-K not fetched). Identity: 282,304,000 + 138,245,000 = 420,549,000 ✓
- Gross margin: 197,478,000 / 469,822,000 = 42.0% — above Online benchmark; expected for Amazon's model.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 469,822,000 | — | 469,822,000 | 469,822,000 |
| Cost of Goods | 272,344,000 | — | 272,344,000 | 272,344,000 |
| Gross Margin | 197,478,000 | — | 197,478,000 | 197,478,000 |
| SGA | **41,374,000*** | — | 41,436,000* | **41,374,000** |
| Operating Profit | 24,879,000 | — | 24,879,000 | 24,879,000 |
| Net Profit | 33,364,000 | — | 33,364,000 | 33,364,000 |
| Inventory | — | — | 32,640,000 | 32,640,000 |
| Current Assets | — | — | 161,580,000 | 161,580,000 |
| Total Assets | — | — | 420,549,000 | 420,549,000 |
| Current Liabilities | — | — | 142,266,000 | 142,266,000 |
| Liabilities | — | — | 282,304,000 | 282,304,000 |
| Total SE | — | — | 138,245,000 | 138,245,000 |
| Total L+SE | — | — | 420,549,000 | 420,549,000 |

*SEC SGA = Marketing (32,551) + G&A (8,823) = 41,374K. Dolt 41,436K includes Other op expense (62K) → exclude per anomaly rules.

**Action: Correction — SGA only. All other values confirmed or identity passes.**

---

## FY2022

**Sources:** Dolt + SEC (FY2022 10-K, leftmost column 2022-12-31) + Yahoo (column 2022-12-31).

### Anomaly Detection
- `[WARNING]` SGA: Dolt 55,392,000K includes "Other operating expense" (1,263,000K = restructuring/layoffs). Per anomaly rules, exclude one-time charges. Correcting to Marketing (42,238) + G&A (11,891) = 54,129,000K.
- Yahoo SGA = 54,129,000K (Marketing + G&A) → confirms corrected value ✓
- All balance sheet fields confirmed: SEC = Dolt ✓
- Gross margin: 225,152,000 / 513,983,000 = 43.8% — above Online benchmark; expected for Amazon.
- Net Profit = -2,722,000K (loss year) — confirmed by SEC ✓
- Balance sheet: 316,632,000 + 146,043,000 = 462,675,000 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 513,983,000 | 513,983,000 | 513,983,000 | 513,983,000 |
| Cost of Goods | 288,831,000 | 288,831,000 | 288,831,000 | 288,831,000 |
| Gross Margin | 225,152,000 | 225,152,000 | 225,152,000 | 225,152,000 |
| SGA | **54,129,000*** | 54,129,000 | 55,392,000* | **54,129,000** |
| Operating Profit | 12,248,000 | 12,248,000 | 12,248,000 | 12,248,000 |
| Net Profit | -2,722,000 | -2,722,000 | -2,722,000 | -2,722,000 |
| Inventory | 34,405,000 | 34,405,000 | 34,405,000 | 34,405,000 |
| Current Assets | 146,791,000 | 146,791,000 | 146,791,000 | 146,791,000 |
| Total Assets | 462,675,000 | 462,675,000 | 462,675,000 | 462,675,000 |
| Current Liabilities | 155,393,000 | 155,393,000 | 155,393,000 | 155,393,000 |
| Liabilities | 316,632,000 | 316,632,000 | 316,632,000 | 316,632,000 |
| Total SE | 146,043,000 | 146,043,000 | 146,043,000 | 146,043,000 |
| Total L+SE | 462,675,000 | 462,675,000 | 462,675,000 | 462,675,000 |

*SEC SGA = Marketing (42,238) + G&A (11,891) = 54,129K. Dolt 55,392K included Other op expense (1,263K) → exclude per anomaly rules.

**Action: Correction — SGA only. All balance sheet fields confirmed.**

---

## FY2023

**Sources:** Dolt + SEC (FY2023 10-K, leftmost column 2023-12-31) + Yahoo (column 2023-12-31).

### Anomaly Detection
- All fields confirmed: SEC = Dolt = Yahoo ✓
- Gross margin: 270,046,000 / 574,785,000 = 47.0% — above Online benchmark; expected for Amazon.
- Balance sheet: 325,979,000 + 201,875,000 = 527,854,000 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 574,785,000 | 574,785,000 | 574,785,000 | 574,785,000 |
| Cost of Goods | 304,739,000 | 304,739,000 | 304,739,000 | 304,739,000 |
| Gross Margin | 270,046,000 | 270,046,000 | 270,046,000 | 270,046,000 |
| SGA | 56,186,000 | 56,186,000 | 56,186,000 | 56,186,000 |
| Operating Profit | 36,852,000 | 36,852,000 | 36,852,000 | 36,852,000 |
| Net Profit | 30,425,000 | 30,425,000 | 30,425,000 | 30,425,000 |
| Inventory | 33,318,000 | 33,318,000 | 33,318,000 | 33,318,000 |
| Current Assets | 172,351,000 | 172,351,000 | 172,351,000 | 172,351,000 |
| Total Assets | 527,854,000 | 527,854,000 | 527,854,000 | 527,854,000 |
| Current Liabilities | 164,917,000 | 164,917,000 | 164,917,000 | 164,917,000 |
| Liabilities | 325,979,000 | 325,979,000 | 325,979,000 | 325,979,000 |
| Total SE | 201,875,000 | 201,875,000 | 201,875,000 | 201,875,000 |
| Total L+SE | 527,854,000 | 527,854,000 | 527,854,000 | 527,854,000 |

**Action: No change.**

---

## FY2024

**Sources:** Dolt + SEC (FY2024 10-K, leftmost column 2024-12-31) + Yahoo (column 2024-12-31).

### Anomaly Detection
- All fields confirmed: SEC = Dolt = Yahoo ✓
- Gross margin: 311,671,000 / 637,959,000 = 48.9% — above Online benchmark; expected for Amazon.
- Balance sheet: 338,924,000 + 285,970,000 = 624,894,000 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 637,959,000 | 637,959,000 | 637,959,000 | 637,959,000 |
| Cost of Goods | 326,288,000 | 326,288,000 | 326,288,000 | 326,288,000 |
| Gross Margin | 311,671,000 | 311,671,000 | 311,671,000 | 311,671,000 |
| SGA | 55,266,000 | 55,266,000 | 55,266,000 | 55,266,000 |
| Operating Profit | 68,593,000 | 68,593,000 | 68,593,000 | 68,593,000 |
| Net Profit | 59,248,000 | 59,248,000 | 59,248,000 | 59,248,000 |
| Inventory | 34,214,000 | 34,214,000 | 34,214,000 | 34,214,000 |
| Current Assets | 190,867,000 | 190,867,000 | 190,867,000 | 190,867,000 |
| Total Assets | 624,894,000 | 624,894,000 | 624,894,000 | 624,894,000 |
| Current Liabilities | 179,431,000 | 179,431,000 | 179,431,000 | 179,431,000 |
| Liabilities | 338,924,000 | 338,924,000 | 338,924,000 | 338,924,000 |
| Total SE | 285,970,000 | 285,970,000 | 285,970,000 | 285,970,000 |
| Total L+SE | 624,894,000 | 624,894,000 | 624,894,000 | 624,894,000 |

**Action: No change.**

---

## FY2025

**Sources:** SEC (FY2025 10-K, leftmost column 2025-12-31) + Yahoo (column 2025-12-31). New insert.

### Anomaly Detection
- All fields confirmed: SEC = Yahoo ✓
- SGA = Marketing (47,129,000) + G&A (11,172,000) = 58,301,000K (Other op expense 4,639,000K excluded per anomaly rules).
- Gross margin: 360,510,000 / 716,924,000 = 50.3% — above Online benchmark; expected for Amazon's AWS/advertising mix.
- Balance sheet: 406,977,000 + 411,065,000 = 818,042,000 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 716,924,000 | 716,924,000 | — | 716,924,000 |
| Cost of Goods | 356,414,000 | 356,414,000 | — | 356,414,000 |
| Gross Margin | 360,510,000 | 360,510,000 | — | 360,510,000 |
| SGA | 58,301,000* | 58,301,000 | — | 58,301,000 |
| Operating Profit | 79,975,000 | 79,975,000 | — | 79,975,000 |
| Net Profit | 77,670,000 | 77,670,000 | — | 77,670,000 |
| Inventory | 38,325,000 | 38,325,000 | — | 38,325,000 |
| Current Assets | 229,083,000 | 229,083,000 | — | 229,083,000 |
| Total Assets | 818,042,000 | 818,042,000 | — | 818,042,000 |
| Current Liabilities | 218,005,000 | 218,005,000 | — | 218,005,000 |
| Liabilities | 406,977,000 | 406,977,000 | — | 406,977,000 |
| Total SE | 411,065,000 | 411,065,000 | — | 411,065,000 |
| Total L+SE | 818,042,000 | 818,042,000 | — | 818,042,000 |

*SGA = Marketing (47,129,000) + G&A (11,172,000) = 58,301,000K. "Other operating expense" (4,639,000K, primarily restructuring/asset disposals) excluded per anomaly rules.

**Action: New insert.**

---

## Unresolved Flags

1. `[WARNING]` FY2018 and FY2019 income statements not verified from SEC (older 10-Ks not fetched). Balance sheet identities pass.
2. `[WARNING]` FY2021 balance sheet not confirmed from SEC. Identity passes.

**Analysis complete.** Run `/insert-financials AMZN` to write all changed years to the database.
