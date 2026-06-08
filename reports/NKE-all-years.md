# Nike (NKE) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action | Notes |
|------|-----------|--------|-------|
| 2018 | 2019-05-31 | Correction: Operating Profit | Dolt has 4,801,000 (Income Before Taxes); should be 4,772,000 (Gross − SGA) |
| 2019 | 2020-05-31 | **Correction: Operating Profit [ERROR]** | Dolt has 16,241,000 (equals Gross Margin); should be 3,115,000 (Gross − SGA) |
| 2020 | 2021-05-31 | Correction: Operating Profit | Dolt has 6,661,000 (Income Before Taxes); should be 6,937,000 (Gross − SGA) |
| 2021 | 2022-05-31 | Correction: Operating Profit | Dolt has 6,651,000; should be 6,675,000 (Gross − SGA). Diff of −24K |
| 2022 | 2023-05-31 | No change | All values match across SEC, Yahoo, Dolt |
| 2023 | 2024-05-31 | No change | All values match across SEC, Yahoo, Dolt |
| 2024 | **2025-05-31** | Correction: reportDate | Dolt has reportDate=2024-05-31; should be 2025-05-31. Values are correct |

---

## Year 2018 (reportDate 2019-05-31)

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 39,117,000 | N/A | 39,117,000 | 39,117,000 |
| Cost of Goods | 21,643,000 | N/A | 21,643,000 | 21,643,000 |
| Gross Margin | 17,474,000 | N/A | 17,474,000 | 17,474,000 |
| SGA | 12,702,000 | N/A | 12,702,000 | 12,702,000 |
| **Operating Profit** | **4,772,000** | N/A | ***4,801,000*** | **4,772,000** |
| Net Profit | 4,029,000 | N/A | 4,029,000 | 4,029,000 |
| Inventory | 5,622,000 | N/A | 5,622,000 | 5,622,000 |
| Current Assets | 16,525,000 | N/A | 16,525,000 | 16,525,000 |
| Total Assets | 23,717,000 | N/A | 23,717,000 | 23,717,000 |
| Current Liabilities | 7,866,000 | N/A | 7,866,000 | 7,866,000 |
| Liabilities | 14,677,000 | N/A | 14,677,000 | 14,677,000 |
| Total SE | 9,040,000 | N/A | 9,040,000 | 9,040,000 |
| Total L+SE | 23,717,000 | N/A | 23,717,000 | 23,717,000 |

### Anomalies Detected

- **[WARNING] Operating Profit mismatch:** Dolt stores 4,801,000 = SEC "Income before income taxes." True Operating Profit (Gross − SGA) = 17,474,000 − 12,702,000 = 4,772,000.
- **Balance sheet identity:** Total Assets (23,717,000) = Total L+SE (23,717,000) ✓

### Reconciliation

All values correct except Operating Profit. Recommended: 4,772,000 (SEC Gross − SGA). This aligns with how years 2022–2024 are already stored.

---

## Year 2019 (reportDate 2020-05-31)

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 37,403,000 | N/A | 37,403,000 | 37,403,000 |
| Cost of Goods | 21,162,000 | N/A | 21,162,000 | 21,162,000 |
| Gross Margin | 16,241,000 | N/A | 16,241,000 | 16,241,000 |
| SGA | 13,126,000 | N/A | 13,126,000 | 13,126,000 |
| **Operating Profit** | **3,115,000** | N/A | ***16,241,000*** | **3,115,000** |
| Net Profit | 2,539,000 | N/A | 2,539,000 | 2,539,000 |
| Inventory | 7,367,000 | N/A | 7,367,000 | 7,367,000 |
| Current Assets | 20,556,000 | N/A | 20,556,000 | 20,556,000 |
| Total Assets | 31,342,000 | N/A | 31,342,000 | 31,342,000 |
| Current Liabilities | 8,284,000 | N/A | 8,284,000 | 8,284,000 |
| Liabilities | 23,287,000 | N/A | 23,287,000 | 23,287,000 |
| Total SE | 8,055,000 | N/A | 8,055,000 | 8,055,000 |
| Total L+SE | 31,342,000 | N/A | 31,342,000 | 31,342,000 |

### Anomalies Detected

- **[ERROR] Operating Profit equals Gross Margin:** Dolt stores Operating Profit = 16,241,000, which is identical to Gross Margin. This is a copy-paste error. True Operating Profit (Gross − SGA) = 16,241,000 − 13,126,000 = 3,115,000.
- **Balance sheet identity:** Total Assets (31,342,000) = Total L+SE (31,342,000) ✓

### Reconciliation

**Must fix:** Operating Profit should be 3,115,000 (SEC Gross − SGA). Dolt has copied Gross Margin into Operating Profit. All other values match SEC.

---

## Year 2020 (reportDate 2021-05-31)

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 44,538,000 | N/A | 44,538,000 | 44,538,000 |
| Cost of Goods | 24,576,000 | N/A | 24,576,000 | 24,576,000 |
| Gross Margin | 19,962,000 | N/A | 19,962,000 | 19,962,000 |
| SGA | 13,025,000 | N/A | 13,025,000 | 13,025,000 |
| **Operating Profit** | **6,937,000** | N/A | ***6,661,000*** | **6,937,000** |
| Net Profit | 5,727,000 | N/A | 5,727,000 | 5,727,000 |
| Inventory | 6,854,000 | N/A | 6,854,000 | 6,854,000 |
| Current Assets | 26,291,000 | N/A | 26,291,000 | 26,291,000 |
| Total Assets | 37,740,000 | N/A | 37,740,000 | 37,740,000 |
| Current Liabilities | 9,674,000 | N/A | 9,674,000 | 9,674,000 |
| Liabilities | 24,973,000 | N/A | 24,973,000 | 24,973,000 |
| Total SE | 12,767,000 | N/A | 12,767,000 | 12,767,000 |
| Total L+SE | 37,740,000 | N/A | 37,740,000 | 37,740,000 |

### Anomalies Detected

- **[WARNING] Operating Profit mismatch:** Dolt has 6,661,000 = SEC "Income before income taxes." True Operating Profit (Gross − SGA) = 19,962,000 − 13,025,000 = 6,937,000. Difference of −276K.
- **Balance sheet identity:** ✓

### Reconciliation

Operating Profit should be 6,937,000 (SEC Gross − SGA). All other values match SEC.

---

## Year 2021 (reportDate 2022-05-31)

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 46,710,000 | 46,710,000 | 46,710,000 | 46,710,000 |
| Cost of Goods | 25,231,000 | 25,231,000 | 25,231,000 | 25,231,000 |
| Gross Margin | 21,479,000 | 21,479,000 | 21,479,000 | 21,479,000 |
| SGA | 14,804,000 | 14,804,000 | 14,804,000 | 14,804,000 |
| **Operating Profit** | **6,675,000** | **6,675,000** | ***6,651,000*** | **6,675,000** |
| Net Profit | 6,046,000 | 6,046,000 | 6,046,000 | 6,046,000 |
| Inventory | 8,420,000 | 8,420,000 | 8,420,000 | 8,420,000 |
| Current Assets | 28,213,000 | 28,213,000 | 28,213,000 | 28,213,000 |
| Total Assets | 40,321,000 | 40,321,000 | 40,321,000 | 40,321,000 |
| Current Liabilities | 10,730,000 | 10,730,000 | 10,730,000 | 10,730,000 |
| Liabilities | 25,040,000 | 25,040,000 | 25,040,000 | 25,040,000 |
| Total SE | 15,281,000 | 15,281,000 | 15,281,000 | 15,281,000 |
| Total L+SE | 40,321,000 | 40,321,000 | 40,321,000 | 40,321,000 |

### Anomalies Detected

- **[WARNING] Operating Profit mismatch:** Dolt has 6,651,000 = SEC "Income before income taxes." SEC Gross − SGA = 6,675,000. Yahoo Operating Income = 6,675,000. Dolt is off by −24K.
- **Balance sheet identity:** ✓
- **SEC/Yahoo agreement:** All fields match perfectly between SEC and Yahoo.

### Reconciliation

Operating Profit should be 6,675,000 (SEC/Yahoo consensus). All other values are correct across all sources.

---

## Year 2022 (reportDate 2023-05-31)

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 51,217,000 | 51,217,000 | 51,217,000 | 51,217,000 |
| Cost of Goods | 28,925,000 | 28,925,000 | 28,925,000 | 28,925,000 |
| Gross Margin | 22,292,000 | 22,292,000 | 22,292,000 | 22,292,000 |
| SGA | 16,377,000 | 16,377,000 | 16,377,000 | 16,377,000 |
| Operating Profit | 5,915,000 | 5,915,000 | 5,915,000 | 5,915,000 |
| Net Profit | 5,070,000 | 5,070,000 | 5,070,000 | 5,070,000 |
| Inventory | 8,454,000 | 8,454,000 | 8,454,000 | 8,454,000 |
| Current Assets | 25,202,000 | 25,202,000 | 25,202,000 | 25,202,000 |
| Total Assets | 37,531,000 | 37,531,000 | 37,531,000 | 37,531,000 |
| Current Liabilities | 9,256,000 | 9,256,000 | 9,256,000 | 9,256,000 |
| Liabilities | 23,527,000 | 23,527,000 | 23,527,000 | 23,527,000 |
| Total SE | 14,004,000 | 14,004,000 | 14,004,000 | 14,004,000 |
| Total L+SE | 37,531,000 | 37,531,000 | 37,531,000 | 37,531,000 |

### Anomalies Detected

- **No anomalies.** All three sources agree perfectly. ✓
- **Balance sheet identity:** Total Assets (37,531,000) = Total L+SE (37,531,000) ✓
- **Gross margin sanity:** 22,292/51,217 = 43.5% — within expected 35–55% for specialty apparel ✓

### Reconciliation

No changes needed for this year.

---

## Year 2023 (reportDate 2024-05-31)

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 51,362,000 | 51,362,000 | 51,362,000 | 51,362,000 |
| Cost of Goods | 28,475,000 | 28,475,000 | 28,475,000 | 28,475,000 |
| Gross Margin | 22,887,000 | 22,887,000 | 22,887,000 | 22,887,000 |
| SGA | 16,576,000 | 16,576,000 | 16,576,000 | 16,576,000 |
| Operating Profit | 6,311,000 | 6,311,000 | 6,311,000 | 6,311,000 |
| Net Profit | 5,700,000 | 5,700,000 | 5,700,000 | 5,700,000 |
| Inventory | 7,519,000 | 7,519,000 | 7,519,000 | 7,519,000 |
| Current Assets | 25,382,000 | 25,382,000 | 25,382,000 | 25,382,000 |
| Total Assets | 38,110,000 | 38,110,000 | 38,110,000 | 38,110,000 |
| Current Liabilities | 10,593,000 | 10,593,000 | 10,593,000 | 10,593,000 |
| Liabilities | 23,680,000 | 23,680,000 | 23,680,000 | 23,680,000 |
| Total SE | 14,430,000 | 14,430,000 | 14,430,000 | 14,430,000 |
| Total L+SE | 38,110,000 | 38,110,000 | 38,110,000 | 38,110,000 |

### Anomalies Detected

- **No anomalies.** All three sources agree perfectly. ✓
- **Balance sheet identity:** Total Assets (38,110,000) = Total L+SE (38,110,000) ✓

### Reconciliation

No changes needed for this year.

---

## Year 2024 (reportDate 2025-05-31 — CORRECTION NEEDED)

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 46,309,000 | 46,309,000 | 46,309,000 | 46,309,000 |
| Cost of Goods | 26,519,000 | 26,519,000 | 26,519,000 | 26,519,000 |
| Gross Margin | 19,790,000 | 19,790,000 | 19,790,000 | 19,790,000 |
| SGA | 16,088,000 | 16,088,000 | 16,088,000 | 16,088,000 |
| Operating Profit | 3,702,000 | 3,702,000 | 3,702,000 | 3,702,000 |
| Net Profit | 3,219,000 | 3,219,000 | 3,219,000 | 3,219,000 |
| Inventory | 7,489,000 | 7,489,000 | 7,489,000 | 7,489,000 |
| Current Assets | 23,362,000 | 23,362,000 | 23,362,000 | 23,362,000 |
| Total Assets | 36,579,000 | 36,579,000 | 36,579,000 | 36,579,000 |
| Current Liabilities | 10,566,000 | 10,566,000 | 10,566,000 | 10,566,000 |
| Liabilities | 23,366,000 | 23,366,000 | 23,366,000 | 23,366,000 |
| Total SE | 13,213,000 | 13,213,000 | 13,213,000 | 13,213,000 |
| Total L+SE | 36,579,000 | 36,579,000 | 36,579,000 | 36,579,000 |

### Anomalies Detected

- **[WARNING] reportDate mismatch:** Dolt has reportDate=2024-05-31 for this row, but the actual fiscal year end is 2025-05-31. All field values are correct — only the date is wrong.
- **Balance sheet identity:** Total Assets (36,579,000) = Total L+SE (36,579,000) ✓
- **SEC/Yahoo agreement:** All values match perfectly.

### Reconciliation

**All field values are correct.** Only the `reportDate` needs updating from 2024-05-31 to 2025-05-31.

---

## Global Anomaly Summary

### Operating Profit Inconsistency (Years 2018–2021)

Years 2018, 2019, 2020, and 2021 in the Dolt DB store "Income Before Income Taxes" as Operating Profit, while years 2022, 2023, and 2024 correctly store "Gross Profit − SGA." The Operating Profit field should consistently represent operating income (Gross − SGA), excluding non-operating items (interest, other income/expense).

| Year | Dolt Operating Profit | SEC Operating Profit (Gross − SGA) | SEC Income Before Taxes | Correction Needed? |
|------|----------------------|-----------------------------------|------------------------|-------------------|
| 2018 | 4,801,000 | 4,772,000 | 4,801,000 | Yes (−29K) |
| 2019 | **16,241,000** | 3,115,000 | 2,887,000 | **Yes (−13,126K) — copied Gross Margin** |
| 2020 | 6,661,000 | 6,937,000 | 6,661,000 | Yes (+276K) |
| 2021 | 6,651,000 | 6,675,000 | 6,651,000 | Yes (+24K) |
| 2022 | 5,915,000 | 5,915,000 | 6,201,000 | No ✓ |
| 2023 | 6,311,000 | 6,311,000 | 6,700,000 | No ✓ |
| 2024 | 3,702,000 | 3,702,000 | 3,885,000 | No ✓ |

### reportDate Error (Year 2024)

Dolt year=2024 has reportDate=2024-05-31. The correct date is 2025-05-31 (Nike's FY2025 ends May 31, 2025).

### SGA Construction

Nike reports a combined `us-gaap_SellingGeneralAndAdministrativeExpense` tag in SEC filings. Yahoo also reports a combined SGA. No SGA composite rules are triggered. The Dolt SGA values match SEC and Yahoo across all years.

### Gross Margin Sanity Check

| Year | Gross Margin % | Segment Range (35–55%) |
|------|---------------|----------------------|
| 2018 | 44.7% | ✓ |
| 2019 | 43.4% | ✓ |
| 2020 | 44.8% | ✓ |
| 2021 | 46.0% | ✓ |
| 2022 | 43.5% | ✓ |
| 2023 | 44.6% | ✓ |
| 2024 | 42.7% | ✓ |

All within expected range for specialty apparel retailer.

### Floor-Line Items

- **Inventory:** Nike carries physical inventory — positive values across all years (5.6B–8.5B). No anomaly.
- **Total Shareholder Equity:** Positive across all years. No anomaly.
- **Balance Sheet Identity:** Total Assets = Total L+SE within rounding for all years. ✓

---

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql NKE` to write all changed years to the database.

### Unresolved Flags to Review Before Inserting

1. **[ERROR] Year 2019 Operating Profit:** Currently 16,241,000 (copied from Gross Margin). Must be corrected to 3,115,000.
2. **[WARNING] Year 2018, 2020, 2021 Operating Profit:** Off by 24K–276K due to mixing Income Before Taxes with Operating Profit.
3. **[WARNING] Year 2024 reportDate:** Must change from 2024-05-31 to 2025-05-31.
