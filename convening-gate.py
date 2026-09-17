#!/usr/bin/env python3
"""convening-gate.py — the Convening comparator (OS §6 0.5-A; ruled 2026-09-17).

A build's findings file must exist and carry five signed seats before a draft
is in process. This gate makes that arithmetic instead of discipline.

Usage:
  convening-gate.py <build-name>          check convening/<build>-CONVENING.md
  convening-gate.py --audit               check every file in convening/
  convening-gate.py --template <build>    print a blank findings file
  convening-gate.py --selftest            prove the gate on fixtures in /tmp

Findings-file format (what the gate reads, nothing more):
  A line starting  SENTENCE:  with real content after the colon.
  For each standing seat, a section header  ## SEAT: <name>  whose body holds
  at least 120 characters of answer and a line starting  SIGNED  .
  An unsigned seat, a missing seat, or an empty sentence is a HALT.

Exit 0 = all seats signed. Exit 1 = HALT (reasons printed). Exit 2 = misuse.
The browser-is-the-oracle lesson applies in spirit: this gate checks presence
and signature, never quality — quality is the seats' job, not the parser's.
"""
import os, re, sys, tempfile

SEATS = ["Coordinator", "Stranger", "Osterweil", "Aleph", "Studio Voice"]
MIN_BODY = 120  # chars of real answer a signature must sit under

def check_file(path):
    problems = []
    try:
        src = open(path, encoding="utf-8").read()
    except OSError as e:
        return ["cannot read %s (%s)" % (path, e)]
    m = re.search(r'^SENTENCE:\s*(.+)$', src, re.M)
    if not m or len(m.group(1).strip()) < 20:
        problems.append("no sentence — SENTENCE: line missing or empty; the Convening HALTs at step one")
    sections = re.split(r'^## SEAT:\s*', src, flags=re.M)[1:]
    found = {}
    for sec in sections:
        name_line, _, body = sec.partition("\n")
        found[name_line.strip()] = body
    for seat in SEATS:
        body = found.get(seat)
        if body is None:
            problems.append("seat missing: %s — no '## SEAT: %s' section" % (seat, seat))
            continue
        # the answer is the body with the SIGNED line removed
        signed = re.search(r'^SIGNED\b.*$', body, re.M)
        answer = re.sub(r'^SIGNED\b.*$', '', body, flags=re.M).strip()
        if len(answer) < MIN_BODY:
            problems.append("seat empty: %s — %d chars of answer (floor %d); an empty answer is unsigned"
                            % (seat, len(answer), MIN_BODY))
        if not signed:
            problems.append("seat unsigned: %s — no SIGNED line" % seat)
    extra = [n for n in found if n not in SEATS]
    # extra seats (Conductor, per-build bench) are welcome; only report, never HALT
    return problems, extra if 'extra' in dir() else []

def run_one(path, label):
    res = check_file(path)
    problems = res[0] if isinstance(res, tuple) else res
    extra = res[1] if isinstance(res, tuple) and len(res) > 1 else []
    if problems:
        print("HALT  %s" % label)
        for p in problems:
            print("      - %s" % p)
        return False
    note = ("  (+%d bench seats)" % len(extra)) if extra else ""
    print("pass  %s — 5 standing seats signed%s" % (label, note))
    return True

def template(build):
    lines = ["# CONVENING — %s" % build, "",
             "SENTENCE: <what the player does, and what the founder wants them to notice>", ""]
    for s in SEATS:
        lines += ["## SEAT: %s" % s, "",
                  "<the seat's answer to the sentence, in its own voice>", "",
                  "SIGNED <date>", ""]
    lines += ["## SEAT: Conductor", "", "<sits whenever anything is seen; delete only for an unseen build>",
              "", "SIGNED <date>", ""]
    return "\n".join(lines)

def selftest():
    d = tempfile.mkdtemp(prefix="convening-selftest-")
    good = os.path.join(d, "good-CONVENING.md")
    src = template("selftest")
    src = src.replace("<what the player does, and what the founder wants them to notice>",
                      "The player sorts real ledger lines and notices which laws never fired.")
    src = src.replace("<the seat's answer to the sentence, in its own voice>",
                      "A real answer long enough to clear the floor: " + "the seat speaks. " * 8)
    src = src.replace("<sits whenever anything is seen; delete only for an unseen build>",
                      "Visual constraints set before craft: " + "one light source. " * 8)
    open(good, "w").write(src)
    bad = os.path.join(d, "bad-CONVENING.md")
    open(bad, "w").write(src.replace("## SEAT: Osterweil", "## SEAT: Osterweil-ABSENT")
                            .replace("SENTENCE: The player", "SENTENCE: x #"))
    ok_good = run_one(good, "fixture: complete")
    ok_bad = not run_one(bad, "fixture: missing seat + empty sentence")
    if ok_good and ok_bad:
        print("SELFTEST PASS — the gate passes a signed file and HALTs an unsigned one")
        return 0
    print("SELFTEST FAIL — the gate itself is wrong; do not trust its verdicts")
    return 1

def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    if argv[1] == "--selftest":
        return selftest()
    if argv[1] == "--template":
        if len(argv) < 3: print("--template needs a build name"); return 2
        print(template(argv[2])); return 0
    if argv[1] == "--audit":
        cdir = argv[2] if len(argv) > 2 else "convening"
        if not os.path.isdir(cdir):
            print("no %s/ directory — zero builds are in process under the Convening (that is a fact, not a pass)" % cdir)
            return 0
        files = [f for f in sorted(os.listdir(cdir)) if f.endswith("-CONVENING.md")]
        if not files:
            print("%s/ exists and is empty — zero convened builds" % cdir); return 0
        bad = sum(0 if run_one(os.path.join(cdir, f), f) else 1 for f in files)
        return 1 if bad else 0
    build = argv[1]
    path = os.path.join("convening", "%s-CONVENING.md" % build)
    if not os.path.exists(path):
        print("HALT  %s — no findings file at %s; a draft without one is out of process" % (build, path))
        print("      (convening-gate.py --template %s > %s  starts one)" % (build, path))
        return 1
    return 0 if run_one(path, path) else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))
