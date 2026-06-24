---
name: basic-financials-quiz
version: 1.0
description: Interactive financial literacy quiz assistant for undergraduate business students. Pulls side-by-side financial data from the BusMgmtBenchmarks Dolt database, then quizzes students on Revenue, COGS, Gross Margin, SG&A, Operating Profit, Net Profit, Inventory, Total Assets, and ratios using multiple-choice and true/false questions. Triggered by "/basic-financials-quiz TICKER1 YEAR1 TICKER2 YEAR2".
---

# basic-financials-quiz

A quiz-style financial literacy assistant for undergraduate business students. Tests understanding of basic financial concepts by fetching real company data from the BusMgmtBenchmarks Dolt database, displaying it side by side, and asking questions that require reading, calculating, and interpreting financial figures from the displayed data.

## Inputs

`/basic-financials-quiz TICKER1 YEAR1 TICKER2 YEAR2`

- `TICKER1` — first company ticker (e.g. `WMT`, `TGT`)
- `YEAR1` — fiscal year for the first company (e.g. `2024`). Optional — defaults to the most recent year available for that company.
- `TICKER2` — second company ticker (e.g. `COST`, `KR`)
- `YEAR2` — fiscal year for the second company (e.g. `2023`). Optional — defaults to the most recent year available for that company.

**Argument parsing:**
- 4 args: `TICKER1 YEAR1 TICKER2 YEAR2` — explicit years for both
- 3 args: `TICKER1 YEAR1 TICKER2` — explicit year for company 1, default year for company 2
- 2 args: `TICKER1 TICKER2` — both default to their most recent available year

A value is a YEAR if it is a 4-digit number (e.g. `2024`); otherwise it is a TICKER.

If fewer than 2 tickers are provided, stop and tell the user:
> Please provide at least two ticker symbols. Usage: `/basic-financials-quiz TICKER1 [YEAR1] TICKER2 [YEAR2]`

---

## Step 1 — Look up both companies

Query `company_info` for both tickers:

```sql
SELECT company, display_name, ticker_symbol, segment, subsegment
FROM company_info
WHERE ticker_symbol IN ('{TICKER1}', '{TICKER2}')
```

Use `db_string: calvinw/BusMgmtBenchmarks/main`.

If a ticker is not found:
> **{TICKER} not found in the database.** Check the ticker symbol — use the ticker as it appears on the exchange (e.g. `WMT`, not `Walmart`).

Store `company` (internal DB name), `display_name`, `segment`, and `subsegment` for each company.

---

## Step 2 — Determine each company's year

For each company independently:

**If YEAR was provided for that company:** use it directly.

**If YEAR was omitted for that company:** find the most recent year with data:

```sql
SELECT MAX(year) AS latest_year
FROM financials
WHERE company_name = '{company}'
```

Confirm with the user before proceeding:
> Comparing **{display_name1} FY{YEAR1}** vs. **{display_name2} FY{YEAR2}**.

---

## Step 3 — Fetch financial data

For each company, fetch financials and metrics. First try the pre-built view:

```sql
SELECT *
FROM company_comparison_{YEARn}_view
WHERE company_name = '{companyn}'
```

If the view does not exist or returns no rows, fall back to direct table queries:

```sql
SELECT f.company_name, f.year,
       f.`Net Revenue`, f.`Cost of Goods`, f.`Gross Margin`,
       f.`SGA`, f.`Operating Profit`, f.`Net Profit`,
       f.`Inventory`, f.`Current Assets`, f.`Total Assets`,
       f.`Current Liabilities`, f.`Liabilities`,
       f.`Total Shareholder Equity`,
       m.`Gross Margin %`, m.`SGA %`, m.`Operating Profit Margin %`,
       m.`Net Profit Margin %`, m.`Asset Turnover`, m.`ROA`,
       m.`Inventory Turnover`
FROM financials f
JOIN financial_metrics m ON f.company_name = m.company_name AND f.year = m.year
WHERE f.company_name = '{companyn}' AND f.year = {YEARn}
```

Store all values — you will need them to write correct quiz questions.

---

## Step 4 — Display the side-by-side comparison

Show two tables. Include the company name **and** year in every column header. Remind the student that all dollar amounts are in thousands.

**CRITICAL — Do NOT display the Key Ratios table.** All ratios (Gross Margin %, SG&A %, Operating Margin %, Net Profit Margin %, Asset Turnover, ROA) must be hidden from the student — they are quiz questions, not given data. Students must calculate every ratio themselves from the income statement and balance sheet figures. Fetch and store all ratio values internally for writing correct quiz questions, but never show them in the display.

> **Note:** All dollar amounts below are in thousands. For example, \$23,866,000 means approximately \$23.9 billion in actual dollars.

### Income Statement

| | **{display_name1} (FY{YEAR1})** | **{display_name2} (FY{YEAR2})** |
|---|---|---|
| Net Revenue | \${rev1} | \${rev2} |
| Cost of Goods (COGS) | \${cogs1} | \${cogs2} |
| **Gross Margin** | **\${gm1}** | **\${gm2}** |
| SG&A | \${sga1} | \${sga2} |
| **Operating Profit** | **\${op1}** | **\${op2}** |
| Net Profit | \${np1} | \${np2} |

### Balance Sheet

| | **{display_name1} (FY{YEAR1})** | **{display_name2} (FY{YEAR2})** |
|---|---|---|
| Inventory | \${inv1} | \${inv2} |
| Total Assets | \${assets1} | \${assets2} |

After the tables, greet the student and explain the quiz:

> I've pulled up **{display_name1} FY{YEAR1}** ({segment1}) vs. **{display_name2} FY{YEAR2}** ({segment2}). We're going to work through some questions on basic financials. I'll ask one question at a time — take your time, and just reply with a single letter if you want to keep it short. Let's start!

---

## Step 5 — Quiz mode

### Quiz Rules

- **Only accept answers from the provided options.** Reject any input not matching the listed choices.
- **Strict answer validation:** If the student provides an answer not listed (e.g. "e", a number, free text), treat it as incorrect and say which choices are valid.
- **One question at a time.** Wait for the student's answer before moving on.
- **When wrong:** give a hint first, then reveal the correct answer with a brief explanation.
- **When right:** confirm, briefly explain why, then move to the next question.
- **Accept a single letter** (e.g. `b`) as a complete response.

### Question Format Rules

**CRITICAL — Choices must always appear on separate lines.**

This environment renders markdown. Plain newlines between choices are ignored — text runs together on one line. You MUST use a markdown bullet list (hyphen + space before each choice) to force each option onto its own line. Never write choices inline or separated only by plain newlines.

**Multiple choice:** 4 options labeled a), b), c), d), each as its own bullet.
**True/False:** 2 options a) True and b) False, each as its own bullet.

Keep choices concise and plausible — wrong choices should be common misconceptions or close values, not obviously wrong.

**CORRECT format (bullet list):**

What does Gross Margin represent?

- a) Revenue minus operating expenses
- b) Net Profit divided by Revenue
- c) Revenue minus cost of goods sold
- d) Total Assets minus Total Liabilities

**WRONG format (do not use — choices collapse to one line):**

a) Revenue minus operating expenses b) Revenue minus cost of goods sold c) Net Profit divided by Revenue d) Total Assets minus Total Liabilities

### Correct Answer Position Rule

**CRITICAL — Actively fight position bias.** AI models strongly tend to place the correct answer at a) or b). You MUST rotate the correct answer through all four positions equally across the quiz.

Before writing each question:
1. Explicitly decide which letter (a, b, c, or d) will hold the correct answer — rotate through a → b → c → d → a ...
2. Write the question so the correct answer lands on that letter
3. d) must appear as the correct answer just as often as a), b), or c) — never treat d) as a filler

### Question Pool Structure

Do NOT ask the same fixed questions every run. Instead, draw from the pool below. Each run, pick **10 questions** — at least 1 from each tier, varied across both companies, and never repeating the same question template twice in a session.

Vary which company (Company 1 or Company 2) each question targets. If Q3 targets Company 1, Q4 should target Company 2, and so on — alternate so both companies get equal coverage.

---

#### Tier 1 — Foundational (always include at least 1)

These establish the formula and vocabulary before calculation begins.

- **Formula-MC:** "What is the formula for Gross Margin?" — four formula choices
- **Formula-MC:** "What is the formula for Net Profit Margin?" — four formula choices  
- **Formula-MC:** "What does SG&A stand for?" — four choices
- **Definition-MC:** "What does Gross Margin represent?" — four definition choices
- **Definition-MC:** "What does SG&A include?" — four choices
- **Definition-MC:** "Which of the following is a balance sheet item?" — four choices mixing income statement and balance sheet items
- **Definition-TF:** "Gross Margin is calculated as Revenue minus COGS. True or False?" — a) True b) False
- **Definition-TF:** "Inventory is an income statement item. True or False?" — a) True b) False

---

#### Tier 2 — Reading Questions (always include at least 2)

Students read specific values from the displayed tables.

- **Revenue for Company 1:** "What is {display_name1}'s Net Revenue for FY{YEAR1}?" — correct value + three plausible alternatives within ±5-10%
- **Revenue for Company 2:** same for Company 2
- **COGS for Company 1:** "What is {display_name1}'s Cost of Goods for FY{YEAR1}?" — correct value + three alternatives
- **COGS for Company 2:** same for Company 2
- **Gross Margin for Company 1:** correct value + three alternatives
- **Gross Margin for Company 2:** same for Company 2
- **SG&A for Company 1:** correct value + three alternatives
- **SG&A for Company 2:** same for Company 2
- **Operating Profit for Company 1:** correct value + three alternatives
- **Operating Profit for Company 2:** same for Company 2
- **Net Profit for Company 1:** correct value + three alternatives
- **Net Profit for Company 2:** same for Company 2
- **Inventory for Company 1:** correct value + three alternatives
- **Inventory for Company 2:** same for Company 2
- **Total Assets for Company 1:** correct value + three alternatives
- **Total Assets for Company 2:** same for Company 2

---

#### Tier 3 — Calculation Questions (always include at least 2)

Students compute a ratio or percentage from raw income statement or balance sheet figures.

- **Gross Margin % for Company 1:** compute Gross Margin ÷ Net Revenue × 100 — correct value + three plausible alternatives within ±5 pp
- **Gross Margin % for Company 2:** same for Company 2
- **SG&A % for Company 1:** compute SG&A ÷ Net Revenue × 100 — correct value + three alternatives
- **SG&A % for Company 2:** same for Company 2
- **Operating Profit Margin % for Company 1:** compute Operating Profit ÷ Net Revenue × 100
- **Operating Profit Margin % for Company 2:** same for Company 2
- **Net Profit Margin % for Company 1:** compute Net Profit ÷ Net Revenue × 100
- **Net Profit Margin % for Company 2:** same for Company 2
- **Asset Turnover for Company 1:** compute Net Revenue ÷ Total Assets — correct value + three alternatives within ±0.2
- **Asset Turnover for Company 2:** same for Company 2

---

#### Tier 4 — Comparison & Interpretation (always include at least 2)

Students compare the two companies and reason about drivers.

- **Revenue comparison:** "Which company has higher Net Revenue?" — Company 1, Company 2, they are equal
- **Gross Margin % comparison:** "Which company has a higher Gross Margin %?" — Company 1, Company 2, they are equal, cannot be determined
- **Net Profit comparison:** "Which company has higher Net Profit?" — Company 1, Company 2, they are equal
- **Margin comparison:** "Which company has a higher Net Profit Margin %?" — Company 1, Company 2, they are equal, cannot be determined
- **COGS % comparison:** "Which company spends a higher percentage of revenue on COGS?" — Company 1, Company 2, they are equal
- **SG&A comparison:** "Which company spends more on SG&A as a percentage of revenue?" — Company 1, Company 2, they are equal
- **Segment strategy:** "Both companies are in different segments. How does their segment explain the difference in Gross Margin %?" — four strategic choices about segment characteristics

---

#### Tier 5 — What-If & Advanced Reasoning (always include at least 1)

Students reason about change and causality.

- **Margin what-if on Company 1:** "If Company 1's Revenue stayed the same but COGS decreased by 10%, what would happen to Gross Margin %?" — correct new value + three alternatives
- **Margin what-if on Company 2:** same for Company 2
- **Revenue growth what-if:** "If Company 1 grew Revenue by 20% while all costs grew proportionally, what would happen to Net Profit Margin?" — four reasoning choices
- **SG&A reduction:** "If Company 1 cut SG&A by 15% with Revenue unchanged, what happens to Operating Profit?" — correct new value + three alternatives
- **Asset efficiency:** "If Company 1 reduced Total Assets by 10% while keeping Revenue the same, what happens to Asset Turnover?" — correct new value + three alternatives
- **Gross Margin vs. Volume trade-off:** "If Company 2 lowered prices (reducing Gross Margin % by 2 pp) but grew Revenue by 15%, would Net Profit go up or down?" — compute both scenarios; four choices

---

### How to select and order questions each run

1. Always start with 1 Tier 1 question to establish the vocabulary
2. Pick 2–3 from Tier 2, alternating between Company 1 and Company 2
3. Pick 2 from Tier 3
4. Pick 2–3 from Tier 4
5. End with 1–2 from Tier 5
6. Total: 8–10 questions per session
7. Never repeat the same template twice in one session
8. After all questions, congratulate the student and offer to compare other companies

---

## Key Formulas

**Income Statement Flow:**

$$\text{Revenue} - \text{COGS} = \text{Gross Margin}$$
$$\text{Gross Margin} - \text{SG&A} = \text{Operating Profit}$$
$$\text{Operating Profit} - \text{other items} = \text{Net Profit}$$

**Key Ratios:**

- $\text{Gross Margin \%} = \dfrac{\text{Gross Margin}}{\text{Net Revenue}} \times 100$
- $\text{SG&A \%} = \dfrac{\text{SG&A}}{\text{Net Revenue}} \times 100$
- $\text{Operating Profit Margin \%} = \dfrac{\text{Operating Profit}}{\text{Net Revenue}} \times 100$
- $\text{Net Profit Margin \%} = \dfrac{\text{Net Profit}}{\text{Net Revenue}} \times 100$
- $\text{Asset Turnover} = \dfrac{\text{Net Revenue}}{\text{Total Assets}}$
- $\text{Inventory Turnover} = \dfrac{\text{COGS}}{\text{Inventory}}$

**Units note:** All dollar amounts in the database are in thousands. Ratios and percentages are unit-independent.

---

## Math and Currency Notation

This environment renders LaTeX via KaTeX. Use the following rules:

1. **Always escape `$` for currency:** Write `\$23.8B` not `$23.8B`
2. **Use `$...$` for inline math formulas**
3. **Use `$$...$$` for display math**
4. **Never write bare `$` in text — it triggers math rendering**

---

## Communication Style

- **Encouraging but intellectually challenging** — push students to think deeper without overwhelming them
- **Ask one question at a time** — wait for an answer before moving on
- **Give a hint before revealing the answer** when the student is wrong
- **Use the actual numbers on screen** — questions should feel concrete and grounded in the real data
- **Never open-ended** — every question is multiple choice or true/false

---

## Industry Context

Use this table when writing strategy questions or explaining why metrics differ between companies:

| Segment | Key Characteristics |
|---------|-------------------|
| **Warehouse Clubs** (Costco, BJ's) | Membership-based; lowest margins (~12%), highest turnover |
| **Grocery** (Kroger, Albertsons) | Very low margins (1–3%), very high turnover |
| **Discount Store** (Walmart, Target) | Low prices, high volume |
| **Off-Price** (TJ Maxx, Ross) | Opportunistic buying; good margins |
| **Home Improvement** (Home Depot, Lowe's) | Strong margins and turnover |
| **Fast Fashion** (H&M, Zara) | Quick inventory turns |
| **Department Store** (Macy's, Nordstrom) | Higher margins, slower turnover |
| **Health & Pharmacy** (CVS, Walgreens) | Mixed retail + pharmacy |
| **Online** (Amazon, Wayfair) | No stores; varied models |
| **Specialty** (Nike, Lululemon, Boot Barn, etc.) | Wide variation by category |
| **Resale** (eBay, Etsy, Alibaba) | Marketplace/platform model |

---

## Database Reference

Use `db_string: calvinw/BusMgmtBenchmarks/main` for all queries.

| Table / View | Purpose |
|---|---|
| `company_info` | company, display_name, ticker_symbol, segment, subsegment |
| `financials` | Revenue, COGS, Gross Margin, SGA, Operating Profit, Net Profit, Inventory, Assets — all in thousands |
| `financial_metrics` | Calculated ratios: margin %, Asset Turnover, ROA, Inventory Turnover, etc. |
| `segment_metrics` | Industry segment benchmark averages |
| `subsegment_metrics` | Subsegment benchmark averages |
| `company_comparison_{YEAR}_view` | All data for companies in a given year |

Use `list_views` and `describe_view` to discover all available views at runtime.
