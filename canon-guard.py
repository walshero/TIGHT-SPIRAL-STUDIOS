#!/usr/bin/env python3
"""
canon-guard.py — enforce ROLE-canon so a stale/superseded file can't be read as current.

WHY THIS EXISTS
---------------
resolve-canon.py resolves a NAME across the four lanes (repo/netlify/shelf) by md5 — the
Warriors rule (never ship the smaller stub). It CANNOT catch the class that burned this studio
repeatedly: a role served by the WRONG, differently-named file — the wired render-proof gate
studio-eyes-sweep.py (v4) vs the unwired studio-eyes/studio-eyes.py (v3); a wired preship-gate vN
vs a newer unwired one; a shelf index.html read as current. Those are different names, all
legitimately in the repo. (Note: which of two same-role files is canon is a DECLARATION derived
from wiring + version, not an inference from prose — declaring it backwards is itself the hazard.) The map that
was supposed to prevent it (FUNES-INDEX.md) is hand-typed prose that went stale and mis-pointed.

This guard reads canon-manifest.json (curated: role -> canonical + superseded) and HALTs when a
superseded file is USED or REFERENCED. Canon is DECLARED once, and INTENDED to be ENFORCED in CI.
STATUS 2026-07-26: NOT YET WIRED into CI (floor.yml) — needs the workflow-scope paste. Until then
this guard is ADVISORY and only runs when a human types it; do not claim it enforces (red-team #1).
Known weak spots being hardened: non-recursive/code-only globs miss subdir + .md/.html/.js callers;
substring matching over-/under-counts; the self-test does not exercise the file-scan it ships.
See claude_convening-systems-2026-07-26.md (RED TEAM section) for the full list and the fixes.

Not a rival to resolve-canon.py — its complement. Name-drift -> resolve-canon; role-supersession
-> canon-guard.

USAGE
    canon-guard.py --self-test          gate the guard on a canary (refuses if it can't grade it)
    canon-guard.py --refs               scan repo code/workflows for refs to superseded files; HALT
    canon-guard.py --check <file>       is <file> superseded for a role? print the canonical pointer
EXIT  0 clean · 1 HALT (superseded file used/referenced) · 2 guard self-test failed (do not trust)
"""
import json, os, re, sys, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(ROOT, "canon-manifest.json")
# files that legitimately NAME a superseded file (the map + its own corrections); never flag these.
REF_EXEMPT = {"canon-manifest.json", "canon-guard.py", "claude_FUNES-INDEX.md",
              "claude_seat-playtesting-agents.md", "claude_cyl-playtest-table-2026-07-26.md"}
# where a live reference to a superseded file is a real bug: code + workflows + shell.
REF_GLOBS = ["*.py", ".github/workflows/*.yml", "*.yml", "*.sh"]


def load(path=MANIFEST):
    with open(path) as f:
        return json.load(f)


def superseded_map(manifest):
    """superseded filename (basename) -> (canonical, role, status)."""
    m = {}
    for r in manifest.get("roles", []):
        for s in r.get("superseded", []):
            m[os.path.basename(s)] = (r["canonical"], r["role"], r.get("status", ""))
    return m


def check_file(name, manifest):
    sm = superseded_map(manifest)
    base = os.path.basename(name)
    if base in sm:
        canon, role, status = sm[base]
        print(f"  HALT — {base} is SUPERSEDED for role '{role}'. Canon = {canon}"
              + (f"  [{status}]" if status else ""))
        return 1
    print(f"  OK — {base} is not a declared-superseded file (role-canon says nothing against it).")
    return 0


def scan_refs(manifest):
    sm = superseded_map(manifest)
    if not sm:
        print("  (no superseded files declared yet — nothing to enforce)")
        return 0
    hits = []
    seen = set()
    for pat in REF_GLOBS:
        for path in glob.glob(os.path.join(ROOT, pat)):
            rel = os.path.relpath(path, ROOT)
            if rel in seen or os.path.basename(path) in REF_EXEMPT:
                continue
            seen.add(rel)
            try:
                text = open(path, encoding="utf-8", errors="replace").read()
            except Exception:
                continue
            for supbase, (canon, role, _status) in sm.items():
                if os.path.basename(path) == supbase:
                    continue  # a superseded file naming itself (its own docstring) is not a bug
                for i, line in enumerate(text.splitlines(), 1):
                    if supbase in line:
                        hits.append((rel, i, supbase, canon, role))
    if hits:
        print("  HALT — live references to SUPERSEDED files (fix to the canonical, or split the role):")
        for rel, i, sup, canon, role in hits:
            print(f"     {rel}:{i}  uses {sup}  →  canon for '{role}' is {canon}")
        return 1
    print("  OK — no code/workflow references a superseded file.")
    return 0


def count_refs(basename):
    """How many code/workflow/shell files reference this basename (excluding itself + exempt)."""
    n, where, seen = 0, [], set()
    for pat in REF_GLOBS:
        for path in glob.glob(os.path.join(ROOT, pat)):
            rel = os.path.relpath(path, ROOT)
            b = os.path.basename(path)
            if rel in seen or b in REF_EXEMPT or b == basename:
                continue
            seen.add(rel)
            try:
                if basename in open(path, encoding="utf-8", errors="replace").read():
                    n += 1; where.append(rel)
            except Exception:
                pass
    return n, where


def wiring_verdict(canon_refs, sibling_refs):
    """Pure decision (canary-able): is the DECLARED canonical actually the wired one?"""
    if canon_refs == 0 and any(s > 0 for s in sibling_refs):
        return "HALT"   # canon names an unwired file while a sibling is wired — the 2026-07-26 error
    if canon_refs == 0:
        return "WARN"   # nobody wired: not-yet-wired, or a doc/standalone tool
    return "OK"


def wiring(manifest):
    """Derive canon from WIRING and flag any role whose declared canonical is unwired
    while a sibling is wired. This is the check that catches a manifest declared from prose."""
    bad = 0
    for r in manifest.get("roles", []):
        print(f"  role: {r['role']}")
        canon = r["canonical"]
        cn, cw = count_refs(os.path.basename(canon))
        print(f"     [canonical] {canon}: {cn} ref(s)" + (f"  ({', '.join(cw[:4])})" if cw else "  — UNWIRED"))
        sib_counts = []
        for s in r.get("siblings", []):
            sn, sw = count_refs(os.path.basename(s))
            sib_counts.append(sn)
            print(f"     [sibling]   {s}: {sn} ref(s)" + (f"  ({', '.join(sw[:4])})" if sw else "  — UNWIRED"))
        verdict = wiring_verdict(cn, sib_counts)
        if verdict == "HALT":
            print(f"     HALT — declared canonical is UNWIRED while a sibling is wired. The declaration "
                  f"likely points at the wrong file (the exact error class of 2026-07-26). Re-declare from wiring.")
            bad += 1
        elif verdict == "WARN":
            print(f"     WARN — canonical unwired and no sibling wired (not-yet-wired, or a standalone/doc tool).")
        else:
            print(f"     OK — declared canonical is the wired one ({cn} ref(s)).")
    return 1 if bad else 0


def self_test():
    """Gate the guard on a synthetic canary. If it can't catch a planted superseded ref, REFUSE."""
    fake = {"roles": [{"role": "canary", "canonical": "the-real.py",
                       "superseded": ["the-old.py"], "status": ""}]}
    # 1) --check must flag the superseded name and pass the canonical.
    sm = superseded_map(fake)
    if "the-old.py" not in sm or sm["the-old.py"][0] != "the-real.py":
        print("  SELF-TEST FAIL — guard did not map a planted superseded->canonical.")
        return 2
    # 2) an empty manifest must map nothing (no false positives).
    if superseded_map({"roles": []}):
        print("  SELF-TEST FAIL — guard invented a superseded entry from an empty manifest.")
        return 2
    # 3) the wiring verdict must HALT an unwired canonical beside a wired sibling.
    if not (wiring_verdict(0, [2]) == "HALT" and wiring_verdict(3, [0]) == "OK"
            and wiring_verdict(0, [0]) == "WARN"):
        print("  SELF-TEST FAIL — wiring verdict does not catch an unwired canonical.")
        return 2
    print("  SELF-TEST OK — superseded mapping bites, invents none, and wiring catches an unwired canonical.")
    return 0


def main(argv):
    if "--self-test" in argv:
        return self_test()
    # self-test always runs before real work (studio law: a gate that can't grade its canary refuses).
    if self_test() == 2:
        return 2
    manifest = load()
    if "--wiring" in argv:
        return wiring(manifest)
    if "--refs" in argv:
        return scan_refs(manifest)
    if "--check" in argv:
        i = argv.index("--check")
        if i + 1 >= len(argv):
            print("  usage: canon-guard.py --check <file>")
            return 2
        return check_file(argv[i + 1], manifest)
    print(__doc__.strip().splitlines()[0])
    print("  usage: --self-test | --wiring | --refs | --check <file>")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
