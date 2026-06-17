---
name: insert-dolt-db-sql
version: 0.1
description: Find SQL files in extract/2026/inserts/, clone the BusMgmtBenchmarks Dolt database, execute each SQL file against the local clone, show the diff, then commit and push. Triggered by "/insert-dolt-db-sql" (all files) or "/insert-dolt-db-sql FILE1 FILE2 ..." (specific files).
---

# insert-dolt-db-sql

Find SQL files in `extract/2026/inserts/`, clone the target Dolt database, execute each SQL file, show the diff, and commit+push to DoltHub.

**This skill writes directly to the Dolt database. Use with caution.**

## Prerequisites

- Dolt CLI must be installed (`dolt version`)
- Git-style user config must be set (`dolt config --global --add user.email` and `user.name`)
- The target repo must be public (clone-able without auth). For push access, DoltHub credentials must be configured.

## Inputs

- `/insert-dolt-db-sql` — find and apply all `.sql` files in `extract/2026/inserts/`
- `/insert-dolt-db-sql FILE1 FILE2 ...` — apply only the named files (paths relative to `extract/2026/inserts/`)

## Step 0 — Gather SQL files

List all `.sql` files under `extract/2026/inserts/`. If specific filenames were provided, filter to only those (error if any are not found).

Display the list:

> Found {N} SQL file(s): file1.sql, file2.sql, …

If no files found, stop and tell the user: "No SQL files found in `extract/2026/inserts/`."

## Step 1 — Clone the target database

Create a temporary directory and clone `calvinw/BusMgmtBenchmarks` into it:

```bash
TMPDIR=$(mktemp -d)
dolt clone calvinw/BusMgmtBenchmarks "$TMPDIR"
```

Confirm clone succeeded. If it fails, stop with an error.

## Step 2 — Execute each SQL file

For each SQL file (in alphabetical order):

```bash
dolt sql < "{SQL_FILE_PATH}"
```

Show the output of each execution. If any SQL file produces errors, display them but continue processing remaining files.

## Step 3 — Show the diff

```bash
cd "$TMPDIR"
dolt diff
```

Display the full diff to the user for review.

## Step 4 — Commit

```bash
cd "$TMPDIR"
dolt add -A
dolt commit -am "Apply SQL inserts from extract/2026/inserts/"
```

Show the commit hash.

## Step 5 — Push

```bash
cd "$TMPDIR"
dolt push origin main
```

If push fails due to missing credentials, tell the user to push manually:

> Push requires DoltHub credentials. Run `dolt push origin main` from `{TMPDIR}` manually.

## Step 6 — Cleanup

Remove the temporary clone directory:

```bash
rm -rf "$TMPDIR"
```

## Step 7 — Print summary

---

**Applied {N} SQL file(s) to calvinw/BusMgmtBenchmarks/main:**
- file1.sql
- file2.sql
- …

**Commit:** {hash}

**Diff summary:** {N} rows changed across {N} tables.
