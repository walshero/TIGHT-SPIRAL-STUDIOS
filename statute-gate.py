#!/usr/bin/env python3
"""statute-gate.py — the LAWS-REGISTRY sweep tooth (ruled 2026-09-17).

The hook principle: a law is only law when it names a hook that fires without
memory. This gate makes the registry itself checkable. WEEKLY hook.

What it checks, v1 — deterministic checks BLOCK, judgment-shaped checks REPORT:

  BLOCK  R1  every script named in the registry exists on disk
  BLOCK  R2  every law the registry marks WIRED-to-PUSH is actually named in
             studio-belt.sh or a .github/workflows file — a WIRED claim that
             the belt does not know is the registry lying
  BLOCK  R3  the registry parses at all: the hooks table and at least 15 law
             rows — an empty parse must never read as a clean sweep
  REPORT R4  REPORT-status rows, by name — report mode is a phase, not a
             destination (floor.yml's own words); these age publicly here
  REPORT R5  DISCIPLINE and WISH rows, counted and named — the number that
             should shrink; the trend is the finding
  REPORT R6  gate-shaped scripts on disk that the registry does not mention —
             the UNCENSUSED backlog, computed instead of estimated

Usage:  statute-gate.py [repo-dir]     (default .)
        statute-gate.py --selftest
Exit 0 = blocks clean (reports may still print). Exit 1 = a BLOCK failed.
"""
import os, re, sys, glob

REG = "LAWS-REGISTRY.md"

def load(repo):
    p = os.path.join(repo, REG)
    if not os.path.exists(p):
        return None
    return open(p, encoding="utf-8").read()

def backticked_scripts(text):
    return sorted(set(re.findall(r'`([\w./-]+\.(?:py|sh))`', text)))

def table_rows(text):
    rows = []
    for line in text.splitlines():
        if line.startswith("|") and "---" not in line and line.count("|") >= 3:
            cells = [c.strip() for c in line.strip("|").split("|")]
            rows.append(cells)
    return rows

def main(argv):
    if len(argv) > 1 and argv[1] == "--selftest":
        return selftest()
    repo = argv[1] if len(argv) > 1 else "."
    text = load(repo)
    fails, reports = [], []

    if text is None:
        print("HALT  R3: %s missing — a registry that is gone must never read as clean" % REG)
        return 1
    rows = table_rows(text)
    law_rows = [r for r in rows if len(r) >= 2 and any(
        k in " ".join(r) for k in ("WIRED", "REPORT", "DISCIPLINE", "WISH", "UNVERIFIED"))]
    if len(law_rows) < 15:
        fails.append("R3: only %d law rows parsed (floor 15) — parser or registry is broken" % len(law_rows))

    # R1 — named scripts exist
    for s in backticked_scripts(text):
        if not os.path.exists(os.path.join(repo, s)):
            fails.append("R1: registry names `%s` and it does not exist on disk" % s)

    # R2 — WIRED-to-PUSH claims are known to the belt or CI
    belt = ""
    bp = os.path.join(repo, "studio-belt.sh")
    if os.path.exists(bp):
        belt = open(bp, encoding="utf-8", errors="replace").read()
    for wf in glob.glob(os.path.join(repo, ".github", "workflows", "*.yml")):
        belt += open(wf, encoding="utf-8", errors="replace").read()
    if not belt:
        fails.append("R2: neither studio-belt.sh nor any workflow found — the PUSH hook itself is unverifiable")
    else:
        push_zone = text.split("Wired to PUSH", 1)[-1].split("### ", 1)[0]
        for s in backticked_scripts(push_zone):
            if os.path.basename(s) not in belt:
                fails.append("R2: `%s` is claimed WIRED to PUSH but the belt and CI never name it" % s)

    # R4 — report-mode rows age here, publicly
    for r in law_rows:
        status = r[-1]
        if re.search(r'\bREPORT\b', status) and "WIRED" not in status:
            law_name = next((c for c in r if c and not c.isdigit() and "REPORT" not in c), r[0])
            reports.append("R4 report-mode (a phase, not a destination): %s" % law_name[:70])

    # R5 — the numbers that should shrink
    n_disc = len(re.findall(r'\bDISCIPLINE\b', text))
    n_wish = len(re.findall(r'\bWISH\b', text))
    reports.append("R5 counts: DISCIPLINE mentions=%d, WISH mentions=%d — the trend, week over week, is the finding"
                   % (n_disc, n_wish))

    # R6 — gate-shaped scripts the registry never mentions
    named = set(os.path.basename(s) for s in backticked_scripts(text))
    on_disk = sorted(os.path.basename(p) for p in
                     glob.glob(os.path.join(repo, "*.py")) + glob.glob(os.path.join(repo, "*.sh"))
                     if re.search(r'gate|sweep|check|guard|fuse|ratchet|floor|fingers|belt|canon|verify',
                                  os.path.basename(p)))
    uncensused = [s for s in on_disk if s not in named]
    reports.append("R6 uncensused: %d gate-shaped scripts on disk the registry never names%s"
                   % (len(uncensused), (": " + ", ".join(uncensused[:8]) + ("…" if len(uncensused) > 8 else ""))
                      if uncensused else ""))

    print("STATUTE GATE — %s law rows parsed, %d scripts named" % (len(law_rows), len(named)))
    for f in fails:
        print("HALT  " + f)
    for r in reports:
        print("note  " + r)
    if not fails:
        print("BLOCKS CLEAN — the registry's deterministic claims hold; the notes are the homework")
    return 1 if fails else 0

def selftest():
    import tempfile, shutil
    d = tempfile.mkdtemp(prefix="statute-selftest-")
    try:
        rows = "\n".join("| %d | law | `ghost-%d.py` | WIRED, flat |" % (i, i) for i in range(16))
        open(os.path.join(d, REG), "w").write("### Wired to PUSH\n" + rows + "\n### next\n")
        open(os.path.join(d, "studio-belt.sh"), "w").write("# empty belt\n")
        rc_bad = main(["x", d])
        for i in range(16):
            open(os.path.join(d, "ghost-%d.py" % i), "w").write("# present\n")
        open(os.path.join(d, "studio-belt.sh"), "w").write(
            "\n".join("ghost-%d.py" % i for i in range(16)))
        rc_good = main(["x", d])
        if rc_bad == 1 and rc_good == 0:
            print("SELFTEST PASS — missing scripts HALT, present+wired scripts pass")
            return 0
        print("SELFTEST FAIL (bad=%s good=%s) — do not trust this gate" % (rc_bad, rc_good))
        return 1
    finally:
        shutil.rmtree(d, ignore_errors=True)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
