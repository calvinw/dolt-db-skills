# Williams-Sonoma (WSM) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2019-02-03 | Correction: SGA −1,665,060K → +1,665,060K (sign error) |
| 2019 | 2020-02-02 | No change |
| 2020 | 2021-01-31 | No change |
| 2021 | 2022-01-30 | No change |
| 2022 | 2023-01-29 | No change |
| 2023 | 2024-01-28 | No change |
| 2024 | 2025-02-02 | Correction: reportDate 2025-01-28 → 2025-02-02 |
| 2025 | 2026-02-01 | New insert |

---

## Company Background

**Segment:** Specialty (home furnishings, kitchen, décor) — brands: Williams-Sonoma, Pottery Barn, West Elm, Pottery Barn Kids/Teens, Rejuvenation.

**Fiscal year:** Ends on the Sunday nearest February 1 (varies: may fall in late January or early February). DB year = reportDate year − 1. Example: reportDate 2026-02-01 → Dolt year=2025.

**SGA:** Single combined `us-gaap_SellingGeneralAndAdministrativeExpense` line. Use directly. No composite rule needed.

**COGS:** Older filings use `wsm_CostOfGoodsSoldAndOccupancyExpenses`; newer filings use `us-gaap_CostOfRevenue`. Both represent the same single "Cost of goods sold" line (inclusive of store occupancy). COGS and Gross are unaffected by the tag change.

**Gross margin benchmark:** 36–47% for home/kitchen specialty (within anomaly-rules.md specialty range of 35–55%).

**ASC 842 adoption:** FY2019 (reportDate 2020-02-02) — large jump in Total Assets (~$1.2B) from operating lease ROU assets being added to the balance sheet. Not an error.

**No NCI:** WSM has no noncontrolling interest. TSE = `us-gaap_StockholdersEquity`.

---

## FY2018 (reportDate: 2019-02-03)

**Sources:** Dolt existing; SEC not fetched for FY2018 directly. Internal consistency verified.

### Anomaly Flags

**[ERROR] SGA stored as negative: −1,665,060K → should be +1,665,060K.**
- Magnitude is clearly correct: Gross(2,101,013) − |SGA|(1,665,060) = 435,953 = OpInc ✓
- This is a sign error introduced at data entry — expenses were entered with the SEC income statement sign convention (negative) instead of the DB convention (positive).
- Correction: −1,665,060K → +1,665,060K.

Balance sheet identity: 2,812,844 − 1,155,714 = 1,657,130K = Liab ✓
Gross margin: 2,101,013 / 5,671,593 = 37.0% ✓ (within specialty range)

### Side-by-Side Comparison (thousands)

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Revenue | N/A | N/A | 5,671,593 | 5,671,593 |
| COGS | N/A | N/A | 3,570,580 | 3,570,580 |
| Gross | N/A | N/A | 2,101,013 | 2,101,013 |
| SGA | N/A | N/A | **−1,665,060 [ERROR]** | **+1,665,060** |
| OpInc | N/A | N/A | 435,953 | 435,953 |
| NetInc | N/A | N/A | 333,684 | 333,684 |
| Inventory | N/A | N/A | 1,124,992 | 1,124,992 |
| Current Assets | N/A | N/A | 1,694,343 | 1,694,343 |
| Total Assets | N/A | N/A | 2,812,844 | 2,812,844 |
| Current Liab | N/A | N/A | 1,074,812 | 1,074,812 |
| Liabilities | N/A | N/A | 1,657,130 | 1,657,130 |
| TSE | N/A | N/A | 1,155,714 | 1,155,714 |
| TL+SE | N/A | N/A | 2,812,844 | 2,812,844 |

### Reconciled Recommendation — FY2018
**Correction required:** SGA sign only. All other fields unchanged.

| Field | Value |
|-------|-------|
| company_name | 'Williams-Sonoma' |
| year | 2018 |
| reportDate | '2019-02-03' |
| Net Revenue | 5,671,593 |
| Cost of Goods | 3,570,580 |
| Gross Margin | 2,101,013 |
| SGA | **1,665,060** |
| Operating Profit | 435,953 |
| Net Profit | 333,684 |
| Inventory | 1,124,992 |
| Current Assets | 1,694,343 |
| Total Assets | 2,812,844 |
| Current Liabilities | 1,074,812 |
| Liabilities | 1,657,130 |
| Total Shareholder Equity | 1,155,714 |
| Total Liabilities and SE | 2,812,844 |

---

## FY2019 (reportDate: 2020-02-02)

**Sources:** Dolt existing. SEC not fetched for FY2019 directly. Internal consistency verified.

### Anomaly Flags
- Balance sheet identity: 4,054,042 − 1,235,860 = 2,818,182K = Liab ✓
- ASC 842 adoption: TA jumped from 2,812,844K (FY2018) to 4,054,042K (FY2019), a $1.24B increase from operating lease ROU assets added. Expected, not an error.
- Gross margin: 2,139,092 / 5,898,008 = 36.3% ✓
- Income statement check: Revenue(5,898,008) − COGS(3,758,916) = Gross(2,139,092); Gross − SGA(1,673,218) = OpInc(465,874) ✓

### Side-by-Side Comparison (thousands)

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Revenue | N/A | N/A | 5,898,008 | 5,898,008 |
| COGS | N/A | N/A | 3,758,916 | 3,758,916 |
| Gross | N/A | N/A | 2,139,092 | 2,139,092 |
| SGA | N/A | N/A | 1,673,218 | 1,673,218 |
| OpInc | N/A | N/A | 465,874 | 465,874 |
| NetInc | N/A | N/A | 356,062 | 356,062 |
| Inventory | N/A | N/A | 1,100,544 | 1,100,544 |
| Current Assets | N/A | N/A | 1,755,635 | 1,755,635 |
| Total Assets | N/A | N/A | 4,054,042 | 4,054,042 |
| Current Liab | N/A | N/A | 1,609,555 | 1,609,555 |
| Liabilities | N/A | N/A | 2,818,182 | 2,818,182 |
| TSE | N/A | N/A | 1,235,860 | 1,235,860 |
| TL+SE | N/A | N/A | 4,054,042 | 4,054,042 |

### Reconciled Recommendation — FY2019
Internally consistent. **No change.**

---

## FY2020 (reportDate: 2021-01-31)

**Source:** SEC FY2022 10-K (year=2022) — 2021-01-31 comparative column (income statement); balance sheet not verifiable from available SEC data.

### Anomaly Flags
- Balance sheet identity: 4,661,424 − 1,651,185 = 3,010,239K = Liab ✓
- Gross margin: 2,636,269 / 6,783,189 = 38.9% ✓

### Side-by-Side Comparison (thousands)

| Field | SEC (FY2022 comparative) | Yahoo | Dolt | Recommended |
|-------|--------------------------|-------|------|-------------|
| Revenue | 6,783,189 | N/A | 6,783,189 | 6,783,189 |
| COGS | 4,146,920 | N/A | 4,146,920 | 4,146,920 |
| Gross | 2,636,269 | N/A | 2,636,269 | 2,636,269 |
| SGA | 1,725,572 | N/A | 1,725,572 | 1,725,572 |
| OpInc | 910,697 | N/A | 910,697 | 910,697 |
| NetInc | 680,714 | N/A | 680,714 | 680,714 |
| Inventory | N/A | N/A | 1,006,299 | 1,006,299 |
| Current Assets | N/A | N/A | 2,467,080 | 2,467,080 |
| Total Assets | N/A | N/A | 4,661,424 | 4,661,424 |
| Current Liab | N/A | N/A | 1,848,000 | 1,848,000 |
| Liabilities | N/A | N/A | 3,010,239 | 3,010,239 |
| TSE | N/A | N/A | 1,651,185 | 1,651,185 |
| TL+SE | N/A | N/A | 4,661,424 | 4,661,424 |

### Reconciled Recommendation — FY2020
Income statement verified from SEC FY2022 10-K comparative (exact match). Balance sheet accepted as-is (identity holds). **No change.**

---

## FY2021 (reportDate: 2022-01-30)

**Source:** SEC FY2022 10-K (year=2022) — 2022-01-30 comparative column; both income statement and balance sheet verified.

### Anomaly Flags
- Balance sheet identity: 4,625,620 − 1,664,207 = 2,961,413K = Liab ✓
- Gross margin: 3,631,963 / 8,245,936 = 44.0% ✓

### Side-by-Side Comparison (thousands)

| Field | SEC (FY2022 comparative) | Yahoo | Dolt | Recommended |
|-------|--------------------------|-------|------|-------------|
| Revenue | 8,245,936 | NaN | 8,245,936 | 8,245,936 |
| COGS | 4,613,973 | NaN | 4,613,973 | 4,613,973 |
| Gross | 3,631,963 | NaN | 3,631,963 | 3,631,963 |
| SGA | 2,178,847 | NaN | 2,178,847 | 2,178,847 |
| OpInc | 1,453,116 | NaN | 1,453,116 | 1,453,116 |
| NetInc | 1,126,337 | NaN | 1,126,337 | 1,126,337 |
| Inventory | 1,246,372 | NaN | 1,246,372 | 1,246,372 |
| Current Assets | 2,323,894 | NaN | 2,323,894 | 2,323,894 |
| Total Assets | 4,625,620 | NaN | 4,625,620 | 4,625,620 |
| Current Liab | 1,771,686 | NaN | 1,771,686 | 1,771,686 |
| Liabilities | 2,961,413 | NaN | 2,961,413 | 2,961,413 |
| TSE | 1,664,207 | NaN | 1,664,207 | 1,664,207 |
| TL+SE | 4,625,620 | NaN | 4,625,620 | 4,625,620 |

### Reconciled Recommendation — FY2021
All fields verified from SEC FY2022 10-K. **No change.**

---

## FY2022 (reportDate: 2023-01-29)

**Source:** SEC FY2022 10-K (year=2022) — primary column (2023-01-29); Yahoo Finance; Dolt existing.

### Anomaly Flags
- Balance sheet identity: 4,663,016 − 1,701,051 = 2,961,965K = Liab ✓
- Gross margin: 3,677,733 / 8,674,417 = 42.4% ✓

### Side-by-Side Comparison (thousands)

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Revenue | 8,674,417 | 8,674,420 | 8,674,417 | 8,674,417 |
| COGS | 4,996,684 | 4,996,680 | 4,996,684 | 4,996,684 |
| Gross | 3,677,733 | 3,677,730 | 3,677,733 | 3,677,733 |
| SGA | 2,179,311 | 2,179,310 | 2,179,311 | 2,179,311 |
| OpInc | 1,498,422 | 1,498,420 | 1,498,422 | 1,498,422 |
| NetInc | 1,127,904 | 1,127,900 | 1,127,904 | 1,127,904 |
| Inventory | 1,456,123 | 1,456,120 | 1,456,123 | 1,456,123 |
| Current Assets | 2,036,080 | 2,036,080 | 2,036,080 | 2,036,080 |
| Total Assets | 4,663,016 | 4,663,020 | 4,663,016 | 4,663,016 |
| Current Liab | 1,636,451 | 1,636,450 | 1,636,451 | 1,636,451 |
| Liabilities | 2,961,965 | N/A | 2,961,965 | 2,961,965 |
| TSE | 1,701,051 | 1,701,050 | 1,701,051 | 1,701,051 |
| TL+SE | 4,663,016 | 4,663,020 | 4,663,016 | 4,663,016 |

### Reconciled Recommendation — FY2022
All fields verified from SEC FY2022 10-K (exact match; Yahoo differs only by rounding). **No change.**

---

## FY2023 (reportDate: 2024-01-28)

**Source:** SEC FY2025 10-K (year=2025) — 2024-01-28 comparative column (income statement); Yahoo Finance; Dolt existing.

### Anomaly Flags
- Balance sheet identity: 5,273,548 − 2,127,861 = 3,145,687K = Liab ✓
- Gross margin: 3,303,601 / 7,750,652 = 42.6% ✓

### Side-by-Side Comparison (thousands)

| Field | SEC (FY2025 comparative) | Yahoo | Dolt | Recommended |
|-------|--------------------------|-------|------|-------------|
| Revenue | 7,750,652 | 7,750,650 | 7,750,652 | 7,750,652 |
| COGS | 4,447,051 | 4,447,050 | 4,447,051 | 4,447,051 |
| Gross | 3,303,601 | 3,303,600 | 3,303,601 | 3,303,601 |
| SGA | 2,059,408 | 2,059,410 | 2,059,408 | 2,059,408 |
| OpInc | 1,244,193 | 1,244,190 | 1,244,193 | 1,244,193 |
| NetInc | 949,762 | 949,762 | 949,762 | 949,762 |
| Inventory | N/A | 1,246,370 | 1,246,369 | 1,246,369 |
| Current Assets | N/A | 2,719,800 | 2,719,797 | 2,719,797 |
| Total Assets | N/A | 5,273,550 | 5,273,548 | 5,273,548 |
| Current Liab | N/A | 1,880,320 | 1,880,315 | 1,880,315 |
| Liabilities | N/A | N/A | 3,145,687 | 3,145,687 |
| TSE | N/A | 2,127,860 | 2,127,861 | 2,127,861 |
| TL+SE | N/A | 5,273,550 | 5,273,548 | 5,273,548 |

### Reconciled Recommendation — FY2023
Income statement verified from SEC FY2025 10-K comparative. Balance sheet matches Yahoo (minor rounding). **No change.**

---

## FY2024 (reportDate: 2025-02-02)

**Source:** SEC FY2025 10-K (year=2025) — 2025-02-02 comparative column; Yahoo Finance (2025-01-31 approx); Dolt existing.

### Anomaly Flags

**[WARNING→Correction] reportDate error:** Dolt has 2025-01-28. SEC FY2025 10-K shows the period header for FY2024 as 2025-02-02. WSM's fiscal year ends the Sunday nearest February 1; in 2025, February 2 was that Sunday. Dolt's 2025-01-28 is incorrect.

All financial data is correct — only the reportDate needs updating.

- Balance sheet identity: 5,301,607 − 2,142,419 = 3,159,188K = Liab ✓
- Gross margin: 3,582,299 / 7,711,541 = 46.5% ✓

### Side-by-Side Comparison (thousands)

| Field | SEC (2025-02-02) | Yahoo (2025-01-31 approx) | Dolt (current) | Recommended |
|-------|-----------------|--------------------------|----------------|-------------|
| reportDate | **2025-02-02** | 2025-01-31 | **2025-01-28 [ERR]** | **2025-02-02** |
| Revenue | 7,711,541 | 7,711,540 | 7,711,541 | 7,711,541 |
| COGS | 4,129,242 | 4,129,240 | 4,129,242 | 4,129,242 |
| Gross | 3,582,299 | 3,582,300 | 3,582,299 | 3,582,299 |
| SGA | 2,152,115 | 2,152,120 | 2,152,115 | 2,152,115 |
| OpInc | 1,430,184 | 1,430,180 | 1,430,184 | 1,430,184 |
| NetInc | 1,125,251 | 1,125,250 | 1,125,251 | 1,125,251 |
| Inventory | 1,332,429 | 1,332,430 | 1,332,429 | 1,332,429 |
| Current Assets | 2,754,609 | 2,754,610 | 2,754,609 | 2,754,609 |
| Total Assets | 5,301,607 | 5,301,610 | 5,301,607 | 5,301,607 |
| Current Liab | 1,911,974 | 1,911,970 | 1,911,974 | 1,911,974 |
| Liabilities | 3,159,188 | N/A | 3,159,188 | 3,159,188 |
| TSE | 2,142,419 | 2,142,420 | 2,142,419 | 2,142,419 |
| TL+SE | 5,301,607 | 5,301,610 | 5,301,607 | 5,301,607 |

### Reconciled Recommendation — FY2024
**Correction required:** reportDate 2025-01-28 → 2025-02-02. All financial values unchanged.

| Field | Value |
|-------|-------|
| company_name | 'Williams-Sonoma' |
| year | 2024 |
| reportDate | **'2025-02-02'** |
| Net Revenue | 7,711,541 |
| Cost of Goods | 4,129,242 |
| Gross Margin | 3,582,299 |
| SGA | 2,152,115 |
| Operating Profit | 1,430,184 |
| Net Profit | 1,125,251 |
| Inventory | 1,332,429 |
| Current Assets | 2,754,609 |
| Total Assets | 5,301,607 |
| Current Liabilities | 1,911,974 |
| Liabilities | 3,159,188 |
| Total Shareholder Equity | 2,142,419 |
| Total Liabilities and SE | 5,301,607 |

---

## FY2025 (reportDate: 2026-02-01)

**Source:** SEC FY2025 10-K (year=2025) — primary column (2026-02-01); Yahoo Finance; no Dolt row exists.

### Anomaly Flags
- Balance sheet identity: 5,411,912 − 2,082,559 = 3,329,353K = Liab ✓
- Gross margin: 3,603,051 / 7,806,816 = 46.2% ✓ (within specialty range)
- No NCI. TSE = `us-gaap_StockholdersEquity` = 2,082,559K.
- Large inventory ($1.46B) — expected for specialty home goods retailer ✓

### SEC Income Statement FY2025
- Revenue: `us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax` = 7,806,816K
- COGS: `us-gaap_CostOfRevenue` = 4,203,765K
- Gross: `us-gaap_GrossProfit` = 3,603,051K
- SGA: `us-gaap_SellingGeneralAndAdministrativeExpense` = 2,187,329K
- OpInc: `us-gaap_OperatingIncomeLoss` = 1,415,722K
- NetInc: `us-gaap_NetIncomeLoss` = 1,088,437K

### Side-by-Side Comparison (thousands)

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Revenue | 7,806,816 | 7,806,820 | — | 7,806,816 |
| COGS | 4,203,765 | 4,203,760 | — | 4,203,765 |
| Gross | 3,603,051 | 3,603,050 | — | 3,603,051 |
| SGA | 2,187,329 | 2,187,330 | — | 2,187,329 |
| OpInc | 1,415,722 | 1,415,720 | — | 1,415,722 |
| NetInc | 1,088,437 | 1,088,440 | — | 1,088,437 |
| Inventory | 1,462,849 | 1,462,850 | — | 1,462,849 |
| Current Assets | 2,713,187 | 2,713,190 | — | 2,713,187 |
| Total Assets | 5,411,912 | 5,411,910 | — | 5,411,912 |
| Current Liab | 1,954,130 | 1,954,130 | — | 1,954,130 |
| Liabilities | 3,329,353 | N/A | — | 3,329,353 |
| TSE | 2,082,559 | 2,082,560 | — | 2,082,559 |
| TL+SE | 5,411,912 | 5,411,910 | — | 5,411,912 |

### Reconciled Recommendation — FY2025
New insert. All values from SEC FY2025 10-K; confirmed by Yahoo (minor rounding only).

| Field | Value |
|-------|-------|
| company_name | 'Williams-Sonoma' |
| year | 2025 |
| reportDate | '2026-02-01' |
| Net Revenue | 7,806,816 |
| Cost of Goods | 4,203,765 |
| Gross Margin | 3,603,051 |
| SGA | 2,187,329 |
| Operating Profit | 1,415,722 |
| Net Profit | 1,088,437 |
| Inventory | 1,462,849 |
| Current Assets | 2,713,187 |
| Total Assets | 5,411,912 |
| Current Liabilities | 1,954,130 |
| Liabilities | 3,329,353 |
| Total Shareholder Equity | 2,082,559 |
| Total Liabilities and SE | 5,411,912 |

---

## Analysis Complete

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql WSM` to write all changed years to the database.

**Years requiring changes (3 of 8):**
1. **FY2018** — Correction: SGA sign error −1,665,060K → +1,665,060K
2. **FY2024** — Correction: reportDate 2025-01-28 → 2025-02-02 (financial data unchanged)
3. **FY2025** — New insert

**Years with no change (5 of 8):** 2019, 2020, 2021, 2022, 2023
