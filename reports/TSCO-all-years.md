# Tractor Supply (TSCO) — FY2018–2025 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2018-12-29 | No change |
| 2019 | 2019-12-28 | No change |
| 2020 | 2020-12-26 | Correction: Revenue $116,370K → $10,620,352K; Gross Margin −$6,742,433K → $3,761,549K |
| 2021 | 2021-12-25 | No change |
| 2022 | 2022-12-31 | No change |
| 2023 | 2023-12-30 | No change |
| 2024 | 2024-12-28 | Correction: reportDate '2024-12-31' → '2024-12-28' |
| 2025 | 2025-12-27 | New insert |

---

## Company Metadata

- **Ticker:** TSCO
- **CIK:** 916365
- **Company name in DB:** Tractor Supply
- **Segment:** Specialty (farm/ranch supply)
- **Fiscal year:** 52/53-week year ending last Saturday of December
- **No company-specific entry in company-notes.md** — generic rules applied

---

## SGA Construction Notes (all years)

Tractor Supply reports a single `us-gaap_SellingGeneralAndAdministrativeExpense` line. No separate `us-gaap_MarketingExpense`. No platform/ops-tech line. D&A is reported as a separate operating expense line and is **not** included in SGA.

- Rule 1 (SGA + Marketing): Does not apply — no separate marketing line
- Rule 2 (Exclude ops-tech): Does not apply
- Rule 3 (Yahoo SGA = Total OpEx): Does not trigger — Yahoo SGA ≠ Yahoo Operating Expense (D&A is additive)
- Rule 4 (G&A + Selling): Does not apply — combined SGA tag exists

**Conclusion:** SGA = `us-gaap_SellingGeneralAndAdministrativeExpense` directly for all years.

---

## Gross Margin Benchmark

Expected for specialty retail: 35–55%. TSCO is a farm/ranch supply retailer with relatively lower merchandise margins than apparel/beauty specialty. Observed range ~34–36% across all years — consistent and logical for this subsegment. Values at or slightly below the 35% lower bound are expected for TSCO specifically; not flagged as error.

---

## FY2018 Analysis

**reportDate:** 2018-12-29 (fiscal year-end per SEC 10-K header)

### Source Data

| Field | SEC | Yahoo | Dolt (current) |
|-------|-----|-------|----------------|
| Net Revenue | 7,911,046 | N/A | 7,911,046 |
| Cost of Goods | 5,208,518 | N/A | 5,208,518 |
| Gross Margin | 2,702,528 | N/A | 2,702,528 |
| SGA | 1,823,440 | N/A | 1,823,440 |
| Operating Profit | 701,737 | N/A | 701,737 |
| Net Profit | 532,357 | N/A | 532,357 |
| Inventory | 1,589,542 | N/A | 1,589,542 |
| Current Assets | 1,794,399 | N/A | 1,794,399 |
| Total Assets | 3,085,262 | N/A | 3,085,262 |
| Current Liabilities | 938,107 | N/A | 938,107 |
| Liabilities | 1,523,442 | N/A | 1,523,442 |
| Total Shareholder Equity | 1,561,820 | N/A | 1,561,820 |
| TL&SE | 3,085,262 | N/A | 3,085,262 |

(Yahoo Finance does not carry TSCO data before FY2022.)

### Anomaly Checks

- Gross margin: 2,702,528 / 7,911,046 = **34.2%** — slightly below specialty floor of 35%, but consistent with farm/ranch subsegment. No flag.
- Balance sheet identity: 1,523,442 + 1,561,820 = 3,085,262 = Total Assets ✓
- No negative equity, no impairments in SGA.

### Reconciled Recommendation

All 13 fields match SEC exactly. **No change needed.**

---

## FY2019 Analysis

**reportDate:** 2019-12-28 (fiscal year-end per SEC 10-K header)

### Source Data

| Field | SEC | Yahoo | Dolt (current) |
|-------|-----|-------|----------------|
| Net Revenue | 8,351,931 | N/A | 8,351,931 |
| Cost of Goods | 5,480,161 | N/A | 5,480,161 |
| Gross Margin | 2,871,770 | N/A | 2,871,770 |
| SGA | 1,932,572 | N/A | 1,932,572 |
| Operating Profit | 743,220 | N/A | 743,220 |
| Net Profit | 562,354 | N/A | 562,354 |
| Inventory | 1,602,781 | N/A | 1,602,781 |
| Current Assets | 1,787,887 | N/A | 1,787,887 |
| Total Assets | 5,289,268 | N/A | 5,289,268 |
| Current Liabilities | 1,247,600 | N/A | 1,247,600 |
| Liabilities | 3,722,145 | N/A | 3,722,145 |
| Total Shareholder Equity | 1,567,123 | N/A | 1,567,123 |
| TL&SE | 5,289,268 | N/A | 5,289,268 |

### Anomaly Checks

- Gross margin: 2,871,770 / 8,351,931 = **34.4%** — consistent with TSCO pattern.
- Total Assets jumped from $3.1B (2018) to $5.3B (2019): caused by ASC 842 adoption — operating lease right-of-use assets ($2.19B) added to balance sheet. Not an error; structural one-time change.
- Balance sheet identity: 3,722,145 + 1,567,123 = 5,289,268 ✓

### Reconciled Recommendation

All fields match SEC exactly. **No change needed.**

---

## FY2020 Analysis

**reportDate:** 2020-12-26 (fiscal year-end per SEC 10-K header)

### Source Data

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 10,620,352 | N/A | **116,370*** | **10,620,352** |
| Cost of Goods | 6,858,803 | N/A | 6,858,803 | 6,858,803 |
| Gross Margin | 3,761,549 | N/A | **−6,742,433*** | **3,761,549** |
| SGA | 2,478,524 | N/A | 2,478,524 | 2,478,524 |
| Operating Profit | 996,928 | N/A | 996,928 | 996,928 |
| Net Profit | 748,958 | N/A | 748,958 | 748,958 |
| Inventory | 1,783,270 | N/A | 1,783,270 | 1,783,270 |
| Current Assets | 3,258,685 | N/A | 3,258,685 | 3,258,685 |
| Total Assets | 7,049,116 | N/A | 7,049,116 | 7,049,116 |
| Current Liabilities | 1,743,798 | N/A | 1,743,798 | 1,743,798 |
| Liabilities | 5,125,276 | N/A | 5,125,276 | 5,125,276 |
| Total Shareholder Equity | 1,923,840 | N/A | 1,923,840 | 1,923,840 |
| TL&SE | 7,049,116 | N/A | 7,049,116 | 7,049,116 |

`*` = differs from SEC

### Anomaly Checks

- **[ERROR] Net Revenue: Dolt has $116,370K — this is the weighted average basic shares outstanding (116,370,000 shares → 116,370K in "thousands of shares"), not revenue.** SEC Revenue = $10,620,352K. A wrong field was entered.
- **[ERROR] Gross Margin: Dolt has −$6,742,433K** (derived from incorrect Revenue). Correct = $3,761,549K.
- Gross margin at correct values: 3,761,549 / 10,620,352 = **35.4%** ✓ within range.
- Note: FY2020 income statement also contains a goodwill/intangible impairment charge of $68,973K as a separate line (`us-gaap_GoodwillAndIntangibleAssetImpairment`). This is correctly NOT included in SGA per anomaly rules.
- Balance sheet identity: 5,125,276 + 1,923,840 = 7,049,116 ✓

### Reconciled Recommendation

| Field | Recommended | Source | Change? |
|-------|-------------|--------|---------|
| Net Revenue | **10,620,352** | SEC 2020 10-K | YES — was $116,370 |
| Cost of Goods | 6,858,803 | SEC 2020 10-K | No |
| Gross Margin | **3,761,549** | Calculated | YES — was −6,742,433 |
| SGA | 2,478,524 | SEC 2020 10-K | No |
| Operating Profit | 996,928 | SEC 2020 10-K | No |
| Net Profit | 748,958 | SEC 2020 10-K | No |
| Inventory | 1,783,270 | SEC 2020 10-K | No |
| Current Assets | 3,258,685 | SEC 2020 10-K | No |
| Total Assets | 7,049,116 | SEC 2020 10-K | No |
| Current Liabilities | 1,743,798 | SEC 2020 10-K | No |
| Liabilities | 5,125,276 | SEC 2020 10-K | No |
| Total Shareholder Equity | 1,923,840 | SEC 2020 10-K | No |
| TL&SE | 7,049,116 | SEC 2020 10-K | No |
| reportDate | 2020-12-26 | SEC 2020 10-K | No |

**Action: Correction — Revenue $116,370K → $10,620,352K; Gross Margin −$6,742,433K → $3,761,549K**

---

## FY2021 Analysis

**reportDate:** 2021-12-25 (fiscal year-end per SEC 10-K header)

### Source Data

| Field | SEC | Yahoo | Dolt (current) |
|-------|-----|-------|----------------|
| Net Revenue | 12,731,105 | N/A | 12,731,105 |
| Cost of Goods | 8,253,952 | N/A | 8,253,952 |
| Gross Margin | 4,477,153 | N/A | 4,477,153 |
| SGA | 2,900,297 | N/A | 2,900,297 |
| Operating Profit | 1,306,698 | N/A | 1,306,698 |
| Net Profit | 997,114 | N/A | 997,114 |
| Inventory | 2,191,192 | N/A | 2,191,192 |
| Current Assets | 3,250,440 | N/A | 3,250,440 |
| Total Assets | 7,767,467 | N/A | 7,767,467 |
| Current Liabilities | 2,064,842 | N/A | 2,064,842 |
| Liabilities | 5,764,802 | N/A | 5,764,802 |
| Total Shareholder Equity | 2,002,665 | N/A | 2,002,665 |
| TL&SE | 7,767,467 | N/A | 7,767,467 |

(Yahoo Finance does not carry TSCO data before FY2022.)

### Anomaly Checks

- Gross margin: 4,477,153 / 12,731,105 = **35.2%** ✓
- Balance sheet identity: 5,764,802 + 2,002,665 = 7,767,467 ✓
- No anomalies.

### Reconciled Recommendation

All fields match SEC exactly. **No change needed.**

---

## FY2022 Analysis

**reportDate:** 2022-12-31 (fiscal year-end per SEC 10-K header)

### Source Data

| Field | SEC | Yahoo | Dolt (current) |
|-------|-----|-------|----------------|
| Net Revenue | 14,204,717 | 14,204,700 | 14,204,717 |
| Cost of Goods | 9,232,513 | 9,232,510 | 9,232,513 |
| Gross Margin | 4,972,204 | 4,972,190 | 4,972,204 |
| SGA | 3,194,199 | 3,194,200 | 3,194,199 |
| Operating Profit | 1,434,943 | 1,434,940 | 1,434,943 |
| Net Profit | 1,088,712 | 1,088,710 | 1,088,712 |
| Inventory | 2,709,597 | N/A | 2,709,597 |
| Current Assets | 3,157,775 | N/A | 3,157,775 |
| Total Assets | 8,489,990 | N/A | 8,489,990 |
| Current Liabilities | 2,376,212 | N/A | 2,376,212 |
| Liabilities | 6,447,574 | N/A | 6,447,574 |
| Total Shareholder Equity | 2,042,416 | N/A | 2,042,416 |
| TL&SE | 8,489,990 | N/A | 8,489,990 |

Yahoo differences are rounding only (≤$10K). SEC is authoritative.

### Anomaly Checks

- Gross margin: 4,972,204 / 14,204,717 = **35.0%** ✓
- Balance sheet identity: 6,447,574 + 2,042,416 = 8,489,990 ✓
- Yahoo Rule 3 check: Yahoo SGA $3,194,200K ≠ Yahoo total operating expense ($3,194,200 + $343,062 D&A = ~$3,537,262). Rule 3 does not trigger.

### Reconciled Recommendation

All fields match SEC exactly (Yahoo rounding only). **No change needed.**

---

## FY2023 Analysis

**reportDate:** 2023-12-30 (fiscal year-end per SEC 10-K header)

### Source Data

| Field | SEC | Yahoo | Dolt (current) |
|-------|-----|-------|----------------|
| Net Revenue | 14,555,741 | 14,555,700 | 14,555,741 |
| Cost of Goods | 9,327,522 | 9,327,520 | 9,327,522 |
| Gross Margin | 5,228,219 | 5,228,180 | 5,228,219 |
| SGA | 3,356,258 | 3,356,260 | 3,356,258 |
| Operating Profit | 1,478,912 | 1,478,910 | 1,478,912 |
| Net Profit | 1,107,226 | 1,107,230 | 1,107,226 |
| Inventory | 2,645,854 | N/A | 2,645,854 |
| Current Assets | 3,263,939 | N/A | 3,263,939 |
| Total Assets | 9,188,151 | N/A | 9,188,151 |
| Current Liabilities | 2,177,082 | N/A | 2,177,082 |
| Liabilities | 7,038,389 | N/A | 7,038,389 |
| Total Shareholder Equity | 2,149,762 | N/A | 2,149,762 |
| TL&SE | 9,188,151 | N/A | 9,188,151 |

Yahoo differences are rounding only (≤$10K). SEC is authoritative.

### Anomaly Checks

- Gross margin: 5,228,219 / 14,555,741 = **35.9%** ✓
- Balance sheet identity: 7,038,389 + 2,149,762 = 9,188,151 ✓

### Reconciled Recommendation

All fields match SEC exactly. **No change needed.**

---

## FY2024 Analysis

**reportDate per SEC:** 2024-12-28 (fiscal year-end per 2024 10-K income statement and balance sheet headers)
**reportDate in Dolt:** 2024-12-31 ← INCORRECT

### Source Data

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| reportDate | 2024-12-28 | 2024-12-31 | **2024-12-31*** | **2024-12-28** |
| Net Revenue | 14,883,231 | 14,883,200 | 14,883,231 | 14,883,231 |
| Cost of Goods | 9,486,674 | 9,486,670 | 9,486,674 | 9,486,674 |
| Gross Margin | 5,396,557 | 5,396,530 | 5,396,557 | 5,396,557 |
| SGA | 3,481,863 | 3,481,860 | 3,481,863 | 3,481,863 |
| Operating Profit | 1,467,532 | 1,467,530 | 1,467,532 | 1,467,532 |
| Net Profit | 1,101,240 | 1,101,240 | 1,101,240 | 1,101,240 |
| Inventory | 2,840,177 | N/A | 2,840,177 | 2,840,177 |
| Current Assets | 3,309,917 | N/A | 3,309,917 | 3,309,917 |
| Total Assets | 9,805,485 | N/A | 9,805,485 | 9,805,485 |
| Current Liabilities | 2,319,193 | N/A | 2,319,193 | 2,319,193 |
| Liabilities | 7,535,151 | N/A | 7,535,151 | 7,535,151 |
| Total Shareholder Equity | 2,270,334 | N/A | 2,270,334 | 2,270,334 |
| TL&SE | 9,805,485 | N/A | 9,805,485 | 9,805,485 |

`*` = differs from SEC

### Anomaly Checks

- **[WARNING] reportDate: Dolt has '2024-12-31' but the actual fiscal year-end per the 2024 10-K is 2024-12-28 (last Saturday of December).** The pattern for all prior years in Dolt uses the actual fiscal year-end date (e.g. 2023-12-30, 2022-12-31, 2021-12-25), not the calendar year-end. This is a data entry error.
- Gross margin: 5,396,557 / 14,883,231 = **36.3%** ✓
- Balance sheet identity: 7,535,151 + 2,270,334 = 9,805,485 ✓
- Restatement check: FY2024 comparative values in the 2025 10-K match exactly — no restatement.

### Reconciled Recommendation

**Action: Correction — reportDate '2024-12-31' → '2024-12-28'. All financial values unchanged.**

---

## FY2025 Analysis

**reportDate:** 2025-12-27 (fiscal year-end per 2025 10-K income statement and balance sheet headers)

Not yet in Dolt DB — new insert required.

### Source Data

| Field | SEC | Yahoo | Recommended |
|-------|-----|-------|-------------|
| Net Revenue | 15,524,046 | 15,524,050 | 15,524,046 |
| Cost of Goods | 9,869,538 | 9,869,540 | 9,869,538 |
| Gross Margin | 5,654,508 | 5,654,510 | 5,654,508 |
| SGA | 3,693,108 | 3,693,110 | 3,693,108 |
| Operating Profit | 1,467,389 | 1,467,390 | 1,467,389 |
| Net Profit | 1,096,087 | 1,096,090 | 1,096,087 |
| Inventory | 3,084,086 | 3,084,090 | 3,084,086 |
| Current Assets | 3,507,797 | 3,507,800 | 3,507,797 |
| Total Assets | 10,933,679 | 10,933,700 | 10,933,679 |
| Current Liabilities | 2,614,449 | 2,614,450 | 2,614,449 |
| Liabilities | 8,352,386 | N/A (calc) | 8,352,386 |
| Total Shareholder Equity | 2,581,293 | 2,581,290 | 2,581,293 |
| TL&SE | 10,933,679 | 10,933,700 | 10,933,679 |

Yahoo differences are rounding only (≤$21K, less than 0.001%). Use SEC values.

### Anomaly Checks

- Gross margin: 5,654,508 / 15,524,046 = **36.4%** ✓
- Balance sheet identity: Liabilities $8,352,386 + TSE $2,581,293 = $10,933,679 = Total Assets ✓
- Liabilities verification: Total Assets $10,933,679 − TSE $2,581,293 = $8,352,386 = SEC Total Liabilities ✓
- SEC and Yahoo agree across all income statement and balance sheet fields ✓

### Reconciled Recommendation

| Field | Recommended | Source |
|-------|-------------|--------|
| reportDate | 2025-12-27 | SEC 2025 10-K |
| Net Revenue | 15,524,046 | SEC |
| Cost of Goods | 9,869,538 | SEC |
| Gross Margin | 5,654,508 | Calculated |
| SGA | 3,693,108 | SEC |
| Operating Profit | 1,467,389 | SEC |
| Net Profit | 1,096,087 | SEC |
| Inventory | 3,084,086 | SEC |
| Current Assets | 3,507,797 | SEC |
| Total Assets | 10,933,679 | SEC |
| Current Liabilities | 2,614,449 | SEC |
| Liabilities | 8,352,386 | Calculated |
| Total Shareholder Equity | 2,581,293 | SEC |
| TL&SE | 10,933,679 | SEC |

**Action: New insert**

---

## Analysis Complete

**3 years require action:**
- **FY2020** — Correction: Revenue and Gross Margin wrong (Revenue was accidentally entered as shares outstanding)
- **FY2024** — Correction: reportDate '2024-12-31' → '2024-12-28' (all financial values correct)
- **FY2025** — New insert

Run `/create-verified-dolt-db-financials-sql TSCO` to write all changed years to the database.
