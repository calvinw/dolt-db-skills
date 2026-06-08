# BusMgmtBenchmarks — 2018–2024 Verification Summary

**Generated:** 2026-06-08
**Source:** 59 `*-all-years.md` report files in `reports/`
**Scope:** Fiscal years 2018–2024 only (2025 excluded)

---

## No Changes (all years 2018–2024 match across sources)

| # | Ticker | Notes |
|---|--------|-------|
| 1 | **ADS.DE** | No change — cannot verify (non-US, no Yahoo/SEC data) |
| 2 | **ATZ.TO** | No change — Yahoo data only (non-Canadian ticker) |
| 3 | **BURL** | No change — Dolt matches SEC across all years |
| 4 | **CPRI** | No change — all values confirmed |
| 5 | **ETSY** | No change — all values confirmed |
| 6 | **HD** | No change — all values confirmed |
| 7 | **ITX.MC** | No change — all values confirmed (non-US) |
| 8 | **LULU** | No change — all values confirmed |
| 9 | **ROST** | No change — all values confirmed |
| 10 | **ULTA** | No change — all values confirmed |
| 11 | **YETI** | No change — all values confirmed |

---

## Changes (at least one year 2018–2024 requires correction)

### All years have changes

| Ticker | Years | Issues |
|--------|-------|--------|
| **BABA** | 2018–2024 | All 7 years need fixes — scope not detailed in summary |
| **BBWI** | 2018–2024 | Wrong CIK in Dolt (886158 → 701985); 2018–2022 rows contain Bed Bath & Beyond data instead of BBWI/L Brands |
| **COST** | 2018–2024 | All 7 years — SGA construction/restatement corrections across the board |
| **SHW** | 2018–2022 | 2018–2022: Operating Profit, SGA corrections; 2023–2024: no change |

### Mixed — some years have changes

| Ticker | Years with changes | What changed |
|--------|-------------------|--------------|
| **ACI** | 2024 | reportDate correction (2025-02-24 → 2025-02-22) |
| **AD.AS** | 2020 | Missing from Dolt and Yahoo — skipped |
| **AEO** | 2024 | reportDate correction (2025-02-03 → 2025-02-01) |
| **AMZN** | 2020 | Liabilities (101,408,000 → 227,791,000) |
| | 2021 | SGA (41,436,000 → 41,374,000) |
| | 2022 | SGA (55,392,000 → 54,129,000) |
| **ANF** | 2018 | SGA (484,863 → 2,021,079), Net Profit (78,808 → 74,541) |
| | 2019 | SGA (464,615 → 2,015,858), Net Profit (44,960 → 39,358) |
| | 2020 | SGA (463,843 → 1,843,791), Net Profit (108,954 → −103,887) |
| | 2021 | SGA (536,815 → 1,965,138), Net Profit (270,066 → 263,010) |
| | 2022 | SGA (517,602 → 2,014,560), Net Profit (10,385 → 2,816) |
| | 2024 | reportDate correction (2025-02-03 → 2025-02-01) |
| **ASO** | 2024 | reportDate correction (2025-02-03 → 2025-02-01) |
| **ASOMF** | 2022 | Operating Profit (33,400 → −9,800) |
| | 2024 | SGA (1,496,400 → 1,340,800) |
| **BBW** | 2018–2020 | Operating Profit — Dolt stores pre-tax income instead of operating profit |
| **BBY** | 2024 | reportDate correction (2025-02-03 → 2025-02-01) |
| **BJ** | 2020 | Operating Profit (652,201 → 642,392 — pre-opening costs) |
| **BOOT** | 2024 | reportDate correction (2025-03-31 → 2025-03-29) |
| **CHWY** | 2022 | WARNING: Dolt revenue/COGS differ from latest SEC filing |
| **CVS** | 2019 | UPDATE — Current Assets, Liabilities, Total SE are wrong |
| | 2022 | REVIEW — Net Profit discrepancy (restatement); other fields match |
| **DDS** | 2024 | ERROR — Net Revenue is 6,482,636 (net sales only); should include total revenue |
| **DG** | 2024 | WARNING — GM% slightly below 30% threshold; values confirmed correct |
| **DKS** | 2019 | UPDATE NEEDED — Dolt SGA is negative (−2,173,677) |
| | 2024 | Dolt reportDate is 2025-02-03 (minor error); values match SEC |
| **DLTR** | 2023 | UPDATE NEEDED — SGA in Dolt includes $1,069M goodwill impairment |
| **EBAY** | 2019 | ERROR — SGA 4,383K impossible (exceeds total OpEx 4,074K) |
| **FIVE** | 2021 | SGA (650,564 → 565,733) |
| | 2022 | SGA (750,448 → 644,831) |
| **FL** | 2021 | Net Revenue (8,958,000 → 8,968,000), Gross Margin |
| | 2022 | Net Profit (341,000 → 342,000) |
| **GAP** | 2024 | reportDate correction (2025-02-03 → 2025-02-01) |
| **HM-B.ST** | 2018 | SGA (7,882,000 → 95,394,000) |
| | 2019 | SGA (8,828,000 → 105,107,000) |
| | 2020 | Missing from Dolt; no Yahoo data available — skipped |
| **JWN** | 2019 | Net Revenue, Gross Margin — Dolt used Net Sales (15,132,000K) instead of total Revenue (15,524,000K) |
| **KR** | 2018 | COGS (−94,894,000 → 94,894,000), Gross Margin |
| | 2022 | Inventory (9,756,000 → 7,560,000) |
| | 2023 | Inventory (9,414,000 → 7,105,000) |
| | 2024 | SGA (NULL → 25,431,000) |
| **KSS** | 2019–2021 | ANOMALY — Income statement formula inconsistency (SEC verified) |
| **LEVI** | 2024 | Inventory (1,239,400 → 1,131,300) |
| **LOW** | 2024 | reportDate correction (2025-02-02 → 2025-01-31) |
| **M** | 2020 | COGS, Gross Margin — Dolt COGS slightly rounded |
| | 2022 | COGS, Gross Margin — Dolt COGS slightly rounded |
| | 2023 | COGS, SGA, Gross Margin, Operating Profit — FY2023 anomaly |
| | 2024 | Net Revenue — Dolt uses Contract Revenue ($22,294M) vs total Revenue |
| **MC.PA** | 2018 | CORRECTION — Balance sheet ×1000 (7 fields); SGA (3,466,000 → 21,616,000) |
| | 2019 | CORRECTION — Balance sheet ×1000 (7 fields); SGA (3,864,000 → 24,445,000) |
| | 2020 | Missing from Dolt; Yahoo FY2020 not in 4-year history — skip |
| **NKE** | 2018 | Correction: Operating Profit |
| | 2019 | **Correction: Operating Profit [ERROR]** — Dolt has 16,241,000 (equals Gross Margin); should be 3,115,000 |
| | 2020 | Correction: Operating Profit |
| | 2021 | Correction: Operating Profit (−24K diff) |
| | 2024 | Correction: reportDate (2024-05-31 → 2025-05-31) |
| **RAD** | 2020 | Net Profit (restated), Operating Profit |
| | 2021 | Net Profit (restated), Operating Profit |
| | 2022 | Operating Profit, Net Profit, Current Liabilities, Total SE, Liabilities |
| **REAL** | 2020 | SGA $196,575K → $195,465K (−$1,110K legal settlement reclassification) |
| | 2021 | SGA $239,167K → $238,995K (−$172K minor reclassification) |
| **RH** | 2018 | Correction: COGS, Gross Margin, SGA, Operating Profit, Net Profit |
| **SIG** | 2018 | Net Profit correction |
| | 2021 | Net Profit correction |
| **TGT** | 2022 | COGS, SGA (restatement) |
| | 2023 | COGS, SGA (restatement) |
| **TJX** | 2024 | Operating Profit correction |
| **TPR** | 2018 | SGA, Operating Profit correction |
| | 2024 | New insert (year not yet in Dolt) |
| **TSCO** | 2020 | Revenue $116,370K → $10,620,352K; Gross Margin massively wrong |
| | 2024 | reportDate correction (2024-12-31 → 2024-12-28) |
| **URBN** | 2019 | SGA −993,990K → +993,990K (sign flip) |
| **VSCO** | 2020 | reportDate correction (2021-01-31 → 2021-01-30) |
| | 2023 | NetInc $116,000K → $109,000K (wrong line item) |
| | 2024 | TSE $664,000K → $640,000K; Liabilities $3,868,000K → $3,892,000K |
| **W** | 2024 | SGA 4,035,000K → 1,977,000K |
| **WBA** | 2022 | NetProfit $4,065,000K → $4,337,000K (wrong line item) |
| | 2023 | NetProfit −$3,528,000K → −$3,080,000K (wrong line item) |
| | 2024 | Liabilities $68,992,000K → $69,032,000K (balance sheet identity) |
| **WMT** | 2018 | TSE $79,634K → $72,496K; Liabilities $139,661K → $146,799K |
| | 2019 | Revenue $519,926K → $523,964K; Gross $125,321K → $125,096K |
| | 2024 | TSE $97,421K → $91,013K; Liabilities $163,402K → $169,810K |
| **WSM** | 2018 | SGA −1,665,060K → +1,665,060K (sign error) |
| | 2024 | reportDate correction (2025-01-28 → 2025-02-02) |

---

## Quick Stats

| Category | Count |
|----------|-------|
| Total companies analyzed | **59** |
| No changes (2018–2024) | **11** |
| At least one change needed | **48** |
| Only reportDate fix (minor) | **11** (ACI, AEO, ASO, BBY, BOOT, GAP, LOW, plus minor reportDate in ANF, DKS, NKE, TSCO, WSM) |
| Significant data corrections | **37** |
