# Company-Specific Notes

Per-company quirks discovered during validation. Check this file in Step 4 for the company being analyzed.

Add new entries here whenever a new pattern is discovered for a company — this file grows over time.

---

## TheRealReal (TRR)

**Segment:** Specialty → Consignment/Resale marketplace

**SGA construction:**
- Include: `us-gaap_SellingGeneralAndAdministrativeExpense` + `us-gaap_MarketingExpense`
- Exclude: `real_OperationsAndTechnologyExpense` (platform infrastructure cost — see Rule 2 in anomaly-rules.md)
- FY2024 correct SGA = $243,000K (SGA $187,737K + Marketing $55,256K)
- Former incorrect Dolt value: $485,571K (was wrongly including Ops & Tech)

**Inventory:** NULL — pure consignment model, holds no owned inventory.

**Equity:** Negative Total Shareholder Equity is expected and valid.

**Gross margin:** ~70%+ is normal for consignment model (net revenue is net of consignor payouts).

---

## Walmart (WMT)

**Segment:** Discount

**SGA:** Single combined `us-gaap_SellingGeneralAndAdministrativeExpense` line. No separate marketing or ops split. Use directly.

**Fiscal year:** Ends late January. DB year = reportDate year − 1. Example: reportDate 2025-01-31 → Dolt year=2024; reportDate 2026-01-31 → Dolt year=2025.

**Revenue convention (CRITICAL):** SEC reports two revenue lines. Always use `us-gaap_Revenues` (= contract revenue + membership/other income), NOT `us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax` (contract only). The difference is membership fees (~$4–7B/year). Gross = `us-gaap_Revenues` − COGS. Year 2019 in DB incorrectly used contract-only revenue — corrected 2026-06-08.

**Minority interest (CRITICAL):** WMT has NCI from international JVs (Flipkart India, PhonePe, etc.). DB convention:
- **TSE = `us-gaap_StockholdersEquity`** (common shareholders only, excluding minority interest)
- **Liabilities = Total Assets − TSE** (absorbs NCI and Redeemable NCI into DB "Liabilities")
- Do NOT use `us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest`
- Minority interest by year (non-redeemable NCI): ~$6–9B/year
- Redeemable NCI appeared FY2024 onwards: 2025-01-31 $271K; 2026-01-31 $293K → also absorbed into DB Liabilities
- Years 2018, 2019, and 2024 in Dolt were using total-equity convention — corrected 2026-06-08

**Net Income:** Always use `us-gaap_NetIncomeLoss` (attributable to common shareholders), not `us-gaap_ProfitLoss`. NCI entities (international JVs) have net income each year, so ProfitLoss > NetIncomeLoss consistently.

**Inventory:** Large positive value expected. A missing or small inventory figure is [ERROR].

---

## Macy's (M)

**Segment:** Department Stores

**SGA:** Single combined line. Yahoo and SEC generally agree. Use SEC.

**Fiscal year:** Ends late January/early February.

**Notes:** Multi-year data verified from SEC and Yahoo — values consistent.

---

## Costco (COST)

**Segment:** Warehouse Clubs

**Gross margin:** Unusually low (~13%) is correct for warehouse club model — bulk pricing, low markup.

**Membership fees:** Reported separately as revenue; included in Net Revenue total.

**Fiscal year:** Ends late August.

---

## Amazon (AMZN)

**Segment:** Online

**SGA:** Separate "Technology and content" and "General and administrative" lines. Do NOT add "Technology and content" to SGA — it is a product/platform cost. Use G&A only, or SGA as labeled.

**Inventory:** Amazon carries physical inventory for its retail segment; include.

**Fiscal year:** Calendar year (ends Dec 31).

---

## Non-US Companies

The following companies are in the DB but have no SEC filings. Skip the SEC fetch step; use Yahoo only and flag that SEC data is unavailable.

- Louis Vuitton (LVMUY)
- H&M (HNNMY)
- Adidas (ADDYY)
- Inditex / Zara (IDEXY)
- Aritzia (ATZ.TO)
- Ahold Delhaize (ADRNY)
- ASOS (ASOS.L)

---

## Urban Outfitters (URBN)

**Segment:** Specialty (apparel, home, accessories) — brands: Urban Outfitters, Anthropologie, Free People, Nuuly (subscription)

**Fiscal year:** Ends January 31 each year. FY2025 = fiscal year ending 2026-01-31.

**SGA construction:** Single combined `us-gaap_SellingGeneralAndAdministrativeExpense` line. Use directly. No separate marketing or ops split.

**Store impairment (CRITICAL):** URBN reports `urbn_StoreImpairmentAndLeaseAbandonment` as a separate income statement line *between* Cost of Revenue and Gross Profit. This means:
- SEC-reported Gross Profit = Revenue − COGS − Store Impairment
- **DB approach:** Use Revenue − `us-gaap_CostOfRevenue` only for Gross Margin (excludes store impairment). Operating Profit is taken directly from SEC (which does include the impairment impact).
- **Yahoo COGS artifact:** Yahoo bundles store impairment into its Cost of Revenue figure. Always use SEC for COGS and Gross Margin for URBN.
- Store impairment amounts by year: FY2019 $14,611K; FY2020 $15,496K; FY2021 $0; FY2022 $6,417K; FY2023 $11,875K; FY2024 $4,601K; FY2025 $1,989K.

**Gross margin:** URBN's gross margins (25–36%) are below the typical specialty range (35–55%) because COGS includes all store occupancy costs. This is expected and not an anomaly.

**ASC 842 adoption:** FY2019 balance sheet shows a large jump in Total Assets ($2.16B → $3.32B) due to operating lease right-of-use assets being added. This is not an error.

---

## Victoria's Secret (VSCO)

**Segment:** Specialty (lingerie/intimate apparel) — brands: Victoria's Secret, PINK, Adore Me

**Fiscal year:** Ends late January/early February (varies: 2022-01-29, 2023-01-28, 2024-02-03, 2025-02-01, 2026-01-31).

**Spinoff history:** VSCO was carved out of L Brands on August 2, 2021 (CIK 1856437). FY2020 (ending 2021-01-30) is from L Brands carved-out financials — no standalone 10-K exists for FY2020. FY2020 income statement is verifiable from the FY2021 10-K comparative; balance sheet is NOT verifiable from any 10-K.

**SGA construction:** Single combined `us-gaap_SellingGeneralAndAdministrativeExpense` line. Use directly. No separate marketing or ops split.

**Minority interest (CRITICAL):** VSCO has a Chinese JV with a noncontrolling interest starting FY2022. DB convention:
- **TSE = `us-gaap_StockholdersEquity`** (common shareholders only, excluding minority interest)
- **Liabilities = Total Assets − TSE** (implicitly includes minority interest in "liabilities")
- Do NOT use `us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest`
- Minority interest by year: FY2022 $18M, FY2023 $21M, FY2024 $24M, FY2025 $54M

**Net Income:** Always use `us-gaap_NetIncomeLoss` (attributable to common shareholders). Do NOT use `us-gaap_ProfitLoss` (consolidated including NCI). These diverge whenever the JV has income or losses.

**Gross margin:** 35–45% expected for specialty lingerie. FY2020 was 29% (COVID impact — acceptable).

---

## Walgreens (WBA)

**Segment:** Health & Pharmacy (drug store chain + Boots UK international + pharmaceutical wholesale)

**Fiscal year:** Ends August 31. FY2024 = fiscal year ending 2024-08-31.

**Went private:** Sycamore Partners acquisition closed March 2025. Yahoo Finance unavailable. FY2025 filing status uncertain.

**SGA construction:** Single combined `us-gaap_SellingGeneralAndAdministrativeExpense` line. No marketing or ops-tech split. Note: FY2023 SGA includes opioid litigation settlement reserves (~$6.9B above prior year). FY2024 has a SEPARATE `us-gaap_GoodwillImpairmentLoss` line ($12.7B for VillageMD) that is NOT part of SGA — do not add to SGA.

**Minority interest (CRITICAL):** WBA has NCI from Boots UK and healthcare ventures (VillageMD/CityMD FY2022–FY2024). DB convention:
- **TSE = `us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest`** (total equity including NCI)
- **Liabilities = Total Assets − TSE** (Redeemable NCI is absorbed into "Liabilities")
- This is the OPPOSITE of VSCO's convention (VSCO uses common-only TSE)

**Net Income:** Always use `us-gaap_NetIncomeLoss` (to parent). Do NOT use `us-gaap_ProfitLoss` (consolidated). In FY2022–FY2024, NCI entities had large losses absorbed by minority investors, making parent's net income significantly different from consolidated profit.

**SEC data limitation:** FY2021, FY2022, FY2023 10-K filings fail to load from SEC MCP ('NoneType' error). Use FY2024 10-K comparative for FY2022 and FY2023 income statements. Balance sheets for FY2021–FY2023 unverifiable from SEC.

**Gross margin:** 18–25% expected (pharmacy-heavy; ~22% historically, declining toward 18% as pharmacy mix increases and reimbursement rates compress).

---

## Wayfair (W)

**Segment:** Online home furnishings marketplace

**SGA convention (CRITICAL):** Wayfair uses a non-standard income statement structure. There is NO traditional SGA line. DB SGA = `w_SellingTechnologyOperationsGeneralAndAdministrativeExpense` (SOTG&A) **only**. The other operating expense lines below gross profit are excluded:
- `w_CustomerServiceAndMerchantFees` — NOT in SGA
- `us-gaap_AdvertisingExpense` (Marketing) — NOT in SGA
- `us-gaap_OtherAssetImpairmentCharges` (Impairment) — NOT in SGA
- `us-gaap_RestructuringCharges` — NOT in SGA
- `us-gaap_OperatingExpenses` = total of all above — **do NOT use as SGA**
- Yahoo Finance shows "Selling General And Administration" = Marketing + SOTG&A. **Do not use Yahoo SGA for Wayfair.**

**Operating Income:** Use `us-gaap_OperatingIncomeLoss` (SEC as-reported, includes restructuring and impairment). Yahoo sometimes reports a higher normalized OpInc excluding those items — always use SEC.

**Fiscal year:** Calendar year (ends Dec 31). DB year = reportDate year. Example: 2024-12-31 → Dolt year=2024.

**Equity:** Negative Total Shareholder Equity is expected and persistent ($−330M to $−3B). Accumulated deficit from years of operating losses. Not an anomaly.

**No NCI:** Wayfair has no noncontrolling interest. TSE = `us-gaap_StockholdersEquity` = total equity. No NCI adjustment needed for TSE or NetInc.

**Net Income:** `us-gaap_NetIncomeLoss`. No parent/NCI split needed (Wayfair has no subsidiaries with NCI).

**Year 2024 SGA error (corrected 2026-06-08):** Dolt used 4,035,000K = `us-gaap_OperatingExpenses` (total OpEx including customer service, marketing, SOTG&A, impairment, and restructuring). Correct DB convention = 1,977,000K = SOTG&A only.

---

## Williams-Sonoma (WSM)

**Segment:** Specialty (home furnishings, kitchen, décor) — brands: Williams-Sonoma, Pottery Barn, West Elm, Pottery Barn Kids/Teens, Rejuvenation

**Fiscal year:** Ends on the Sunday nearest February 1 (varies — may fall in late January or early February). DB year = reportDate year − 1. Example: reportDate 2026-02-01 → Dolt year=2025. Unlike WMT which always ends Jan 31, WSM's date moves by up to a week, so always verify the actual reportDate from SEC rather than assuming a fixed date.

**SGA:** Single combined `us-gaap_SellingGeneralAndAdministrativeExpense` line. Use directly. No composite rule needed.

**COGS tag change:** Older filings (≤ FY2022) use `wsm_CostOfGoodsSoldAndOccupancyExpenses`; newer filings (FY2023+) use `us-gaap_CostOfRevenue`. Both represent the same single "Cost of goods sold" line (inclusive of store occupancy). Use whichever is present — both are correct.

**ASC 842 adoption (CRITICAL for FY2019 balance sheet):** FY2019 (reportDate 2020-02-02) shows a ~$1.2B jump in Total Assets from operating lease right-of-use assets added. Not an error.

**Gross margin:** 36–47% expected. Has expanded from ~37% (FY2018) to ~46% (FY2024–FY2025) as the company shifted mix toward e-commerce and higher-margin brands.

**No NCI:** WSM has no noncontrolling interest. TSE = `us-gaap_StockholdersEquity`.

**Year 2018 SGA error (corrected 2026-06-08):** Dolt stored SGA as −1,665,060K (negative). Correct = +1,665,060K. Magnitude was correct; sign was entered as negative from SEC income statement sign convention.

**Year 2024 reportDate error (corrected 2026-06-08):** Dolt had 2025-01-28. Correct = 2025-02-02 (fiscal year ended the Sunday nearest Feb 1 = Feb 2, 2025). Financial data was otherwise correct.

---

## YETI (YETI)

**Segment:** Specialty (premium outdoor brand — coolers, drinkware, bags, accessories)

**Fiscal year (CRITICAL):** YETI uses a **52/53-week fiscal year ending on the Saturday nearest December 31**. reportDates are NOT always Dec 31 — they vary by up to ±3 days. Always verify from SEC period header, never assume Dec 31. Historical reportDates:
- FY2018: 2018-12-29 | FY2019: 2019-12-28 | FY2020: 2021-01-02 | FY2021: 2022-01-01
- FY2022: 2022-12-31 | FY2023: 2023-12-30 | FY2024: 2024-12-28 | FY2025: 2026-01-03

**DB year convention:** DB year = YETI's own fiscal year label (the calendar year the majority of the fiscal period falls in). E.g., fiscal year ending 2026-01-03 → Dolt year=2025. Yahoo Finance rounds reportDate to Dec 31 — never use Yahoo for reportDate.

**SGA:** Single combined `us-gaap_SellingGeneralAndAdministrativeExpense`. No composite needed. Yahoo SGA matches SEC exactly.

**Gross margin:** 45–60% expected (above generic specialty 35–55% benchmark due to premium brand pricing power and DTC growth). FY2022 dipped to ~48% from supply chain cost pressure. FY2020–2021 and FY2023–2025 run 57–58%.

**No NCI.** TSE = `us-gaap_StockholdersEquity`. Pre-FY2020 filings may use the `...IncludingPortionAttributableToNoncontrollingInterest` tag for the same value — no actual NCI.

**Inventory:** Positive; YETI carries physical manufactured inventory. Always required.

**Year 2024 reportDate corrected 2026-06-08:** Was 2024-12-31 → corrected to 2024-12-28 (Saturday nearest Dec 31, 2024). Financial data was correct; only reportDate needed fixing.

---

## eBay (EBAY)

**Segment:** Online marketplace (pure platform — marketplace fees + advertising; no physical goods)

**SGA convention (CRITICAL):** eBay reports separate lines. DB SGA = `us-gaap_SellingAndMarketingExpense` + `us-gaap_GeneralAndAdministrativeExpense` (Rule 4 — no combined SGA tag). Exclude:
- `us-gaap_ResearchAndDevelopmentExpense` (R&D) — NOT in SGA
- `ebay_ProvisionForTransactionLosses` — NOT in SGA
- `ebay_AmortizationofAcquiredIntangibleAssets1` — NOT in SGA

Yahoo "Selling General And Administration" = S&M + G&A (matches DB convention). Yahoo is reliable for SGA for FY2022 onward.

**Inventory:** NULL always. Pure marketplace — holds no physical goods.

**Fiscal year:** Calendar year (ends Dec 31). DB year = reportDate year.

**Non-operating items:** eBay holds equity stakes (Adevinta, Gmarket) generating large one-time gains/losses. FY2022 NetInc = −1,269,000K (Adevinta write-down). FY2023 NetInc = 2,767,000K (investment gain). FY2021 NetInc = 13,608,000K (Classifieds/Adevinta divestiture gain). These are real, not errors.

**Discontinued operations:** StubHub sold (closed Feb 2020), Classifieds/Adevinta stake (2021). DB uses total `us-gaap_NetIncomeLoss`.

**No NCI.** TSE = `us-gaap_StockholdersEquity`.

**Gross margin:** 70–80% expected for pure marketplace.

**SEC data limitation:** SEC MCP returns NoneType for older filings. FY2018–FY2021 unverifiable from SEC; Yahoo only covers FY2022+.

**FY2019 [ERROR] (unresolved as of 2026-06-08):** DB SGA = 4,383K but total OpEx from IS (Gross 5,844K − OpInc 1,770K) = 4,074K. SGA > total OpEx is impossible. Cannot fix without SEC data.

Historical confirmed SGA (S&M+G&A):
- FY2022: 3,099,000K | FY2023: 3,413,000K | FY2024: 3,233,000K | FY2025: 3,592,000K

---

*Add new company entries below as patterns are discovered.*
