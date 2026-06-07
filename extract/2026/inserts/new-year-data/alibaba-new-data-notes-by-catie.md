# Alibaba (BABA) — New Year Data Notes
**Author:** Catie He  
**Date:** 2026-06-07  
**Skill:** `/download-new-year-data BABA`

---

## Problems Encountered

### 1. SEC Tool Does Not Work for Alibaba

Alibaba is a Chinese company listed on the NYSE as an ADR. Because it is a foreign company, it files a **20-F** (the foreign private issuer equivalent of an annual report) with the SEC — not a 10-K like American companies. The `/download-new-year-data` skill uses an SEC tool that only reads 10-K filings, so every attempt to fetch Alibaba's SEC data returns an error:

> `Error processing financial data: No 10-K filing found for fiscal year XXXX`

This error occurs regardless of what year, company name variation, or CIK (1577552) is used. The tool simply cannot access 20-F filings.

### 2. Yahoo Finance Returns Values in RMB, Not USD

The database stores Alibaba's financials in **USD**, but when Yahoo Finance is fetched for ticker `BABA`, all values are returned in **Chinese Yuan (RMB)**. These values cannot be inserted directly into the database — they must first be converted to USD.

### 3. Year Labeling Convention Is Non-Standard

Alibaba's fiscal year runs **April to March** (e.g., April 2024 – March 2025). The database labels each fiscal year by the calendar year in which **most of the activity occurred** — meaning 9 months (April–December) fall in year N, so the label is N even though the fiscal year ends in March of year N+1.

For example:
- Fiscal year April 2024 – March 2025 → **DB label: 2024**
- Fiscal year April 2025 – March 2026 → **DB label: 2025** ← next year to add

This is the opposite of the standard January fiscal year convention used for most US retailers in this database, and it is easy to accidentally mislabel Alibaba's years.

---

## How the Existing Data Was Created (Reverse-Engineered)

By comparing all existing DB values against Yahoo Finance RMB values, the original methodology was confirmed:

1. Fetch Yahoo Finance RMB values for the fiscal year column ending **March 31, year N+1**
2. Divide each value by the **USD/CNY spot exchange rate on March 31** of that year
3. Store the result as USD thousands in the database under **DB label year N**

This was verified across multiple years with high precision (differences of <$1M, consistent with rounding):

| DB Year | Fiscal Year End | Yahoo RMB Revenue | Rate Used | DB USD Revenue |
|---------|----------------|-------------------|-----------|----------------|
| 2022 | 2023-03-31 | 868,687,000 | 6.87 | 126,491,000 |
| 2023 | 2024-03-31 | 941,168,000 | 7.22 | 130,350,000 |
| 2024 | 2025-03-31 | 996,347,000 | 7.257 | 137,300,000 |

The database is **current through DB year 2024** (fiscal year ending March 31, 2025).

---

## What Is Needed to Add DB Year 2025

The next year to add is **DB year 2025**, which covers the fiscal year ending **March 31, 2026**.

Yahoo Finance already has the 2026-03-31 RMB values available. The only missing piece is:

> **The USD/CNY spot exchange rate on March 31, 2026**

This can be looked up on any currency website (xe.com, Google Finance, Bloomberg, etc.).

Once that rate is provided, the conversion is straightforward:

```
USD value (thousands) = Yahoo RMB value (thousands) ÷ March 31, 2026 USD/CNY rate
```

All 13 fields (Revenue, COGS, Gross Margin, SGA, Operating Profit, Net Profit, Inventory, Current Assets, Total Assets, Current Liabilities, Liabilities, Total SE, Total L&SE) need to be converted using this same rate.

---

## Suggestion

**Step 1:** Look up the closing USD/CNY exchange rate on **March 31, 2026**.

**Step 2:** Divide each of the following Yahoo Finance 2026-03-31 RMB values by that rate to get USD thousands:

| Field | Yahoo 2026-03-31 (RMB thousands) |
|-------|----------------------------------|
| Net Revenue | 1,023,670,000 |
| Cost of Goods | 616,136,000 |
| Gross Margin | 407,534,000 |
| SGA | 278,105,000 |
| Operating Profit (Total Op. Inc. As Reported) | 50,150,000 |
| Net Profit (Net Income) | 103,592,000 |
| Inventory | 18,909,000 |
| Current Assets | 610,769,000 |
| Total Assets | 1,909,570,000 |
| Current Liabilities | 476,398,000 |
| Total Shareholder Equity | 1,060,890,000 |

Then compute:
- `Liabilities = Total Assets − Total Shareholder Equity`
- `Total L&SE = Total Assets`

**Step 3:** Insert the converted values into the SQL template and run against the local Dolt clone.

---

## Notes for Future Years

- Always use the **March 31 spot rate** (not an average annual rate) to stay consistent with prior entries.
- Always label the fiscal year as **the year most of the activity occurred** (the April start year, not the March end year).
- The SEC tool will never work for Alibaba — skip it and go straight to Yahoo Finance.
