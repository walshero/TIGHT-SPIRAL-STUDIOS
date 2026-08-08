#!/usr/bin/env python3
"""
funes-ledger.py - the append tooth. Every gate routes its verdict here.

A gate that runs and does not log is itself a HALT: no silent gates.
The ledger is APPEND-ONLY. It is never rewritten. It is canon for STATE
(what a gate last computed about a file); the founder is canon for practice.

Usage (call at the end of any gate, or via funes-gate.sh):
  python3 funes-ledger.py --file index.html --gate preship-v5 --verdict HALT \
      --detail "16 halts: fonts<18 + dark-missing" --commit 7700f9a --md5 542a18a7

Read back:
  python3 funes-ledger.py --tail 20
  python3 funes-ledger.py --last index.html preship-v5   # latest verdict for a (file,gate)
"""
import sys, os, argparse, datetime

LEDGER = os.environ.get(
    "FUNES_LEDGER",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "FUNES-LEDGER.md"),
)


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def ensure_header():
    if not os.path.exists(LEDGER):
        with open(LEDGER, "w") as f:
            f.write("# FUNES LEDGER - append-only. Canon for gate STATE. Never rewrite.\n")
            f.write("Every gate routes here. A gate that does not log is a HALT.\n")
            f.write("State = the last stamped line for a (file, gate). Founder = canon for practice.\n\n")
            f.write("| stamp (UTC) | file | gate | verdict | detail | commit | md5 |\n")
            f.write("|---|---|---|---|---|---|---|\n")


def append(a):
    ensure_header()
    detail = (a.detail or "").replace("|", "/").replace("\n", " ")[:220]
    row = f"| {now()} | {a.file} | {a.gate} | {a.verdict} | {detail} | {a.commit or ''} | {a.md5 or ''} |\n"
    with open(LEDGER, "a") as f:
        f.write(row)
    print(f"logged: {a.file} {a.gate} {a.verdict}")


def tail(n):
    if not os.path.exists(LEDGER):
        print("(empty ledger)")
        return
    for l in open(LEDGER).read().splitlines()[-n:]:
        print(l)


def last(file, gate):
    hit = None
    if os.path.exists(LEDGER):
        for l in open(LEDGER):
            if l.startswith("| ") and f"| {file} |" in l and f"| {gate} |" in l:
                hit = l
    if hit:
        print(hit)
        return 0
    print(f"NONE - {file}/{gate} never logged. UNVERIFIED. A zero-result is not absence; run the gate.")
    return 2


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--file"); p.add_argument("--gate"); p.add_argument("--verdict")
    p.add_argument("--detail"); p.add_argument("--commit"); p.add_argument("--md5")
    p.add_argument("--tail", type=int); p.add_argument("--last", nargs=2)
    a = p.parse_args()
    if a.tail is not None:
        tail(a.tail)
    elif a.last:
        sys.exit(last(a.last[0], a.last[1]))
    elif a.file and a.gate and a.verdict:
        append(a)
    else:
        print(__doc__)
