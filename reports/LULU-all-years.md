# Lululemon (LULU) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2018 | 2019-02-03 | No change |
| 2019 | 2020-02-02 | No change |
| 2020 | 2021-01-31 | No change |
| 2021 | 2022-01-30 | No change |
| 2022 | 2023-01-29 | No change |
| 2023 | 2024-01-28 | No change |
| 2024 | 2025-02-02 | No change |
| 2025 | 2026-02-01 | New insert |

---

## Company Metadata

- **company_name:** Lululemon
- **display_name:** Lululemon
- **ticker_symbol:** LULU
- **CIK:** 1397187
- **Segment:** Specialty (premium athletic apparel)
- **Fiscal year end:** Late January / early February

---

## Anomaly Detection Notes (applies across all years)

**[WARNING] Gross margin consistently above specialty benchmark (35–55%):**
Lululemon's gross margins run 55–59% across all years, above the stated 35–55% specialty range. This is consistent with LULU's premium brand positioning and high direct-to-consumer mix. No action needed — this is a known characteristic.

**[WARNING] FY2022 — Lululemon Studio goodwill impairment:**
$407,913K impairment of goodwill and other assets (Mirror/Lululemon Studio acquisition write-down) reported as a separate operating line in FY2022 10-K. This is correctly excluded from SGA and correctly included in the Operating Profit as-reported. The Dolt DB value of $1,328,408K is correct.

**[WARNING] FY2023 — Lululemon Studio restructuring charge:**
$74,501K restructuring/impairment charge (Lululemon Studio wind-down) reported as a separate operating line. This is correctly excluded from SGA and correctly included in Operating Profit as-reported. The Dolt DB value of $2,132,676K is correct.

**[WARNING] FY2025 — Operating profit declined year-over-year despite revenue growth:**
Revenue grew +$514M (+4.9% YoY) but gross margin only grew +$13M due to higher COGS. SGA grew +$304M (+8.1%), compressing operating profit from $2,505,697K to $2,210,615K (operating margin: 23.7% → 19.9%).

**SGA construction:** Lululemon uses a single combined `us-gaap_SellingGeneralAndAdministrativeExpense` line with no separate marketing or platform tech splits. No composite construction needed. Rule 1/2/3/4 do not apply. Yahoo SGA closely matches SEC SGA for all available years.

**Minor restatement note (FY2019 SGA):** The FY2019 10-K shows SGA = $1,334,276K; the FY2020 10-K's comparative column shows $1,334,247K (a $29K difference, 0.002%). The Dolt DB has $1,334,276K from the original filing. Difference is trivial — no change recommended.

---

## FY2018 Analysis

**reportDate:** 2019-02-03 | **Source:** SEC 10-K (FY2018 filing)

### Step 5 — Side-by-side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 3,288,319 | N/A | 3,288,319 | 3,288,319 |
| Cost of Goods | 1,472,032 | N/A | 1,472,032 | 1,472,032 |
| Gross Margin | 1,816,287 | N/A | 1,816,287 | 1,816,287 |
| SGA | 1,110,451 | N/A | 1,110,451 | 1,110,451 |
| Operating Profit | 705,836 | N/A | 705,836 | 705,836 |
| Net Profit | 483,801 | N/A | 483,801 | 483,801 |
| Inventory | 404,842 | N/A | 404,842 | 404,842 |
| Current Assets | 1,429,282 | N/A | 1,429,282 | 1,429,282 |
| Total Assets | 2,084,711 | N/A | 2,084,711 | 2,084,711 |
| Current Liabilities | 500,477 | N/A | 500,477 | 500,477 |
| Liabilities | 638,736 | N/A | 638,736 | 638,736 |
| Total SE | 1,445,975 | N/A | 1,445,975 | 1,445,975 |
| Total L+SE | 2,084,711 | N/A | 2,084,711 | 2,084,711 |

### Step 6 — Reconciled Recommendation

All fields match Dolt DB exactly. No changes needed.

- Balance sheet identity: $2,084,711K = $638,736K + $1,445,975K ✓
- Gross Margin %: 55.2% — above specialty benchmark [WARNING — expected for LULU]
- SGA: Single combined line from SEC. No composite construction needed.

**Verdict: No change.**

---

## FY2019 Analysis

**reportDate:** 2020-02-02 | **Source:** SEC 10-K (FY2019 filing)

### Step 5 — Side-by-side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 3,979,296 | N/A | 3,979,296 | 3,979,296 |
| Cost of Goods | 1,755,910 | N/A | 1,755,910 | 1,755,910 |
| Gross Margin | 2,223,386 | N/A | 2,223,386 | 2,223,386 |
| SGA | 1,334,276 | N/A | 1,334,276 | 1,334,276 |
| Operating Profit | 889,110 | N/A | 889,110 | 889,110 |
| Net Profit | 645,596 | N/A | 645,596 | 645,596 |
| Inventory | 518,513 | N/A | 518,513 | 518,513 |
| Current Assets | 1,807,938 | N/A | 1,807,938 | 1,807,938 |
| Total Assets | 3,281,354 | N/A | 3,281,354 | 3,281,354 |
| Current Liabilities | 620,418 | N/A | 620,418 | 620,418 |
| Liabilities | 1,329,136 | N/A | 1,329,136 | 1,329,136 |
| Total SE | 1,952,218 | N/A | 1,952,218 | 1,952,218 |
| Total L+SE | 3,281,354 | N/A | 3,281,354 | 3,281,354 |

### Step 6 — Reconciled Recommendation

All fields match Dolt DB exactly. No changes needed.

- Balance sheet identity: $3,281,354K = $1,329,136K + $1,952,218K ✓
- Gross Margin %: 55.9% — above specialty benchmark [WARNING — expected for LULU]
- Minor restatement note: FY2020 10-K comparative shows SGA as $1,334,247K ($29K lower). Difference is trivial (0.002%), no action taken.

**Verdict: No change.**

---

## FY2020 Analysis

**reportDate:** 2021-01-31 | **Source:** SEC 10-K (FY2020 filing)

### Step 5 — Side-by-side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 4,401,879 | N/A | 4,401,879 | 4,401,879 |
| Cost of Goods | 1,937,888 | N/A | 1,937,888 | 1,937,888 |
| Gross Margin | 2,463,991 | N/A | 2,463,991 | 2,463,991 |
| SGA | 1,609,003 | N/A | 1,609,003 | 1,609,003 |
| Operating Profit | 819,986 | N/A | 819,986 | 819,986 |
| Net Profit | 588,913 | N/A | 588,913 | 588,913 |
| Inventory | 647,230 | N/A | 647,230 | 647,230 |
| Current Assets | 2,124,379 | N/A | 2,124,379 | 2,124,379 |
| Total Assets | 4,185,215 | N/A | 4,185,215 | 4,185,215 |
| Current Liabilities | 883,178 | N/A | 883,178 | 883,178 |
| Liabilities | 1,626,649 | N/A | 1,626,649 | 1,626,649 |
| Total SE | 2,558,566 | N/A | 2,558,566 | 2,558,566 |
| Total L+SE | 4,185,215 | N/A | 4,185,215 | 4,185,215 |

### Step 6 — Reconciled Recommendation

All fields match Dolt DB exactly. No changes needed.

- Balance sheet identity: $4,185,215K = $1,626,649K + $2,558,566K ✓
- Gross Margin %: 55.9% — above specialty benchmark [WARNING — expected for LULU]
- Note: FY2020 10-K also shows $29,842K acquisition-related costs (Mirror acquisition) and $5,160K amortization as separate lines. These are correctly excluded from SGA.

**Verdict: No change.**

---

## FY2021 Analysis

**reportDate:** 2022-01-30 | **Source:** SEC 10-K (FY2021 filing)

### Step 5 — Side-by-side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 6,256,617 | N/A* | 6,256,617 | 6,256,617 |
| Cost of Goods | 2,648,052 | N/A* | 2,648,052 | 2,648,052 |
| Gross Margin | 3,608,565 | N/A* | 3,608,565 | 3,608,565 |
| SGA | 2,225,034 | N/A* | 2,225,034 | 2,225,034 |
| Operating Profit | 1,333,355 | N/A* | 1,333,355 | 1,333,355 |
| Net Profit | 975,322 | N/A* | 975,322 | 975,322 |
| Inventory | 966,481 | N/A* | 966,481 | 966,481 |
| Current Assets | 2,614,853 | N/A* | 2,614,853 | 2,614,853 |
| Total Assets | 4,942,478 | N/A* | 4,942,478 | 4,942,478 |
| Current Liabilities | 1,405,334 | N/A* | 1,405,334 | 1,405,334 |
| Liabilities | 2,202,432 | N/A* | 2,202,432 | 2,202,432 |
| Total SE | 2,740,046 | N/A* | 2,740,046 | 2,740,046 |
| Total L+SE | 4,942,478 | N/A* | 4,942,478 | 4,942,478 |

*Yahoo Finance FY2021 column (2022-01-31) returns mostly null values; not usable.

### Step 6 — Reconciled Recommendation

All fields match Dolt DB exactly. No changes needed.

- Balance sheet identity: $4,942,478K = $2,202,432K + $2,740,046K ✓
- Gross Margin %: 57.7% — above specialty benchmark [WARNING — expected for LULU]
- Note: $41,394K acquisition-related costs (Mirror/Lululemon Studio) correctly excluded from SGA.

**Verdict: No change.**

---

## FY2022 Analysis

**reportDate:** 2023-01-29 | **Source:** SEC 10-K (FY2022 filing)

### Step 5 — Side-by-side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 8,110,518 | 8,110,520 | 8,110,518 | 8,110,518 |
| Cost of Goods | 3,618,178 | 3,618,180 | 3,618,178 | 3,618,178 |
| Gross Margin | 4,492,340 | 4,492,340 | 4,492,340 | 4,492,340 |
| SGA | 2,757,447 | 2,757,450 | 2,757,447 | 2,757,447 |
| Operating Profit | 1,328,408 | 1,328,410* | 1,328,408 | 1,328,408 |
| Net Profit | 854,800 | 854,800 | 854,800 | 854,800 |
| Inventory | 1,447,367 | 1,447,370 | 1,447,367 | 1,447,367 |
| Current Assets | 3,159,453 | 3,159,450 | 3,159,453 | 3,159,453 |
| Total Assets | 5,607,038 | 5,607,040 | 5,607,038 | 5,607,038 |
| Current Liabilities | 1,492,198 | 1,492,200 | 1,492,198 | 1,492,198 |
| Liabilities | 2,458,239 | 2,458,240 | 2,458,239 | 2,458,239 |
| Total SE | 3,148,799 | 3,148,800 | 3,148,799 | 3,148,799 |
| Total L+SE | 5,607,038 | 5,607,040 | 5,607,038 | 5,607,038 |

*Yahoo "Total Operating Income As Reported" = $1,328,410K (matches SEC). Yahoo's "Operating Income" = $1,726,140K excludes the $407,913K goodwill impairment — do not use that figure.

### Step 6 — Reconciled Recommendation

All fields match Dolt DB exactly. No changes needed.

- Balance sheet identity: $5,607,038K = $2,458,239K + $3,148,799K ✓
- Gross Margin %: 55.4% — at the upper bound of specialty benchmark [WARNING — expected for LULU]
- [WARNING] $407,913K Lululemon Studio (Mirror acquisition) goodwill impairment in FY2022. Operating Profit of $1,328,408K correctly includes this charge as reported.
- Yahoo and SEC agree on all values within rounding.

**Verdict: No change.**

---

## FY2023 Analysis

**reportDate:** 2024-01-28 | **Source:** SEC 10-K (FY2023 filing)

### Step 5 — Side-by-side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 9,619,278 | 9,619,280 | 9,619,278 | 9,619,278 |
| Cost of Goods | 4,009,873 | 4,009,870 | 4,009,873 | 4,009,873 |
| Gross Margin | 5,609,405 | 5,609,400 | 5,609,405 | 5,609,405 |
| SGA | 3,397,218 | 3,397,220 | 3,397,218 | 3,397,218 |
| Operating Profit | 2,132,676 | 2,132,680* | 2,132,676 | 2,132,676 |
| Net Profit | 1,550,190 | 1,550,190 | 1,550,190 | 1,550,190 |
| Inventory | 1,323,602 | 1,323,600 | 1,323,602 | 1,323,602 |
| Current Assets | 4,060,577 | 4,060,580 | 4,060,577 | 4,060,577 |
| Total Assets | 7,091,941 | 7,091,940 | 7,091,941 | 7,091,941 |
| Current Liabilities | 1,631,261 | 1,631,260 | 1,631,261 | 1,631,261 |
| Liabilities | 2,859,860 | 2,859,860 | 2,859,860 | 2,859,860 |
| Total SE | 4,232,081 | 4,232,080 | 4,232,081 | 4,232,081 |
| Total L+SE | 7,091,941 | 7,091,940 | 7,091,941 | 7,091,941 |

*Yahoo "Total Operating Income As Reported" = $2,132,680K (matches SEC). Yahoo's "Operating Income" = $2,207,180K excludes the $74,501K Lululemon Studio restructuring charge — do not use that figure.

### Step 6 — Reconciled Recommendation

All fields match Dolt DB exactly. No changes needed.

- Balance sheet identity: $7,091,941K = $2,859,860K + $4,232,081K ✓
- Gross Margin %: 58.3% — above specialty benchmark [WARNING — expected for LULU]
- [WARNING] $74,501K Lululemon Studio restructuring/impairment charge in FY2023 (wind-down of the Mirror business). Operating Profit of $2,132,676K correctly includes this charge as reported.
- Confirmed no restatement in subsequent FY2024 10-K comparative column.

**Verdict: No change.**

---

## FY2024 Analysis

**reportDate:** 2025-02-02 | **Source:** SEC 10-K (FY2024 filing)

### Step 5 — Side-by-side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 10,588,126 | 10,588,100 | 10,588,126 | 10,588,126 |
| Cost of Goods | 4,317,315 | 4,317,320 | 4,317,315 | 4,317,315 |
| Gross Margin | 6,270,811 | 6,270,810 | 6,270,811 | 6,270,811 |
| SGA | 3,762,379 | 3,762,380 | 3,762,379 | 3,762,379 |
| Operating Profit | 2,505,697 | 2,505,700 | 2,505,697 | 2,505,697 |
| Net Profit | 1,814,616 | 1,814,620 | 1,814,616 | 1,814,616 |
| Inventory | 1,442,081 | 1,442,080 | 1,442,081 | 1,442,081 |
| Current Assets | 3,980,302 | 3,980,300 | 3,980,302 | 3,980,302 |
| Total Assets | 7,603,292 | 7,603,290 | 7,603,292 | 7,603,292 |
| Current Liabilities | 1,839,630 | 1,839,630 | 1,839,630 | 1,839,630 |
| Liabilities | 3,279,245 | 3,279,240 | 3,279,245 | 3,279,245 |
| Total SE | 4,324,047 | 4,324,050 | 4,324,047 | 4,324,047 |
| Total L+SE | 7,603,292 | 7,603,290 | 7,603,292 | 7,603,292 |

### Step 6 — Reconciled Recommendation

All fields match Dolt DB exactly. No changes needed.

- Balance sheet identity: $7,603,292K = $3,279,245K + $4,324,047K ✓
- Gross Margin %: 59.2% — above specialty benchmark [WARNING — expected for LULU]
- Confirmed no restatement in subsequent FY2025 10-K comparative column.
- Yahoo and SEC agree on all values within rounding.

**Verdict: No change.**

---

## FY2025 Analysis (New Data)

**reportDate:** 2026-02-01 | **Source:** SEC 10-K (FY2025 filing, filed spring 2026)

### Step 4 — Anomaly Detection

- [WARNING] Gross margin 56.6% — above specialty benchmark. Consistent with LULU premium positioning, no action needed.
- [WARNING] Operating profit declined YoY: $2,505,697K → $2,210,615K (-$295M, -11.8%) despite revenue growing +4.9%. Root cause: COGS growth outpaced revenue growth (COGS +$501M vs Revenue +$514M, minimal gross margin expansion of only $13M) while SGA grew +$304M (+8.1%). Operating margin compressed from 23.7% to 19.9%.
- Balance sheet identity check: $8,456,743K = $3,494,903K + $4,961,840K ✓
- Yahoo reportDate shows 2026-01-31; SEC filing shows 2026-02-01. Using SEC date as authoritative.
- SGA: single combined line, no composite construction needed.
- No restructuring or impairment charges in FY2025.

### Step 5 — Side-by-side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| Net Revenue | 11,102,600 | 11,102,600 | — | **11,102,600** |
| Cost of Goods | 4,818,468 | 4,818,470 | — | **4,818,468** |
| Gross Margin | 6,284,132 | 6,284,130 | — | **6,284,132** |
| SGA | 4,066,556 | 4,066,560 | — | **4,066,556** |
| Operating Profit | 2,210,615 | 2,210,620 | — | **2,210,615** |
| Net Profit | 1,579,183 | 1,579,180 | — | **1,579,183** |
| Inventory | 1,700,753 | 1,700,750 | — | **1,700,753** |
| Current Assets | 4,262,701 | 4,262,700 | — | **4,262,701** |
| Total Assets | 8,456,743 | 8,456,740 | — | **8,456,743** |
| Current Liabilities | 1,887,548 | 1,887,550 | — | **1,887,548** |
| Liabilities | 3,494,903 | 3,494,900 | — | **3,494,903** |
| Total SE | 4,961,840 | 4,961,840 | — | **4,961,840** |
| Total L+SE | 8,456,743 | 8,456,740 | — | **8,456,743** |

### Step 6 — Reconciled Recommendation

All values from SEC and Yahoo agree (within $5K rounding). Use SEC as authoritative source.

**Recommended values for new insert:**

| Field | Value |
|-------|-------|
| company_name | Lululemon |
| year | 2025 |
| reportDate | 2026-02-01 |
| Net Revenue | 11,102,600 |
| Cost of Goods | 4,818,468 |
| Gross Margin | 6,284,132 |
| SGA | 4,066,556 |
| Operating Profit | 2,210,615 |
| Net Profit | 1,579,183 |
| Inventory | 1,700,753 |
| Current Assets | 4,262,701 |
| Total Assets | 8,456,743 |
| Current Liabilities | 1,887,548 |
| Liabilities | 3,494,903 |
| Total SE | 4,961,840 |
| Total L+SE | 8,456,743 |

**Derivation checks:**
- Gross Margin = Revenue − COGS = 11,102,600 − 4,818,468 = 6,284,132 ✓
- Liabilities = Total Assets − Total SE = 8,456,743 − 4,961,840 = 3,494,903 ✓
- Total L+SE = Liabilities + Total SE = 3,494,903 + 4,961,840 = 8,456,743 ✓
- Balance sheet identity: ✓

**Verdict: New insert.**

---

## Step 7 — Readiness Signal

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql LULU` to write all changed years to the database.

**Unresolved flags to review before inserting:**
- [WARNING] FY2025 gross margin 56.6% is above specialty benchmark — expected for LULU, no action needed.
- [WARNING] FY2025 operating profit declined YoY by $295M despite revenue growth — no data error, reflects actual business performance.
- All other warnings are informational and apply consistently to LULU's premium positioning.

**No ERRORs found. All 8 years verified. Only FY2025 requires a new insert.**
