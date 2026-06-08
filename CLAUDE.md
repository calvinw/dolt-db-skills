# dolt-db-skills

This repo is for working on skills that manage the **BusMgmtBenchmarks** Dolt database — a financial data project tracking retail company financials from SEC 10-K filings and Yahoo Finance.

Skills are slash commands available through agent execution.

## Available Skills

- `/create-new-company-sql TICKER [CIK]` — Fetches financial data from SEC 10-K filings and Yahoo Finance for a NEW company (2018 through current year), reconciles values, and generates SQL files to insert the company_info row and all financials rows. Writes to `extract/2026/create_company/` and `reports/`. Does NOT write to the database directly.
- `/verify-dolt-db-financials TICKER YEAR` — Fetches financials from SEC, Yahoo Finance, and the Dolt DB, compares them side by side, detects anomalies, and produces reconciled DB-ready values. Saves a report to `reports/`.
- `/create-verified-dolt-db-financials-sql TICKER YEAR` — Generates a `REPLACE INTO` SQL file from the reconciled values produced by `/verify-dolt-db-financials`. Writes to `extract/2026/inserts/`. Does NOT write to the database directly.
- `/download-new-year-data TICKER` — Checks a specific company for newly available fiscal year data not yet in the Dolt DB, cross-checks SEC and Yahoo Finance (American companies) or Yahoo only (non-American), validates consistency against prior years, and generates a `REPLACE INTO` SQL file. Writes to `extract/2026/inserts/new-year-data/`. Does NOT write to the database directly.

Always run `/verify-dolt-db-financials` before `/create-verified-dolt-db-financials-sql` in the same session.

## MCP Servers

The following MCP servers are pre-installed and available:

```
dolt=https://bus-mgmt-databases.mcp.mathplosion.com/mcp-dolt-database/sse
sec-10ks=https://bus-mgmt-databases.mcp.mathplosion.com/mcp-sec-10ks/sse
yfinance-10ks=https://bus-mgmt-databases.mcp.mathplosion.com/mcp-yfinance-10ks/sse
```

Check available MCPs with `/mcp` in your agent.

The target database is `calvinw/BusMgmtBenchmarks/main`.

## Setup

The environment is automatically set up on container creation. Skills are pre-installed and ready to use through agent execution with `claude.sh` or `opencode.sh`.
