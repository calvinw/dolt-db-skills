# Ulta Beauty (ULTA) — FY2018–2025 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2019-02-02 | No change |
| 2019 | 2020-02-01 | No change |
| 2020 | 2021-01-30 | No change |
| 2021 | 2022-01-29 | No change |
| 2022 | 2023-01-28 | No change |
| 2023 | 2024-02-03 | No change |
| 2024 | 2025-02-01 | No change |
| 2025 | 2026-01-31 | New insert |

---

## Company Metadata

- **Ticker:** ULTA
- **CIK:** 1403568
- **Company name in DB:** Ulta Beauty
- **Segment:** Specialty (beauty/cosmetics)
- **Fiscal year:** 52/53-week year ending Saturday nearest to January 31
- **No company-specific entry in company-notes.md** — generic rules applied

---

## SGA Construction Notes (all years)

Ulta Beauty reports a single `us-gaap_SellingGeneralAndAdministrativeExpense` line. A separate `us-gaap_PreOpeningCosts` line also appears on the income statement but is NOT part of SGA — it is its own operating expense line.

- Rule 1 (SGA + Marketing): Does not apply — no separate marketing tag
- Rule 2 (Exclude ops-tech): Does not apply
- Rule 3 (Yahoo SGA ≈ Total OpEx): Does not trigger — Yahoo SGA matches SEC SGA exactly; the $15–20K discrepancy is the pre-opening line
- Rule 4 (G&A + Selling): Does not apply — combined SGA tag exists

**Yahoo Operating Income note:** Yahoo consistently calculates Operating Income as Gross Profit − SGA only, ignoring pre-opening costs. This inflates Yahoo's Operating Profit vs. GAAP by the pre-opening amount each year (~$9K–$20K). **Always use SEC for Operating Profit.**

**SGA = `us-gaap_SellingGeneralAndAdministrativeExpense` directly for all years. Pre-opening costs are correctly excluded.**

---

## Gross Margin Benchmark

Expected for specialty retail (beauty): 35–55%. Ulta runs 35–40%. FY2020 is an exception (~31.7%) due to COVID store closures — not a data error.

---

## FY2018 Analysis

**reportDate:** 2019-02-02

### Source Data

| Field | SEC | Yahoo | Dolt (current) |
|-------|-----|-------|----------------|
| Net Revenue | 6,716,615 | N/A | 6,716,615 |
| Cost of Goods | 4,307,304 | N/A | 4,307,304 |
| Gross Margin | 2,409,311 | N/A | 2,409,311 |
| SGA | 1,535,464 | N/A | 1,535,464 |
| Operating Profit | 854,080 | N/A | 854,080 |
| Net Profit | 658,559 | N/A | 658,559 |
| Inventory | 1,214,329 | N/A | 1,214,329 |
| Current Assets | 1,914,861 | N/A | 1,914,861 |
| Total Assets | 3,191,172 | N/A | 3,191,172 |
| Current Liabilities | 823,736 | N/A | 823,736 |
| Liabilities | 1,370,954 | N/A | 1,370,954 |
| Total Shareholder Equity | 1,820,218 | N/A | 1,820,218 |
| TL&SE | 3,191,172 | N/A | 3,191,172 |

(Yahoo does not carry ULTA data before FY2022.)

### Anomaly Checks

- Gross margin: 2,409,311 / 6,716,615 = **35.9%** ✓ within specialty range
- Balance sheet identity: 1,370,954 + 1,820,218 = 3,191,172 ✓
- FY2018 10-K has pre-opening costs $19,767K as a separate line — correctly excluded from SGA ✓

### Reconciled Recommendation

All fields match SEC exactly. **No change needed.**

---

## FY2019 Analysis

**reportDate:** 2020-02-01

### Source Data

| Field | SEC | Yahoo | Dolt (current) |
|-------|-----|-------|----------------|
| Net Revenue | 7,398,068 | N/A | 7,398,068 |
| Cost of Goods | 4,717,004 | N/A | 4,717,004 |
| Gross Margin | 2,681,064 | N/A | 2,681,064 |
| SGA | 1,760,716 | N/A | 1,760,716 |
| Operating Profit | 901,094 | N/A | 901,094 |
| Net Profit | 705,945 | N/A | 705,945 |
| Inventory | 1,293,701 | N/A | 1,293,701 |
| Current Assets | 2,055,317 | N/A | 2,055,317 |
| Total Assets | 4,863,872 | N/A | 4,863,872 |
| Current Liabilities | 1,137,261 | N/A | 1,137,261 |
| Liabilities | 2,961,778 | N/A | 2,961,778 |
| Total Shareholder Equity | 1,902,094 | N/A | 1,902,094 |
| TL&SE | 4,863,872 | N/A | 4,863,872 |

### Anomaly Checks

- Gross margin: 2,681,064 / 7,398,068 = **36.2%** ✓
- Total Assets jumped from $3.19B (FY2018) to $4.86B (FY2019): caused by ASC 842 adoption — operating lease ROU assets ($1.54B) added to balance sheet. Not an error; structural one-time change.
- Balance sheet identity: 2,961,778 + 1,902,094 = 4,863,872 ✓

### Reconciled Recommendation

All fields match SEC exactly. **No change needed.**

---

## FY2020 Analysis

**reportDate:** 2021-01-30

### Source Data

| Field | SEC | Yahoo | Dolt (current) |
|-------|-----|-------|----------------|
| Net Revenue | 6,151,953 | N/A | 6,151,953 |
| Cost of Goods | 4,202,794 | N/A | 4,202,794 |
| Gross Margin | 1,949,159 | N/A | 1,949,159 |
| SGA | 1,583,017 | N/A | 1,583,017 |
| Operating Profit | 236,820 | N/A | 236,820 |
| Net Profit | 175,835 | N/A | 175,835 |
| Inventory | 1,168,215 | N/A | 1,168,215 |
| Current Assets | 2,514,777 | N/A | 2,514,777 |
| Total Assets | 5,089,969 | N/A | 5,089,969 |
| Current Liabilities | 1,343,713 | N/A | 1,343,713 |
| Liabilities | 3,090,420 | N/A | 3,090,420 |
| Total Shareholder Equity | 1,999,549 | N/A | 1,999,549 |
| TL&SE | 5,089,969 | N/A | 5,089,969 |

### Anomaly Checks

- Gross margin: 1,949,159 / 6,151,953 = **31.7%** — [NOTE] below specialty floor of 35%. Expected: COVID-19 forced store closures reduced revenue while fixed costs remained. Not a data error.
- FY2020 10-K includes a $114,322K "Impairment, restructuring and other costs" line (`us-gaap_RestructuringSettlementAndImpairmentProvisions`). Per anomaly rules, restructuring charges are excluded from SGA. Dolt SGA ($1,583,017K) = SEC SGA label only — correctly excludes restructuring ✓
- Balance sheet identity: 3,090,420 + 1,999,549 = 5,089,969 ✓

### Reconciled Recommendation

All fields match SEC exactly. **No change needed.**

---

## FY2021 Analysis

**reportDate:** 2022-01-29

### Source Data

| Field | SEC | Yahoo | Dolt (current) |
|-------|-----|-------|----------------|
| Net Revenue | 8,630,889 | N/A | 8,630,889 |
| Cost of Goods | 5,262,335 | N/A | 5,262,335 |
| Gross Margin | 3,368,554 | N/A | 3,368,554 |
| SGA | 2,061,545 | N/A | 2,061,545 |
| Operating Profit | 1,297,492 | N/A | 1,297,492 |
| Net Profit | 985,837 | N/A | 985,837 |
| Inventory | 1,499,218 | N/A | 1,499,218 |
| Current Assets | 2,281,183 | N/A | 2,281,183 |
| Total Assets | 4,764,379 | N/A | 4,764,379 |
| Current Liabilities | 1,558,010 | N/A | 1,558,010 |
| Liabilities | 3,229,006 | N/A | 3,229,006 |
| Total Shareholder Equity | 1,535,373 | N/A | 1,535,373 |
| TL&SE | 4,764,379 | N/A | 4,764,379 |

### Anomaly Checks

- Gross margin: 3,368,554 / 8,630,889 = **39.0%** ✓ Post-COVID recovery
- Balance sheet identity: 3,229,006 + 1,535,373 = 4,764,379 ✓

### Reconciled Recommendation

All fields match SEC exactly. **No change needed.**

---

## FY2022 Analysis

**reportDate:** 2023-01-28

### Source Data

| Field | SEC | Yahoo | Dolt (current) |
|-------|-----|-------|----------------|
| Net Revenue | 10,208,580 | 10,208,600 | 10,208,580 |
| Cost of Goods | 6,164,070 | 6,164,070 | 6,164,070 |
| Gross Margin | 4,044,510 | 4,044,530 | 4,044,510 |
| SGA | 2,395,299 | 2,395,300 | 2,395,299 |
| Operating Profit | 1,638,610 | 1,649,210* | 1,638,610 |
| Net Profit | 1,242,408 | 1,242,410 | 1,242,408 |
| Inventory | 1,603,451 | N/A | 1,603,451 |
| Current Assets | 2,709,304 | N/A | 2,709,304 |
| Total Assets | 5,370,411 | N/A | 5,370,411 |
| Current Liabilities | 1,681,775 | N/A | 1,681,775 |
| Liabilities | 3,410,600 | N/A | 3,410,600 |
| Total Shareholder Equity | 1,959,811 | N/A | 1,959,811 |
| TL&SE | 5,370,411 | N/A | 5,370,411 |

`*` Yahoo Operating Profit overstates by ~$10,601K (pre-opening costs excluded from Yahoo's OpInc calculation). Use SEC.

### Anomaly Checks

- Gross margin: 4,044,510 / 10,208,580 = **39.6%** ✓
- Yahoo Operating Profit: $1,649,210K vs SEC $1,638,610K. Difference = $10,601K = pre-opening costs for FY2022. Yahoo artifact, not an error in Dolt ✓
- Balance sheet identity: 3,410,600 + 1,959,811 = 5,370,411 ✓

### Reconciled Recommendation

All fields match SEC exactly. **No change needed.**

---

## FY2023 Analysis

**reportDate:** 2024-02-03

### Source Data

| Field | SEC | Yahoo | Dolt (current) |
|-------|-----|-------|----------------|
| Net Revenue | 11,207,303 | 11,207,300 | 11,207,303 |
| Cost of Goods | 6,826,203 | 6,826,200 | 6,826,203 |
| Gross Margin | 4,381,100 | 4,381,100 | 4,381,100 |
| SGA | 2,694,561 | 2,694,560 | 2,694,561 |
| Operating Profit | 1,678,029 | 1,686,540* | 1,678,029 |
| Net Profit | 1,291,005 | 1,291,000 | 1,291,005 |
| Inventory | 1,742,136 | N/A | 1,742,136 |
| Current Assets | 2,836,518 | N/A | 2,836,518 |
| Total Assets | 5,707,011 | N/A | 5,707,011 |
| Current Liabilities | 1,658,191 | N/A | 1,658,191 |
| Liabilities | 3,427,683 | N/A | 3,427,683 |
| Total Shareholder Equity | 2,279,328 | N/A | 2,279,328 |
| TL&SE | 5,707,011 | N/A | 5,707,011 |

`*` Yahoo Operating Profit overstates by ~$8,510K (pre-opening costs). Use SEC.

### Anomaly Checks

- Gross margin: 4,381,100 / 11,207,303 = **39.1%** ✓
- Balance sheet identity: 3,427,683 + 2,279,328 = 5,707,011 ✓
- FY2024 10-K comparative shows FY2023 SGA = $2,694,561K — unchanged from FY2023 10-K ✓ No restatement.

### Reconciled Recommendation

All fields match SEC exactly. **No change needed.**

---

## FY2024 Analysis

**reportDate:** 2025-02-01

### Source Data

| Field | SEC | Yahoo | Dolt (current) |
|-------|-----|-------|----------------|
| Net Revenue | 11,295,654 | 11,295,700 | 11,295,654 |
| Cost of Goods | 6,908,401 | 6,908,400 | 6,908,401 |
| Gross Margin | 4,387,253 | 4,387,300 | 4,387,253 |
| SGA | 2,808,592 | 2,808,590 | 2,808,592 |
| Operating Profit | 1,564,972 | 1,578,660* | 1,564,972 |
| Net Profit | 1,201,118 | 1,201,120 | 1,201,118 |
| Inventory | 1,968,214 | N/A | 1,968,214 |
| Current Assets | 3,028,808 | N/A | 3,028,808 |
| Total Assets | 6,001,693 | N/A | 6,001,693 |
| Current Liabilities | 1,779,478 | N/A | 1,779,478 |
| Liabilities | 3,513,340 | N/A | 3,513,340 |
| Total Shareholder Equity | 2,488,353 | N/A | 2,488,353 |
| TL&SE | 6,001,693 | N/A | 6,001,693 |

`*` Yahoo Operating Profit overstates by ~$13,689K (pre-opening costs). Use SEC.

### Anomaly Checks

- Gross margin: 4,387,253 / 11,295,654 = **38.8%** ✓
- Balance sheet identity: 3,513,340 + 2,488,353 = 6,001,693 ✓
- FY2025 10-K comparative shows FY2024 SGA = $2,808,592K — unchanged ✓ No restatement.

### Reconciled Recommendation

All fields match SEC exactly. **No change needed.**

---

## FY2025 Analysis

**reportDate:** 2026-01-31 (fiscal year-end per 2025 10-K income statement and balance sheet headers)

Not yet in Dolt DB — new insert required.

### Source Data

| Field | SEC | Yahoo | Recommended |
|-------|-----|-------|-------------|
| Net Revenue | 12,392,820 | 12,392,800 | **12,392,820** |
| Cost of Goods | 7,547,596 | 7,547,600 | **7,547,596** |
| Gross Margin | 4,845,224 | 4,845,200 | **4,845,224** |
| SGA | 3,296,411 | 3,296,410 | **3,296,411** |
| Operating Profit | 1,532,992 | 1,548,810* | **1,532,992** |
| Net Profit | 1,153,479 | 1,153,480 | **1,153,479** |
| Inventory | 2,181,127 | 2,181,130 | **2,181,127** |
| Current Assets | 3,144,146 | 3,144,150 | **3,144,146** |
| Total Assets | 6,999,294 | 6,999,290 | **6,999,294** |
| Current Liabilities | 2,224,342 | 2,224,340 | **2,224,342** |
| Liabilities | 4,195,843 | N/A (calc) | **4,195,843** |
| Total Shareholder Equity | 2,803,451 | 2,803,450 | **2,803,451** |
| TL&SE | 6,999,294 | 6,999,290 | **6,999,294** |

`*` Yahoo Operating Profit $1,548,810K excludes pre-opening costs ($15,821K). GAAP Operating Income per SEC = $1,532,992K. Use SEC.

### Anomaly Checks

- Gross margin: 4,845,224 / 12,392,820 = **39.1%** ✓
- Balance sheet identity: Liabilities $4,195,843 + TSE $2,803,451 = $6,999,294 = Total Assets ✓
- Derived Liabilities: $6,999,294 − $2,803,451 = $4,195,843 = SEC Total Liabilities ✓
- Yahoo SGA Rule 3 check: Yahoo SGA ($3,296,410K) = SEC SGA ($3,296,411K). Yahoo Operating Expense ($3,296,410K) ≠ SEC Total Operating Expenses ($3,296,411K + $15,821K = $3,312,232K). Rule 3 does NOT trigger — Yahoo SGA is accurate; the discrepancy is in Operating Income only.
- FY2025 10-K introduces a new income line: `us-gaap_IncomeLossFromEquityMethodInvestments` = −$3,857K (equity net loss of affiliate). This appears below Operating Income. Net Income ($1,153,479K) already includes this correctly as: Income before equity loss ($1,157,336K) + equity loss (−$3,857K) = $1,153,479K ✓
- No separate marketing line, no ops-tech line. SGA construction is straightforward.

### Reconciled Recommendation

| Field | Recommended | Source |
|-------|-------------|--------|
| reportDate | 2026-01-31 | SEC 2025 10-K |
| Net Revenue | 12,392,820 | SEC |
| Cost of Goods | 7,547,596 | SEC |
| Gross Margin | 4,845,224 | Calculated |
| SGA | 3,296,411 | SEC |
| Operating Profit | 1,532,992 | SEC (not Yahoo — pre-opening excluded from Yahoo's calc) |
| Net Profit | 1,153,479 | SEC |
| Inventory | 2,181,127 | SEC |
| Current Assets | 3,144,146 | SEC |
| Total Assets | 6,999,294 | SEC |
| Current Liabilities | 2,224,342 | SEC |
| Liabilities | 4,195,843 | Calculated |
| Total Shareholder Equity | 2,803,451 | SEC |
| TL&SE | 6,999,294 | SEC |

**Action: New insert**

---

## Analysis Complete

**1 year requires action:**
- **FY2025** — New insert (SEC 2025 10-K; Yahoo agrees on all fields except Operating Profit — use SEC $1,532,992K)

FY2018–FY2024 all verified against SEC: no changes needed.

Run `/create-verified-dolt-db-financials-sql ULTA` to write the new year to the database.
