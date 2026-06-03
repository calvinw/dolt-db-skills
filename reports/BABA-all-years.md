# Alibaba (BABA) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-03
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2019-03-31 | Correction: TSE (73,348→91,697) — balance sheet identity fix |
| 2019 | 2020-03-31 | Correction: TSE (106,683→124,231) — balance sheet identity fix |
| 2020 | 2021-03-31 | Correction: TSE (143,086→165,395) — balance sheet identity fix |
| 2021 | 2022-03-31 | Correction: TSE (149,619→170,712) — balance sheet identity fix |
| 2022 | 2023-03-31 | Correction: TSE (144,105→163,510) — balance sheet identity fix |
| 2023 | 2024-03-31 | Correction: TSE (136,635→154,093) — balance sheet identity fix |
| 2024 | 2025-03-31 | Correction: TSE (139,162→150,220) — balance sheet identity fix |
| 2025 | 2026-03-31 | New insert |

---

## Notes

- **Chinese company with US ADR:** CIK = 1577552. Files 20-F (foreign private issuer), NOT 10-K. The SEC MCP tool returned "No 10-K filings found" — SEC cross-check not available. All verification uses Yahoo Finance only.
- **Fiscal year end:** March 31 each year. Year label = calendar year of the 20-F filing (i.e., year 2018 in Dolt → FY ending March 31, 2019).
- **Currency:** Alibaba reports in RMB (CNY). All Dolt values are in thousands of USD, converted from RMB at the approximate average FX rate for each fiscal year.
- **Yahoo verification:** Revenue, COGS, gross margin %, and operating profit match Yahoo ratios closely (differences ≤1% attributable to FX rate). Net Profit shows slightly larger variation — exact FX rate and NCI treatment uncertain without 20-F.
- **Balance sheet identity [ERROR] all years:** Dolt stores TSE = Common Stock Equity (parent-only, excludes NCI). Liabilities = Total Liabilities (excludes NCI equity). These two don't sum to Total Assets — the difference is the NCI (non-controlling interest) equity, which ranges from ~$11B to ~$22B USD across years. Fix: set TSE = Total Assets − Liabilities (= Total Equity including NCI). Liabilities values are correct and unchanged.
- **Inventory:** NULL for all years — Alibaba is a marketplace/platform company, does not carry physical inventory.
- **Gross margin benchmark:** Alibaba's effective gross margin (28–40%) is above the Online/Marketplace 25–35% benchmark, consistent with its high-margin platform and cloud segments.
- **FY2025 operating profit:** 6,908K USD (down 64% from FY2024 19,417K) — reflects significant restructuring and segment spin-offs. Flag as [WARNING] — confirm against 20-F when available.
- **FY2025 FX rate:** ~7.26 RMB/USD (approximate average for April 2025–March 2026).

---

## Balance Sheet Identity Correction (all years)

The anomaly rule requires: Total Assets = Liabilities + TSE (within $1K). This currently fails for ALL BABA years. The fix for each year is:

**Corrected TSE = Total Assets − Liabilities** (Liabilities values are correct and unchanged.)

| Year | Total Assets | Liabilities (unchanged) | Old TSE | Corrected TSE |
|------|-------------|------------------------|---------|---------------|
| 2018 | 143,801,000 | 52,104,000 | 73,348,000 | **91,697,000** |
| 2019 | 185,429,000 | 61,198,000 | 106,683,000 | **124,231,000** |
| 2020 | 257,978,000 | 92,583,000 | 143,086,000 | **165,395,000** |
| 2021 | 267,467,000 | 96,755,000 | 149,619,000 | **170,712,000** |
| 2022 | 255,263,000 | 91,753,000 | 144,105,000 | **163,510,000** |
| 2023 | 244,426,000 | 90,333,000 | 136,635,000 | **154,093,000** |
| 2024 | 248,629,000 | 98,409,000 | 139,162,000 | **150,220,000** |

The corrected TSE ≈ Total Equity Gross Minority Interest (parent equity + NCI). Yahoo confirms the NCI equity for FY2022–FY2024:
- FY2022: Yahoo Total Equity Inc NCI = 1.12292e+12 RMB / 6.87 ≈ 163,451K USD (Corrected 163,510K — 59K rounding) ✓
- FY2023: Yahoo Total Equity Inc NCI = 1.1126e+12 RMB / 7.22 ≈ 154,100K USD (Corrected 154,093K — 7K rounding) ✓
- FY2024: Yahoo Total Equity Inc NCI = 1.09011e+12 RMB / 7.26 ≈ 150,152K USD (Corrected 150,220K — 68K rounding) ✓

---

## Income Statement Verification (FY2022–FY2024 via Yahoo)

All values confirmed via Yahoo ratio checks (Yahoo in RMB, Dolt in USD; implicit FX rate applied):

| Year | Dolt Revenue (K USD) | Implied FX Rate | Yahoo Revenue (RMB) | GM% Dolt | GM% Yahoo |
|------|---------------------|-----------------|---------------------|----------|----------|
| 2022 | 126,491,000 | 6.87 | 8.69e+11 | 36.7% | 36.7% ✓ |
| 2023 | 130,350,000 | 7.22 | 9.41e+11 | 37.7% | 37.7% ✓ |
| 2024 | 137,300,000 | 7.26 | 9.96e+11 | 39.9% | 39.9% ✓ |

Operating Profit confirmed: FY2023 Dolt 15,699K × 7.22 = 113,347M RMB ≈ Yahoo "Total Op Inc As Reported" 113,350M ✓

FY2018–FY2021 cannot be directly verified (Yahoo shows only 4 years; no SEC 20-F available).

---

## FY2025 New Insert

**Sources:** Yahoo Finance (column 2026-03-31). FX rate: ~7.26 RMB/USD.

### Anomaly Detection
- `[WARNING]` Operating Profit: 6,908K USD (50,150M RMB) — down 64% from FY2024 (19,417K USD). Alibaba's restructuring and segment separations may explain this. Verify against 20-F when available.
- Gross margin: ~39.8% (407,534M / 1,023,670M RMB) — consistent with prior years ✓
- Balance sheet identity: 107,890,000 + 155,135,000 = 263,025,000 ≈ Total Assets 263,028,000 ✓ (3K rounding)
- Inventory: NULL (marketplace model, no physical inventory) ✓

### Side-by-Side

| Field | SEC (20-F) | Yahoo (RMB) | Yahoo (USD @7.26) | Dolt | Recommended |
|-------|-----------|-------------|-------------------|------|-------------|
| Net Revenue | — | 1,023,670,000K RMB | 141,001,000 | — | 141,001,000 |
| Cost of Goods | — | 616,136,000K RMB | 84,866,000 | — | 84,866,000 |
| Gross Margin | — | 407,534,000K RMB | 56,135,000 | — | 56,135,000 |
| SGA | — | 278,105,000K RMB | 38,306,000 | — | 38,306,000 |
| Operating Profit | — | 50,150,000K RMB | 6,908,000 | — | 6,908,000 |
| Net Profit | — | 103,592,000K RMB | 14,269,000 | — | 14,269,000 |
| Inventory | — | — | NULL | — | NULL |
| Current Assets | — | 610,769,000K RMB | 84,128,000 | — | 84,128,000 |
| Total Assets | — | 1,909,570,000K RMB | 263,028,000 | — | 263,028,000 |
| Current Liabilities | — | 476,398,000K RMB | 65,621,000 | — | 65,621,000 |
| Liabilities | — | 783,300,000K RMB | 107,890,000 | — | 107,890,000 |
| Total SE | — | 1,126,270,000K RMB | 155,138,000 | — | 155,138,000 |
| Total L+SE | — | ~1,909,570,000K RMB | 263,028,000 | — | 263,028,000 |

*All USD values converted from RMB at ~7.26 exchange rate. Exact values depend on the 20-F (not available via SEC MCP).*

**Action: New insert.**

---

## Unresolved Flags

1. `[WARNING]` SEC 20-F not accessible via the SEC MCP tool (searches 10-K only). All verification is Yahoo-only. Recommend re-running when a 20-F-capable MCP is available.
2. `[WARNING]` FY2018–FY2021 income statements not verified from any external source.
3. `[WARNING]` Net Profit values for all years may vary depending on exact FX rate and NCI treatment definition used in original data entry.
4. `[WARNING]` FY2025 operating profit shows 64% decline — verify against 20-F when available.

**Analysis complete.** Run `/insert-financials BABA` to write all changed years to the database.
