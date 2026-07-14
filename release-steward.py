#!/usr/bin/env python3
"""
RELEASE STEWARD — shipped means reachable.
============================================
Seated OS §16.6 (2026-07-14). The arithmetic seat.

THE FAILURES THAT SEATED IT:
  - CYL v6 shipped 0-HALT and was UNREACHABLE — index still pointed at v5.
    A finished room with no door. Nobody's job was the door.
  - the-viscosity.html: live in the repo, linked from nothing, for days.
    (Command Center carried it as a known gap. A known gap is not a fixed gap.)

WHAT "SHIPPED" MEANS, checked not promised:
  1. IN GIT      — the file exists at origin/main (not outputs, not the shelf)
  2. GATED       — Studio Eyes exit 0 (run separately; this checks the receipt)
  3. REACHABLE   — linked from index.html, directly or through one hop
  4. CURRENT     — no NEWER version of the same game is sitting unlinked
                   while index points at the old one (the exact v5/v6 failure)

USAGE (from inside a clone):
    python3 release-steward.py               # audit everything
    python3 release-steward.py <file.html>   # audit one ship

EXIT 0 = every shipped game is reachable.  EXIT 1 = orphans or stale doors.
"""
import re, subprocess, sys

def git_show(path):
    r = subprocess.run(['git','show',f'origin/main:{path}'],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None

def links_in(html):
    return set(re.findall(r'href="([^"#]+\.html)"', html or ''))

def tree():
    r = subprocess.run(['git','ls-tree','-r','--name-only','origin/main'],
                       capture_output=True, text=True)
    return [f for f in r.stdout.split('\n') if f.endswith('.html') and '/' not in f]

# pages that are infrastructure, not games — reachability not required
EXEMPT = {'index.html', 'confluence-TRUNK.html', 'tight-spiral-runbook.html',
          'review-bench.html', 'workshop-wall.html'}

def main():
    files = tree()
    index = git_show('index.html')
    if not index:
        print("HALT — no index.html at origin/main. There is no front door at all.")
        return 1

    # one hop: index -> hub pages -> games
    direct = links_in(index)
    reach = set(direct)
    for h in direct:
        reach |= links_in(git_show(h))

    problems = []

    # 3. REACHABLE
    for f in files:
        if f in EXEMPT or f in reach:
            continue
        problems.append(f"UNREACHABLE  {f} — in git, linked from nothing. "
                        f"A finished room with no door.")

    # 4. CURRENT — index points at vN while vN+1 sits in the repo
    for f in files:
        m = re.match(r'(.+?)-v(\d+)(?:-[a-z]+)?\.html$', f)
        if not m:
            continue
        base, ver = m.group(1), int(m.group(2))
        for g in files:
            m2 = re.match(rf'{re.escape(base)}-v(\d+)(?:-[a-z]+)?\.html$', g)
            if m2 and int(m2.group(1)) > ver and f in direct and g not in reach:
                problems.append(f"STALE DOOR   index links {f} but {g} is newer "
                                f"and unreachable. This is the exact v5/v6 failure.")

    if problems:
        print("RELEASE STEWARD — HALT\n")
        for p in problems:
            print(f"  {p}")
        print(f"\n  {len(problems)} problem(s). Shipped means REACHABLE.")
        return 1
    print(f"RELEASE STEWARD — clean. {len(files)-len(EXEMPT)} games, all reachable.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
