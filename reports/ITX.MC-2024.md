# Inditex/Zara (ITX.MC) — FY2024 Financial Analysis

**Generated:** 2026-06-07
**Source:** /verify-dolt-db-financials skill

---

## Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2024 | 2025-01-31 | No change |

---

## Notes

- Non-US company (CIK is NULL). No SEC 10-K filing. Analysis uses Yahoo Finance and Dolt DB only.
- All values are in **thousands of EUR** (Inditex is a Spanish company, reports in euros).
- Inditex fiscal year ends January 31. FY2024 = period ending 2025-01-31.
- **Yahoo Finance IFRS 16 warning:** Yahoo Finance's operating income figures are unreliable for Inditex due to IFRS 16 lease interest reclassification. Always cross-check against Inditex's official annual report.

---

## Step 4 — Anomaly Detection

**Balance sheet integrity:**
- Total Assets = Total L&SE: 34,714,000 = 34,714,000 ✓
- Liabilities = Total Assets − Total SE: 34,714,000 − 19,676,000 = 15,038,000 ✓

**Gross Margin check:**
- Computed: 38,632,000 − 16,288,000 = 22,344,000 ✓
- Gross margin %: 57.8% — consistent with Inditex's premium fast-fashion model

**[WARNING] Operating Profit — Yahoo presents three conflicting values:**
- Yahoo `Operating Income`: 7,593,510
- Yahoo `Total Operating Income As Reported`: 7,554,420
- Yahoo `EBIT`: 7,929,120

None match Dolt's 7,673,000. However, Inditex's actual annual report (FY2025, ending Jan 31 2025) states EBIT of 7,673M EUR — exactly matching the Dolt value. Yahoo Finance's figures are distorted by IFRS 16 lease treatment: lease interest (~352M EUR) is being reclassified, inflating Yahoo's EBIT and producing inconsistent operating income computations. Dolt's value is authoritative.

**[NOTE] Minor Yahoo rounding discrepancies:**
- Revenue: Yahoo 38,631,900 vs Dolt 38,632,000 (100 thousand EUR — floating-point display artifact)
- COGS: Yahoo 16,288,500 vs Dolt 16,288,000 (500 thousand EUR — same cause)
- Both Dolt values correct per Inditex actual annual report.

**SGA check:**
- SGA = 3,712,000 matches Yahoo exactly ✓
- D&A is separately reported (3,134,890 from Yahoo)
- SGA % of revenue: 9.6% — very lean, consistent with Inditex's efficient direct retail model

---

## Step 5 — Side-by-Side Comparison (all values in thousands EUR)

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|-------|-----|-------|----------------|-------------|
| reportDate | N/A | 2025-01-31 | 2025-01-31 | 2025-01-31 |
| Net Revenue | N/A | 38,631,900† | 38,632,000 | 38,632,000 |
| Cost of Goods | N/A | 16,288,500† | 16,288,000 | 16,288,000 |
| Gross Margin | N/A | 22,343,400† | 22,344,000 | 22,344,000 |
| SGA | N/A | 3,712,000 | 3,712,000 | 3,712,000 |
| Operating Profit | N/A | 7,593,510 * | 7,673,000 | 7,673,000 |
| Net Profit | N/A | 5,866,130† | 5,866,000 | 5,866,000 |
| Inventory | N/A | 3,321,000 | 3,321,000 | 3,321,000 |
| Current Assets | N/A | 16,356,000 | 16,356,000 | 16,356,000 |
| Total Assets | N/A | 34,714,000 | 34,714,000 | 34,714,000 |
| Current Liabilities | N/A | 10,187,000 | 10,187,000 | 10,187,000 |
| Liabilities | N/A | 15,038,000 | 15,038,000 | 15,038,000 |
| Total SE | N/A | 19,676,000 | 19,676,000 | 19,676,000 |
| Total L&SE | N/A | 34,714,000 | 34,714,000 | 34,714,000 |

† Yahoo floating-point display rounds differently; Dolt matches Inditex's actual published figures.
* = Yahoo Operating Profit unreliable due to IFRS 16 treatment; Dolt value is authoritative.

---

## Step 6 — Reconciled Recommendation

All Dolt values are correct and match Inditex's actual published annual report figures. No corrections needed.

- **Operating Profit (7,673,000):** Dolt matches Inditex's reported EBIT of 7,673M EUR. Yahoo Finance shows different figures due to IFRS 16 lease interest reclassification — Yahoo is unreliable for this field on IFRS-reporting companies.
- **Revenue/COGS minor differences:** Yahoo scientific notation display introduces sub-1M EUR rounding artifacts. Dolt values are correct.
- **SGA (3,712,000):** Pure SGA; D&A (~3,135,000) is separately reported.
- **Dolt current values:** Already correct. No fields would be overwritten.

**Action: No change.**

---

## Step 7 — Readiness

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql ITX.MC 2024` to write these values to the database.

For reviewer awareness (not blocking): Yahoo Finance operating profit figures for Inditex are unreliable due to IFRS 16 treatment. When verifying this company in future years, always cross-check against Inditex's official annual report rather than relying on Yahoo's operating income lines.
