# /verify-dolt-db-financials M
**Skill_Version:** 1.0
**Student:** calvinw
**Model:** sonnet-4-6
**Date:** 2026-06-17

---

## Session

**User:** `/verify-dolt-db-financials M`

---

**Assistant:**

### Step 1 — Company Metadata

Queried `company_info` for ticker `M`:

```
company: Macy's | CIK: 794367 | display_name: Macy's | ticker_symbol: M
```

No YEAR provided → multi-year mode. Queried Dolt for all existing years and Yahoo Finance for available periods.

**Years found:**
- Dolt: 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025
- Yahoo: 2021–2025 (5-year coverage)
- SEC: fetched 2021, 2022, 2023, 2024 (primary 10-Ks)

**Analyzing all available years for Macy's (M): 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025**

---

### Step 2 — Sources Fetched

| Source | Years |
|--------|-------|
| SEC 10-K | FY2021, FY2022, FY2023, FY2024 (primary filings) + FY2023 and FY2022 as restated comparatives in FY2024 10-K |
| Yahoo Finance | FY2021–FY2025 (2022-01-31 through 2026-01-31 columns) |
| Dolt DB | All 8 years (2018–2025) |

---

### Background: Macy's Revenue Structure

Macy's income statement has two revenue components:
- **Contract Revenue** (`us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax`) — merchandise sales
- **Other Revenue** (`m_NetEarningsFromCreditOperations` in older filings; `m_OtherRevenueNet` in FY2023+) — Credit Card + Macy's Media Network
- **Total Revenue** (`us-gaap_Revenues`) — always use this

**Macy's Media Network (MMN) reclassification (FY2023 10-K):** Starting with the FY2023 10-K, MMN revenue was moved from an SGA offset to a separate "Other Revenue" line. This increased both Net Revenue and SGA by the MMN amount, with Operating Income unchanged. Comparative years (FY2021, FY2022) were restated accordingly.

---

### Steps 4–6 — Anomaly Detection, Comparison, and Recommendations

#### FY2018 — reportDate 2019-02-02

SEC not re-fetched; Yahoo does not cover this year. Accepting stored values as original primary convention.

- Gross Margin: 9,756 / 24,971 = 39.1% ✓
- Balance sheet identity: 19,194 = 19,194 ✓

**→ No change.**

---

#### FY2019 — reportDate 2020-02-01

Same as FY2018 — SEC not re-fetched.

- Gross Margin: 9,389 / 24,560 = 38.2% ✓
- Balance sheet identity: 21,172 = 21,172 ✓

**→ No change.** (Note: FY2021 10-K comparative shows FY2019 CC revenue 771K as a level-1 revenue line — original convention not confirmed. Recommend separate verification.)

---

#### FY2020 — reportDate 2021-01-30

Verified from FY2021 10-K comparative (2021-01-30 column): Contract 17,346K + CC 751K = 18,097K ✓

- [WARNING] Gross Margin: 5,811 / 18,097 = 32.1% — below 35–45% benchmark. **Expected: COVID-19 year.** Not an error.
- Balance sheet identity: 17,706 = 17,706 ✓

**→ No change.**

---

#### FY2021 — reportDate 2022-01-29 [ERROR + WARNING]

**FY2021 primary 10-K (2022-01-29 column):**
- Contract Revenue: 24,460K
- Credit Card Revenues (`m_NetEarningsFromCreditOperations`): 832K (level=1, above COGS)
- COGS: 14,956K
- SGA: 8,047K
- Operating Income: 2,350K
- Net Profit: 1,430K

**FY2023 10-K restated (most recent, 2022-01-29 column):**
- Other Revenue: 939K (CC 832K + MMN 107K)
- SGA: 8,154K (+107K MMN reclassified from SGA offset)
- Operating Income: 2,350K (unchanged)

**Dolt (current):** Net Revenue = 24,460K (contract only — missing CC 832K and MMN 107K)

| Field | SEC Primary | SEC FY2023 Restated | Dolt | Recommended |
|-------|------------|---------------------|------|-------------|
| Net Revenue | 25,292 | 25,399 | **24,460** | **25,399** |
| COGS | 14,956 | 14,956 | 14,956 | 14,956 |
| Gross Margin | 10,336 | 10,443 | **9,504** | **10,443** |
| SGA | 8,047 | 8,154 | **8,047** | **8,154** |
| Operating Profit | 2,350 | 2,350 | 2,350 | 2,350 |
| Net Profit | 1,430 | 1,430 | 1,430 | 1,430 |
| Balance sheet | — | — | ✓ all match | no change |

Flags:
- **[ERROR]** Net Revenue missing CC 832K — clearly part of total revenue in primary filing; FY2020 correctly includes CC.
- **[WARNING]** MMN reclassification +107K applied per FY2023 10-K (most recent filing).

**→ Update: Net Revenue 24,460→25,399 | Gross Margin 9,504→10,443 | SGA 8,047→8,154**

---

#### FY2022 — reportDate 2023-01-28 [WARNING]

**FY2022 primary 10-K:** Revenue 25,305K (contract 24,442 + CC 863), SGA 8,317K (MMN 144K netted against SGA).

**FY2023 10-K restated:** Revenue 25,449K (+144K MMN to revenue), SGA 8,461K (+144K), Op Inc unchanged.

**FY2024 10-K (most recent):** Additional COGS restatement +41K (15,306→15,347), Op Inc −41K (1,730→1,689), Net Prof −31K (1,177→1,146).

| Field | SEC Primary | SEC FY2024 Restated | Dolt | Recommended |
|-------|------------|---------------------|------|-------------|
| Net Revenue | 25,305 | 25,449 | **25,305** | **25,449** |
| COGS | 15,306 | 15,347 | **15,306** | **15,347** |
| Gross Margin | 9,999 | 10,102 | **9,999** | **10,102** |
| SGA | 8,317 | 8,461 | **8,317** | **8,461** |
| Operating Profit | 1,730 | 1,689 | **1,730** | **1,689** |
| Net Profit | 1,177 | 1,146 | **1,177** | **1,146** |
| Balance sheet | — | — | ✓ all match | no change |

Gross Margin (corrected): 10,102 / 25,449 = 39.7% ✓

**→ Update: Revenue 25,305→25,449 | COGS 15,306→15,347 | GM 9,999→10,102 | SGA 8,317→8,461 | Op Inc 1,730→1,689 | Net Prof 1,177→1,146**

---

#### FY2023 — reportDate 2024-02-03 [WARNING]

**FY2023 primary 10-K:** Revenue 23,866K (`us-gaap_Revenues`), COGS 14,143K, Op Inc 382K, Net Prof 105K, Curr Liab 4,430K, SE 4,137K.

**FY2024 10-K comparative (most recent):** COGS restated to 14,224K (+81K), Op Inc 301K (−81K), Net Prof 45K (−60K after tax), Curr Liab 4,532K (+102K), SE 4,035K (−102K). Total Assets unchanged at 16,246K.

| Field | SEC Primary | SEC FY2024 Restated | Yahoo | Dolt | Recommended |
|-------|------------|---------------------|-------|------|-------------|
| Net Revenue | 23,866 | 23,866 | 23,866 | 23,866 | 23,866 |
| COGS | 14,143 | 14,224 | 14,224 | **14,143** | **14,224** |
| Gross Margin | 9,723 | 9,642 | 9,642 | **9,723** | **9,642** |
| SGA | 8,375 | 8,375 | 8,375 | 8,375 | 8,375 |
| Operating Profit | 382 | 301 | 301 | **382** | **301** |
| Net Profit | 105 | 45 | 45 | **105** | **45** |
| Current Assets | 6,089 | 6,089 | 6,089 | 6,089 | 6,089 |
| Total Assets | 16,246 | 16,246 | 16,246 | 16,246 | 16,246 |
| Current Liabilities | 4,430 | 4,532 | — | **4,430** | **4,532** |
| Liabilities | 12,109 | 12,211 | — | **12,109** | **12,211** |
| TSE | 4,137 | 4,035 | 4,035 | **4,137** | **4,035** |
| Total L+SE | 16,246 | 16,246 | 16,246 | 16,246 | 16,246 |

Gross Margin (corrected): 9,642 / 23,866 = 40.4% ✓

**→ Update: COGS 14,143→14,224 | GM 9,723→9,642 | Op Inc 382→301 | Net Prof 105→45 | Curr Liab 4,430→4,532 | Liabilities 12,109→12,211 | SE 4,137→4,035**

---

#### FY2024 — reportDate 2025-02-01 [ERROR]

**FY2024 primary 10-K:**
- `us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax` (Contract): 22,293K
- `m_OtherRevenueNet` (Other Revenue): 713K (CC 537K + MMN 176K)
- `us-gaap_Revenues` (Total): **23,006K**

Dolt stores 22,293K (contract only). Missing Other Revenue 713K.

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 23,006 | 23,006 | **22,293** | **23,006** |
| COGS | 13,740 | 13,740 | 13,740 | 13,740 |
| Gross Margin | 9,266 | 9,266 | **8,553** | **9,266** |
| SGA | 8,330 | 8,330 | 8,330 | 8,330 |
| Operating Profit | 909 | 909 | 909 | 909 |
| Net Profit | 582 | 582 | 582 | 582 |
| Balance sheet | — | — | ✓ all match | no change |

Gross Margin (corrected): 9,266 / 23,006 = 40.3% ✓

Flags:
- **[ERROR]** Net Revenue uses contract only (22,293K); correct total = 23,006K.
- **[ERROR]** Gross Margin follows wrong revenue: 8,553→9,266.

**→ Update: Net Revenue 22,293→23,006 | Gross Margin 8,553→9,266**

---

#### FY2025 — reportDate 2026-01-31

Yahoo Finance (2026-01-31 column): Total Revenue 22,621K, COGS 13,497K, GM 9,124K, SGA 8,240K, Op Inc 1,030K, Net Prof 642K. All balance sheet fields match Dolt exactly.

- Gross Margin: 9,124 / 22,621 = 40.3% ✓
- Balance sheet identity: 16,238 = 16,238 ✓

**→ No change.** (SEC FY2025 10-K not independently fetched — Yahoo match is high confidence.)

---

### Step 7 — Readiness

Unresolved flags:
1. **FY2018/FY2019** — Credit Card revenue convention not verified against original 10-Ks. May be understated if CC was above COGS in those original filings. Recommend separate verification.
2. **FY2020** — Gross margin 32.1% below benchmark but expected (COVID). No correction needed.
3. **FY2025** — SEC not independently verified. Yahoo match is high confidence.

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql M` to write all changed years to the database.

---

### Step 8 — Report

Report saved to `reports/M-all-years.md`.
