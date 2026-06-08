# Urban Outfitters (URBN) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2019-01-31 | No change |
| 2019 | 2020-01-31 | Correction: SGA −993,990K → +993,990K (sign flip) |
| 2020 | 2021-01-31 | No change |
| 2021 | 2022-01-31 | No change |
| 2022 | 2023-01-31 | No change |
| 2023 | 2024-01-31 | No change |
| 2024 | 2025-01-31 | No change |
| 2025 | 2026-01-31 | New insert |

---

## Company Notes

**Segment:** Specialty (apparel, home, accessories) — brands: Urban Outfitters, Anthropologie, Free People, Nuuly (subscription), FP Movement

**Fiscal year:** Ends late January 31 each year. FY2025 = fiscal year ending 2026-01-31.

**SGA construction:** Single combined `us-gaap_SellingGeneralAndAdministrativeExpense` line. No separate marketing or ops split. Use directly.

**Store impairment and lease abandonment charges:** URBN reports `urbn_StoreImpairmentAndLeaseAbandonment` as a separate income statement line between Cost of Revenue and Gross Profit. This reduces the SEC-reported Gross Profit below Revenue − COGS.
- **DB approach:** Use Revenue − `us-gaap_CostOfRevenue` for Gross Margin (excludes store impairment). Operating Profit is taken directly from SEC, which does include the impairment impact.
- **Yahoo COGS artifact:** Yahoo bundles store impairment into its Cost of Revenue. Always use SEC for COGS and Gross Margin for URBN.

**Gross margins:** URBN's gross margins (29–36%) are below the typical specialty range (35–55%) because COGS includes store occupancy costs (rent, utilities). This is company-specific and expected.

---

## FY2018 (ends 2019-01-31)

### Anomaly Detection

- Gross margin: $1,346,712 / $3,950,623 = 34.1% — slightly below specialty range (35–55%) but consistent with URBN's occupancy-heavy COGS structure. [WARNING — company-specific pattern, not an error]
- Balance sheet identity: $671,417 + $1,489,098 = $2,160,515 = Total Assets ✓
- No store impairment in FY2018.
- SGA: Single line, no composite rules triggered.
- No company notes entry for URBN at time of prior analysis.

### Side-by-Side Comparison

| Field | SEC (FY2018 10-K) | Yahoo | Dolt (current) | Recommended |
|-------|-------------------|-------|----------------|-------------|
| reportDate | 2019-01-31 | — | 2019-01-31 | 2019-01-31 |
| Net Revenue | 3,950,623 | — | 3,950,623 | 3,950,623 |
| Cost of Goods | 2,603,911 | — | 2,603,911 | 2,603,911 |
| Gross Margin | 1,346,712 | — | 1,346,712 | 1,346,712 |
| SGA | 965,399 | — | 965,399 | 965,399 |
| Operating Profit | 381,313 | — | 381,313 | 381,313 |
| Net Profit | 298,003 | — | 298,003 | 298,003 |
| Inventory | 370,507 | — | 370,507 | 370,507 |
| Current Assets | 1,202,756 | — | 1,202,756 | 1,202,756 |
| Total Assets | 2,160,515 | — | 2,160,515 | 2,160,515 |
| Current Liabilities | 386,644 | — | 386,644 | 386,644 |
| Liabilities | 671,417 | — | 671,417 | 671,417 |
| Total Shareholder Equity | 1,489,098 | — | 1,489,098 | 1,489,098 |
| Total Liab and SE | 2,160,515 | — | 2,160,515 | 2,160,515 |

### Reconciled Recommendation

All 14 fields match SEC exactly. **No change needed.**

---

## FY2019 (ends 2020-01-31)

### Anomaly Detection

- **[ERROR] SGA = −993,990K in Dolt:** Negative SGA is impossible. Correct value is +993,990K per SEC. This is a sign flip data entry error.
- Gross margin (clean): $1,254,437 / $3,983,789 = 31.5% — below range but this includes the effect of COVID start and store impairment charges on operations. [WARNING — pattern]
- Store impairment: $14,611K (FY2019 10-K). Separate from COGS; reduces SEC-reported gross to $1,239,826K. DB uses clean gross $1,254,437K (Revenue − COGS only).
- Goodwill impairment: $13,911K (FY2019). Separate line, correctly excluded from SGA.
- Balance sheet identity: $1,860,278 + $1,455,355 = $3,315,633 = Total Assets ✓
- Note: FY2019 balance sheet jump ($2.16B → $3.32B Total Assets) reflects adoption of ASC 842 lease accounting; operating lease right-of-use assets ($1,170,531K) added to balance sheet.

### Side-by-Side Comparison

| Field | SEC (FY2019 10-K) | Yahoo | Dolt (current) | Recommended |
|-------|-------------------|-------|----------------|-------------|
| reportDate | 2020-01-31 | — | 2020-01-31 | 2020-01-31 |
| Net Revenue | 3,983,789 | — | 3,983,789 | 3,983,789 |
| Cost of Goods | 2,729,352 | — | 2,729,352 | 2,729,352 |
| Gross Margin | 1,254,437* | — | 1,254,437 | 1,254,437 |
| SGA | 993,990 | — | **−993,990*** | **993,990** |
| Operating Profit | 231,925 | — | 231,925 | 231,925 |
| Net Profit | 168,096 | — | 168,096 | 168,096 |
| Inventory | 409,534 | — | 409,534 | 409,534 |
| Current Assets | 1,053,396 | — | 1,053,396 | 1,053,396 |
| Total Assets | 3,315,633 | — | 3,315,633 | 3,315,633 |
| Current Liabilities | 638,770 | — | 638,770 | 638,770 |
| Liabilities | 1,860,278 | — | 1,860,278 | 1,860,278 |
| Total Shareholder Equity | 1,455,355 | — | 1,455,355 | 1,455,355 |
| Total Liab and SE | 3,315,633 | — | 3,315,633 | 3,315,633 |

*SEC Gross Margin note: SEC-reported Gross Profit = $1,239,826K (includes $14,611K store impairment deduction). DB uses clean Revenue − COGS = $1,254,437K, consistent with all other URBN years.

### Reconciled Recommendation

- **SGA:** $993,990K (from SEC). Dolt has −993,990K (wrong sign). **Overwrite.**
- All other 13 fields: unchanged.

---

## FY2020 (ends 2021-01-31)

### Anomaly Detection

- Gross margin (clean): $877,402 / $3,449,749 = 25.4% — significantly below range due to COVID-19 store closures and reduced revenue. [WARNING — COVID year, expected]
- Store impairment: $15,496K. Separate from COGS.
- Balance sheet identity: $2,068,987 + $1,477,358 = $3,546,345 ✓
- OpInc barely positive ($3,972K): consistent with COVID-disrupted year.

### Side-by-Side Comparison

| Field | SEC (FY2020 10-K) | Yahoo | Dolt (current) | Recommended |
|-------|-------------------|-------|----------------|-------------|
| reportDate | 2021-01-31 | — | 2021-01-31 | 2021-01-31 |
| Net Revenue | 3,449,749 | — | 3,449,749 | 3,449,749 |
| Cost of Goods | 2,572,347 | — | 2,572,347 | 2,572,347 |
| Gross Margin | 877,402 | — | 877,402 | 877,402 |
| SGA | 857,934 | — | 857,934 | 857,934 |
| Operating Profit | 3,972 | — | 3,972 | 3,972 |
| Net Profit | 1,236 | — | 1,236 | 1,236 |
| Inventory | 389,618 | — | 389,618 | 389,618 |
| Current Assets | 1,223,332 | — | 1,223,332 | 1,223,332 |
| Total Assets | 3,546,345 | — | 3,546,345 | 3,546,345 |
| Current Liabilities | 906,132 | — | 906,132 | 906,132 |
| Liabilities | 2,068,987 | — | 2,068,987 | 2,068,987 |
| Total Shareholder Equity | 1,477,358 | — | 1,477,358 | 1,477,358 |
| Total Liab and SE | 3,546,345 | — | 3,546,345 | 3,546,345 |

### Reconciled Recommendation

All fields match SEC exactly. **No change needed.**

---

## FY2021 (ends 2022-01-31)

### Anomaly Detection

- Gross margin: $1,493,950 / $4,548,763 = 32.8% — below range; recovery year post-COVID. [WARNING — pattern]
- No store impairment in FY2021 (first clean year).
- Balance sheet identity: $2,045,607 + $1,745,740 = $3,791,347 ✓

### Side-by-Side Comparison

| Field | SEC (FY2021 10-K) | Yahoo | Dolt (current) | Recommended |
|-------|-------------------|-------|----------------|-------------|
| reportDate | 2022-01-31 | — | 2022-01-31 | 2022-01-31 |
| Net Revenue | 4,548,763 | — | 4,548,763 | 4,548,763 |
| Cost of Goods | 3,054,813 | — | 3,054,813 | 3,054,813 |
| Gross Margin | 1,493,950 | — | 1,493,950 | 1,493,950 |
| SGA | 1,085,384 | — | 1,085,384 | 1,085,384 |
| Operating Profit | 408,566 | — | 408,566 | 408,566 |
| Net Profit | 310,616 | — | 310,616 | 310,616 |
| Inventory | 569,699 | — | 569,699 | 569,699 |
| Current Assets | 1,285,747 | — | 1,285,747 | 1,285,747 |
| Total Assets | 3,791,347 | — | 3,791,347 | 3,791,347 |
| Current Liabilities | 981,473 | — | 981,473 | 981,473 |
| Liabilities | 2,045,607 | — | 2,045,607 | 2,045,607 |
| Total Shareholder Equity | 1,745,740 | — | 1,745,740 | 1,745,740 |
| Total Liab and SE | 3,791,347 | — | 3,791,347 | 3,791,347 |

### Reconciled Recommendation

All fields match SEC exactly. **No change needed.**

---

## FY2022 (ends 2023-01-31)

### Anomaly Detection

- Gross margin (clean): $1,433,633 / $4,795,244 = 29.9% — below range; inflation/supply-chain pressures year. [WARNING — pattern]
- Store impairment: $6,417K. Separate.
- Balance sheet identity: $1,890,229 + $1,792,683 = $3,682,912 ✓
- Yahoo COGS: $3,368,030K (includes store impairment $6,417K) vs SEC $3,361,611K. Yahoo artifact confirmed; use SEC.

### Side-by-Side Comparison

| Field | SEC (FY2022 10-K) | Yahoo (FY2022) | Dolt (current) | Recommended |
|-------|-------------------|----------------|----------------|-------------|
| reportDate | 2023-01-31 | — | 2023-01-31 | 2023-01-31 |
| Net Revenue | 4,795,244 | 4,795,240 | 4,795,244 | 4,795,244 |
| Cost of Goods | 3,361,611 | 3,368,030* | 3,361,611 | 3,361,611 |
| Gross Margin | 1,433,633 | — | 1,433,633 | 1,433,633 |
| SGA | 1,200,593 | 1,200,593 | 1,200,593 | 1,200,593 |
| Operating Profit | 226,623 | 226,623 | 226,623 | 226,623 |
| Net Profit | 159,699 | 159,699 | 159,699 | 159,699 |
| Inventory | 587,510 | 587,510 | 587,510 | 587,510 |
| Current Assets | 1,237,719 | 1,237,720 | 1,237,719 | 1,237,719 |
| Total Assets | 3,682,912 | 3,682,910 | 3,682,912 | 3,682,912 |
| Current Liabilities | 890,374 | 890,374 | 890,374 | 890,374 |
| Liabilities | 1,890,229 | 1,890,230 | 1,890,229 | 1,890,229 |
| Total Shareholder Equity | 1,792,683 | 1,792,680 | 1,792,683 | 1,792,683 |
| Total Liab and SE | 3,682,912 | 3,682,910 | 3,682,912 | 3,682,912 |

*Yahoo COGS includes store impairment ($6,417K); use SEC.

### Reconciled Recommendation

All fields match SEC exactly. Yahoo differences are store impairment artifact or rounding. **No change needed.**

---

## FY2023 (ends 2024-01-31)

### Anomaly Detection

- Gross margin (clean): $1,727,279 / $5,153,237 = 33.5% — below range; improving trend. [WARNING — pattern]
- Store impairment and lease abandonment: $11,875K. Separate.
- Asset impairment: $6,404K (Nuuly Thrift marketplace writedown). Separate from SGA per anomaly rules.
- Balance sheet identity: $1,998,669 + $2,112,540 = $4,111,209 ✓

### Side-by-Side Comparison

| Field | SEC (FY2023 10-K) | Yahoo (FY2023) | Dolt (current) | Recommended |
|-------|-------------------|----------------|----------------|-------------|
| reportDate | 2024-01-31 | — | 2024-01-31 | 2024-01-31 |
| Net Revenue | 5,153,237 | 5,153,240 | 5,153,237 | 5,153,237 |
| Cost of Goods | 3,425,958 | 3,437,830* | 3,425,958 | 3,425,958 |
| Gross Margin | 1,727,279 | — | 1,727,279 | 1,727,279 |
| SGA | 1,339,205 | 1,339,200 | 1,339,205 | 1,339,205 |
| Operating Profit | 369,795 | 369,795 | 369,795 | 369,795 |
| Net Profit | 287,674 | 287,674 | 287,674 | 287,674 |
| Inventory | 550,242 | 550,242 | 550,242 | 550,242 |
| Current Assets | 1,282,503 | 1,282,500 | 1,282,503 | 1,282,503 |
| Total Assets | 4,111,209 | 4,111,210 | 4,111,209 | 4,111,209 |
| Current Liabilities | 994,205 | 994,205 | 994,205 | 994,205 |
| Liabilities | 1,998,669 | 1,998,670 | 1,998,669 | 1,998,669 |
| Total Shareholder Equity | 2,112,540 | 2,112,540 | 2,112,540 | 2,112,540 |
| Total Liab and SE | 4,111,209 | 4,111,210 | 4,111,209 | 4,111,209 |

*Yahoo COGS includes store impairment/lease abandonment ($11,875K); use SEC.

### Reconciled Recommendation

All fields match SEC exactly. **No change needed.**

---

## FY2024 (ends 2025-01-31)

### Anomaly Detection

- Gross margin (clean): $1,931,271 / $5,550,666 = 34.8% — approaching lower bound of specialty range. [WARNING — pattern]
- Store impairment and lease abandonment: $4,601K. Separate.
- No asset impairment in FY2024.
- Balance sheet identity: $2,047,976 + $2,471,504 = $4,519,480 ✓
- Yahoo COGS: $3,624,000K (includes store impairment $4,601K ≈ $3,619,395 + $4,601 = $3,623,996K). Yahoo artifact confirmed; use SEC.

### Side-by-Side Comparison

| Field | SEC (FY2024 10-K) | Yahoo (FY2024) | Dolt (current) | Recommended |
|-------|-------------------|----------------|----------------|-------------|
| reportDate | 2025-01-31 | — | 2025-01-31 | 2025-01-31 |
| Net Revenue | 5,550,666 | 5,550,670 | 5,550,666 | 5,550,666 |
| Cost of Goods | 3,619,395 | 3,624,000* | 3,619,395 | 3,619,395 |
| Gross Margin | 1,931,271 | — | 1,931,271 | 1,931,271 |
| SGA | 1,452,906 | 1,452,910 | 1,452,906 | 1,452,906 |
| Operating Profit | 473,764 | 473,764 | 473,764 | 473,764 |
| Net Profit | 402,462 | 402,462 | 402,462 | 402,462 |
| Inventory | 621,146 | 621,146 | 621,146 | 621,146 |
| Current Assets | 1,492,796 | 1,492,800 | 1,492,796 | 1,492,796 |
| Total Assets | 4,519,480 | 4,519,480 | 4,519,480 | 4,519,480 |
| Current Liabilities | 1,075,679 | 1,075,680 | 1,075,679 | 1,075,679 |
| Liabilities | 2,047,976 | 2,047,980 | 2,047,976 | 2,047,976 |
| Total Shareholder Equity | 2,471,504 | 2,471,500 | 2,471,504 | 2,471,504 |
| Total Liab and SE | 4,519,480 | 4,519,480 | 4,519,480 | 4,519,480 |

*Yahoo COGS includes store impairment ($4,601K); use SEC.

### Reconciled Recommendation

All fields match SEC exactly. Yahoo COGS difference = store impairment artifact. **No change needed.**

---

## FY2025 (ends 2026-01-31) — NEW INSERT

### Anomaly Detection

- Gross margin (clean): $2,219,742 / $6,165,376 = 36.0% — at lower bound of specialty range (35–55%). Within acceptable range. ✓
- Store impairment and lease abandonment: $1,989K (much smaller than prior years). Separate.
- No asset impairment in FY2025.
- Balance sheet identity: $2,192,326 + $2,815,287 = $5,007,613 ✓
- Yahoo revenue $6,165,380K vs SEC $6,165,376K — $4K rounding, use SEC.
- Yahoo COGS $3,947,620K (includes store impairment ~$1,989K) vs SEC $3,945,634K — Yahoo artifact confirmed; use SEC.
- Yahoo SGA $1,612,120K vs SEC $1,612,119K — $1K rounding; use SEC.
- Yahoo Operating Income: $605,634K ✓ (exact match SEC).
- All Yahoo balance sheet values within $4K rounding of SEC.

### Side-by-Side Comparison

| Field | SEC (FY2025 10-K) | Yahoo (FY2025) | Dolt (current) | Recommended |
|-------|-------------------|----------------|----------------|-------------|
| reportDate | 2026-01-31 | 2026-01-31 | (not in DB) | 2026-01-31 |
| Net Revenue | 6,165,376 | 6,165,380 | — | 6,165,376 |
| Cost of Goods | 3,945,634 | 3,947,620* | — | 3,945,634 |
| Gross Margin | 2,219,742 | — | — | 2,219,742 |
| SGA | 1,612,119 | 1,612,120 | — | 1,612,119 |
| Operating Profit | 605,634 | 605,634 | — | 605,634 |
| Net Profit | 464,919 | 464,919 | — | 464,919 |
| Inventory | 700,945 | 700,945 | — | 700,945 |
| Current Assets | 1,686,104 | 1,686,100 | — | 1,686,104 |
| Total Assets | 5,007,613 | 5,007,610 | — | 5,007,613 |
| Current Liabilities | 1,118,094 | 1,118,090 | — | 1,118,094 |
| Liabilities | 2,192,326 | 2,192,330 | — | 2,192,326 |
| Total Shareholder Equity | 2,815,287 | 2,815,290 | — | 2,815,287 |
| Total Liab and SE | 5,007,613 | 5,007,610 | — | 5,007,613 |

*Yahoo COGS includes store impairment ($1,989K); use SEC.

Gross Margin derivation: $6,165,376 − $3,945,634 = $2,219,742K (clean, DB approach)
OpInc cross-check: SEC Gross (with imp.) $2,217,753 − SGA $1,612,119 = $605,634 ✓
Clean check: $2,219,742 − $1,989 (store imp.) − $1,612,119 = $605,634 ✓

### Reconciled Recommendation

All 13 fields sourced from SEC FY2025 10-K. Yahoo agrees on Operating Profit and Net Profit exactly; COGS and revenue differ only by store impairment treatment and rounding.

---

## Analysis Complete

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql URBN` to write all changed years to the database.

**Changes to apply:**
- FY2019 correction: SGA −993,990K → +993,990K (sign flip error)
- FY2025 new insert (reportDate 2026-01-31)

**Flags for review before inserting:**
- [WARNING] Gross margins across all URBN years are 25–36%, below the 35–55% specialty benchmark. This is a company-specific structural pattern (occupancy costs in COGS, multi-brand including subscription) — not an error.
- [WARNING] FY2020 gross margin of 25.4% reflects COVID-19 store disruption year — expected anomaly.
