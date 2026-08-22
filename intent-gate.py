#!/usr/bin/env python3
"""
INTENT_GATE - does this build know what it is for?

Built 2026-08-22, the day after the founder halted Funnybonies with
"we are so far from vision", and a search of the repo found
rescued/shelf-2026-07-13/funny-boneys-factory-spec.md: a 28KB panel-reviewed Game
Design Document for that exact game, sitting in the trunk the whole time, never
opened. Seven builds were made against a screenshot instead.

THE THING THIS EXISTS TO CATCH
------------------------------
Every one of those seven wrong builds PASSED EVERY BELT TICK. That is not a
scoring accident, it is a structural hole. The belt's ten ticks grade contrast,
attribution, image ratio, voice, entry paint, retired lines, touch floor, scope,
number sense. All ten are ARTIFACT-QUALITY checks. Not one of them asks whether
the artifact matches its spec, or whether it serves its named player.

So the cheap mechanical floors ran on every push while the expensive judgment
stages of the pipeline (Stage 3 Fidelity, Stage 5 two-ledger playtest) were
skipped by any session that started by writing code. The pipeline is paper. The
belt is automation. Work flows to the automation.

That is also how funny-boneys-factory.html, a mnemonic tool for adults, could be
labeled "the Peter deliverable" in the 2026-08-08 HITL packet and pass clean.
Peter asked for a game for KIDS that makes them laugh. Nothing in the machinery
was ever asked to check.

THE TWO CLAUSES, ONE QUESTION
-----------------------------
CLAUSE A - SPEC-LINK. A build must name the spec it is built against, and that
spec must exist in the repo.
    <meta name="spec-source" content="path/to/spec.md">

CLAUSE B - AUDIENCE. A build must name its player, and that player must be a
player, not a shrug.
    <meta name="audience" content="kids, grades 3 to 6, with real watchers">

WHY ONE TICK AND NOT TWO
Both clauses ask one question: does this file know what it is for and who it is
for? The stock-take proposed them as TICK 0 and TICK 9. Splitting one question
into two ticks is the mistake this repo already made once, the day it grew two
studio-fingers gates. TICK 8 is the precedent: two clauses, one question, one
baseline. Also the recursion loop's rate governor says one graduates per build,
and this is one lesson, not two.

RATCHET ON PRESENCE, FLAT ON CONTRADICTION
Presence RATCHETS. On the day this armed, most surfaces in the trunk carried no
spec-source and no audience. Armed flat it would paint every repo red on every
push and be disarmed inside a week, which is exactly how floor.yml lost its teeth
in July. Today's silence is CARRIED as debt in intent-baseline.json. Only a NEW
surface must declare.

Contradiction is FLAT, zero tolerance, baseline or not:
  - a spec-source that names a file the repo cannot reach (the TICK 8B failure
    class, wearing a different hat)
  - an audience that names nobody: "everyone", "users", "general", "tbd"
  - an audience that shares no word with the spec it points at. When the artifact
    says "kids" and its spec never says kids, that is a visible contradiction and
    arithmetic can see it.

LIMITS (do not read silence here as coverage)
---------------------------------------------
  * This gate reads a DECLARATION. A build can name a spec it does not follow,
    and this gate will pass it. It grades whether intent was declared and whether
    the declaration resolves. It cannot grade fidelity. Fidelity is Stage 3 and
    Stage 5, and those are founder seats, not greps.
  * Two greps do not replace reading the spec before writing code. They make
    skipping it visible, which is the whole ask.
  * The audience word-match is deliberately forgiving: one content word in common
    is enough. It is built to catch "kids" against a spec about adults, not to
    police phrasing.

EXIT CODES
    0  declared, resolves, and does not contradict its spec (or carried as debt)
    1  HALT - a new build declared nothing, or a declaration contradicts itself
    2  usage / unreadable input / self-test failure
"""

import sys, os, re, json, subprocess

BASELINE = os.environ.get("INTENT_BASELINE",
                          os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                       "intent-baseline.json"))

META = lambda n: re.compile(
    r'<meta[^>]*name\s*=\s*["\']' + n + r'["\'][^>]*content\s*=\s*["\']([^"\']*)["\']', re.I)
SPEC_META = META("spec-source")
AUD_META  = META("audience")

# An audience that names nobody. These are the shapes that mean the question was
# never asked. "All ages" is a real editorial choice and is NOT on this list.
NOBODY = {
    "everyone", "anyone", "all", "users", "user", "people", "the public",
    "general", "general public", "the world", "audience", "tbd", "todo",
    "n/a", "na", "none", "any", "whoever", "readers", "visitors",
}

STOP = {"with", "that", "this", "from", "their", "them", "they", "have", "when",
        "into", "over", "under", "some", "most", "real", "some", "very", "than",
        "then", "also", "just", "least", "more", "each", "such", "were", "been",
        "about", "which", "while", "would", "could", "should", "there", "these",
        "those", "other", "using", "used", "does", "doing", "make", "made"}

WORD = re.compile(r"[a-z][a-z'-]{3,}")


# ------------------------------------------------------------------ repo reads
def repo_root():
    try:
        return subprocess.run(["git", "rev-parse", "--show-toplevel"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return os.getcwd()


def repo_name():
    try:
        u = subprocess.run(["git", "remote", "get-url", "origin"],
                           capture_output=True, text=True, check=True).stdout.strip()
        return os.path.basename(u[:-4] if u.endswith(".git") else u)
    except Exception:
        return os.path.basename(repo_root())


def tracked_files(root):
    """Every path git knows about. Worktree, not a ref: a gate must grade what is
       ABOUT to ship, not what already shipped."""
    try:
        out = subprocess.run(["git", "ls-files"], cwd=root,
                             capture_output=True, text=True, check=True).stdout
        return [p for p in out.splitlines() if p]
    except Exception:
        return []


def resolves(cite, allpaths, bynames):
    """A citation resolves if it is an exact tracked path, or if the trunk holds
       that basename anywhere. Same rule scope-gate.py clause B uses, on purpose:
       one repo, one definition of 'reachable'."""
    c = cite.strip().lstrip("./")
    if not c:
        return False
    if c in allpaths:
        return True
    if "/" in c:
        # an ASSERTED path must be real. a bare basename may live anywhere.
        return False
    return bool(bynames.get(os.path.basename(c)))


def read_spec_text(cite, root, allpaths, bynames):
    c = cite.strip().lstrip("./")
    hit = c if c in allpaths else (bynames.get(os.path.basename(c), [None])[0])
    if not hit:
        return ""
    try:
        with open(os.path.join(root, hit), encoding="utf-8", errors="replace") as f:
            return f.read().lower()
    except Exception:
        return ""


# ------------------------------------------------------------------- the grade
def content_words(phrase):
    return [w for w in WORD.findall(phrase.lower()) if w not in STOP]


def grade(path, html, root, allpaths, bynames):
    """Returns (halts, notes). halts is what blocks. notes is what it carried."""
    halts, notes = [], []

    spec = SPEC_META.search(html)
    aud = AUD_META.search(html)
    spec_v = spec.group(1).strip() if spec else ""
    aud_v = aud.group(1).strip() if aud else ""

    # ---- clause A
    if not spec_v:
        notes.append(("A-NO-SPEC",
                      "no <meta name=\"spec-source\">. This build does not name what it "
                      "is built against."))
    elif not resolves(spec_v, allpaths, bynames):
        halts.append("A-SPEC-DANGLES spec-source names '" + spec_v + "' and the repo "
                     "cannot reach it. A spec nobody can fetch is a wish wearing a "
                     "citation's clothes.")

    # ---- clause B
    if not aud_v:
        notes.append(("B-NO-AUDIENCE",
                      "no <meta name=\"audience\">. This build does not name its player."))
        return halts, notes

    primary = aud_v.split(",")[0].strip().lower().rstrip(".")
    if primary in NOBODY or aud_v.strip().lower() in NOBODY:
        halts.append("B-AUDIENCE-NOBODY audience is '" + aud_v + "'. That names nobody. "
                     "An audience everyone belongs to is an audience nobody was asked "
                     "about.")
        return halts, notes

    words = content_words(primary)
    if not words:
        halts.append("B-AUDIENCE-EMPTY audience '" + aud_v + "' carries no nameable "
                     "player in its first phrase.")
        return halts, notes

    # contradiction check only runs when there IS a spec to contradict
    if spec_v and resolves(spec_v, allpaths, bynames):
        text = read_spec_text(spec_v, root, allpaths, bynames)
        if text and not any(w in text for w in words):
            halts.append("B-AUDIENCE-CONTRADICTS build says its player is '" + primary +
                         "' and its own spec (" + spec_v + ") never says any of: " +
                         ", ".join(words) + ". One of the two is wrong.")

    return halts, notes


# ---------------------------------------------------------------------- driver
def load_baseline():
    try:
        with open(BASELINE) as f:
            return json.load(f)
    except Exception:
        return None


def check_one(path, root, allpaths, bynames, base, repo):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            html = f.read()
    except Exception as e:
        print("HALT  cannot read " + path + ": " + str(e))
        return 2

    rel = os.path.relpath(os.path.abspath(path), root).replace(os.sep, "/")
    key = repo + "/" + rel
    halts, notes = grade(path, html, root, allpaths, bynames)

    carried = set()
    if base:
        carried = set(base.get("debt", {}).get(key, []))

    fresh = [n for n in notes if n[0] not in carried]

    print("== intent-gate: " + rel + " ==")
    for h in halts:
        print("   HALT  " + h)
    for code, msg in notes:
        tag = "debt " if code in carried else "NEW  "
        print("   " + tag + " " + code + " " + msg)
    if not halts and not notes:
        print("   clean  names its spec and its player, and they agree")

    if halts:
        print()
        print("HALT - a declaration contradicts itself. This is flat, no baseline "
              "forgives it.")
        return 1
    if fresh:
        print()
        print("HALT - " + str(len(fresh)) + " NEW undeclared build(s). Add the meta tag. "
              "Do not add the file to the baseline to make this quiet: the baseline is "
              "debt that must fall, not a place to put today's shortcut.")
        return 1
    if base is None:
        print("   (no baseline - UNMEAS, not a pass. Freeze one with --freeze.)")
    return 0


def freeze(paths, root, allpaths, bynames, repo):
    debt, n = {}, 0
    for p in paths:
        try:
            with open(p, encoding="utf-8", errors="replace") as f:
                html = f.read()
        except Exception:
            continue
        rel = os.path.relpath(os.path.abspath(p), root).replace(os.sep, "/")
        halts, notes = grade(p, html, root, allpaths, bynames)
        if halts:
            print("   REFUSED to freeze " + rel + ": it HALTS, and a HALT is never debt.")
            for h in halts:
                print("           " + h)
            continue
        if notes:
            debt[repo + "/" + rel] = sorted(c for c, _ in notes)
            n += len(notes)
    rec = {"repo": repo, "count": n, "surfaces": len(debt), "debt": debt}
    with open(BASELINE, "w") as f:
        # compact on purpose: 122 near-identical entries, and a diff nobody can read
        # is a diff nobody reviews. One line, sorted, stable across re-freezes.
        f.write(json.dumps(rec, separators=(",", ":"), sort_keys=True) + "\n")
    print("FROZE " + BASELINE + ": " + str(n) + " undeclared field(s) across " +
          str(len(debt)) + " surface(s).")
    print("This number must fall. It is debt, not a standard.")
    return 0


# ------------------------------------------------------------------ self-test
def self_test():
    """Prove it discriminates. A gate with no canary is a gate nobody has tested."""
    root = "/tmp"
    allpaths = {"specs/real-spec.md", "funny-boneys-factory-spec.md"}
    bynames = {"real-spec.md": ["specs/real-spec.md"],
               "funny-boneys-factory-spec.md": ["funny-boneys-factory-spec.md"]}
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = (got == want)
        ok &= good
        print("   " + ("PASS" if good else "FAIL") + "  " + label +
              "  (got " + repr(got) + ", want " + repr(want) + ")")

    def codes(html, spectext=None):
        real = read_spec_text
        if spectext is not None:
            globals()["read_spec_text"] = lambda *a, **k: spectext
        try:
            h, n = grade("x.html", html, root, allpaths, bynames)
        finally:
            globals()["read_spec_text"] = real
        return sorted([x.split()[0] for x in h] + [c for c, _ in n])

    M = '<meta name="spec-source" content="specs/real-spec.md">'
    A = '<meta name="audience" content="kids, grades 3 to 6">'

    print("-- clause A --")
    chk("silent build is debt, not halt", codes("<html></html>"),
        ["A-NO-SPEC", "B-NO-AUDIENCE"])
    chk("dangling spec halts",
        codes('<meta name="spec-source" content="specs/ghost.md">' + A, "kids play"),
        ["A-SPEC-DANGLES"])
    chk("bare basename resolves",
        codes('<meta name="spec-source" content="funny-boneys-factory-spec.md">' + A,
              "a game for kids"), [])
    chk("asserted wrong path dangles",
        codes('<meta name="spec-source" content="wrong/dir/real-spec.md">' + A, "kids"),
        ["A-SPEC-DANGLES"])

    print("-- clause B --")
    chk("declared and agreeing is clean", codes(M + A, "a game for kids that makes them laugh"), [])
    chk("everyone names nobody",
        codes(M + '<meta name="audience" content="everyone">', "kids"),
        ["B-AUDIENCE-NOBODY"])
    chk("users names nobody",
        codes(M + '<meta name="audience" content="Users">', "kids"),
        ["B-AUDIENCE-NOBODY"])
    chk("THE incident: kids vs an adult spec",
        codes(M + A, "a mnemonic forge for the founder, an adult professor"),
        ["B-AUDIENCE-CONTRADICTS"])
    chk("forgiving on phrasing",
        codes(M + '<meta name="audience" content="first-year students in EN101">',
              "designed for students in the first year seminar"), [])
    chk("all ages is a real choice, not nobody",
        codes(M + '<meta name="audience" content="all ages, read aloud">',
              "written for all ages"), [])
    chk("audience with no spec cannot contradict",
        codes('<meta name="audience" content="kids">'), ["A-NO-SPEC"])

    print("-- word extraction --")
    chk("stopwords dropped", content_words("kids, with real watchers"), ["kids", "watchers"])
    chk("short words dropped", content_words("kids age 8"), ["kids"])

    print()
    print("SELF-TEST " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 2


if __name__ == "__main__":
    argv = sys.argv[1:]
    if argv and argv[0] in ("-h", "--help"):
        print(__doc__)
        print("  intent-gate.py [--ratchet] [--repo=NAME] FILE...   grade surfaces")
        print("  intent-gate.py --freeze FILE...                    write intent-baseline.json")
        print("  intent-gate.py --self-test                         prove it discriminates")
        sys.exit(0)
    if argv and argv[0] == "--self-test":
        sys.exit(self_test())

    do_freeze = "--freeze" in argv
    repo_override = None
    files = []
    for a in argv:
        if a == "--ratchet" or a == "--freeze":
            continue
        if a.startswith("--repo="):
            repo_override = a.split("=", 1)[1]
            continue
        files.append(a)

    if not files:
        print("usage: intent-gate.py [--ratchet] [--repo=NAME] FILE...")
        sys.exit(2)

    root = repo_root()
    repo = repo_override or repo_name()
    allpaths = set(tracked_files(root))
    bynames = {}
    for p in allpaths:
        bynames.setdefault(os.path.basename(p), []).append(p)

    if do_freeze:
        sys.exit(freeze(files, root, allpaths, bynames, repo))

    base = load_baseline()
    rc = 0
    for p in files:
        rc = max(rc, check_one(p, root, allpaths, bynames, base, repo))
    sys.exit(rc)
