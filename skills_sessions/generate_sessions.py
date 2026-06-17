"""
Scans skills_sessions/ for *.md files and writes sessions.json.
Run from the repo root:  python3 skills_sessions/generate_sessions.py
"""

import json, re, sys
from pathlib import Path

here = Path(__file__).parent
ROOT = here.parent

_WORD_MAP = {"sql": "SQL", "db": "DB", "pdfs": "PDFs"}
_CONJUNCTIONS = {"and", "or", "of", "the", "a", "an", "in", "on", "at", "to", "from"}

SKILL_ORDER = [
    "basic-financials",
    "find-financials-from-pdfs",
    "create-new-company-sql",
    "verify-dolt-db-financials",
    "create-verified-dolt-db-financials-sql",
    "download-new-year-data",
    "insert-dolt-db-sql",
]


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


sessions = []

for md in sorted(here.glob('**/*.md')):
    if md.name == 'index.md':
        continue
    lines = md.read_text(encoding='utf-8').split('\n')
    m = re.match(r'^#\s+/(\S+)(?:\s+(.+))?', lines[0])
    if not m:
        continue
    skill_slug = m.group(1)
    case_raw   = m.group(2)
    meta = {}
    for line in lines[1:10]:
        mm = re.match(r'^\*\*([^*]+):\*\*\s*(.+)', line)
        if mm:
            key = mm.group(1).strip().lower().replace(' ', '_')
            meta[key] = mm.group(2).strip()
    n_match = re.search(r'session(\d+)', md.stem)
    n = int(n_match.group(1)) if n_match else 1
    command = f'/{skill_slug}' if not case_raw else f'/{skill_slug} {case_raw}'
    sessions.append({
        'file':      str(md.relative_to(here)),
        'command':   command,
        'skill':     format_skill(skill_slug),
        'caseStudy': format_case_study(case_raw),
        'student':   meta.get('student', '').capitalize(),
        'model':     format_model(meta.get('model', '')),
        'version':   meta.get('skill_version', ''),
        'n':         n,
        '_slug':     skill_slug,
    })

slug_order = {s: i for i, s in enumerate(SKILL_ORDER)}
sessions.sort(key=lambda s: (slug_order.get(s['_slug'], 999), s['file']))
for session in sessions:
    del session['_slug']

out = ROOT / 'quarto_docs' / 'sessions.json'
out.write_text(json.dumps(sessions, indent=2), encoding='utf-8')
print(f'sessions.json: wrote {len(sessions)} sessions', file=sys.stderr)
