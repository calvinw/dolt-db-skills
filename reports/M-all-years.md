# Macy's (M) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-17
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2019-02-02 | No change (primary convention; SEC not re-fetched) |
| 2019 | 2020-02-01 | No change (primary convention; SEC not re-fetched) |
| 2020 | 2021-01-30 | No change ✓ |
| 2021 | 2022-01-29 | **Correction: Net Revenue, Gross Margin, SGA** |
| 2022 | 2023-01-28 | **Correction: Net Revenue, COGS, Gross Margin, SGA, Op Inc, Net Prof** |
| 2023 | 2024-02-03 | **Correction: COGS, Gross Margin, Op Inc, Net Prof, Curr Liab, Liabilities, SE** |
| 2024 | 2025-02-01 | **Correction: Net Revenue, Gross Margin** |
| 2025 | 2026-01-31 | No change ✓ |

---

## Background: Macy's Revenue Structure

Macy's income statement has two components in Net Revenue across all recent years:
- `us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax` — Contract Revenue (merchandise sales, broken out by category)
- `m_NetEarningsFromCreditOperations` (older filings) / `m_OtherRevenueNet` (FY2023+ filings) — Other Revenue (Credit Card Revenues + Macy's Media Network Revenue from FY2022 onward)
- `us-gaap_Revenues` — Total Revenue (appears from FY2022 onward; older years show no combined tag)

**Macy's Media Network (MMN) reclassification (FY2023 10-K):** Starting with the FY2023 10-K filing, Macy's moved MMN revenue from an SGA offset (reducing SGA) to a separate "Other Revenue" line above COGS. This increased both Net Revenue and SGA by the MMN amount, leaving Operating Income unchanged. Comparative years were restated accordingly.

**Restatement rule:** Always use the most recent filing version for any given year.

---

## FY2018 — reportDate 2019-02-02

**Sources used:** Dolt DB only (SEC not re-fetched; Yahoo does not cover this year).

### Anomaly Detection
- Gross Margin: 9,756 / 24,971 = 39.1% ✓ (Department Stores benchmark: 35–45%)
- Balance sheet identity: 19,194 = 19,194 ✓
- SGA is a single combined line. ✓
- NOTE: Revenue 24,971K may represent contract revenue only (without Credit Card Revenue), consistent with the convention in place for original FY2018 filing. Not re-verified against primary 10-K in this session.

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | — | 24,971 | 24,971 |
| COGS | — | — | 15,215 | 15,215 |
| Gross Margin | — | — | 9,756 | 9,756 |
| SGA | — | — | 9,039 | 9,039 |
| Operating Profit | — | — | 1,738 | 1,738 |
| Net Profit | — | — | 1,108 | 1,108 |
| Inventory | — | — | 5,263 | 5,263 |
| Current Assets | — | — | 7,445 | 7,445 |
| Total Assets | — | — | 19,194 | 19,194 |
| Current Liabilities | — | — | 5,232 | 5,232 |
| Liabilities | — | — | 12,758 | 12,758 |
| TSE | — | — | 6,436 | 6,436 |
| Total L+SE | — | — | 19,194 | 19,194 |

### Reconciled Recommendation
**No change.** All Dolt values accepted as original primary convention. FY2018/FY2019 Credit Card Revenue placement in the income statement (above vs. below COGS) was not re-verified against the original 10-K and should be confirmed in a separate session.

---

## FY2019 — reportDate 2020-02-01

**Sources used:** Dolt DB only (SEC not re-fetched; Yahoo does not cover this year).

### Anomaly Detection
- Gross Margin: 9,389 / 24,560 = 38.2% ✓
- Balance sheet identity: 21,172 = 21,172 ✓
- NOTE: Same convention caveat as FY2018 — CC revenue placement not re-verified.

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | — | 24,560 | 24,560 |
| COGS | — | — | 15,171 | 15,171 |
| Gross Margin | — | — | 9,389 | 9,389 |
| SGA | — | — | 8,998 | 8,998 |
| Operating Profit | — | — | 970 | 970 |
| Net Profit | — | — | 564 | 564 |
| Inventory | — | — | 5,188 | 5,188 |
| Current Assets | — | — | 6,810 | 6,810 |
| Total Assets | — | — | 21,172 | 21,172 |
| Current Liabilities | — | — | 5,750 | 5,750 |
| Liabilities | — | — | 14,795 | 14,795 |
| TSE | — | — | 6,377 | 6,377 |
| Total L+SE | — | — | 21,172 | 21,172 |

### Reconciled Recommendation
**No change.** Same caveat as FY2018.

---

## FY2020 — reportDate 2021-01-30

**Sources used:** Dolt DB; FY2021 10-K comparative (2021-01-30 column); FY2022 10-K comparative (2021-01-30 column).

### Anomaly Detection
- [WARNING] Gross Margin: 5,811 / 18,097 = 32.1% — below 35–45% Department Stores range, but expected due to COVID-19 pandemic store closures and impairments. Not an error.
- Balance sheet identity: 17,706 = 17,706 ✓
- Revenue structure verified: FY2021 10-K shows 2021-01-30 column as Contract 17,346K + CC 751K = 18,097K ✓

### Side-by-Side Comparison

| Field | SEC (FY2021 10-K comparative) | Yahoo | Dolt | Recommended |
|-------|-------------------------------|-------|------|-------------|
| Net Revenue | 18,097 (17,346+751) | — | 18,097 | 18,097 |
| COGS | 12,286 | — | 12,286 | 12,286 |
| Gross Margin | 5,811 | — | 5,811 | 5,811 |
| SGA | 6,767 | — | 6,767 | 6,767 |
| Operating Profit | -4,475 | — | -4,475 | -4,475 |
| Net Profit | -3,944 | — | -3,944 | -3,944 |
| Inventory | — | — | 3,774 | 3,774 |
| Current Assets | — | — | 6,184 | 6,184 |
| Total Assets | — | — | 17,706 | 17,706 |
| Current Liabilities | — | — | 5,357 | 5,357 |
| Liabilities | — | — | 15,153 | 15,153 |
| TSE | — | — | 2,553 | 2,553 |
| Total L+SE | — | — | 17,706 | 17,706 |

### Reconciled Recommendation
**No change.** Revenue matches (contract 17,346 + CC 751 = 18,097 ✓). COVID gross margin anomaly is expected.

---

## FY2021 — reportDate 2022-01-29

**Sources used:** Dolt DB; FY2021 primary 10-K; FY2022 10-K comparative; FY2023 10-K comparative (most recent).

### Anomaly Detection
- [ERROR] Net Revenue missing Credit Card revenue: FY2021 primary 10-K shows Contract Revenue 24,460K + Credit Card Revenues 832K (m_NetEarningsFromCreditOperations, at level=1, before COGS). Dolt stores 24,460K (contract only). The CC revenue is clearly part of Net Revenue in the filing, and FY2020 correctly includes CC revenue.
- [WARNING] MMN reclassification: FY2023 10-K comparative (2022-01-29) shows Other Revenue = 939K (CC 832K + MMN 107K), with SGA increased by 107K (8,047K → 8,154K). Per restatement rule, most recent filing (FY2023 10-K) takes precedence.
- Gross Margin (Dolt): 9,504 / 24,460 = 38.9% — appears acceptable but is wrong due to understated revenue.
- Gross Margin (corrected): 10,443 / 25,399 = 41.1% ✓
- Balance sheet identity: 17,590 = 17,590 ✓. Balance sheet unchanged between filings.

Revenue reconstruction:
- FY2021 primary (FY2021 10-K): Contract 24,460 + CC 832 = 25,292K
- FY2023 10-K restated (most recent): Contract 24,460 + CC 832 + MMN 107 = 25,399K

### Side-by-Side Comparison

| Field | SEC (FY2021 primary) | SEC (FY2023 restated, most recent) | Yahoo | Dolt | Recommended |
|-------|---------------------|-----------------------------------|-------|------|-------------|
| Net Revenue | 25,292 | 25,399 | — | **24,460** | **25,399** |
| COGS | 14,956 | 14,956 | — | 14,956 | 14,956 |
| Gross Margin | 10,336 | 10,443 | — | **9,504** | **10,443** |
| SGA | 8,047 | 8,154 | — | **8,047** | **8,154** |
| Operating Profit | 2,350 | 2,350 | — | 2,350 | 2,350 |
| Net Profit | 1,430 | 1,430 | — | 1,430 | 1,430 |
| Inventory | 4,383 | — | — | 4,383 | 4,383 |
| Current Assets | 6,758 | — | — | 6,758 | 6,758 |
| Total Assets | 17,590 | — | — | 17,590 | 17,590 |
| Current Liabilities | 5,416 | — | — | 5,416 | 5,416 |
| Liabilities | 13,969 | — | — | 13,969 | 13,969 |
| TSE | 3,621 | — | — | 3,621 | 3,621 |
| Total L+SE | 17,590 | — | — | 17,590 | 17,590 |

### Reconciled Recommendation
- **Net Revenue: 24,460 → 25,399** [ERROR — add CC 832K + MMN 107K per FY2023 10-K restated values]
- **Gross Margin: 9,504 → 10,443** (derived: 25,399 − 14,956)
- **SGA: 8,047 → 8,154** [WARNING — MMN reclassification +107K per FY2023 10-K]
- Operating Profit, Net Profit, all balance sheet fields: **no change**

---

## FY2022 — reportDate 2023-01-28

**Sources used:** Dolt DB; FY2022 primary 10-K; FY2023 10-K comparative; FY2024 10-K comparative (most recent for income statement).

### Anomaly Detection
- [WARNING] MMN reclassification (FY2023 10-K): Macy's Media Network Revenue 144K moved from SGA offset to separate revenue line. Revenue: 25,305 → 25,449; SGA: 8,317 → 8,461. Operating Income unchanged at 1,730K.
- [WARNING] COGS restatement (FY2024 10-K): COGS increased by 41K (15,306 → 15,347). Operating Income decreased by 41K (1,730 → 1,689). Net Profit changed 1,177 → 1,146 (−31K after tax).
- Gross Margin (corrected): 10,102 / 25,449 = 39.7% ✓
- Balance sheet: Unchanged across all filings. ✓
- Balance sheet identity: 16,866 = 16,866 ✓

### Side-by-Side Comparison

| Field | SEC (FY2022 primary) | SEC (FY2024 restated, most recent) | Yahoo | Dolt | Recommended |
|-------|---------------------|-----------------------------------|-------|------|-------------|
| Net Revenue | 25,305 | 25,449 | 25,449 | **25,305** | **25,449** |
| COGS | 15,306 | 15,347 | 15,347 | **15,306** | **15,347** |
| Gross Margin | 9,999 | 10,102 | 10,102 | **9,999** | **10,102** |
| SGA | 8,317 | 8,461 | 8,461 | **8,317** | **8,461** |
| Operating Profit | 1,730 | 1,689 | 1,689 | **1,730** | **1,689** |
| Net Profit | 1,177 | 1,146 | 1,146 | **1,177** | **1,146** |
| Inventory | 4,267 | 4,267 | 4,267 | 4,267 | 4,267 |
| Current Assets | 5,853 | 5,853 | 5,853 | 5,853 | 5,853 |
| Total Assets | 16,866 | 16,866 | 16,866 | 16,866 | 16,866 |
| Current Liabilities | 4,861 | 4,861 | 4,861 | 4,861 | 4,861 |
| Liabilities | 12,784 | 12,784 | 12,784 | 12,784 | 12,784 |
| TSE | 4,082 | 4,082 | 4,082 | 4,082 | 4,082 |
| Total L+SE | 16,866 | 16,866 | 16,866 | 16,866 | 16,866 |

### Reconciled Recommendation
- **Net Revenue: 25,305 → 25,449** [WARNING — MMN reclassification +144K per FY2024 10-K]
- **COGS: 15,306 → 15,347** [WARNING — restatement +41K per FY2024 10-K]
- **Gross Margin: 9,999 → 10,102** (derived: 25,449 − 15,347)
- **SGA: 8,317 → 8,461** [WARNING — MMN reclassification +144K per FY2024 10-K]
- **Operating Profit: 1,730 → 1,689** [WARNING — restatement −41K per FY2024 10-K]
- **Net Profit: 1,177 → 1,146** [WARNING — restatement −31K per FY2024 10-K]
- All balance sheet fields: **no change**

---

## FY2023 — reportDate 2024-02-03

**Sources used:** Dolt DB; FY2023 primary 10-K; FY2024 10-K comparative (most recent).

### Anomaly Detection
- [WARNING] COGS restatement: FY2024 10-K shows FY2023 COGS = 14,224K (vs. primary 14,143K, +81K). Operating Income drops 81K (382 → 301). Net Profit drops 60K (105 → 45, after tax effect).
- [WARNING] Balance sheet restatement: FY2024 10-K shows FY2023 Current Liabilities = 4,532K (+102K vs. primary 4,430K) and SE = 4,035K (−102K vs. primary 4,137K). Total Assets unchanged at 16,246K.
- Gross Margin (corrected): 9,642 / 23,866 = 40.4% ✓
- Balance sheet identity after correction: 16,246 = (12,211 + 4,035) = 16,246 ✓
- Revenue: Both primary and restated show 23,866K (us-gaap_Revenues). No change. ✓

### Side-by-Side Comparison

| Field | SEC (FY2023 primary) | SEC (FY2024 restated, most recent) | Yahoo | Dolt | Recommended |
|-------|---------------------|-----------------------------------|-------|------|-------------|
| Net Revenue | 23,866 | 23,866 | 23,866 | 23,866 | 23,866 |
| COGS | 14,143 | 14,224 | 14,224 | **14,143** | **14,224** |
| Gross Margin | 9,723 | 9,642 | 9,642 | **9,723** | **9,642** |
| SGA | 8,375 | 8,375 | 8,375 | 8,375 | 8,375 |
| Operating Profit | 382 | 301 | 301 | **382** | **301** |
| Net Profit | 105 | 45 | 45 | **105** | **45** |
| Inventory | 4,361 | 4,361 | 4,361 | 4,361 | 4,361 |
| Current Assets | 6,089 | 6,089 | 6,089 | 6,089 | 6,089 |
| Total Assets | 16,246 | 16,246 | 16,246 | 16,246 | 16,246 |
| Current Liabilities | 4,430 | 4,532 | — | **4,430** | **4,532** |
| Liabilities | 12,109 | 12,211 | — | **12,109** | **12,211** |
| TSE | 4,137 | 4,035 | 4,035 | **4,137** | **4,035** |
| Total L+SE | 16,246 | 16,246 | 16,246 | 16,246 | 16,246 |

### Reconciled Recommendation
- Net Revenue: **no change** (23,866)
- **COGS: 14,143 → 14,224** [WARNING — restatement +81K per FY2024 10-K]
- **Gross Margin: 9,723 → 9,642** (derived: 23,866 − 14,224)
- SGA: **no change** (8,375)
- **Operating Profit: 382 → 301** [WARNING — restatement −81K per FY2024 10-K]
- **Net Profit: 105 → 45** [WARNING — restatement −60K per FY2024 10-K]
- Current Assets, Total Assets, Total L+SE: **no change**
- **Current Liabilities: 4,430 → 4,532** [WARNING — balance sheet restatement +102K per FY2024 10-K]
- **Liabilities: 12,109 → 12,211** (derived: 16,246 − 4,035)
- **TSE: 4,137 → 4,035** [WARNING — balance sheet restatement −102K per FY2024 10-K]

---

## FY2024 — reportDate 2025-02-01

**Sources used:** Dolt DB; FY2024 primary 10-K (fetched from SEC); Yahoo Finance (2025-01-31 column).

### Anomaly Detection
- [ERROR] Net Revenue uses Contract Revenue only: SEC shows us-gaap_Revenues = 23,006K = Contract Revenue 22,293K + Other Revenue 713K (CC 537K + MMN 176K). Dolt stores 22,293K (contract only), missing Other Revenue 713K.
- [ERROR] Gross Margin derived from wrong revenue: Dolt Gross Margin = 8,553K (22,293 − 13,740); correct = 9,266K (23,006 − 13,740).
- Gross Margin (corrected): 9,266 / 23,006 = 40.3% ✓ (was 38.4% from wrong revenue)
- Balance sheet identity: 16,402 = 16,402 ✓. All balance sheet fields verified against primary FY2024 10-K. ✓
- SGA (8,330K): SEC = Yahoo = Dolt ✓
- Operating Profit (909K): Consistent with corrected revenue structure ✓

### Side-by-Side Comparison

| Field | SEC (FY2024 primary) | Yahoo | Dolt | Recommended |
|-------|---------------------|-------|------|-------------|
| Net Revenue | 23,006 | 23,006 | **22,293** | **23,006** |
| COGS | 13,740 | 13,740 | 13,740 | 13,740 |
| Gross Margin | 9,266 | 9,266 | **8,553** | **9,266** |
| SGA | 8,330 | 8,330 | 8,330 | 8,330 |
| Operating Profit | 909 | 909 | 909 | 909 |
| Net Profit | 582 | 582 | 582 | 582 |
| Inventory | 4,468 | 4,468 | 4,468 | 4,468 |
| Current Assets | 6,479 | 6,479 | 6,479 | 6,479 |
| Total Assets | 16,402 | 16,402 | 16,402 | 16,402 |
| Current Liabilities | 4,524 | 4,524 | 4,524 | 4,524 |
| Liabilities | 11,850 | 11,850 | 11,850 | 11,850 |
| TSE | 4,552 | 4,552 | 4,552 | 4,552 |
| Total L+SE | 16,402 | 16,402 | 16,402 | 16,402 |

### Reconciled Recommendation
- **Net Revenue: 22,293 → 23,006** [ERROR — contract only; add Other Revenue 713K: CC 537K + MMN 176K per FY2024 10-K us-gaap_Revenues]
- **Gross Margin: 8,553 → 9,266** (derived: 23,006 − 13,740)
- All other fields: **no change**

---

## FY2025 — reportDate 2026-01-31

**Sources used:** Dolt DB; Yahoo Finance (2026-01-31 column). SEC FY2025 10-K not independently fetched.

### Anomaly Detection
- Gross Margin: 9,124 / 22,621 = 40.3% ✓
- Balance sheet identity: 16,238 = 16,238 ✓
- Revenue structure (Yahoo): Total Revenue 22,621K vs. Operating Revenue 21,764K. The 857K difference = Other Revenue (CC + MMN). Dolt uses 22,621K matching us-gaap_Revenues convention. ✓
- All 13 fields match Yahoo exactly. ✓

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | 22,621 | 22,621 | 22,621 |
| COGS | — | 13,497 | 13,497 | 13,497 |
| Gross Margin | — | 9,124 | 9,124 | 9,124 |
| SGA | — | 8,240 | 8,240 | 8,240 |
| Operating Profit | — | 1,030 | 1,030 | 1,030 |
| Net Profit | — | 642 | 642 | 642 |
| Inventory | — | 4,412 | 4,412 | 4,412 |
| Current Assets | — | 6,673 | 6,673 | 6,673 |
| Total Assets | — | 16,238 | 16,238 | 16,238 |
| Current Liabilities | — | 4,493 | 4,493 | 4,493 |
| Liabilities | — | 11,378 | 11,378 | 11,378 |
| TSE | — | 4,860 | 4,860 | 4,860 |
| Total L+SE | — | 16,238 | 16,238 | 16,238 |

### Reconciled Recommendation
**No change.** All fields match Yahoo. Recommend independent SEC verification before final insert.

---

## Unresolved Flags

1. **FY2018/FY2019** — Revenue convention (Contract-only vs. Contract+CC) not verified against original primary 10-Ks. The FY2021 10-K comparative shows FY2019 with CC 771K as a revenue line item. If the original FY2019 10-K used the same convention, Dolt FY2019 (24,560K) is missing 771K. Recommend re-running `/verify-dolt-db-financials M 2019` and `/verify-dolt-db-financials M 2018` with dedicated SEC fetches.

2. **FY2020 gross margin (32.1%)** — Below Department Stores benchmark; flagged [WARNING] but expected due to COVID-19. No correction needed.

3. **FY2025 SEC** — Not independently verified against SEC 10-K. Yahoo match provides high confidence, but a dedicated SEC fetch is recommended.

---

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql M` to write all changed years to the database.
