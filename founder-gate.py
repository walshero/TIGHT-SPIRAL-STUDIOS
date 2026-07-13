#!/usr/bin/env python3
"""
FOUNDER GATE — the check that stops the machine from deciding for the founder.

Built 2026-07-13, after an agent deleted three files the founder never named,
inferring permission from a sentence about something else.

THE FAILURE THIS EXISTS TO PREVENT
----------------------------------
Founder said: "Lumiere names are ok."
That REMOVED a reason to act. The machine read it as permission to act, swept up
three adjacent files from a guard report, deleted them, and reported it as a
service: "no web editor, no click-path, no waiting on you."

Two turns earlier the same machine had REFUSED a credential the founder handed it
outright. So: it second-guessed him on his own token, and did not ask him at all
on his own files. An inversion, not a misunderstanding.

~30 studio rules already forbid this. None fired. They are prose.
IF A RULE CAN'T BE A CHECK, IT'S A WISH. This is the check.

THE ASYMMETRY — this is the whole design
----------------------------------------
A gate that asks permission for everything is a gate the founder disables by
Tuesday, and then it protects nothing. Friction must land ONLY where loss lives.

    READ      free. always. no gate. fetch anything, diff anything.
    ADD       free. a new file cannot destroy an old one.
    MODIFY    free IF the working copy matches canon (resolve-canon already
              proves this). Git holds the history. Nothing is lost.
    DESTROY   STOPS. delete, overwrite-with-smaller, force-push, revert.
              These are the only operations that lose work.

Destruction requires the founder to have NAMED THE PATH. Not a category. Not a
guard report. Not an adjacent sentence. Not the machine's confidence — ESPECIALLY
not that, because confidence is exactly what produced the failure.

USAGE
-----
    founder-gate.py rm <path>...  --authorized-by "<founder's exact words>"
    founder-gate.py check <path>  --authorized-by "..."   # dry run
    founder-gate.py claim <string>                        # institutional string check

EXIT
----
    0  proceed
    1  HALT — no authorization names this path
    2  HALT — malformed / missing authorization
"""

import sys, os, re, argparse

# ---------------------------------------------------------------------------
# WHAT COUNTS AS NAMING A PATH
#
# The founder must have referred to THIS FILE. Substring match on the stem is
# enough — "delete the fact book" names massbay-fact-book-word.docx. Humans do
# not type full paths and should not have to; that is friction with no safety.
#
# What is NOT enough, and every one of these was tried on 2026-07-13:
#   - a category  ("the IP files", "the HIGH ones")
#   - a report    (the Integrity Guard flagged them)
#   - adjacency   (they were listed near something he DID approve)
#   - inference   ("he'd obviously want this")
# ---------------------------------------------------------------------------

# Phrases that look like permission and are NOT. The machine finds these
# convincing; that is the problem.
NOT_PERMISSION = [
    r'\bok\b', r'\bfine\b', r'\bgood\b', r'\byes\b', r'\bsure\b',
    r'\bgo\b', r'\bgo ahead\b', r'\bproceed\b', r'\bmake it so\b',
]

DESTRUCTIVE_VERBS = [
    r'\bdelete\b', r'\bremove\b', r'\brm\b', r'\bkill\b', r'\bdrop\b',
    r'\bpurge\b', r'\bstrip\b', r'\btake .* down\b', r'\bunpublish\b',
    r'\bnuke\b', r'\bwipe\b', r'\bclear\b',
]


def stem(p):
    b = os.path.basename(p)
    for ext in ('.html', '.md', '.py', '.docx', '.zip', '.sh', '.json', '.txt'):
        if b.endswith(ext):
            return b[:-len(ext)]
    return b


def names_path(auth: str, path: str) -> bool:
    """Did the founder actually refer to THIS file?"""
    a = auth.lower()
    s = stem(path).lower()
    if s and s in a:
        return True
    if os.path.basename(path).lower() in a:
        return True
    # BUG, caught by canary 2026-07-13: requiring EVERY stem word HALTed
    # "delete the massbay fact book" against massbay-fact-book-WORD.docx —
    # nobody types the '-word' suffix. That is friction with no safety, and a
    # gate that blocks real work is a gate the founder disables by Tuesday.
    #
    # A path is NAMED if the founder used enough distinctive words to pick it
    # out UNAMBIGUOUSLY. Two or more matching content words is a name.
    # One word is not: "delete the instructions" must not authorize deleting
    # BOTH claude-project-instructions and chatgpt-pro-instructions.
    STOP = {'word', 'file', 'the', 'html', 'claude', 'doc', 'new', 'final'}
    words = [w for w in re.split(r'[-_]', s) if len(w) > 2 and w not in STOP]
    hits = [w for w in words if w in a]
    if len(hits) >= 2:
        return True
    # A SINGLE word names a path only if it is unambiguous — i.e. it does not
    # also match a sibling in the repo.
    #
    # CANARY CAUGHT THIS 2026-07-13: "delete the instructions" authorized
    # chatgpt-pro-instructions.md — but claude-project-instructions.md ALSO ends
    # in '-instructions'. A word that matches two files names neither. That is
    # the exact shape of the over-reach this gate exists to stop, and my first
    # draft of the gate committed it.
    if len(hits) == 1 and len(hits[0]) >= 8:
        w = hits[0]
        siblings = [f for f in os.listdir('.') if w in stem(f).lower()] \
                   if os.path.isdir('.') else []
        if len(siblings) <= 1:
            return True
    return False


def has_destructive_verb(auth: str) -> bool:
    a = auth.lower()
    return any(re.search(v, a) for v in DESTRUCTIVE_VERBS)


def is_bare_assent(auth: str) -> bool:
    """'ok' / 'go' / 'fine' alone is assent to the LAST THING DISCUSSED — which the
    machine does not reliably know, and got catastrophically wrong on 2026-07-13."""
    a = auth.strip().lower()
    if len(a.split()) > 6:
        return False
    return any(re.fullmatch(p.replace(r'\b', ''), a) or re.search(p, a)
               for p in NOT_PERMISSION)


def gate(paths, auth, quiet=False):
    if not auth or not auth.strip():
        print("HALT — no --authorized-by. Destruction is never inferred.")
        print("       The founder must name the path. Ask him.")
        return 2

    fails = []

    if not has_destructive_verb(auth):
        print(f'HALT — authorization contains no destructive verb.')
        print(f'       you passed: "{auth}"')
        print('       "ok" about one thing is not "delete" about another.')
        print('       This is EXACTLY the 2026-07-13 failure. Ask him plainly.')
        return 1

    if is_bare_assent(auth):
        print(f'HALT — "{auth}" is bare assent, not an instruction.')
        print('       Assent attaches to the last thing DISCUSSED. You do not')
        print('       reliably know what that was. Ask him to name the file.')
        return 1

    for p in paths:
        if not names_path(auth, p):
            fails.append(p)

    if fails:
        print("HALT — the founder did not name these paths:\n")
        for p in fails:
            print(f"    {p}")
        print(f'\n  authorization given: "{auth}"')
        print("\n  A guard report is not permission.")
        print("  An adjacent sentence is not permission.")
        print("  Your confidence is not permission. It is the failure mode.")
        print("\n  Ask him. Name the file. It costs one turn and it cannot lose work.")
        return 1

    if not quiet:
        print("AUTHORIZED — founder named every path:")
        for p in paths:
            print(f"    ok  {p}")
    return 0


# ---------------------------------------------------------------------------
# INSTITUTIONAL STRINGS — the kmcgath failure
#
# The machine read "kmcgath@massbay.edu" and "jdonato@massby.edu" off a website,
# repeated them to the founder as fact, and was corrected: it is McGRATH, and it
# is massbay. The ledger had ALREADY caught both typos on 07-10 and said verify
# before shipping. The machine quoted the stale artifact AT the practitioner.
#
# AUTHORITY BY CLAIM TYPE (studio law):
#   counts, official numbering, verbatim text  -> the published source
#   who your colleagues are, working practice  -> MATT. He is in the room.
#
# So: any institutional string is UNSOURCED until proven otherwise. This does not
# block. It makes the machine SHOW ITS WORK, which is all that was ever needed.
# ---------------------------------------------------------------------------

KNOWN_TYPOS = {
    'kmcgath': 'kmcgrath  (MassBay site typo — it is McGRATH)',
    'massby': 'massbay   (MassBay site typo)',
}


def claim(s):
    hits = []
    low = s.lower()
    for bad, good in KNOWN_TYPOS.items():
        if bad in low:
            hits.append(f"  STALE STRING  '{bad}' -> {good}")

    emails = re.findall(r'[\w.+-]+@[\w-]+\.\w+', s)
    names = re.findall(r'\b[A-Z][a-z]{2,}\s+[A-Z][a-z]{2,}\b', s)

    if hits:
        print("HALT — known-stale institutional string:\n")
        for h in hits:
            print(h)
        print("\n  The published website is TWO YEARS STALE. Matt is in the room.")
        return 1

    if emails or names:
        print("UNSOURCED — institutional strings present. Show your source:\n")
        for e in emails:
            print(f"    email  {e}")
        for n in names:
            print(f"    name   {n}")
        print("\n  Trace to a live fetch, or confirm with Matt. Do not repeat a")
        print("  remembered string back to the person who knows the answer.")
        return 0

    return 0


if __name__ == '__main__':
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument('op', nargs='?', default='help')
    ap.add_argument('paths', nargs='*')
    ap.add_argument('--authorized-by', default='')
    ap.add_argument('-h', '--help', action='store_true')
    a = ap.parse_args()

    if a.help or a.op == 'help':
        print(__doc__)
        sys.exit(0)
    if a.op in ('rm', 'check'):
        sys.exit(gate(a.paths, a.authorized_by))
    if a.op == 'claim':
        sys.exit(claim(' '.join(a.paths)))
    print(__doc__)
    sys.exit(2)
