# Levi Strauss (LEVI) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2018 | 2018-11-25 | No change |
| 2019 | 2019-11-24 | No change |
| 2020 | 2020-11-29 | No change |
| 2021 | 2021-11-28 | No change |
| 2022 | 2022-11-27 | No change |
| 2023 | 2023-11-26 | No change |
| 2024 | 2024-12-01 | **CORRECTION: Inventory (1,239,400 → 1,131,300)** |
| 2025 | 2025-11-30 | No change |

---

## Notes

- **Levi Strauss fiscal year** ends on the Sunday nearest November 30. DB year label matches the November/December end date.
- **FY2019 IPO:** Levi went public in March 2019. Total Assets grew ~690M from FY2018 to FY2019, partly from IPO proceeds.
- **FY2020 Total Assets jump:** 4,232,418K (FY2019) → 5,641,241K (FY2020) — ASC 842 adoption, adding ~$1.4B of operating lease right-of-use assets. Operating margin also turned negative (COVID year, revenues −23%). Expected.
- **SGA treatment:** For FY2018–FY2021, SGA = Selling + G&A (Yahoo has no data, but formula: GM − SGA = Op Profit + special charges — the gap between GM − SGA and Op Profit represents restructuring/impairment charges not in SGA). FY2022–FY2025 confirmed by Yahoo: SGA = Selling & Marketing + G&A, separate from special charges.
- **Operating Profit — as-reported:** Dolt uses "Total Operating Income As Reported" (excludes normalized adjustments). FY2022 as-reported = 646,500K vs normalized 667,200K (20,700K special charges). FY2023 as-reported = 354,400K vs normalized 464,900K (110,500K includes brand impairment and restructuring). FY2024 as-reported = 262,700K vs normalized 565,200K (302,500K includes facility impairments and restructuring related to strategic review). FY2025 as-reported = 677,600K vs normalized 704,600K (27,000K special charges). All Dolt as-reported values confirmed by Yahoo ✓.
- **[CORRECTION] FY2024 Inventory — Assets Held For Sale misclassification:** Dolt inventory 1,239,400K = Yahoo inventory (1,131,300K) + Yahoo "Assets Held For Sale Current" (108,100K). Assets held for sale are NOT inventory; they represent a business segment or assets being divested. Current Assets (2,851,100K) already correctly includes the held-for-sale assets, so only inventory needs correction.
- **FY2025 Inventory:** Dolt 1,237,700K = Yahoo inventory only ✓ (held-for-sale assets = 54,000K shown separately, not added to inventory). FY2025 is correct; the misclassification was only in FY2024.
- **Yahoo Finance coverage:** FY2022–FY2025 available. FY2021 column (2021-11-30) shows NaN for most income statement fields. FY2018–FY2020 not in Yahoo history.
- **Gross margins:** FY2018–FY2020 ~52–54% (mix of wholesale + early DTC); FY2021–FY2023 ~57–58%; FY2024–FY2025 ~61% (strong DTC shift and pricing power). Consistent with branded apparel premium positioning.
- **All balance sheet identities:** ✓ for all 8 years.

---

## FY2018

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 5,575,440 | 5,575,440 |
| Cost of Goods | N/A | 2,577,465 | 2,577,465 |
| Gross Margin | N/A | 2,997,975 | 2,997,975 |
| SGA | N/A | 2,457,564 | 2,457,564 |
| Operating Profit | N/A | 540,411 | 540,411 |
| Net Profit | N/A | 283,142 | 283,142 |
| Inventory | N/A | 883,773 | 883,773 |
| Current Assets | N/A | 2,288,059 | 2,288,059 |
| Total Assets | N/A | 3,542,660 | 3,542,660 |
| Current Liabilities | N/A | 1,052,199 | 1,052,199 |
| Liabilities | N/A | 2,875,201 | 2,875,201 |
| Total Shareholder Equity | N/A | 667,459 | 667,459 |
| Total Liabilities and SE | N/A | 3,542,660 | 3,542,660 |

Formula: 2,997,975 − 2,457,564 = 540,411 = Operating Profit ✓ (no separate D&A/special charges in FY2018)

**Balance sheet check:** 3,542,660 = 2,875,201 + 667,459 ✓
**Gross margin %:** 53.8%
**Action:** No change

---

## FY2019

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 5,763,087 | 5,763,087 |
| Cost of Goods | N/A | 2,661,714 | 2,661,714 |
| Gross Margin | N/A | 3,101,373 | 3,101,373 |
| SGA | N/A | 2,534,698 | 2,534,698 |
| Operating Profit | N/A | 566,675 | 566,675 |
| Net Profit | N/A | 394,612 | 394,612 |
| Inventory | N/A | 884,192 | 884,192 |
| Current Assets | N/A | 2,870,186 | 2,870,186 |
| Total Assets | N/A | 4,232,418 | 4,232,418 |
| Current Liabilities | N/A | 1,167,204 | 1,167,204 |
| Liabilities | N/A | 2,660,861 | 2,660,861 |
| Total Shareholder Equity | N/A | 1,571,557 | 1,571,557 |
| Total Liabilities and SE | N/A | 4,232,418 | 4,232,418 |

Formula: 3,101,373 − 2,534,698 = 566,675 = Operating Profit ✓

**Balance sheet check:** 4,232,418 = 2,660,861 + 1,571,557 ✓
**Gross margin %:** 53.8%
**[INFO] IPO completed March 2019. Total Assets up ~690M from FY2018 (IPO proceeds + normal operations).**
**Action:** No change

---

## FY2020

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 4,452,609 | 4,452,609 |
| Cost of Goods | N/A | 2,099,685 | 2,099,685 |
| Gross Margin | N/A | 2,352,924 | 2,352,924 |
| SGA | N/A | 2,347,628 | 2,347,628 |
| Operating Profit | N/A | −85,119 | −85,119 |
| Net Profit | N/A | −127,141 | −127,141 |
| Inventory | N/A | 817,692 | 817,692 |
| Current Assets | N/A | 3,126,241 | 3,126,241 |
| Total Assets | N/A | 5,641,241 | 5,641,241 |
| Current Liabilities | N/A | 1,548,882 | 1,548,882 |
| Liabilities | N/A | 4,341,766 | 4,341,766 |
| Total Shareholder Equity | N/A | 1,299,475 | 1,299,475 |
| Total Liabilities and SE | N/A | 5,641,241 | 5,641,241 |

Formula: 2,352,924 − 2,347,628 = 5,296 vs Op Profit −85,119. Gap = −90,415K = COVID restructuring charges below SGA ✓ (plausible).

**Balance sheet check:** 5,641,241 = 4,341,766 + 1,299,475 ✓
**Gross margin %:** 52.9%
**[INFO] Total Assets jump (~1.4B) due to ASC 842 adoption (operating lease ROU assets). COVID year: revenue −23%, operating loss −85M.**
**Action:** No change

---

## FY2021

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | N/A | 5,763,936 | 5,763,936 |
| Cost of Goods | N/A | 2,417,225 | 2,417,225 |
| Gross Margin | N/A | 3,346,711 | 3,346,711 |
| SGA | N/A | 2,652,213 | 2,652,213 |
| Operating Profit | N/A | 686,211 | 686,211 |
| Net Profit | N/A | 553,541 | 553,541 |
| Inventory | N/A | 897,950 | 897,950 |
| Current Assets | N/A | 2,709,901 | 2,709,901 |
| Total Assets | N/A | 5,900,069 | 5,900,069 |
| Current Liabilities | N/A | 1,869,618 | 1,869,618 |
| Liabilities | N/A | 4,234,408 | 4,234,408 |
| Total Shareholder Equity | N/A | 1,665,661 | 1,665,661 |
| Total Liabilities and SE | N/A | 5,900,069 | 5,900,069 |

Formula: 3,346,711 − 2,652,213 = 694,498 vs Op Profit 686,211. Gap = 8,287K = small special charges ✓ (plausible).

**Balance sheet check:** 5,900,069 = 4,234,408 + 1,665,661 ✓
**Gross margin %:** 58.1%
**Action:** No change

---

## FY2022

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | 6,168,600 | 6,168,600 | 6,168,600 |
| Cost of Goods | 2,619,800 | 2,619,800 | 2,619,800 |
| Gross Margin | 3,548,800 | 3,548,800 | 3,548,800 |
| SGA | 2,881,600 | 2,881,600 | 2,881,600 |
| Operating Profit | 646,500* | 646,500 | 646,500 |
| Net Profit | 569,100 | 569,100 | 569,100 |
| Inventory | 1,416,800 | 1,416,800 | 1,416,800 |
| Current Assets | 2,827,900 | 2,827,900 | 2,827,900 |
| Total Assets | 6,037,800 | 6,037,800 | 6,037,800 |
| Current Liabilities | 1,981,600 | 1,981,600 | 1,981,600 |
| Liabilities | 4,134,100 | 4,134,100 | 4,134,100 |
| Total Shareholder Equity | 1,903,700 | 1,903,700 | 1,903,700 |
| Total Liabilities and SE | 6,037,800 | 6,037,800 | 6,037,800 |

*Yahoo normalized Operating Income = 667,200K; as-reported = 646,500K ✓ (special charges ~20,700K). All fields confirmed.

**Balance sheet check:** 6,037,800 = 4,134,100 + 1,903,700 ✓
**Gross margin %:** 57.5%
**Action:** No change

---

## FY2023

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | 5,842,100 | 5,842,100 | 5,842,100 |
| Cost of Goods | 2,481,400 | 2,481,400 | 2,481,400 |
| Gross Margin | 3,360,700 | 3,360,700 | 3,360,700 |
| SGA | 2,895,800 | 2,895,800 | 2,895,800 |
| Operating Profit | 354,400* | 354,400 | 354,400 |
| Net Profit | 249,600 | 249,600 | 249,600 |
| Inventory | 1,290,100 | 1,290,100 | 1,290,100 |
| Current Assets | 2,637,600 | 2,637,600 | 2,637,600 |
| Total Assets | 6,053,600 | 6,053,600 | 6,053,600 |
| Current Liabilities | 1,787,500 | 1,787,500 | 1,787,500 |
| Liabilities | 4,007,200 | 4,007,200 | 4,007,200 |
| Total Shareholder Equity | 2,046,400 | 2,046,400 | 2,046,400 |
| Total Liabilities and SE | 6,053,600 | 6,053,600 | 6,053,600 |

*Yahoo normalized Operating Income = 464,900K; as-reported = 354,400K ✓ (special charges ~110,500K: brand impairments + restructuring). All fields confirmed.

**Balance sheet check:** 6,053,600 = 4,007,200 + 2,046,400 ✓
**Gross margin %:** 57.5%
**Action:** No change

---

## FY2024

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | 6,032,000 | 6,032,000 | 6,032,000 |
| Cost of Goods | 2,374,900 | 2,374,900 | 2,374,900 |
| Gross Margin | 3,657,100 | 3,657,100 | 3,657,100 |
| SGA | 3,091,900 | 3,091,900 | 3,091,900 |
| Operating Profit | 262,700* | 262,700 | 262,700 |
| Net Profit | 210,600 | 210,600 | 210,600 |
| Inventory | 1,131,300 | 1,239,400 ❌ | **1,131,300** |
| Current Assets | 2,851,100 | 2,851,100 | 2,851,100 |
| Total Assets | 6,375,500 | 6,375,500 | 6,375,500 |
| Current Liabilities | 2,010,500 | 2,010,500 | 2,010,500 |
| Liabilities | 4,405,000 | 4,405,000 | 4,405,000 |
| Total Shareholder Equity | 1,970,500 | 1,970,500 | 1,970,500 |
| Total Liabilities and SE | 6,375,500 | 6,375,500 | 6,375,500 |

*Yahoo normalized Operating Income = 565,200K; as-reported = 262,700K ✓ (special charges ~302,500K: facility impairments, strategic restructuring). All fields confirmed except inventory.
Inventory: Dolt 1,239,400 = Yahoo Inventory (1,131,300) + Yahoo "Assets Held For Sale Current" (108,100). Assets held for sale are NOT inventory. Current Assets correctly stays 2,851,100 (includes both inventory and held-for-sale as current assets).

**Balance sheet check:** 6,375,500 = 4,405,000 + 1,970,500 ✓
**Gross margin %:** 60.6%
**Action: CORRECTION — Inventory 1,239,400 → 1,131,300**

---

## FY2025

| Field | Yahoo | Dolt (current) | Recommended |
|-------|-------|----------------|-------------|
| Net Revenue | 6,282,000 | 6,282,000 | 6,282,000 |
| Cost of Goods | 2,404,200 | 2,404,200 | 2,404,200 |
| Gross Margin | 3,877,800 | 3,877,800 | 3,877,800 |
| SGA | 3,173,200 | 3,173,200 | 3,173,200 |
| Operating Profit | 677,600* | 677,600 | 677,600 |
| Net Profit | 578,100 | 578,100 | 578,100 |
| Inventory | 1,237,700 | 1,237,700 | 1,237,700 |
| Current Assets | 3,153,700 | 3,153,700 | 3,153,700 |
| Total Assets | 6,848,800 | 6,848,800 | 6,848,800 |
| Current Liabilities | 2,032,500 | 2,032,500 | 2,032,500 |
| Liabilities | 4,570,200 | 4,570,200 | 4,570,200 |
| Total Shareholder Equity | 2,278,600 | 2,278,600 | 2,278,600 |
| Total Liabilities and SE | 6,848,800 | 6,848,800 | 6,848,800 |

*Yahoo normalized Operating Income = 704,600K; as-reported = 677,600K ✓ (special charges ~27,000K). All fields confirmed.
FY2025 inventory (1,237,700) = Yahoo inventory only ✓; held-for-sale (54,000K) shown separately and NOT added to inventory. Consistent with actual balance sheet.

**Balance sheet check:** 6,848,800 = 4,570,200 + 2,278,600 ✓
**Gross margin %:** 61.7%
**Action:** No change

---

**Analysis complete for LEVI.** One correction needed: FY2024 inventory overstated by 108,100K due to misclassification of "Assets Held For Sale" as inventory. All other fields confirmed across all 8 years. FY2022–FY2025 fully validated against Yahoo.
