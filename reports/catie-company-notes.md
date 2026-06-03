# Catie's Company Notes — Unresolved Issues
**Last updated:** 2026-06-03

All SQL files are ready to apply. The items below are problems that **cannot be fixed** with the current tools.

---

## BBWI — Bath & Body Works

**FY2018–2020 are L Brands combined, not B&BW standalone**
- Revenue ($11.8–13.2B) includes Victoria's Secret and is not comparable to BBWI standalone ($7.9B in FY2021+). Cannot extract B&BW-only segment data with current tools.

**FY2021 Net Profit includes $258M VS spinoff gain**
- Total Net Profit = 1,333,000K. Ongoing operations only = 1,075,000K.

---

## BABA — Alibaba

**No SEC verification for any year**
- Files 20-F not 10-K. SEC MCP only fetches 10-K. Zero SEC cross-check.

**FY2018–2021 income statements unverified**
- Outside Yahoo 5-year window. No external source for those years.

**FY2025 Operating Profit — 64% decline unconfirmed**
- Op Profit = 6,908K USD, down 64% from FY2024. Cannot verify without 20-F.

**RMB/USD exchange rates are approximate**
- All values converted from estimated annual average rates.

---

## ADS.DE — Adidas

**FY2018–2019 SGA likely incomplete**
- Outside Yahoo 5-year window. SGA may be G&A only, missing full selling expense (~9–10B EUR).

**FY2020–2021 unverifiable**
- No external source available.

---

## AD.AS — Ahold Delhaize

**FY2020 missing from DB entirely**
- No data in Dolt or Yahoo for this year. Gap in the time series.

**FY2018–2019 SGA likely incomplete**
- Outside Yahoo 5-year window. SGA may be G&A only.

**FY2021 unverifiable**
- Yahoo returns NaN for FY2021.

---

## ANF — Abercrombie & Fitch

**FY2018 balance sheet pre-ASC 842 discontinuity**
- FY2018 has no ROU lease assets. FY2019 adopted ASC 842, adding ~$1.17B. The two years are on different accounting bases — not an error, but Total Assets is not directly comparable across FY2018/2019.

---

## AEO — American Eagle

**FY2018/2019 accounting discontinuity**
- FY2018 is pre-ASC 842 ($1.9B total assets). FY2019 adopted ASC 842 ($3.3B total assets). The jump is correct accounting, not a data error.

---

## ACI — Albertsons

**FY2018 balance sheet unverified**
- SGA corrected in SQL. Balance sheet not cross-checked against SEC (identity passes).

---

## ATZ.TO — Aritzia

**FY2018–2021 SGA unverifiable**
- Canadian company, no SEC filings, outside Yahoo 5-year window. SGA may be incomplete.

**FY2023 Current Liabilities discrepancy**
- Yahoo shows 411,627K vs Dolt 403,432K (~8.2M gap). Total liabilities agree — current/non-current split differs. Cannot resolve without SEDAR filing.

---

## ASOMF — ASOS

**FY2019–2021 unverifiable**
- UK company, no SEC filings, outside Yahoo 5-year window. No external cross-check possible.

---

## AMZN — Amazon

**FY2021 balance sheet unverified**
- Income statement confirmed by SEC. Balance sheet identity passes but not independently verified.

---

## BJ — BJ's Wholesale Club

**FY2020 balance sheet unverified**
- Income statement corrected from SEC. Balance sheet identity passes but not independently verified. (Low priority — all other years confirmed.)
