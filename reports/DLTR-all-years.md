# Dollar Tree (DLTR) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-06
**Source:** /verify-dolt-db-financials skill

---

## Company Info

- **Company name in DB:** Dollar Tree
- **Ticker:** DLTR
- **CIK:** 935703
- **Display name:** Dollar Tree
- **Fiscal year end:** Late January / early February
- **Note:** Dollar Tree + Family Dollar combined since FY2015 acquisition. Family Dollar divested/discontinued operations reflected in FY2024–FY2025 SEC filings.

---

## Per-Year Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2018 | 2019-02-02 | No change needed |
| 2019 | 2020-02-01 | No change needed |
| 2020 | 2021-01-30 | No change needed |
| 2021 | 2022-01-29 | No change needed |
| 2022 | 2023-01-28 | No change needed |
| 2023 | 2024-02-03 | **UPDATE NEEDED** — SGA in Dolt includes $1,069M goodwill impairment; should be clean SGA only |
| 2024 | 2025-02-01 | No change needed |
| 2025 | 2026-01-31 | **INSERT NEEDED** — New year not yet in Dolt |

---

## FY2018 (reportDate: 2019-02-02)

### Data Sources

**SEC 10-K (FY2018, filed FY2019-02-02):**
- Net Revenue: $22,823,300,000
- COGS: $15,875,800,000
- Gross Margin: $6,947,500,000 (30.4%) — within 30–35% benchmark
- SGA: `dltr_SellingGeneralandAdministrativeExpenseExcludingReceivableImpairment` = $5,160,000,000
  - Note: `us-gaap_SellingGeneralAndAdministrativeExpense` = $7,887,000,000 (includes $2,727M goodwill impairment charge); use clean tag
- Operating Profit: -$939,500,000 (negative due to $2,727M goodwill impairment on Family Dollar)
- Net Profit: -$1,590,800,000
- Inventory: $3,536,000,000
- Current Assets: $4,293,300,000
- Total Assets: $13,501,200,000
- Current Liabilities: $2,095,700,000
- Total Liabilities: $7,858,300,000
- Total SE: $5,642,900,000
- Total L+SE: $13,501,200,000

**Yahoo Finance:** Not available for FY2018 (Yahoo only covers 2022–2026 columns)

**Dolt DB (current):**
- Net Revenue: 22,823,300 | COGS: 15,875,800 | Gross Margin: 6,947,500 | SGA: 5,160,000
- Operating Profit: -939,500 | Net Profit: -1,590,800
- Inventory: 3,536,000 | Current Assets: 4,293,300 | Total Assets: 13,501,200
- Current Liabilities: 2,095,700 | Liabilities: 7,858,300 | Total SE: 5,642,900
- Total L+SE: 13,501,200

### Side-by-Side Comparison (values in $thousands)

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| reportDate | 2019-02-02 | N/A | 2019-02-02 | 2019-02-02 |
| Net Revenue | 22,823,300 | N/A | 22,823,300 | 22,823,300 |
| Cost of Goods | 15,875,800 | N/A | 15,875,800 | 15,875,800 |
| Gross Margin | 6,947,500 | N/A | 6,947,500 | 6,947,500 |
| SGA | 5,160,000 | N/A | 5,160,000 | 5,160,000 |
| Operating Profit | -939,500 | N/A | -939,500 | -939,500 |
| Net Profit | -1,590,800 | N/A | -1,590,800 | -1,590,800 |
| Inventory | 3,536,000 | N/A | 3,536,000 | 3,536,000 |
| Current Assets | 4,293,300 | N/A | 4,293,300 | 4,293,300 |
| Total Assets | 13,501,200 | N/A | 13,501,200 | 13,501,200 |
| Current Liabilities | 2,095,700 | N/A | 2,095,700 | 2,095,700 |
| Liabilities | 7,858,300 | N/A | 7,858,300 | 7,858,300 |
| Total SE | 5,642,900 | N/A | 5,642,900 | 5,642,900 |
| Total L+SE | 13,501,200 | N/A | 13,501,200 | 13,501,200 |

### Anomaly Checks
- Balance sheet: Total Assets ($13,501,200) = Liabilities ($7,858,300) + SE ($5,642,900) = $13,501,200. OK.
- Gross margin: 30.4% — within 30–35% benchmark. OK.
- SGA: Used clean tag (excluded $2,727M goodwill impairment). Dolt matches clean SGA. OK.
- Operating profit negative due to goodwill impairment — expected.

### Reconciliation
All values match. **No update needed.**

---

## FY2019 (reportDate: 2020-02-01)

### Data Sources

**SEC 10-K (FY2019, filed 2020-02-01):**
- Net Revenue: $23,610,800,000
- COGS: $16,570,100,000
- Gross Margin: $7,040,700,000 (29.8%) — slightly below benchmark
- SGA: `us-gaap_SellingGeneralAndAdministrativeExpense` = $5,465,500,000
  - Goodwill impairment ($313M) is a separate line item; SGA tag is clean
- Operating Profit: $1,262,200,000
- Net Profit: $827,000,000
- Inventory: $3,522,000,000
- Current Assets: $4,269,400,000 (includes $6,225M operating lease ROU assets on balance sheet as non-current from ASC 842)
- Total Assets: $19,574,600,000 (jumped significantly vs FY2018 due to adoption of ASC 842 lease accounting)
- Current Liabilities: $3,546,500,000 (includes $1,279.3M current operating lease liabilities)
- Total Liabilities: $13,319,800,000
- Total SE: $6,254,800,000
- Total L+SE: $19,574,600,000

**Yahoo Finance:** Not available for FY2019

**Dolt DB (current):**
- Net Revenue: 23,610,800 | COGS: 16,570,100 | Gross Margin: 7,040,700 | SGA: 5,465,500
- Operating Profit: 1,262,200 | Net Profit: 827,000
- Inventory: 3,522,000 | Current Assets: 4,269,400 | Total Assets: 19,574,600
- Current Liabilities: 3,546,500 | Liabilities: 13,319,800 | Total SE: 6,254,800
- Total L+SE: 19,574,600

### Side-by-Side Comparison (values in $thousands)

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| reportDate | 2020-02-01 | N/A | 2020-02-01 | 2020-02-01 |
| Net Revenue | 23,610,800 | N/A | 23,610,800 | 23,610,800 |
| Cost of Goods | 16,570,100 | N/A | 16,570,100 | 16,570,100 |
| Gross Margin | 7,040,700 | N/A | 7,040,700 | 7,040,700 |
| SGA | 5,465,500 | N/A | 5,465,500 | 5,465,500 |
| Operating Profit | 1,262,200 | N/A | 1,262,200 | 1,262,200 |
| Net Profit | 827,000 | N/A | 827,000 | 827,000 |
| Inventory | 3,522,000 | N/A | 3,522,000 | 3,522,000 |
| Current Assets | 4,269,400 | N/A | 4,269,400 | 4,269,400 |
| Total Assets | 19,574,600 | N/A | 19,574,600 | 19,574,600 |
| Current Liabilities | 3,546,500 | N/A | 3,546,500 | 3,546,500 |
| Liabilities | 13,319,800 | N/A | 13,319,800 | 13,319,800 |
| Total SE | 6,254,800 | N/A | 6,254,800 | 6,254,800 |
| Total L+SE | 19,574,600 | N/A | 19,574,600 | 19,574,600 |

### Anomaly Checks
- Balance sheet: $19,574,600 = $13,319,800 + $6,254,800 = $19,574,600. OK.
- Gross margin: 29.8% — slightly below 30% benchmark. [WARNING] but consistent with discount retail model and high Family Dollar COGS.
- ASC 842 adoption in FY2019 caused large jump in Total Assets (from ~$13.5B to ~$19.6B) — expected structural change.

### Reconciliation
All values match. **No update needed.**

---

## FY2020 (reportDate: 2021-01-30)

### Data Sources

**SEC 10-K (FY2020, filed 2021-01-30):**
- Net Revenue: $25,509,300,000
- COGS: $17,721,000,000
- Gross Margin: $7,788,300,000 (30.5%)
- SGA: $5,900,400,000 (clean tag; goodwill impairment = $0)
- Operating Profit: $1,887,900,000
- Net Profit: $1,341,900,000
- Inventory: $3,427,000,000
- Current Assets: $5,050,800,000
- Total Assets: $20,696,000,000
- Current Liabilities: $3,730,300,000
- Total Liabilities: $13,410,700,000
- Total SE: $7,285,300,000
- Total L+SE: $20,696,000,000

**Yahoo Finance:** Not available for FY2020

**Dolt DB (current):**
- Net Revenue: 25,509,300 | COGS: 17,721,000 | Gross Margin: 7,788,300 | SGA: 5,900,400
- Operating Profit: 1,887,900 | Net Profit: 1,341,900
- Inventory: 3,427,000 | Current Assets: 5,050,800 | Total Assets: 20,696,000
- Current Liabilities: 3,730,300 | Liabilities: 13,410,700 | Total SE: 7,285,300
- Total L+SE: 20,696,000

### Side-by-Side Comparison (values in $thousands)

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| reportDate | 2021-01-30 | N/A | 2021-01-30 | 2021-01-30 |
| Net Revenue | 25,509,300 | N/A | 25,509,300 | 25,509,300 |
| Cost of Goods | 17,721,000 | N/A | 17,721,000 | 17,721,000 |
| Gross Margin | 7,788,300 | N/A | 7,788,300 | 7,788,300 |
| SGA | 5,900,400 | N/A | 5,900,400 | 5,900,400 |
| Operating Profit | 1,887,900 | N/A | 1,887,900 | 1,887,900 |
| Net Profit | 1,341,900 | N/A | 1,341,900 | 1,341,900 |
| Inventory | 3,427,000 | N/A | 3,427,000 | 3,427,000 |
| Current Assets | 5,050,800 | N/A | 5,050,800 | 5,050,800 |
| Total Assets | 20,696,000 | N/A | 20,696,000 | 20,696,000 |
| Current Liabilities | 3,730,300 | N/A | 3,730,300 | 3,730,300 |
| Liabilities | 13,410,700 | N/A | 13,410,700 | 13,410,700 |
| Total SE | 7,285,300 | N/A | 7,285,300 | 7,285,300 |
| Total L+SE | 20,696,000 | N/A | 20,696,000 | 20,696,000 |

### Anomaly Checks
- Balance sheet: $20,696,000 = $13,410,700 + $7,285,300 = $20,696,000. OK.
- Gross margin: 30.5% — within benchmark. OK.

### Reconciliation
All values match. **No update needed.**

---

## FY2021 (reportDate: 2022-01-29)

### Data Sources

**SEC 10-K (FY2021, filed 2022-01-29):**
- Net Revenue: $26,309,800,000 (contract) + $11,400,000 (other) = $26,321,200,000
- COGS: $18,583,900,000
- Gross Margin: $26,321,200,000 − $18,583,900,000 = $7,737,300,000 (29.4%)
- SGA: $5,925,900,000 (standard tag; goodwill impairment = $0)
- Operating Profit: $1,811,400,000
- Net Profit: $1,327,900,000
- Inventory: $4,367,300,000
- Current Assets: $5,609,200,000
- Total Assets: $21,721,800,000
- Current Liabilities: $4,176,600,000
- Total Liabilities: $14,003,300,000
- Total SE: $7,718,500,000
- Total L+SE: $21,721,800,000

**Yahoo Finance:** Not available for FY2021

**Dolt DB (current):**
- Net Revenue: 26,321,200 | COGS: 18,583,900 | Gross Margin: 7,737,300 | SGA: 5,925,900
- Operating Profit: 1,811,400 | Net Profit: 1,327,900
- Inventory: 4,367,300 | Current Assets: 5,609,200 | Total Assets: 21,721,800
- Current Liabilities: 4,176,600 | Liabilities: 14,003,300 | Total SE: 7,718,500
- Total L+SE: 21,721,800

### Side-by-Side Comparison (values in $thousands)

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| reportDate | 2022-01-29 | N/A | 2022-01-29 | 2022-01-29 |
| Net Revenue | 26,321,200 | N/A | 26,321,200 | 26,321,200 |
| Cost of Goods | 18,583,900 | N/A | 18,583,900 | 18,583,900 |
| Gross Margin | 7,737,300 | N/A | 7,737,300 | 7,737,300 |
| SGA | 5,925,900 | N/A | 5,925,900 | 5,925,900 |
| Operating Profit | 1,811,400 | N/A | 1,811,400 | 1,811,400 |
| Net Profit | 1,327,900 | N/A | 1,327,900 | 1,327,900 |
| Inventory | 4,367,300 | N/A | 4,367,300 | 4,367,300 |
| Current Assets | 5,609,200 | N/A | 5,609,200 | 5,609,200 |
| Total Assets | 21,721,800 | N/A | 21,721,800 | 21,721,800 |
| Current Liabilities | 4,176,600 | N/A | 4,176,600 | 4,176,600 |
| Liabilities | 14,003,300 | N/A | 14,003,300 | 14,003,300 |
| Total SE | 7,718,500 | N/A | 7,718,500 | 7,718,500 |
| Total L+SE | 21,721,800 | N/A | 21,721,800 | 21,721,800 |

### Anomaly Checks
- Balance sheet: $21,721,800 = $14,003,300 + $7,718,500 = $21,721,800. OK.
- Gross margin: 29.4% — slightly below benchmark. [WARNING] minor — consistent with period.
- Net Revenue note: Dolt correctly includes $11.4M "other revenue" in total; SEC contract revenue alone = $26,309,800; total including other = $26,321,200. Dolt matches total. OK.

### Reconciliation
All values match. **No update needed.**

---

## FY2022 (reportDate: 2023-01-28)

### Data Sources

**SEC 10-K (FY2022, filed 2023-01-28):**
- Net Revenue: $28,331,700,000 (contract $28,318,200 + other $13,500)
- COGS: $19,396,300,000
- Gross Margin: $8,935,400,000 (31.5%)
- SGA: `dltr_SellingGeneralandAdministrativeExpenseIncludingImpairmentCharges` = $6,699,100,000 (goodwill impairment = $0, so this equals clean SGA)
  - Cross-check: `us-gaap_SellingGeneralAndAdministrativeExpense` — not separately tagged in FY2022 filing (using company custom tag only = $6,699,100,000)
- Operating Profit: $2,236,300,000
- Net Profit: $1,615,400,000
- Inventory: $5,449,300,000
- Current Assets: $6,367,100,000
- Total Assets: $23,022,100,000
- Current Liabilities: $4,225,200,000
- Total Liabilities: $14,270,600,000
- Total SE: $8,751,500,000
- Total L+SE: $23,022,100,000

**Yahoo Finance (2023-01-31 column — note: Yahoo date differs by 3 days):**
- Yahoo Operating Revenue: $15,405,700,000 — [WARNING] This is Dollar Tree segment only, not consolidated company revenue ($28.3B). Yahoo is reporting segment revenue, not total company.
- Yahoo SGA: $3,682,000,000 — [WARNING] Same issue; likely segment SGA only. Do not use Yahoo for FY2022.
- Yahoo balance sheet: NaN for most fields in 2022-01-31 column. Not usable.

**Dolt DB (current):**
- Net Revenue: 28,331,700 | COGS: 19,396,300 | Gross Margin: 8,935,400 | SGA: 6,699,100
- Operating Profit: 2,236,300 | Net Profit: 1,615,400
- Inventory: 5,449,300 | Current Assets: 6,367,100 | Total Assets: 23,022,100
- Current Liabilities: 4,225,200 | Liabilities: 14,270,600 | Total SE: 8,751,500
- Total L+SE: 23,022,100

### Side-by-Side Comparison (values in $thousands)

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| reportDate | 2023-01-28 | N/A (unusable) | 2023-01-28 | 2023-01-28 |
| Net Revenue | 28,331,700 | [WARNING] partial | 28,331,700 | 28,331,700 |
| Cost of Goods | 19,396,300 | [WARNING] partial | 19,396,300 | 19,396,300 |
| Gross Margin | 8,935,400 | [WARNING] partial | 8,935,400 | 8,935,400 |
| SGA | 6,699,100 | [WARNING] partial | 6,699,100 | 6,699,100 |
| Operating Profit | 2,236,300 | [WARNING] partial | 2,236,300 | 2,236,300 |
| Net Profit | 1,615,400 | [WARNING] partial | 1,615,400 | 1,615,400 |
| Inventory | 5,449,300 | N/A | 5,449,300 | 5,449,300 |
| Current Assets | 6,367,100 | N/A | 6,367,100 | 6,367,100 |
| Total Assets | 23,022,100 | N/A | 23,022,100 | 23,022,100 |
| Current Liabilities | 4,225,200 | N/A | 4,225,200 | 4,225,200 |
| Liabilities | 14,270,600 | N/A | 14,270,600 | 14,270,600 |
| Total SE | 8,751,500 | N/A | 8,751,500 | 8,751,500 |
| Total L+SE | 23,022,100 | N/A | 23,022,100 | 23,022,100 |

### Anomaly Checks
- Balance sheet: $23,022,100 = $14,270,600 + $8,751,500 = $23,022,100. OK.
- Gross margin: 31.5% — within benchmark. OK.
- [WARNING] Yahoo reports only Dollar Tree segment revenue/SGA for years when Family Dollar was still consolidated. Not usable for FY2022 and earlier income statement validation.

### Reconciliation
All values match SEC. **No update needed.**

---

## FY2023 (reportDate: 2024-02-03)

### Data Sources

**SEC 10-K (FY2023, filed 2024-02-03):**
- Net Revenue: $30,603,800,000
- COGS: $21,272,000,000
- Gross Margin: $9,331,800,000 (30.5%)
- SGA analysis:
  - `us-gaap_SellingGeneralAndAdministrativeExpense` = $9,144,600,000 (CLEAN SGA — excludes goodwill impairment)
  - `us-gaap_GoodwillImpairmentLoss` = $1,069,000,000 (Family Dollar segment)
  - `dltr_SellingGeneralandAdministrativeExpenseIncludingImpairmentCharges` = $10,213,600,000 (INCLUDES $1,069M goodwill impairment)
  - **Correct SGA = $9,144,600,000** (the clean standard GAAP tag)
- Operating Profit: -$881,800,000 (negative due to $1,069M goodwill impairment included in operating expenses)
- Net Profit: -$998,400,000
- Inventory: $5,112,800,000
- Current Assets: $6,132,700,000
- Total Assets: $22,023,500,000
- Current Liabilities: $4,696,700,000
- Total Liabilities: $14,710,400,000
- Total SE: $7,313,100,000
- Total L+SE: $22,023,500,000

**Yahoo Finance (2024-01-31 column):**
- Yahoo Total Revenue: $16,781,100,000 — [WARNING] Segment revenue only (Dollar Tree segment = $16,770,300,000). Full company = $30,603,800,000. Do not use Yahoo for revenue FY2023.
- Yahoo SGA: $4,245,200,000 — [WARNING] Appears to be Dollar Tree segment SGA only; full company clean SGA = $9,144,600,000. Do not use for SGA.

**Dolt DB (current):**
- Net Revenue: 30,603,800 | COGS: 21,272,000 | Gross Margin: 9,331,800
- **SGA: 10,213,600** ← [ERROR] Includes $1,069M goodwill impairment; should be 9,144,600
- Operating Profit: -881,800 | Net Profit: -998,400
- Inventory: 5,112,800 | Current Assets: 6,132,700 | Total Assets: 22,023,500
- Current Liabilities: 4,696,700 | Liabilities: 14,710,400 | Total SE: 7,313,100
- Total L+SE: 22,023,500

### Side-by-Side Comparison (values in $thousands)

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| reportDate | 2024-02-03 | [WARNING] | 2024-02-03 | 2024-02-03 |
| Net Revenue | 30,603,800 | [WARNING] partial | 30,603,800 | 30,603,800 |
| Cost of Goods | 21,272,000 | [WARNING] partial | 21,272,000 | 21,272,000 |
| Gross Margin | 9,331,800 | [WARNING] partial | 9,331,800 | 9,331,800 |
| **SGA** | **9,144,600** | [WARNING] partial | **10,213,600 \*** | **9,144,600** |
| Operating Profit | -881,800 | [WARNING] | -881,800 | -881,800 |
| Net Profit | -998,400 | [WARNING] | -998,400 | -998,400 |
| Inventory | 5,112,800 | N/A | 5,112,800 | 5,112,800 |
| Current Assets | 6,132,700 | N/A | 6,132,700 | 6,132,700 |
| Total Assets | 22,023,500 | N/A | 22,023,500 | 22,023,500 |
| Current Liabilities | 4,696,700 | N/A | 4,696,700 | 4,696,700 |
| Liabilities | 14,710,400 | N/A | 14,710,400 | 14,710,400 |
| Total SE | 7,313,100 | N/A | 7,313,100 | 7,313,100 |
| Total L+SE | 22,023,500 | N/A | 22,023,500 | 22,023,500 |

`*` = disagrees with recommended value

### Anomaly Checks
- Balance sheet: $22,023,500 = $14,710,400 + $7,313,100 = $22,023,500. OK.
- Gross margin: 30.5% — within benchmark. OK.
- **[ERROR] SGA in Dolt = 10,213,600 includes $1,069,000 goodwill impairment.** Per anomaly rules, goodwill write-downs must never be included in SGA. The clean SEC tag `us-gaap_SellingGeneralAndAdministrativeExpense` = 9,144,600 is the correct value. Dolt used the custom tag `dltr_SellingGeneralandAdministrativeExpenseIncludingImpairmentCharges` which bundles in the impairment.
- [WARNING] Yahoo data for FY2023 shows only Dollar Tree segment revenue/SGA (company was still reporting Family Dollar as a segment). Not usable for company-wide figures.

### Reconciliation
**SGA must be corrected: Dolt 10,213,600 → 9,144,600 (remove $1,069,000 goodwill impairment)**
**UPDATE NEEDED for FY2023.**

---

## FY2024 (reportDate: 2025-02-01)

### Context
Family Dollar was reclassified as discontinued operations during FY2024. The SEC 10-K reports continuing operations (Dollar Tree segment) separately. Revenue, COGS, SGA, and Operating Profit reflect only the Dollar Tree segment for continuing operations. Net Profit includes discontinued operations losses from Family Dollar divestiture.

### Data Sources

**SEC 10-K (FY2024, filed 2025-02-01):**
- Net Revenue (continuing ops): $17,578,500,000 (`us-gaap_Revenues` top-level)
- COGS (continuing ops): $11,284,100,000
- Gross Margin: $6,294,400,000 (35.8%) — [WARNING] slightly above 35% upper benchmark, reflects Dollar Tree segment without low-margin Family Dollar
- SGA (continuing ops): $4,832,400,000
- Operating Profit (continuing ops): $1,462,000,000
- Net Income from Continuing Operations: $1,042,500,000
- Net Income from Discontinued Operations (Family Dollar): -$4,072,600,000
- **Total Net Profit: -$3,030,100,000** (continuing + discontinued)
- Inventory: $2,672,000,000
- Current Assets: $9,107,200,000 (includes $5,008,900,000 current assets of discontinued operations)
- Total Assets: $18,644,000,000
- Current Liabilities: $8,585,900,000 (includes $4,224,900,000 current liabilities of discontinued operations)
- Total Liabilities: $14,666,600,000
- Total SE: $3,977,400,000
- Total L+SE: $18,644,000,000

**Yahoo Finance (2025-02-01 column — matches SEC):**
- Yahoo Total Revenue: $17,578,500,000 — matches SEC continuing ops
- Yahoo COGS: $11,284,100,000 — matches
- Yahoo SGA: $4,832,400,000 — matches
- Yahoo Operating Income: $1,462,000,000 — matches
- Yahoo Net Income: -$3,030,100,000 — matches (total including discontinued ops)
- Yahoo Inventory: $2,672,000,000 — matches
- Yahoo Current Assets: $9,107,200,000 — matches (includes discontinued ops assets)
- Yahoo Total Assets: $18,644,000,000 — matches
- Yahoo Current Liabilities: $8,585,900,000 — matches (includes discontinued ops liabilities)
- Yahoo Total SE: $3,977,400,000 — matches
- Yahoo Total L+SE: $18,644,000,000 — matches

**Dolt DB (current):**
- Net Revenue: 17,578,500 | COGS: 11,284,100 | Gross Margin: 6,294,400 | SGA: 4,832,400
- Operating Profit: 1,462,000 | Net Profit: -3,030,100
- Inventory: 2,672,000 | Current Assets: 9,107,200 | Total Assets: 18,644,000
- Current Liabilities: 8,585,900 | Liabilities: 14,666,600 | Total SE: 3,977,400
- Total L+SE: 18,644,000

### Side-by-Side Comparison (values in $thousands)

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| reportDate | 2025-02-01 | 2025-01-31 (≈same) | 2025-02-01 | 2025-02-01 |
| Net Revenue | 17,578,500 | 17,578,500 | 17,578,500 | 17,578,500 |
| Cost of Goods | 11,284,100 | 11,284,100 | 11,284,100 | 11,284,100 |
| Gross Margin | 6,294,400 | 6,294,400 | 6,294,400 | 6,294,400 |
| SGA | 4,832,400 | 4,832,400 | 4,832,400 | 4,832,400 |
| Operating Profit | 1,462,000 | 1,462,000 | 1,462,000 | 1,462,000 |
| Net Profit | -3,030,100 | -3,030,100 | -3,030,100 | -3,030,100 |
| Inventory | 2,672,000 | 2,672,000 | 2,672,000 | 2,672,000 |
| Current Assets | 9,107,200 | 9,107,200 | 9,107,200 | 9,107,200 |
| Total Assets | 18,644,000 | 18,644,000 | 18,644,000 | 18,644,000 |
| Current Liabilities | 8,585,900 | 8,585,900 | 8,585,900 | 8,585,900 |
| Liabilities | 14,666,600 | 14,666,600 | 14,666,600 | 14,666,600 |
| Total SE | 3,977,400 | 3,977,400 | 3,977,400 | 3,977,400 |
| Total L+SE | 18,644,000 | 18,644,000 | 18,644,000 | 18,644,000 |

### Anomaly Checks
- Balance sheet: $18,644,000 = $14,666,600 + $3,977,400 = $18,644,000. OK.
- Gross margin: 35.8% — [WARNING] slightly above 35% upper benchmark, but expected as Family Dollar (lower-margin segment) is now discontinued. Dollar Tree segment historically runs higher gross margins.
- Net Profit is very negative due to $4,072,600,000 Family Dollar discontinued operations loss.
- Current Assets and Current Liabilities are inflated by discontinued operations assets/liabilities of ~$5B and ~$4.2B respectively.

### Reconciliation
All values match SEC and Yahoo. **No update needed.**

---

## FY2025 (reportDate: 2026-01-31)

### Context
Family Dollar divestiture completed during FY2025. Dollar Tree now operates as a single-segment company. Revenue, COGS, SGA reflect Dollar Tree operations only. Discontinued operations income of $57,200,000 reflects final Family Dollar transaction items.

### Data Sources

**SEC 10-K (FY2025, filed 2026-01-31):**
- Net Revenue: $19,411,800,000 (`us-gaap_Revenues` = $19,411,800,000; contract revenue = $19,395,700,000 + other $16,100,000)
- COGS: $12,345,000,000
- Gross Margin: $19,411,800,000 − $12,345,000,000 = $7,066,800,000 (36.4%) — [WARNING] above 35% benchmark, expected post-Family Dollar
- SGA: $5,468,600,000 (standard GAAP tag; no goodwill impairment in FY2025)
  - Note: Also includes $54,900,000 transition services agreement income (netted in operating income, not SGA)
- Operating Profit: $1,653,100,000
- Net Income from Continuing Operations: $1,225,300,000
- Net Income from Discontinued Operations: $57,200,000
- **Total Net Profit: $1,282,500,000**
- Inventory: $2,495,400,000
- Current Assets: $3,446,200,000
- Total Assets: $13,466,200,000
- Current Liabilities: $3,228,600,000
- Total Liabilities: $9,711,300,000
- Total SE: $3,754,900,000
- Total L+SE: $13,466,200,000

**Yahoo Finance (2026-01-31 column):**
- Yahoo Total Revenue: $19,411,800,000 — matches SEC
- Yahoo COGS: $12,345,000,000 — matches
- Yahoo Gross Profit: $7,066,800,000 — matches
- Yahoo SGA: $5,468,600,000 — matches SEC
- Yahoo Operating Income: $1,653,100,000 — matches
- Yahoo Net Income: $1,282,500,000 — matches
- Yahoo Inventory: $2,495,400,000 — matches (SEC = $2,495,400,000)
- Yahoo Current Assets: $3,446,200,000 — matches
- Yahoo Total Assets: $13,466,200,000 — matches
- Yahoo Current Liabilities: $3,228,600,000 — matches
- Yahoo Total SE: $3,754,900,000 — matches
- Yahoo Total L+SE: $13,466,200,000 — matches

Note: Yahoo balance sheet shows `Inventory = 2,495,400,000` (from `Finished Goods` = 2,495,400,000 for 2026-01-31 column) matching SEC merchandise inventories of $2,495,400,000. However, Yahoo income statement shows `Selling General And Administration = 5,468,600,000` while SEC shows $5,468,600,000 — exact match. Note Yahoo shows an `Other Operating Expenses = -54,900,000` entry that represents transition services income, which is already included in Operating Income.

**Dolt DB:** Not yet present (new year).

### Side-by-Side Comparison (values in $thousands)

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| reportDate | 2026-01-31 | 2026-01-31 | N/A | 2026-01-31 |
| Net Revenue | 19,411,800 | 19,411,800 | N/A | 19,411,800 |
| Cost of Goods | 12,345,000 | 12,345,000 | N/A | 12,345,000 |
| Gross Margin | 7,066,800 | 7,066,800 | N/A | 7,066,800 |
| SGA | 5,468,600 | 5,468,600 | N/A | 5,468,600 |
| Operating Profit | 1,653,100 | 1,653,100 | N/A | 1,653,100 |
| Net Profit | 1,282,500 | 1,282,500 | N/A | 1,282,500 |
| Inventory | 2,495,400 | 2,495,400 | N/A | 2,495,400 |
| Current Assets | 3,446,200 | 3,446,200 | N/A | 3,446,200 |
| Total Assets | 13,466,200 | 13,466,200 | N/A | 13,466,200 |
| Current Liabilities | 3,228,600 | 3,228,600 | N/A | 3,228,600 |
| Liabilities | 9,711,300 | 9,711,300 | N/A | 9,711,300 |
| Total SE | 3,754,900 | 3,754,900 | N/A | 3,754,900 |
| Total L+SE | 13,466,200 | 13,466,200 | N/A | 13,466,200 |

### Anomaly Checks
- Balance sheet: $13,466,200 = $9,711,300 + $3,754,900 = $13,466,200. OK.
- Gross margin: 36.4% — [WARNING] above 35% upper benchmark. Expected post-Family Dollar divestiture; Dollar Tree segment has historically higher margins than blended company. Structurally consistent going forward.
- SEC and Yahoo agree on all fields. High confidence.
- Total Assets dropped significantly from $18.6B (FY2024) to $13.5B (FY2025) — consistent with Family Dollar divestiture completion.

### Reconciliation
SEC and Yahoo agree on all fields. **INSERT NEEDED for FY2025.**

**Recommended values for INSERT:**

| Field | Value (in $thousands) |
|-------|-----------------------|
| company_name | Dollar Tree |
| year | 2025 |
| reportDate | 2026-01-31 |
| Net Revenue | 19,411,800 |
| Cost of Goods | 12,345,000 |
| Gross Margin | 7,066,800 |
| SGA | 5,468,600 |
| Operating Profit | 1,653,100 |
| Net Profit | 1,282,500 |
| Inventory | 2,495,400 |
| Current Assets | 3,446,200 |
| Total Assets | 13,466,200 |
| Current Liabilities | 3,228,600 |
| Liabilities | 9,711,300 |
| Total SE | 3,754,900 |
| Total L+SE | 13,466,200 |

---

## Summary of All Recommended Values (in $thousands)

| Field | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|-------|------|------|------|------|------|------|------|------|
| reportDate | 2019-02-02 | 2020-02-01 | 2021-01-30 | 2022-01-29 | 2023-01-28 | 2024-02-03 | 2025-02-01 | 2026-01-31 |
| Net Revenue | 22,823,300 | 23,610,800 | 25,509,300 | 26,321,200 | 28,331,700 | 30,603,800 | 17,578,500 | 19,411,800 |
| Cost of Goods | 15,875,800 | 16,570,100 | 17,721,000 | 18,583,900 | 19,396,300 | 21,272,000 | 11,284,100 | 12,345,000 |
| Gross Margin | 6,947,500 | 7,040,700 | 7,788,300 | 7,737,300 | 8,935,400 | 9,331,800 | 6,294,400 | 7,066,800 |
| SGA | 5,160,000 | 5,465,500 | 5,900,400 | 5,925,900 | 6,699,100 | **9,144,600** | 4,832,400 | 5,468,600 |
| Operating Profit | -939,500 | 1,262,200 | 1,887,900 | 1,811,400 | 2,236,300 | -881,800 | 1,462,000 | 1,653,100 |
| Net Profit | -1,590,800 | 827,000 | 1,341,900 | 1,327,900 | 1,615,400 | -998,400 | -3,030,100 | 1,282,500 |
| Inventory | 3,536,000 | 3,522,000 | 3,427,000 | 4,367,300 | 5,449,300 | 5,112,800 | 2,672,000 | 2,495,400 |
| Current Assets | 4,293,300 | 4,269,400 | 5,050,800 | 5,609,200 | 6,367,100 | 6,132,700 | 9,107,200 | 3,446,200 |
| Total Assets | 13,501,200 | 19,574,600 | 20,696,000 | 21,721,800 | 23,022,100 | 22,023,500 | 18,644,000 | 13,466,200 |
| Current Liabilities | 2,095,700 | 3,546,500 | 3,730,300 | 4,176,600 | 4,225,200 | 4,696,700 | 8,585,900 | 3,228,600 |
| Liabilities | 7,858,300 | 13,319,800 | 13,410,700 | 14,003,300 | 14,270,600 | 14,710,400 | 14,666,600 | 9,711,300 |
| Total SE | 5,642,900 | 6,254,800 | 7,285,300 | 7,718,500 | 8,751,500 | 7,313,100 | 3,977,400 | 3,754,900 |
| Total L+SE | 13,501,200 | 19,574,600 | 20,696,000 | 21,721,800 | 23,022,100 | 22,023,500 | 18,644,000 | 13,466,200 |

Bold = value differs from current Dolt DB.

---

## Unresolved Flags

1. **[WARNING] FY2018 Operating/Net Profit negative** — due to $2,727M goodwill impairment on Family Dollar. Expected; already correct in Dolt.
2. **[WARNING] FY2019 Gross Margin 29.8%** — slightly below 30% benchmark. Structurally consistent with combined DLTR+Family Dollar model.
3. **[WARNING] FY2021 Gross Margin 29.4%** — same as above.
4. **[WARNING] FY2022 Yahoo data shows segment revenue only** — Yahoo cannot be used to validate FY2022 and earlier company-wide figures due to Family Dollar segment consolidation.
5. **[WARNING] FY2024–FY2025 Gross Margin above 35%** — expected post-Family Dollar divestiture; Dollar Tree segment operates at higher gross margin.
6. **[WARNING] FY2024 Net Profit very negative** (-$3,030,100) — due to $4,072,600 discontinued operations loss from Family Dollar divestiture. Correct per SEC.
7. **[ERROR] FY2023 SGA in Dolt includes $1,069,000 goodwill impairment** — must be corrected to 9,144,600.

---

**Analysis complete.** Run `/insert-financials DLTR` to write all changed years to the database.

**Changes required:**
- FY2023: UPDATE SGA from 10,213,600 to 9,144,600 (remove goodwill impairment)
- FY2025: INSERT new year (all fields)
