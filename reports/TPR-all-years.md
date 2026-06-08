# Tapestry (TPR) — FY2019–FY2025 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year (Dolt) | reportDate | Fiscal Year | Action | Notes |
|---|---|---|---|---|
| 2018 | 2019-06-29 | FY2019 | Correction: SGA, Operating Profit | SGA off by $5,600K vs SEC; Operating Profit off by -$5,600K |
| 2019 | 2020-06-27 | FY2020 | No change | All sources agree |
| 2020 | 2021-07-03 | FY2021 | No change | All sources agree |
| 2021 | 2022-07-02 | FY2022 | No change | All sources agree |
| 2022 | 2023-07-01 | FY2023 | No change | All sources agree |
| 2023 | 2024-06-29 | FY2024 | No change | All sources agree |
| 2024 | 2025-06-28 | FY2025 | New insert | New year not in Dolt |

---

## Year 2018 (reportDate 2019-06-29) — FY2019

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|---|---|---|---|---|
| Net Revenue | 6,027,100 | — | 6,027,100 | 6,027,100 |
| Cost of Goods | 1,973,400 | — | 1,973,400 | 1,973,400 |
| Gross Margin | 4,053,700 | — | 4,053,700 | 4,053,700 |
| SGA | **3,234,000** | — | **3,239,600*** | **3,234,000** |
| Operating Profit | **819,700** | — | **814,100*** | **819,700** |
| Net Profit | 643,400 | — | 643,400 | 643,400 |
| Inventory | — | — | 778,300 | 778,300 |
| Current Assets | — | — | 2,556,800 | 2,556,800 |
| Total Assets | — | — | 6,877,300 | 6,877,300 |
| Current Liabilities | — | — | 918,000 | 918,000 |
| Liabilities | — | — | 3,363,900 | 3,363,900 |
| Total Shareholder Equity | — | — | 3,513,400 | 3,513,400 |
| Total Liabilities and SE | — | — | 6,877,300 | 6,877,300 |

*Marked with `*` where Dolt disagrees with SEC.*

### Anomaly Detection

- **[WARNING] SGA discrepancy:** SEC reports SGA of $3,234,000K for FY2019 (from `OtherSellingGeneralAndAdministrativeExpense`), but Dolt stores $3,239,600K — a difference of $5,600K. Operating Profit is correspondingly off by -$5,600K (SEC: $819,700K, Dolt: $814,100K). This is a small error, possibly from an earlier extraction using a different source. Recommend using SEC values.
- **[WARNING] Gross Margin:** 67.3% — above the 35–55% range for specialty retail. This is expected for luxury accessories (Coach, Kate Spade), which typically command 60–75% gross margins. No action needed.
- **Balance sheet identity:** Total Assets ($6,877,300K) = Total Liabilities + SE ($6,877,300K) ✓
- **Derived:** Gross Margin = 6,027,100 − 1,973,400 = 4,053,700 ✓
- **Derived:** Liabilities = 6,877,300 − 3,513,400 = 3,363,900 ✓

### Recommendation

Correct SGA to $3,234,000K and Operating Profit to $819,700K to match SEC filing. All other values are consistent.

---

## Year 2019 (reportDate 2020-06-27) — FY2020

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|---|---|---|---|---|
| Net Revenue | 4,961,400 | — | 4,961,400 | 4,961,400 |
| Cost of Goods | 1,722,100 | — | 1,722,100 | 1,722,100 |
| Gross Margin | 3,239,300 | — | 3,239,300 | 3,239,300 |
| SGA | 3,312,400 | — | 3,312,400 | 3,312,400 |
| Operating Profit | -550,800 | — | -550,800 | -550,800 |
| Net Profit | -652,100 | — | -652,100 | -652,100 |
| Inventory | — | — | 736,900 | 736,900 |
| Current Assets | 2,553,100 | — | 2,553,100 | 2,553,100 |
| Total Assets | 7,924,200 | — | 7,924,200 | 7,924,200 |
| Current Liabilities | 1,742,100 | — | 1,742,100 | 1,742,100 |
| Liabilities | 5,647,800 | — | 5,647,800 | 5,647,800 |
| Total Shareholder Equity | 2,276,400 | — | 2,276,400 | 2,276,400 |
| Total Liabilities and SE | 7,924,200 | — | 7,924,200 | 7,924,200 |

### Anomaly Detection

- **[WARNING] Gross Margin:** 65.3% — above specialty range; expected for luxury. No action.
- **[WARNING] Negative Net Profit:** FY2020 was impacted by COVID-19 ($652.1M loss). Valid.
- **[WARNING] Goodwill impairment:** SEC filing shows $477,700K impairment in FY2020. This contributed to the loss. Not reflected in SGA or Operating Profit — it is a separate line below operating income.
- **Balance sheet identity:** Total Assets ($7,924,200K) = Total Liabilities + SE ($7,924,200K) ✓
- **Derived:** Gross Margin = 4,961,400 − 1,722,100 = 3,239,300 ✓
- **Derived:** Liabilities = 7,924,200 − 2,276,400 = 5,647,800 ✓

### Recommendation

All values consistent across SEC and Dolt. No changes needed.

---

## Year 2020 (reportDate 2021-07-03) — FY2021

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|---|---|---|---|---|
| Net Revenue | 5,746,300 | — | 5,746,300 | 5,746,300 |
| Cost of Goods | 1,664,400 | — | 1,664,400 | 1,664,400 |
| Gross Margin | 4,081,900 | — | 4,081,900 | 4,081,900 |
| SGA | 3,113,900 | — | 3,113,900 | 3,113,900 |
| Operating Profit | 968,000 | — | 968,000 | 968,000 |
| Net Profit | 834,200 | — | 834,200 | 834,200 |
| Inventory | — | — | 734,800 | 734,800 |
| Current Assets | — | — | 3,375,300 | 3,375,300 |
| Total Assets | — | — | 8,382,400 | 8,382,400 |
| Current Liabilities | — | — | 1,425,800 | 1,425,800 |
| Liabilities | — | — | 5,123,100 | 5,123,100 |
| Total Shareholder Equity | — | — | 3,259,300 | 3,259,300 |
| Total Liabilities and SE | — | — | 8,382,400 | 8,382,400 |

### Anomaly Detection

- **[WARNING] Gross Margin:** 71.0% — high but expected for luxury.
- **Balance sheet identity:** Total Assets ($8,382,400K) = Total Liabilities + SE ($8,382,400K) ✓
- **Derived:** Gross Margin = 5,746,300 − 1,664,400 = 4,081,900 ✓
- **Derived:** Liabilities = 8,382,400 − 3,259,300 = 5,123,100 ✓

### Recommendation

All values match. No changes needed.

---

## Year 2021 (reportDate 2022-07-02) — FY2022

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|---|---|---|---|---|
| Net Revenue | 6,684,500 | 6,684,500 | 6,684,500 | 6,684,500 |
| Cost of Goods | 2,034,100 | 2,034,100 | 2,034,100 | 2,034,100 |
| Gross Margin | 4,650,400 | 4,650,400 | 4,650,400 | 4,650,400 |
| SGA | 3,474,600 | 3,474,600 | 3,474,600 | 3,474,600 |
| Operating Profit | 1,175,800 | 1,175,800 | 1,175,800 | 1,175,800 |
| Net Profit | 856,300 | 856,300 | 856,300 | 856,300 |
| Inventory | — | 994,200 | 994,200 | 994,200 |
| Current Assets | 2,573,800 | 2,573,800 | 2,573,800 | 2,573,800 |
| Total Assets | 7,265,300 | 7,265,300 | 7,265,300 | 7,265,300 |
| Current Liabilities | 1,468,800 | 1,468,800 | 1,468,800 | 1,468,800 |
| Liabilities | 4,979,800 | 4,979,800 | 4,979,800 | 4,979,800 |
| Total Shareholder Equity | 2,285,500 | 2,285,500 | 2,285,500 | 2,285,500 |
| Total Liabilities and SE | 7,265,300 | 7,265,300 | 7,265,300 | 7,265,300 |

### Anomaly Detection

- **[WARNING] Gross Margin:** 69.6% — high but expected for luxury.
- **Balance sheet identity:** Total Assets ($7,265,300K) = Total Liabilities + SE ($7,265,300K) ✓
- **Derived:** Gross Margin = 6,684,500 − 2,034,100 = 4,650,400 ✓
- **Derived:** Liabilities = 7,265,300 − 2,285,500 = 4,979,800 ✓
- **SGA Rule 3 check:** Yahoo SGA ($3,474,600K) vs SEC SGA ($3,474,600K) — identical, no issue.

### Recommendation

All values consistent across SEC, Yahoo, and Dolt. No changes needed.

---

## Year 2022 (reportDate 2023-07-01) — FY2023

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|---|---|---|---|---|
| Net Revenue | 6,660,900 | 6,660,900 | 6,660,900 | 6,660,900 |
| Cost of Goods | 1,946,000 | 1,946,000 | 1,946,000 | 1,946,000 |
| Gross Margin | 4,714,900 | 4,714,900 | 4,714,900 | 4,714,900 |
| SGA | 3,542,500 | 3,542,500 | 3,542,500 | 3,542,500 |
| Operating Profit | 1,172,400 | 1,172,400 | 1,172,400 | 1,172,400 |
| Net Profit | 936,000 | 936,000 | 936,000 | 936,000 |
| Inventory | — | 919,500 | 919,500 | 919,500 |
| Current Assets | — | 2,363,500 | 2,363,500 | 2,363,500 |
| Total Assets | — | 7,116,800 | 7,116,800 | 7,116,800 |
| Current Liabilities | — | 1,286,500 | 1,286,500 | 1,286,500 |
| Liabilities | — | 4,839,000 | 4,839,000 | 4,839,000 |
| Total Shareholder Equity | — | 2,277,800 | 2,277,800 | 2,277,800 |
| Total Liabilities and SE | — | 7,116,800 | 7,116,800 | 7,116,800 |

### Anomaly Detection

- **[WARNING] Gross Margin:** 70.8% — high but expected for luxury.
- **Balance sheet identity:** Total Assets ($7,116,800K) = Total Liabilities + SE ($7,116,800K) ✓
- **Derived:** Gross Margin = 6,660,900 − 1,946,000 = 4,714,900 ✓
- **SGA Rule 3 check:** Yahoo SGA ($3,542,500K) vs SEC SGA ($3,542,500K) — match.

### Recommendation

All values consistent across SEC, Yahoo, and Dolt. No changes needed.

---

## Year 2023 (reportDate 2024-06-29) — FY2024

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|---|---|---|---|---|
| Net Revenue | 6,671,200 | 6,671,200 | 6,671,200 | 6,671,200 |
| Cost of Goods | 1,781,700 | 1,781,700 | 1,781,700 | 1,781,700 |
| Gross Margin | 4,889,500 | 4,889,500 | 4,889,500 | 4,889,500 |
| SGA | 3,749,400 | 3,749,400 | 3,749,400 | 3,749,400 |
| Operating Profit | 1,140,100 | 1,140,100 | 1,140,100 | 1,140,100 |
| Net Profit | 816,000 | 816,000 | 816,000 | 816,000 |
| Inventory | — | 824,800 | 824,800 | 824,800 |
| Current Assets | — | 8,803,700 | 8,803,700 | 8,803,700 |
| Total Assets | — | 13,396,300 | 13,396,300 | 13,396,300 |
| Current Liabilities | — | 1,711,600 | 1,711,600 | 1,711,600 |
| Liabilities | — | 10,499,400 | 10,499,400 | 10,499,400 |
| Total Shareholder Equity | — | 2,896,900 | 2,896,900 | 2,896,900 |
| Total Liabilities and SE | — | 13,396,300 | 13,396,300 | 13,396,300 |

### Anomaly Detection

- **[WARNING] Gross Margin:** 73.3% — high but expected for luxury.
- **[WARNING] Large balance sheet expansion:** Total Assets nearly doubled from $7,116,800K (FY2023) to $13,396,300K (FY2024), driven by a significant debt increase (Long-term debt from $1,636M to $6,937M, total debt from $3,292M to $8,765M). This is related to Tapestry's financing for the proposed Capri Holdings acquisition (announced August 2023, later blocked). Valid — not a data error.
- **Balance sheet identity:** Total Assets ($13,396,300K) = Total Liabilities + SE ($13,396,300K) ✓
- **Derived:** Gross Margin = 6,671,200 − 1,781,700 = 4,889,500 ✓
- **Derived:** Liabilities = 13,396,300 − 2,896,900 = 10,499,400 ✓

### Recommendation

All values consistent. No changes needed.

---

## Year 2024 (reportDate 2025-06-28) — FY2025 (NEW)

### Side-by-Side Comparison

| Field | SEC | Yahoo | Dolt (current) | Recommended |
|---|---|---|---|---|
| Net Revenue | 7,010,700 | 7,010,700 | — | 7,010,700 |
| Cost of Goods | 1,721,800 | 1,721,800 | — | 1,721,800 |
| Gross Margin | 5,288,900 | 5,288,900 | — | 5,288,900 |
| SGA | 4,019,100 | 4,019,100 | — | 4,019,100 |
| Operating Profit | **415,000** | **415,000** | — | **415,000** |
| Net Profit | 183,200 | 183,200 | — | 183,200 |
| Inventory | 860,700 | 860,700 | — | 860,700 |
| Current Assets | 2,905,600 | 2,905,600 | — | 2,905,600 |
| Total Assets | 6,580,500 | 6,580,500 | — | 6,580,500 |
| Current Liabilities | 1,556,900 | 1,556,900 | — | 1,556,900 |
| Liabilities | 5,722,700 | 5,722,700 | — | 5,722,700 |
| Total Shareholder Equity | **857,800** | **857,800** | — | **857,800** |
| Total Liabilities and SE | 6,580,500 | 6,580,500 | — | 6,580,500 |

### Anomaly Detection

- **[WARNING] Gross Margin:** 75.4% — at the high end but continues Tapestry's trend.
- **[WARNING] Large goodwill impairment:** SEC/Yahoo show $854,800K impairment of goodwill and intangible assets in FY2025. This reduced Operating Profit from ~$1,269,800K (before impairment) to $415,000K (after). Related to the terminated Capri Holdings acquisition.
- **[WARNING] Negative retained earnings:** Retained Earnings are -$2,556,800K (vs -$722,200K in FY2024). The large impairment is the primary driver.
- **[WARNING] Significant shareholder equity drop:** SE dropped from $2,896,900K (FY2024) to $857,800K (FY2025) — a 70% decline driven by the impairment and retained earnings impact.
- **[WARNING] Reduction in total assets:** Total Assets dropped from $13,396,300K (FY2024) to $6,580,500K (FY2025), as the Capri acquisition funds were redeployed/returned.
- **Balance sheet identity:** Total Assets ($6,580,500K) = Total Liabilities + SE ($6,580,500K) ✓
- **Derived:** Gross Margin = 7,010,700 − 1,721,800 = 5,288,900 ✓
- **Derived:** Liabilities = 6,580,500 − 857,800 = 5,722,700 ✓

### Recommendation

Insert as new year (Dolt year = 2024). SEC and Yahoo are fully aligned. Use the values above.

---

## SGA Composite Analysis

Tapestry reports `us-gaap_SellingGeneralAndAdministrativeExpense` as a single combined line item in the most recent SEC filing. There is no separate marketing expense or operations/tech expense line. The earlier filings use `us-gaap_OtherSellingGeneralAndAdministrativeExpense` (functionally equivalent).

- **Rule 1 (SGA + Marketing):** Not triggered — no separate marketing line.
- **Rule 2 (Exclude platform/ops-tech):** Not triggered — Tapestry is a traditional retailer, not a marketplace.
- **Rule 3 (Yahoo SGA = Total OpEx):** Not triggered — Yahoo SGA values match SEC values for all years where both are available.
- **Rule 4 (G&A + Selling):** Not triggered — combined SGA tag exists.

**Conclusion:** No composite SGA adjustments needed for Tapestry. SEC SGA values should be used directly.

---

## Company Notes Check

No specific notes for Tapestry in `company-notes.md`. Segment: Specialty → Luxury Accessories. Gross margins of 65–75% are normal for this segment.

---

## Unresolved Flags

1. **Year 2018 (FY2019):** SGA off by $5,600K vs SEC ($3,234,000K vs $3,239,600K). Recommend correction.

---

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql TPR` to write all changed/new years to SQL files.
