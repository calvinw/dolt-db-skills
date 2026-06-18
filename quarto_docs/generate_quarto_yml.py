#!/usr/bin/env python3
"""Generate quarto_docs/ content and _quarto.yml from current project files."""

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
QUARTO_DIR = Path(__file__).parent
SESSIONS_DIR = ROOT / "skills_sessions"
PLANS_DIR = ROOT / "plan"
SKILLS_DIR = ROOT / ".skillshare" / "skills"

_WORD_MAP = {"sql": "SQL", "db": "DB", "pdfs": "PDFs"}
_CONJUNCTIONS = {"and", "or", "of", "the", "a", "an", "in", "on", "at", "to", "from"}


def skill_title(folder_name):
    words = folder_name.replace("-", " ").split()
    stop = {"and", "or", "of", "the", "a", "from"}
    return " ".join(
        _WORD_MAP[w] if w in _WORD_MAP else (w if w in stop else w.title())
        for w in words
    )


def session_text(stem, skill_prefix):
    return stem[len(skill_prefix):].lstrip("-")


def plan_text(stem):
    return stem[5:] if stem.startswith("PLAN_") else stem


def format_skill(slug):
    words = slug.lstrip('/').split('-')
    result = []
    for i, w in enumerate(words):
        if w in _WORD_MAP:
            result.append(_WORD_MAP[w])
        elif i > 0 and w in _CONJUNCTIONS:
            result.append(w)
        else:
            result.append(w.capitalize())
    return ' '.join(result)


def format_case_study(raw):
    if not raw:
        return None
    return ' '.join(w.capitalize() for w in raw.replace('_', ' ').split())


def format_model(raw):
    parts = raw.split('-')
    result = []
    i = 0
    while i < len(parts):
        p = parts[i]
        if re.match(r'^\d+$', p):
            ver = [p]
            while i + 1 < len(parts) and re.match(r'^\d+$', parts[i + 1]):
                i += 1
                ver.append(parts[i])
            result.append('.'.join(ver))
        elif re.match(r'^v\d', p):
            result.append(p.upper())
        else:
            result.append(p.capitalize())
        i += 1
    return ' '.join(result)


SKILL_ORDER = [
    "find-financials-from-pdfs",
    "create-new-company-sql",
    "verify-dolt-db-financials",
    "create-verified-dolt-db-financials-sql",
    "download-new-year-data",
    "insert-dolt-db-sql",
]

SESSIONS_SKILL_ORDER = [
    "basic-financials",
    "find-financials-from-pdfs",
    "create-new-company-sql",
    "verify-dolt-db-financials",
    "create-verified-dolt-db-financials-sql",
    "download-new-year-data",
    "insert-dolt-db-sql",
]


def q(path):
    return str(path.relative_to(QUARTO_DIR))


# --- Clean and recreate output dirs ---
for d in [QUARTO_DIR / "skills", QUARTO_DIR / "skills_sessions", QUARTO_DIR / "plan"]:
    shutil.rmtree(d, ignore_errors=True)
    d.mkdir(parents=True, exist_ok=True)

# --- Copy session files ---
session_groups = {}
if SESSIONS_DIR.exists():
    for folder in sorted(SESSIONS_DIR.iterdir()):
        if not folder.is_dir() or folder.name.startswith("."):
            continue
        md_files = sorted(folder.glob("*.md"))
        if not md_files:
            continue
        dest_folder = QUARTO_DIR / "skills_sessions" / folder.name
        dest_folder.mkdir(parents=True, exist_ok=True)
        copies = []
        for f in md_files:
            dest = dest_folder / f.name
            shutil.copy2(f, dest)
            copies.append(dest)
        session_groups[folder.name] = copies

# Copy sessions index
sessions_index = SESSIONS_DIR / "index.md"
if sessions_index.exists():
    shutil.copy2(sessions_index, QUARTO_DIR / "skills_sessions" / "index.md")

# --- Copy plan files ---
plan_copies = []
if PLANS_DIR.exists():
    for f in sorted(PLANS_DIR.glob("PLAN_*.md")):
        dest = QUARTO_DIR / "plan" / f.name
        shutil.copy2(f, dest)
        plan_copies.append(dest)
    plan_index = PLANS_DIR / "index.md"
    if plan_index.exists():
        shutil.copy2(plan_index, QUARTO_DIR / "plan" / "index.md")

# --- Copy skill files ---
all_skill_files = {f.parent.name: f for f in SKILLS_DIR.glob("*/SKILL.md")}
ordered_names = [n for n in SKILL_ORDER if n in all_skill_files]
remaining = sorted(n for n in all_skill_files if n not in SKILL_ORDER)
skill_files = [all_skill_files[n] for n in ordered_names + remaining]

skill_copies = []
for f in skill_files:
    dest = QUARTO_DIR / "skills" / f"{f.parent.name}.md"
    shutil.copy2(f, dest)
    skill_copies.append(dest)

(QUARTO_DIR / "skills" / "index.md").write_text(
    "# Skills\n\nDolt DB management skills for the BusMgmtBenchmarks database.\nBrowse by skill in the sidebar on the left.\n"
)

# --- Write _quarto.yml ---
yml_lines = [
    "project:",
    "  type: website",
    "  output-dir: _site",
    "  render:",
    "    - index.md",
    "    - skills_sessions/index.md",
]
for files in session_groups.values():
    for f in files:
        yml_lines.append(f"    - {q(f)}")
yml_lines.append("    - plan/index.md")
for f in plan_copies:
    yml_lines.append(f"    - {q(f)}")
yml_lines.append("    - skills/index.md")
for f in skill_copies:
    yml_lines.append(f"    - {q(f)}")

yml_lines += [
    "",
    "website:",
    '  title: "Dolt DB Skills"',
    "  navbar:",
    "    left:",
    "      - text: Home",
    "        href: index.md",
    "      - text: Sessions",
    "        href: skills_sessions/index.md",
    "      - text: Plans",
    "        href: plan/index.md",
    "      - text: Skills",
    "        href: skills/index.md",
    "",
    "  sidebar:",
    "    - id: sessions",
    '      title: "Sessions"',
    "      style: docked",
    "      collapse-level: 1",
    "      contents:",
    "        - text: Overview",
    "          href: skills_sessions/index.md",
]
ordered_folders = [n for n in SESSIONS_SKILL_ORDER if n in session_groups] + \
                  sorted(n for n in session_groups if n not in SESSIONS_SKILL_ORDER)
for folder_name in ordered_folders:
    files = session_groups[folder_name]
    yml_lines.append(f'        - section: "{skill_title(folder_name)}"')
    yml_lines.append(f"          contents:")
    for f in files:
        text = session_text(f.stem, folder_name)
        yml_lines.append(f'            - text: "{text}"')
        yml_lines.append(f"              href: {q(f)}")

yml_lines += [
    "",
    "    - id: plans",
    '      title: "Plans"',
    "      style: docked",
    "      contents:",
    "        - text: Overview",
    "          href: plan/index.md",
]
for f in plan_copies:
    yml_lines.append(f'        - text: "{plan_text(f.stem)}"')
    yml_lines.append(f"          href: {q(f)}")

yml_lines += [
    "",
    "    - id: skills",
    '      title: "Skills"',
    "      style: docked",
    "      contents:",
    "        - text: Overview",
    "          href: skills/index.md",
]
GITHUB_REPO = "https://github.com/calvinw/dolt-db-skills/blob/main"

for src, copy in zip(skill_files, skill_copies):
    label = skill_title(src.parent.name)
    github_url = f"{GITHUB_REPO}/.skillshare/skills/{src.parent.name}/SKILL.md"
    yml_lines.append(f'        - text: "{label}"')
    yml_lines.append(f"          href: {q(copy)}")
    yml_lines.append(f'        - text: "(.md)"')
    yml_lines.append(f"          href: {github_url}")

yml_lines += [
    "",
    "format:",
    "  html:",
    "    theme: cosmo",
    "    css: custom.css",
    "    toc: true",
    "    include-after-body: sidebar-tweaks.html",
    "    grid:",
    "      sidebar-width: 400px",
    "      body-width: 2000px",
    "",
]

(QUARTO_DIR / "_quarto.yml").write_text("\n".join(yml_lines))
n_sessions = sum(len(v) for v in session_groups.values())

# --- Write sessions.json ---
sessions_data = []
for md in sorted(SESSIONS_DIR.glob("**/*.md")):
    if md.name == "index.md":
        continue
    md_lines = md.read_text(encoding="utf-8").split("\n")
    m = re.match(r'^#\s+/(\S+)(?:\s+(.+))?', md_lines[0])
    if not m:
        continue
    skill_slug = m.group(1)
    case_raw = m.group(2)
    meta = {}
    for line in md_lines[1:10]:
        mm = re.match(r'^\*\*([^*]+):\*\*\s*(.+)', line)
        if mm:
            key = mm.group(1).strip().lower().replace(' ', '_')
            meta[key] = mm.group(2).strip()
    n_match = re.search(r'session(\d+)', md.stem)
    n = int(n_match.group(1)) if n_match else 1
    command = f'/{skill_slug}' if not case_raw else f'/{skill_slug} {case_raw}'
    sessions_data.append({
        'file':      str(md.relative_to(SESSIONS_DIR)),
        'command':   command,
        'skill':     format_skill(skill_slug),
        'caseStudy': format_case_study(case_raw),
        'student':   meta.get('student', '').capitalize(),
        'model':     format_model(meta.get('model', '')),
        'version':   meta.get('skill_version', ''),
        'n':         n,
        '_slug':     skill_slug,
    })

slug_order = {s: i for i, s in enumerate(SESSIONS_SKILL_ORDER)}
sessions_data.sort(key=lambda s: (slug_order.get(s['_slug'], 999), s['file']))
for session in sessions_data:
    del session['_slug']

(QUARTO_DIR / "sessions.json").write_text(json.dumps(sessions_data, indent=2))

# --- Write plans.json ---
plans_data = []
for md in sorted(PLANS_DIR.glob("PLAN_*.md")):
    md_lines = md.read_text(encoding="utf-8").split("\n")
    title = next(
        (re.match(r"^#\s+(.+)", l).group(1) for l in md_lines[:5] if re.match(r"^#\s+", l)),
        md.stem,
    )
    plans_data.append({"file": md.name, "title": title})
(QUARTO_DIR / "plans.json").write_text(json.dumps(plans_data, indent=2))

print(f"quarto_docs/ generated — {n_sessions} sessions, {len(plan_copies)} plans, {len(skill_copies)} skills.", file=sys.stderr)
