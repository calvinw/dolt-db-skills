# H&M (HM-B.ST) — FY2024 Financial Analysis

**Generated:** 2026-06-07
**Source:** /verify-dolt-db-financials skill

---

## Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2024 | 2024-11-30 | No change |

---

## Notes

- Non-US company (CIK is NULL). No SEC 10-K filing. Analysis uses Yahoo Finance and Dolt DB only.
- All values are in **thousands of SEK** (Swedish Kronor). H&M reports in its local currency.
- H&M fiscal year ends November 30. FY2024 = period ending 2024-11-30.

---

## Step 4 — Anomaly Detection

**Balance sheet integrity:**
- Total Assets = Total L&SE: 180,214,000 = 180,214,000 ✓
- Liabilities = Total Assets − Total SE: 180,214,000 − 46,142,000 = 134,072,000 ✓
- Note: Yahoo's `Total Liabilities Net Minority Interest` = 134,003,000 excludes minority interest (69,000); DB uses Total Assets − Common Stock Equity = 134,072,000 ✓

**Gross Margin check:**
- Computed: 234,478,000 − 109,179,000 = 125,299,000 ✓
- Gross margin %: 53.4% — characteristic of H&M's fast-fashion own-brand model

**Operating Profit reconciliation:**
- Gross Profit − Operating Expenses = 125,299,000 − 107,915,000 = 17,384,000 ✓
- SGA (87,970,000) + D&A (19,945,000) = 107,915,000 ✓
- SGA is pure SGA, D&A is separately reported — no composite issue

**No warnings or errors.**

---

## Step 5 — Side-by-Side Comparison (all values in thousands SEK)

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| reportDate | N/A | 2024-11-30 | 2024-11-30 | 2024-11-30 |
| Net Revenue | N/A | 234,478,000 | 234,478,000 | 234,478,000 |
| Cost of Goods | N/A | 109,179,000 | 109,179,000 | 109,179,000 |
| Gross Margin | N/A | 125,299,000 | 125,299,000 | 125,299,000 |
| SGA | N/A | 87,970,000 | 87,970,000 | 87,970,000 |
| Operating Profit | N/A | 17,384,000 | 17,384,000 | 17,384,000 |
| Net Profit | N/A | 11,621,000 | 11,621,000 | 11,621,000 |
| Inventory | N/A | 40,348,000 | 40,348,000 | 40,348,000 |
| Current Assets | N/A | 75,727,000 | 75,727,000 | 75,727,000 |
| Total Assets | N/A | 180,214,000 | 180,214,000 | 180,214,000 |
| Current Liabilities | N/A | 66,650,000 | 66,650,000 | 66,650,000 |
| Liabilities | N/A | 134,072,000† | 134,072,000 | 134,072,000 |
| Total SE | N/A | 46,142,000 | 46,142,000 | 46,142,000 |
| Total L&SE | N/A | 180,214,000 | 180,214,000 | 180,214,000 |

†Computed as Total Assets − Common Stock Equity (excludes minority interest of 69,000 per DB convention).

---

## Step 6 — Reconciled Recommendation

All 13 fields and reportDate are **identical between Yahoo and the current Dolt row**. No corrections are needed.

- **SGA (87,970,000):** Pure SGA from Yahoo `Selling General And Administration`. D&A (19,945,000) is separately reported. No composite adjustment needed.
- **Liabilities:** Correctly uses Total Assets − Total SE = 134,072,000.
- **Dolt current values:** Already correct. No fields would be overwritten.

**Action: No change.**

---

## Step 7 — Readiness

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql HM-B.ST 2024` to write these values to the database.

No unresolved flags.
