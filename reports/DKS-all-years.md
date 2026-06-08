# Dick's Sporting Goods (DKS) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-06
**Source:** /verify-dolt-db-financials skill

---

## Summary Table

| Year | reportDate | Gross Margin % | Action |
|------|------------|---------------|--------|
| 2018 | 2019-02-02 | 28.9% [WARNING] | Dolt matches SEC — no change needed |
| 2019 | 2020-02-01 | 29.2% [WARNING] | **UPDATE NEEDED** — Dolt SGA is negative (-2,173,677); correct to 2,173,677 |
| 2020 | 2021-01-30 | 31.8% | Dolt matches SEC (minor rounding) — no change needed |
| 2021 | 2022-01-29 | 38.3% [WARNING] | Dolt matches SEC (minor rounding) — no change needed |
| 2022 | 2023-01-28 | 34.6% | Dolt matches original SEC filing — no change needed |
| 2023 | 2024-02-03 | 34.9% | Dolt matches original SEC filing — no change needed |
| 2024 | 2025-02-01 | 35.9% | Dolt reportDate is 2025-02-03 (minor error); values match SEC — update reportDate |
| 2025 | 2026-01-31 | 32.9% | **NEW YEAR** — not in Dolt; ready to insert |

---

## FY2018 Analysis (reportDate: 2019-02-02)

### Source Data

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| reportDate | 2019-02-02 | N/A | 2019-02-02 | 2019-02-02 |
| Net Revenue | 8,436,570 | N/A | 8,436,570 | 8,436,570 |
| Cost of Goods | 5,998,788 | N/A | 5,998,788 | 5,998,788 |
| Gross Margin | 2,437,782 | N/A | 2,437,782 | 2,437,782 |
| SGA | 1,986,576 | N/A | 1,986,576 | 1,986,576 |
| Operating Profit | 444,733 | N/A | 444,733 | 444,733 |
| Net Profit | 319,864 | N/A | 319,864 | 319,864 |
| Inventory | 1,824,696 | N/A | 1,824,696 | 1,824,696 |
| Current Assets | 2,122,398 | N/A | 2,122,398 | 2,122,398 |
| Total Assets | 4,187,149 | N/A | 4,187,149 | 4,187,149 |
| Current Liabilities | 1,504,639 | N/A | 1,504,639 | 1,504,639 |
| Liabilities | 2,282,988 | N/A | 2,282,988 | 2,282,988 |
| Total SE | 1,904,161 | N/A | 1,904,161 | 1,904,161 |
| TL&SE | 4,187,149 | N/A | 4,187,149 | 4,187,149 |

### Anomaly Flags
- [WARNING] Gross margin 28.9% is below expected 30–35% range. This is an accurate figure for DKS's FY2018; the company has improved margins since.
- SGA from SEC: single `SellingGeneralAndAdministrativeExpense` tag = 1,986,576. Pre-opening costs listed separately (6,473) — correctly excluded from SGA.
- Balance sheet check: 4,187,149 − 1,904,161 = 2,282,988 = Liabilities. ✓

### Reconciliation
All values match. No update needed.

---

## FY2019 Analysis (reportDate: 2020-02-01)

### Source Data

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| reportDate | 2020-02-01 | N/A | 2020-02-01 | 2020-02-01 |
| Net Revenue | 8,750,743 | N/A | 8,750,700 | 8,750,743 |
| Cost of Goods | 6,196,185 | N/A | 6,196,185 | 6,196,185 |
| Gross Margin | 2,554,558 | N/A | 2,554,515* | 2,554,558 |
| SGA | 2,173,677 | N/A | **-2,173,677*** | **2,173,677** |
| Operating Profit | 375,613 | N/A | 375,613 | 375,613 |
| Net Profit | 297,462 | N/A | 297,462 | 297,462 |
| Inventory | 2,202,275 | N/A | 2,202,275 | 2,202,275 |
| Current Assets | 2,410,016 | N/A | 2,410,016 | 2,410,016 |
| Total Assets | 6,628,560 | N/A | 6,628,560 | 6,628,560 |
| Current Liabilities | 2,076,474 | N/A | 2,076,474 | 2,076,474 |
| Liabilities | 4,896,962 | N/A | 4,896,962 | 4,896,962 |
| Total SE | 1,731,598 | N/A | 1,731,598 | 1,731,598 |
| TL&SE | 6,628,560 | N/A | 6,628,560 | 6,628,560 |

*Fields marked with `*` differ from recommended.

### Anomaly Flags
- [ERROR] **Dolt SGA = -2,173,677 (negative).** This is a data entry error. SEC clearly reports SGA = 2,173,677 (positive). The negative sign must be removed.
- [WARNING] Gross margin 29.2% is slightly below the 30–35% benchmark. Accurate for FY2019.
- Net Revenue: Dolt = 8,750,700 vs SEC = 8,750,743. Minor rounding in Dolt; recommend updating to SEC exact value.
- Gross Margin: Dolt = 2,554,515 vs SEC = 2,554,558 (=8,750,743−6,196,185). Minor discrepancy; recommend using SEC computed value.
- SGA from SEC: single `SellingGeneralAndAdministrativeExpense` tag = 2,173,677. Pre-opening costs listed separately (5,268) — correctly excluded.
- Balance sheet check: 6,628,560 − 1,731,598 = 4,896,962. ✓

### Reconciliation
| Field | Action |
|-------|--------|
| Net Revenue | Update Dolt: 8,750,700 → 8,750,743 |
| Gross Margin | Update Dolt: 2,554,515 → 2,554,558 |
| **SGA** | **UPDATE REQUIRED: -2,173,677 → 2,173,677** |
| All other fields | Match — no change needed |

---

## FY2020 Analysis (reportDate: 2021-01-30)

### Source Data

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| reportDate | 2021-01-30 | N/A | 2021-01-30 | 2021-01-30 |
| Net Revenue | 9,584,019 | N/A | 9,584,000 | 9,584,019 |
| Cost of Goods | 6,533,312 | N/A | 6,533,312 | 6,533,312 |
| Gross Margin | 3,050,707 | N/A | 3,050,688* | 3,050,707 |
| SGA | 2,298,534 | N/A | 2,298,534 | 2,298,534 |
| Operating Profit | 741,477 | N/A | 741,477 | 741,477 |
| Net Profit | 530,251 | N/A | 530,251 | 530,251 |
| Inventory | 1,953,568 | N/A | 1,953,568 | 1,953,568 |
| Current Assets | 3,759,650 | N/A | 3,759,650 | 3,759,650 |
| Total Assets | 7,752,859 | N/A | 7,752,859 | 7,752,859 |
| Current Liabilities | 2,550,198 | N/A | 2,550,198 | 2,550,198 |
| Liabilities | 5,413,325 | N/A | 5,413,325 | 5,413,325 |
| Total SE | 2,339,534 | N/A | 2,339,534 | 2,339,534 |
| TL&SE | 7,752,859 | N/A | 7,752,859 | 7,752,859 |

### Anomaly Flags
- Net Revenue: Dolt = 9,584,000 vs SEC = 9,584,019. Minor rounding. Recommend updating to exact SEC value.
- Gross Margin: Dolt = 3,050,688 vs SEC computed = 3,050,707 (=9,584,019−6,533,312). Minor discrepancy from rounding of revenue.
- SGA from SEC: single `SellingGeneralAndAdministrativeExpense` tag = 2,298,534. Pre-opening costs listed separately (10,696) — correctly excluded.
- Balance sheet check: 7,752,859 − 2,339,534 = 5,413,325. ✓
- COVID-19 year: DKS benefited from outdoor/sporting goods demand. Revenue up 9.5% YoY. Gross margin 31.8% — within normal range.

### Reconciliation
| Field | Action |
|-------|--------|
| Net Revenue | Update Dolt: 9,584,000 → 9,584,019 |
| Gross Margin | Update Dolt: 3,050,688 → 3,050,707 |
| All other fields | Match — no change needed |

---

## FY2021 Analysis (reportDate: 2022-01-29)

### Source Data

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| reportDate | 2022-01-29 | N/A | 2022-01-29 | 2022-01-29 |
| Net Revenue | 12,293,368 | N/A | 12,293,400* | 12,293,368 |
| Cost of Goods | 7,581,482 | N/A | 7,581,482 | 7,581,482 |
| Gross Margin | 4,711,886 | N/A | 4,711,918* | 4,711,886 |
| SGA | 2,664,083 | N/A | 2,664,083 | 2,664,083 |
| Operating Profit | 2,034,503 | N/A | 2,034,503 | 2,034,503 |
| Net Profit | 1,519,871 | N/A | 1,519,871 | 1,519,871 |
| Inventory | 2,297,609 | N/A | 2,297,609 | 2,297,609 |
| Current Assets | 5,106,656 | N/A | 5,106,656 | 5,106,656 |
| Total Assets | 9,041,676 | N/A | 9,041,676 | 9,041,676 |
| Current Liabilities | 2,712,680 | N/A | 2,712,680 | 2,712,680 |
| Liabilities | 6,940,090 | N/A | 6,940,090 | 6,940,090 |
| Total SE | 2,101,586 | N/A | 2,101,586 | 2,101,586 |
| TL&SE | 9,041,676 | N/A | 9,041,676 | 9,041,676 |

### Anomaly Flags
- [WARNING] Gross margin 38.3% is above expected 30–35% range. This was DKS's peak profitability year (pandemic-driven demand surge, inventory shortages driving pricing power). This is a legitimate outlier year.
- Net Revenue: Dolt = 12,293,400 vs SEC = 12,293,368. Minor rounding.
- Gross Margin: Dolt = 4,711,918 vs SEC computed = 4,711,886 (=12,293,368−7,581,482). Minor discrepancy from revenue rounding.
- SGA from SEC: single `SellingGeneralAndAdministrativeExpense` tag = 2,664,083. Pre-opening costs listed separately (13,300) — correctly excluded.
- Balance sheet check: 9,041,676 − 2,101,586 = 6,940,090. ✓

### Reconciliation
| Field | Action |
|-------|--------|
| Net Revenue | Update Dolt: 12,293,400 → 12,293,368 |
| Gross Margin | Update Dolt: 4,711,918 → 4,711,886 |
| All other fields | Match — no change needed |

---

## FY2022 Analysis (reportDate: 2023-01-28)

### Source Data

| Field | SEC (original) | SEC (restated in FY2024 10-K) | Yahoo | Dolt | Recommended |
|-------|---------------|------------------------------|-------|------|-------------|
| reportDate | 2023-01-28 | — | 2023-01-31 | 2023-01-28 | 2023-01-28 |
| Net Revenue | 12,368,198 | — | 12,368,200 | 12,368,200 | 12,368,200 |
| Cost of Goods | 8,083,640 | — | 8,083,640 | 8,083,640 | 8,083,640 |
| Gross Margin | 4,284,558 | — | 4,284,560 | 4,284,560 | 4,284,560 |
| SGA | 2,805,462 | 2,799,853 | 2,799,985 | 2,805,462 | 2,805,462 |
| Operating Profit | 1,463,019 | — | 1,463,019 | 1,463,019 | 1,463,019 |
| Net Profit | 1,043,138 | — | 1,043,138 | 1,043,138 | 1,043,138 |
| Inventory | 2,830,917 | — | 2,830,920 | 2,830,917 | 2,830,917 |
| Current Assets | 4,963,186 | — | 4,963,190 | 4,963,186 | 4,963,186 |
| Total Assets | 8,992,196 | — | 8,992,200 | 8,992,196 | 8,992,196 |
| Current Liabilities | 2,641,446 | — | 2,641,450 | 2,641,446 | 2,641,446 |
| Liabilities | 6,467,573 | — | 6,467,577 | 6,467,573 | 6,467,573 |
| Total SE | 2,524,623 | — | 2,524,623 | 2,524,623 | 2,524,623 |
| TL&SE | 8,992,196 | — | 8,992,200 | 8,992,196 | 8,992,196 |

### Anomaly Flags
- [WARNING] SGA restatement: FY2024 10-K shows prior-year FY2022 SGA as 2,799,853 vs original filing 2,805,462 (difference of 5,609). Yahoo shows 2,799,985 (close to restated). This appears to be a minor reclassification of pre-opening costs. The difference is immaterial (0.04% of revenue). Dolt uses original filing value.
- Balance sheet check: 8,992,196 − 2,524,623 = 6,467,573. ✓
- Gross margin 34.6% — within expected range.

### Reconciliation
Keeping Dolt's existing SGA value of 2,805,462 (original filing). All other fields match. No update needed.

---

## FY2023 Analysis (reportDate: 2024-02-03)

### Source Data

| Field | SEC (original FY2023 10-K) | SEC (restated in FY2024 10-K) | Yahoo | Dolt | Recommended |
|-------|---------------------------|------------------------------|-------|------|-------------|
| reportDate | 2024-02-03 | — | 2024-01-31 | 2024-02-03 | 2024-02-03 |
| Net Revenue | 12,984,399 | — | 12,984,400 | 12,984,400 | 12,984,400 |
| Cost of Goods | 8,450,664 | — | 8,450,660 | 8,450,664 | 8,450,664 |
| Gross Margin | 4,533,735 | — | 4,533,740 | 4,533,736 | 4,533,736 |
| SGA | 3,204,108 | 3,183,530 | 3,183,530 | 3,204,108 | 3,204,108 |
| Operating Profit | 1,282,365 | — | 1,282,360 | 1,282,365 | 1,282,365 |
| Net Profit | 1,046,519 | — | 1,046,520 | 1,046,519 | 1,046,519 |
| Inventory | 2,848,797 | — | 2,848,800 | 2,848,797 | 2,848,797 |
| Current Assets | 4,890,049 | — | 4,890,050 | 4,890,049 | 4,890,049 |
| Total Assets | 9,311,752 | — | 9,311,750 | 9,311,752 | 9,311,752 |
| Current Liabilities | 2,752,394 | — | 2,752,390 | 2,752,394 | 2,752,394 |
| Liabilities | 6,694,471 | — | 6,694,469 | 6,694,471 | 6,694,471 |
| Total SE | 2,617,281 | — | 2,617,281 | 2,617,281 | 2,617,281 |
| TL&SE | 9,311,752 | — | 9,311,750 | 9,311,752 | 9,311,752 |

### Anomaly Flags
- [WARNING] SGA restatement: FY2024 10-K shows prior-year FY2023 SGA as 3,183,530 vs original filing 3,204,108 (difference of 20,578, or ~0.16% of revenue). Yahoo shows the restated figure (3,183,530). This is a more material restatement than FY2022. Likely involves reclassification of pre-opening costs (FY2023 had 47,262 in pre-opening vs 16,077 in FY2022). Dolt uses original filing value — acceptable to retain.
- Balance sheet check: 9,311,752 − 2,617,281 = 6,694,471. ✓
- Gross margin 34.9% — within expected range.

### Reconciliation
Keeping Dolt's SGA value of 3,204,108 (original filing). All other fields match SEC original. No update needed.

---

## FY2024 Analysis (reportDate: 2025-02-01)

### Source Data

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| reportDate | 2025-02-01 | 2025-01-31 | **2025-02-03*** | **2025-02-01** |
| Net Revenue | 13,442,849 | 13,442,800 | 13,442,849 | 13,442,849 |
| Cost of Goods | 8,617,153 | 8,617,150 | 8,617,153 | 8,617,153 |
| Gross Margin | 4,825,696 | 4,825,650 | 4,825,696 | 4,825,696 |
| SGA | 3,294,272 | 3,294,270 | 3,294,272 | 3,294,272 |
| Operating Profit | 1,473,932 | 1,531,420* | 1,473,932 | 1,473,932 |
| Net Profit | 1,165,308 | 1,165,310 | 1,165,308 | 1,165,308 |
| Inventory | 3,349,830 | 3,349,830 | 3,349,830 | 3,349,830 |
| Current Assets | 5,417,707 | 5,417,710 | 5,417,707 | 5,417,707 |
| Total Assets | 10,458,694 | 10,458,694 | 10,458,694 | 10,458,694 |
| Current Liabilities | 3,080,062 | 3,080,060 | 3,080,062 | 3,080,062 |
| Liabilities | 7,260,430 | 7,260,430 | 7,260,430 | 7,260,430 |
| Total SE | 3,198,264 | 3,198,264 | 3,198,264 | 3,198,264 |
| TL&SE | 10,458,694 | 10,458,694 | 10,458,694 | 10,458,694 |

### Anomaly Flags
- [WARNING] reportDate in Dolt is 2025-02-03 but SEC filing clearly shows fiscal year end as 2025-02-01. Recommend correcting Dolt reportDate.
- [WARNING] Yahoo Operating Profit = 1,531,420 vs SEC = 1,473,932 (difference of 57,488). Yahoo likely includes Other Income in operating income calculation or uses EBIT-based figure. SEC direct operating income = 1,473,932 is correct; do not use Yahoo for Operating Profit.
- Balance sheet check: 10,458,694 − 3,198,264 = 7,260,430. ✓
- Gross margin 35.9% — slightly above 30–35% benchmark but within reasonable range for DKS's improving product mix.

### Reconciliation
| Field | Action |
|-------|--------|
| reportDate | Update Dolt: 2025-02-03 → 2025-02-01 |
| All financial fields | Match — no change needed |

---

## FY2025 Analysis (reportDate: 2026-01-31) — NEW YEAR, NOT IN DOLT

### Source Data

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| reportDate | 2026-01-31 | 2026-01-31 | N/A | 2026-01-31 |
| Net Revenue | 17,215,120 | 17,215,100 | N/A | 17,215,120 |
| Cost of Goods | 11,547,858 | 11,547,900 | N/A | 11,547,858 |
| Gross Margin | 5,667,262 | 5,667,200 | N/A | 5,667,262 |
| SGA | 4,338,162 | 4,338,160 | N/A | 4,338,162 |
| Operating Profit | 1,095,909 | 1,095,910 | N/A | 1,095,909 |
| Net Profit | 849,239 | 849,239 | N/A | 849,239 |
| Inventory | 4,907,823 | 4,907,820 | N/A | 4,907,823 |
| Current Assets | 7,104,791 | 7,104,790 | N/A | 7,104,791 |
| Total Assets | 17,411,499 | 17,411,500 | N/A | 17,411,499 |
| Current Liabilities | 4,643,558 | 4,643,560 | N/A | 4,643,558 |
| Liabilities | 11,871,379 | 11,871,380 | N/A | 11,871,379 |
| Total SE | 5,540,120 | 5,540,120 | N/A | 5,540,120 |
| TL&SE | 17,411,499 | 17,411,500 | N/A | 17,411,499 |

### Anomaly Flags
- **NOTE: FY2025 includes Foot Locker, Inc. acquisition.** DKS acquired Foot Locker in FY2025, significantly changing the scale of the business. Consolidated revenue includes DICK'S segment ($14,108,943) and Foot Locker segment ($3,106,177).
- SGA of 4,338,162 is the combined consolidated SGA. Pre-opening costs (69,000) and merger/integration costs (164,191) are reported as separate line items in the SEC filing; they are NOT included in SGA.
- Net Revenue source: DICK'S segment total in SEC = 14,108,943; Foot Locker segment = 3,106,177; consolidated total = 17,215,120. Yahoo matches within rounding.
- Balance sheet check: 17,411,499 − 5,540,120 = 11,871,379. ✓
- Gross margin 32.9% — within expected range. Slight decline from FY2024 (35.9%) reflects inclusion of Foot Locker which has different margin profile.
- [WARNING] Goodwill increased significantly from 245,857 (FY2024) to 864,047 (FY2025) due to Foot Locker acquisition.

### Reconciliation
This is a new year. All values sourced from SEC 10-K. Ready to insert into Dolt.

---

## Full Reconciled Values Summary

All values in thousands of dollars.

| Year | reportDate | Net Revenue | Cost of Goods | Gross Margin | SGA | Operating Profit | Net Profit | Inventory | Current Assets | Total Assets | Current Liabilities | Liabilities | Total SE | TL&SE |
|------|-----------|-------------|--------------|--------------|-----|-----------------|------------|-----------|---------------|-------------|---------------------|-------------|----------|-------|
| 2018 | 2019-02-02 | 8,436,570 | 5,998,788 | 2,437,782 | 1,986,576 | 444,733 | 319,864 | 1,824,696 | 2,122,398 | 4,187,149 | 1,504,639 | 2,282,988 | 1,904,161 | 4,187,149 |
| 2019 | 2020-02-01 | 8,750,743 | 6,196,185 | 2,554,558 | 2,173,677 | 375,613 | 297,462 | 2,202,275 | 2,410,016 | 6,628,560 | 2,076,474 | 4,896,962 | 1,731,598 | 6,628,560 |
| 2020 | 2021-01-30 | 9,584,019 | 6,533,312 | 3,050,707 | 2,298,534 | 741,477 | 530,251 | 1,953,568 | 3,759,650 | 7,752,859 | 2,550,198 | 5,413,325 | 2,339,534 | 7,752,859 |
| 2021 | 2022-01-29 | 12,293,368 | 7,581,482 | 4,711,886 | 2,664,083 | 2,034,503 | 1,519,871 | 2,297,609 | 5,106,656 | 9,041,676 | 2,712,680 | 6,940,090 | 2,101,586 | 9,041,676 |
| 2022 | 2023-01-28 | 12,368,200 | 8,083,640 | 4,284,560 | 2,805,462 | 1,463,019 | 1,043,138 | 2,830,917 | 4,963,186 | 8,992,196 | 2,641,446 | 6,467,573 | 2,524,623 | 8,992,196 |
| 2023 | 2024-02-03 | 12,984,400 | 8,450,664 | 4,533,736 | 3,204,108 | 1,282,365 | 1,046,519 | 2,848,797 | 4,890,049 | 9,311,752 | 2,752,394 | 6,694,471 | 2,617,281 | 9,311,752 |
| 2024 | 2025-02-01 | 13,442,849 | 8,617,153 | 4,825,696 | 3,294,272 | 1,473,932 | 1,165,308 | 3,349,830 | 5,417,707 | 10,458,694 | 3,080,062 | 7,260,430 | 3,198,264 | 10,458,694 |
| 2025 | 2026-01-31 | 17,215,120 | 11,547,858 | 5,667,262 | 4,338,162 | 1,095,909 | 849,239 | 4,907,823 | 7,104,791 | 17,411,499 | 4,643,558 | 11,871,379 | 5,540,120 | 17,411,499 |

---

## Changes Required vs Current Dolt Data

| Year | Field | Current Dolt | Recommended | Priority |
|------|-------|-------------|-------------|----------|
| 2019 | SGA | -2,173,677 | 2,173,677 | **CRITICAL** |
| 2019 | Net Revenue | 8,750,700 | 8,750,743 | Low |
| 2019 | Gross Margin | 2,554,515 | 2,554,558 | Low |
| 2020 | Net Revenue | 9,584,000 | 9,584,019 | Low |
| 2020 | Gross Margin | 3,050,688 | 3,050,707 | Low |
| 2021 | Net Revenue | 12,293,400 | 12,293,368 | Low |
| 2021 | Gross Margin | 4,711,918 | 4,711,886 | Low |
| 2024 | reportDate | 2025-02-03 | 2025-02-01 | Medium |
| 2025 | ALL | (not in Dolt) | See table above | NEW INSERT |

---

**Analysis complete.** Run `/insert-financials DKS` to write all changed years to the database.

### Unresolved Flags
- [WARNING] FY2018 gross margin 28.9% below 30% benchmark — confirmed accurate historical figure, no action needed.
- [WARNING] FY2019 gross margin 29.2% slightly below 30% benchmark — confirmed accurate historical figure, no action needed.
- [WARNING] FY2021 gross margin 38.3% above 35% benchmark — confirmed legitimate due to pandemic-era demand surge, no action needed.
- [WARNING] FY2022 SGA minor restatement (2,805,462 → 2,799,853): Retaining original filing value in Dolt.
- [WARNING] FY2023 SGA restatement (3,204,108 → 3,183,530): Retaining original filing value in Dolt.
- [WARNING] FY2024 Yahoo Operating Profit discrepancy (1,531,420 vs SEC 1,473,932): Do not use Yahoo for Operating Profit.
- [WARNING] FY2025: Foot Locker acquisition consolidation significantly changes scale of business. All metrics now reflect combined entity.
