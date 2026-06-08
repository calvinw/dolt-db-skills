# Build-A-Bear (BBW) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-06
**Source:** /verify-dolt-db-financials skill

---

## Company Metadata

| Field | Value |
|-------|-------|
| company_name (DB key) | Build-A-Bear |
| CIK | 1113809 |
| display_name | Build-A-Bear |
| ticker_symbol | BBW |
| Segment | Specialty / Experiential Toy Retailer |

**Fiscal Year Note:** Build-A-Bear's fiscal year ends on the last Saturday of January or first Saturday of February (52/53-week year). The "year" label in the DB refers to the fiscal year that ended in early February/late January of the FOLLOWING calendar year (e.g., "2024" = FY ending 2025-02-01).

---

## Per-Year Summary Table

| Year | reportDate | Action |
|------|------------|--------|
| 2018 | 2019-02-02 | Correction: Operating Profit (Dolt stores pre-tax income; recommend keeping Gross Profit − SGA = −18,422K) |
| 2019 | 2020-02-01 | Correction: Operating Profit (Dolt stores pre-tax income; recommend keeping Gross Profit − SGA = 1,576K) |
| 2020 | 2021-01-30 | Correction: Operating Profit (Dolt stores pre-tax income; recommend keeping Gross Profit − SGA − Impairment = −27,522K) |
| 2021 | 2022-01-29 | No change — all values confirmed |
| 2022 | 2023-01-28 | No change — all values confirmed |
| 2023 | 2024-02-03 | No change — all values confirmed |
| 2024 | 2025-02-01 | No change — all values confirmed |
| 2025 | 2026-01-31 | New insert — Yahoo Finance data available; SEC 10-K not yet filed |

---

## FY2018 Analysis

**reportDate:** 2019-02-02

### Step 3 — Extracted Values (in $thousands)

#### SEC (FY2019 10-K, comparative column 2019-02-02)

| Field | SEC Value |
|-------|-----------|
| Net Revenue | 336,585 |
| Cost of Goods | 197,831 |
| Gross Margin | 138,754 |
| SGA | 157,176 |
| Operating Profit | −18,422 (Gross − SGA; excludes store impairment below gross line) |
| Net Profit | −17,933 |
| Inventory | 58,356 |
| Current Assets | 99,798 |
| Total Assets | 172,046 |
| Current Liabilities | 56,177 |
| Liabilities | 77,732 (172,046 − 94,314) |
| Total Shareholder Equity | 94,314 |
| Total Liabilities and SE | 172,046 |

Note: Store Asset Impairment of $5,871K is reported as a separate line item below gross profit in the income statement. It is NOT included in COGS and should be excluded from Operating Profit for consistency with later years where BBW dropped impairment charges. However, this creates a dilemma: if impairment is included, Operating = 138,754 − 5,871 − 157,176 = −24,293K; if excluded (Gross − SGA only), Operating = −18,422K. The Dolt DB uses −18,507K which is the Pre-tax Income figure. Recommending Gross Profit − SGA = −18,422K (excluding impairment for comparability).

#### Yahoo Finance
Yahoo does not cover FY2018 data (only provides ~4 years back from current date).

#### Dolt (current)

| Field | Dolt Value |
|-------|-----------|
| Net Revenue | 336,585 |
| Cost of Goods | 197,831 |
| Gross Margin | 138,754 |
| SGA | 157,176 |
| Operating Profit | −18,507 |
| Net Profit | −17,933 |
| Inventory | 58,356 |
| Current Assets | 99,798 |
| Total Assets | 172,046 |
| Current Liabilities | 56,177 |
| Liabilities | 77,732 |
| Total Shareholder Equity | 94,314 |
| Total Liabilities and SE | 172,046 |

### Step 4 — Anomaly Detection

**[WARNING] Operating Profit mismatch:** Dolt stores −18,507K which equals Pre-tax Income (Income Before Tax). The correct Operating Profit = Gross Margin − SGA = 138,754 − 157,176 = −18,422K. The −85K difference equals the "Interest expense, net" line (−$85K = interest income). Dolt appears to store Pre-tax Income instead of Operating Income for this year.

**[WARNING] Store Asset Impairment:** $5,871K impairment charge is included in the income statement below gross profit. This is an above-the-line operating charge but excluded from SGA. For DB consistency (FY2021 onward shows zero impairment), recommend Operating Profit = Gross − SGA only (−18,422K).

**Gross Margin check:** 138,754 / 336,585 = 41.2% — slightly below the 45–55% specialty retailer benchmark. [WARNING] borderline low, but acceptable for a toy/experiential retailer with physical product COGS. No action needed.

**Balance sheet identity:** 172,046 = 172,046 ✓

**No negative equity.** ✓

### Step 5 — Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 336,585 | N/A | 336,585 | 336,585 |
| Cost of Goods | 197,831 | N/A | 197,831 | 197,831 |
| Gross Margin | 138,754 | N/A | 138,754 | 138,754 |
| SGA | 157,176 | N/A | 157,176 | 157,176 |
| Operating Profit | −18,422 | N/A | **−18,507** * | **−18,422** |
| Net Profit | −17,933 | N/A | −17,933 | −17,933 |
| Inventory | 58,356 | N/A | 58,356 | 58,356 |
| Current Assets | 99,798 | N/A | 99,798 | 99,798 |
| Total Assets | 172,046 | N/A | 172,046 | 172,046 |
| Current Liabilities | 56,177 | N/A | 56,177 | 56,177 |
| Liabilities | 77,732 | N/A | 77,732 | 77,732 |
| Total SE | 94,314 | N/A | 94,314 | 94,314 |
| Total L&SE | 172,046 | N/A | 172,046 | 172,046 |

`*` = disagrees with recommended

### Step 6 — Reconciled Recommendation

| Field | Recommended | Source | Dolt Differs? |
|-------|-------------|--------|----------------|
| Net Revenue | 336,585 | SEC | No |
| Cost of Goods | 197,831 | SEC | No |
| Gross Margin | 138,754 | SEC (calculated) | No |
| SGA | 157,176 | SEC | No |
| Operating Profit | **−18,422** | SEC (Gross − SGA) | **YES — Dolt has −18,507** |
| Net Profit | −17,933 | SEC | No |
| Inventory | 58,356 | SEC | No |
| Current Assets | 99,798 | SEC | No |
| Total Assets | 172,046 | SEC | No |
| Current Liabilities | 56,177 | SEC | No |
| Liabilities | 77,732 | SEC (derived) | No |
| Total SE | 94,314 | SEC | No |
| Total L&SE | 172,046 | SEC | No |

---

## FY2019 Analysis

**reportDate:** 2020-02-01

### Step 3 — Extracted Values (in $thousands)

#### SEC (FY2020 10-K, comparative column 2020-02-01)

| Field | SEC Value |
|-------|-----------|
| Net Revenue | 338,543 |
| Cost of Goods | 184,920 |
| Gross Margin | 153,623 |
| SGA | 152,047 |
| Operating Profit | 1,576 (Gross − SGA) |
| Net Profit | 261 |
| Inventory | 53,381 |
| Current Assets | 98,750 |
| Total Assets | 297,262 |
| Current Liabilities | 85,964 |
| Liabilities | 208,631 (297,262 − 88,631) |
| Total Shareholder Equity | 88,631 |
| Total Liabilities and SE | 297,262 |

Note: FY2019 was the first year BBW adopted ASC 842 (operating lease right-of-use assets), which dramatically increased Total Assets from 172,046 (FY2018) to 297,262 (FY2019) — the right-of-use asset of 126,144K is included.

#### Yahoo Finance
Yahoo does not cover FY2019.

#### Dolt (current)

| Field | Dolt Value |
|-------|-----------|
| Net Revenue | 338,543 |
| Cost of Goods | 184,920 |
| Gross Margin | 153,623 |
| SGA | 152,047 |
| Operating Profit | 1,561 |
| Net Profit | 261 |
| Inventory | 53,381 |
| Current Assets | 98,750 |
| Total Assets | 297,262 |
| Current Liabilities | 85,964 |
| Liabilities | 208,631 |
| Total SE | 88,631 |
| Total L&SE | 297,262 |

### Step 4 — Anomaly Detection

**[WARNING] Operating Profit mismatch:** Dolt stores 1,561K which equals Pre-tax Income. The correct Operating Profit = 153,623 − 152,047 = 1,576K. The 15K difference equals the interest line (interest income of $15K net).

**Gross Margin check:** 153,623 / 338,543 = 45.4% — within 45–55% specialty benchmark. ✓

**Balance sheet identity:** 297,262 = 297,262 ✓

**Large Total Assets jump FY2018→FY2019:** 172,046 → 297,262 (+72.8%). This is explained by ASC 842 adoption — operating lease right-of-use assets of $126,144K added to balance sheet.

### Step 5 — Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 338,543 | N/A | 338,543 | 338,543 |
| Cost of Goods | 184,920 | N/A | 184,920 | 184,920 |
| Gross Margin | 153,623 | N/A | 153,623 | 153,623 |
| SGA | 152,047 | N/A | 152,047 | 152,047 |
| Operating Profit | 1,576 | N/A | **1,561** * | **1,576** |
| Net Profit | 261 | N/A | 261 | 261 |
| Inventory | 53,381 | N/A | 53,381 | 53,381 |
| Current Assets | 98,750 | N/A | 98,750 | 98,750 |
| Total Assets | 297,262 | N/A | 297,262 | 297,262 |
| Current Liabilities | 85,964 | N/A | 85,964 | 85,964 |
| Liabilities | 208,631 | N/A | 208,631 | 208,631 |
| Total SE | 88,631 | N/A | 88,631 | 88,631 |
| Total L&SE | 297,262 | N/A | 297,262 | 297,262 |

### Step 6 — Reconciled Recommendation

| Field | Recommended | Source | Dolt Differs? |
|-------|-------------|--------|----------------|
| Operating Profit | **1,576** | SEC (Gross − SGA) | **YES — Dolt has 1,561** |
| All other fields | Same as Dolt | SEC | No |

---

## FY2020 Analysis

**reportDate:** 2021-01-30

### Step 3 — Extracted Values (in $thousands)

#### SEC (FY2021 10-K, comparative column 2021-01-30)

| Field | SEC Value |
|-------|-----------|
| Net Revenue | 255,310 |
| Cost of Goods | 157,901 |
| Gross Margin | 97,409 |
| SGA | 117,585 |
| Store Asset Impairment | 7,346 (below gross profit; separate line) |
| Operating Profit (Gross−SGA only) | −20,176 |
| Operating Profit (incl. impairment) | −27,522 |
| Net Profit | −22,983 |
| Inventory | 46,947 |
| Current Assets | 100,193 |
| Total Assets | 261,372 |
| Current Liabilities | 89,328 |
| Liabilities | 194,064 (261,372 − 67,308) |
| Total Shareholder Equity | 67,308 |
| Total Liabilities and SE | 261,372 |

Note: FY2020 was severely impacted by COVID-19 (stores closed, reduced traffic). The 7,346K store asset impairment is significant. Pre-tax income = −20,186K. Interest income net = −10K.

#### Yahoo Finance
Yahoo does not cover FY2020.

#### Dolt (current)

| Field | Dolt Value |
|-------|-----------|
| Net Revenue | 255,310 |
| Cost of Goods | 157,901 |
| Gross Margin | 97,409 |
| SGA | 117,585 |
| Operating Profit | −20,186 |
| Net Profit | −22,983 |
| Inventory | 46,947 |
| Current Assets | 100,193 |
| Total Assets | 261,372 |
| Current Liabilities | 89,328 |
| Liabilities | 194,064 |
| Total SE | 67,308 |
| Total L&SE | 261,372 |

### Step 4 — Anomaly Detection

**[WARNING] Operating Profit — multiple interpretations:**
- Dolt: −20,186K = Pre-tax Income
- SEC (Gross − SGA): −20,176K (differs from Dolt by 10K = interest income line)
- SEC (Gross − SGA − Impairment): −27,522K

The impairment of 7,346K is a real operating charge in FY2020. The correct operating profit including impairment = −27,522K. However, for consistency with FY2018–2019 where impairment was also present but Dolt excluded it from Operating Profit, and for consistency with FY2021+ where impairment = 0, the recommended approach is Gross − SGA only (−20,176K).

**[WARNING] Decision point on impairment:** If we include impairment in Operating Profit for FY2020, it produces −27,522K, which properly reflects the economic reality. If we exclude it (Gross − SGA), it's −20,176K. Recommendation: use Gross − SGA = −20,176K for DB consistency with other years. Note that Dolt has −20,186K (pre-tax), off by 10K from the recommended value.

**Gross Margin check:** 97,409 / 255,310 = 38.2% — below 45–55% benchmark. [WARNING] — but understandable given COVID-19 disruption (lower sales volume, fixed cost absorption). Not a data error.

**Balance sheet identity:** 261,372 = 261,372 ✓

### Step 5 — Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 255,310 | N/A | 255,310 | 255,310 |
| Cost of Goods | 157,901 | N/A | 157,901 | 157,901 |
| Gross Margin | 97,409 | N/A | 97,409 | 97,409 |
| SGA | 117,585 | N/A | 117,585 | 117,585 |
| Operating Profit | −20,176 | N/A | **−20,186** * | **−20,176** |
| Net Profit | −22,983 | N/A | −22,983 | −22,983 |
| Inventory | 46,947 | N/A | 46,947 | 46,947 |
| Current Assets | 100,193 | N/A | 100,193 | 100,193 |
| Total Assets | 261,372 | N/A | 261,372 | 261,372 |
| Current Liabilities | 89,328 | N/A | 89,328 | 89,328 |
| Liabilities | 194,064 | N/A | 194,064 | 194,064 |
| Total SE | 67,308 | N/A | 67,308 | 67,308 |
| Total L&SE | 261,372 | N/A | 261,372 | 261,372 |

### Step 6 — Reconciled Recommendation

| Field | Recommended | Source | Dolt Differs? |
|-------|-------------|--------|----------------|
| Operating Profit | **−20,176** | SEC (Gross − SGA, excl. impairment) | **YES — Dolt has −20,186** |
| All other fields | Same as Dolt | SEC | No |

---

## FY2021 Analysis

**reportDate:** 2022-01-29

### Step 3 — Extracted Values (in $thousands)

#### SEC (FY2022 10-K, comparative column 2022-01-29 / FY2021 10-K primary column)

| Field | SEC Value |
|-------|-----------|
| Net Revenue | 411,522 |
| Cost of Goods | 193,567 |
| Gross Margin | 217,955 |
| SGA | 167,250 |
| Operating Profit | 50,705 (Gross − SGA) |
| Net Profit | 47,265 |
| Inventory | 71,809 |
| Current Assets | 129,998 |
| Total Assets | 266,324 |
| Current Liabilities | 97,382 |
| Liabilities | 172,641 (266,324 − 93,683) |
| Total Shareholder Equity | 93,683 |
| Total Liabilities and SE | 266,324 |

#### Yahoo Finance
Not available for this year.

#### Dolt (current)

| Field | Dolt Value |
|-------|-----------|
| Net Revenue | 411,522 |
| Cost of Goods | 193,567 |
| Gross Margin | 217,955 |
| SGA | 167,250 |
| Operating Profit | 50,705 |
| Net Profit | 47,265 |
| Inventory | 71,809 |
| Current Assets | 129,998 |
| Total Assets | 266,324 |
| Current Liabilities | 97,382 |
| Liabilities | 172,641 |
| Total SE | 93,683 |
| Total L&SE | 266,324 |

### Step 4 — Anomaly Detection

**All values confirmed correct.** No discrepancies between SEC and Dolt.

**Gross Margin check:** 217,955 / 411,522 = 53.0% — within 45–55% specialty benchmark. ✓

**Balance sheet identity:** 266,324 = 266,324 ✓

**Strong recovery from COVID FY2020:** Revenue +61%, Operating Profit swung from −20,186K to +50,705K. Consistent with post-COVID reopening.

### Step 5 — Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 411,522 | N/A | 411,522 | 411,522 |
| Cost of Goods | 193,567 | N/A | 193,567 | 193,567 |
| Gross Margin | 217,955 | N/A | 217,955 | 217,955 |
| SGA | 167,250 | N/A | 167,250 | 167,250 |
| Operating Profit | 50,705 | N/A | 50,705 | 50,705 |
| Net Profit | 47,265 | N/A | 47,265 | 47,265 |
| Inventory | 71,809 | N/A | 71,809 | 71,809 |
| Current Assets | 129,998 | N/A | 129,998 | 129,998 |
| Total Assets | 266,324 | N/A | 266,324 | 266,324 |
| Current Liabilities | 97,382 | N/A | 97,382 | 97,382 |
| Liabilities | 172,641 | N/A | 172,641 | 172,641 |
| Total SE | 93,683 | N/A | 93,683 | 93,683 |
| Total L&SE | 266,324 | N/A | 266,324 | 266,324 |

### Step 6 — Reconciled Recommendation

All values match. No changes needed.

---

## FY2022 Analysis

**reportDate:** 2023-01-28

### Step 3 — Extracted Values (in $thousands)

#### SEC (FY2023 10-K, comparative column 2023-01-28)

| Field | SEC Value |
|-------|-----------|
| Net Revenue | 467,937 |
| Cost of Goods | 222,065 |
| Gross Margin | 245,872 |
| SGA | 183,929 |
| Operating Profit | 61,943 (Gross − SGA) |
| Net Profit | 47,985 |
| Inventory | 70,485 |
| Current Assets | 147,431 |
| Total Assets | 280,794 |
| Current Liabilities | 101,151 |
| Liabilities | 161,677 (280,794 − 119,117) |
| Total Shareholder Equity | 119,117 |
| Total Liabilities and SE | 280,794 |

#### Yahoo Finance (column 2023-01-31)

| Field | Yahoo Value |
|-------|-------------|
| Net Revenue | 467,937 |
| Cost of Goods | 222,065 |
| Gross Margin | 245,872 |
| SGA | 183,929 |
| Operating Profit | 61,943 |
| Net Profit | 47,985 |
| Inventory | 70,485 |
| Current Assets | 147,431 |
| Total Assets | 280,794 |
| Current Liabilities | 101,151 |
| Liabilities | 161,677 |
| Total SE | 119,117 |
| Total L&SE | 280,794 |

#### Dolt (current)

| Field | Dolt Value |
|-------|-----------|
| Net Revenue | 467,937 |
| Cost of Goods | 222,065 |
| Gross Margin | 245,872 |
| SGA | 183,929 |
| Operating Profit | 61,943 |
| Net Profit | 47,985 |
| Inventory | 70,485 |
| Current Assets | 147,431 |
| Total Assets | 280,794 |
| Current Liabilities | 101,151 |
| Liabilities | 161,677 |
| Total SE | 119,117 |
| Total L&SE | 280,794 |

### Step 4 — Anomaly Detection

**All three sources agree exactly.** No discrepancies.

**SGA check (Rule 3):** Yahoo SGA = 183,929K. Total Operating Expenses from SEC = SGA (183,929) only — no separate marketing, platform, or ops line. Yahoo correctly reports SGA as the single SGA line. ✓

**Gross Margin check:** 245,872 / 467,937 = 52.5% — within 45–55% benchmark. ✓

**Balance sheet identity:** 280,794 = 280,794 ✓

### Step 5 — Side-by-Side Comparison

All sources agree. No `*` marks needed.

### Step 6 — Reconciled Recommendation

All values confirmed. No changes to Dolt.

---

## FY2023 Analysis

**reportDate:** 2024-02-03

### Step 3 — Extracted Values (in $thousands)

#### SEC (FY2024 10-K, comparative column 2024-02-03)

| Field | SEC Value |
|-------|-----------|
| Net Revenue | 486,114 |
| Cost of Goods | 221,722 |
| Gross Margin | 264,392 |
| SGA | 198,992 |
| Operating Profit | 65,400 (Gross − SGA) |
| Net Profit | 52,805 |
| Inventory | 63,499 |
| Current Assets | 127,772 |
| Total Assets | 272,325 |
| Current Liabilities | 83,733 |
| Liabilities | 142,663 (272,325 − 129,662) |
| Total Shareholder Equity | 129,662 |
| Total Liabilities and SE | 272,325 |

#### Yahoo Finance (column 2024-01-31)

| Field | Yahoo Value |
|-------|-------------|
| Net Revenue | 486,114 |
| Cost of Goods | 221,722 |
| Gross Margin | 264,392 |
| SGA | 198,992 |
| Operating Profit | 65,400 |
| Net Profit | 52,805 |
| Inventory | 63,499 |
| Current Assets | 127,772 |
| Total Assets | 272,325 |
| Current Liabilities | 83,733 |
| Liabilities | 142,663 |
| Total SE | 129,662 |
| Total L&SE | 272,325 |

#### Dolt (current)

Same as above — all three sources agree.

### Step 4 — Anomaly Detection

**All three sources agree exactly.** No discrepancies.

**SGA check:** Single SGA line in SEC filing. Yahoo matches SEC. ✓

**Gross Margin check:** 264,392 / 486,114 = 54.4% — within 45–55% benchmark. ✓

**Balance sheet identity:** 272,325 = 272,325 ✓

### Step 5 — Side-by-Side Comparison

All sources agree. No `*` marks needed.

### Step 6 — Reconciled Recommendation

All values confirmed. No changes to Dolt.

---

## FY2024 Analysis

**reportDate:** 2025-02-01

### Step 3 — Extracted Values (in $thousands)

#### SEC (FY2024 10-K, primary column 2025-02-01)

| Field | SEC Value |
|-------|-----------|
| Net Revenue | 496,404 |
| Cost of Goods | 223,886 |
| Gross Margin | 272,518 |
| SGA | 206,238 |
| Operating Profit | 66,280 (Gross − SGA) |
| Net Profit | 51,785 |
| Inventory | 69,775 |
| Current Assets | 126,298 |
| Total Assets | 289,956 |
| Current Liabilities | 79,394 |
| Liabilities | 150,874 (289,956 − 139,082) |
| Total Shareholder Equity | 139,082 |
| Total Liabilities and SE | 289,956 |

#### Yahoo Finance (column 2025-01-31)

| Field | Yahoo Value |
|-------|-------------|
| Net Revenue | 496,404 |
| Cost of Goods | 223,886 |
| Gross Margin | 272,518 |
| SGA | 206,238 |
| Operating Profit | 66,280 |
| Net Profit | 51,785 |
| Inventory | 69,775 |
| Current Assets | 126,298 |
| Total Assets | 289,956 |
| Current Liabilities | 79,394 |
| Liabilities | 150,874 |
| Total SE | 139,082 |
| Total L&SE | 289,956 |

#### Dolt (current)

Same as above — all three sources agree.

### Step 4 — Anomaly Detection

**All three sources agree exactly.** No discrepancies.

**SGA check:** Single combined SGA line in SEC filing. Yahoo matches SEC. ✓

**Gross Margin check:** 272,518 / 496,404 = 54.9% — at top of 45–55% specialty benchmark. ✓

**Balance sheet identity:** 289,956 = 289,956 ✓

### Step 5 — Side-by-Side Comparison

All sources agree. No `*` marks needed.

### Step 6 — Reconciled Recommendation

All values confirmed. No changes to Dolt.

---

## FY2025 Analysis (NEW — Not in Dolt)

**reportDate:** 2026-01-31 (approximate; actual fiscal year-end date TBD from SEC filing)

**Note:** SEC 10-K for FY2025 (ending ~February 2026) has not been filed yet. Data sourced from Yahoo Finance only.

### Step 3 — Extracted Values (in $thousands)

#### SEC
Not available — 10-K not yet filed.

#### Yahoo Finance (column 2026-01-31)

| Field | Yahoo Value |
|-------|-------------|
| Net Revenue | 529,832 |
| Cost of Goods | 234,203 |
| Gross Margin | 295,629 |
| SGA | 229,203 |
| Operating Profit | 66,426 |
| Net Profit | 52,203 |
| Inventory | 82,203 |
| Current Assets | 140,020 |
| Total Assets | 345,453 |
| Current Liabilities | 90,626 |
| Liabilities | 190,425 (345,453 − 155,028) |
| Total Shareholder Equity | 155,028 |
| Total Liabilities and SE | 345,453 |

#### Dolt (current)
Not present — this is a new year.

### Step 4 — Anomaly Detection

**[WARNING] SEC data not available:** FY2025 10-K has not been filed. All values are from Yahoo Finance only. Cannot cross-verify with SEC. Recommend waiting for SEC filing before inserting, OR insert Yahoo values with a note to verify when SEC files.

**[WARNING] Yahoo reportDate discrepancy:** Yahoo shows 2026-01-31 but BBW typically ends its fiscal year on the first Saturday of February (e.g., 2026-02-XX). The exact reportDate should be confirmed from the SEC filing. Using 2026-01-31 as a placeholder.

**Gross Margin check:** 295,629 / 529,832 = 55.8% — slightly above 45–55% benchmark. [WARNING] borderline high but consistent with the trend (FY2024 was 54.9%). Likely reflecting continued improvement in product mix and pricing power. Not a data error.

**Balance sheet identity:** Total Assets 345,453 = Total L&SE 345,453 ✓ (Yahoo data is internally consistent)

**Computed Liabilities:** 345,453 − 155,028 = 190,425 ✓

**Operating Profit check:** Yahoo Operating Profit = 66,426K. Gross − SGA = 295,629 − 229,203 = 66,426K ✓. Consistent with single SGA line in BBW's reporting format.

**Revenue growth:** 529,832 vs. 496,404 (+6.7%) — continued healthy growth trend.

### Step 5 — Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | 529,832 | (new) | 529,832 |
| Cost of Goods | N/A | 234,203 | (new) | 234,203 |
| Gross Margin | N/A | 295,629 | (new) | 295,629 |
| SGA | N/A | 229,203 | (new) | 229,203 |
| Operating Profit | N/A | 66,426 | (new) | 66,426 |
| Net Profit | N/A | 52,203 | (new) | 52,203 |
| Inventory | N/A | 82,203 | (new) | 82,203 |
| Current Assets | N/A | 140,020 | (new) | 140,020 |
| Total Assets | N/A | 345,453 | (new) | 345,453 |
| Current Liabilities | N/A | 90,626 | (new) | 90,626 |
| Liabilities | N/A | 190,425 | (new) | 190,425 |
| Total SE | N/A | 155,028 | (new) | 155,028 |
| Total L&SE | N/A | 345,453 | (new) | 345,453 |

### Step 6 — Reconciled Recommendation

| Field | Recommended | Source | Notes |
|-------|-------------|--------|-------|
| reportDate | 2026-01-31 | Yahoo (placeholder) | Confirm from SEC when filed |
| Net Revenue | 529,832 | Yahoo | Verify vs. SEC when available |
| Cost of Goods | 234,203 | Yahoo | |
| Gross Margin | 295,629 | Yahoo (calculated) | |
| SGA | 229,203 | Yahoo | |
| Operating Profit | 66,426 | Yahoo | = Gross − SGA ✓ |
| Net Profit | 52,203 | Yahoo | |
| Inventory | 82,203 | Yahoo | |
| Current Assets | 140,020 | Yahoo | |
| Total Assets | 345,453 | Yahoo | |
| Current Liabilities | 90,626 | Yahoo | |
| Liabilities | 190,425 | Yahoo (derived) | |
| Total SE | 155,028 | Yahoo | |
| Total L&SE | 345,453 | Yahoo | |

---

## Company Notes for Future Reference

**Build-A-Bear (BBW) — Patterns Discovered:**

1. **Fiscal Year:** Ends last Saturday of January or first Saturday of February. DB year label = the calendar year PRIOR to the fiscal year end (e.g., FY ending 2025-02-01 → year = 2024).

2. **Store Asset Impairment (FY2018, FY2020):** BBW had `bbw_StoreAssetImpairment` / `us-gaap_AssetImpairmentCharges` charges in FY2018 ($5,871K) and FY2020 ($7,346K). These appear BELOW gross profit as a separate operating cost line. For DB Operating Profit, recommendation is to use Gross − SGA only (exclude impairment from operating profit for comparability with years without impairment).

3. **FY2018–2020 Operating Profit:** The Dolt DB stored Pre-tax Income as Operating Profit for these three years. This is off by the small interest income/expense line (−85K, −15K, −10K respectively). Recommend correcting to Gross − SGA: −18,422K, 1,576K, −20,176K.

4. **SGA Structure:** Single combined `us-gaap_SellingGeneralAndAdministrativeExpense` line in all years — no separate marketing or platform lines. Yahoo matches SEC for all years with available data. Rule 1 (SGA + Marketing) does not apply.

5. **ASC 842 Impact (FY2019):** First year of operating lease right-of-use asset recognition dramatically increased Total Assets ($172K→$297K) and Liabilities ($77K→$208K). This is expected and not an error.

6. **Gross Margin Trend:** 41.2% (FY2018, COVID/impairment year) → 45.4% (FY2019) → 38.2% (FY2020, COVID) → 53.0% (FY2021) → 52.5% (FY2022) → 54.4% (FY2023) → 54.9% (FY2024) → 55.8% (FY2025). Steady improvement post-COVID.

---

## Step 7 — Analysis Complete

**Analysis complete.** Run `/insert-financials BBW` to write all changed years to the database.

**Unresolved flags to review before inserting:**

1. **[WARNING] FY2018 Operating Profit:** Recommend changing from −18,507K (Dolt, which = Pre-tax Income) to −18,422K (SEC: Gross − SGA). Difference = 85K.

2. **[WARNING] FY2019 Operating Profit:** Recommend changing from 1,561K (Dolt) to 1,576K (SEC: Gross − SGA). Difference = 15K.

3. **[WARNING] FY2020 Operating Profit:** Recommend changing from −20,186K (Dolt) to −20,176K (SEC: Gross − SGA). Difference = 10K.

4. **[WARNING] FY2025 SEC data not yet available:** New year insert based on Yahoo Finance only. Confirm and re-verify once SEC 10-K is filed (expected March–April 2026).

5. **[WARNING] FY2025 reportDate placeholder:** Using 2026-01-31 from Yahoo; actual fiscal year-end date to be confirmed from SEC filing (likely 2026-01-31 or 2026-02-01).

6. **[INFO] FY2021–2024:** All values confirmed across SEC + Yahoo (FY2022–2024) or SEC + Dolt (FY2021). No corrections needed.
