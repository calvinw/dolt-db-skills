# American Eagle (AEO) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-03
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|-----------|--------|
| 2018 | 2019-02-02 | No change (unverified — pre-ASC 842; balance sheet identity passes) |
| 2019 | 2020-02-01 | No change (unverified — ASC 842 adoption year; balance sheet identity passes) |
| 2020 | 2021-01-30 | No change (income stmt confirmed by SEC; balance sheet unverified, identity passes) |
| 2021 | 2022-01-29 | No change (income stmt confirmed by SEC; balance sheet unverified, identity passes) |
| 2022 | 2023-01-28 | No change (all fields confirmed vs SEC + Yahoo) |
| 2023 | 2024-02-03 | No change (all fields confirmed vs SEC + Yahoo) |
| 2024 | 2025-02-01 | Correction: reportDate (2025-02-03→2025-02-01) |
| 2025 | 2026-01-31 | New insert |

---

## Notes

- **US company:** CIK = 919012. SEC 10-K filings fetched for FY2022 (covers FY2020–FY2022), FY2023, FY2024, FY2025.
- **Fiscal year end:** Late January / early February. Year label = calendar year majority of fiscal year falls in.
- **Currency:** All values in $thousands (USD).
- **Segment:** Specialty apparel (American Eagle + Aerie). Gross margins 35–40% — within Specialty benchmark (35–55%).
- **SGA:** Single `us-gaap_SellingGeneralAndAdministrativeExpense` line — no composite construction needed. Yahoo matches SEC exactly. Restructuring charges (`aeo_ImpairmentRestructuringAndOtherCharges`) and D&A are separate lines — not included in SGA.
- **NCI (Minority Interest):** FY2025 SEC filing shows AEO has minority interest. NCI had a loss of $6.461M in FY2025, so the parent's (AEO shareholders') net income (191,983K) is HIGHER than total consolidated net income (185,522K). This is correct. Prior years had no material NCI.
- **FY2024 reportDate:** SEC 10-K period header = 2025-02-01; Dolt has 2025-02-03. Correcting.
- **FY2018 balance sheet:** Pre-ASC 842 (no operating lease ROU assets on balance sheet). Total assets ~$1.9B. Identity: 615,823 + 1,287,555 = 1,903,378 ✓
- **FY2019 balance sheet:** ASC 842 adoption year — ROU assets added ($1.3B+), causing total assets to jump to $3.3B. Not directly verified from SEC. Identity: 2,080,826 + 1,247,853 = 3,328,679 ✓
- **FY2020–FY2021 balance sheets:** Not confirmed from SEC (FY2020/FY2021 10-Ks not fetched). Both pass identity checks.
- **FY2025 TSE:** Uses parent-only Stockholders' Equity (1,693,153K), consistent with prior years. Total Equity Gross Minority Interest = 1,691,434K (includes -1,719K minority interest).

---

## FY2018

**Sources:** Dolt only (no SEC/Yahoo). Pre-ASC 842.

### Anomaly Detection
- `[WARNING]` Cannot verify income statement or balance sheet.
- `[WARNING]` Balance sheet is pre-ASC 842 (no operating lease ROU assets). Significantly different structure from FY2019+.
- Gross margin: 1,487,638 / 4,035,720 = 36.9% — within Specialty benchmark ✓
- Balance sheet: 615,823 + 1,287,555 = 1,903,378 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | — | 4,035,720 | 4,035,720 |
| Cost of Goods | — | — | 2,548,082 | 2,548,082 |
| Gross Margin | — | — | 1,487,638 | 1,487,638 |
| SGA | — | — | 980,610 | 980,610 |
| Operating Profit | — | — | 337,129 | 337,129 |
| Net Profit | — | — | 261,902 | 261,902 |
| Inventory | — | — | 424,404 | 424,404 |
| Current Assets | — | — | 1,046,253 | 1,046,253 |
| Total Assets | — | — | 1,903,378 | 1,903,378 |
| Current Liabilities | — | — | 542,645 | 542,645 |
| Liabilities | — | — | 615,823 | 615,823 |
| Total SE | — | — | 1,287,555 | 1,287,555 |
| Total L+SE | — | — | 1,903,378 | 1,903,378 |

**Action: No change.**

---

## FY2019

**Sources:** Dolt only (no SEC/Yahoo). ASC 842 adoption year.

### Anomaly Detection
- `[WARNING]` Cannot verify income statement or balance sheet from external source.
- `[WARNING]` Total assets jumped from 1,903,378K (FY2018) to 3,328,679K (FY2019) — consistent with ASC 842 adoption adding operating lease ROU assets (~$1.3B). Not an anomaly.
- Gross margin: 1,522,301 / 4,308,212 = 35.3% — within Specialty benchmark ✓
- Balance sheet: 2,080,826 + 1,247,853 = 3,328,679 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | — | — | 4,308,212 | 4,308,212 |
| Cost of Goods | — | — | 2,785,911 | 2,785,911 |
| Gross Margin | — | — | 1,522,301 | 1,522,301 |
| SGA | — | — | 1,029,412 | 1,029,412 |
| Operating Profit | — | — | 233,345 | 233,345 |
| Net Profit | — | — | 191,257 | 191,257 |
| Inventory | — | — | 446,278 | 446,278 |
| Current Assets | — | — | 1,047,930 | 1,047,930 |
| Total Assets | — | — | 3,328,679 | 3,328,679 |
| Current Liabilities | — | — | 751,756 | 751,756 |
| Liabilities | — | — | 2,080,826 | 2,080,826 |
| Total SE | — | — | 1,247,853 | 1,247,853 |
| Total L+SE | — | — | 3,328,679 | 3,328,679 |

**Action: No change.**

---

## FY2020

**Sources:** Dolt + SEC comparative (FY2022 10-K, column 2021-01-30). Balance sheet unverified.

### Anomaly Detection
- Income statement confirmed by SEC comparative — all values match ✓
- `[WARNING]` Balance sheet not confirmed from SEC. Identity: 2,348,141 + 1,086,665 = 3,434,806 ✓
- Gross margin: 1,148,147 / 3,759,113 = 30.5% — below Specialty benchmark; COVID year (store closures, clearance) ✓
- Operating Profit: -271,345K (loss) — COVID year ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 3,759,113 | — | 3,759,113 | 3,759,113 |
| Cost of Goods | 2,610,966 | — | 2,610,966 | 2,610,966 |
| Gross Margin | 1,148,147 | — | 1,148,147 | 1,148,147 |
| SGA | 977,264 | — | 977,264 | 977,264 |
| Operating Profit | -271,345 | — | -271,345 | -271,345 |
| Net Profit | -209,274 | — | -209,274 | -209,274 |
| Inventory | — | — | 405,445 | 405,445 |
| Current Assets | — | — | 1,522,643 | 1,522,643 |
| Total Assets | — | — | 3,434,806 | 3,434,806 |
| Current Liabilities | — | — | 858,482 | 858,482 |
| Liabilities | — | — | 2,348,141 | 2,348,141 |
| Total SE | — | — | 1,086,665 | 1,086,665 |
| Total L+SE | — | — | 3,434,806 | 3,434,806 |

**Action: No change.**

---

## FY2021

**Sources:** Dolt + SEC comparative (FY2022 10-K, column 2022-01-29). Balance sheet unverified.

### Anomaly Detection
- Income statement confirmed by SEC comparative — all values match ✓
- `[WARNING]` Balance sheet not confirmed from SEC. Identity: 2,362,971 + 1,423,672 = 3,786,643 ✓
- Gross margin: 1,991,790 / 5,010,785 = 39.7% — within Specialty benchmark ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 5,010,785 | — | 5,010,785 | 5,010,785 |
| Cost of Goods | 3,018,995 | — | 3,018,995 | 3,018,995 |
| Gross Margin | 1,991,790 | — | 1,991,790 | 1,991,790 |
| SGA | 1,222,000 | — | 1,222,000 | 1,222,000 |
| Operating Profit | 591,065 | — | 591,065 | 591,065 |
| Net Profit | 419,629 | — | 419,629 | 419,629 |
| Inventory | — | — | 553,458 | 553,458 |
| Current Assets | — | — | 1,396,924 | 1,396,924 |
| Total Assets | — | — | 3,786,643 | 3,786,643 |
| Current Liabilities | — | — | 842,871 | 842,871 |
| Liabilities | — | — | 2,362,971 | 2,362,971 |
| Total SE | — | — | 1,423,672 | 1,423,672 |
| Total L+SE | — | — | 3,786,643 | 3,786,643 |

**Action: No change.**

---

## FY2022

**Sources:** Dolt + SEC (FY2022 10-K, leftmost column 2023-01-28) + Yahoo (column 2023-01-31).

### Anomaly Detection
- All income statement fields confirmed: SEC ≈ Dolt ≈ Yahoo (minor ≤5K precision differences in COGS and SGA due to SEC extractor rounding; Dolt values are more precise and match Yahoo).
- All balance sheet fields confirmed: SEC = Dolt ✓
- Gross margin: 1,745,248 / 4,989,833 = 35.0% — at lower edge of Specialty benchmark ✓
- Balance sheet: 1,821,793 + 1,599,163 = 3,420,956 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | ~4,989,830 | 4,989,830 | 4,989,833 | 4,989,833 |
| Cost of Goods | ~3,244,580 | 3,244,580 | 3,244,585 | 3,244,585 |
| Gross Margin | ~1,745,250 | 1,745,250 | 1,745,248 | 1,745,248 |
| SGA | ~1,269,100 | 1,269,100 | 1,269,095 | 1,269,095 |
| Operating Profit | 247,047 | 247,047 | 247,047 | 247,047 |
| Net Profit | 125,136 | 125,136 | 125,136 | 125,136 |
| Inventory | 585,083 | 585,083 | 585,083 | 585,083 |
| Current Assets | 1,100,241 | 1,100,241 | 1,100,241 | 1,100,241 |
| Total Assets | 3,420,956 | 3,420,956 | 3,420,956 | 3,420,956 |
| Current Liabilities | 768,948 | 768,948 | 768,948 | 768,948 |
| Liabilities | 1,821,793 | 1,821,793 | 1,821,793 | 1,821,793 |
| Total SE | 1,599,163 | 1,599,163 | 1,599,163 | 1,599,163 |
| Total L+SE | 3,420,956 | 3,420,956 | 3,420,956 | 3,420,956 |

**Action: No change.**

---

## FY2023

**Sources:** Dolt + SEC (FY2023 10-K, leftmost column 2024-02-03) + Yahoo (column 2024-01-31).

### Anomaly Detection
- All income statement fields confirmed ✓ (minor ≤2K precision differences; Dolt values are more precise)
- All balance sheet fields confirmed ✓
- Gross margin: 2,024,578 / 5,261,770 = 38.5% — within Specialty benchmark ✓
- Balance sheet: 1,821,150 + 1,736,759 = 3,557,909 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 5,261,770 | 5,261,770 | 5,261,770 | 5,261,770 |
| Cost of Goods | ~3,237,190 | 3,237,190 | 3,237,192 | 3,237,192 |
| Gross Margin | ~2,024,580 | 2,024,580 | 2,024,578 | 2,024,578 |
| SGA | 1,433,300 | 1,433,300 | 1,433,300 | 1,433,300 |
| Operating Profit | 222,717 | 222,717 | 222,717 | 222,717 |
| Net Profit | 170,038 | 170,038 | 170,038 | 170,038 |
| Inventory | 640,662 | 640,662 | 640,662 | 640,662 |
| Current Assets | 1,433,350 | 1,433,350 | 1,433,350 | 1,433,350 |
| Total Assets | 3,557,909 | 3,557,909 | 3,557,909 | 3,557,909 |
| Current Liabilities | 891,172 | 891,172 | 891,172 | 891,172 |
| Liabilities | 1,821,150 | 1,821,150 | 1,821,150 | 1,821,150 |
| Total SE | 1,736,759 | 1,736,759 | 1,736,759 | 1,736,759 |
| Total L+SE | 3,557,909 | 3,557,909 | 3,557,909 | 3,557,909 |

**Action: No change.**

---

## FY2024

**Sources:** Dolt + SEC (FY2024 10-K, leftmost column 2025-02-01) + Yahoo (column 2025-01-31).

### Anomaly Detection
- `[WARNING]` reportDate: Dolt has 2025-02-03; SEC 10-K header = 2025-02-01. Correcting.
- All financial fields confirmed: SEC = Dolt = Yahoo ✓
- Gross margin: 2,088,930 / 5,328,650 = 39.2% — within Specialty benchmark ✓
- Balance sheet: 2,063,915 + 1,766,860 = 3,830,775 = Total Assets ✓

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| reportDate | **2025-02-01*** | 2025-01-31 | 2025-02-03* | **2025-02-01** |
| Net Revenue | ~5,328,652 | 5,328,650 | 5,328,650 | 5,328,650 |
| Cost of Goods | 3,239,720 | 3,239,720 | 3,239,720 | 3,239,720 |
| Gross Margin | 2,088,930 | 2,088,930 | 2,088,930 | 2,088,930 |
| SGA | 1,431,810 | 1,431,810 | 1,431,810 | 1,431,810 |
| Operating Profit | 427,303 | 427,303 | 427,303 | 427,303 |
| Net Profit | 329,380 | 329,380 | 329,380 | 329,380 |
| Inventory | 636,655 | 636,655 | 636,655 | 636,655 |
| Current Assets | 1,354,231 | 1,354,231 | 1,354,231 | 1,354,231 |
| Total Assets | 3,830,775 | 3,830,775 | 3,830,775 | 3,830,775 |
| Current Liabilities | 882,656 | 882,656 | 882,656 | 882,656 |
| Liabilities | 2,063,915 | 2,063,915 | 2,063,915 | 2,063,915 |
| Total SE | 1,766,860 | 1,766,860 | 1,766,860 | 1,766,860 |
| Total L+SE | 3,830,775 | 3,830,775 | 3,830,775 | 3,830,775 |

**Action: Correction — reportDate only. All financial values confirmed.**

---

## FY2025

**Sources:** SEC (FY2025 10-K, leftmost column 2026-01-31) + Yahoo (column 2026-01-31). New insert.

### Anomaly Detection
- All fields confirmed: SEC = Yahoo ✓
- Gross margin: 2,025,321 / 5,547,236 = 36.5% — within Specialty benchmark ✓
- Balance sheet: 2,316,527 + 1,693,153 = 4,009,680 = Total Assets ✓
- NCI: AEO has minority interest in a subsidiary. The subsidiary had a loss of $6.461M in FY2025. Parent's (AEO) share = 191,983K, total consolidated = 185,522K. Using parent's net income (191,983K) per `us-gaap_NetIncomeLoss` = AEO shareholders' portion.
- TSE: Using parent-only Stockholders' Equity (1,693,153K), consistent with all prior years. Minority Interest (-1,719K) is excluded.

### Side-by-Side

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 5,547,236 | 5,547,236 | — | 5,547,236 |
| Cost of Goods | 3,521,915 | 3,521,915 | — | 3,521,915 |
| Gross Margin | 2,025,321 | 2,025,321 | — | 2,025,321 |
| SGA | 1,485,535 | 1,485,535 | — | 1,485,535 |
| Operating Profit | 226,222 | 226,222 | — | 226,222 |
| Net Profit | 191,983 | 191,983 | — | 191,983 |
| Inventory | 701,966 | 701,966 | — | 701,966 |
| Current Assets | 1,314,173 | 1,314,173 | — | 1,314,173 |
| Total Assets | 4,009,680 | 4,009,680 | — | 4,009,680 |
| Current Liabilities | 867,563 | 867,563 | — | 867,563 |
| Liabilities | 2,316,527 | 2,316,527 | — | 2,316,527 |
| Total SE | 1,693,153 | 1,693,153 | — | 1,693,153 |
| Total L+SE | 4,009,680 | 4,009,680 | — | 4,009,680 |

**Action: New insert.**

---

**Analysis complete.** Run `/insert-financials AEO` to write all changed years to the database.
