#!/usr/bin/env python3
"""
emit-state.py - write STUDIO-STATE.md from what is actually in the tree.

Every drift this studio has had came from a hand-typed number that aged. The
console was carried at 40,429 B in memory and was 42,949 B in the repo. Nobody
lied. A number got old.

So no number here is typed. Bytes come from the filesystem. Gate verdicts come
from running the gate. Name-floor debt comes from grepping. CI runs this on every
push and commits the result, so chat, Claude Code, and Cowork all read one page
that was true a commit ago instead of four memories that were true at different
times.

Usage:  python3 emit-state.py  [--out STUDIO-STATE.md]
Stdlib only. Run from the repo root.
"""

import os, re, sys, subprocess, datetime, json

ROOT   = os.path.dirname(os.path.abspath(__file__))
GATE   = os.path.join(ROOT, 'preship-gate-v4.py')
BASE   = os.path.join(ROOT, 'gate-baseline.json')
OUT    = 'STUDIO-STATE.md'
DEAD   = 'Tight Spiral Studios'          # renamed 2026-07-02
LIVE   = 'Tight Spiral Productions'

SKIP_DIRS  = {'.git', '.github', 'node_modules', 'archive', 'rescued', '.netlify'}
# Owned by the Confluence project, mounted read-only here. Never gated, never
# renamed, never counted as our debt.
RO_MOUNTS  = {'confluence-TRUNK.html'}


def sh(cmd):
    try:
        return subprocess.run(cmd, shell=True, capture_output=True,
                              text=True, cwd=ROOT).stdout.strip()
    except Exception:
        return ''


def walk():
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]
        for f in files:
            if f.startswith('.'):
                continue
            p = os.path.join(base, f)
            yield os.path.relpath(p, ROOT).replace(os.sep, '/'), p


def gate(path):
    """exit 0 = SHIP, exit 1 = HALT, anything else = the gate itself broke."""
    if not os.path.exists(GATE):
        return 'no gate'
    r = subprocess.run([sys.executable, GATE, '--ratchet', path],
                       capture_output=True, text=True, cwd=ROOT)
    if r.returncode == 0:
        return 'SHIP'
    if r.returncode == 1:
        codes = re.findall(r'^\s+([EH][\w-]*)', r.stdout, re.M)
        return 'HALT ' + (', '.join(sorted(set(codes))) if codes else '')
    return 'gate error'


def main():
    out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else OUT

    surfaces, others, dead_name = [], [], []
    for rel, full in walk():
        try:
            size = os.path.getsize(full)
        except OSError:
            continue
        row = (rel, size)
        if rel.endswith('.html'):
            surfaces.append(row)
        else:
            others.append(row)
        if rel in RO_MOUNTS:
            continue
        if rel.endswith(('.html', '.md', '.py', '.js', '.mjs', '.toml', '.css')):
            try:
                t = open(full, encoding='utf-8', errors='ignore').read()
            except OSError:
                continue
            n = t.count(DEAD)
            if n:
                dead_name.append((rel, n))

    surfaces.sort()
    others.sort()
    dead_name.sort()

    verdicts = {rel: gate(rel) for rel, _ in surfaces if rel not in RO_MOUNTS}
    ships    = sum(1 for v in verdicts.values() if v == 'SHIP')

    base = {}
    if os.path.exists(BASE):
        try:
            base = json.load(open(BASE))
        except Exception:
            base = {}
    debt = sum(len(v) for v in base.values())

    sha  = sh('git rev-parse HEAD')[:10] or 'unknown'
    when = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')

    L = []
    L.append('# STUDIO STATE')
    L.append('')
    L.append('**Computed, not remembered.** Written by `emit-state.py` in CI on every')
    L.append('push. Do not hand-edit - the next push overwrites it. If a number here')
    L.append('disagrees with a number in a chat, in a session log, or in memory, **this')
    L.append('one is right and the other one is old.**')
    L.append('')
    L.append('| | |')
    L.append('|---|---|')
    L.append('| commit | `' + sha + '` |')
    L.append('| computed | ' + when + ' |')
    L.append('| surfaces | ' + str(len(surfaces)) + ' |')
    L.append('| gate clean | ' + str(ships) + ' of ' + str(len(verdicts)) + ' |')
    L.append('| baseline debt | ' + str(debt) + ' halts across ' + str(len(base)) + ' files |')
    L.append('| dead studio name | ' + str(sum(n for _, n in dead_name)) +
             ' occurrences in ' + str(len(dead_name)) + ' files |')
    L.append('')
    L.append('## Surfaces')
    L.append('')
    L.append('| file | bytes | gate |')
    L.append('|---|---|---|')
    for rel, size in surfaces:
        v = 'read-only mount' if rel in RO_MOUNTS else verdicts.get(rel, '')
        L.append('| `' + rel + '` | ' + format(size, ',') + ' | ' + v + ' |')
    L.append('')
    L.append('## Name floor')
    L.append('')
    if dead_name:
        L.append('Renamed 2026-07-02. These still say "' + DEAD + '" and should say')
        L.append('"' + LIVE + '". This list only shrinks. A blind sweep is forbidden -')
        L.append('it would touch read-only mounts and fossils.')
        L.append('')
        L.append('| file | occurrences |')
        L.append('|---|---|')
        for rel, n in dead_name:
            L.append('| `' + rel + '` | ' + str(n) + ' |')
    else:
        L.append('Clear. No file carries the dead studio name.')
    L.append('')
    L.append('## Everything else')
    L.append('')
    L.append('| file | bytes |')
    L.append('|---|---|')
    for rel, size in others:
        L.append('| `' + rel + '` | ' + format(size, ',') + ' |')
    L.append('')

    open(os.path.join(ROOT, out), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('wrote ' + out + ': ' + str(len(surfaces)) + ' surfaces, ' +
          str(ships) + ' gate-clean, ' + str(len(dead_name)) + ' files carrying the dead name')


if __name__ == '__main__':
    main()
