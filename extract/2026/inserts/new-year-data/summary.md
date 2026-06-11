# /download-new-year-data — Run Summary
**Generated:** 2026-06-11  
**Skill:** `/download-new-year-data`  
**Database:** calvinw/BusMgmtBenchmarks/main

---

## Results by Status

### SQL Files Generated (32 companies)

| Company | Ticker | File | DB Year Added | Notes |
|---------|--------|------|---------------|-------|
| ASOS | ASOMF | new_year_ASOMF_2026-06-07.sql | 2025 | |
| Abercrombie & Fitch | ANF | new_year_ANF_2026-06-07.sql | 2025 | |
| Academy Sports | ASO | new_year_ASO_2026-06-07.sql | 2025 | |
| Adidas | ADS.DE | new_year_ADS.DE_2026-06-07.sql | 2025 | |
| Ahold Delhaize | AD.AS | new_year_AD.AS_2026-06-07.sql | 2025 | |
| Albertsons | ACI | new_year_ACI_2026-06-07.sql | 2025 | |
| Amazon | AMZN | new_year_AMZN_2026-06-07.sql | 2025 | |
| American Eagle | AEO | new_year_AEO_2026-06-07.sql | 2025 | |
| Aritzia | ATZ.TO | new_year_ATZ.TO_2026-06-07.sql | 2025 | |
| Bath & Body Works | BBWI | new_year_BBWI_2026-06-07.sql | 2024 | FY ends late Jan; reportDate 2025-01-31 |
| BJ's | BJ | new_year_BJ_2026-06-07.sql | 2025 | |
| CVS | CVS | new_year_CVS_2026-06-11.sql | 2025 | |
| Dollar General | DG | new_year_DG_2026-06-11.sql | 2025 | |
| Etsy | ETSY | new_year_ETSY_2026-06-11.sql | 2025 | |
| Five Below | FIVE | new_year_FIVE_2026-06-11.sql | 2025 | |
| Gap | GAP | new_year_GAP_2026-06-11.sql | 2025 | |
| H&M | HM-B.ST | new_year_HM-B.ST_2026-06-11.sql | 2025 | |
| Home Depot | HD | new_year_HD_2026-06-11.sql | 2025 | |
| Inditex/Zara | ITX.MC | new_year_ITX.MC_2026-06-11.sql | 2025 | |
| Kohl's | KSS | new_year_KSS_2026-06-11.sql | 2025 | |
| Kroger | KR | new_year_KR_2026-06-11.sql | 2025 | |
| Louis Vuitton | MC.PA | new_year_MC.PA_2026-06-11.sql | 2025 | |
| Lowe's | LOW | new_year_LOW_2026-06-11.sql | 2025 | |
| Lululemon | LULU | new_year_LULU_2026-06-11.sql | 2025 | |
| Macy's | M | new_year_M_2026-06-11.sql | 2025 | |
| RH | RH | new_year_RH_2026-06-11.sql | 2025 | |
| Ross | ROST | new_year_ROST_2026-06-11.sql | 2025 | |
| Sherwin-Williams | SHW | new_year_SHW_2026-06-11.sql | 2025 | ⚠️ FY2024 op profit was wrong in DB — see Data Quality Issues section |
| Signet Jewelers | SIG | new_year_SIG_2026-06-11.sql | 2025 | |
| Tapestry | TPR | new_year_TPR_2026-06-11.sql | 2024 | ⚠️ Op Profit drop (~$854M Kate Spade impairment); Total Assets halved (repaid Capri acquisition debt after FTC block) |
| Target | TGT | new_year_TGT_2026-06-11.sql | 2025 | |
| TJ Maxx | TJX | new_year_TJX_2026-06-11.sql | 2025 | |

---

### Up to Date — No New Data (22 companies)

These companies were checked and their most recently filed fiscal year is already in the database.

**Breakdown by group:**
- **Jessie** — 10 of 12 companies up to date; only CVS and DG had new data to insert.
- **Souyen** — 10 of 11 companies up to date; entire group was current (WBA went private).
- **Diana** — 1 of 12 up to date (LEVI only); all other Diana companies had new SQL files generated.
- **Elena** — 1 of 12 up to date (NKE only); rest had new SQL files or went private (JWN, RAD).

| Company | Ticker | Group | Latest DB Year | Notes |
|---------|--------|-------|---------------|-------|
| Best Buy | BBY | Jessie | 2025 | FY ends late Jan. DB year 2025 (reportDate 2026-01-31) current. |
| Boot Barn | BOOT | Jessie | 2025 | FY ends late Mar. DB year 2025 (reportDate 2026-03-28) current. |
| Build-A-Bear | BBW | Jessie | 2025 | FY ends late Jan. DB year 2025 (reportDate 2026-01-31) current. |
| Burlington | BURL | Jessie | 2025 | FY ends late Jan. DB year 2025 (reportDate 2026-01-31) current. |
| Capri Holdings | CPRI | Jessie | 2025 | FY ends late Mar. DB year 2025 (reportDate 2026-03-28) current. |
| Chewy | CHWY | Jessie | 2025 | FY ends early Feb. DB year 2025 (reportDate 2026-02-01) current. |
| Costco | COST | Jessie | 2025 | FY ends Aug 31. DB year 2025 (reportDate 2025-08-31) current. FY2026 closes ~Aug 2026. |
| Dick's Sporting Goods | DKS | Jessie | 2025 | FY ends late Jan. DB year 2025 (reportDate 2026-01-31) current. |
| Dillard's | DDS | Jessie | 2025 | FY ends late Jan. DB year 2025 (reportDate 2026-01-31) current. |
| Dollar Tree | DLTR | Jessie | 2025 | FY ends late Jan. DB year 2025 (reportDate 2026-01-31) current. |
| eBay | EBAY | Souyen | 2025 | FY ends Dec 31. DB year 2025 current. |
| Levi Strauss | LEVI | Diana | 2025 | FY ends Nov 30. DB year 2025 (reportDate 2025-11-30) current. |
| Nike | NKE | Elena | 2024 | FY ends May 31. FY2025 (ending 2025-05-31) is in DB as year 2024. Next filing ~Aug 2026. |
| The RealReal | REAL | Souyen | 2025 | FY ends Dec 31. DB year 2025 current. |
| Tractor Supply | TSCO | Souyen | 2025 | FY ends Dec 31. DB year 2025 current. |
| Ulta Beauty | ULTA | Souyen | 2025 | FY ends late Jan. DB year 2025 (reportDate 2026-01-31) current. |
| Urban Outfitters | URBN | Souyen | 2025 | FY ends late Jan. DB year 2025 (reportDate 2026-01-31) current. |
| Victoria's Secret | VSCO | Souyen | 2025 | FY ends early Feb. DB year 2025 (reportDate 2026-01-31) current. |
| Walmart | WMT | Souyen | 2025 | FY ends late Jan. DB year 2025 (reportDate 2026-01-31) current. |
| Wayfair | W | Souyen | 2025 | FY ends Dec 31. DB year 2025 current. |
| Williams-Sonoma | WSM | Souyen | 2025 | FY ends early Feb. DB year 2025 (reportDate 2026-02-01) current. |
| YETI Holdings | YETI | Souyen | 2025 | FY ends Dec 31. DB year 2025 current. |

---

### Went Private or Bankrupt — No Future Public Filings (4 companies)

| Company | Ticker | Last DB Year | Notes |
|---------|--------|-------------|-------|
| Nordstrom | JWN | 2024 | Nordstrom family completed leveraged buyout, delisted March 2025. Last 10-K: FY ending 2025-02-01 (DB year 2024). No future public filings. |
| Rite Aid | RAD | 2022 | Filed Chapter 11 bankruptcy Oct 2023. Emerged as private company Sept 2024, delisted from NYSE. Last 10-K: FY ending 2023-03-04 (DB year 2022). No future public filings. |
| Walgreens | WBA | 2024 | Sycamore Partners acquisition closed March 2025. Delisted. FY2025 (ending Aug 2025) had no public 10-K filed. No future public filings expected. |
| Foot Locker | FL | 2024 | Merged with DICK'S Sporting Goods, delisted from NYSE September 8, 2025. Filed Form 15 Sept 18, 2025 — all SEC reporting terminated. Last public data: FY ending 2025-02-01 (DB year 2024). No FY2025 10-K will ever be filed. |

---

### Special Case — Manual Intervention Required (1 company)

| Company | Ticker | Status | Notes |
|---------|--------|--------|-------|
| Alibaba | BABA | Needs manual USD/CNY conversion | SEC tool does not work (files 20-F, not 10-K). Yahoo Finance returns RMB values. DB stores USD. FY2025 (ending 2026-03-31) data is available on Yahoo but requires dividing by the March 31, 2026 USD/CNY spot rate. See `alibaba-new-data-notes-by-catie.md` for full methodology and the raw RMB values. |

---

### Data Quality Issues Found

| Company | Ticker | Issue | Details |
|---------|--------|-------|---------|
| Sherwin-Williams | SHW | ⚠️ FY2024 Operating Profit wrong in DB | DB has 3,451,800K (which is actually the Pretax Income figure). Correct Operating Profit = Gross Profit (11,195,100) − SGA (7,422,100) − Other operating expense (38,800) = **3,734,200K**. Difference: 282,400K. The FY2025 SQL file (new_year_SHW_2026-06-11.sql) uses the correct methodology, but FY2024 in the DB needs a separate correction. |

---


## Summary Counts

| Status | Count |
|--------|-------|
| SQL file generated | 32 |
| Up to date (no new data) | 22 |
| Went private / bankrupt / acquired | 4 |
| Special case (manual — Alibaba) | 1 |
| **Total** | **59** |
