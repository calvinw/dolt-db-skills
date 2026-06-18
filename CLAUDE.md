# dolt-db-skills

This repo is for working on skills that manage the **BusMgmtBenchmarks** Dolt database — a financial data project tracking retail company financials from SEC 10-K filings and Yahoo Finance.

Skills are slash commands available through agent execution.

## Skill authoring — master copies live in `.skillshare/`

**The canonical source of truth for all skills is `.skillshare/skills/`.** This is the only place skills should be edited or created. Do not edit skill files anywhere else.

Agent-specific directories (`.claude/skills/`, `.agents/skills/`, `.opencode/skills/`, etc.) are **generated copies** — populated by running `skillshare sync` from `.skillshare/`. They are git-ignored and must never be committed. If a skill file appears outside `.skillshare/`, treat it as stale and refer to `.skillshare/` instead.

To update a skill: edit `.skillshare/skills/<skill-name>/SKILL.md`, then run `skillshare sync` to push the change to all agent directories.

## Available Skills

- `/basic-financials TICKER1 [YEAR1] TICKER2 [YEAR2]` — Interactive financial comparison assistant for undergraduate business students. Each company gets its own fiscal year. Pulls side-by-side income statement, ratio, and balance sheet data from the BusMgmtBenchmarks Dolt database and stays open for student questions about what the numbers mean. Years default to the most recent available for each company if omitted.
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

---

## Skill session files — naming convention and format

When a skill session is run and the user asks to save it, save the transcript inside a subfolder named after the skill, inside `skills_sessions/`. Each skill has its own subfolder:

```
skills_sessions/
  basic-financials/
  find-financials-from-pdfs/
  create-new-company-sql/
  verify-dolt-db-financials/
  create-verified-dolt-db-financials-sql/
  download-new-year-data/
  insert-dolt-db-sql/
```

The file itself follows this naming convention:

```
skills_sessions/{skill-name}/{skill-name}-{args}-v{version}-{user}-{model}-session{n}.md
```

For skills with no arguments, omit the `{args}` segment:

```
skills_sessions/{skill-name}/{skill-name}-v{version}-{user}-{model}-session{n}.md
```

**Examples:**
- `skills_sessions/basic-financials/basic-financials-WMT-2024-TGT-2024-v1.0-calvinw-sonnet-4-6-session1.md`
- `skills_sessions/verify-dolt-db-financials/verify-dolt-db-financials-M-v1.0-calvinw-sonnet-4-6-session1.md`
- `skills_sessions/create-new-company-sql/create-new-company-sql-BOOT-v1.0-calvinw-sonnet-4-6-session1.md`
- `skills_sessions/download-new-year-data/download-new-year-data-WMT-v1.0-calvinw-sonnet-4-6-session2.md`

**Rules:**
- `{skill-name}` — the kebab-case skill name exactly as it appears in the slash command (e.g. `verify-dolt-db-financials`, `create-new-company-sql`)
- `{args}` — all arguments passed to the skill, joined with hyphens in the same order they were given (e.g. `WMT-2024-TGT-2024` for `/basic-financials WMT 2024 TGT 2024`, `M` for `/verify-dolt-db-financials M`, `BOOT` for `/create-new-company-sql BOOT`); omit entirely for skills that take no arguments
- `{version}` — the skill version (e.g. `1.0`, `1.1`); use `1.0` if the SKILL.md has no explicit version field
- `{user}` — the first name or username of the person who ran the session (e.g. `calvinw`)
- `{model}` — the short model name of the AI running the skill (e.g. `sonnet-4-6`, `opus-4-8`)
- `{n}` — a counter starting at 1; increment it when the same skill+args+version+user+model combination has already been saved

**File header format:**

The first line of every session file must be the slash command that was used to invoke the skill, including any argument:

```markdown
# /verify-dolt-db-financials M
**Skill_Version:** 1.0
**Student:** calvinw
**Model:** sonnet-4-6
**Date:** 2026-06-17
```

For skills with no argument, the first line is just the command, e.g. `# /find-financials-from-pdfs`.

**Speaker labels:**

Always use `**AI:**` for the AI's turns and `**User:**` for the user's turns.

**What to include in the file:**

Save only the header and the verbatim conversation that took place while the skill was running — the back-and-forth between `**AI:**` and `**User:**` turns, exactly as they happened. Nothing else. Do not add notes, summaries, meta-comments, or any text that was not part of the actual skill conversation. If the session ended early, just stop — do not add a line explaining that it was incomplete.

**After saving a session file, always run:**

```bash
python3 skills_sessions/generate_sessions.py
```

This updates `sessions.json`, which the Quarto site uses to list sessions. If you skip this step, the new session will not appear in the site.
