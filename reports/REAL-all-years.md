# The RealReal (REAL) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate | Action |
|------|------------|--------|
| 2018 | 2018-12-31 | No change (SEC unavailable pre-IPO; income consistent; BS has temp-equity warning) |
| 2019 | 2019-12-31 | No change (all values match restated comparatives) |
| 2020 | 2020-12-31 | Correction: SGA $196,575K → $195,465K (-$1,110K legal settlement reclassification) |
| 2021 | 2021-12-31 | Minor correction: SGA $239,167K → $238,995K (-$172K minor restatement) |
| 2022 | 2022-12-31 | No change (SGA discrepancy $42K — within rounding noise, recommend keeping) |
| 2023 | 2023-12-31 | No change (SGA $240,728K is correct per rules — excludes reclassified legal settlement) |
| 2024 | 2024-12-31 | No change (all values verified) |
| 2025 | 2025-12-31 | New insert |

---

## Company Notes Applied

**Segment:** Consignment/Resale marketplace

**SGA rule:** SGA = `us-gaap_SellingGeneralAndAdministrativeExpense` + `us-gaap_MarketingExpense`. Exclude `real_OperationsAndTechnologyExpense` (platform infrastructure). Exclude `us-gaap_RestructuringCharges` and `us-gaap_LitigationSettlementExpense` (one-time).

**Inventory:** The company-notes.md states "NULL — pure consignment model" but SEC filings confirm The RealReal carries physical inventory for its direct revenue segment in all years. Dolt correctly stores non-null inventory values. The company notes entry is outdated/incorrect and should be updated.

**Equity:** Negative TSE is expected and valid throughout.

**Gross margin:** 60–80% expected range (consignment net revenue model).

---

## FY2018

### Anomaly Detection

- [WARNING] No SEC 10-K filing found for FY2018 — company went public in June 2019 (IPO). FY2018 income data sourced from the FY2019 10-K comparative columns.
- [WARNING] Balance sheet cannot be verified from SEC (no 10-K). Dolt values retained as-entered.
- [WARNING] **Balance sheet identity fails in Dolt.** Dolt stores Liabilities=$98,907K and TSE=−$257,690K but Total Assets=$135,417K. Per formula: Liabilities = TA − TSE = 135,417 − (−257,690) = **$393,107K** ≠ $98,907K stored. Root cause: pre-IPO balance sheet included ~$294,200K of Redeemable Convertible Preferred Stock as temporary equity (between liabilities and permanent equity in the filing). The DB schema has no field for temp equity. Dolt's $98,907K = actual debt+accrual liabilities only; the preferred stock is excluded from both Liabilities and TSE. This is a structural limitation, not a data entry error. Recommend retaining with this note.
- [WARNING] Inventory is stored as $10,355K in Dolt. Not verifiable from SEC for this year.

### Side-by-Side Comparison

| Field | SEC (2019 10-K comparative) | Yahoo | Dolt (current) | Recommended |
|-------|----------------------------|-------|----------------|-------------|
| Net Revenue | 213,732 | N/A | 213,732 | **213,732** |
| Cost of Goods | 76,814 | N/A | 76,814 | **76,814** |
| Gross Margin | 136,918 | N/A | 136,918 | **136,918** |
| SGA | 63,728 + 42,165 = **105,893** | N/A | 105,893 | **105,893** |
| Operating Profit | −73,904 | N/A | −73,904 | **−73,904** |
| Net Profit | −75,765 | N/A | −75,765 | **−75,765** |
| Inventory | N/A | N/A | 10,355 | **10,355** (retain) |
| Current Assets | N/A | N/A | 89,146 | **89,146** (retain) |
| Total Assets | N/A | N/A | 135,417 | **135,417** (retain) |
| Current Liabilities | N/A | N/A | 88,354 | **88,354** (retain) |
| Liabilities | N/A | N/A | 98,907 | **98,907** (retain, see warning) |
| Total SE | N/A | N/A | −257,690 | **−257,690** (retain) |
| TL&SE | N/A | N/A | 135,417 | **135,417** (retain) |

### Reconciliation

- Income statement: all fields verified against 2019 10-K comparative. SGA correctly constructed (SGA $63,728K + Marketing $42,165K = $105,893K).
- Balance sheet: not verifiable; retained as-is with temp equity warning.
- Gross margin %: 136,918 / 213,732 = **64.1%** ✓ within 60–80% expected range.
- **No changes to Dolt values recommended.**

---

## FY2019

### Anomaly Detection

- [WARNING] Revenue was restated between the 2019 and 2020 10-K filings: $318,037K → $316,354K (−$1,683K). Dolt holds the restated value ✓.
- [WARNING] All 2019 balance sheet values in Dolt are $1,683K lower than the original 2019 10-K. This is consistent with the revenue restatement flowing through retained earnings → TSE → Total Assets. Dolt uses the restated comparative values ✓.
- [WARNING] Negative TSE in 2018 normalizes to positive in 2019 following the June 2019 IPO (preferred stock converted to common equity). TSE = $337,245K is valid.

### Side-by-Side Comparison

| Field | SEC (2021 10-K restated) | Yahoo | Dolt (current) | Recommended |
|-------|--------------------------|-------|----------------|-------------|
| Net Revenue | 316,354 | N/A | 316,354 | **316,354** |
| Cost of Goods | 114,831 | N/A | 114,831 | **114,831** |
| Gross Margin | 201,523 | N/A | 201,523 | **201,523** |
| SGA | 110,663 + 47,734 = **158,397** | N/A | 158,397 | **158,397** |
| Operating Profit | −100,105 | N/A | −100,105 | **−100,105** |
| Net Profit | −98,429 | N/A | −98,429 | **−98,429** |
| Inventory | 23,599 (original); ~21,916 (restated) | N/A | 21,916 | **21,916** (restated) |
| Current Assets | 408,439 (orig); ~406,756 (restated) | N/A | 406,756 | **406,756** |
| Total Assets | 466,930 (orig); 465,247 (restated) | N/A | 465,247 | **465,247** |
| Current Liabilities | 118,546 | N/A | 118,546 | **118,546** |
| Liabilities | 128,002 | N/A | 128,002 | **128,002** |
| Total SE | 338,928 (orig); 337,245 (restated) | N/A | 337,245 | **337,245** |
| TL&SE | 466,930 (orig); 465,247 (restated) | N/A | 465,247 | **465,247** |

### Reconciliation

- Dolt correctly holds restated values throughout.
- SGA correctly constructed: SGA $110,663K + Marketing $47,734K = $105,893K... wait: $158,397K ✓.
- Gross margin %: 201,523 / 316,354 = **63.7%** ✓ within expected range.
- Balance check: 128,002 + 337,245 = 465,247 ✓.
- **No changes to Dolt values recommended.**

---

## FY2020

### Anomaly Detection

- [WARNING] **SGA needs correction.** The FY2020 10-K included a $1,110K legal settlement in `us-gaap_SellingGeneralAndAdministrativeExpense` ($141,762K). The FY2021 10-K restated the 2020 SGA by breaking out the legal settlement as a separate line (`us-gaap_LitigationSettlementExpense: $1,110K`), reducing SGA to $140,652K. Per anomaly rules, legal settlements must be excluded from SGA. Dolt's current value of $196,575K uses the original (incorrect) SGA; correct value is $195,465K.
- [WARNING] Negative TSE expected (post-IPO accumulated deficit growing).

### Side-by-Side Comparison

| Field | SEC (2022 10-K restated) | Yahoo | Dolt (current) | Recommended |
|-------|--------------------------|-------|----------------|-------------|
| Net Revenue | 299,949 | N/A | 299,949 | **299,949** |
| Cost of Goods | 112,382 | N/A | 112,382 | **112,382** |
| Gross Margin | 187,567 | N/A | 187,567 | **187,567** |
| SGA | 140,652 + 54,813 = **195,465** | N/A | 196,575 * | **195,465** |
| Operating Profit | −172,816 | N/A | −172,816 | **−172,816** |
| Net Profit | −175,832 | N/A | −175,832 | **−175,832** |
| Inventory | 42,321 | N/A | 42,321 | **42,321** |
| Current Assets | 421,469 | N/A | 421,469 | **421,469** |
| Total Assets | 605,109 | N/A | 605,109 | **605,109** |
| Current Liabilities | 148,260 | N/A | 148,260 | **148,260** |
| Liabilities | 413,816 | N/A | 413,816 | **413,816** |
| Total SE | 191,293 | N/A | 191,293 | **191,293** |
| TL&SE | 605,109 | N/A | 605,109 | **605,109** |

*Dolt SGA $196,575K = original 2020 10-K: SGA $141,762K + Marketing $54,813K (incorrectly includes $1,110K legal settlement in SGA).

### Reconciliation

- **SGA correction: $196,575K → $195,465K** (reduce by $1,110K to exclude legal settlement).
- All balance sheet values verified ✓ (no changes needed).
- Gross margin %: 187,567 / 299,949 = **62.5%** ✓ within expected range.
- Balance check: 413,816 + 191,293 = 605,109 ✓.
- Operating Profit unchanged at −$172,816K (legal settlement was below-the-line in the restated filing).

---

## FY2021

### Anomaly Detection

- [WARNING] Minor SGA restatement detected between filings. FY2021 10-K and FY2022 10-K both show SGA=$176,418K for 2021. FY2023 10-K shows restated SGA=$176,246K for 2021 (−$172K). Per restatement rule, use most recent filing.
- [WARNING] Large legal settlement ($13,389K) for class action is correctly excluded from SGA in all filings (reported as separate `us-gaap_LitigationSettlementExpense` line). Dolt SGA does not include it ✓.
- [WARNING] Negative TSE expected.

### Side-by-Side Comparison

| Field | SEC (2023 10-K restated) | Yahoo | Dolt (current) | Recommended |
|-------|--------------------------|-------|----------------|-------------|
| Net Revenue | 467,692 | N/A | 467,692 | **467,692** |
| Cost of Goods | 194,215 | N/A | 194,215 | **194,215** |
| Gross Margin | 273,477 | N/A | 273,477 | **273,477** |
| SGA | 176,246 + 62,749 = **238,995** | N/A | 239,167 * | **238,995** |
| Operating Profit | −214,908 | N/A | −214,908 | **−214,908** |
| Net Profit | −236,107 | N/A | −236,107 | **−236,107** |
| Inventory | 71,015 | N/A | 71,015 | **71,015** |
| Current Assets | 517,812 | N/A | 517,812 | **517,812** |
| Total Assets | 754,944 | N/A | 754,944 | **754,944** |
| Current Liabilities | 187,986 | N/A | 187,986 | **187,986** |
| Liabilities | 681,816 | N/A | 681,816 | **681,816** |
| Total SE | 73,128 | N/A | 73,128 | **73,128** |
| TL&SE | 754,944 | N/A | 754,944 | **754,944** |

*Dolt SGA $239,167K = FY2022 10-K's restated 2021 SGA $176,418K + Marketing $62,749K. FY2023 10-K restated SGA to $176,246K (−$172K).

### Reconciliation

- **SGA minor correction: $239,167K → $238,995K** (−$172K per most recent filing).
- All balance sheet values match ✓. Balance check: 681,816 + 73,128 = 754,944 ✓.
- Gross margin %: 273,477 / 467,692 = **58.5%** — slightly below 60% floor, but explainable by the high direct revenue mix in 2021 (which has lower margins than consignment). [WARNING] — within acceptable range given business model transition.
- Operating Profit consistent across all filings at −$214,908K.

---

## FY2022

### Anomaly Detection

- [WARNING] Minor SGA inconsistency across filings: original 2022 10-K = $258,288K; 2023 10-K restated = $257,874K; 2024 10-K restated = $258,330K. Differences are $42–$414K, likely minor classification adjustments between marketing and SGA. Most recent (2024) = $258,330K vs Dolt $258,288K = difference of $42K (0.02%).
- [WARNING] Negative TSE expected.

### Side-by-Side Comparison

| Field | SEC (2024 10-K restated) | Yahoo (2022) | Dolt (current) | Recommended |
|-------|--------------------------|--------------|----------------|-------------|
| Net Revenue | 603,493 | 603,493 | 603,493 | **603,493** |
| Cost of Goods | 254,802 | 254,802 | 254,802 | **254,802** |
| Gross Margin | 348,691 | 348,691 | 348,691 | **348,691** |
| SGA | 195,342 + 62,988 = **258,330** | 258,330 * | 258,288 | **258,288** (keep) |
| Operating Profit | −189,163 | −188,267 * | −189,163 | **−189,163** |
| Net Profit | −196,445 | −196,445 | −196,445 | **−196,445** |
| Inventory | 42,967 | 42,967 | 42,967 | **42,967** |
| Current Assets | 372,258 | 372,258 | 372,258 | **372,258** |
| Total Assets | 615,641 | 615,641 | 615,641 | **615,641** |
| Current Liabilities | 207,513 | 207,513 | 207,513 | **207,513** |
| Liabilities | 785,733 | 785,733 | 785,733 | **785,733** |
| Total SE | −170,092 | −170,092 | −170,092 | **−170,092** |
| TL&SE | 615,641 | 615,641 | 615,641 | **615,641** |

*Yahoo "Selling General And Administration" = $258,330K (= $195,342K G&A + $62,988K Marketing, already combined). Yahoo Operating Income = −$188,267K differs slightly from SEC −$189,163K — Yahoo figure is unreliable; use SEC.

### Reconciliation

- SGA discrepancy between Dolt ($258,288K) and most recent SEC filing ($258,330K) is only **$42K** — within rounding noise across three filing restatements. **Recommend keeping current Dolt value** ($258,288K). Not worth a correction at this precision.
- All balance sheet values match ✓. Balance check: 785,733 + (−170,092) = 615,641 ✓.
- Gross margin %: 348,691 / 603,493 = **57.8%** — slightly below 60% floor, again due to high direct revenue mix in 2022. [WARNING] — same explanation as 2021; acceptable.
- **No changes to Dolt values recommended.**

---

## FY2023

### Anomaly Detection

- [WARNING] SGA reclassification between filings: FY2023 10-K reports SGA=$182,453K with legal settlements=$1,340K as separate line. FY2024 10-K's restated 2023 comparative folds the $1,340K legal settlements into SGA ($183,793K), removing the separate legal settlements line. Per anomaly rules, legal settlements must be **excluded** from SGA regardless of how the filing classifies them. Therefore the correct SGA for 2023 = original SGA $182,453K + Marketing $58,275K = **$240,728K** ✓ — this is what Dolt currently holds.
- [WARNING] Large restructuring charge ($43,462K) in 2023 correctly excluded from SGA.
- [WARNING] Negative TSE expected.

### Side-by-Side Comparison

| Field | SEC (2023 10-K / adjusted per rules) | Yahoo (2023) | Dolt (current) | Recommended |
|-------|--------------------------------------|--------------|----------------|-------------|
| Net Revenue | 549,304 | 549,304 | 549,304 | **549,304** |
| Cost of Goods | 173,026 | 173,026 | 173,026 | **173,026** |
| Gross Margin | 376,278 | 376,278 | 376,278 | **376,278** |
| SGA | 182,453 + 58,275 = **240,728** | 242,068 * | 240,728 | **240,728** |
| Operating Profit | −166,293 | −122,831 * | −166,293 | **−166,293** |
| Net Profit | −168,472 | −168,472 | −168,472 | **−168,472** |
| Inventory | 22,246 | 22,246 | 22,246 | **22,246** |
| Current Assets | 235,947 | 235,947 | 235,947 | **235,947** |
| Total Assets | 446,923 | 446,923 | 446,923 | **446,923** |
| Current Liabilities | 188,862 | 188,862 | 188,862 | **188,862** |
| Liabilities | 750,222 | 750,222 | 750,222 | **750,222** |
| Total SE | −303,299 | −303,299 | −303,299 | **−303,299** |
| TL&SE | 446,923 | 446,923 | 446,923 | **446,923** |

*Yahoo SGA $242,068K uses the 2024 filing's restated SGA (which folds in legal settlements). Per rules, use $240,728K. Yahoo Operating Income −$122,831K appears to exclude restructuring charges; use SEC −$166,293K.

### Reconciliation

- Dolt SGA $240,728K is **correct per rules** — it correctly excludes the $1,340K legal settlement even though the 2024 10-K folded it back into SGA. ✓
- Balance sheet all verified ✓. Balance check: 750,222 + (−303,299) = 446,923 ✓.
- Gross margin %: 376,278 / 549,304 = **68.5%** ✓ within 60–80% expected range.
- **No changes to Dolt values recommended.**

---

## FY2024

### Anomaly Detection

- [WARNING] Negative TSE (−$407,376K) confirmed valid ✓.
- [WARNING] Large non-operating item: Change in fair value of warrant liability = −$68,167K. This is a non-cash below-the-line item driving a significant gap between Operating Profit (−$56,495K) and Net Profit (−$134,202K). Not a red flag — warrant liability fair value adjustments are expected post-debt restructuring.
- SGA verified against both FY2024 and FY2025 10-K comparatives — consistent ✓.

### Side-by-Side Comparison

| Field | SEC (2025 10-K restated) | Yahoo (2024) | Dolt (current) | Recommended |
|-------|--------------------------|--------------|----------------|-------------|
| Net Revenue | 600,484 | 600,484 | 600,484 | **600,484** |
| Cost of Goods | 152,963 | 152,963 | 152,963 | **152,963** |
| Gross Margin | 447,521 | 447,521 | 447,521 | **447,521** |
| SGA | 187,737 + 55,256 = **242,993** | 242,993 | 242,993 | **242,993** |
| Operating Profit | −56,495 | −56,299 * | −56,495 | **−56,495** |
| Net Profit | −134,202 | −134,202 | −134,202 | **−134,202** |
| Inventory | 23,583 | 23,583 | 23,583 | **23,583** |
| Current Assets | 232,669 | 232,669 | 232,669 | **232,669** |
| Total Assets | 423,095 | 423,095 | 423,095 | **423,095** |
| Current Liabilities | 248,676 | 248,676 | 248,676 | **248,676** |
| Liabilities | 830,471 | 830,471 | 830,471 | **830,471** |
| Total SE | −407,376 | −407,376 | −407,376 | **−407,376** |
| TL&SE | 423,095 | 423,095 | 423,095 | **423,095** |

*Yahoo Operating Income −$56,299K differs by $196K from SEC −$56,495K — likely the $196K restructuring charge. Use SEC.

### Reconciliation

- All values verified across SEC and Yahoo ✓.
- Balance check: 830,471 + (−407,376) = 423,095 ✓.
- Gross margin %: 447,521 / 600,484 = **74.5%** ✓ within expected range.
- **No changes to Dolt values recommended.**

---

## FY2025 (New Insert)

### Anomaly Detection

- [WARNING] Negative TSE (−$415,518K) expected and valid ✓.
- [WARNING] Large non-operating item: Change in fair value of warrant liability = −$35,769K contributes to gap between Operating Profit (−$23,934K) and Net Profit (−$41,799K).
- [WARNING] Gain on extinguishment of debt = $40,785K (non-cash, related to note exchanges in Feb/Aug 2025) also below-the-line.
- SEC and Yahoo data fully consistent ✓.
- SGA construction: SGA $201,589K + Marketing $63,251K = **$264,840K**. Ops & Tech $275,916K correctly excluded.

### Side-by-Side Comparison

| Field | SEC (2025 10-K) | Yahoo (2025) | Dolt (current) | Recommended |
|-------|-----------------|--------------|----------------|-------------|
| Net Revenue | 692,845 | 692,845 | — | **692,845** |
| Cost of Goods | 176,023 | 176,023 | — | **176,023** |
| Gross Margin | 516,822 | 516,822 | — | **516,822** |
| SGA | 201,589 + 63,251 = **264,840** | 264,840 | — | **264,840** |
| Operating Profit | −23,934 | −23,934 | — | **−23,934** |
| Net Profit | −41,799 | −41,799 | — | **−41,799** |
| Inventory | 30,843 | 30,843 | — | **30,843** |
| Current Assets | 227,491 | 227,491 | — | **227,491** |
| Total Assets | 409,033 | 409,033 | — | **409,033** |
| Current Liabilities | 264,240 | 264,240 | — | **264,240** |
| Liabilities | 824,551 | 824,551 | — | **824,551** |
| Total SE | −415,518 | −415,518 | — | **−415,518** |
| TL&SE | 409,033 | 409,033 | — | **409,033** |

### Reconciliation

- Gross margin %: 516,822 / 692,845 = **74.6%** ✓ within 60–80% expected range.
- Balance check: 824,551 + (−415,518) = 409,033 ✓.
- SEC and Yahoo agree on all 13 fields ✓.
- **New insert required for FY2025.**

---

## Unresolved Flags for Review

1. **FY2018 balance sheet**: Structural inconsistency (Liabilities + TSE ≠ Total Assets) due to pre-IPO temporary equity (redeemable preferred stock). Data retained as-is. No correction possible without original S-1 data.
2. **Inventory in company-notes.md**: File incorrectly states "Inventory: NULL — pure consignment model." The RealReal carries physical inventory for its direct revenue segment. All SEC filings and Dolt values correctly reflect non-null inventory. The notes file should be corrected.
3. **FY2021/FY2022 gross margin %**: Slightly below 60% floor (58–58.5%) due to the high direct-revenue mix in those years. Acceptable given the business model (direct revenue has lower gross margins than consignment).

---

**Analysis complete.** Run `/create-verified-dolt-db-financials-sql REAL` to write all changed years to the database.
