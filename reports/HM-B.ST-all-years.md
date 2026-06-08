# H&M (HM-B.ST) — FY2018–FY2024 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill
**Currency:** SEK (thousands) | Non-US company — Yahoo Finance only (no SEC)

---

## Per-Year Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2018 | 2018-11-30 | Correction: SGA (7,882,000 → 95,394,000) |
| 2019 | 2019-11-30 | Correction: SGA (8,828,000 → 105,107,000) |
| 2020 | —          | Missing from Dolt; no Yahoo data available — skipped |
| 2021 | 2021-11-30 | No change |
| 2022 | 2022-11-30 | No change |
| 2023 | 2023-11-30 | No change |
| 2024 | 2024-11-30 | No change |

---

## Notes

- **Non-US company:** No SEC filings. Yahoo Finance is the only data source. H&M reports in SEK under IFRS.
- **H&M fiscal year** ends November 30. DB year label corresponds to the November 30 end date.
- **FY2020 missing from Dolt:** H&M adopted IFRS 16 in fiscal year ending November 30, 2020. That year was not loaded into Dolt, and Yahoo Finance also shows NaN for FY2020 (not included in 4-year history window). FY2020 remains missing.
- **FY2019→FY2021 Total Assets jump:** 120,485,000K (FY2019, pre-IFRS 16) → 179,781,000K (FY2021, post-IFRS 16). The ~59B SEK increase reflects operating lease right-of-use assets added to the balance sheet when H&M adopted IFRS 16 in FY2020 (the missing year). Expected, not an error.
- **[CRITICAL] FY2018 and FY2019 SGA are wrong:** The Dolt values (7,882,000K and 8,828,000K) are implausibly low — they appear to be only H&M's administrative expenses, missing the much larger selling expenses. The correct SGA (total operating expenses ex-COGS) must equal Gross Margin − Operating Profit. FY2018: 95,394,000K; FY2019: 105,107,000K.
- **SGA treatment inconsistency across years (note for DB):**
  - FY2018, FY2019 (after correction): SGA = total OpEx ex-COGS (includes D&A, as D&A not separately reported by Yahoo for these years)
  - FY2021, FY2022: SGA = total OpEx ex-COGS (includes D&A ~22B SEK; Yahoo does not break it out for these years — Rule 3 applies)
  - FY2023, FY2024: SGA = Selling + G&A (D&A ~20–22B SEK shown separately by Yahoo; excluded from SGA)
  - This inconsistency is inherent in Yahoo's reporting of H&M data across years. Operating profit values are correct throughout.
- **Gross margins 51–53%:** Consistent with H&M's fast-fashion model (vertically integrated, strong brand, global scale). Higher than typical specialty retail due to their cost-efficient supply chain.
- **Yahoo data coverage:** Available for FY2022–FY2024 (confirms Dolt values). FY2021 shows NaN in Yahoo. FY2018–FY2020 not in Yahoo history.

---

## FY2018

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 210,400,000 | 210,400,000 |
| Cost of Goods | N/A | 99,513,000 | 99,513,000 |
| Gross Margin | N/A | 110,887,000 | 110,887,000 |
| SGA | N/A | 7,882,000 ❌ | **95,394,000** |
| Operating Profit | N/A | 15,493,000 | 15,493,000 |
| Net Profit | N/A | 12,652,000 | 12,652,000 |
| Inventory | N/A | 37,721,000 | 37,721,000 |
| Current Assets | N/A | 61,576,000 | 61,576,000 |
| Total Assets | N/A | 118,790,000 | 118,790,000 |
| Current Liabilities | N/A | 44,219,000 | 44,219,000 |
| Liabilities | N/A | 60,244,000 | 60,244,000 |
| Total Shareholder Equity | N/A | 58,546,000 | 58,546,000 |
| Total Liabilities and SE | N/A | 118,790,000 | 118,790,000 |

Derived SGA: 110,887,000 (Gross Margin) − 15,493,000 (Operating Profit) = **95,394,000**. Dolt value 7,882,000 is only the administrative expense component; selling expenses (~87.5B SEK) were not captured.

**Balance sheet check:** 118,790,000 = 60,244,000 + 58,546,000 ✓
**Gross margin %:** 52.7%
**Action: Correction — SGA 7,882,000 → 95,394,000**

---

## FY2019

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 232,755,000 | 232,755,000 |
| Cost of Goods | N/A | 110,302,000 | 110,302,000 |
| Gross Margin | N/A | 122,453,000 | 122,453,000 |
| SGA | N/A | 8,828,000 ❌ | **105,107,000** |
| Operating Profit | N/A | 17,346,000 | 17,346,000 |
| Net Profit | N/A | 13,443,000 | 13,443,000 |
| Inventory | N/A | 37,823,000 | 37,823,000 |
| Current Assets | N/A | 62,272,000 | 62,272,000 |
| Total Assets | N/A | 120,485,000 | 120,485,000 |
| Current Liabilities | N/A | 47,836,000 | 47,836,000 |
| Liabilities | N/A | 63,416,000 | 63,416,000 |
| Total Shareholder Equity | N/A | 57,069,000 | 57,069,000 |
| Total Liabilities and SE | N/A | 120,485,000 | 120,485,000 |

Derived SGA: 122,453,000 − 17,346,000 = **105,107,000**. Same issue as FY2018 — only admin expense captured.

**Balance sheet check:** 120,485,000 = 63,416,000 + 57,069,000 ✓
**Gross margin %:** 52.6%
**Action: Correction — SGA 8,828,000 → 105,107,000**

---

## FY2020

**MISSING FROM DOLT.** H&M adopted IFRS 16 in FY2020 (year ending 2020-11-30). Yahoo Finance does not have this year in its history window. FY2020 cannot be verified or loaded without H&M's actual 2020 annual report. Skipped.

---

## FY2021

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 198,967,000 | 198,967,000 |
| Cost of Goods | N/A | 93,961,000 | 93,961,000 |
| Gross Margin | N/A | 105,006,000 | 105,006,000 |
| SGA | N/A | 89,751,000 | 89,751,000 |
| Operating Profit | N/A | 15,255,000 | 15,255,000 |
| Net Profit | N/A | 11,010,000 | 11,010,000 |
| Inventory | N/A | 37,306,000 | 37,306,000 |
| Current Assets | N/A | 78,986,000 | 78,986,000 |
| Total Assets | N/A | 179,781,000 | 179,781,000 |
| Current Liabilities | N/A | 60,997,000 | 60,997,000 |
| Liabilities | N/A | 119,763,000 | 119,763,000 |
| Total Shareholder Equity | N/A | 60,018,000 | 60,018,000 |
| Total Liabilities and SE | N/A | 179,781,000 | 179,781,000 |

SGA check: 105,006,000 − 89,751,000 = 15,255,000 = Operating Profit ✓ (SGA = total OpEx ex-COGS)

**Balance sheet check:** 179,781,000 = 119,763,000 + 60,018,000 ✓
**Gross margin %:** 52.8%
**[INFO] Total Assets reflects IFRS 16 ROU assets (~59B SEK increase from FY2019). Expected.**
**Action:** No change

---

## FY2022

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | 223,553,000 | 223,553,000 | 223,553,000 |
| Cost of Goods | 110,183,000 | 110,183,000 | 110,183,000 |
| Gross Margin | 113,370,000 | 113,370,000 | 113,370,000 |
| SGA | 105,932,000 | 105,932,000 | 105,932,000 |
| Operating Profit | 7,438,000 | 7,438,000 | 7,438,000 |
| Net Profit | 3,566,000 | 3,566,000 | 3,566,000 |
| Inventory | 42,495,000 | 42,495,000 | 42,495,000 |
| Current Assets | 79,523,000 | 79,523,000 | 79,523,000 |
| Total Assets | 182,048,000 | 182,048,000 | 182,048,000 |
| Current Liabilities | 68,335,000 | 68,335,000 | 68,335,000 |
| Liabilities | 131,291,000 | 131,291,000 | 131,291,000 |
| Total Shareholder Equity | 50,757,000 | 50,757,000 | 50,757,000 |
| Total Liabilities and SE | 182,048,000 | 182,048,000 | 182,048,000 |

SGA check: 113,370,000 − 105,932,000 = 7,438,000 = Operating Profit ✓. Yahoo SGA = total OpEx (Rule 3 — D&A not separately broken out for this year).

**Balance sheet check:** 182,048,000 = 131,291,000 + 50,757,000 ✓
**Gross margin %:** 50.7%
**Action:** No change

---

## FY2023

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | 236,035,000 | 236,035,000 | 236,035,000 |
| Cost of Goods | 115,139,000 | 115,139,000 | 115,139,000 |
| Gross Margin | 120,896,000 | 120,896,000 | 120,896,000 |
| SGA | 86,486,000 | 86,486,000 | 86,486,000 |
| Operating Profit | 13,566,000 | 13,566,000 | 13,566,000 |
| Net Profit | 8,745,000 | 8,745,000 | 8,745,000 |
| Inventory | 37,358,000 | 37,358,000 | 37,358,000 |
| Current Assets | 80,529,000 | 80,529,000 | 80,529,000 |
| Total Assets | 181,273,000 | 181,273,000 | 181,273,000 |
| Current Liabilities | 67,927,000 | 67,927,000 | 67,927,000 |
| Liabilities | 133,845,000 | 133,845,000 | 133,845,000 |
| Total Shareholder Equity | 47,428,000 | 47,428,000 | 47,428,000 |
| Total Liabilities and SE | 181,273,000 | 181,273,000 | 181,273,000 |

Yahoo D&A separately reported: 20,844,000K. Total OpEx ex-COGS = 86,486 + 20,844 = 107,330K. Operating Profit = 120,896 − 107,330 = 13,566K ✓.

**Balance sheet check:** 181,273,000 = 133,845,000 + 47,428,000 ✓
**Gross margin %:** 51.2%
**Action:** No change

---

## FY2024

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | 234,478,000 | 234,478,000 | 234,478,000 |
| Cost of Goods | 109,179,000 | 109,179,000 | 109,179,000 |
| Gross Margin | 125,299,000 | 125,299,000 | 125,299,000 |
| SGA | 87,970,000 | 87,970,000 | 87,970,000 |
| Operating Profit | 17,384,000 | 17,384,000 | 17,384,000 |
| Net Profit | 11,621,000 | 11,621,000 | 11,621,000 |
| Inventory | 40,348,000 | 40,348,000 | 40,348,000 |
| Current Assets | 75,727,000 | 75,727,000 | 75,727,000 |
| Total Assets | 180,214,000 | 180,214,000 | 180,214,000 |
| Current Liabilities | 66,650,000 | 66,650,000 | 66,650,000 |
| Liabilities | 134,072,000 | 134,072,000 | 134,072,000 |
| Total Shareholder Equity | 46,142,000 | 46,142,000 | 46,142,000 |
| Total Liabilities and SE | 180,214,000 | 180,214,000 | 180,214,000 |

Yahoo D&A separately reported: 19,945,000K. Total OpEx ex-COGS = 87,970 + 19,945 = 107,915K. Operating Profit = 125,299 − 107,915 = 17,384K ✓.

**Balance sheet check:** 180,214,000 = 134,072,000 + 46,142,000 ✓
**Gross margin %:** 53.4%
**Action:** No change

---

**Analysis complete for HM-B.ST.** Two corrections needed (FY2018 and FY2019 SGA — selling expenses were not captured). FY2020 remains missing from Dolt. Run `/create-verified-dolt-db-financials-sql HM-B.ST` to generate SQL.
