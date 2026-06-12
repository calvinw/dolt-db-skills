# dolt-db-skills

This repo is for working on skills that manage the **BusMgmtBenchmarks** Dolt database — a financial data project tracking retail company financials from SEC 10-K filings and Yahoo Finance.

Skills are slash commands (e.g., `/verify-dolt-db-financials`) available through AI tool agents.

## Available Skills

### `/create-new-company-sql TICKER [CIK]`

**Purpose:** Fetch financial data from SEC 10-K filings and Yahoo Finance for a **new** company (2018 through current year), reconcile values, and generate SQL files to insert the `company_info` row and all `financials` rows. Does NOT write to the database directly.

**What it does:**
1. Verifies the company doesn't already exist in the Dolt DB
2. Determines the CIK and company metadata (segment, subsegment, currency)
3. Fetches SEC and Yahoo Finance data for all years 2018–present
4. Reconciles values using anomaly detection rules (SGA composite rules, balance sheet checks)
5. Writes `extract/2026/create_company/{TICKER}_create.sql` — one `INSERT INTO company_info` + one `REPLACE INTO financials` per year
6. Writes a report to `reports/{TICKER}-create.md`

**Usage:** `/create-new-company-sql WSM` or `/create-new-company-sql WSM 107140` (with CIK)

**Note:** For companies already in the DB, use `/verify-dolt-db-financials` instead.

---

### `/verify-dolt-db-financials TICKER [YEAR]`

**Purpose:** Fetch financials from SEC 10-K filings and Yahoo Finance for a company already in the Dolt DB, compare all sources side by side, detect anomalies, and produce reconciled values ready for the database.

**What it does:**
1. Looks up company metadata (CIK, display name) in the Dolt database
2. Fetches income statements and balance sheets from SEC and Yahoo Finance
3. Extracts 13 standard financial fields (Revenue, COGS, Gross Margin, SGA, Operating Profit, Net Profit, Inventory, Current Assets, Total Assets, Current Liabilities, Liabilities, Total Shareholder Equity, Total Liabilities & SE)
4. Runs automated anomaly detection (SGA composite rules, balance sheet mismatches, restatement checks)
5. Presents a side-by-side comparison table showing differences across sources
6. Recommends reconciled values with source attribution
7. Saves a report to `reports/{TICKER}-{YEAR}.md` (or `{TICKER}-all-years.md`)

**Usage:** `/verify-dolt-db-financials WMT 2024` (single year) or `/verify-dolt-db-financials WMT` (all years)

---

### `/create-verified-dolt-db-financials-sql TICKER [YEAR]`

**Purpose:** Generate a SQL `REPLACE INTO` file from the reconciled values produced by `/verify-dolt-db-financials`. Does NOT connect to or write to the database — output is a `.sql` file only.

**What it does:**
1. Reads reconciled values from the prior `/verify-dolt-db-financials` run (must be in the same session)
2. Constructs `REPLACE INTO financials` statements for all reconciled years
3. Writes the SQL to `extract/2026/inserts/`

**Usage:** `/create-verified-dolt-db-financials-sql WMT 2024` (single year) or `/create-verified-dolt-db-financials-sql WMT` (all years)

**Workflow:** Always run `/verify-dolt-db-financials` first, review the reconciled values, then run this skill to generate the SQL file.

---

### `/download-new-year-data TICKER`

**Purpose:** Check a company in the Dolt DB for newly available fiscal year data not yet in the database, validate it for consistency, and generate a SQL INSERT file. For American companies, cross-checks SEC and Yahoo Finance. For non-American companies, uses Yahoo Finance only. Does NOT write to the database directly.

**What it does:**
1. Queries Dolt for the company's latest fiscal year on record
2. Fetches SEC and/or Yahoo Finance to find any newer fiscal year data
3. Cross-checks SEC vs Yahoo values for all 13 fields (American companies)
4. Runs trend consistency checks against prior years in the DB
5. Flags anomalies as `[WARNING]` (investigate) or `[ERROR]` (must resolve before inserting)
6. Writes `extract/2026/inserts/new-year-data/new_year_{TICKER}_{date}.sql`

**Usage:** `/download-new-year-data WMT`

---

### `/insert-dolt-db-sql [FILE1 FILE2 ...]`

**Purpose:** Apply pending SQL files to the BusMgmtBenchmarks Dolt database. Clones the database, executes each SQL file, shows the diff, then commits and pushes. **Writes directly to the Dolt database — use with caution.**

**What it does:**
1. Finds all `.sql` files in `extract/2026/inserts/` (or applies only the specified files)
2. Clones `calvinw/BusMgmtBenchmarks` into a temporary directory
3. Executes each SQL file against the local clone
4. Shows the full diff for review
5. Commits and pushes to DoltHub

**Usage:** `/insert-dolt-db-sql` (all files) or `/insert-dolt-db-sql new-year-data/new_year_WMT_2026-06-05.sql` (specific files)

---

## Typical Workflows

**Add a new company:**
```
/create-new-company-sql TICKER
/insert-dolt-db-sql create_company/TICKER_create.sql
```

**Fix or update an existing company's historical data:**
```
/verify-dolt-db-financials TICKER
/create-verified-dolt-db-financials-sql TICKER
/insert-dolt-db-sql TICKER_multi_insert.sql
```

**Add the latest fiscal year for an existing company:**
```
/download-new-year-data TICKER
/insert-dolt-db-sql new-year-data/new_year_TICKER_DATE.sql
```

---

## Starting Agents

Start an AI agent with permissive tool access using:

```bash
claude.sh      # Starts Claude agent
opencode.sh    # Starts OpenCode agent
```

These scripts invoke the agent with access to Dolt database tools, financial data tools (SEC 10-K, Yahoo Finance), and the installed skills for analyzing and reconciling financial data.

## MCP Servers

```
dolt=https://bus-mgmt-databases.mcp.mathplosion.com/mcp-dolt-database/sse
sec-10ks=https://bus-mgmt-databases.mcp.mathplosion.com/mcp-sec-10ks/sse
yfinance-10ks=https://bus-mgmt-databases.mcp.mathplosion.com/mcp-yfinance-10ks/sse
```

Target database: `calvinw/BusMgmtBenchmarks/main`
