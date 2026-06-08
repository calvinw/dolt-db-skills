# Rite Aid (RAD) — FY2018–FY2022 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2019-03-02 | No change — all values match |
| 2019 | 2020-02-29 | No change — all values match |
| 2020 | 2021-02-27 | Correction: Net Profit (restated), Operating Profit |
| 2021 | 2022-02-26 | Correction: Net Profit (restated), Operating Profit |
| 2022 | 2023-03-04 | Correction: Operating Profit, Net Profit, Current Liabilities, Total SE, Liabilities |

**Note:** The 2023 10-K filing (FY ending 2023-03-04) includes a restatement of prior periods. Dolt values reflect original (pre-restatement) figures. Per the Restatement Rule, the most recent filing (2023 10-K) restated values should be used.

**Note:** Yahoo Finance data is unavailable for RAD — ticker was delisted after Rite Aid's Chapter 11 bankruptcy filing (October 2023). All comparisons are SEC vs Dolt only.

---

## FY2018 (reportDate: 2019-03-02)

### Comparison Table

| Field | SEC | Dolt | Recommended |
|-------|-----|------|-------------|
| Net Revenue | 21,639,557 | 21,639,557 | 21,639,557 |
| Cost of Goods | 16,963,205 | 16,963,205 | 16,963,205 |
| Gross Margin | 4,676,352 | 4,676,352 | 4,676,352 |
| SGA | 4,592,375 | 4,592,375 | 4,592,375 |
| Operating Profit | -589,477 | -589,477 | -589,477 |
| Net Profit | -422,213 | -422,213 | -422,213 |
| Inventory | 1,871,941 | 1,871,941 | 1,871,941 |
| Current Assets | 4,101,719 | 4,101,719 | 4,101,719 |
| Total Assets | 7,591,367 | 7,591,367 | 7,591,367 |
| Current Liabilities | 2,443,135 | 2,443,135 | 2,443,135 |
| Liabilities | 6,404,677 | 6,404,677 | 6,404,677 |
| Total SE | 1,186,690 | 1,186,690 | 1,186,690 |
| Total L+SE | 7,591,367 | 7,591,367 | 7,591,367 |

**Result: All fields match. No change required.**

### Anomaly Checks
- Gross Margin: 21.6% — within Health & Pharmacy benchmark (18-25%) ✓
- Balance Sheet Identity: Total Assets (7,591,367) = Total L+SE (7,591,367) ✓
- Derived Liabilities: 7,591,367 − 1,186,690 = 6,404,677 = SEC reported Liabilities ✓
- SGA: Single combined `us-gaap_SellingGeneralAndAdministrativeExpense` — no composite needed ✓

---

## FY2019 (reportDate: 2020-02-29)

### Comparison Table

| Field | SEC | Dolt | Recommended |
|-------|-----|------|-------------|
| Net Revenue | 21,928,393 | 21,928,393 | 21,928,393 |
| Cost of Goods | 17,201,635 | 17,201,635 | 17,201,635 |
| Gross Margin | 4,726,758 | 4,726,758 | 4,726,758 |
| SGA | 4,587,336 | 4,587,336 | 4,587,336 |
| Operating Profit | -81,612 | -81,612 | -81,612 |
| Net Profit | -452,174 | -452,174 | -452,174 |
| Inventory | 1,921,604 | 1,921,604 | 1,921,604 |
| Current Assets | 3,700,641 | 3,700,641 | 3,700,641 |
| Total Assets | 9,452,369 | 9,452,369 | 9,452,369 |
| Current Liabilities | 2,766,463 | 2,766,463 | 2,766,463 |
| Liabilities | 8,777,842 | 8,777,842 | 8,777,842 |
| Total SE | 674,527 | 674,527 | 674,527 |
| Total L+SE | 9,452,369 | 9,452,369 | 9,452,369 |

**Result: All fields match. No change required.**

### Anomaly Checks
- Gross Margin: 21.6% — in range ✓
- Balance Sheet Identity: 9,452,369 = 9,452,369 ✓
- Derived Liabilities: 9,452,369 − 674,527 = 8,777,842 ✓

---

## FY2020 (reportDate: 2021-02-27)

### Comparison Table

| Field | SEC (original) | SEC (restated) | Dolt | Recommended |
|-------|---------------|---------------|------|-------------|
| Net Revenue | 24,043,240 | 24,043,240 | 24,043,240 | 24,043,240 |
| Cost of Goods | 19,338,918 | 19,338,918 | 19,338,918 | 19,338,918 |
| Gross Margin | 4,704,322 | 4,704,322 | 4,704,322 | 4,704,322 |
| SGA | 4,657,185 | 4,657,185 | 4,657,185 | 4,657,185 |
| Operating Profit | -120,227 | -119,538* | -120,227 | -119,538 |
| Net Profit | -90,909 | -90,220* | -90,909 | -90,220 |
| Inventory | 1,864,890 | 1,864,890 | 1,864,890 | 1,864,890 |
| Current Assets | 3,595,174 | 3,595,174 | 3,595,174 | 3,595,174 |
| Total Assets | 9,335,404 | 9,335,404 | 9,335,404 | 9,335,404 |
| Current Liabilities | 2,602,946 | 2,602,946 | 2,602,946 | 2,602,946 |
| Liabilities | 8,720,250 | 8,720,250 | 8,720,250 | 8,720,250 |
| Total SE | 615,154 | 615,154 | 615,154 | 615,154 |
| Total L+SE | 9,335,404 | 9,335,404 | 9,335,404 | 9,335,404 |

\* Restated in the 2023 10-K filing (adjustment of +$689K to Net Profit).

### Anomaly Checks
- Gross Margin: 19.6% — in range ✓
- Balance Sheet Identity: 9,335,404 = 9,335,404 ✓
- `[WARNING]` Restatement: The 2023 10-K restated FY2020 Net Profit from -90,909 to -90,220 (+689K adjustment to facility exit charges). Dolt has pre-restatement value.
- Negative equity: No (SE = 615,154 > 0)

---

## FY2021 (reportDate: 2022-02-26)

### Comparison Table

| Field | SEC (original) | SEC (restated) | Dolt | Recommended |
|-------|---------------|---------------|------|-------------|
| Net Revenue | 24,568,255 | 24,568,255 | 24,568,255 | 24,568,255 |
| Cost of Goods | 19,461,760 | 19,461,760 | 19,461,760 | 19,461,760 |
| Gross Margin | 5,106,495 | 5,106,495 | 5,106,495 | 5,106,495 |
| SGA | 5,033,876 | 5,033,876 | 5,033,876 | 5,033,876 |
| Operating Profit | -542,258 | -526,152* | -542,258 | -526,152 |
| Net Profit | -538,478 | -522,372* | -538,478 | -522,372 |
| Inventory | 1,959,389 | 1,959,389 | 1,959,389 | 1,959,389 |
| Current Assets | 3,449,355 | 3,449,355 | 3,449,355 | 3,449,355 |
| Total Assets | 8,529,003 | 8,529,003 | 8,529,003 | 8,529,003 |
| Current Liabilities | 2,933,088 | 2,933,088 | 2,933,088 | 2,933,088 |
| Liabilities | 8,429,970 | 8,429,970 | 8,429,970 | 8,429,970 |
| Total SE | 99,033 | 99,033 | 99,033 | 99,033 |
| Total L+SE | 8,529,003 | 8,529,003 | 8,529,003 | 8,529,003 |

\* Restated in the 2023 10-K filing (adjustment of +$16,106K to Net Profit).

### Anomaly Checks
- Gross Margin: 20.8% — in range ✓
- Balance Sheet Identity: 8,529,003 = 8,529,003 ✓
- `[WARNING]` Restatement: The 2023 10-K restated FY2021 Net Profit from -538,478 to -522,372 (+16,106K adjustment). Dolt has pre-restatement value.
- `[WARNING]` Total SE near zero ($99M). Rite Aid was approaching insolvency — negative equity in FY2022.

---

## FY2022 (reportDate: 2023-03-04)

### Comparison Table

| Field | SEC (original†) | SEC (restated) | Dolt | Recommended |
|-------|----------------|---------------|------|-------------|
| Net Revenue | 24,091,899 | 24,091,899 | 24,091,899 | 24,091,899 |
| Cost of Goods | 19,287,959 | 19,287,959 | 19,287,959 | 19,287,959 |
| Gross Margin | 4,803,940 | 4,803,940 | 4,803,940 | 4,803,940 |
| SGA | 4,902,087 | 4,902,087 | 4,902,087 | 4,902,087 |
| Operating Profit | -756,403 | -725,655‡ | **-1,099,147** ★ | -501,256§ |
| Net Profit | -749,936 | -719,188‡ | **-749,936** | -719,188 |
| Inventory | 1,900,744 | 1,900,744 | 1,900,744 | 1,900,744 |
| Current Assets | 3,301,047 | 3,301,047 | 3,301,047 | 3,301,047 |
| Total Assets | 7,527,362 | 7,527,362 | 7,527,362 | 7,527,362 |
| Current Liabilities | 2,727,875 | **2,713,237**‡ | **2,727,875** | 2,713,237 |
| Liabilities | 8,169,138 | **8,121,595**‡ | **8,169,138** | 8,121,595 |
| Total SE | -641,776 | **-594,233**‡ | **-641,776** | -594,233 |
| Total L+SE | 7,527,362 | 7,527,362 | 7,527,362 | 7,527,362 |

† "Original" = pre-restatement values from the 2023 10-K filing's "As Previously Reported" column.
‡ Restated in the same 2023 10-K filing (adjustment of +$30,748K to Net Profit).
★ Operating Profit in Dolt (-1,099,147) does not match any SEC figure — see below.
§ Operating Profit (recommended) = Income Before Tax (−725,655) + Interest Expense (+224,399) = −501,256 (EBIT).

### Anomaly Checks

- **`[ERROR]` Dolt Operating Profit incorrect:** Dolt records -1,099,147 for Operating Profit in FY2022. This does not match any SEC figure. The Income Before Tax (as previously reported) was -756,403, and the restated figure is -725,655. The Operating Profit (EBIT, i.e., Income Before Tax + Interest) = -725,655 + 224,399 = -501,256. Recommend using -501,256.

- **`[ERROR]` Dolt Net Profit pre-restatement:** Dolt records -749,936, which is the pre-restatement value. The restated Net Profit is -719,188. Recommend using -719,188.

- **`[WARNING]` Balance sheet components restated:** Dolt Total SE (-641,776) and Liabilities (8,169,138) differ from restated SEC values (-594,233 and 8,121,595 respectively). The balance sheet identity holds in both (Total Assets = 7,527,362, Total L+SE = 7,527,362), but the SE/Liabilities split differs by $47,543K. Recommend using restated SEC values.

- **`[WARNING]` Negative Total SE:** -594,233 (restated). Valid given Rite Aid's financial distress and subsequent Chapter 11 filing.

- Gross Margin: 19.9% — in range ✓
- Balance Sheet Identity: 7,527,362 = 7,527,362 ✓

---

## SGA Analysis

Rite Aid reports a single `us-gaap_SellingGeneralAndAdministrativeExpense` line item in all years. No separate marketing expense or operations/technology cost is broken out. The SGA values in Dolt match the SEC filing for all years.

**Anomaly Rule 3 check:** Not applicable — no Yahoo Finance data available.

---

## Recommended Values for Database

Based on the analysis above, the following values should be written to the database (restated versions from the 2023 10-K filing, and corrected Operating Profit).

### Fields to update:

**FY2020:**
| Field | Dolt (current) | Recommended |
|-------|---------------|-------------|
| Operating Profit | -120,227 | -119,538 |
| Net Profit | -90,909 | -90,220 |

**FY2021:**
| Field | Dolt (current) | Recommended |
|-------|---------------|-------------|
| Operating Profit | -542,258 | -526,152 |
| Net Profit | -538,478 | -522,372 |

**FY2022:**
| Field | Dolt (current) | Recommended |
|-------|---------------|-------------|
| Operating Profit | -1,099,147 | -501,256 |
| Net Profit | -749,936 | -719,188 |
| Current Liabilities | 2,727,875 | 2,713,237 |
| Liabilities | 8,169,138 | 8,121,595 |
| Total SE | -641,776 | -594,233 |

### Fields to keep (no change needed):

**FY2018, FY2019:** All fields match SEC. No changes.

**All years:** Net Revenue, Cost of Goods, Gross Margin, SGA, Inventory, Current Assets, Total Assets, Total L+SE match SEC and require no changes.

---

## Analysis complete.

Run `/create-verified-dolt-db-financials-sql RAD` to write all changed years to the database.

### Unresolved flags to review before inserting:
1. **FY2022 Operating Profit — large discrepancy resolved** (Dolt had -1,099,147, correct EBIT is -501,256)
2. **Restatements applied** — FY2020/2021/2022 use 2023 10-K restated figures
3. **Negative equity FY2022** — confirmed valid
4. **Yahoo Finance unavailable** — RAD was delisted; all validation based on SEC filings only
