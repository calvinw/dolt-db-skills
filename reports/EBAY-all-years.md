# eBay (EBAY) — FY2018–FY2025 Financial Analysis

**Generated:** 2026-06-08
**Source:** /verify-dolt-db-financials skill

---

## Per-Year Summary

| Year | reportDate   | Action                                                                          |
|------|-------------|---------------------------------------------------------------------------------|
| 2018 | 2018-12-31  | No change (SEC unavailable; internally consistent)                              |
| 2019 | 2019-12-31  | [ERROR] SGA 4,383K impossible — exceeds total OpEx 4,074K. SEC unavailable to fix. |
| 2020 | 2020-12-31  | No change (SEC unavailable; internally consistent)                              |
| 2021 | 2021-12-31  | No change (SEC unavailable; internally consistent)                              |
| 2022 | 2022-12-31  | No change (confirmed by Yahoo)                                                  |
| 2023 | 2023-12-31  | No change (confirmed by SEC year=2025 comparative)                              |
| 2024 | 2024-12-31  | No change (confirmed by SEC year=2025 comparative)                              |
| 2025 | 2025-12-31  | New insert                                                                      |

---

## Company Notes

**Segment:** Online marketplace (pure platform — no physical goods; marketplace fees + advertising revenue)

**SGA convention (CRITICAL):** eBay reports separate operating expense lines. DB SGA = `us-gaap_SellingAndMarketingExpense` + `us-gaap_GeneralAndAdministrativeExpense` (Rule 4 — no combined SGA tag). Exclude:
- `us-gaap_ResearchAndDevelopmentExpense` (R&D) — NOT in SGA
- `ebay_ProvisionForTransactionLosses` (transaction losses) — NOT in SGA
- `ebay_AmortizationofAcquiredIntangibleAssets1` (intangible amortization) — NOT in SGA

Yahoo "Selling General And Administration" = S&M + G&A (matches DB convention). Yahoo is reliable for SGA for FY2022 onward.

**Inventory:** NULL always. eBay is a pure marketplace — no physical goods held.

**Fiscal year:** Calendar year (ends Dec 31). DB year = reportDate year.

**Non-operating items:** eBay holds equity stakes in Adevinta, Gmarket, and others. These generate large one-time gains/losses in "other income". FY2022 had a $3.789B loss (driving total NetInc to -$1.269B). FY2023 had a $1.832B gain. NetInc = `us-gaap_NetIncomeLoss` captures these correctly.

**Discontinued operations:** eBay divested StubHub (closed Feb 2020), Classifieds/Adevinta stake (2021), and other businesses. These divestitures created income from discontinued operations in various years. DB uses total `us-gaap_NetIncomeLoss` which includes discontinued ops.

**No NCI.** TSE = `us-gaap_StockholdersEquity`.

**Gross margin:** 70–80% expected for pure marketplace model.

**SEC data limitation:** SEC MCP returns NoneType errors for older eBay filings (year=2022 and year=2019 both failed). FY2018–FY2021 cannot be independently verified from SEC. Only Yahoo (FY2022–FY2025) and the FY2025 10-K comparative (FY2023–FY2024) are available.

**FY2019 [ERROR] (unresolved as of 2026-06-08):** DB SGA = 4,383K but total operating expenses from IS (Gross 5,844K − OpInc 1,770K) = 4,074K. SGA cannot exceed total OpEx. Correct values unknown — SEC data unavailable. Investigate when SEC MCP supports older eBay filings.

---

## FY2018 Analysis (reportDate 2018-12-31)

### Anomaly Detection
- Gross margin: 6,627/8,650 = 76.6% ✓ (within 60–80% marketplace range)
- Balance sheet identity: 22,819 − 6,281 = 16,538 ✓
- Internal IS consistency: Total OpEx = 6,627 − 1,752 = 4,875K. SGA = 4,522K < 4,875K ✓ (gap 353K = amortization + other)
- SEC unavailable (NoneType error). Yahoo does not cover this year. Cannot verify independently.

### Comparison Table

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | N/A | 8,650,000 | 8,650,000 |
| Cost of Goods | N/A | N/A | 2,023,000 | 2,023,000 |
| Gross Margin | N/A | N/A | 6,627,000 | 6,627,000 |
| SGA | N/A | N/A | 4,522,000 | 4,522,000 |
| Operating Profit | N/A | N/A | 1,752,000 | 1,752,000 |
| Net Profit | N/A | N/A | 2,530,000 | 2,530,000 |
| Inventory | N/A | N/A | NULL | NULL |
| Current Assets | N/A | N/A | 7,126,000 | 7,126,000 |
| Total Assets | N/A | N/A | 22,819,000 | 22,819,000 |
| Current Liabilities | N/A | N/A | 4,454,000 | 4,454,000 |
| Liabilities | N/A | N/A | 16,538,000 | 16,538,000 |
| TSE | N/A | N/A | 6,281,000 | 6,281,000 |
| TL+SE | N/A | N/A | 22,819,000 | 22,819,000 |
| reportDate | N/A | N/A | 2018-12-31 | 2018-12-31 |

**Action: No change.** (Cannot verify; internally consistent.)

---

## FY2019 Analysis (reportDate 2019-12-31)

### Anomaly Detection
- Gross margin: 5,844/7,429 = 78.7% ✓
- Balance sheet identity: 18,174 − 2,870 = 15,304 ✓
- **[ERROR] SGA impossible:** Total OpEx from IS = Gross (5,844K) − OpInc (1,770K) = 4,074K. DB SGA = 4,383K > 4,074K. SGA cannot exceed total operating expenses. Data is internally inconsistent.
- SEC unavailable. Yahoo does not cover FY2019.
- Root cause unknown — may reflect a data entry error, mixing of discontinued/continuing ops, or SGA calculated using a different convention in 2019.

### Comparison Table

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | N/A | 7,429,000 | [UNVERIFIED] |
| Cost of Goods | N/A | N/A | 1,585,000 | [UNVERIFIED] |
| Gross Margin | N/A | N/A | 5,844,000 | [UNVERIFIED] |
| SGA | N/A | N/A | **4,383,000 [ERROR]** | [CANNOT FIX — SEC unavailable] |
| Operating Profit | N/A | N/A | 1,770,000 | [UNVERIFIED] |
| Net Profit | N/A | N/A | 1,786,000 | [UNVERIFIED] |
| Inventory | N/A | N/A | NULL | NULL |
| Current Assets | N/A | N/A | 4,706,000 | [UNVERIFIED] |
| Total Assets | N/A | N/A | 18,174,000 | [UNVERIFIED] |
| Current Liabilities | N/A | N/A | 4,066,000 | [UNVERIFIED] |
| Liabilities | N/A | N/A | 15,304,000 | [UNVERIFIED] |
| TSE | N/A | N/A | 2,870,000 | [UNVERIFIED] |
| TL+SE | N/A | N/A | 18,174,000 | [UNVERIFIED] |
| reportDate | N/A | N/A | 2019-12-31 | 2019-12-31 |

**Action: [ERROR] — SGA is physically impossible. Cannot fix without SEC data. Flag for investigation.**

---

## FY2020 Analysis (reportDate 2020-12-31)

### Anomaly Detection
- Gross margin: 7,097/8,894 = 79.8% ✓ (at top of 60–80% range)
- Balance sheet identity: 19,310 − 3,561 = 15,749 ✓
- Internal IS consistency: Total OpEx = 7,097 − 2,636 = 4,461K. SGA = 3,642K < 4,461K ✓ (gap 819K = R&D + transaction losses + amort)
- SEC unavailable. Yahoo does not cover FY2020.

### Comparison Table

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | N/A | 8,894,000 | 8,894,000 |
| Cost of Goods | N/A | N/A | 1,797,000 | 1,797,000 |
| Gross Margin | N/A | N/A | 7,097,000 | 7,097,000 |
| SGA | N/A | N/A | 3,642,000 | 3,642,000 |
| Operating Profit | N/A | N/A | 2,636,000 | 2,636,000 |
| Net Profit | N/A | N/A | 5,667,000 | 5,667,000 |
| Inventory | N/A | N/A | NULL | NULL |
| Current Assets | N/A | N/A | 7,190,000 | 7,190,000 |
| Total Assets | N/A | N/A | 19,310,000 | 19,310,000 |
| Current Liabilities | N/A | N/A | 4,002,000 | 4,002,000 |
| Liabilities | N/A | N/A | 15,749,000 | 15,749,000 |
| TSE | N/A | N/A | 3,561,000 | 3,561,000 |
| TL+SE | N/A | N/A | 19,310,000 | 19,310,000 |
| reportDate | N/A | N/A | 2020-12-31 | 2020-12-31 |

**Action: No change.** (Cannot verify; internally consistent.)

---

## FY2021 Analysis (reportDate 2021-12-31)

### Anomaly Detection
- Gross margin: 7,770/10,420 = 74.6% ✓
- Balance sheet identity: 26,626 − 9,778 = 16,848 ✓
- Internal IS consistency: Total OpEx = 7,770 − 2,923 = 4,847K. SGA = 3,091K < 4,847K ✓
- NetInc = 13,608,000K — very high. This reflects a large gain from the Classifieds Group / Adevinta divestiture in 2021 (eBay received Adevinta shares worth ~$9B).
- SEC unavailable. Yahoo does not cover FY2021.

### Comparison Table

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | N/A | N/A | 10,420,000 | 10,420,000 |
| Cost of Goods | N/A | N/A | 2,650,000 | 2,650,000 |
| Gross Margin | N/A | N/A | 7,770,000 | 7,770,000 |
| SGA | N/A | N/A | 3,091,000 | 3,091,000 |
| Operating Profit | N/A | N/A | 2,923,000 | 2,923,000 |
| Net Profit | N/A | N/A | 13,608,000 | 13,608,000 |
| Inventory | N/A | N/A | NULL | NULL |
| Current Assets | N/A | N/A | 9,111,000 | 9,111,000 |
| Total Assets | N/A | N/A | 26,626,000 | 26,626,000 |
| Current Liabilities | N/A | N/A | 4,622,000 | 4,622,000 |
| Liabilities | N/A | N/A | 16,848,000 | 16,848,000 |
| TSE | N/A | N/A | 9,778,000 | 9,778,000 |
| TL+SE | N/A | N/A | 26,626,000 | 26,626,000 |
| reportDate | N/A | N/A | 2021-12-31 | 2021-12-31 |

**Action: No change.** (Cannot verify; internally consistent. Large NetInc expected from Adevinta stake gain.)

---

## FY2022 Analysis (reportDate 2022-12-31)

### Anomaly Detection
- Gross margin: 7,115/9,795 = 72.6% ✓
- Balance sheet identity: 20,850 − 5,153 = 15,697 ✓
- NetInc = -1,269,000K — large loss from Adevinta stake write-down (~$3.789B loss on equity investments). Not an error.
- All fields confirmed by Yahoo.

### Comparison Table

| Field | Yahoo | Dolt | Recommended |
|-------|-------|------|-------------|
| Net Revenue | 9,795,000 | 9,795,000 | 9,795,000 |
| Cost of Goods | 2,680,000 | 2,680,000 | 2,680,000 |
| Gross Margin | 7,115,000 | 7,115,000 | 7,115,000 |
| SGA (S&M+G&A) | 3,099,000 | 3,099,000 | 3,099,000 |
| Operating Profit | 2,350,000 | 2,350,000 | 2,350,000 |
| Net Profit | -1,269,000 | -1,269,000 | -1,269,000 |
| Inventory | NULL | NULL | NULL |
| Current Assets | 9,290,000 | 9,290,000 | 9,290,000 |
| Total Assets | 20,850,000 | 20,850,000 | 20,850,000 |
| Current Liabilities | 4,271,000 | 4,271,000 | 4,271,000 |
| Liabilities | 15,697,000 | 15,697,000 | 15,697,000 |
| TSE | 5,153,000 | 5,153,000 | 5,153,000 |
| TL+SE | 20,850,000 | 20,850,000 | 20,850,000 |
| reportDate | 2022-12-31 | 2022-12-31 | 2022-12-31 |

**Action: No change.** All confirmed.

---

## FY2023 Analysis (reportDate 2023-12-31)

### Anomaly Detection
- Gross margin: 7,279/10,112 = 72.0% ✓
- Balance sheet identity: 21,620 − 6,396 = 15,224 ✓
- NetInc = 2,767,000K includes $1.832B gain on equity investments (Adevinta stake).
- All fields confirmed by SEC year=2025 comparative + Yahoo.

### Comparison Table

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 10,112,000 | 10,112,000 | 10,112,000 | 10,112,000 |
| Cost of Goods | 2,833,000 | 2,833,000 | 2,833,000 | 2,833,000 |
| Gross Margin | 7,279,000 | 7,279,000 | 7,279,000 | 7,279,000 |
| SGA (S&M+G&A) | 3,413,000 | 3,413,000 | 3,413,000 | 3,413,000 |
| Operating Profit | 1,941,000 | 1,941,000 | 1,941,000 | 1,941,000 |
| Net Profit | 2,767,000 | 2,767,000 | 2,767,000 | 2,767,000 |
| Inventory | NULL | NULL | NULL | NULL |
| Current Assets | 11,016,000 | 11,016,000 | 11,016,000 | 11,016,000 |
| Total Assets | 21,620,000 | 21,620,000 | 21,620,000 | 21,620,000 |
| Current Liabilities | 4,520,000 | 4,520,000 | 4,520,000 | 4,520,000 |
| Liabilities | 15,224,000 | 15,224,000 | 15,224,000 | 15,224,000 |
| TSE | 6,396,000 | 6,396,000 | 6,396,000 | 6,396,000 |
| TL+SE | 21,620,000 | 21,620,000 | 21,620,000 | 21,620,000 |
| reportDate | 2023-12-31 | 2023-12-31 | 2023-12-31 | 2023-12-31 |

**Action: No change.** All confirmed.

---

## FY2024 Analysis (reportDate 2024-12-31)

### Anomaly Detection
- Gross margin: 7,403/10,283 = 72.0% ✓
- Balance sheet identity: 19,365 − 5,158 = 14,207 ✓
- All fields confirmed by SEC year=2025 comparative + Yahoo.

### Comparison Table

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 10,283,000 | 10,283,000 | 10,283,000 | 10,283,000 |
| Cost of Goods | 2,880,000 | 2,880,000 | 2,880,000 | 2,880,000 |
| Gross Margin | 7,403,000 | 7,403,000 | 7,403,000 | 7,403,000 |
| SGA (S&M+G&A) | 3,233,000 | 3,233,000 | 3,233,000 | 3,233,000 |
| Operating Profit | 2,318,000 | 2,318,000 | 2,318,000 | 2,318,000 |
| Net Profit | 1,975,000 | 1,975,000 | 1,975,000 | 1,975,000 |
| Inventory | NULL | NULL | NULL | NULL |
| Current Assets | 7,567,000 | 7,567,000 | 7,567,000 | 7,567,000 |
| Total Assets | 19,365,000 | 19,365,000 | 19,365,000 | 19,365,000 |
| Current Liabilities | 6,098,000 | 6,098,000 | 6,098,000 | 6,098,000 |
| Liabilities | 14,207,000 | 14,207,000 | 14,207,000 | 14,207,000 |
| TSE | 5,158,000 | 5,158,000 | 5,158,000 | 5,158,000 |
| TL+SE | 19,365,000 | 19,365,000 | 19,365,000 | 19,365,000 |
| reportDate | 2024-12-31 | 2024-12-31 | 2024-12-31 | 2024-12-31 |

**Action: No change.** All confirmed.

---

## FY2025 Analysis (reportDate 2025-12-31)

### Anomaly Detection
- Gross margin: 7,931/11,100 = 71.4% ✓ (within 60–80% marketplace range)
- Balance sheet identity: 17,610 − 4,615 = 12,995 ✓
- SGA = S&M (2,394K) + G&A (1,198K) = 3,592K (confirmed from SEC; Yahoo matches exactly)
- NetInc = 2,031,000K from `us-gaap_NetIncomeLoss` (total, including +$11M from equity investments and -$35M from discontinued ops)
- No NCI; Inventory = NULL ✓

### Comparison Table

| Field | SEC | Yahoo | Dolt | Recommended |
|-------|-----|-------|------|-------------|
| Net Revenue | 11,100,000 | 11,100,000 | — | **11,100,000** |
| Cost of Goods | 3,169,000 | 3,169,000 | — | **3,169,000** |
| Gross Margin | 7,931,000 | 7,931,000 | — | **7,931,000** |
| SGA (S&M+G&A) | 3,592,000 | 3,592,000 | — | **3,592,000** |
| Operating Profit | 2,277,000 | 2,277,000 | — | **2,277,000** |
| Net Profit | 2,031,000 | 2,031,000 | — | **2,031,000** |
| Inventory | NULL | NULL | — | **NULL** |
| Current Assets | 5,086,000 | 5,086,000 | — | **5,086,000** |
| Total Assets | 17,610,000 | 17,610,000 | — | **17,610,000** |
| Current Liabilities | 4,637,000 | 4,637,000 | — | **4,637,000** |
| Liabilities | 12,995,000 | 12,995,000 | — | **12,995,000** |
| TSE | 4,615,000 | 4,615,000 | — | **4,615,000** |
| TL+SE | 17,610,000 | 17,610,000 | — | **17,610,000** |
| reportDate | 2025-12-31 | 2025-12-31 | — | **2025-12-31** |

**Action: New insert.** All values confirmed from SEC FY2025 10-K primary; Yahoo matches exactly.

---

## Final Status

**7 of 8 years verified or accepted. 1 unresolved [ERROR] (FY2019 SGA). FY2025 new insert ready.**

Unresolved: FY2019 SGA = 4,383K is physically impossible (exceeds total operating expenses). Cannot fix without SEC data. SEC MCP returns NoneType errors for older eBay filings.
