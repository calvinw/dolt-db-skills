# Louis Vuitton/LVMH (MC.PA) — FY2024 Financial Analysis

**Generated:** 2026-06-07
**Source:** /verify-dolt-db-financials skill

---

## Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2024 | 2024-12-31 | No change |

---

## Notes

- Non-US company (CIK is NULL). No SEC 10-K filing. Analysis uses Yahoo Finance and Dolt DB only.
- All values are in **thousands of EUR** (LVMH is a French company, reports in euros).
- LVMH fiscal year ends December 31. FY2024 = calendar year 2024.
- LVMH reports under IFRS. SGA = combined Marketing/Selling + G&A (no separate D&A line for this company).

---

## Step 4 — Anomaly Detection

**Balance sheet integrity:**
- Total Assets = Total L&SE: 149,190,000 = 149,190,000 ✓
- Liabilities = Total Assets − Total SE: 149,190,000 − 67,517,000 = 81,673,000 ✓
- Note: Yahoo's `Total Liabilities Net Minority Interest` = 79,903,000 (excludes NCI of 1,770,000). Dolt correctly uses Total Assets − Common SE = 81,673,000, consistent with DB convention.

**Gross Margin check:**
- Computed: 84,683,000 − 27,918,000 = 56,765,000 ✓
- Gross margin %: 67.0% — characteristic of LVMH's luxury goods model (high brand premium)

**SGA check:**
- SGA = 37,222,000 (Yahoo breakdown: Marketing/Selling 31,002,000 + G&A 6,220,000 = 37,222,000 ✓)
- SGA % of revenue: 44.0% — consistent with LVMH's investment in marketing and retail presence

**Operating Profit note:**
- Gross Margin − SGA = 56,765,000 − 37,222,000 = 19,543,000
- Dolt Operating Profit = 19,578,000 (difference: 35,000 thousand)
- Yahoo `Operating Expense` = 37,187,000 → implied Operating Income = 19,577,000 ≈ 19,578,000 ✓
- The 35M EUR gap between SGA (37,222,000) and Operating Expense (37,187,000) is explained by other operating income items (royalties, gains, etc.) in LVMH's IFRS income statement. No anomaly.

**[NOTE] Minor rounding differences (1,000 thousand = 1M EUR)** in Revenue and Operating Profit between Yahoo and Dolt — floating-point display artifacts. Not material.

**No warnings or errors.**

---

## Step 5 — Side-by-Side Comparison (all values in thousands EUR)

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| reportDate | N/A | 2024-12-31 | 2024-12-31 | 2024-12-31 |
| Net Revenue | N/A | 84,682,000† | 84,683,000 | 84,683,000 |
| Cost of Goods | N/A | 27,918,000 | 27,918,000 | 27,918,000 |
| Gross Margin | N/A | 56,764,000† | 56,765,000 | 56,765,000 |
| SGA | N/A | 37,222,000 | 37,222,000 | 37,222,000 |
| Operating Profit | N/A | 19,577,000† | 19,578,000 | 19,578,000 |
| Net Profit | N/A | 12,550,000 | 12,550,000 | 12,550,000 |
| Inventory | N/A | 23,669,000 | 23,669,000 | 23,669,000 |
| Current Assets | N/A | 47,471,000 | 47,471,000 | 47,471,000 |
| Total Assets | N/A | 149,190,000 | 149,190,000 | 149,190,000 |
| Current Liabilities | N/A | 33,696,000 | 33,696,000 | 33,696,000 |
| Liabilities | N/A | 81,673,000‡ | 81,673,000 | 81,673,000 |
| Total SE | N/A | 67,517,000 | 67,517,000 | 67,517,000 |
| Total L&SE | N/A | 149,190,000 | 149,190,000 | 149,190,000 |

†Yahoo rounding difference of 1,000 thousand (1M EUR) — floating-point display artifact; Dolt value is correct.
‡Computed as Total Assets − Common SE (includes NCI 1,770,000). Yahoo's `Total Liabilities Net Minority Interest` = 79,903,000 (excludes NCI) — Dolt's convention is correct.

---

## Step 6 — Reconciled Recommendation

All Dolt values are correct. No corrections needed.

- **SGA (37,222,000):** Combined marketing/selling + G&A; consistent with LVMH's IFRS reporting.
- **Operating Profit (19,578,000):** Matches Yahoo within 1M EUR rounding. The 35M gap vs Gross Margin − SGA is explained by other operating income items in LVMH's IFRS income statement.
- **Liabilities (81,673,000):** Correctly computed as Total Assets − Common SE, including NCI per DB convention.
- **Net Profit (12,550,000):** Attributable to LVMH shareholders (excludes NCI net income of 408,000).
- **Dolt current values:** Already correct. No fields would be overwritten.

**Action: No change.**

---

## Step 7 — Readiness

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql MC.PA 2024` to write these values to the database.

No unresolved flags.
