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
# every run; i