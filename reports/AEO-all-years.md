# American Eagle (AEO) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-05-29
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2018 | 2019-02-02 | No change — no alternate source to verify |
| 2019 | 2020-02-01 | No change — no alternate source to verify |
| 2020 | 2021-01-30 | No change — no alternate source to verify |
| 2021 | 2022-01-29 | No change — no alternate source to verify |
| 2022 | 2023-01-28 | No change — Yahoo values match within rounding |
| 2023 | 2024-02-03 | No change — Yahoo values match within rounding |
| 2024 | 2025-02-03 | No change — Yahoo values match within rounding |
| 2025 | 2026-01-31 | **New insert** |

---

## Company Metadata

- **Company name (DB):** American Eagle
- **Display name:** American Eagle
- **Ticker:** AEO
- **CIK:** 919012
- **Segment:** Specialty — Apparel
- **Fiscal year end:** Late January / early February
- **SEC available:** Yes (CIK present), but SEC MCP unavailable this session — Yahoo Finance + Dolt only
- **Operating Profit convention:** "Total Operating Income As Reported" (confirmed from Dolt years 2022–2024)
- **TSE convention:** Total Equity Gross Minority Interest (confirmed from Dolt year 2024 = 1,766,860K)

---

## Anomaly Rules Applied

- **Rule 3 (Yahoo SGA = Total OpEx):** Not triggered. Yahoo SGA (~$1.49B for FY2025) << Total Expenses (~$5.22B). Yahoo SGA is safe to use.
- **Rule 1 (SGA + Marketing):** No separate Marketing line visible in Yahoo data for AEO. Yahoo "Selling General And Administration" is the single combined SGA line. Use directly.
- **Rule 4 (Sum G&A + Selling):** Not needed — Yahoo provides a single combined SGA line.
- **D&A exclusion:** Yahoo Operating Expense (2026-01-31) = $1,697,500K = SGA $1,485,540K + D&A $211,961K. SGA line correctly excludes D&A. ✓
- **Gross margin benchmark:** Specialty apparel expected 35–55%. All years within range (see per-year tables).
- **Inventory:** AEO is a traditional apparel retailer. Inventory expected. All years have inventory values. ✓
- **Balance sheet identity:** Verified for all Dolt years (2018–2024) and new FY2025 data. ✓

---

## Years 2018–2021: Existing Dolt Data (No Alternate Source)

Yahoo Finance does not provide data for these years. No correction is possible without external data.

[WARNING] SGA for years 2018–2021 cannot be verified against Yahoo Finance. Per recurring project convention, companies with data older than ~2021 may have incomplete SGA (G&A only). Recommend review against SEC filings if precision is needed. Do not correct without external data.

### Year 2018

| Field | Dolt (current) | Yahoo | Recommended |
|-------|---------------|-------|-------------|
| reportDate | 2019-02-02 | N/A | 2019-02-02 |
| Net Revenue | 4,035,720 | N/A | 4,035,720 |
| Cost of Goods | 2,548,082 | N/A | 2,548,082 |
| Gross Margin | 1,487,638 | N/A | 1,487,638 |
| Gross Margin % | 36.9% | N/A | — |
| SGA | 980,610 | N/A | 980,610 [WARNING: unverified] |
| Operating Profit | 337,129 | N/A | 337,129 |
| Net Profit | 261,902 | N/A | 261,902 |
| Inventory | 424,404 | N/A | 424,404 |
| Current Assets | 1,046,253 | N/A | 1,046,253 |
| Total Assets | 1,903,378 | N/A | 1,903,378 |
| Current Liabilities | 542,645 | N/A | 542,645 |
| Liabilities | 615,823 | N/A | 615,823 |
| TSE | 1,287,555 | N/A | 1,287,555 |
| Total L+E | 1,903,378 | N/A | 1,903,378 |

Balance sheet identity: 615,823 + 1,287,555 = 1,903,378 = Total Assets ✓

**Action: No change.**

---

### Year 2019

| Field | Dolt (current) | Yahoo | Recommended |
|-------|---------------|-------|-------------|
| reportDate | 2020-02-01 | N/A | 2020-02-01 |
| Net Revenue | 4,308,212 | N/A | 4,308,212 |
| Cost of Goods | 2,785,911 | N/A | 2,785,911 |
| Gross Margin | 1,522,301 | N/A | 1,522,301 |
| Gross Margin % | 35.3% | N/A | — |
| SGA | 1,029,412 | N/A | 1,029,412 [WARNING: unverified] |
| Operating Profit | 233,345 | N/A | 233,345 |
| Net Profit | 191,257 | N/A | 191,257 |
| Inventory | 446,278 | N/A | 446,278 |
| Current Assets | 1,047,930 | N/A | 1,047,930 |
| Total Assets | 3,328,679 | N/A | 3,328,679 |
| Current Liabilities | 751,756 | N/A | 751,756 |
| Liabilities | 2,080,826 | N/A | 2,080,826 |
| TSE | 1,247,853 | N/A | 1,247,853 |
| Total L+E | 3,328,679 | N/A | 3,328,679 |

Balance sheet identity: 2,080,826 + 1,247,853 = 3,328,679 = Total Assets ✓

Note: Large jump in Total Assets and Liabilities from 2018 to 2019 reflects ASC 842 lease accounting adoption (right-of-use assets and lease liabilities added to balance sheet).

**Action: No change.**

---

### Year 2020

| Field | Dolt (current) | Yahoo | Recommended |
|-------|---------------|-------|-------------|
| reportDate | 2021-01-30 | N/A | 2021-01-30 |
| Net Revenue | 3,759,113 | N/A | 3,759,113 |
| Cost of Goods | 2,610,966 | N/A | 2,610,966 |
| Gross Margin | 1,148,147 | N/A | 1,148,147 |
| Gross Margin % | 30.5% | N/A | — |
| SGA | 977,264 | N/A | 977,264 [WARNING: unverified] |
| Operating Profit | -271,345 | N/A | -271,345 |
| Net Profit | -209,274 | N/A | -209,274 |
| Inventory | 405,445 | N/A | 405,445 |
| Current Assets | 1,522,643 | N/A | 1,522,643 |
| Total Assets | 3,434,806 | N/A | 3,434,806 |
| Current Liabilities | 858,482 | N/A | 858,482 |
| Liabilities | 2,348,141 | N/A | 2,348,141 |
| TSE | 1,086,665 | N/A | 1,086,665 |
| Total L+E | 3,434,806 | N/A | 3,434,806 |

Balance sheet identity: 2,348,141 + 1,086,665 = 3,434,806 = Total Assets ✓

Note: Negative Operating Profit and Net Profit reflect COVID-19 impact on FY2020.

[WARNING] Gross margin % of 30.5% is slightly below specialty apparel range (35–55%). This is attributable to COVID-19 disruptions in FY2020 (ended Jan 30, 2021) — expected anomaly. Not an error.

**Action: No change.**

---

### Year 2021

| Field | Dolt (current) | Yahoo | Recommended |
|-------|---------------|-------|-------------|
| reportDate | 2022-01-29 | N/A | 2022-01-29 |
| Net Revenue | 5,010,785 | N/A | 5,010,785 |
| Cost of Goods | 3,018,995 | N/A | 3,018,995 |
| Gross Margin | 1,991,790 | N/A | 1,991,790 |
| Gross Margin % | 39.7% | N/A | — |
| SGA | 1,222,000 | N/A | 1,222,000 [WARNING: unverified] |
| Operating Profit | 591,065 | N/A | 591,065 |
| Net Profit | 419,629 | N/A | 419,629 |
| Inventory | 553,458 | N/A | 553,458 |
| Current Assets | 1,396,924 | N/A | 1,396,924 |
| Total Assets | 3,786,643 | N/A | 3,786,643 |
| Current Liabilities | 842,871 | N/A | 842,871 |
| Liabilities | 2,362,971 | N/A | 2,362,971 |
| TSE | 1,423,672 | N/A | 1,423,672 |
| Total L+E | 3,786,643 | N/A | 3,786,643 |

Balance sheet identity: 2,362,971 + 1,423,672 = 3,786,643 = Total Assets ✓

**Action: No change.**

---

## Years 2022–2024: Yahoo vs Dolt Comparison

Yahoo fiscal year dates map to Dolt years as follows:
- Yahoo 2023-01-31 → Dolt year 2022 (reportDate 2023-01-28)
- Yahoo 2024-01-31 → Dolt year 2023 (reportDate 2024-02-03)
- Yahoo 2025-01-31 → Dolt year 2024 (reportDate 2025-02-03)

Operating Profit confirmation: Dolt uses Yahoo "Total Operating Income As Reported" (not the clean "Operating Income"). Confirmed against all three years — differences match Special Income Charges line.

### Year 2022

| Field | Yahoo (2023-01-31) | Dolt (current) | Recommended |
|-------|-------------------|---------------|-------------|
| reportDate | 2023-01-31 | 2023-01-28 | 2023-01-28 (keep Dolt) |
| Net Revenue | 4,989,830 | 4,989,833 | 4,989,833 |
| Cost of Goods | 3,244,580 | 3,244,585 | 3,244,585 |
| Gross Margin | 1,745,250 | 1,745,248 | 1,745,248 |
| Gross Margin % | 35.0% | 35.0% | — |
| SGA | 1,269,100 | 1,269,095 | 1,269,095 |
| Operating Profit (As Reported) | 247,047 | 247,047 | 247,047 |
| Net Profit | 125,136 | 125,136 | 125,136 |
| Inventory | 585,083 | 585,083 | 585,083 |
| Current Assets | 1,100,240 | 1,100,241 | 1,100,241 |
| Total Assets | 3,420,960 | 3,420,956 | 3,420,956 |
| Current Liabilities | 768,948 | 768,948 | 768,948 |
| Liabilities | 1,821,790 | 1,821,793 | 1,821,793 |
| TSE | 1,599,160 | 1,599,163 | 1,599,163 |
| Total L+E | 3,420,960 | 3,420,956 | 3,420,956 |

All differences ≤ 5K (rounding only). Gross margin 35.0% is at the low end but within specialty apparel range.

Balance sheet identity: 1,821,793 + 1,599,163 = 3,420,956 ✓

**Action: No change.**

---

### Year 2023

| Field | Yahoo (2024-01-31) | Dolt (current) | Recommended |
|-------|-------------------|---------------|-------------|
| reportDate | 2024-01-31 | 2024-02-03 | 2024-02-03 (keep Dolt) |
| Net Revenue | 5,261,770 | 5,261,770 | 5,261,770 |
| Cost of Goods | 3,237,190 | 3,237,192 | 3,237,192 |
| Gross Margin | 2,024,580 | 2,024,578 | 2,024,578 |
| Gross Margin % | 38.5% | 38.5% | — |
| SGA | 1,433,300 | 1,433,300 | 1,433,300 |
| Operating Profit (As Reported) | 222,717 | 222,717 | 222,717 |
| Net Profit | 170,038 | 170,038 | 170,038 |
| Inventory | 640,662 | 640,662 | 640,662 |
| Current Assets | 1,433,350 | 1,433,350 | 1,433,350 |
| Total Assets | 3,557,910 | 3,557,909 | 3,557,909 |
| Current Liabilities | 891,172 | 891,172 | 891,172 |
| Liabilities | 1,821,150 | 1,821,150 | 1,821,150 |
| TSE | 1,736,760 | 1,736,759 | 1,736,759 |
| Total L+E | 3,557,910 | 3,557,909 | 3,557,909 |

All differences ≤ 2K (rounding only).

Balance sheet identity: 1,821,150 + 1,736,759 = 3,557,909 ✓

**Action: No change.**

---

### Year 2024

| Field | Yahoo (2025-01-31) | Dolt (current) | Recommended |
|-------|-------------------|---------------|-------------|
| reportDate | 2025-01-31 | 2025-02-03 | 2025-02-03 (keep Dolt) |
| Net Revenue | 5,328,650 | 5,328,650 | 5,328,650 |
| Cost of Goods | 3,239,720 | 3,239,720 | 3,239,720 |
| Gross Margin | 2,088,930 | 2,088,930 | 2,088,930 |
| Gross Margin % | 39.2% | 39.2% | — |
| SGA | 1,431,810 | 1,431,810 | 1,431,810 |
| Operating Profit (As Reported) | 427,303 | 427,303 | 427,303 |
| Net Profit | 329,380 | 329,380 | 329,380 |
| Inventory | 636,655 | 636,655 | 636,655 |
| Current Assets | 1,354,230 | 1,354,231 | 1,354,231 |
| Total Assets | 3,830,780 | 3,830,775 | 3,830,775 |
| Current Liabilities | 882,656 | 882,656 | 882,656 |
| Liabilities | 2,063,920 | 2,063,915 | 2,063,915 |
| TSE (Total Equity Gross Minority Interest) | 1,766,860 | 1,766,860 | 1,766,860 |
| Total L+E | 3,830,780 | 3,830,775 | 3,830,775 |

All differences ≤ 5K (rounding only). TSE confirmed using Total Equity Gross Minority Interest = 1,766,860K.

Balance sheet identity: 2,063,915 + 1,766,860 = 3,830,775 ✓

**Action: No change.**

---

## Year 2025: New Insert (Yahoo 2026-01-31)

This year is not yet in the Dolt database.

### Source Data

Yahoo Finance (column: 2026-01-31):

**Income Statement:**
| Item | Yahoo Raw | Value ($K) |
|------|-----------|-----------|
| Total Revenue | 5.54724e+09 | 5,547,240 |
| Cost Of Revenue | 3.52192e+09 | 3,521,920 |
| Gross Profit | 2.02532e+09 | 2,025,320 |
| Selling General And Administration | 1.48554e+09 | 1,485,540 |
| Operating Income (clean) | 3.27825e+08 | 327,825 |
| Total Operating Income As Reported | 2.26222e+08 | 226,222 |
| Net Income Common Stockholders | 1.91983e+08 | 191,983 |
| Special Income Charges | -1.01603e+08 | -101,603 |

Note: 327,825 − 101,603 = 226,222 ✓ (As Reported = clean − special charges)

**Balance Sheet:**
| Item | Yahoo Raw | Value ($K) |
|------|-----------|-----------|
| Inventory | 7.01966e+08 | 701,966 |
| Current Assets | 1.31417e+09 | 1,314,170 |
| Total Assets | 4.00968e+09 | 4,009,680 |
| Current Liabilities | 8.67563e+08 | 867,563 |
| Common Stock Equity | 1.69315e+09 | 1,693,150 |
| Total Equity Gross Minority Interest | 1.69143e+09 | 1,691,430 |
| Minority Interest | -1.719e+06 | -1,719 |
| Total Liabilities Net Minority Interest | 2.31825e+09 | 2,318,250 |

### Anomaly Checks

- **Gross margin:** 2,025,320 / 5,547,240 = **36.5%** — within specialty apparel range (35–55%) ✓
- **SGA rule 3:** Yahoo SGA 1,485,540K << Total Expenses 5,219,410K — no inflation ✓
- **D&A excluded from SGA:** Yahoo OpEx = SGA + D&A (1,485,540 + 211,961 = 1,697,501 ≈ 1,697,500) ✓
- **Operating Profit:** Using "Total Operating Income As Reported" (226,222K) — consistent with AEO Dolt convention ✓
- **TSE:** Using Total Equity Gross Minority Interest (1,691,430K) — consistent with AEO Dolt convention (minority interest is −1,719K this year, making total equity slightly below common stock equity) ✓
- **Balance sheet identity:** 2,318,250 + 1,691,430 = 4,009,680 = Total Assets ✓
- **Inventory:** 701,966K — positive, expected for apparel retailer ✓

### Reconciled Values for FY2025

| Field | Recommended Value | Source | Notes |
|-------|------------------|--------|-------|
| reportDate | 2026-01-31 | Yahoo column header | Actual may vary slightly; use as reported |
| Net Revenue | 5,547,240 | Yahoo | |
| Cost of Goods | 3,521,920 | Yahoo | |
| Gross Margin | 2,025,320 | Calculated | Revenue − COGS |
| SGA | 1,485,540 | Yahoo | Combined SGA line; D&A excluded ✓ |
| Operating Profit | 226,222 | Yahoo "As Reported" | AEO convention; clean figure would be 327,825 |
| Net Profit | 191,983 | Yahoo | |
| Inventory | 701,966 | Yahoo | |
| Current Assets | 1,314,170 | Yahoo | |
| Total Assets | 4,009,680 | Yahoo | |
| Current Liabilities | 867,563 | Yahoo | |
| Liabilities | 2,318,250 | Calculated | Total Assets − TSE |
| TSE | 1,691,430 | Yahoo (Total Equity Gross Minority Interest) | Consistent with AEO convention |
| Total L+E | 4,009,680 | Yahoo | |

**Action: New insert.**

---

## Flags Summary

| Year | Flag | Severity | Description |
|------|------|----------|-------------|
| 2018 | SGA unverified | [WARNING] | No Yahoo data for this year; SGA may be incomplete (G&A only per recurring convention) |
| 2019 | SGA unverified | [WARNING] | No Yahoo data for this year; SGA may be incomplete |
| 2020 | SGA unverified | [WARNING] | No Yahoo data for this year; SGA may be incomplete |
| 2020 | Gross margin 30.5% | [WARNING] | Below specialty apparel range — attributable to COVID-19 impact; expected anomaly |
| 2021 | SGA unverified | [WARNING] | No Yahoo data for this year; SGA may be incomplete |
| 2025 | Operating Profit (As Reported) | [INFO] | Uses "Total Operating Income As Reported" (226,222K); clean Operating Income is 327,825K; consistent with AEO convention |

No [ERROR] flags. All unresolved flags are [WARNING] only.

---

**Analysis complete.** Run `/insert-financials AEO` to write all changed years to the database.

Only FY2025 requires a new insert. Years 2018–2024 have no changes.
