# BJ's (BJ) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-05-29
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2018 | 2019-02-02 | No change — no alternate source to verify |
| 2019 | 2020-02-01 | No change — no alternate source to verify |
| 2020 | 2021-01-31 | No change — no alternate source to verify |
| 2021 | 2022-01-29 | No change — no alternate source to verify |
| 2022 | 2023-01-28 | No change — Yahoo values match within rounding |
| 2023 | 2024-02-03 | No change — Yahoo values match within rounding |
| 2024 | 2025-02-01 | No change — Yahoo values match within rounding |
| 2025 | 2026-01-31 | **New insert** |

---

## Company Metadata

- **Company name (DB):** BJ's
- **Display name:** BJ's
- **Ticker:** BJ
- **CIK:** 1531152
- **Segment:** Warehouse Club
- **Fiscal year end:** Late January
- **SEC available:** Yes (CIK present), but SEC MCP unavailable this session — Yahoo Finance + Dolt only
- **Operating Profit convention:** "Total Operating Income As Reported" (confirmed from Dolt years 2022–2024 matching Yahoo exactly)
- **TSE convention:** Common Stock Equity = Total Equity Gross Minority Interest (no minority interest)

---

## Anomaly Rules Applied

- **Rule 3 (Yahoo SGA = Total OpEx):** Not triggered. Yahoo Total Expenses (~$20.6B for FY2025) >> SGA (~$3.15B). SGA is safe to use.
- **Rule 1 (SGA + Marketing):** No separate Marketing line in Yahoo for BJ's. Single combined SGA/Operating Expense line. Use directly.
- **Rule 4:** Not needed — combined SGA line present.
- **SGA structure:** Yahoo "Selling General And Administration" = "Operating Expense" for BJ's — a single combined line covering all selling/general/admin costs including D&A. Gross Profit − SGA ≈ Operating Income (clean) for all years, confirming the structure. Consistent with all existing Dolt years 2022–2024.
- **Gross margin benchmark:** Warehouse clubs expected 10–15%. BJ's runs 17.8–18.6% across all years in DB. [WARNING] flagged but this is a consistent known pattern for BJ's — membership revenue included in Net Revenue, different product mix from Costco.
- **Negative TSE (2018–2019):** BJ's had negative equity in 2018–2019 following its 2017 LBO. Valid — see flags.
- **Inventory:** BJ's is a warehouse club retailer. Large positive inventory expected. All years show large inventory values. ✓
- **Balance sheet identity:** Verified for all Dolt years (2018–2024) and new FY2025 data. ✓
- **Operating Profit:** Dolt uses "Total Operating Income As Reported" for all verified years. FY2025 value = 816,604K.

---

## Years 2018–2021: Existing Dolt Data (No Alternate Source)

Yahoo Finance does not provide data for these years. No correction is possible without external data.

[WARNING] SGA for years 2018–2021 cannot be verified against Yahoo Finance. Per recurring project convention, companies with data older than ~2021 may have incomplete SGA (G&A only). Do not correct without external data.

### Year 2018

| Field | Dolt (current) | Yahoo | Recommended |
|-------|---------------|-------|-------------|
| reportDate | 2019-02-02 | N/A | 2019-02-02 |
| Net Revenue | 13,007,347 | N/A | 13,007,347 |
| Cost of Goods | 10,646,452 | N/A | 10,646,452 |
| Gross Margin | 2,360,895 | N/A | 2,360,895 |
| Gross Margin % | 18.2% | N/A | — |
| SGA | 2,051,324 | N/A | 2,051,324 [WARNING: unverified] |
| Operating Profit | 303,453 | N/A | 303,453 |
| Net Profit | 127,261 | N/A | 127,261 |
| Inventory | 1,052,306 | N/A | 1,052,306 |
| Current Assets | 1,337,206 | N/A | 1,337,206 |
| Total Assets | 3,239,285 | N/A | 3,239,285 |
| Current Liabilities | 1,577,688 | N/A | 1,577,688 |
| Liabilities | 3,441,369 | N/A | 3,441,369 |
| TSE | -202,084 | N/A | -202,084 |
| Total L+E | 3,239,285 | N/A | 3,239,285 |

Balance sheet identity: 3,441,369 + (−202,084) = 3,239,285 = Total Assets ✓

[WARNING] TSE = −202,084K (negative equity). Valid — BJ's was taken private in a 2017 LBO and carried significant debt. TSE became positive in FY2020.

**Action: No change.**

---

### Year 2019

| Field | Dolt (current) | Yahoo | Recommended |
|-------|---------------|-------|-------------|
| reportDate | 2020-02-01 | N/A | 2020-02-01 |
| Net Revenue | 13,190,707 | N/A | 13,190,707 |
| Cost of Goods | 10,763,926 | N/A | 10,763,926 |
| Gross Margin | 2,426,781 | N/A | 2,426,781 |
| Gross Margin % | 18.4% | N/A | — |
| SGA | 2,059,430 | N/A | 2,059,430 [WARNING: unverified] |
| Operating Profit | 352,199 | N/A | 352,199 |
| Net Profit | 187,176 | N/A | 187,176 |
| Inventory | 1,081,502 | N/A | 1,081,502 |
| Current Assets | 1,360,020 | N/A | 1,360,020 |
| Total Assets | 5,269,780 | N/A | 5,269,780 |
| Current Liabilities | 1,801,416 | N/A | 1,801,416 |
| Liabilities | 5,324,124 | N/A | 5,324,124 |
| TSE | -54,344 | N/A | -54,344 |
| Total L+E | 5,269,780 | N/A | 5,269,780 |

Balance sheet identity: 5,324,124 + (−54,344) = 5,269,780 = Total Assets ✓

[WARNING] TSE = −54,344K (negative equity). Valid — final year of LBO-era negative equity; TSE turned positive in FY2020.

Note: Large jump in Total Assets from 2018 to 2019 reflects FASB ASC 842 adoption (lease assets and liabilities added to balance sheet).

**Action: No change.**

---

### Year 2020

| Field | Dolt (current) | Yahoo | Recommended |
|-------|---------------|-------|-------------|
| reportDate | 2021-01-31 | N/A | 2021-01-31 |
| Net Revenue | 15,430,017 | N/A | 15,430,017 |
| Cost of Goods | 12,451,061 | N/A | 12,451,061 |
| Gross Margin | 2,978,956 | N/A | 2,978,956 |
| Gross Margin % | 19.3% | N/A | — |
| SGA | 2,326,755 | N/A | 2,326,755 [WARNING: unverified] |
| Operating Profit | 652,201 | N/A | 652,201 |
| Net Profit | 421,030 | N/A | 421,030 |
| Inventory | 1,205,695 | N/A | 1,205,695 |
| Current Assets | 1,470,581 | N/A | 1,470,581 |
| Total Assets | 5,411,530 | N/A | 5,411,530 |
| Current Liabilities | 2,031,212 | N/A | 2,031,212 |
| Liabilities | 5,092,203 | N/A | 5,092,203 |
| TSE | 319,327 | N/A | 319,327 |
| Total L+E | 5,411,530 | N/A | 5,411,530 |

Balance sheet identity: 5,092,203 + 319,327 = 5,411,530 = Total Assets ✓

Note: Strong performance in FY2020 (COVID-19 beneficiary — warehouse clubs saw elevated demand).

**Action: No change.**

---

### Year 2021

| Field | Dolt (current) | Yahoo | Recommended |
|-------|---------------|-------|-------------|
| reportDate | 2022-01-29 | N/A | 2022-01-29 |
| Net Revenue | 16,667,302 | N/A | 16,667,302 |
| Cost of Goods | 13,588,612 | N/A | 13,588,612 |
| Gross Margin | 3,078,690 | N/A | 3,078,690 |
| Gross Margin % | 18.5% | N/A | — |
| SGA | 2,446,465 | N/A | 2,446,465 [WARNING: unverified] |
| Operating Profit | 617,323 | N/A | 617,323 |
| Net Profit | 426,652 | N/A | 426,652 |
| Inventory | 1,242,935 | N/A | 1,242,935 |
| Current Assets | 1,517,056 | N/A | 1,517,056 |
| Total Assets | 5,668,894 | N/A | 5,668,894 |
| Current Liabilities | 2,002,481 | N/A | 2,002,481 |
| Liabilities | 5,020,786 | N/A | 5,020,786 |
| TSE | 648,108 | N/A | 648,108 |
| Total L+E | 5,668,894 | N/A | 5,668,894 |

Balance sheet identity: 5,020,786 + 648,108 = 5,668,894 = Total Assets ✓

**Action: No change.**

---

## Years 2022–2024: Yahoo vs Dolt Comparison

Yahoo fiscal year dates map to Dolt years as follows:
- Yahoo 2023-01-31 → Dolt year 2022 (reportDate 2023-01-28)
- Yahoo 2024-01-31 → Dolt year 2023 (reportDate 2024-02-03)
- Yahoo 2025-01-31 → Dolt year 2024 (reportDate 2025-02-01)

Operating Profit confirmation: Dolt consistently uses "Total Operating Income As Reported" for BJ's. All three years match Yahoo "Total Operating Income As Reported" exactly.

### Year 2022

| Field | Yahoo (2023-01-31) | Dolt (current) | Recommended |
|-------|-------------------|---------------|-------------|
| reportDate | 2023-01-31 | 2023-01-28 | 2023-01-28 (keep Dolt) |
| Net Revenue | 19,315,200 | 19,315,165 | 19,315,165 |
| Cost of Goods | 15,883,700 | 15,883,677 | 15,883,677 |
| Gross Margin | 3,431,490* | 3,431,488 | 3,431,488 |
| Gross Margin % | 17.8% | 17.8% | — |
| SGA | 2,668,570 | 2,668,569 | 2,668,569 |
| Operating Profit (As Reported) | 737,986 | 737,986 | 737,986 |
| Net Profit | 513,177 | 513,177 | 513,177 |
| Inventory | 1,378,550 | 1,378,551 | 1,378,551 |
| Current Assets | 1,703,240 | 1,703,245 | 1,703,245 |
| Total Assets | 6,349,960 | 6,349,956 | 6,349,956 |
| Current Liabilities | 2,545,340 | 2,545,341 | 2,545,341 |
| Liabilities | 5,303,120 | 5,303,119 | 5,303,119 |
| TSE | 1,046,840 | 1,046,837 | 1,046,837 |
| Total L+E | 6,349,960 | 6,349,956 | 6,349,956 |

*Yahoo Gross Profit shown as 3,431,490K. Dolt value 3,431,488K is more precise (from original filing).

All differences ≤ 35K (rounding/truncation from scientific notation only).

Balance sheet identity: 5,303,119 + 1,046,837 = 6,349,956 ✓

**Action: No change.**

---

### Year 2023

| Field | Yahoo (2024-01-31) | Dolt (current) | Recommended |
|-------|-------------------|---------------|-------------|
| reportDate | 2024-01-31 | 2024-02-03 | 2024-02-03 (keep Dolt) |
| Net Revenue | 19,968,700 | 19,968,689 | 19,968,689 |
| Cost of Goods | 16,326,100 | 16,326,129 | 16,326,129 |
| Gross Margin | 3,642,560 | 3,642,560 | 3,642,560 |
| Gross Margin % | 18.2% | 18.2% | — |
| SGA | 2,822,510 | 2,822,513 | 2,822,513 |
| Operating Profit (As Reported) | 800,419 | 800,419 | 800,419 |
| Net Profit | 523,741 | 523,741 | 523,741 |
| Inventory | 1,454,820 | 1,454,822 | 1,454,822 |
| Current Assets | 1,794,010 | 1,794,006 | 1,794,006 |
| Total Assets | 6,677,620 | 6,677,622 | 6,677,622 |
| Current Liabilities | 2,468,050 | 2,468,048 | 2,468,048 |
| Liabilities | 5,218,770 | 5,218,771 | 5,218,771 |
| TSE | 1,458,850 | 1,458,851 | 1,458,851 |
| Total L+E | 6,677,620 | 6,677,622 | 6,677,622 |

All differences ≤ 29K (rounding only).

Balance sheet identity: 5,218,771 + 1,458,851 = 6,677,622 ✓

**Action: No change.**

---

### Year 2024

| Field | Yahoo (2025-01-31) | Dolt (current) | Recommended |
|-------|-------------------|---------------|-------------|
| reportDate | 2025-01-31 | 2025-02-01 | 2025-02-01 (keep Dolt) |
| Net Revenue | 20,501,800 | 20,501,804 | 20,501,804 |
| Cost of Goods | 16,737,400 | 16,737,378 | 16,737,378 |
| Gross Margin | 3,764,430* | 3,764,426 | 3,764,426 |
| Gross Margin % | 18.4% | 18.4% | — |
| SGA | 2,963,880 | 2,963,883 | 2,963,883 |
| Operating Profit (As Reported) | 772,206 | 772,206 | 772,206 |
| Net Profit | 534,417 | 534,417 | 534,417 |
| Inventory | 1,508,990 | 1,508,988 | 1,508,988 |
| Current Assets | 1,878,960 | 1,878,960 | 1,878,960 |
| Total Assets | 7,065,300 | 7,065,305 | 7,065,305 |
| Current Liabilities | 2,534,080 | 2,534,082 | 2,534,082 |
| Liabilities | 5,217,850 | 5,217,851 | 5,217,851 |
| TSE | 1,847,450 | 1,847,454 | 1,847,454 |
| Total L+E | 7,065,300 | 7,065,305 | 7,065,305 |

*Yahoo Gross Profit shown as 3,764,430K; Dolt 3,764,426K is from original filing.

All differences ≤ 22K (rounding only).

Balance sheet identity: 5,217,851 + 1,847,454 = 7,065,305 ✓

**Action: No change.**

---

## Year 2025: New Insert (Yahoo 2026-01-31)

This year is not yet in the Dolt database.

### Source Data

Yahoo Finance (column: 2026-01-31):

**Income Statement:**
| Item | Yahoo Raw | Value ($K) |
|------|-----------|-----------|
| Total Revenue | 2.14573e+10 | 21,457,300 |
| Cost Of Revenue | 1.74577e+10 | 17,457,700 |
| Gross Profit | 3.99962e+09 | 3,999,620 |
| Selling General And Administration | 3.15358e+09 | 3,153,580 |
| Operating Income (clean) | 8.46045e+08 | 846,045 |
| Total Operating Income As Reported | 8.16604e+08 | 816,604 |
| Net Income Common Stockholders | 5.78377e+08 | 578,377 |

Note: Operating Income (846,045) − As Reported (816,604) = 29,441K = Special/Other Charges (2.9441e+07 = 29,441K) ✓

Note on Gross Margin: Yahoo states Gross Profit = 3,999,620K, but 21,457,300 − 17,457,700 = 3,999,600K (20K diff from scientific notation truncation). Per anomaly rule, using calculated value: 3,999,600K.

**Balance Sheet:**
| Item | Yahoo Raw | Value ($K) |
|------|-----------|-----------|
| Inventory | 1.55547e+09 | 1,555,470 |
| Current Assets | 1.99009e+09 | 1,990,090 |
| Total Assets | 7.51048e+09 | 7,510,480 |
| Current Liabilities | 2.67023e+09 | 2,670,230 |
| Common Stock Equity (= Total Equity Gross Minority Interest) | 2.19766e+09 | 2,197,660 |
| Total Liabilities Net Minority Interest | 5.31282e+09 | 5,312,820 |

### Anomaly Checks

- **Gross margin:** 3,999,600 / 21,457,300 = **18.6%** — above warehouse club benchmark (10–15%) [WARNING]. Consistent with all BJ's historical years in DB (range 17.8–19.3%). Known pattern: BJ's includes membership revenue in Net Revenue and has different product mix vs. Costco. Not an error.
- **SGA rule 3:** Yahoo SGA 3,153,580K << Total Expenses 20,611,200K — no inflation ✓
- **SGA structure:** Combined operating expense line including D&A. Gross Profit − SGA = 3,999,600 − 3,153,580 = 846,020 ≈ clean Operating Income (846,045; 25K rounding diff) ✓
- **Operating Profit:** Using "Total Operating Income As Reported" (816,604K) — consistent with BJ's convention ✓
- **TSE:** Common Stock Equity = Total Equity Gross Minority Interest = 2,197,660K (no minority interest) ✓
- **Balance sheet identity:** 5,312,820 + 2,197,660 = 7,510,480 = Total Assets ✓
- **Inventory:** 1,555,470K — large positive value, expected for warehouse club ✓

### Reconciled Values for FY2025

| Field | Recommended Value | Source | Notes |
|-------|------------------|--------|-------|
| reportDate | 2026-01-31 | Yahoo column header | |
| Net Revenue | 21,457,300 | Yahoo | |
| Cost of Goods | 17,457,700 | Yahoo | |
| Gross Margin | 3,999,600 | Calculated | Revenue − COGS; 20K below Yahoo stated Gross Profit (sci notation artifact) |
| SGA | 3,153,580 | Yahoo | Combined operating expense including D&A; consistent with BJ's convention |
| Operating Profit | 816,604 | Yahoo "As Reported" | BJ's convention; clean figure would be 846,045K |
| Net Profit | 578,377 | Yahoo | |
| Inventory | 1,555,470 | Yahoo | |
| Current Assets | 1,990,090 | Yahoo | |
| Total Assets | 7,510,480 | Yahoo | |
| Current Liabilities | 2,670,230 | Yahoo | |
| Liabilities | 5,312,820 | Calculated | Total Assets − TSE |
| TSE | 2,197,660 | Yahoo Common Stock Equity | No minority interest |
| Total L+E | 7,510,480 | Yahoo | |

**Action: New insert.**

---

## Flags Summary

| Year | Flag | Severity | Description |
|------|------|----------|-------------|
| 2018 | SGA unverified | [WARNING] | No Yahoo data for this year; SGA may be incomplete per recurring convention |
| 2018 | Negative TSE | [WARNING] | TSE = −202,084K — valid, post-LBO capital structure |
| 2019 | SGA unverified | [WARNING] | No Yahoo data for this year; SGA may be incomplete |
| 2019 | Negative TSE | [WARNING] | TSE = −54,344K — valid, final LBO-era year |
| 2020 | SGA unverified | [WARNING] | No Yahoo data for this year; SGA may be incomplete |
| 2021 | SGA unverified | [WARNING] | No Yahoo data for this year; SGA may be incomplete |
| 2018–2025 | Gross margin above benchmark | [WARNING] | All years 17.8–19.3%; above warehouse club benchmark of 10–15%. Consistent known pattern for BJ's; not an error |
| 2025 | Gross margin calc | [INFO] | Calculated Gross Margin (3,999,600K) is 20K below Yahoo stated Gross Profit (3,999,620K) — scientific notation truncation artifact only |

No [ERROR] flags. All unresolved flags are [WARNING] or [INFO] only.

---

**Analysis complete.** Run `/insert-financials BJ` to write all changed years to the database.

Only FY2025 requires a new insert. Years 2018–2024 have no changes.
