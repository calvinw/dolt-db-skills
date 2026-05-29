# Alibaba (BABA) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-05-29
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2019-03-31 | No change (cannot verify — no Yahoo data for this period) |
| 2019 | 2020-03-31 | No change (cannot verify — no Yahoo data for this period) |
| 2020 | 2021-03-31 | No change (cannot verify — no Yahoo data for this period) |
| 2021 | 2022-03-31 | No change (cannot verify — no Yahoo data for this period) |
| 2022 | 2023-03-31 | No change (all fields confirmed against Yahoo) |
| 2023 | 2024-03-31 | No change (all fields confirmed against Yahoo) |
| 2024 | 2025-03-31 | No change (all fields confirmed against Yahoo) |
| 2025 | 2026-03-31 | New insert (values approximate — exchange rate ~7.27 RMB/USD estimated) |

---

## Notes

- **Chinese company with US ADR:** CIK = 1577552. Files 20-F with SEC as foreign private issuer. SEC MCP unavailable this session.
- **Fiscal year end:** March 31 each year. Dolt year labels: year N = fiscal year ending March 31 of year N+1. E.g., Dolt year 2024 = FY ending 2025-03-31.
- **Currency / unit convention:** Yahoo Finance shows Alibaba values in **absolute RMB (CNY)**. Dolt stores in **thousands of USD**, converted at the period fiscal-year-end exchange rate. Confirmed exchange rates: March 2023 ≈ 6.868, March 2024 ≈ 7.220, March 2025 ≈ 7.257. For March 2026, ~7.27 estimated.
- **Inventory:** NULL for all years — Alibaba is primarily a marketplace (Taobao, Tmall, Alibaba.com). Dolt has NULL for all existing years.
- **Balance sheet minority interest:** Alibaba has significant minority interest (~$9B+ USD). Dolt stores Liabilities = Total Liabilities Net Minority Interest and TSE = Common Stock Equity, both excluding minority interest. This means Liabilities + TSE ≠ Total Assets (by the minority interest amount). Total L+SE = Total Assets regardless.
- **Operating Profit:** Dolt uses Yahoo "Total Operating Income As Reported" (includes impairment charges), confirmed for FY2022–2024.
- **Net Profit:** Dolt uses Yahoo "Net Income" (total, before preferred dividend adjustments), confirmed for FY2022–2024.
- **FY2025 anomaly:** SGA jumped 47.7% in RMB vs 2.7% revenue growth; operating income fell ~66%. Likely reflects intensified marketing spend vs competitors (Pinduoduo, JD.com). User should verify before applying.

---

## FY2018

**Sources:** Dolt only (no Yahoo data)

### Anomaly Detection
- `[WARNING]` Cannot verify against any external source.
- Gross margin: 25,319,000 / 56,152,000 = 45.1% — above Online/Marketplace range (25–35%); Alibaba has high-margin cloud and ad revenue ✓
- Balance sheet: 52,104,000 + 73,348,000 = 125,452,000 ≠ 143,801,000 (Total Assets). Gap = 18,349,000K = minority interest. Expected per DB convention.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | — | 56,152,000 | 56,152,000 |
| Cost of Goods | N/A | — | 30,833,000 | 30,833,000 |
| Gross Margin | N/A | — | 25,319,000 | 25,319,000 |
| SGA | N/A | — | 9,636,000 | 9,636,000 |
| Operating Profit | N/A | — | 8,506,000 | 8,506,000 |
| Net Profit | N/A | — | 13,095,000 | 13,095,000 |
| Inventory | N/A | — | NULL | NULL |
| Current Assets | N/A | — | 40,272,000 | 40,272,000 |
| Total Assets | N/A | — | 143,801,000 | 143,801,000 |
| Current Liabilities | N/A | — | 30,944,000 | 30,944,000 |
| Liabilities | N/A | — | 52,104,000 | 52,104,000 |
| Total SE | N/A | — | 73,348,000 | 73,348,000 |
| Total L+SE | N/A | — | 143,801,000 | 143,801,000 |

**Action: No change.**

---

## FY2019

**Sources:** Dolt only (no Yahoo data)

### Anomaly Detection
- `[WARNING]` Cannot verify against any external source.
- Gross margin: 32,107,000 / 71,985,000 = 44.6% — above Online/Marketplace range; consistent with Alibaba's profile.
- Balance sheet: 61,198,000 + 106,683,000 = 167,881,000 ≠ 185,429,000. Gap = 17,548,000K = minority interest. Expected.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | — | 71,985,000 | 71,985,000 |
| Cost of Goods | N/A | — | 39,878,000 | 39,878,000 |
| Gross Margin | N/A | — | 32,107,000 | 32,107,000 |
| SGA | N/A | — | 11,138,000 | 11,138,000 |
| Operating Profit | N/A | — | 12,912,000 | 12,912,000 |
| Net Profit | N/A | — | 21,104,000 | 21,104,000 |
| Inventory | N/A | — | NULL | NULL |
| Current Assets | N/A | — | 65,377,000 | 65,377,000 |
| Total Assets | N/A | — | 185,429,000 | 185,429,000 |
| Current Liabilities | N/A | — | 34,159,000 | 34,159,000 |
| Liabilities | N/A | — | 61,198,000 | 61,198,000 |
| Total SE | N/A | — | 106,683,000 | 106,683,000 |
| Total L+SE | N/A | — | 185,429,000 | 185,429,000 |

**Action: No change.**

---

## FY2020

**Sources:** Dolt only (no Yahoo data)

### Anomaly Detection
- `[WARNING]` Cannot verify against any external source.
- Gross margin: 45,191,000 / 109,480,000 = 41.3% — above Online/Marketplace range; consistent.
- Balance sheet: 92,583,000 + 143,086,000 = 235,669,000 ≠ 257,978,000. Gap = 22,309,000K = minority interest. Expected.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | — | 109,480,000 | 109,480,000 |
| Cost of Goods | N/A | — | 64,289,000 | 64,289,000 |
| Gross Margin | N/A | — | 45,191,000 | 45,191,000 |
| SGA | N/A | — | 20,871,000 | 20,871,000 |
| Operating Profit | N/A | — | 13,688,000 | 13,688,000 |
| Net Profit | N/A | — | 22,983,000 | 22,983,000 |
| Inventory | N/A | — | NULL | NULL |
| Current Assets | N/A | — | 98,196,000 | 98,196,000 |
| Total Assets | N/A | — | 257,978,000 | 257,978,000 |
| Current Liabilities | N/A | — | 57,596,000 | 57,596,000 |
| Liabilities | N/A | — | 92,583,000 | 92,583,000 |
| Total SE | N/A | — | 143,086,000 | 143,086,000 |
| Total L+SE | N/A | — | 257,978,000 | 257,978,000 |

**Action: No change.**

---

## FY2021

**Sources:** Dolt only (no Yahoo data)

### Anomaly Detection
- `[WARNING]` Cannot verify against any external source.
- Gross margin: 49,471,000 / 134,567,000 = 36.7% — above Online/Marketplace range; consistent.
- Balance sheet: 96,755,000 + 149,619,000 = 246,374,000 ≠ 267,467,000. Gap = 21,093,000K = minority interest. Expected.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | — | 134,567,000 | 134,567,000 |
| Cost of Goods | N/A | — | 85,096,000 | 85,096,000 |
| Gross Margin | N/A | — | 49,471,000 | 49,471,000 |
| SGA | N/A | — | 23,934,000 | 23,934,000 |
| Operating Profit | N/A | — | 10,985,000 | 10,985,000 |
| Net Profit | N/A | — | 9,820,000 | 9,820,000 |
| Inventory | N/A | — | NULL | NULL |
| Current Assets | N/A | — | 100,726,000 | 100,726,000 |
| Total Assets | N/A | — | 267,467,000 | 267,467,000 |
| Current Liabilities | N/A | — | 60,540,000 | 60,540,000 |
| Liabilities | N/A | — | 96,755,000 | 96,755,000 |
| Total SE | N/A | — | 149,619,000 | 149,619,000 |
| Total L+SE | N/A | — | 267,467,000 | 267,467,000 |

**Action: No change.**

---

## FY2022

**Sources:** Yahoo Finance (2023-03-31 column, absolute RMB) + Dolt (thousands USD at ~6.868 RMB/USD)

### Anomaly Detection
- All 13 fields confirmed against Yahoo at implied exchange rate 6.868 RMB/USD. ✓
- Gross margin: 46,449,000 / 126,491,000 = 36.7% — above Online/Marketplace range; consistent for Alibaba ✓
- Operating Profit uses Yahoo "Total Operating Income As Reported" = 100,351M RMB / 6.868 / 1000 = 14,612,000K ✓
- Net Profit uses Yahoo "Net Income" = 72,783M RMB / 6.868 / 1000 = 10,598,000K ✓
- Balance sheet: 91,753,000 + 144,105,000 = 235,858,000 ≠ 255,263,000. Gap = 19,405,000K = minority interest. Expected per DB convention.

### Side-by-Side (Yahoo values shown in thousands USD after conversion)

| Field | SEC | Yahoo (converted) | Dolt | Recommended |
|-------|-----|-------------------|------|-------------|
| Net Revenue | N/A | 126,491,000 | 126,491,000 | 126,491,000 |
| Cost of Goods | N/A | 80,042,000 | 80,042,000 | 80,042,000 |
| Gross Margin | N/A | 46,449,000 | 46,449,000 | 46,449,000 |
| SGA | N/A | 21,212,000 | 21,212,000 | 21,212,000 |
| Operating Profit | N/A | 14,612,000 | 14,612,000 | 14,612,000 |
| Net Profit | N/A | 10,598,000 | 10,598,000 | 10,598,000 |
| Inventory | N/A | NULL | NULL | NULL |
| Current Assets | N/A | 101,629,000 | 101,632,000 | 101,632,000 |
| Total Assets | N/A | 255,247,000 | 255,263,000 | 255,263,000 |
| Current Liabilities | N/A | 56,120,000 | 56,111,000 | 56,111,000 |
| Liabilities | N/A | 91,756,000 | 91,753,000 | 91,753,000 |
| Total SE | N/A | 144,107,000 | 144,105,000 | 144,105,000 |
| Total L+SE | N/A | 255,263,000 | 255,263,000 | 255,263,000 |

**Action: No change.**

---

## FY2023

**Sources:** Yahoo Finance (2024-03-31 column, absolute RMB) + Dolt (thousands USD at ~7.220 RMB/USD)

### Anomaly Detection
- All 13 fields confirmed against Yahoo at implied exchange rate 7.220 RMB/USD. ✓
- Gross margin: 49,145,000 / 130,350,000 = 37.7% — above Online/Marketplace range; consistent ✓
- Balance sheet: 90,333,000 + 136,635,000 = 226,968,000 ≠ 244,426,000. Gap = 17,458,000K = minority interest. Expected.

### Side-by-Side (Yahoo values shown in thousands USD after conversion)

| Field | SEC | Yahoo (converted) | Dolt | Recommended |
|-------|-----|-------------------|------|-------------|
| Net Revenue | N/A | 130,350,000 | 130,350,000 | 130,350,000 |
| Cost of Goods | N/A | 81,205,000 | 81,205,000 | 81,205,000 |
| Gross Margin | N/A | 49,145,000 | 49,145,000 | 49,145,000 |
| SGA | N/A | 21,762,000 | 21,762,000 | 21,762,000 |
| Operating Profit | N/A | 15,699,000 | 15,699,000 | 15,699,000 |
| Net Profit | N/A | 11,081,000 | 11,081,000 | 11,081,000 |
| Inventory | N/A | NULL | NULL | NULL |
| Current Assets | N/A | 104,270,000 | 104,270,000 | 104,270,000 |
| Total Assets | N/A | 244,426,000 | 244,426,000 | 244,426,000 |
| Current Liabilities | N/A | 58,378,000 | 58,378,000 | 58,378,000 |
| Liabilities | N/A | 90,333,000 | 90,333,000 | 90,333,000 |
| Total SE | N/A | 136,635,000 | 136,635,000 | 136,635,000 |
| Total L+SE | N/A | 244,426,000 | 244,426,000 | 244,426,000 |

**Action: No change.**

---

## FY2024

**Sources:** Yahoo Finance (2025-03-31 column, absolute RMB) + Dolt (thousands USD at ~7.257 RMB/USD)

### Anomaly Detection
- All 13 fields confirmed against Yahoo at implied exchange rate 7.257 RMB/USD. ✓
- Gross margin: 54,854,000 / 137,300,000 = 39.9% — above Online/Marketplace range; consistent ✓
- Balance sheet: 98,409,000 + 139,162,000 = 237,571,000 ≠ 248,629,000. Gap = 11,058,000K = minority interest. Expected.

### Side-by-Side (Yahoo values shown in thousands USD after conversion)

| Field | SEC | Yahoo (converted) | Dolt | Recommended |
|-------|-----|-------------------|------|-------------|
| Net Revenue | N/A | 137,300,000 | 137,300,000 | 137,300,000 |
| Cost of Goods | N/A | 82,446,000 | 82,446,000 | 82,446,000 |
| Gross Margin | N/A | 54,854,000 | 54,854,000 | 54,854,000 |
| SGA | N/A | 25,943,000 | 25,943,000 | 25,943,000 |
| Operating Profit | N/A | 19,417,000 | 19,417,000 | 19,417,000 |
| Net Profit | N/A | 17,929,000 | 17,929,000 | 17,929,000 |
| Inventory | N/A | NULL | NULL | NULL |
| Current Assets | N/A | 92,886,000 | 92,886,000 | 92,886,000 |
| Total Assets | N/A | 248,629,000 | 248,629,000 | 248,629,000 |
| Current Liabilities | N/A | 59,992,000 | 59,992,000 | 59,992,000 |
| Liabilities | N/A | 98,409,000 | 98,409,000 | 98,409,000 |
| Total SE | N/A | 139,162,000 | 139,162,000 | 139,162,000 |
| Total L+SE | N/A | 248,629,000 | 248,629,000 | 248,629,000 |

**Action: No change.**

---

## FY2025

**Sources:** Yahoo Finance (2026-03-31 column, absolute RMB) only — new year not yet in Dolt

**Exchange rate assumption:** ~7.27 RMB/USD for March 31, 2026 (estimated). All USD values are approximate.

### Anomaly Detection
- `[WARNING]` **Exchange rate estimated.** The RMB/USD rate on 2026-03-31 is assumed ~7.27 based on prior-year trend (6.868 → 7.220 → 7.257). User should verify actual rate before applying.
- `[WARNING]` **SGA spike:** SGA = 278,105M RMB (+47.7% vs FY2024 of 188,260M RMB) despite only 2.7% revenue growth. Driven by Selling & Marketing jump (144,021M → 245,023M RMB, +70%). Likely reflects intensified competitive marketing (vs Pinduoduo, JD.com). Investigate before inserting.
- `[WARNING]` **Operating Profit sharp decline:** Total Operating Income As Reported = 50,150M RMB (-64% vs FY2024 of 140,905M RMB). Largely driven by SGA spike above.
- Gross margin: 56,057,000 / 140,807,000 = 39.8% — consistent with prior years ✓
- Balance sheet: 107,745,000 + 145,924,000 = 253,669,000 ≠ 262,664,000. Gap = 8,995,000K = minority interest. Expected per DB convention.
- Inventory: NULL (marketplace model, consistent with all prior years) ✓

### Side-by-Side (Yahoo RMB converted at ~7.27 RMB/USD)

| Field | SEC | Yahoo (converted ~7.27) | Dolt | Recommended |
|-------|-----|-------------------------|------|-------------|
| Net Revenue | N/A | 140,807,000 | — | 140,807,000 |
| Cost of Goods | N/A | 84,750,000 | — | 84,750,000 |
| Gross Margin | N/A | 56,057,000 | — | 56,057,000 |
| SGA | N/A | 38,254,000 | — | 38,254,000 |
| Operating Profit | N/A | 6,899,000 | — | 6,899,000 |
| Net Profit | N/A | 14,248,000 | — | 14,248,000 |
| Inventory | N/A | NULL | — | NULL |
| Current Assets | N/A | 84,013,000 | — | 84,013,000 |
| Total Assets | N/A | 262,664,000 | — | 262,664,000 |
| Current Liabilities | N/A | 65,530,000 | — | 65,530,000 |
| Liabilities | N/A | 107,745,000 | — | 107,745,000 |
| Total SE | N/A | 145,924,000 | — | 145,924,000 |
| Total L+SE | N/A | 262,664,000 | — | 262,664,000 |

**Action: New insert (verify exchange rate and SGA spike before applying).**

---

## Step 7 — Unresolved Flags

1. `[WARNING]` FY2018–FY2021 cannot be verified — no Yahoo data for those periods.
2. `[WARNING]` FY2025 exchange rate is estimated (~7.27 RMB/USD). Verify the actual March 31, 2026 RMB/USD rate before applying SQL.
3. `[WARNING]` FY2025 SGA spike (+47.7% YoY) and operating income collapse (-64%) are significant anomalies. Confirm this reflects actual Alibaba reporting before inserting.

**Analysis complete.** Run `/insert-financials BABA` to write all changed years to the database.
