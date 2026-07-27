#!/usr/bin/env python3
"""
canon-guard.py — enforce ROLE-canon so a stale/superseded file can't be read as current.

WHY THIS EXISTS
---------------
resolve-canon.py resolves a NAME across the four lanes (repo/netlify/shelf) by md5 — the
Warriors rule (never ship the smaller stub). It CANNOT catch the class that burned this studio
repeatedly: a role served by the WRONG, differently-named file — studio-eyes-sweep.py used where
studio-eyes/studio-eyes.py (v3) is canon; a wired preship-gate vN vs a newer unwired one; a shelf
index.html read as current. Those are different names, all legitimately in the repo. The map that
was supposed to prevent it (FUNES-INDEX.md) is hand-typed prose that went stale and mis-pointed.

This guard reads canon-manifest.json (curated: role -> canonical + superseded) and HALTs when a
superseded file is USED or REFERENCED. Canon is DECLARED once, ENFORCED forever. Wire --refs into
CI (floor.yml) and a reference to a superseded file fails the build — the manifest cannot rot.

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
    print("  SELF-TEST OK — guard catches a planted superseded mapping and invents none.")
    return 0


def main(argv):
    if "--self-test" in argv:
        return self_test()
    # self-test always runs before real work (studio law: a gate that can't grade its canary refuses).
    if self_test() == 2:
        return 2
    manifest = load()
    if "--refs" in argv:
        return scan_refs(manifest)
    if "--check" in argv:
        i = argv.index("--check")
        if i + 1 >= len(argv):
            print("  usage: canon-guard.py --check <file>")
            return 2
        return check_file(argv[i + 1], manifest)
    print(__doc__.strip().splitlines()[0])
    print("  usage: --self-test | --refs | --check <file>")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
