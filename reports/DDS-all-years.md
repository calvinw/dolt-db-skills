# Dillard's (DDS) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-06
**Source:** /verify-dolt-db-financials skill

---

## Summary Table

| Year | reportDate   | Action                                                      |
|------|--------------|-------------------------------------------------------------|
| 2018 | 2019-02-02   | OK — no changes needed                                      |
| 2019 | 2020-02-01   | OK — no changes needed                                      |
| 2020 | 2021-01-30   | OK — no changes needed                                      |
| 2021 | 2022-01-29   | OK — no changes needed                                      |
| 2022 | 2023-01-28   | OK — no changes needed                                      |
| 2023 | 2024-02-03   | OK — no changes needed                                      |
| 2024 | 2025-02-01   | [ERROR] Net Revenue in Dolt is 6,482,636 (net sales only); should be 6,590,231 (total revenue incl. service charges) — UPDATE NEEDED |
| 2025 | 2026-01-31   | NEW YEAR — not in Dolt; insert needed                       |

---

## Company Metadata

- **company:** Dillard's
- **CIK:** 28917
- **display_name:** Dillard's
- **ticker_symbol:** DDS
- **Type:** Department store chain
- **Fiscal Year End:** Late January / early February

### Revenue Note
Dillard's total revenue (`us-gaap_Revenues`) = Net Sales (`RevenueFromContractWithCustomerExcludingAssessedTax`) + Service Charges & Other Income. All years in the Dolt DB consistently use the total revenue figure. FY2024 in Dolt incorrectly uses only net sales (6,482,636) rather than total revenue (6,590,231).

### Operating Profit Note
Dillard's income statement does not show a traditional operating profit subtotal. The "Operating Profit" field in this database is mapped to **Income Before Income Taxes** (pretax income), which is how it has been recorded in the Dolt DB consistently. This is maintained for all years.

### SGA Note
Dillard's reports a single combined `SellingGeneralAndAdministrativeExpense` line. D&A and Rentals are reported as separate line items and are NOT included in SGA. Yahoo's `Selling General And Administration` field matches SEC directly. No composite SGA adjustment required.

---

## FY2018 (reportDate: 2019-02-02)

### Source Data

**SEC 10-K (period ending 2019-02-02):**
- Net Revenue: 6,503,349
- Cost of Goods: 4,291,520
- Gross Margin: 2,211,829
- SGA: 1,691,180
- Operating Profit (pretax): 207,962
- Net Profit: 170,263
- Inventory: 1,528,417
- Current Assets: 1,770,532
- Total Assets: 3,431,369
- Current Liabilities: 933,535
- Total SE: 1,678,381
- Liabilities (derived): 1,752,988
- Total L+SE: 3,431,369

**Yahoo Finance:** Not available for FY2018 (Yahoo only provides data back to FY2022 ending Jan 2022)

**Dolt DB (current):**
- Net Revenue: 6,503,349 | Cost of Goods: 4,291,520 | Gross Margin: 2,211,829
- SGA: 1,691,180 | Operating Profit: 207,962 | Net Profit: 170,263
- Inventory: 1,528,417 | Current Assets: 1,770,532 | Total Assets: 3,431,369
- Current Liabilities: 933,535 | Liabilities: 1,752,988 | Total SE: 1,678,381
- Total L+SE: 3,431,369

### Side-by-Side Comparison

| Field                         | SEC        | Yahoo | Dolt (current) | Recommended |
|-------------------------------|------------|-------|----------------|-------------|
| Net Revenue                   | 6,503,349  | N/A   | 6,503,349      | 6,503,349   |
| Cost of Goods                 | 4,291,520  | N/A   | 4,291,520      | 4,291,520   |
| Gross Margin                  | 2,211,829  | N/A   | 2,211,829      | 2,211,829   |
| SGA                           | 1,691,180  | N/A   | 1,691,180      | 1,691,180   |
| Operating Profit              | 207,962    | N/A   | 207,962        | 207,962     |
| Net Profit                    | 170,263    | N/A   | 170,263        | 170,263     |
| Inventory                     | 1,528,417  | N/A   | 1,528,417      | 1,528,417   |
| Current Assets                | 1,770,532  | N/A   | 1,770,532      | 1,770,532   |
| Total Assets                  | 3,431,369  | N/A   | 3,431,369      | 3,431,369   |
| Current Liabilities           | 933,535    | N/A   | 933,535        | 933,535     |
| Liabilities                   | 1,752,988  | N/A   | 1,752,988      | 1,752,988   |
| Total SE                      | 1,678,381  | N/A   | 1,678,381      | 1,678,381   |
| Total L+SE                    | 3,431,369  | N/A   | 3,431,369      | 3,431,369   |

### Anomaly Checks
- Balance sheet: 3,431,369 = 1,678,381 + 1,752,988 ✓
- Gross margin %: 2,211,829 / 6,503,349 = 34.0% — [WARNING] Below expected 40–45% department store range. Note: Dillard's total revenue includes service charges in denominator, which partially deflates the ratio. Net sales = 6,356,109; GM/net sales = 34.8% — still below benchmark, consistent with Dillard's typical performance.
- No SGA anomalies. D&A (223,815) and Rentals (28,646) are separate and correctly excluded from SGA.

### Verdict: **OK — no changes needed**

---

## FY2019 (reportDate: 2020-02-01)

### Source Data

**SEC 10-K (period ending 2020-02-01):**
- Net Revenue: 6,343,211
- Cost of Goods: 4,235,978
- Gross Margin: 2,107,233
- SGA: 1,691,017
- Operating Profit (pretax): 133,891
- Net Profit: 111,081
- Inventory: 1,465,007
- Current Assets: 1,848,082
- Total Assets: 3,430,257
- Current Liabilities: 930,820
- Total SE: 1,623,259
- Liabilities (derived): 1,806,998
- Total L+SE: 3,430,257

**Yahoo Finance:** Not available for FY2019

**Dolt DB (current):**
- Net Revenue: 6,343,211 | Cost of Goods: 4,235,978 | Gross Margin: 2,107,233
- SGA: 1,691,017 | Operating Profit: 133,891 | Net Profit: 111,081
- Inventory: 1,465,007 | Current Assets: 1,848,082 | Total Assets: 3,430,257
- Current Liabilities: 930,820 | Liabilities: 1,806,998 | Total SE: 1,623,259
- Total L+SE: 3,430,257

### Side-by-Side Comparison

| Field                         | SEC        | Yahoo | Dolt (current) | Recommended |
|-------------------------------|------------|-------|----------------|-------------|
| Net Revenue                   | 6,343,211  | N/A   | 6,343,211      | 6,343,211   |
| Cost of Goods                 | 4,235,978  | N/A   | 4,235,978      | 4,235,978   |
| Gross Margin                  | 2,107,233  | N/A   | 2,107,233      | 2,107,233   |
| SGA                           | 1,691,017  | N/A   | 1,691,017      | 1,691,017   |
| Operating Profit              | 133,891    | N/A   | 133,891        | 133,891     |
| Net Profit                    | 111,081    | N/A   | 111,081        | 111,081     |
| Inventory                     | 1,465,007  | N/A   | 1,465,007      | 1,465,007   |
| Current Assets                | 1,848,082  | N/A   | 1,848,082      | 1,848,082   |
| Total Assets                  | 3,430,257  | N/A   | 3,430,257      | 3,430,257   |
| Current Liabilities           | 930,820    | N/A   | 930,820        | 930,820     |
| Liabilities                   | 1,806,998  | N/A   | 1,806,998      | 1,806,998   |
| Total SE                      | 1,623,259  | N/A   | 1,623,259      | 1,623,259   |
| Total L+SE                    | 3,430,257  | N/A   | 3,430,257      | 3,430,257   |

### Anomaly Checks
- Balance sheet: 3,430,257 = 1,623,259 + 1,806,998 ✓
- Gross margin %: 2,107,233 / 6,343,211 = 33.2% — [WARNING] Below 40–45% benchmark. Consistent with Dillard's historical pattern (total revenue denominator effect + lower-end department store pricing).
- No SGA anomalies. D&A (222,349) and Rentals (26,375) correctly excluded.

### Verdict: **OK — no changes needed**

---

## FY2020 (reportDate: 2021-01-30)

### Source Data

**SEC 10-K (period ending 2021-01-30):**
- Net Revenue: 4,433,185
- Cost of Goods: 3,069,063
- Gross Margin: 1,364,122
- SGA: 1,211,483
- Operating Profit (pretax): -153,404
- Net Profit: -71,654
- Inventory: 1,087,763
- Current Assets: 1,661,940
- Total Assets: 3,092,515
- Current Liabilities: 772,877
- Total SE: 1,441,008
- Liabilities (derived): 1,651,507
- Total L+SE: 3,092,515

Note: FY2020 was severely impacted by COVID-19 (stores closed spring 2020). Asset impairment charge of 10,736 was also recorded. Revenue dropped ~30% YoY.

**Yahoo Finance:** Not available for FY2020

**Dolt DB (current):**
- Net Revenue: 4,433,185 | Cost of Goods: 3,069,063 | Gross Margin: 1,364,122
- SGA: 1,211,483 | Operating Profit: -153,404 | Net Profit: -71,654
- Inventory: 1,087,763 | Current Assets: 1,661,940 | Total Assets: 3,092,515
- Current Liabilities: 772,877 | Liabilities: 1,651,507 | Total SE: 1,441,008
- Total L+SE: 3,092,515

### Side-by-Side Comparison

| Field                         | SEC        | Yahoo | Dolt (current) | Recommended |
|-------------------------------|------------|-------|----------------|-------------|
| Net Revenue                   | 4,433,185  | N/A   | 4,433,185      | 4,433,185   |
| Cost of Goods                 | 3,069,063  | N/A   | 3,069,063      | 3,069,063   |
| Gross Margin                  | 1,364,122  | N/A   | 1,364,122      | 1,364,122   |
| SGA                           | 1,211,483  | N/A   | 1,211,483      | 1,211,483   |
| Operating Profit              | -153,404   | N/A   | -153,404       | -153,404    |
| Net Profit                    | -71,654    | N/A   | -71,654        | -71,654     |
| Inventory                     | 1,087,763  | N/A   | 1,087,763      | 1,087,763   |
| Current Assets                | 1,661,940  | N/A   | 1,661,940      | 1,661,940   |
| Total Assets                  | 3,092,515  | N/A   | 3,092,515      | 3,092,515   |
| Current Liabilities           | 772,877    | N/A   | 772,877        | 772,877     |
| Liabilities                   | 1,651,507  | N/A   | 1,651,507      | 1,651,507   |
| Total SE                      | 1,441,008  | N/A   | 1,441,008      | 1,441,008   |
| Total L+SE                    | 3,092,515  | N/A   | 3,092,515      | 3,092,515   |

### Anomaly Checks
- Balance sheet: 3,092,515 = 1,441,008 + 1,651,507 ✓
- Gross margin %: 1,364,122 / 4,433,185 = 30.8% — [WARNING] Below benchmark, driven by COVID-19 revenue shortfall and markdowns.
- Operating loss: -153,404 — expected for COVID year.
- Impairment charge (10,736) on long-lived assets correctly excluded from SGA.

### Verdict: **OK — no changes needed**

---

## FY2021 (reportDate: 2022-01-29)

### Source Data

**SEC 10-K (period ending 2022-01-29):**
- Net Revenue: 6,624,267
- Cost of Goods: 3,747,665
- Gross Margin: 2,876,602
- SGA: 1,536,554
- Operating Profit (pretax): 1,088,363
- Net Profit: 862,473
- Inventory: 1,080,178
- Current Assets: 1,914,651
- Total Assets: 3,245,557
- Current Liabilities: 966,186
- Total SE: 1,451,218
- Liabilities (derived): 1,794,339
- Total L+SE: 3,245,557

**Yahoo Finance:** Not available for FY2021 (Yahoo data starts at FY2022 ending 2023-01-28)

**Dolt DB (current):**
- Net Revenue: 6,624,267 | Cost of Goods: 3,747,665 | Gross Margin: 2,876,602
- SGA: 1,536,554 | Operating Profit: 1,088,363 | Net Profit: 862,473
- Inventory: 1,080,178 | Current Assets: 1,914,651 | Total Assets: 3,245,557
- Current Liabilities: 966,186 | Liabilities: 1,794,339 | Total SE: 1,451,218
- Total L+SE: 3,245,557

### Side-by-Side Comparison

| Field                         | SEC        | Yahoo | Dolt (current) | Recommended |
|-------------------------------|------------|-------|----------------|-------------|
| Net Revenue                   | 6,624,267  | N/A   | 6,624,267      | 6,624,267   |
| Cost of Goods                 | 3,747,665  | N/A   | 3,747,665      | 3,747,665   |
| Gross Margin                  | 2,876,602  | N/A   | 2,876,602      | 2,876,602   |
| SGA                           | 1,536,554  | N/A   | 1,536,554      | 1,536,554   |
| Operating Profit              | 1,088,363  | N/A   | 1,088,363      | 1,088,363   |
| Net Profit                    | 862,473    | N/A   | 862,473        | 862,473     |
| Inventory                     | 1,080,178  | N/A   | 1,080,178      | 1,080,178   |
| Current Assets                | 1,914,651  | N/A   | 1,914,651      | 1,914,651   |
| Total Assets                  | 3,245,557  | N/A   | 3,245,557      | 3,245,557   |
| Current Liabilities           | 966,186    | N/A   | 966,186        | 966,186     |
| Liabilities                   | 1,794,339  | N/A   | 1,794,339      | 1,794,339   |
| Total SE                      | 1,451,218  | N/A   | 1,451,218      | 1,451,218   |
| Total L+SE                    | 3,245,557  | N/A   | 3,245,557      | 3,245,557   |

### Anomaly Checks
- Balance sheet: 3,245,557 = 1,451,218 + 1,794,339 ✓
- Gross margin %: 2,876,602 / 6,624,267 = 43.4% — within 40–45% benchmark ✓
- Strong recovery year post-COVID with gross margin improving significantly vs. FY2020.

### Verdict: **OK — no changes needed**

---

## FY2022 (reportDate: 2023-01-28)

### Source Data

**SEC 10-K (period ending 2023-01-28):**
- Net Revenue: 6,996,215
- Cost of Goods: 3,983,598
- Gross Margin: 3,012,617
- SGA: 1,674,317
- Operating Profit (pretax): 1,109,467
- Net Profit: 891,637
- Inventory: 1,120,208
- Current Assets: 2,071,846
- Total Assets: 3,329,150
- Current Liabilities: 858,961
- Total SE: 1,598,638
- Liabilities (derived): 1,730,512
- Total L+SE: 3,329,150

**Yahoo Finance (period ending 2023-01-31 per Yahoo header):**
- Total Revenue: 6,996,220 (~6,996,215 rounded)
- Cost of Revenue: 3,983,600 (~3,983,598 rounded)
- Gross Profit: 3,012,620 (~3,012,617 rounded)
- SGA (GeneralAndAdministrativeExpense): 1,697,490 [WARNING: Yahoo shows 1,697,490 vs SEC 1,674,317 — difference of 23,173]
- Operating Income: 1,126,690 [Note: Yahoo uses different line item structure]
- Net Income: 891,637 ✓
- Inventory: 1,120,210 (~1,120,208)
- Current Assets: 2,071,850 (~2,071,846)
- Total Assets: 3,329,150 ✓
- Current Liabilities: 858,961 ✓
- Total SE: 1,598,638 ✓
- Total L+SE: 3,329,150 ✓

Note on Yahoo SGA discrepancy: Yahoo's `GeneralAndAdministrativeExpense` (1,697,490) appears to include items beyond the SEC `SellingGeneralAndAdministrativeExpense` (1,674,317). The SEC value is authoritative. Yahoo's `OperatingExpense` line of 1,885,930 likely represents total operating expenses (SGA + D&A + Rentals), not pure SGA — [WARNING] Yahoo SGA ≈ composite line, use SEC value.

**Dolt DB (current):**
- Net Revenue: 6,996,215 | Cost of Goods: 3,983,598 | Gross Margin: 3,012,617
- SGA: 1,674,317 | Operating Profit: 1,260,329 | Net Profit: 891,637
- Inventory: 1,120,208 | Current Assets: 2,071,846 | Total Assets: 3,329,150
- Current Liabilities: 858,961 | Liabilities: 1,730,512 | Total SE: 1,598,638
- Total L+SE: 3,329,150

**Note on Operating Profit discrepancy:** Dolt has 1,260,329 but SEC shows pretax income of 1,109,467. The difference is 150,862 — this appears to be because the Dolt value uses an earlier filing or different line item. Let me re-examine: The SEC 2022 filing for the year ending 2023-01-28 shows `IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItems` = 1,109,467. But the Dolt has 1,260,329 for Operating Profit in 2022. Yahoo shows Operating Income = 1,126,690. This Dolt value of 1,260,329 does NOT match SEC pretax income or Yahoo operating income. The difference between 1,260,329 and 1,109,467 is 150,862. However, given that the net profit matches (891,637 both SEC and Dolt), and that the definition used in this database for Operating Profit is pretax income, the Dolt value of 1,260,329 may be from a prior filing or represents a different line item. Using the most recent SEC filing: pretax = 1,109,467. [WARNING] Operating Profit in Dolt (1,260,329) does not match SEC pretax income (1,109,467) — investigate.

Actually, re-checking the SEC data: for the 2022 filing (period 2023-01-28), the SEC income statement shows Income Before Tax = 1,109,467. For the 2021 year (period 2022-01-29) the same filing confirmed pretax = 1,088,363 which matches Dolt's 2021 value. So the 2022 Dolt value of 1,260,329 does not match. However, looking at Yahoo's `Operating Income` = 1,126,690 for this period (closer to SEC's pretax), neither matches Dolt's 1,260,329.

The difference between Dolt 1,260,329 and SEC pretax 1,109,467 = 150,862. This could be the interest expense (43,354 → no) or other items. Without further data, flag this as a discrepancy. The recommended value is SEC pretax income: **1,109,467**.

### Side-by-Side Comparison

| Field                         | SEC        | Yahoo      | Dolt (current) | Recommended |
|-------------------------------|------------|------------|----------------|-------------|
| Net Revenue                   | 6,996,215  | ~6,996,220 | 6,996,215      | 6,996,215   |
| Cost of Goods                 | 3,983,598  | ~3,983,600 | 3,983,598      | 3,983,598   |
| Gross Margin                  | 3,012,617  | ~3,012,620 | 3,012,617      | 3,012,617   |
| SGA                           | 1,674,317  | 1,697,490* | 1,674,317      | 1,674,317   |
| Operating Profit              | 1,109,467  | 1,126,690  | 1,260,329 *    | 1,109,467   |
| Net Profit                    | 891,637    | 891,637    | 891,637        | 891,637     |
| Inventory                     | 1,120,208  | ~1,120,210 | 1,120,208      | 1,120,208   |
| Current Assets                | 2,071,846  | ~2,071,850 | 2,071,846      | 2,071,846   |
| Total Assets                  | 3,329,150  | 3,329,150  | 3,329,150      | 3,329,150   |
| Current Liabilities           | 858,961    | 858,961    | 858,961        | 858,961     |
| Liabilities                   | 1,730,512  | 1,730,512  | 1,730,512      | 1,730,512   |
| Total SE                      | 1,598,638  | 1,598,638  | 1,598,638      | 1,598,638   |
| Total L+SE                    | 3,329,150  | 3,329,150  | 3,329,150      | 3,329,150   |

*Yahoo SGA uses composite line — use SEC value. *Dolt Operating Profit differs from SEC.

### Anomaly Checks
- Balance sheet: 3,329,150 = 1,598,638 + 1,730,512 ✓
- Gross margin %: 3,012,617 / 6,996,215 = 43.1% — within benchmark ✓
- [WARNING] Yahoo SGA (1,697,490) ≈ SGA + other items — do not use Yahoo SGA.
- [WARNING] Dolt Operating Profit (1,260,329) does not match SEC pretax income (1,109,467). Recommend updating to 1,109,467.

### Reconciled Values
| Field            | Recommended | Source | Dolt Differs? |
|------------------|-------------|--------|---------------|
| Net Revenue      | 6,996,215   | SEC    | No            |
| Cost of Goods    | 3,983,598   | SEC    | No            |
| Gross Margin     | 3,012,617   | SEC    | No            |
| SGA              | 1,674,317   | SEC    | No            |
| Operating Profit | 1,109,467   | SEC    | **YES**       |
| Net Profit       | 891,637     | SEC/Yahoo | No         |
| Inventory        | 1,120,208   | SEC    | No            |
| Current Assets   | 2,071,846   | SEC    | No            |
| Total Assets     | 3,329,150   | SEC    | No            |
| Current Liab.    | 858,961     | SEC    | No            |
| Liabilities      | 1,730,512   | SEC    | No            |
| Total SE         | 1,598,638   | SEC    | No            |
| Total L+SE       | 3,329,150   | SEC    | No            |

### Verdict: **UPDATE NEEDED — Operating Profit: 1,260,329 → 1,109,467**

---

## FY2023 (reportDate: 2024-02-03)

### Source Data

**SEC 10-K (period ending 2024-02-03):**
- Net Revenue: 6,874,420
- Cost of Goods: 4,031,108
- Gross Margin: 2,843,312
- SGA: 1,717,415
- Operating Profit (pretax): 916,617
- Net Profit: 738,847
- Inventory: 1,093,999
- Current Assets: 2,208,210
- Total Assets: 3,448,906
- Current Liabilities: 827,756
- Total SE: 1,697,068
- Liabilities (derived): 1,751,838
- Total L+SE: 3,448,906

**Yahoo Finance (period ending 2024-01-31 per Yahoo header):**
- Total Revenue: 6,874,420 ✓
- Cost of Revenue: 4,031,110 (~4,031,108)
- Gross Profit: 2,843,310 (~2,843,312)
- SGA (GeneralAndAdministrativeExpense): 1,738,980 [WARNING: Yahoo shows 1,738,980 vs SEC 1,717,415]
- Operating Income: 924,755 (Yahoo) vs 916,617 (SEC pretax) — small diff due to Yahoo's treatment of interest income/expense as operating vs non-operating
- Net Income: 738,847 ✓
- Inventory: 1,094,000 (~1,093,999) ✓
- Current Assets: 2,208,210 ✓
- Total Assets: 3,448,910 (~3,448,906) ✓
- Current Liabilities: 827,756 ✓
- Total SE: 1,697,068 ✓
- Total L+SE: 3,448,910 (~3,448,906) ✓

**Dolt DB (current):**
- Net Revenue: 6,874,420 | Cost of Goods: 4,031,108 | Gross Margin: 2,843,312
- SGA: 1,717,415 | Operating Profit: 945,897 | Net Profit: 738,847
- Inventory: 1,093,999 | Current Assets: 2,208,210 | Total Assets: 3,448,906
- Current Liabilities: 827,756 | Liabilities: 1,751,838 | Total SE: 1,697,068
- Total L+SE: 3,448,906

**Note on Operating Profit discrepancy:** Dolt has 945,897 but SEC shows pretax income 916,617. Difference = 29,280. Yahoo Operating Income = 924,755. None of these three match. The Dolt value 945,897 = pretax 916,617 + interest expense net 4,600 + other items? The 2023 filing shows Interest Expense line as 4,600 (net interest income, positive). Operating profit before interest and non-operating items: Revenue - COGS - SGA - D&A - Rentals = 6,874,420 - 4,031,108 - 1,717,415 - 179,573 - 21,569 = 924,755. This matches Yahoo's Operating Income of 924,755. So the true operating profit (before interest, other expense, and asset gains) = **924,755**. SEC pretax = 916,617. Dolt has 945,897 — does not match any standard calculation. [WARNING] Dolt Operating Profit (945,897) does not match SEC pretax (916,617) or derived operating income (924,755). Recommend updating to SEC pretax 916,617 for consistency with all other years.

### Side-by-Side Comparison

| Field                         | SEC        | Yahoo      | Dolt (current) | Recommended |
|-------------------------------|------------|------------|----------------|-------------|
| Net Revenue                   | 6,874,420  | 6,874,420  | 6,874,420      | 6,874,420   |
| Cost of Goods                 | 4,031,108  | ~4,031,110 | 4,031,108      | 4,031,108   |
| Gross Margin                  | 2,843,312  | ~2,843,310 | 2,843,312      | 2,843,312   |
| SGA                           | 1,717,415  | 1,738,980* | 1,717,415      | 1,717,415   |
| Operating Profit              | 916,617    | 924,755    | 945,897 *      | 916,617     |
| Net Profit                    | 738,847    | 738,847    | 738,847        | 738,847     |
| Inventory                     | 1,093,999  | ~1,094,000 | 1,093,999      | 1,093,999   |
| Current Assets                | 2,208,210  | 2,208,210  | 2,208,210      | 2,208,210   |
| Total Assets                  | 3,448,906  | ~3,448,910 | 3,448,906      | 3,448,906   |
| Current Liabilities           | 827,756    | 827,756    | 827,756        | 827,756     |
| Liabilities                   | 1,751,838  | 1,751,838  | 1,751,838      | 1,751,838   |
| Total SE                      | 1,697,068  | 1,697,068  | 1,697,068      | 1,697,068   |
| Total L+SE                    | 3,448,906  | ~3,448,910 | 3,448,906      | 3,448,906   |

*Yahoo SGA uses composite line — use SEC value. *Dolt Operating Profit differs.

### Anomaly Checks
- Balance sheet: 3,448,906 = 1,697,068 + 1,751,838 ✓
- Gross margin %: 2,843,312 / 6,874,420 = 41.4% — within benchmark ✓
- [WARNING] Yahoo SGA (1,738,980) is composite — do not use.
- [WARNING] Dolt Operating Profit (945,897) does not match SEC pretax (916,617). Recommend updating.

### Reconciled Values
| Field            | Recommended | Source | Dolt Differs? |
|------------------|-------------|--------|---------------|
| Net Revenue      | 6,874,420   | SEC/Yahoo | No         |
| Cost of Goods    | 4,031,108   | SEC    | No            |
| Gross Margin     | 2,843,312   | SEC    | No            |
| SGA              | 1,717,415   | SEC    | No            |
| Operating Profit | 916,617     | SEC    | **YES**       |
| Net Profit       | 738,847     | SEC/Yahoo | No         |
| Inventory        | 1,093,999   | SEC    | No            |
| Current Assets   | 2,208,210   | SEC    | No            |
| Total Assets     | 3,448,906   | SEC    | No            |
| Current Liab.    | 827,756     | SEC    | No            |
| Liabilities      | 1,751,838   | SEC    | No            |
| Total SE         | 1,697,068   | SEC    | No            |
| Total L+SE       | 3,448,906   | SEC    | No            |

### Verdict: **UPDATE NEEDED — Operating Profit: 945,897 → 916,617**

---

## FY2024 (reportDate: 2025-02-01)

### Source Data

**SEC 10-K (period ending 2025-02-01):**
- Net Revenue: 6,590,231 (= 6,482,636 net sales + 107,595 service charges)
- Cost of Goods: 3,919,549
- Gross Margin: 2,670,682
- SGA: 1,731,234
- Operating Profit (pretax): 729,701
- Net Profit: 593,476
- Inventory: 1,172,047
- Current Assets: 2,368,070
- Total Assets: 3,531,054
- Current Liabilities: 834,906
- Total SE: 1,796,160
- Liabilities (derived): 1,734,894
- Total L+SE: 3,531,054

**Yahoo Finance (period ending 2025-01-31 per Yahoo header):**
- Total Revenue: 6,590,230 (~6,590,231) ✓
- Cost of Revenue: 3,919,550 (~3,919,549) ✓
- Gross Profit: 2,670,680 (~2,670,682) ✓
- SGA (GeneralAndAdministrativeExpense): 1,752,650 [WARNING: Yahoo shows 1,752,650 vs SEC 1,731,234]
- Operating Income: 740,162 (Yahoo) vs 729,701 (SEC pretax) — difference due to interest treatment
- Net Income: 593,476 ✓
- Inventory: 1,172,050 (~1,172,047) ✓
- Current Assets: 2,368,070 ✓
- Total Assets: 3,531,050 (~3,531,054) ✓
- Current Liabilities: 834,906 ✓
- Total SE: 1,796,160 ✓
- Total L+SE: 3,531,050 (~3,531,054) ✓

**Dolt DB (current):**
- Net Revenue: **6,482,636** | Cost of Goods: 3,919,549 | Gross Margin: **2,563,087**
- SGA: 1,731,234 | Operating Profit: **729,701** | Net Profit: 593,476
- Inventory: 1,172,047 | Current Assets: 2,368,070 | Total Assets: 3,531,054
- Current Liabilities: 834,906 | Liabilities: 1,734,894 | Total SE: 1,796,160
- Total L+SE: 3,531,054

**Critical Issue:** Dolt Net Revenue = 6,482,636 which is ONLY the `RevenueFromContractWithCustomerExcludingAssessedTax` (net sales). It is missing the 107,595 of service charges and other income. All prior years in Dolt correctly use total `us-gaap_Revenues`. This is inconsistent with the established convention. The correct value should be 6,590,231.

The Gross Margin in Dolt (2,563,087) = 6,482,636 - 3,919,549, which is also wrong because it uses the incorrect revenue. Correct Gross Margin = 6,590,231 - 3,919,549 = 2,670,682.

### Side-by-Side Comparison

| Field                         | SEC        | Yahoo      | Dolt (current) | Recommended |
|-------------------------------|------------|------------|----------------|-------------|
| Net Revenue                   | 6,590,231  | 6,590,230  | **6,482,636 *** | 6,590,231   |
| Cost of Goods                 | 3,919,549  | ~3,919,550 | 3,919,549      | 3,919,549   |
| Gross Margin                  | 2,670,682  | ~2,670,680 | **2,563,087 *** | 2,670,682   |
| SGA                           | 1,731,234  | 1,752,650* | 1,731,234      | 1,731,234   |
| Operating Profit              | 729,701    | 740,162    | 729,701        | 729,701     |
| Net Profit                    | 593,476    | 593,476    | 593,476        | 593,476     |
| Inventory                     | 1,172,047  | ~1,172,050 | 1,172,047      | 1,172,047   |
| Current Assets                | 2,368,070  | 2,368,070  | 2,368,070      | 2,368,070   |
| Total Assets                  | 3,531,054  | ~3,531,050 | 3,531,054      | 3,531,054   |
| Current Liabilities           | 834,906    | 834,906    | 834,906        | 834,906     |
| Liabilities                   | 1,734,894  | 1,734,894  | 1,734,894      | 1,734,894   |
| Total SE                      | 1,796,160  | 1,796,160  | 1,796,160      | 1,796,160   |
| Total L+SE                    | 3,531,054  | ~3,531,050 | 3,531,054      | 3,531,054   |

*Dolt Net Revenue and Gross Margin use wrong revenue base (net sales only, missing service charges). *Yahoo SGA is composite — use SEC value.

### Anomaly Checks
- Balance sheet: 3,531,054 = 1,796,160 + 1,734,894 ✓
- [ERROR] Dolt Net Revenue (6,482,636) is net sales only; total revenue should be 6,590,231 (includes 107,595 service charges).
- [ERROR] Dolt Gross Margin (2,563,087) is derived from wrong revenue — should be 2,670,682.
- Gross margin % (correct): 2,670,682 / 6,590,231 = 40.5% — within benchmark ✓
- [WARNING] Yahoo SGA (1,752,650) is composite — do not use; SEC value (1,731,234) is correct.

### Reconciled Values
| Field            | Recommended | Source    | Dolt Differs? |
|------------------|-------------|-----------|---------------|
| Net Revenue      | 6,590,231   | SEC/Yahoo | **YES**       |
| Cost of Goods    | 3,919,549   | SEC/Yahoo | No            |
| Gross Margin     | 2,670,682   | SEC/Yahoo | **YES**       |
| SGA              | 1,731,234   | SEC       | No            |
| Operating Profit | 729,701     | SEC       | No            |
| Net Profit       | 593,476     | SEC/Yahoo | No            |
| Inventory        | 1,172,047   | SEC       | No            |
| Current Assets   | 2,368,070   | SEC       | No            |
| Total Assets     | 3,531,054   | SEC       | No            |
| Current Liab.    | 834,906     | SEC       | No            |
| Liabilities      | 1,734,894   | SEC       | No            |
| Total SE         | 1,796,160   | SEC       | No            |
| Total L+SE       | 3,531,054   | SEC       | No            |

### Verdict: **UPDATE NEEDED — Net Revenue: 6,482,636 → 6,590,231; Gross Margin: 2,563,087 → 2,670,682**

---

## FY2025 (reportDate: 2026-01-31) — NEW YEAR

### Source Data

**SEC 10-K (period ending 2026-01-31):**
- Net Revenue: 6,563,336 (= 6,473,623 net sales + 89,713 service charges)
- Cost of Goods: 3,916,862
- Gross Margin: 2,646,474
- SGA: 1,759,236
- Operating Profit (pretax): 694,480
- Net Profit: 570,187
- Inventory: 1,201,098
- Current Assets: 2,386,571
- Total Assets: 3,505,023
- Current Liabilities: 902,084
- Total SE: 1,778,970
- Liabilities (derived): 1,726,053
- Total L+SE: 3,505,023

**Yahoo Finance (period ending 2026-01-31 per Yahoo header):**
- Total Revenue: 6,563,340 (~6,563,336) ✓
- Cost of Revenue: 3,916,860 (~3,916,862) ✓
- Gross Profit: 2,646,470 (~2,646,474) ✓
- SGA (GeneralAndAdministrativeExpense): 1,778,460 [WARNING: Yahoo 1,778,460 vs SEC 1,759,236]
- Operating Income: 688,674 (Yahoo)
- Net Income: 570,187 ✓
- Inventory: 1,201,100 (~1,201,098) ✓
- Current Assets: 2,386,570 (~2,386,571) ✓
- Total Assets: 3,505,020 (~3,505,023) ✓
- Current Liabilities: 902,084 ✓
- Total SE: 1,778,970 ✓
- Total L+SE: 3,505,020 (~3,505,023) ✓

**Dolt DB:** Not present — NEW YEAR

### Side-by-Side Comparison

| Field                         | SEC        | Yahoo      | Dolt (current) | Recommended |
|-------------------------------|------------|------------|----------------|-------------|
| Net Revenue                   | 6,563,336  | ~6,563,340 | —              | 6,563,336   |
| Cost of Goods                 | 3,916,862  | ~3,916,860 | —              | 3,916,862   |
| Gross Margin                  | 2,646,474  | ~2,646,470 | —              | 2,646,474   |
| SGA                           | 1,759,236  | 1,778,460* | —              | 1,759,236   |
| Operating Profit              | 694,480    | 688,674    | —              | 694,480     |
| Net Profit                    | 570,187    | 570,187    | —              | 570,187     |
| Inventory                     | 1,201,098  | ~1,201,100 | —              | 1,201,098   |
| Current Assets                | 2,386,571  | ~2,386,570 | —              | 2,386,571   |
| Total Assets                  | 3,505,023  | ~3,505,020 | —              | 3,505,023   |
| Current Liabilities           | 902,084    | 902,084    | —              | 902,084     |
| Liabilities                   | 1,726,053  | 1,726,053  | —              | 1,726,053   |
| Total SE                      | 1,778,970  | 1,778,970  | —              | 1,778,970   |
| Total L+SE                    | 3,505,023  | ~3,505,020 | —              | 3,505,023   |

*Yahoo SGA (1,778,460) is composite — use SEC value.

### Anomaly Checks
- Balance sheet: 3,505,023 = 1,778,970 + 1,726,053 ✓
- Gross margin %: 2,646,474 / 6,563,336 = 40.3% — within benchmark ✓
- [WARNING] Yahoo SGA (1,778,460) is composite — do not use; SEC value (1,759,236) is authoritative.
- SEC and Yahoo revenue, COGS, gross margin, net income all agree closely.
- D&A (179,341) and Rentals (19,223) are separate and NOT included in SGA.
- Gain on disposal of assets (20,373) correctly excluded from SGA.

### Reconciled Values
| Field            | Value     | Source    | Notes                    |
|------------------|-----------|-----------|--------------------------|
| reportDate       | 2026-01-31 | SEC      |                          |
| Net Revenue      | 6,563,336 | SEC       | Includes service charges |
| Cost of Goods    | 3,916,862 | SEC       |                          |
| Gross Margin     | 2,646,474 | SEC       |                          |
| SGA              | 1,759,236 | SEC       |                          |
| Operating Profit | 694,480   | SEC       | Pretax income            |
| Net Profit       | 570,187   | SEC/Yahoo |                          |
| Inventory        | 1,201,098 | SEC       |                          |
| Current Assets   | 2,386,571 | SEC       |                          |
| Total Assets     | 3,505,023 | SEC       |                          |
| Current Liab.    | 902,084   | SEC       |                          |
| Liabilities      | 1,726,053 | SEC       |                          |
| Total SE         | 1,778,970 | SEC       |                          |
| Total L+SE       | 3,505,023 | SEC       |                          |

### Verdict: **NEW YEAR — insert FY2025 into Dolt DB**

---

## Final Signal

**Analysis complete.** Run `/insert-financials DDS` to write all changed years to the database.

### Years requiring changes:

| Year | Action | Fields to Update |
|------|--------|-----------------|
| 2022 | UPDATE | Operating Profit: 1,260,329 → 1,109,467 |
| 2023 | UPDATE | Operating Profit: 945,897 → 916,617 |
| 2024 | UPDATE | Net Revenue: 6,482,636 → 6,590,231; Gross Margin: 2,563,087 → 2,670,682 |
| 2025 | INSERT | All fields (new year, reportDate: 2026-01-31) |

### Unresolved Flags:
- [WARNING] FY2018 and FY2019 gross margin percentages are below 40–45% benchmark (~34%). This is a consistent characteristic of Dillard's total-revenue-denominator convention and lower gross margins vs. pure apparel department stores. No data error — this is accurate.
- [WARNING] FY2020 gross margin % below benchmark (30.8%) — COVID impact, expected.
- [WARNING] Yahoo SGA consistently overstates vs. SEC across FY2022–FY2025. Yahoo SGA for Dillard's includes items beyond the pure SGA line. Always use SEC values for SGA.
- [WARNING] FY2022 and FY2023 Dolt Operating Profit values do not match SEC pretax income. Origin of those values in Dolt is unclear — may have used an intermediate line item from an older filing format. Updated values use SEC pretax income for consistency with all other years.
