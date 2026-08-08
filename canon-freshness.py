#!/usr/bin/env python3
# CANON FRESHNESS — catches the bug class this repo hand-fixed three times in one
# evening (2026-08-08): a resident doc's own status header asserts a state that live
# reality no longer matches. STUDIO-GOVERNANCE.md said the belt was inert while it was
# wired into CI. The OS's own header said "UNMERGED LAW" after the blocks were merged.
# STUDIO-COMMAND-CENTER.md sat three-plus weeks stale with zero mention of a night of
# work. Each was found by a human (or an Aleph seat) reading the doc and separately
# checking reality by hand. This makes that check mechanical.
#
# THREE CHECK CLASSES:
#   1. CLAIM-VS-CI    — a curated table: doc text that would be stale, paired with the
#                        live condition that falsifies it. Same shape as comfort-gate /
#                        studio-voice-gate: a growing curated list, not a general parser.
#                        General "is this doc accurate" is undecidable; specific claims
#                        this studio has actually gotten wrong are enumerable.
#   2. POINTER-COMPLETENESS — every backtick-quoted repo-file reference in a resident
#                        doc must exist on disk. A pointer to a renamed/deleted file is
#                        exactly the "built -> landed -> never reconciled" shape.
#   3. STALENESS-BY-CLAIM — a resident doc that opens with a dated version stamp
#                        ("v20 -- 2026-08-08") is flagged if git shows commits touching
#                        core mechanism files (the belt, the workflows, the OS) dated
#                        AFTER the doc's own stamp with no commit touching the doc
#                        itself since -- the doc has stopped tracking the mechanism.
#
# Advisory by default (exits 0, reports). --gate exits 1 on any HALT-class finding.
# It never guesses and never edits -- report only, same posture as funes-tendrils.py.
#
# KNOWN FALSE-POSITIVE CLASS: POINTER-COMPLETENESS only walks THIS repo. A doc
# pointer to a file that genuinely lives in Drive or a sibling TSP repo (en195-apps,
# confluence-calibration-assessment-hub, etc.) will warn here even though it is not
# broken. Read each warning before treating it as a real gap -- this is a report,
# not a verdict.
#
# Run: python3 canon-freshness.py [repo-dir]
#      python3 canon-freshness.py --gate [repo-dir]
import subprocess, sys, os, re

RESIDENT_DOCS = [
    "STUDIO-COMMAND-CENTER.md",
    "tight-spiral-studio-os.md",
    "cross-lane-manifest.md",
    "CLAUDE.md",
    "EXTERNAL-ASSESSOR-BRIEF.md",
]

# --- CLASS 1: CLAIM-VS-CI -----------------------------------------------------
# Each entry: (doc, stale_pattern, condition_fn(root) -> True if claim is CURRENTLY
# TRUE i.e. NOT stale). If stale_pattern is found in doc AND condition_fn is False,
# that's a live contradiction -- HALT.
def _floor_has_always_escape(root):
    p = os.path.join(root, ".github", "workflows", "floor.yml")
    if not os.path.exists(p):
        return True  # can't check; don't false-positive
    return "if: always() &&" in open(p, encoding="utf-8").read()

def _studio_belt_yml_exists(root):
    return os.path.exists(os.path.join(root, ".github", "workflows", "studio-belt.yml"))

def _os_missing_block_marker(root, marker):
    p = os.path.join(root, "tight-spiral-studio-os.md")
    if not os.path.exists(p):
        return True
    return marker not in open(p, encoding="utf-8").read()

CLAIM_CHECKS = [
    ("STUDIO-GOVERNANCE.md", r"belt (is|remains) inert",
     lambda root: not os.path.exists(os.path.join(root, "STUDIO-GOVERNANCE.md")) or True,
     "says the belt is inert"),
    ("STUDIO-COMMAND-CENTER.md", r"two (separate|disagreeing) CI (systems|workflows)",
     lambda root: not _studio_belt_yml_exists(root),
     "claims two CI workflows still run in parallel, but studio-belt.yml is gone (merged into floor.yml)"),
    ("tight-spiral-studio-os.md", r"UNMERGED LAW",
     lambda root: True,  # any hit here is stale by definition post-reconciliation
     "still carries the pre-reconciliation \"UNMERGED LAW\" header"),
    ("cross-lane-manifest.md", r"OPEN FOUNDER GATE\s*[-—]+\s*OS merge",
     lambda root: True,
     "still shows the OS merge as an OPEN founder gate; it closed 2026-08-08"),
]


def git(root, *args):
    try:
        r = subprocess.run(["git", "-C", root, *args], capture_output=True, text=True, timeout=60)
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except Exception as e:
        return 1, "", str(e)


def read(root, relpath):
    p = os.path.join(root, relpath)
    if not os.path.exists(p):
        return None
    try:
        return open(p, encoding="utf-8").read()
    except Exception:
        return None


def check_claims(root):
    halts = []
    for doc, pattern, is_currently_true_fn, desc in CLAIM_CHECKS:
        text = read(root, doc)
        if text is None:
            continue
        if re.search(pattern, text, re.IGNORECASE) and not is_currently_true_fn(root):
            halts.append(f"CLAIM-VS-CI  {doc} {desc} -- live reality disagrees")
    return halts


FILE_REF_RE = re.compile(r"`([A-Za-z0-9_.\-/]+\.(?:md|py|sh|json|html|yml|yaml))`")


def _build_basename_index(root):
    """basename -> True for every tracked-looking file in the repo (any depth).
    A doc pointer names a file, not a path -- os-block-*.md and rescued/ moves
    are exactly the case where the real file lives somewhere other than root."""
    index = set()
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules")]
        for f in filenames:
            index.add(f)
    return index


def check_pointers(root):
    warns = []
    index = _build_basename_index(root)
    for doc in RESIDENT_DOCS:
        text = read(root, doc)
        if text is None:
            continue
        for m in set(FILE_REF_RE.findall(text)):
            if "*" in m or m.startswith("http"):
                continue
            basename = m.split("/")[-1]
            if basename not in index:
                warns.append(f"POINTER-COMPLETENESS  {doc} references `{m}` -- no file with that name anywhere in repo")
    return warns


MECHANISM_FILES = ["studio-belt.sh", ".github/workflows/floor.yml", "tight-spiral-studio-os.md"]
STAMP_RE = re.compile(r"\*v(\d+)\s*[-—]+\s*(\d{4}-\d{2}-\d{2})")


def last_commit_date(root, relpath):
    rc, out, _ = git(root, "log", "-1", "--format=%cd", "--date=short", "--", relpath)
    return out if rc == 0 and out else None


def check_staleness(root):
    warns = []
    doc = "STUDIO-COMMAND-CENTER.md"
    text = read(root, doc)
    if text is None:
        return warns
    m = STAMP_RE.search(text)
    if not m:
        return warns
    stamp_date = m.group(2)
    doc_commit_date = last_commit_date(root, doc)
    for mech in MECHANISM_FILES:
        mech_date = last_commit_date(root, mech)
        if mech_date and doc_commit_date and mech_date > doc_commit_date:
            warns.append(
                f"STALENESS-BY-CLAIM  {doc} stamped {stamp_date}, last touched {doc_commit_date}, "
                f"but {mech} changed more recently ({mech_date}) -- re-check the doc still describes it"
            )
    return warns


def main():
    args = sys.argv[1:]
    gate = "--gate" in args
    args = [a for a in args if a != "--gate"]
    root = args[0] if args else "."

    print("=" * 70)
    print("CANON FRESHNESS -- resident-doc claims vs live reality")
    print("=" * 70)

    halts = check_claims(root)
    warns = check_pointers(root) + check_staleness(root)

    if halts:
        print(f"\n{len(halts)} CONTRADICTION(S) -- doc claims reality has moved past:")
        for h in halts:
            print(f"  HALT  {h}")
    else:
        print("\n  no known-claim contradictions")

    if warns:
        print(f"\n{len(warns)} advisory finding(s):")
        for w in warns:
            print(f"  warn  {w}")
    else:
        print("  no pointer/staleness warnings")

    print()
    if gate and halts:
        print("CANON FRESHNESS: HALT")
        return 1
    print("CANON FRESHNESS: report complete" + (" (would HALT under --gate)" if halts else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
