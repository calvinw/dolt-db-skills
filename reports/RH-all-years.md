# RH (RH) — FY2018-FY2025 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2019-02-02 | Correction: COGS, Gross Margin, SGA, Operating Profit, Net Profit (SEC restatement) |
| 2019 | 2020-02-01 | No change |
| 2020 | 2021-01-30 | No change |
| 2021 | 2022-01-29 | No change |
| 2022 | 2023-01-28 | No change |
| 2023 | 2024-02-03 | No change |
| 2024 | 2025-02-03 | No change |
| 2025 | 2026-01-31 | New insert (Yahoo only; not yet in Dolt DB) |

---

## FY2018 — Analysis

**reportDate:** 2019-02-02
**Note:** SEC 2018 API unavailable. Income statement values sourced from SEC FY2019 filing comparative column (restated). Balance sheet values from Dolt only (SEC API did not return FY2018 balance sheet data).

### Anomaly Detection

- `[WARNING]` **FY2018 restatement detected.** Dolt FY2018 values differ from the restated FY2018 comparatives in the SEC FY2019 filing. The restated values from the most recent filing should be used.
- `[WARNING]` **Negative shareholder equity** (-$22,962K) — valid for a leveraged retailer.

### Side-by-Side Comparison

| Field | SEC (restated) | Yahoo | Dolt (current) | Recommended |
|-------|---------------|-------|----------------|-------------|
| Net Revenue | 2,505,653 | N/A | 2,505,653 | 2,505,653 |
| Cost of Goods | 1,520,076 | N/A | *1,504,806* | 1,520,076 |
| Gross Margin | 985,577 | N/A | *1,000,847* | 985,577 |
| SGA | 723,841 | N/A | *711,617* | 723,841 |
| Operating Profit | 261,736 | N/A | *289,230* | 261,736 |
| Net Profit | 135,731 | N/A | *150,639* | 135,731 |
| Inventory | N/A | N/A | 531,947 | 531,947 |
| Current Assets | N/A | N/A | 682,693 | 682,693 |
| Total Assets | N/A | N/A | 1,806,034 | 1,806,034 |
| Current Liabilities | N/A | N/A | 918,172 | 918,172 |
| Liabilities | N/A | N/A | 1,828,996 | 1,828,996 |
| Total SE | N/A | N/A | -22,962 | -22,962 |
| Total L&SE | N/A | N/A | 1,806,034 | 1,806,034 |

### Reconciliation

- **COGS:** Dolt $1,504,806K → Recommended $1,520,076K (SEC restated). Diff: +$15,270K.
- **SGA:** Dolt $711,617K → Recommended $723,841K (SEC restated). Diff: +$12,224K.
- **Operating Profit:** Dolt $289,230K → Recommended $261,736K (SEC restated). Diff: -$27,494K.
- **Net Profit:** Dolt $150,639K → Recommended $135,731K (SEC restated). Diff: -$14,908K.
- Balance sheet values kept from Dolt (no SEC source available to verify). Internally consistent (TA $1,806,034K = Liabilities $1,828,996K + SE -$22,962K).

---

## FY2019 — Analysis

**reportDate:** 2020-02-01

### Anomaly Detection

- No anomalies detected.

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 2,647,437 | N/A | 2,647,437 | 2,647,437 |
| Cost of Goods | 1,552,426 | N/A | 1,552,426 | 1,552,426 |
| Gross Margin | 1,095,011 | N/A | 1,095,011 | 1,095,011 |
| SGA | 732,180 | N/A | 732,180 | 732,180 |
| Operating Profit | 362,831 | N/A | 362,831 | 362,831 |
| Net Profit | 220,375 | N/A | 220,375 | 220,375 |
| Inventory | 438,696 | N/A | 438,696 | 438,696 |
| Current Assets | 596,952 | N/A | 596,952 | 596,952 |
| Total Assets | 2,445,694 | N/A | 2,445,694 | 2,445,694 |
| Current Liabilities | 982,912 | N/A | 982,912 | 982,912 |
| Liabilities | 2,427,043 | N/A | 2,427,043 | 2,427,043 |
| Total SE | 18,651 | N/A | 18,651 | 18,651 |
| Total L&SE | 2,445,694 | N/A | 2,445,694 | 2,445,694 |

### Reconciliation

All values match perfectly between SEC and Dolt. Balance sheet identity: $2,445,694K = $2,427,043K + $18,651K ✓

---

## FY2020 — Analysis

**reportDate:** 2021-01-30

### Anomaly Detection

- No anomalies detected.

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 2,848,626 | N/A | 2,848,626 | 2,848,626 |
| Cost of Goods | 1,523,095 | N/A | 1,523,095 | 1,523,095 |
| Gross Margin | 1,325,531 | N/A | 1,325,531 | 1,325,531 |
| SGA | 858,673 | N/A | 858,673 | 858,673 |
| Operating Profit | 466,858 | N/A | 466,858 | 466,858 |
| Net Profit | 271,815 | N/A | 271,815 | 271,815 |
| Inventory | 544,227 | N/A | 544,227 | 544,227 |
| Current Assets | 801,484 | N/A | 801,484 | 801,484 |
| Total Assets | 2,898,313 | N/A | 2,898,313 | 2,898,313 |
| Current Liabilities | 921,632 | N/A | 921,632 | 921,632 |
| Liabilities | 2,451,287 | N/A | 2,451,287 | 2,451,287 |
| Total SE | 447,026 | N/A | 447,026 | 447,026 |
| Total L&SE | 2,898,313 | N/A | 2,898,313 | 2,898,313 |

### Reconciliation

All values match perfectly between SEC and Dolt. Balance sheet identity: $2,898,313K = $2,451,287K + $447,026K ✓

---

## FY2021 — Analysis

**reportDate:** 2022-01-29

### Anomaly Detection

- No anomalies detected.

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 3,758,820 | N/A | 3,758,820 | 3,758,820 |
| Cost of Goods | 1,903,409 | N/A | 1,903,409 | 1,903,409 |
| Gross Margin | 1,855,411 | N/A | 1,855,411 | 1,855,411 |
| SGA | 928,230 | N/A | 928,230 | 928,230 |
| Operating Profit | 927,181 | N/A | 927,181 | 927,181 |
| Net Profit | 688,546 | N/A | 688,546 | 688,546 |
| Inventory | 734,289 | N/A | 734,289 | 734,289 |
| Current Assets | 3,091,442 | N/A | 3,091,442 | 3,091,442 |
| Total Assets | 5,540,470 | N/A | 5,540,470 | 5,540,470 |
| Current Liabilities | 1,063,758 | N/A | 1,063,758 | 1,063,758 |
| Liabilities | 4,370,193 | N/A | 4,370,193 | 4,370,193 |
| Total SE | 1,170,277 | N/A | 1,170,277 | 1,170,277 |
| Total L&SE | 5,540,470 | N/A | 5,540,470 | 5,540,470 |

### Reconciliation

All values match perfectly between SEC and Dolt. Balance sheet identity: $5,540,470K = $4,370,193K + $1,170,277K ✓

---

## FY2022 — Analysis

**reportDate:** 2023-01-28

### Anomaly Detection

- No anomalies detected. All three sources agree within rounding.

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 3,590,477 | 3,590,480 | 3,590,477 | 3,590,477 |
| Cost of Goods | 1,778,492 | 1,778,490 | 1,778,492 | 1,778,492 |
| Gross Margin | 1,811,985 | 1,811,990 | 1,811,985 | 1,811,985 |
| SGA | 1,089,828 | 1,089,830 | 1,089,828 | 1,089,828 |
| Operating Profit | 722,157 | 722,157 | 722,157 | 722,157 |
| Net Profit | 528,642 | 528,642 | 528,642 | 528,642 |
| Inventory | 801,841 | 801,841 | 801,841 | 801,841 |
| Current Assets | 2,512,664 | 2,512,660 | 2,512,664 | 2,512,664 |
| Total Assets | 5,309,289 | 5,309,290 | 5,309,289 | 5,309,289 |
| Current Liabilities | 885,973 | 885,973 | 885,973 | 885,973 |
| Liabilities | 4,524,628 | 4,524,630 | 4,524,628 | 4,524,628 |
| Total SE | 784,661 | 784,661 | 784,661 | 784,661 |
| Total L&SE | 5,309,289 | 5,309,291 | 5,309,289 | 5,309,289 |

### Reconciliation

All three sources agree within rounding tolerance ($1-3K differences from Yahoo rounding). Balance sheet identity: $5,309,289K = $4,524,628K + $784,661K ✓

---

## FY2023 — Analysis

**reportDate:** 2024-02-03 (Dolt/SEC), 2024-01-31 (Yahoo — 3-day fiscal calendar difference)

### Anomaly Detection

- `[WARNING]` **Negative Total Shareholder Equity** (-$297,394K). Valid for a leveraged retailer.

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 3,029,126 | 3,029,130 | 3,029,126 | 3,029,126 |
| Cost of Goods | 1,640,107 | 1,640,110 | 1,640,107 | 1,640,107 |
| Gross Margin | 1,389,019 | 1,389,020 | 1,389,019 | 1,389,019 |
| SGA | 1,022,948 | 1,022,950 | 1,022,948 | 1,022,948 |
| Operating Profit | 366,071 | 366,071 | 366,071 | 366,071 |
| Net Profit | 127,561 | 127,561 | 127,561 | 127,561 |
| Inventory | 754,126 | 754,126 | 754,126 | 754,126 |
| Current Assets | 1,101,902 | 1,101,900 | 1,101,902 | 1,101,902 |
| Total Assets | 4,143,897 | 4,143,900 | 4,143,897 | 4,143,897 |
| Current Liabilities | 872,868 | 872,868 | 872,868 | 872,868 |
| Liabilities | 4,441,291 | 4,441,290 | 4,441,291 | 4,441,291 |
| Total SE | -297,394 | -297,394 | -297,394 | -297,394 |
| Total L&SE | 4,143,897 | 4,143,896 | 4,143,897 | 4,143,897 |

### Reconciliation

All sources agree within rounding. Balance sheet identity: $4,143,897K = $4,441,291K + (-$297,394K) ✓

---

## FY2024 — Analysis

**reportDate:** 2025-02-03 (Dolt), 2025-02-01 (SEC), 2025-01-31 (Yahoo — minor fiscal calendar variation)

### Anomaly Detection

- `[WARNING]` **Negative Total Shareholder Equity** (-$163,589K). Valid for a leveraged retailer.

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 3,180,753 | 3,180,750 | 3,180,753 | 3,180,753 |
| Cost of Goods | 1,765,821 | 1,765,820 | 1,765,821 | 1,765,821 |
| Gross Margin | 1,414,932 | 1,414,930 | 1,414,932 | 1,414,932 |
| SGA | 1,092,345 | 1,092,340 | 1,092,345 | 1,092,345 |
| Operating Profit | 322,587 | 322,587 | 322,587 | 322,587 |
| Net Profit | 72,412 | 72,412 | 72,412 | 72,412 |
| Inventory | 1,019,591 | 1,019,590 | 1,019,591 | 1,019,591 |
| Current Assets | 1,291,331 | 1,291,330 | 1,291,331 | 1,291,331 |
| Total Assets | 4,554,689 | 4,554,690 | 4,554,689 | 4,554,689 |
| Current Liabilities | 905,126 | 905,126 | 905,126 | 905,126 |
| Liabilities | 4,718,278 | 4,718,280 | 4,718,278 | 4,718,278 |
| Total SE | -163,589 | -163,589 | -163,589 | -163,589 |
| Total L&SE | 4,554,689 | 4,554,691 | 4,554,689 | 4,554,689 |

### Reconciliation

All sources agree within rounding ($1-3K differences from Yahoo). Balance sheet identity: $4,554,689K = $4,718,278K + (-$163,589K) ✓

---

## FY2025 — Analysis (New Year — Not in Dolt DB)

**reportDate:** 2026-01-31
**Source:** Yahoo Finance only (SEC 10-K may not yet be available for this period, or API limitations apply)

### Anomaly Detection

- No SEC data available for cross-reference.

### Yahoo Data

| Field | Yahoo | Recommended |
|-------|-------|-------------|
| Net Revenue | 3,439,540 | 3,439,540 |
| Cost of Goods | 1,923,780 | 1,923,780 |
| Gross Margin | 1,515,760 | 1,515,760 |
| SGA | 1,128,490 | 1,128,490 |
| Operating Profit | 387,268 | 387,268 |
| Net Profit | 124,787 | 124,787 |
| Inventory | 818,550 | 818,550 |
| Current Assets | 1,107,660 | 1,107,660 |
| Total Assets | 4,835,710 | 4,835,710 |
| Current Liabilities | 930,606 | 930,606 |
| Liabilities | 4,775,110 | 4,775,110 |
| Total SE | 60,600 | 60,600 |
| Total L&SE | 4,835,710 | 4,835,710 |

### Reconciliation

Balance sheet identity: $4,835,710K = $4,775,110K + $60,600K ✓
Gross margin: 44.1% (within Specialty retail 35-55% benchmark).
Shareholder equity returned to positive ($60,600K) after two years of negative equity.

**Note:** This is a newly discovered fiscal year. To insert this data, run `/download-new-year-data RH` which will cross-check with SEC (when available) and validate consistency before inserting.

---

## Gross Margin Trend

| Year | Gross Margin % | Benchmark (Specialty 35-55%) |
|------|---------------|------------------------------|
| 2018 | 39.3%* | Within range |
| 2019 | 41.4% | Within range |
| 2020 | 46.5% | Within range |
| 2021 | 49.4% | Within range |
| 2022 | 50.5% | Within range |
| 2023 | 45.9% | Within range |
| 2024 | 44.5% | Within range |
| 2025 | 44.1% | Within range |

*FY2018 based on restated SEC values.

---

## SGA Composite Check

RH reports a single `us-gaap_SellingGeneralAndAdministrativeExpense` line in SEC filings. There is no separate Marketing, Operations & Technology, or other operating expense line. Yahoo SGA matches SEC SGA. No composite adjustment needed.

---

## Unresolved Flags

1. `[WARNING]` **FY2018 restatement.** Dolt FY2018 income statement values differ from SEC restated comparatives. Action needed: update COGS, GM, SGA, OP, NP to SEC restated values.
2. `[WARNING]` **Negative shareholder equity** in FY2023 (-$297,394K) and FY2024 (-$163,589K). Both valid for a leveraged capital structure. By FY2025, equity returned to positive $60,600K.
3. `[WARNING]` **FY2025** is a new year not yet in the Dolt DB. Yahoo-only source — SEC cross-reference not yet available.

---

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql RH` to write all changed years to the database.
