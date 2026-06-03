# Abercrombie & Fitch (ANF) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-03
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2019-02-02 | Correction: SGA (484,863→2,021,079), Net Profit (78,808→74,541) |
| 2019 | 2020-02-01 | Correction: SGA (464,615→2,015,858), Net Profit (44,960→39,358) |
| 2020 | 2021-01-30 | Correction: SGA (463,843→1,843,791), Net Profit (108,954→-103,887) |
| 2021 | 2022-01-29 | Correction: SGA (536,815→1,965,138), Net Profit (270,066→263,010) |
| 2022 | 2023-01-28 | Correction: SGA (517,602→2,014,560), Net Profit (10,385→2,816) |
| 2023 | 2024-02-03 | No change (all fields confirmed vs SEC + Yahoo) |
| 2024 | 2025-02-01 | Correction: reportDate (2025-02-03→2025-02-01) |
| 2025 | 2026-01-31 | New insert |

---

## Notes

- **US company:** CIK = 1018840. SEC 10-K filings fetched for FY2019 (covers FY2018–FY2019), FY2022 (covers FY2020–FY2022), FY2023, FY2024, FY2025.
- **Fiscal year end:** Late January / early February each year.
- **Currency:** All values in $thousands (USD).
- **Segment:** Specialty apparel (Abercrombie brand + Hollister). Gross margins consistently 60–65%, above the 35–55% benchmark — expected for ANF's premium positioning.
- **SGA construction (critical):** ANF files two SGA-type lines separately:
  - `anf_StoresAndDistributionExpense` (stores, labor, occupancy)
  - `anf_MarketingGeneralAndAdministrativeExpense` (marketing + G&A)
  - Correct DB SGA = sum of both. Dolt FY2018–FY2022 captured only the MG&A component.
  - Also exclude: `anf_Flagshipstoreexitcharges` (one-time restructuring) and `anf_Assetimpairmentexclusiveofflagshipstoreexitcharges` (impairment). These are not SGA.
  - Starting FY2023–FY2024 Dolt correctly used the combined figure.
- **Net Profit consistency:** ANF has minority interest (NCI in franchise/sourcing JVs). FY2023–FY2024 Dolt correctly uses `us-gaap_NetIncomeLoss` (A&F portion, excludes NCI). FY2018–FY2022 Dolt used `us-gaap_ProfitLoss` (total including NCI). Correcting all prior years to NetIncomeLoss (A&F only) for consistency.
- **FY2020 Net Profit sign error:** Dolt has 108,954K (positive). COVID year — actual net loss was -103,887K. Both sign and value corrected.
- **FY2018 balance sheet:** Dolt holds the pre-ASC 842 values (from original FY2018 10-K, no ROU assets on balance sheet). The FY2019 10-K comparative restates FY2018 under ASC 842, adding ~$1.17B of ROU assets/liabilities. Dolt retains original pre-ASC 842 values for FY2018 — balance sheet identity passes (2,385,593 ✓).
- **FY2019 balance sheet:** Confirmed against SEC FY2019 10-K (post-ASC 842 adoption). All values match.
- **FY2024 reportDate:** SEC 10-K period header = 2025-02-01; Dolt has 2025-02-03. Correcting to SEC value.
- **TSE convention:** Dolt uses Total Equity Gross Minority Interest (includes minority interest) as Total Shareholder Equity for ANF — consistent across all years.

---

## FY2018

**Sources:** Dolt + SEC (FY2019 10-K, comparative column 2019-02-02). Balance sheet: pre-ASC 842 (original filing).

### Anomaly Detection
- `[WARNING]` SGA in Dolt (484,863K) captures only `anf_MarketingGeneralAndAdministrativeExpense`. Missing `anf_StoresAndDistributionExpense` (1,536,216K). Correcting.
- `[WARNING]` Net Profit (78,808K) uses ProfitLoss including NCI (4,267K). Correcting to NetIncomeLoss A&F = 74,541K.
- `[WARNING]` Balance sheet not confirmed against SEC — Dolt holds pre-ASC 842 values (no ROU assets). Identity check passes: 1,176,693 + 1,208,900 = 2,385,593 ✓
- Gross margin: 2,159,916 / 3,590,109 = 60.2% — above Specialty benchmark (35–55%); expected for ANF premium positioning.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 3,590,109 | — | 3,590,109 | 3,590,109 |
| Cost of Goods | 1,430,193 | — | 1,430,193 | 1,430,193 |
| Gross Margin | 2,159,916 | — | 2,159,916 | 2,159,916 |
| SGA | **2,021,079*** | — | 484,863* | **2,021,079** |
| Operating Profit | 127,366 | — | 127,366 | 127,366 |
| Net Profit | **74,541** | — | 78,808* | **74,541** |
| Inventory | 437,879 | — | 437,879 | 437,879 |
| Current Assets | — (ASC 842) | — | 1,335,950 | 1,335,950 |
| Total Assets | — (ASC 842) | — | 2,385,593 | 2,385,593 |
| Current Liabilities | — (ASC 842) | — | 558,917 | 558,917 |
| Liabilities | — (ASC 842) | — | 1,176,693 | 1,176,693 |
| Total SE | — (ASC 842) | — | 1,208,900 | 1,208,900 |
| Total L+SE | — (ASC 842) | — | 2,385,593 | 2,385,593 |

*SEC SGA = StoresAndDist (1,536,216) + MG&A (484,863) = 2,021,079K; excludes exit charges (5,806K) and impairment (11,580K).
*Dolt Net Profit = ProfitLoss (78,808K); correct = NetIncomeLoss A&F (74,541K).

**Action: Correction — SGA and Net Profit. Balance sheet unchanged (pre-ASC 842).**

---

## FY2019

**Sources:** Dolt + SEC (FY2019 10-K, leftmost column 2020-02-01). Balance sheet fully confirmed.

### Anomaly Detection
- `[WARNING]` SGA in Dolt (464,615K) captures only `anf_MarketingGeneralAndAdministrativeExpense`. Missing `anf_StoresAndDistributionExpense` (1,551,243K). Correcting.
- `[WARNING]` Net Profit (44,960K) uses ProfitLoss including NCI (5,602K). Correcting to NetIncomeLoss A&F = 39,358K.
- Balance sheet fully confirmed vs SEC FY2019 10-K ✓
- Gross margin: 2,150,918 / 3,623,073 = 59.4% — above Specialty benchmark; expected for ANF.
- Balance sheet: 2,478,487 + 1,071,178 = 3,549,665 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 3,623,073 | — | 3,623,073 | 3,623,073 |
| Cost of Goods | 1,472,155 | — | 1,472,155 | 1,472,155 |
| Gross Margin | 2,150,918 | — | 2,150,918 | 2,150,918 |
| SGA | **2,015,858*** | — | 464,615* | **2,015,858** |
| Operating Profit | 70,068 | — | 70,068 | 70,068 |
| Net Profit | **39,358** | — | 44,960* | **39,358** |
| Inventory | 434,326 | — | 434,326 | 434,326 |
| Current Assets | 1,264,749 | — | 1,264,749 | 1,264,749 |
| Total Assets | 3,549,665 | — | 3,549,665 | 3,549,665 |
| Current Liabilities | 815,354 | — | 815,354 | 815,354 |
| Liabilities | 2,478,487 | — | 2,478,487 | 2,478,487 |
| Total SE | 1,071,178 | — | 1,071,178 | 1,071,178 |
| Total L+SE | 3,549,665 | — | 3,549,665 | 3,549,665 |

*SEC SGA = StoresAndDist (1,551,243) + MG&A (464,615) = 2,015,858K; excludes exit charges (47,257K) and impairment (19,135K).
*Dolt Net Profit = ProfitLoss (44,960K); correct = NetIncomeLoss A&F (39,358K).

**Action: Correction — SGA and Net Profit. All balance sheet fields confirmed.**

---

## FY2020

**Sources:** Dolt + SEC (FY2022 10-K, comparative column 2021-01-30). Balance sheet: unverified (identity check passes).

### Anomaly Detection
- `[WARNING]` SGA in Dolt (463,843K) captures only `anf_MarketingGeneralAndAdministrativeExpense`. Missing `anf_StoresAndDistributionExpense` (1,379,948K). Correcting.
- `[ERROR]` Net Profit (108,954K) has wrong sign AND wrong value. COVID year — SEC shows ProfitLoss = -108,954K (loss). A&F portion (NetIncomeLoss) = -103,887K. Correcting to -103,887K.
- `[WARNING]` Balance sheet not confirmed from SEC (FY2020 10-K not fetched). Identity check passes: 2,365,590 + 949,312 = 3,314,902 ✓
- Gross margin: 1,891,205 / 3,125,384 = 60.5% — above Specialty benchmark; expected for ANF.
- Operating Profit = -20,469K (COVID store closures). Tax provision of 60,211K (expense, not benefit) created the larger net loss.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 3,125,384 | — | 3,125,384 | 3,125,384 |
| Cost of Goods | 1,234,179 | — | 1,234,179 | 1,234,179 |
| Gross Margin | 1,891,205 | — | 1,891,205 | 1,891,205 |
| SGA | **1,843,791*** | — | 463,843* | **1,843,791** |
| Operating Profit | -20,469 | — | -20,469 | -20,469 |
| Net Profit | **-103,887** | — | 108,954* | **-103,887** |
| Inventory | — | — | 404,053 | 404,053 |
| Current Assets | — | — | 1,661,629 | 1,661,629 |
| Total Assets | — | — | 3,314,902 | 3,314,902 |
| Current Liabilities | — | — | 959,399 | 959,399 |
| Liabilities | — | — | 2,365,590 | 2,365,590 |
| Total SE | — | — | 949,312 | 949,312 |
| Total L+SE | — | — | 3,314,902 | 3,314,902 |

*SEC SGA = StoresAndDist (1,379,948) + MG&A (463,843) = 1,843,791K; excludes impairment (72,937K).
*Dolt Net Profit = 108,954K (positive, incorrect — sign error and NCI-inclusion error). Correct = NetIncomeLoss A&F = ProfitLoss (-108,954) - NCI (-5,067) = -103,887K.

**Action: Correction — SGA and Net Profit (including sign). Balance sheet unchanged.**

---

## FY2021

**Sources:** Dolt + SEC (FY2022 10-K, comparative column 2022-01-29). Balance sheet: unverified (identity check passes).

### Anomaly Detection
- `[WARNING]` SGA in Dolt (536,815K) captures only `anf_MarketingGeneralAndAdministrativeExpense`. Missing `anf_StoresAndDistributionExpense` (1,428,323K). Correcting.
- `[WARNING]` Net Profit (270,066K) uses ProfitLoss including NCI (7,056K). Correcting to NetIncomeLoss A&F = 263,010K.
- `[WARNING]` Balance sheet not confirmed from SEC (FY2021 10-K not fetched). Identity check passes: 2,102,167 + 837,324 = 2,939,491 ✓
- Gross margin: 2,311,995 / 3,712,768 = 62.3% — above Specialty benchmark; expected for ANF.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 3,712,768 | — | 3,712,768 | 3,712,768 |
| Cost of Goods | 1,400,773 | — | 1,400,773 | 1,400,773 |
| Gross Margin | 2,311,995 | — | 2,311,995 | 2,311,995 |
| SGA | **1,965,138*** | — | 536,815* | **1,965,138** |
| Operating Profit | 343,084 | — | 343,084 | 343,084 |
| Net Profit | **263,010** | — | 270,066* | **263,010** |
| Inventory | — | — | 525,864 | 525,864 |
| Current Assets | — | — | 1,507,759 | 1,507,759 |
| Total Assets | — | — | 2,939,491 | 2,939,491 |
| Current Liabilities | — | — | 1,015,240 | 1,015,240 |
| Liabilities | — | — | 2,102,167 | 2,102,167 |
| Total SE | — | — | 837,324 | 837,324 |
| Total L+SE | — | — | 2,939,491 | 2,939,491 |

*SEC SGA = StoresAndDist (1,428,323) + MG&A (536,815) = 1,965,138K; excludes impairment (12,100K).
*Dolt Net Profit = ProfitLoss (270,066K); correct = NetIncomeLoss A&F (263,010K).

**Action: Correction — SGA and Net Profit. Balance sheet unchanged.**

---

## FY2022

**Sources:** Dolt + SEC (FY2022 10-K, leftmost column 2023-01-28; FY2023 10-K restated comparative) + Yahoo (column 2023-01-31).

### Anomaly Detection
- `[WARNING]` SGA in Dolt (517,602K) captures only `anf_MarketingGeneralAndAdministrativeExpense`. Correcting to 2,014,560K using Yahoo (which reflects the most-recently-stated FY2023 10-K comparative figures: StoresAndDist 1,496,962 + MG&A 517,602 = 2,014,564K, rounds to 2,014,560K).
- `[WARNING]` Net Profit (10,385K) uses ProfitLoss including NCI (7,569K). Correcting to NetIncomeLoss A&F = 2,816K.
- All balance sheet fields confirmed vs SEC ✓
- Gross margin: 2,104,538 / 3,697,751 = 56.9% — slightly above Specialty benchmark; expected for ANF.
- Balance sheet: 2,006,531 + 706,569 = 2,713,100 = Total Assets ✓
- Note: FY2022 10-K shows StoresAndDist = 1,482,931K. FY2023 10-K restated this to 1,496,962K (+14,031K, reclassifying the asset impairment). Per restatement rule, use most recent filing = 2,014,560K.

### Side-by-Side

| Field | SEC (FY2022) | SEC (restated) | Yahoo | Dolt | Recommended |
|-------|-------------|----------------|-------|------|-------------|
| Net Revenue | 3,697,751 | 3,697,751 | 3,697,751 | 3,697,751 | 3,697,751 |
| Cost of Goods | 1,593,213 | 1,593,213 | 1,593,213 | 1,593,213 | 1,593,213 |
| Gross Margin | 2,104,538 | 2,104,538 | 2,104,538 | 2,104,538 | 2,104,538 |
| SGA | 2,000,533 | **2,014,564*** | 2,014,560 | 517,602* | **2,014,560** |
| Operating Profit | 92,648 | 92,648 | 92,648 | 92,648 | 92,648 |
| Net Profit | 10,385 | 10,385 | **2,816*** | 10,385* | **2,816** |
| Inventory | 505,621 | 505,621 | 505,621 | 505,621 | 505,621 |
| Current Assets | 1,228,018 | 1,228,018 | 1,228,018 | 1,228,018 | 1,228,018 |
| Total Assets | 2,713,100 | 2,713,100 | 2,713,100 | 2,713,100 | 2,713,100 |
| Current Liabilities | 902,200 | 902,200 | 902,200 | 902,200 | 902,200 |
| Liabilities | 2,006,531 | 2,006,531 | 2,006,531 | 2,006,531 | 2,006,531 |
| Total SE | 706,569 | 706,569 | 706,569 | 706,569 | 706,569 |
| Total L+SE | 2,713,100 | 2,713,100 | 2,713,100 | 2,713,100 | 2,713,100 |

*Restated SGA from FY2023 10-K comparative = 1,496,962 + 517,602 = 2,014,564 ≈ 2,014,560K (Yahoo).
*Yahoo Net Income Common Stockholders = 2,816K = NetIncomeLoss A&F per SEC.

**Action: Correction — SGA and Net Profit. All balance sheet fields confirmed, no change.**

---

## FY2023

**Sources:** Dolt + SEC (FY2023 10-K, leftmost column 2024-02-03) + Yahoo (column 2024-01-31).

### Anomaly Detection
- All income statement fields confirmed: SEC = Dolt = Yahoo ✓
- All balance sheet fields confirmed: SEC = Dolt ✓
- Gross margin: 2,693,412 / 4,280,677 = 62.9% — above Specialty benchmark; expected for ANF.
- Balance sheet: 1,924,246 + 1,049,987 = 2,974,233 = Total Assets ✓
- SGA = Stores & Distribution (1,571,737) + MG&A (642,877) = 2,214,614K ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 4,280,677 | 4,280,677 | 4,280,677 | 4,280,677 |
| Cost of Goods | 1,587,265 | 1,587,265 | 1,587,265 | 1,587,265 |
| Gross Margin | 2,693,412 | 2,693,412 | 2,693,412 | 2,693,412 |
| SGA | 2,214,614 | 2,214,610 | 2,214,614 | 2,214,614 |
| Operating Profit | 484,671 | 484,671 | 484,671 | 484,671 |
| Net Profit | 328,123 | 328,123 | 328,123 | 328,123 |
| Inventory | 469,466 | 469,466 | 469,466 | 469,466 |
| Current Assets | 1,537,265 | 1,537,265 | 1,537,265 | 1,537,265 |
| Total Assets | 2,974,233 | 2,974,233 | 2,974,233 | 2,974,233 |
| Current Liabilities | 966,820 | 966,820 | 966,820 | 966,820 |
| Liabilities | 1,924,246 | 1,924,246 | 1,924,246 | 1,924,246 |
| Total SE | 1,049,987 | 1,049,987 | 1,049,987 | 1,049,987 |
| Total L+SE | 2,974,233 | 2,974,233 | 2,974,233 | 2,974,233 |

**Action: No change.**

---

## FY2024

**Sources:** Dolt + SEC (FY2024 10-K, leftmost column 2025-02-01) + Yahoo (column 2025-01-31).

### Anomaly Detection
- `[WARNING]` reportDate: Dolt has 2025-02-03; SEC 10-K header shows 2025-02-01. Correcting.
- All financial fields confirmed: SEC = Dolt = Yahoo ✓
- Gross margin: 3,174,661 / 4,948,587 = 64.1% — above Specialty benchmark; expected for ANF.
- Balance sheet: 1,948,564 + 1,351,323 = 3,299,887 = Total Assets ✓
- SGA = Selling (1,689,988) + G&A (750,485) = 2,440,473K ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| reportDate | **2025-02-01*** | 2025-01-31 | 2025-02-03* | **2025-02-01** |
| Net Revenue | 4,948,587 | 4,948,587 | 4,948,587 | 4,948,587 |
| Cost of Goods | 1,773,926 | 1,773,926 | 1,773,926 | 1,773,926 |
| Gross Margin | 3,174,661 | 3,174,661 | 3,174,661 | 3,174,661 |
| SGA | 2,440,473 | 2,440,470 | 2,440,473 | 2,440,473 |
| Operating Profit | 740,820 | 740,820 | 740,820 | 740,820 |
| Net Profit | 566,223 | 566,223 | 566,223 | 566,223 |
| Inventory | 575,005 | 575,005 | 575,005 | 575,005 |
| Current Assets | 1,673,431 | 1,673,431 | 1,673,431 | 1,673,431 |
| Total Assets | 3,299,887 | 3,299,887 | 3,299,887 | 3,299,887 |
| Current Liabilities | 1,126,944 | 1,126,944 | 1,126,944 | 1,126,944 |
| Liabilities | 1,948,564 | 1,948,564 | 1,948,564 | 1,948,564 |
| Total SE | 1,351,323 | 1,351,323 | 1,351,323 | 1,351,323 |
| Total L+SE | 3,299,887 | 3,299,887 | 3,299,887 | 3,299,887 |

*SEC fiscal year end per 10-K header = 2025-02-01. Dolt 2025-02-03 is incorrect.

**Action: Correction — reportDate only. All financial values confirmed, no change.**

---

## FY2025

**Sources:** SEC (FY2025 10-K, leftmost column 2026-01-31) + Yahoo (column 2026-01-31). New insert — not yet in Dolt.

### Anomaly Detection
- All fields confirmed: SEC = Yahoo ✓
- Gross margin: 3,237,408 / 5,266,292 = 61.5% — above Specialty benchmark; expected for ANF.
- Balance sheet: 2,121,463 + 1,420,411 = 3,541,874 = Total Assets ✓
- SGA = Selling (1,809,633) + G&A (725,471) = 2,535,104K ✓
- Net Profit 506,921K is slightly lower than FY2024 (566,223K) — reflects modest slowdown after peak FY2024 growth; not a data anomaly.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 5,266,292 | 5,266,290 | — | 5,266,292 |
| Cost of Goods | 2,028,884 | 2,028,880 | — | 2,028,884 |
| Gross Margin | 3,237,408 | 3,237,410 | — | 3,237,408 |
| SGA | 2,535,104 | 2,535,100 | — | 2,535,104 |
| Operating Profit | 699,143 | 699,143 | — | 699,143 |
| Net Profit | 506,921 | 506,921 | — | 506,921 |
| Inventory | 601,218 | 601,218 | — | 601,218 |
| Current Assets | 1,650,464 | 1,650,460 | — | 1,650,464 |
| Total Assets | 3,541,874 | 3,541,870 | — | 3,541,874 |
| Current Liabilities | 1,106,000 | 1,106,000 | — | 1,106,000 |
| Liabilities | 2,121,463 | 2,121,460 | — | 2,121,463 |
| Total SE | 1,420,411 | 1,420,411 | — | 1,420,411 |
| Total L+SE | 3,541,874 | 3,541,870 | — | 3,541,874 |

**Action: New insert.**

---

## Unresolved Flags

1. `[WARNING]` FY2018 balance sheet uses pre-ASC 842 values (original FY2018 10-K). The FY2019 10-K comparative shows a restated balance sheet with ~$1.17B higher assets/liabilities due to operating lease ROU recognition. Dolt retains original values — note the accounting discontinuity between FY2018 and FY2019.
2. `[WARNING]` FY2020 and FY2021 balance sheets not verified from SEC (FY2020 and FY2021 10-Ks not fetched). Both pass identity checks.

**Analysis complete.** Run `/insert-financials ANF` to write all changed years to the database.
