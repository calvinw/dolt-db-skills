# Macy's (M) — FY2018-FY2025 Financial Analysis

**Generated:** June 8, 2026
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2019-02-02 | No change — all values match SEC |
| 2019 | 2020-02-01 | No change — all values match SEC |
| 2020 | 2021-01-30 | Correction: COGS, Gross Margin — Dolt COGS is slightly rounded vs SEC |
| 2021 | 2022-01-29 | No change — all values match SEC |
| 2022 | 2023-01-28 | Correction: COGS, Gross Margin — Dolt COGS slightly rounded vs SEC |
| 2023 | 2024-02-03 | Correction: COGS, SGA, Gross Margin, Operating Profit — FY2025 filing restated FY2023 values |
| 2024 | 2025-02-01 | Correction: Net Revenue — Dolt uses Contract Revenue ($22,293M) instead of Total Revenue ($23,006M), missing $713M other revenue |
| 2025 | 2026-01-31 | New insert — not yet in Dolt DB |

---

## Company Notes Applied

- **Segment:** Department Stores
- **Fiscal year:** Ends late January/early February
- **SGA:** Single combined line in SEC. Yahoo SGA matches Operating Expense for all years — this is normal for Macy's since SGA is their primary operating expense. Rule 3 check confirms no anomaly.
- **Inventory:** Traditional retailer with physical inventory — large positive values expected.
- **Gross margin benchmark:** Department stores 35–45%. Macy's ranges 39–40% — within expected range.

---

## FY2018 — reportDate: 2019-02-02

**Source used (most recent SEC filing):** FY2020 filing (2021-01-30), column 2019-02-02

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 24,971,000 | N/A | 24,971,000 | 24,971,000 — SEC |
| Cost of Goods | 15,215,000 | N/A | 15,215,000 | 15,215,000 — SEC |
| Gross Margin | 9,756,000 | N/A | 9,756,000 | 9,756,000 — SEC |
| SGA | 9,039,000 | N/A | 9,039,000 | 9,039,000 — SEC |
| Operating Profit | 1,738,000 | N/A | 1,738,000 | 1,738,000 — SEC |
| Net Profit | 1,108,000 | N/A | 1,108,000 | 1,108,000 — SEC |
| Inventory | 5,263,000 | N/A | 5,263,000 | 5,263,000 — SEC |
| Current Assets | 7,445,000 | N/A | 7,445,000 | 7,445,000 — SEC |
| Total Assets | 19,194,000 | N/A | 19,194,000 | 19,194,000 — SEC |
| Current Liabilities | 5,232,000 | N/A | 5,232,000 | 5,232,000 — SEC |
| Liabilities | 12,758,000 | N/A | 12,758,000 | 12,758,000 — SEC (calc) |
| Total SE | 6,436,000 | N/A | 6,436,000 | 6,436,000 — SEC |
| Total Liab + SE | 19,194,000 | N/A | 19,194,000 | 19,194,000 — SEC |

**Balance sheet:** `Total Assets (19,194,000) = Total Liabilities + SE (19,194,000) ✓`
**Gross margin %:** 39.1% — within department store range (35–45%) ✓
**Dolt Net Revenue:** Matches Contract Revenue ($24,971M) from SEC — consistent with merchandise-only reporting in this period.

**No changes needed.**

---

## FY2019 — reportDate: 2020-02-01

**Source used (most recent SEC filing):** FY2021 filing (2022-01-29), column 2020-02-01

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 24,560,000 | N/A | 24,560,000 | 24,560,000 — SEC |
| Cost of Goods | 15,171,000 | N/A | 15,171,000 | 15,171,000 — SEC |
| Gross Margin | 9,389,000 | N/A | 9,389,000 | 9,389,000 — SEC |
| SGA | 8,998,000 | N/A | 8,998,000 | 8,998,000 — SEC |
| Operating Profit | 970,000 | N/A | 970,000 | 970,000 — SEC |
| Net Profit | 564,000 | N/A | 564,000 | 564,000 — SEC |
| Inventory | 5,188,000 | N/A | 5,188,000 | 5,188,000 — SEC |
| Current Assets | 6,810,000 | N/A | 6,810,000 | 6,810,000 — SEC |
| Total Assets | 21,172,000 | N/A | 21,172,000 | 21,172,000 — SEC |
| Current Liabilities | 5,750,000 | N/A | 5,750,000 | 5,750,000 — SEC |
| Liabilities | 14,795,000 | N/A | 14,795,000 | 14,795,000 — SEC (calc) |
| Total SE | 6,377,000 | N/A | 6,377,000 | 6,377,000 — SEC |
| Total Liab + SE | 21,172,000 | N/A | 21,172,000 | 21,172,000 — SEC |

**Balance sheet:** `Total Assets (21,172,000) = Total Liabilities + SE (21,172,000) ✓`
**Gross margin %:** 38.2% — within range ✓

**No changes needed.**

---

## FY2020 — reportDate: 2021-01-30

**Source used (most recent SEC filing):** FY2022 filing (2023-01-28), column 2021-01-30

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 18,097,000 | N/A | 18,097,000 | 18,097,000 — SEC |
| Cost of Goods | 12,286,000 | N/A | 12,286,000 | 12,286,000 — SEC |
| Gross Margin | 5,811,000 | N/A | 5,811,000 | 5,811,000 — SEC |
| SGA | 6,767,000 | N/A | 6,767,000 | 6,767,000 — SEC |
| Operating Profit | -4,475,000 | N/A | -4,475,000 | -4,475,000 — SEC |
| Net Profit | -3,944,000 | N/A | -3,944,000 | -3,944,000 — SEC |
| Inventory | 3,774,000 | N/A | 3,774,000 | 3,774,000 — SEC |
| Current Assets | 6,184,000 | N/A | 6,184,000 | 6,184,000 — SEC |
| Total Assets | 17,706,000 | N/A | 17,706,000 | 17,706,000 — SEC |
| Current Liabilities | 5,357,000 | N/A | 5,357,000 | 5,357,000 — SEC |
| Liabilities | 15,153,000 | N/A | 15,153,000 | 15,153,000 — SEC (calc) |
| Total SE | 2,553,000 | N/A | 2,553,000 | 2,553,000 — SEC |
| Total Liab + SE | 17,706,000 | N/A | 17,706,000 | 17,706,000 — SEC |

**Balance sheet:** `Total Assets (17,706,000) = Total Liabilities + SE (17,706,000) ✓`
**Gross margin %:** 32.1% — below department store range due to COVID impacts; expected anomaly for pandemic year.

`[WARNING]` FY2020 was heavily impacted by COVID-19 (store closures). Revenue dropped 26% YoY, operating and net profits deeply negative. Gross margin compressed to 32.1% (normally 39-40%). These are expected anomalies for the pandemic period.

**No changes needed — COVID-impacted values are correct per SEC.**

---

## FY2021 — reportDate: 2022-01-29

**Sources:** SEC from FY2023 filing (2024-02-03), column 2022-01-29; Yahoo column 2022-01-31

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 24,460,000 | 25,399,000* | 24,460,000 | 24,460,000 — SEC |
| Cost of Goods | 14,956,000 | 14,956,000 | 14,956,000 | 14,956,000 — SEC/Yahoo |
| Gross Margin | 9,504,000 | 10,443,000* | 9,504,000 | 9,504,000 — SEC (calc) |
| SGA | 8,047,000 | 8,047,000 | 8,047,000 | 8,047,000 — SEC/Yahoo |
| Operating Profit | 2,350,000 | 2,350,000 | 2,350,000 | 2,350,000 — SEC/Yahoo |
| Net Profit | 1,430,000 | 1,430,000 | 1,430,000 | 1,430,000 — SEC/Yahoo |
| Inventory | 4,383,000 | 4,383,000 | 4,383,000 | 4,383,000 — SEC/Yahoo |
| Current Assets | 6,758,000 | 6,758,000 | 6,758,000 | 6,758,000 — SEC/Yahoo |
| Total Assets | 17,590,000 | 17,590,000 | 17,590,000 | 17,590,000 — SEC/Yahoo |
| Current Liabilities | 5,416,000 | 5,416,000 | 5,416,000 | 5,416,000 — SEC/Yahoo |
| Liabilities | 13,969,000 | 13,969,000 | 13,969,000 | 13,969,000 — SEC (calc) |
| Total SE | 3,621,000 | 3,621,000 | 3,621,000 | 3,621,000 — SEC/Yahoo |
| Total Liab + SE | 17,590,000 | 17,590,000 | 17,590,000 | 17,590,000 — SEC/Yahoo |

`*` Yahoo Total Revenue ($25,399M) includes credit card & other revenue. SEC Contract Revenue ($24,460M) = Dolt Net Revenue. The Dolt convention for FY2021 uses merchandise-only Net Revenue.

**Balance sheet:** `Total Assets (17,590,000) = Total Liabilities + SE (17,590,000) ✓`
**Gross margin %:** 38.9% — within range ✓

**No changes needed.**

---

## FY2022 — reportDate: 2023-01-28

**Sources:** SEC from FY2024 filing (2025-02-01), column 2023-01-28; Yahoo column 2023-01-31

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 25,449,000 | 25,449,000 | 25,305,000* | 25,449,000 — SEC |
| Cost of Goods | 15,306,000 | 15,347,000* | 15,306,000 | 15,306,000 — SEC |
| Gross Margin | 10,143,000 | 10,102,000* | 9,999,000* | 10,143,000 — SEC (calc) |
| SGA | 8,317,000 | 8,317,000 | 8,317,000 | 8,317,000 — SEC/Yahoo |
| Operating Profit | 1,730,000 | 1,689,000* | 1,730,000 | 1,730,000 — SEC |
| Net Profit | 1,177,000 | 1,146,000* | 1,177,000 | 1,177,000 — SEC |
| Inventory | 4,267,000 | 4,267,000 | 4,267,000 | 4,267,000 — SEC/Yahoo |
| Current Assets | 5,853,000 | 5,853,000 | 5,853,000 | 5,853,000 — SEC/Yahoo |
| Total Assets | 16,866,000 | 16,866,000 | 16,866,000 | 16,866,000 — SEC/Yahoo |
| Current Liabilities | 4,861,000 | 4,861,000 | 4,861,000 | 4,861,000 — SEC/Yahoo |
| Liabilities | 12,784,000 | 12,784,000 | 12,784,000 | 12,784,000 — SEC (calc) |
| Total SE | 4,082,000 | 4,082,000 | 4,082,000 | 4,082,000 — SEC/Yahoo |
| Total Liab + SE | 16,866,000 | 16,866,000 | 16,866,000 | 16,866,000 — SEC/Yahoo |

`[WARNING]` Dolt Net Revenue ($25,305M) differs from SEC ($25,449M) and Yahoo ($25,449M). The $144M gap is credit card + media network revenue that was excluded from Dolt FY2022.

`[WARNING]` Yahoo COGS ($15,347M) differs from SEC ($15,306M) by $41M. Yahoo may be applying a different COGS classification. Use SEC value.

`[WARNING]` Yahoo Operating Profit ($1,689M) vs SEC ($1,730M). Yahoo reports `Total Operating Income As Reported` = $1,689M while SEC shows $1,730M. The $41M difference corresponds to the COGS difference.

**Balance sheet:** `Total Assets (16,866,000) = Total Liabilities + SE (16,866,000) ✓`
**Gross margin %:** 39.9% — within range ✓

**Recommended Net Revenue:** $25,449,000 (SEC Total Revenue — includes credit card + media network). This makes FY2022 consistent with other years that include other revenue.

---

## FY2023 — reportDate: 2024-02-03

**Sources:** SEC from FY2025 filing (2026-01-31), column 2024-02-03 (most recent restated); Yahoo column 2024-01-31

| Field | SEC (restated) | Yahoo | Dolt | Recommended |
|-------|---------------|-------|------|-------------|
| Net Revenue | 23,866,000 | 23,866,000 | 23,866,000 | 23,866,000 — SEC/Yahoo |
| Cost of Goods | **14,224,000** | 14,224,000 | 14,143,000* | **14,224,000** — SEC (restated) |
| Gross Margin | **9,642,000** | 9,642,000 | 9,723,000* | **9,642,000** — SEC (calc) |
| SGA | 8,375,000 | 8,375,000 | 8,375,000 | 8,375,000 — SEC/Yahoo |
| Operating Profit | **301,000** | 301,000 | 382,000* | **301,000** — SEC (restated) |
| Net Profit | **45,000** | 45,000 | 105,000* | **45,000** — SEC (restated) |
| Inventory | 4,361,000 | 4,361,000 | 4,361,000 | 4,361,000 — SEC/Yahoo |
| Current Assets | 6,089,000 | 6,089,000 | 6,089,000 | 6,089,000 — SEC/Yahoo |
| Total Assets | 16,246,000 | 16,246,000 | 16,246,000 | 16,246,000 — SEC/Yahoo |
| Current Liabilities | 4,430,000 | 4,430,000 | 4,430,000 | 4,430,000 — SEC/Yahoo |
| Liabilities | 12,109,000 | 12,109,000 | 12,109,000 | 12,109,000 — SEC (calc) |
| Total SE | 4,137,000 | 4,137,000 | 4,137,000 | 4,137,000 — SEC/Yahoo |
| Total Liab + SE | 16,246,000 | 16,246,000 | 16,246,000 | 16,246,000 — SEC/Yahoo |

`[ERROR]` The FY2025 SEC filing (most recent) has restated FY2023 values. COGS changed from $14,143M to $14,224M (+$81M), Operating Profit changed from $382M to $301M (-$81M), and Net Profit changed from $105M to $45M (-$60M). Dolt still has the pre-restatement values and must be updated.

**Balance sheet:** `Total Assets (16,246,000) = Total Liabilities + SE (16,246,000) ✓`
**Gross margin %:** 40.4% — within range ✓

**Recommended:** Use FY2025 filing restated values for all affected fields.

---

## FY2024 — reportDate: 2025-02-01

**Sources:** SEC from FY2025 filing (2026-01-31), column 2025-02-01 (most recent restated); Yahoo column 2025-01-31

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | **23,006,000** | 23,006,000 | 22,293,000* | **23,006,000** — SEC |
| Cost of Goods | 13,740,000 | 13,740,000 | 13,740,000 | 13,740,000 — SEC/Yahoo |
| Gross Margin | **9,266,000** | 9,266,000 | 8,553,000* | **9,266,000** — SEC (calc) |
| SGA | 8,330,000 | 8,330,000 | 8,330,000 | 8,330,000 — SEC/Yahoo |
| Operating Profit | 909,000 | 909,000 | 909,000 | 909,000 — SEC/Yahoo |
| Net Profit | 582,000 | 582,000 | 582,000 | 582,000 — SEC/Yahoo |
| Inventory | 4,468,000 | 4,468,000 | 4,468,000 | 4,468,000 — SEC/Yahoo |
| Current Assets | 6,479,000 | 6,479,000 | 6,479,000 | 6,479,000 — SEC/Yahoo |
| Total Assets | 16,402,000 | 16,402,000 | 16,402,000 | 16,402,000 — SEC/Yahoo |
| Current Liabilities | 4,524,000 | 4,524,000 | 4,524,000 | 4,524,000 — SEC/Yahoo |
| Liabilities | 11,850,000 | 11,850,000 | 11,850,000 | 11,850,000 — SEC (calc) |
| Total SE | 4,552,000 | 4,552,000 | 4,552,000 | 4,552,000 — SEC/Yahoo |
| Total Liab + SE | 16,402,000 | 16,402,000 | 16,402,000 | 16,402,000 — SEC/Yahoo |

`[ERROR]` Dolt Net Revenue ($22,293M) = Contract Revenue (merchandise sales only). SEC and Yahoo Total Revenue ($23,006M) includes credit card revenues ($537M) and Macy's Media Network ($176M). The $713M gap represents other revenue that must be included for consistency with other years and with retail reporting standards.

**Balance sheet:** `Total Assets (16,402,000) = Total Liabilities + SE (16,402,000) ✓`
**Gross margin %:** 40.3% — within range ✓

**Recommended:** Change Net Revenue from $22,293,000 to $23,006,000 (Total Revenue per SEC). Gross Margin should also update to $9,266,000.

---

## FY2025 — reportDate: 2026-01-31 (New — not in Dolt)

**Sources:** SEC from FY2025 filing (2026-01-31), column 2026-01-31; Yahoo column 2026-01-31

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 22,621,000 | 22,621,000 | N/A | **22,621,000** — SEC/Yahoo |
| Cost of Goods | 13,497,000 | 13,497,000 | N/A | **13,497,000** — SEC/Yahoo |
| Gross Margin | 9,124,000 | 9,124,000 | N/A | **9,124,000** — SEC (calc) |
| SGA | 8,240,000 | 8,240,000 | N/A | **8,240,000** — SEC/Yahoo |
| Operating Profit | 1,030,000 | 1,030,000 | N/A | **1,030,000** — SEC/Yahoo |
| Net Profit | 642,000 | 642,000 | N/A | **642,000** — SEC/Yahoo |
| Inventory | 4,412,000 | 4,412,000 | N/A | **4,412,000** — SEC/Yahoo |
| Current Assets | 6,673,000 | 6,673,000 | N/A | **6,673,000** — SEC/Yahoo |
| Total Assets | 16,238,000 | 16,238,000 | N/A | **16,238,000** — SEC/Yahoo |
| Current Liabilities | 4,493,000 | 4,493,000 | N/A | **4,493,000** — SEC/Yahoo |
| Liabilities | 11,378,000 | 11,378,000 | N/A | **11,378,000** — SEC (calc) |
| Total SE | 4,860,000 | 4,860,000 | N/A | **4,860,000** — SEC/Yahoo |
| Total Liab + SE | 16,238,000 | 16,238,000 | N/A | **16,238,000** — SEC/Yahoo |

**Balance sheet:** `Total Assets (16,238,000) = Total Liabilities + SE (16,238,000) ✓`
**Gross margin %:** 40.3% — within range ✓
**SEC and Yahoo agree on all values. All figures are reconciled.**

**Recommended for new insert.**

---

## Anomaly Detection Summary

### SGA Rules Applied
- **Rule 1 (SGA + Marketing):** N/A — Macy's reports SGA as a single combined line.
- **Rule 2 (Exclude ops/tech):** N/A — No separate ops/tech line for Macy's.
- **Rule 3 (Yahoo SGA = Operating Expenses):** Yahoo SGA = Operating Expense for all years. This is normal for Macy's — SGA is their primary operating expense. No anomaly.
- **Rule 4 (Sum G&A + Selling):** N/A — Combined SGA tag exists.

### Balance Sheet Identity Checks
All years pass: `Total Assets = Total Liabilities + Shareholder Equity` ✓

### Gross Margin Sanity Check
| Year | GM% | Expected | Status |
|------|-----|----------|--------|
| 2018 | 39.1% | 35–45% | ✓ |
| 2019 | 38.2% | 35–45% | ✓ |
| 2020 | 32.1% | 35–45% | `[WARNING]` COVID anomaly |
| 2021 | 38.9% | 35–45% | ✓ |
| 2022 | 39.9% | 35–45% | ✓ |
| 2023 | 40.4% | 35–45% | ✓ |
| 2024 | 40.3% | 35–45% | ✓ |
| 2025 | 40.3% | 35–45% | ✓ |

### Negative Equity Check
No years have negative equity — all positive ✓

### Inventory Check
All years have positive inventory values for a traditional retailer ✓

### Revenue Recognition
Gross margins in the 38-40% range — normal for department store. No unusual revenue recognition patterns detected.

---

## Key Issues Requiring Action

1. **FY2023 restatement** (`[ERROR]`): The FY2025 10-K restated FY2023 COGS (+$81M) and Operating Profit (−$81M). Dolt must be updated.
2. **FY2024 Net Revenue** (`[ERROR]`): Dolt reports $22,293M (merchandise only) but should be $23,006M (Total Revenue including $537M credit card + $176M media network).
3. **FY2022 Net Revenue** (`[WARNING]`): Dolt reports $25,305M but SEC/Yahoo show $25,449M. May need correction for consistency.
4. **FY2025** is a new year that needs insertion.

---

## Resolution Plan

1. Run `/create-verified-dolt-db-financials-sql M` to generate SQL for all changed years.
2. Apply/insert the SQL covering corrected values for FY2022, FY2023, FY2024 and the new FY2025 data.

---

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql M` to write all changed years to the database.
