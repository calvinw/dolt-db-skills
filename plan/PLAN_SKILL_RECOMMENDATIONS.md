# Skill Recommendations — BusMgmtBenchmarks Learning Skills

**Date:** 2026-06-17
**Status:** Draft

---

## Current Skills

| Skill | Command | Purpose |
|-------|---------|---------|
| basic-financials | `/basic-financials TICKER1 [YEAR1] TICKER2 [YEAR2]` | Interactive side-by-side comparison of income statement, ratios, and balance sheet for two companies; stays open for student questions |
| find-financials-from-pdfs | `/find-financials-from-pdfs COMPANY NAME` | Extract financials from PDF annual reports for private companies |
| create-new-company-sql | `/create-new-company-sql TICKER [CIK]` | Fetch SEC + Yahoo data for a new company and generate SQL insert files |
| verify-dolt-db-financials | `/verify-dolt-db-financials TICKER [YEAR]` | Compare SEC, Yahoo, and Dolt DB values, detect anomalies, produce reconciled values |
| create-verified-dolt-db-financials-sql | `/create-verified-dolt-db-financials-sql TICKER [YEAR]` | Generate REPLACE INTO SQL from a verified report |
| download-new-year-data | `/download-new-year-data TICKER` | Check for newly available fiscal year data and generate an insert file |
| insert-dolt-db-sql | `/insert-dolt-db-sql [FILE...]` | Clone Dolt DB, run SQL inserts, show diff, commit, and push |

---

## Proposed New Skills

### 1. basic-financials-quiz

**Command:** `/basic-financials-quiz TICKER1 [YEAR1] TICKER2 [YEAR2]`

A structured quiz companion to `basic-financials`. After the student has explored the comparison, this skill generates a set of multiple-choice and fill-in-the-blank questions drawn from the actual data for the two companies. Questions test whether the student can read, calculate, and interpret the income statement and key ratios.

**Example questions:**
- "What was Walmart's gross margin % in FY2024? (a) 18.2% (b) 24.9% (c) 31.0%"
- "Which company kept more of each sales dollar after paying for merchandise?"
- "Calculate Target's operating margin % using the values shown."

**Data source:** BusMgmtBenchmarks Dolt DB (same data as `basic-financials`)

**Output:** Interactive — presents questions one at a time, checks answers, gives immediate feedback with explanations, shows final score.

---

### 2. roa-analysis

**Command:** `/roa-analysis TICKER1 [YEAR1] TICKER2 [YEAR2]`

An interactive skill that teaches Return on Assets (ROA) — how efficiently a company uses its assets to generate profit. Pulls financials and balance sheet data from the Dolt DB, explains the ROA formula, shows historical trends, and compares each company against its segment benchmark.

**Key concepts covered:**
- ROA = Net Profit ÷ Total Assets × 100
- What "asset efficiency" means in plain language
- Why ROA differs across retail segments (grocery vs. specialty vs. warehouse clubs)
- How ROA relates to the income statement (Net Profit) and balance sheet (Total Assets)
- DuPont decomposition: ROA = Net Profit Margin % × Asset Turnover

**Data source:** BusMgmtBenchmarks Dolt DB — `financials`, `financial_metrics`, `segment_metrics`

**Output:** Interactive — presents ROA comparison table, segment benchmark context, historical trend, then stays open for student questions.

---

### 3. roa-analysis-quiz

**Command:** `/roa-analysis-quiz TICKER1 [YEAR1] TICKER2 [YEAR2]`

A structured quiz on ROA concepts, using the same two-company data as `roa-analysis`. Tests students on calculation, interpretation, and comparison of ROA values.

**Example questions:**
- "Calculate Walmart's ROA for FY2024 using Net Profit and Total Assets."
- "Which company was more efficient at turning its assets into profit?"
- "Walmart's Net Profit Margin is 2.9% and its Asset Turnover is 2.61. What is its ROA?"
- "A grocery store typically has a lower ROA than a specialty retailer — true or false? Why?"

**Data source:** BusMgmtBenchmarks Dolt DB

**Output:** Interactive quiz — one question at a time, answer checking, explanations, final score.

---

## Recommendations

### 1. Establish a Teach → Quiz progression pattern

The three new skills above follow a consistent two-step pattern: a teaching skill (`basic-financials`, `roa-analysis`) is always paired with a quiz skill (`basic-financials-quiz`, `roa-analysis-quiz`). This should become the standard pattern for all student-facing financial concept skills. Future skills covering gross margin deep-dives, inventory turnover, DuPont analysis, or liquidity ratios should be built in teach+quiz pairs from the start rather than added later.

### 2. Share a common quiz engine across all quiz skills

As more quiz skills are built, the mechanics of presenting questions, checking answers, tracking scores, and formatting feedback will be identical across all of them. Extract this into a shared quiz framework — either a `references/quiz-engine.md` instruction block that all quiz SKILLs include, or a base quiz skill that others extend. This avoids duplicating the question-loop logic across `basic-financials-quiz`, `roa-analysis-quiz`, and every future quiz skill, and makes it easy to improve the quiz format in one place.
