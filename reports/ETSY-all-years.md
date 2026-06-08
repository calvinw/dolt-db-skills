# Etsy (ETSY) — FY2018–FY2024 Financial Analysis

**Generated:** 2026-06-06
**Source:** /verify-dolt-db-financials skill

---

## Summary

| Year | reportDate | Action | Notes |
|------|-----------|--------|-------|
| 2018 | 2018-12-31 | No change | All values confirmed |
| 2019 | 2019-12-31 | No change | All values confirmed |
| 2020 | 2020-12-31 | No change | All values confirmed |
| 2021 | 2021-12-31 | No change | All values confirmed |
| 2022 | 2022-12-31 | No change | All values confirmed |
| 2023 | 2023-12-31 | No change | All values confirmed |
| 2024 | 2024-12-31 | No change | All values confirmed |

**New data available:** FY2025 (reportDate 2025-12-31) is available from SEC and Yahoo but not yet in the Dolt DB. Use `/download-new-year-data ETSY` to add it.

---

## FY2018 — Analysis

### Anomaly Checks

- **SGA (Rule 4):** No combined `us-gaap_SellingGeneralAndAdministrativeExpense` tag. SEC has separate `SellingAndMarketingExpense` (158,013K) and `GeneralAndAdministrativeExpense` (82,883K). SGA = 158,013 + 82,883 = 240,896K. ✓
- **Inventory:** NULL — correct for a pure marketplace company.
- **Balance sheet identity:** 901,851K = 901,851K ✓
- **Gross margin:** 68.4% — high but normal for marketplace (revenue net of seller payouts). No WARNING.
- **Total Shareholder Equity:** 400,898K — positive, no WARNING.

### Comparison Table

Values in thousands USD.

| Field | SEC | Dolt | Recommended |
|-------|-----|------|-------------|
| Net Revenue | 603,693 | 603,693 | 603,693 |
| Cost of Goods | 190,762 | 190,762 | 190,762 |
| Gross Margin | 412,931 | 412,931 | 412,931 |
| SGA | 240,896 | 240,896 | 240,896 |
| Operating Profit | 74,786 | 74,786 | 74,786 |
| Net Profit | 77,491 | 77,491 | 77,491 |
| Inventory | NULL | NULL | NULL |
| Current Assets | 680,289 | 680,289 | 680,289 |
| Total Assets | 901,851 | 901,851 | 901,851 |
| Current Liabilities | 112,062 | 112,062 | 112,062 |
| Liabilities | 500,953 | 500,953 | 500,953 |
| Total Shareholder Equity | 400,898 | 400,898 | 400,898 |
| Total Liabilities and SE | 901,851 | 901,851 | 901,851 |

### Reconciliation

All fields match perfectly between SEC and Dolt. No changes needed.

---

## FY2019 — Analysis

### Anomaly Checks

- **SGA (Rule 4):** SellingAndMarketingExpense (215,570K) + GeneralAndAdministrativeExpense (121,134K) = 336,704K. ✓
- **Inventory:** NULL — correct.
- **Balance sheet identity:** 1,542,352K = 1,542,352K ✓
- **Gross margin:** 66.9% — normal for marketplace.
- **Total Shareholder Equity:** 406,634K — positive.

### Comparison Table

Values in thousands USD.

| Field | SEC | Dolt | Recommended |
|-------|-----|------|-------------|
| Net Revenue | 818,379 | 818,379 | 818,379 |
| Cost of Goods | 271,036 | 271,036 | 271,036 |
| Gross Margin | 547,343 | 547,343 | 547,343 |
| SGA | 336,704 | 336,704 | 336,704 |
| Operating Profit | 88,761 | 88,761 | 88,761 |
| Net Profit | 95,894 | 95,894 | 95,894 |
| Inventory | NULL | NULL | NULL |
| Current Assets | 921,038 | 921,038 | 921,038 |
| Total Assets | 1,542,352 | 1,542,352 | 1,542,352 |
| Current Liabilities | 188,528 | 188,528 | 188,528 |
| Liabilities | 1,135,718 | 1,135,718 | 1,135,718 |
| Total Shareholder Equity | 406,634 | 406,634 | 406,634 |
| Total Liabilities and SE | 1,542,352 | 1,542,352 | 1,542,352 |

### Reconciliation

All fields match perfectly. No changes needed.

---

## FY2020 — Analysis

### Anomaly Checks

- **SGA (Rule 4):** SellingAndMarketingExpense (500,756K) + GeneralAndAdministrativeExpense (156,035K) = 656,791K. ✓
- **Inventory:** NULL — correct.
- **Balance sheet identity:** 2,404,489K = 2,404,489K ✓
- **Gross margin:** 73.1% — normal for marketplace.
- **Total Shareholder Equity:** 742,424K — positive.
- **COVID year:** Revenue surge to 1,725,625K (+111% YoY). Consistent across sources.

### Comparison Table

Values in thousands USD.

| Field | SEC | Dolt | Recommended |
|-------|-----|------|-------------|
| Net Revenue | 1,725,625 | 1,725,625 | 1,725,625 |
| Cost of Goods | 464,745 | 464,745 | 464,745 |
| Gross Margin | 1,260,880 | 1,260,880 | 1,260,880 |
| SGA | 656,791 | 656,791 | 656,791 |
| Operating Profit | 424,009 | 424,009 | 424,009 |
| Net Profit | 349,246 | 349,246 | 349,246 |
| Inventory | NULL | NULL | NULL |
| Current Assets | 1,894,781 | 1,894,781 | 1,894,781 |
| Total Assets | 2,404,489 | 2,404,489 | 2,404,489 |
| Current Liabilities | 454,664 | 454,664 | 454,664 |
| Liabilities | 1,662,065 | 1,662,065 | 1,662,065 |
| Total Shareholder Equity | 742,424 | 742,424 | 742,424 |
| Total Liabilities and SE | 2,404,489 | 2,404,489 | 2,404,489 |

### Reconciliation

All fields match perfectly. No changes needed.

---

## FY2021 — Analysis

### Anomaly Checks

- **SGA (Rule 4):** SellingAndMarketingExpense (654,804K) + GeneralAndAdministrativeExpense (282,531K) = 937,335K. ✓
- **Inventory:** NULL — correct.
- **Balance sheet identity:** 3,831,809K = 3,831,809K ✓
- **Gross margin:** 71.9% — normal for marketplace.
- **Total Shareholder Equity:** 628,619K — positive (but declining from 2020).
- **Acquisitions:** Depop and Elo7 acquired (goodwill increased to 1,371,064K).

### Comparison Table

Values in thousands USD.

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 2,329,114 | 2,329,114 | 2,329,114 | 2,329,114 |
| Cost of Goods | 654,512 | 654,512 | 654,512 | 654,512 |
| Gross Margin | 1,674,602 | 1,674,602 | 1,674,602 | 1,674,602 |
| SGA | 937,335 | 937,335 | 937,335 | 937,335 |
| Operating Profit | 465,732 | 465,732 | 465,732 | 465,732 |
| Net Profit | 493,507 | 493,507 | 493,507 | 493,507 |
| Inventory | NULL | NULL | NULL | NULL |
| Current Assets | 1,341,501 | 1,341,501 | 1,341,501 | 1,341,501 |
| Total Assets | 3,831,809 | 3,831,809 | 3,831,809 | 3,831,809 |
| Current Liabilities | 615,588 | 615,588 | 615,588 | 615,588 |
| Liabilities | 3,203,190 | 3,203,190 | 3,203,190 | 3,203,190 |
| Total Shareholder Equity | 628,619 | 628,619 | 628,619 | 628,619 |
| Total Liabilities and SE | 3,831,809 | 3,831,809 | 3,831,809 | 3,831,809 |

### Reconciliation

All fields match perfectly across all sources. No changes needed.

---

## FY2022 — Analysis

### Anomaly Checks

- **SGA (Rule 4):** SellingAndMarketingExpense (710,399K) + GeneralAndAdministrativeExpense (312,260K) = 1,022,659K. ✓
- **Inventory:** NULL — correct.
- **Balance sheet identity:** 2,634,961K = 2,634,961K ✓
- **Gross margin:** 71.0% — normal for marketplace.
- **Total Shareholder Equity:** -547,274K — **[WARNING]** Negative equity. Valid—Etsy has $2.3B in long-term debt. Confirmed.
- **Goodwill impairment:** $1,045,022K impairment (Depop + Elo7). Operating Profit = -658,560K (correctly includes impairment).

### Comparison Table

Values in thousands USD.

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 2,566,111 | 2,566,110 | 2,566,111 | 2,566,111 |
| Cost of Goods | 744,592 | 744,592 | 744,592 | 744,592 |
| Gross Margin | 1,821,519 | 1,821,518 | 1,821,519 | 1,821,519 |
| SGA | 1,022,659 | 1,022,660 | 1,022,659 | 1,022,659 |
| Operating Profit | -658,560 | -658,560 | -658,560 | -658,560 |
| Net Profit | -694,288 | -694,288 | -694,288 | -694,288 |
| Inventory | NULL | NULL | NULL | NULL |
| Current Assets | 1,513,743 | 1,513,740 | 1,513,743 | 1,513,743 |
| Total Assets | 2,634,961 | 2,634,960 | 2,634,961 | 2,634,961 |
| Current Liabilities | 631,755 | 631,755 | 631,755 | 631,755 |
| Liabilities | 3,182,235 | 3,182,240 | 3,182,235 | 3,182,235 |
| Total Shareholder Equity | -547,274 | -547,274 | -547,274 | -547,274 |
| Total Liabilities and SE | 2,634,961 | 2,634,960 | 2,634,961 | 2,634,961 |

### Reconciliation

All fields match. Dolt correctly includes the goodwill impairment in Operating Profit. No changes needed.

---

## FY2023 — Analysis

### Anomaly Checks

- **SGA (Rule 4):** SellingAndMarketingExpense (759,196K) + GeneralAndAdministrativeExpense (343,242K) = 1,102,438K. ✓
- **Inventory:** NULL — correct.
- **Balance sheet identity:** 2,685,400K = 2,685,400K ✓
- **Gross margin:** 69.9% — normal for marketplace.
- **Total Shareholder Equity:** -543,715K — **[WARNING]** Negative equity. Valid.

### Comparison Table

Values in thousands USD.

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 2,748,377 | 2,748,380 | 2,748,377 | 2,748,377 |
| Cost of Goods | 828,675 | 828,675 | 828,675 | 828,675 |
| Gross Margin | 1,919,702 | 1,919,705 | 1,919,702 | 1,919,702 |
| SGA | 1,102,438 | 1,102,440 | 1,102,438 | 1,102,438 |
| Operating Profit | 279,841 | 279,841 | 279,841 | 279,841 |
| Net Profit | 307,568 | 307,568 | 307,568 | 307,568 |
| Inventory | NULL | NULL | NULL | NULL |
| Current Assets | 1,570,446 | 1,570,450 | 1,570,446 | 1,570,446 |
| Total Assets | 2,685,400 | 2,685,400 | 2,685,400 | 2,685,400 |
| Current Liabilities | 710,781 | 710,781 | 710,781 | 710,781 |
| Liabilities | 3,229,115 | 3,229,120 | 3,229,115 | 3,229,115 |
| Total Shareholder Equity | -543,715 | -543,715 | -543,715 | -543,715 |
| Total Liabilities and SE | 2,685,400 | 2,685,400 | 2,685,400 | 2,685,400 |

### Reconciliation

All fields match. No changes needed.

---

## FY2024 — Analysis

### Anomaly Checks

- **SGA (Rule 4):** SellingAndMarketingExpense (856,565K) + GeneralAndAdministrativeExpense (353,949K) = 1,210,514K. ✓
- **Inventory:** NULL — correct.
- **Balance sheet identity:** 2,417,782K = 2,417,782K ✓
- **Gross margin:** 72.4% — normal for marketplace.
- **Total Shareholder Equity:** -758,866K — **[WARNING]** Negative equity (deepening). Valid — large debt load.

### Comparison Table

Values in thousands USD.

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 2,808,332 | 2,808,330 | 2,808,332 | 2,808,332 |
| Cost of Goods | 774,554 | 774,554 | 774,554 | 774,554 |
| Gross Margin | 2,033,778 | 2,033,776 | 2,033,778 | 2,033,778 |
| SGA | 1,210,514 | 1,210,510 | 1,210,514 | 1,210,514 |
| Operating Profit | 380,208 | 380,208 | 380,208 | 380,208 |
| Net Profit | 303,281 | 303,281 | 303,281 | 303,281 |
| Inventory | NULL | NULL | NULL | NULL |
| Current Assets | 1,327,691 | 1,327,690 | 1,327,691 | 1,327,691 |
| Total Assets | 2,417,782 | 2,417,780 | 2,417,782 | 2,417,782 |
| Current Liabilities | 665,113 | 665,113 | 665,113 | 665,113 |
| Liabilities | 3,176,648 | 3,176,650 | 3,176,648 | 3,176,648 |
| Total Shareholder Equity | -758,866 | -758,866 | -758,866 | -758,866 |
| Total Liabilities and SE | 2,417,782 | 2,417,780 | 2,417,782 | 2,417,782 |

### Reconciliation

All fields match. No changes needed.

---

## FY2025 — New Data Available

SEC 10-K for FY2025 is available (reportDate 2025-12-31). This data is NOT in the Dolt DB.

**From SEC:**
| Field | Value |
|-------|-------|
| Net Revenue | 2,883,501 |
| Cost of Goods | 817,800 |
| Gross Margin | 2,065,701 |
| SGA | 1,247,596 |
| Operating Profit | 266,210 |
| Net Profit | 162,982 |
| Inventory | NULL |
| Current Assets | 1,960,983 |
| Total Assets | 2,827,254 |
| Current Liabilities | 1,363,619 |
| Liabilities | 3,925,349 |
| Total Shareholder Equity | -1,098,095 |
| Total Liabilities and SE | 2,827,254 |

Yahoo data confirms these values. Run `/download-new-year-data ETSY` to insert this data.

---

## Overall Assessment

**All 7 years (2018–2024) in the Dolt DB are correct.** No changes needed.

**Flags for review before inserting FY2025:**
- Negative Total Shareholder Equity: -1,098,095K (expected, consistent with prior trend)
- Gross margin: 71.6% (consistent with ~70% marketplace normal)

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql ETSY` to write SQL files (FY2025 would be the only year with new data).

Report saved to `reports/ETSY-all-years.md`.
