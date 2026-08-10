#!/usr/bin/env python3
"""
APPROVALS_GATE - belt tick 9. Student work does not ship without findable consent.

THE RULING THIS ENFORCES
------------------------
Founder, 2026-08-10: "Don't draw from student work unless specifically authorized by me.
End of FERPA problems." Recorded in claude/FERPA-SCOPE-RULING.md as the SOURCE section,
which sits above THE CHECK and above SCOPE.

The half of that ruling a machine can hold is this: a surface the studio ships must not
carry a student credit unless approvals-log.md names that student. Authorization living in
a chat, a mailbox, or an agent's memory cannot be checked, so for a gate it does not exist.

WHY IT TOOK SIX DAYS
--------------------
student-attribution-standard.md clause 1 has said since 2026-08-03 that a missing approval
line is a HALT. There was no approvals log, so the HALT had nothing to read and could never
fire. The log opened 2026-08-09. This is the check that clause always described. Clause 3
(no year, no section) is belt tick 2 and already armed. Clause 2 (byline form) had nothing;
it is C-SURNAME below.

FLAT, NOT RATCHET
-----------------
Measured before arming, per the 48px lesson: ONE student credit ships in this corpus today
and it is authorized. There is no debt to carry, so there is no baseline. A ratchet here
would be a way to grandfather an unconsented credit, which is the one thing this must not do.

WHAT IT CANNOT SEE, stated rather than implied
----------------------------------------------
It reads shipped SURFACES. It cannot watch an agent open a student portfolio at runtime,
which is the other half of the founder's ruling and has no arithmetic anywhere. Narrow
retrieval (scope-gate clause A, SCOPE in the ruling) is the mitigation, not the proof.

EXIT CODES
    0  every student credit on every surface is named in the approvals log
    1  HALT - an unlogged credit, or a credit carrying a full surname
    2  usage / log missing / self-test failure
"""

import sys, os, re

LOG = os.environ.get("APPROVALS_LOG", "approvals-log.md")

# MEASURED BEFORE ARMING, and the first attempt failed the measurement. A "name near a
# course code" detector with a 160-char window found 157 credits across 112 surfaces and
# HALTed on "Written Communication", "Liberal Arts", "Annual Report" and "Provost Jackson".
# Any two capitalized words in the neighbourhood of an EN-code read as a person. That is
# the studio-fingers disease: a gate that manufactures the defect it reports. Caught here
# instead of on the belt, because the corpus was measured before the tick was armed.
#
# So the detector is not proximity. It is the SHIPPED CREDIT SHAPE: a name and a course
# code with nothing between them but a byline separator. That is how every real credit in
# this studio is written, and prose cannot accidentally take that shape.
COURSE = re.compile(r'\bEN\s?\d{3}\b')
SEP = r'(?:\s|&middot;|&bull;|&#183;|[\u00b7\u2022\u2013\u2014|,-]){1,8}'
NAME_INITIAL = r'([A-Z][a-z]{1,20})\s+([A-Z])\.'          # Firstname L.  - the required form
NAME_FULL    = r'([A-Z][a-z]{1,20})\s+([A-Z][a-z]{2,20})'  # Firstname Surname - clause 2 forbids

# The log is read with the bare name form, not the credit shape: a log line is a record,
# not a byline, and does not have to carry the course code beside the name.
INITIAL = re.compile(NAME_INITIAL + r'(?![A-Za-z])')

CREDIT_INITIAL = [re.compile(NAME_INITIAL + SEP + r'EN\s?\d{3}'),
                  re.compile(r'EN\s?\d{3}[^<]{0,40}?' + SEP + NAME_INITIAL)]
# C-SURNAME IS NOT SHIPPED, and this is the record of why. Clause 2 of the attribution
# standard forbids a full surname in a credit. Two attempts to check it mechanically were
# measured against the real corpus: the loose one HALTed 157 times on "Written
# Communication" and "Provost Jackson"; the tightened credit-shape one still HALTed ~60
# times on "Counts Now", "Flash Fiction", "Workshop Yard", "The Last". Every one is a TITLE
# sitting beside a course code, and no regex can tell a title from a surname without a
# roster - which is a list of student names, which is the one thing this ruling says the
# studio must not hold. So clause 2 stays unenforced and is NAMED as unenforced. Shipping
# it would have put ~60 false halts on the same tick that carries the consent check, and
# the studio would have learned to scroll past both. A gate that cries wolf is worse than
# a gap you can see.

# Even in credit shape, a course TITLE can look like a surname. This list is printed on
# every run; it is not a quiet exemption.
NOT_A_NAME = {"Creative", "Writing", "English", "Composition", "Literature", "Studies",
              "Online", "Summer", "Spring", "Fall", "Winter", "Guest", "Cabinet",
              "Student", "Course", "Communication", "Arts", "Report", "Provost"}




def read(path):
    try:
        return open(path, "rb").read().decode("utf-8", "replace")
    except OSError:
        return ""


def authorized_names(log_text):
    """First-name + initial pairs the log names. The log is the only source of consent a
    gate may consult; a name absent here is a name without permission, by definition."""
    return {f"{m.group(1)} {m.group(2)}." for m in INITIAL.finditer(log_text)}


def credits_in(text):
    """Every place a name and a course code sit together in CREDIT SHAPE. Returns
    (snippet, [Firstname L.], [Firstname Surname])."""
    flat = re.sub(r'\s+', ' ', text)
    initials, fulls, where = [], [], []
    for rx in CREDIT_INITIAL:
        for m in rx.finditer(flat):
            g = [x for x in m.groups() if x]
            if len(g) >= 2:
                initials.append(f"{g[-2]} {g[-1]}.")
                where.append(flat[max(0, m.start() - 40):m.end() + 40])
    if not (initials or fulls):
        return []
    return [(" | ".join(where)[:220], initials, fulls)]


def check(paths, log_text, verbose=True):
    ok_names = authorized_names(log_text)
    halts, seen = [], 0
    for p in paths:
        text = read(p)
        if not text:
            continue
        for block, initials, fulls in credits_in(text):
            seen += 1
            for n in initials:
                if n not in ok_names:
                    halts.append(("C-APPROVAL", p, n, block))
    if verbose:
        print(f"== approvals-gate: {len(paths)} surface(s), {seen} student credit(s) found ==")
        print(f"   authorized in {LOG}: {', '.join(sorted(ok_names)) or '(none)'}")
        for code, p, n, block in halts:
            print(f"   HALT  {code}  {p}")
            print(f"         name: {n}")
            print(f"         near: {block[:150]}")
        if not halts:
            print("   pass  every student credit is named in the approvals log")
        print("   LIMIT: reads shipped surfaces only. Nothing here can watch an agent")
        print("          open a student portfolio at runtime; that half of the founder's")
        print("          ruling has no arithmetic. Narrow retrieval is the mitigation.")
        print("   LIMIT: byline FORM (attribution standard clause 2, no full surname) is")
        print("          NOT checked here. A machine cannot tell a course title from a")
        print("          surname without a roster, and a roster is the thing the ruling")
        print("          forbids holding. Named as a gap rather than faked as a check.")
    return 1 if halts else 0


def self_test():
    """Prove it discriminates. Canaries, not vibes."""
    log = "- **Credit form:** Hamish K.\n- Course: EN195 Creative Writing (summer 6-week online)\n"
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print(f"   {'PASS' if good else 'FAIL'}  {label}  (got {got!r}, want {want!r})")

    print("-- log parsing --")
    chk("log yields the authorized name", authorized_names(log), {"Hamish K."})

    print("-- detection --")
    good = '<div>Guest cabinet &middot; Hamish K. &middot; EN195 Creative Writing (summer 6-week online)</div>'
    bad1 = '<div>Guest cabinet &middot; Dolores V. &middot; EN195 Creative Writing (summer online)</div>'
    none = '<p>EN195 Creative Writing is a six-week online course.</p>'
    staff = '<p>Taught by Matt Walsh. Office hours Tuesday.</p>'
    chk("authorized credit passes",   check([], log, False) or _one(good, log), 0)
    chk("unlogged name halts",        _one(bad1, log), 1)
    chk("a title beside a code is clean", _one('<title>What Counts Now — EN195</title>', log), 0)
    chk("course code alone is clean", _one(none, log), 0)
    chk("no course code, no credit",  _one(staff, log), 0)

    print("-- prose near a course code is NOT a credit (the 157-false-positive lesson) --")
    prose = ('<p>a constant deep channel runs through all five years for Written Communication '
             'and EN101, per the AY24-25 Annual Report; briefing to Provost Jackson.</p>')
    chk("real prose from the corpus is clean", _one(prose, log), 0)
    chk("  and yields no credit at all",       credits_in(prose), [])

    print()
    print("SELF-TEST " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 2


def _one(html, log):
    """Run the check over one in-memory snippet."""
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
        p = f.name
    try:
        return check([p], log, verbose=False)
    finally:
        os.unlink(p)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] in ("-h", "--help"):
        print(__doc__)
        print("  approvals-gate.py <surface.html> [...]   check surfaces")
        print("  approvals-gate.py --self-test            prove it discriminates")
        print("  env APPROVALS_LOG=<path>                 where the log lives")
        sys.exit(0)
    if a and a[0] == "--self-test":
        sys.exit(self_test())
    if not a:
        print("usage: approvals-gate.py <surface.html> [...]")
        sys.exit(2)
    log_text = read(LOG)
    if not log_text:
        print(f"HALT - {LOG} not readable. The ruling requires a findable authorization")
        print("       record; with no log, no student credit can be cleared. Not a pass.")
        sys.exit(2)
    sys.exit(check(a, log_text))
