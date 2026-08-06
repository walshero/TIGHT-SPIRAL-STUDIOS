#!/usr/bin/env python3
"""
RESOLVE_CANON - the enforcer.

Built 2026-07-11, after a session spent editing a nine-version-stale file.
Made LANE-AWARE 2026-08-06, after an Aleph pass found four divergences by hand
that this script, being repo-only, could not have seen.

THE FAILURE THIS EXISTS TO PREVENT
----------------------------------
An agent read `confluence-TRUNK.html` off the project shelf (v34), applied two hours of
good work to it, and pushed it over canon (v43). Nine versions clobbered. It was caught
ONLY because someone happened to run a byte-check AFTER the push. Luck.

Six studio rules should have caught it. ONE did, the byte-check, because it is arithmetic.
Every rule that required *remembering* failed: the pointer file (never opened), the
fork-diff rule, the source-first lock, OS section 12.

The studio had already written the diagnosis on 2026-06-29, twelve days earlier:

    "Rich in rules, thin in enforcers. A written floor without an enforcer fails."

This is the enforcer. It is not a rule. It is a REFUSAL.

THE SECOND FAILURE, 2026-08-06 (why this file grew)
---------------------------------------------------
A session-start Aleph pass, run BY HAND, found four things this script was structurally
incapable of finding:

  1. FUNES-LEDGER.md, an APPEND-ONLY file, had lost appends. Repo held 3 rows, the
     project shelf held 5. Gates had been writing the shelf, which is a cache.
  2. FORKING-PATHS-PROTOCOL.md, the document the studio requires reading at session
     start, existed in exactly ONE lane (Drive). Its own header named two homes that
     did not exist. This script never looks at Drive, so it saw nothing.
  3. index.html carried a STANDING preship-gate-v5 HALT and had then drifted +3,013
     bytes with no new gate row. The live front door was shipping off an open halt.
  4. en195-arcade.html had two SHIP verdicts on record against md5 ddcc7a12, while the
     repo holds md5 34bedea0. The gated bytes were not the shipped bytes. The verdicts
     described a file that no longer exists anywhere.

Findings 3 and 4 are the important ones, and note WHAT they have in common: neither is a
lane question. Both are LEDGER questions. The bytes were fine; the RECORD about the bytes
was stale, and nothing compared the two. So this file gained a second half.

    A lane check asks: do my copies agree?
    A ledger check asks: does the RECORD still describe the bytes?

You need both. The studio had neither in code.

THE RULE THIS ENCODES
---------------------
BABEL: name every lane. A lane you did not check is not a lane that is clean; it is a
lane you are BLIND in, and it must be printed BY NAME. A zero-result search is not
evidence of absence.

USAGE
-----
    python3 resolve-canon.py <name>                        # where does this live? what is canon?
    python3 resolve-canon.py <name> --check <local-file>   # is my copy canon? HALT if not.
    python3 resolve-canon.py --audit                       # every file, every lane, all drift
    python3 resolve-canon.py --aleph                       # THE SESSION-START PASS. Run this first.
    python3 resolve-canon.py --aleph --evidence lanes.json # fold in lanes only an agent can reach
    python3 resolve-canon.py --lanes                       # lane roll call: LIVE / BLIND, by name
    python3 resolve-canon.py --ledger <name>               # what does the record say about this file?
    python3 resolve-canon.py --row <file> <gate> <verdict> <detail>   # emit a well-formed ledger row

EVIDENCE FILE
-------------
Drive, Dropbox, OneDrive and iOS Notes are not reachable from a Python process. They are
reachable from an AGENT holding MCP connectors. Rather than pretend those lanes do not
exist (the exact BABEL failure), this script accepts observations gathered elsewhere:

    {
      "generated": "2026-08-06T22:23Z",
      "observations": {
        "FORKING-PATHS-PROTOCOL.md": {
          "drive-post": {"bytes": 3430, "md5": "a731c5c3...", "address": "id 12b8CKf8..."}
        }
      }
    }

Any lane named in BABEL but absent from both the local probes and the evidence file is
reported BLIND, by name, every run. Silence is never taken for agreement.

EXIT CODES
----------
    0  OK - your copy matches canon, or the file is clean
    1  HALT - hash mismatch, you are holding a fossil; or a standing HALT is live
    2  HALT - not found in any lane (or lanes unchecked)
    3  INCOMPLETE - the pass ran but one or more lanes were BLIND. Not a pass. Not a fail.
"""

import sys, os, re, json, hashlib, subprocess, urllib.request, urllib.error

REPO_RAW   = "https://raw.githubusercontent.com/walshero/TIGHT-SPIRAL-STUDIOS/main"
REPO_API   = "https://api.github.com/repos/walshero/TIGHT-SPIRAL-STUDIOS/contents"
NETLIFY    = "https://relaxed-gaufre-a0c223.netlify.app"
SHELF      = "/mnt/project"
OUTPUTS    = "/mnt/user-data/outputs"
LEDGER     = "FUNES-LEDGER.md"

# ---------------------------------------------------------------------------
# LANE PRECEDENCE - earned the hard way, 2026-07-11
#
#   repo    : CANON. Content-addressed. It cannot lie about what it contains.
#   netlify : canon ONLY if the file lives nowhere else (then: SINGLE_LANE, no backup).
#   drive   : holds ADDRESSES, not files. A Drive pointer is a CACHE TO VERIFY, never an
#             oracle to trust - confluence-TRUNK-POINTER.md went stale in under 24 hours.
#   shelf   : NEVER canon. It is a cache and it LAGS. If shelf != repo, the SHELF is wrong.
#   outputs : NOT A LANE. A staging bench that evaporates. Every loss came from here.
# ---------------------------------------------------------------------------
PRECEDENCE = ["repo", "netlify", "shelf"]

# ---------------------------------------------------------------------------
# THE BABEL LIST - added 2026-08-06.
#
# Every lane a TSP file has ever been found in. The point of naming them here is that a
# lane cannot be forgotten: if this process cannot see one, it prints BLIND and the run
# exits 3. Before this list existed, "I checked" meant "I checked repo and shelf" and
# nobody noticed the other six.
#
#   probe = "git"      : readable from a clone
#   probe = "fs"       : readable from the filesystem, if mounted
#   probe = "http"     : readable over the network, if egress allows
#   probe = "evidence" : NOT readable from Python. Requires an agent with MCP connectors
#                        to supply observations. BLIND until it does.
#   probe = "manual"   : no machine path at all. BLIND, permanently, until a human looks.
# ---------------------------------------------------------------------------
BABEL = [
    {"key": "repo",          "probe": "git",      "role": "CANON",
     "note": "git ls-tree origin/main. Content-addressed, cannot lie."},
    {"key": "netlify",       "probe": "http",     "role": "deploy",
     "note": "Sandbox egress blocks *.netlify.app. Failure here is NOT absence."},
    {"key": "shelf",         "probe": "fs",       "role": "cache",
     "note": "Project shelf at /mnt/project. Never canon. It LAGS."},
    {"key": "drive-walshero","probe": "evidence", "role": "archive",
     "note": "Google Drive, walshero. Agent-only."},
    {"key": "drive-post",    "probe": "evidence", "role": "archive",
     "note": "Google Drive, post.massbay. Holds Confluence - Build Versions."},
    {"key": "dropbox",       "probe": "evidence", "role": "archive",
     "note": "Dropbox ns:6905321. Agent-only."},
    {"key": "onedrive",      "probe": "evidence", "role": "archive",
     "note": "OneDrive. No connector wired as of 2026-08-06."},
    {"key": "ios-notes",     "probe": "manual",   "role": "capture",
     "note": "iOS Notes. No machine path. Founder must look."},
    {"key": "sessions",      "probe": "manual",   "role": "volatile",
     "note": "Code sessions, chats, prior cowork runs. Unaddressable after close."},
]

# outputs/ is deliberately NOT in BABEL. It is a bench, not a lane. Naming it as a lane is
# how work gets left there. Every loss the studio has recorded started with that mistake.

BABEL_KEYS = [l["key"] for l in BABEL]


def md5(b: bytes) -> str:
    return hashlib.md5(b).hexdigest()


def fetch(url, timeout=20):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "tsp-resolve-canon"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read()
    except Exception:
        return None


_TREE = {}          # basename -> full repo path. Built once, from git.

def _build_tree():
    """BUG FOUND 2026-07-13 (the second lie): in_repo() used to fetch REPO_RAW/<name>,
    ROOT-LEVEL ONLY, and over the CDN. Anything living in /studio, /archive, /rescued,
    /writerly-moves 404'd, so in_repo said 'absent' and audit() called it an ORPHAN.
    47 deployed files were listed as homeless. It also asked the network for something
    the clone already has on disk, and the raw CDN caches ~5min and will lie anyway.
    GIT IS AUTHORITATIVE, AND IT IS RECURSIVE. Read the tree, once, and match basename."""
    global _TREE
    if _TREE:
        return _TREE
    out = subprocess.run(["git", "ls-tree", "-r", "--name-only", "origin/main"],
                         capture_output=True, text=True, timeout=30)
    for p in out.stdout.splitlines():
        p = p.strip()
        if p:
            _TREE.setdefault(os.path.basename(p), p)   # first wins; root paths sort first
    return _TREE


def git_available():
    try:
        out = subprocess.run(["git", "ls-tree", "-r", "--name-only", "origin/main"],
                             capture_output=True, text=True, timeout=30)
        return bool(out.stdout.strip())
    except Exception:
        return False


def in_repo(name):
    path = _build_tree().get(name)
    if not path:
        return None
    blob = subprocess.run(["git", "show", f"origin/main:{path}"],
                          capture_output=True, timeout=30).stdout
    if not blob:
        return None
    return {"lane": "repo", "bytes": len(blob), "md5": md5(blob),
            "address": f"{REPO_RAW}/{path}", "blob": blob}


def in_netlify(name):
    # NOTE: the container's egress blocks *.netlify.app. This will fail from inside the
    # sandbox and succeed from a machine with open egress. A failure here is NOT proof of
    # absence - that is exactly how a finished game (Dad Energy) got declared lost.
    for path in (f"{NETLIFY}/{name}", NETLIFY + "/"):
        b = fetch(path, timeout=10)
        if b and len(b) > 200:
            return {"lane": "netlify", "bytes": len(b), "md5": md5(b),
                    "address": path, "blob": b, "unreliable": True}
    return None


def on_shelf(name):
    p = os.path.join(SHELF, name)
    if not os.path.exists(p):
        return None
    b = open(p, "rb").read()
    return {"lane": "shelf", "bytes": len(b), "md5": md5(b), "address": p, "blob": b}


# ---------------------------------------------------------------------------
# LANE ROLL CALL
#
# BUG FOUND 2026-08-06 (the third lie, and the quietest): on_shelf() returns None both
# when the file is not on the shelf AND when the shelf is not mounted. Run this script
# from a machine without /mnt/project and EVERY file comes back repo-only, which the old
# code then labelled SINGLE_LANE / no backup. Hundreds of false alarms, or worse, a real
# stranded file buried in them. "Not mounted" and "not there" are different facts and
# must never share a return value.
# ---------------------------------------------------------------------------
def lane_status(evidence=None):
    evidence = evidence or {}
    seen_in_evidence = set()
    for obs in evidence.get("observations", {}).values():
        seen_in_evidence |= set(obs.keys())

    status = {}
    for lane in BABEL:
        k, probe = lane["key"], lane["probe"]
        if probe == "git":
            live = git_available()
            why = "git ls-tree origin/main readable" if live else "no git clone here"
        elif probe == "fs":
            live = os.path.isdir(SHELF)
            why = f"{SHELF} mounted" if live else f"{SHELF} NOT MOUNTED"
        elif probe == "http":
            live = fetch(NETLIFY + "/", timeout=8) is not None
            why = "egress open" if live else "egress blocked or host down (NOT absence)"
        elif probe == "evidence":
            live = k in seen_in_evidence
            why = "supplied by evidence file" if live else "no evidence supplied; agent-only lane"
        else:
            live = False
            why = "no machine path; a human must look"
        status[k] = {"live": live, "why": why, "role": lane["role"], "note": lane["note"]}
    return status


def load_evidence(path):
    if not path:
        return {}
    if not os.path.exists(path):
        print(f"HALT - evidence file not found: {path}")
        print("       Running without it would report reachable lanes as BLIND. Fix the path.")
        sys.exit(2)
    with open(path) as f:
        ev = json.load(f)
    if "observations" not in ev:
        print(f"HALT - evidence file has no 'observations' key: {path}")
        sys.exit(2)
    return ev


# ---------------------------------------------------------------------------
# THE FUNES LEDGER
#
# The ledger is canon for gate STATE. State = the LAST stamped line for a (file, gate).
# Read it from git, not from the working tree: a dirty local ledger is exactly the kind of
# uncommitted edit that vanished on 2026-08-05.
# ---------------------------------------------------------------------------
def read_ledger():
    blob = None
    path = _build_tree().get(LEDGER)
    if path:
        blob = subprocess.run(["git", "show", f"origin/main:{path}"],
                              capture_output=True, timeout=30).stdout
    if not blob and os.path.exists(LEDGER):
        blob = open(LEDGER, "rb").read()
    if not blob:
        return None
    rows = []
    for line in blob.decode("utf-8", "replace").splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 7:
            continue
        if cells[0].startswith("---") or cells[0].lower().startswith("stamp"):
            continue
        rows.append({"stamp": cells[0], "file": cells[1], "gate": cells[2],
                     "verdict": cells[3], "detail": cells[4],
                     "commit": cells[5], "md5": cells[6]})
    return rows


def ledger_state(rows, name):
    """Last stamped line per gate for this file. Order in the file is the order of truth;
    the ledger is append-only, so later lines win."""
    state = {}
    for r in rows:
        if r["file"] == name:
            state[r["gate"]] = r
    return state


HEX32 = re.compile(r"^[0-9a-f]{32}$")

# The ledger cannot stamp its own current hash. Writing the row changes the bytes the row
# would describe. Any self-referential file is structurally guaranteed to fail STALE-STAMP,
# which means the finding carries no information. Found 2026-08-06 on the first real run:
# the ledger was the loudest STALE-STAMP in the report and the only meaningless one.
SELF_REFERENTIAL = {LEDGER}


def ledger_check(rows, name, current_md5):
    """Does the RECORD still describe these bytes? This is the half that was missing.

    UNLEDGERED     - the file exists and no gate has ever stamped it.
    STALE-STAMP    - the last stamp names a different md5. The verdict on record, whatever
                     it says, describes bytes that are not the bytes now shipping.
    STANDING-HALT  - the last verdict for some gate is HALT and has never been cleared.
    UNVERIFIABLE   - the md5 column holds prose instead of a hash. A stamp that cannot be
                     checked is not a weaker stamp, it is a missing one. Found 2026-08-06:
                     a row shipped with 'see-next' in the hash column and no check caught
                     it, because every check compared strings and 'see-next' is a string.
    """
    findings = []
    if rows is None:
        return [("BLIND", "ledger unreadable; cannot check the record")]
    state = ledger_state(rows, name)
    if not state:
        return [("UNLEDGERED", "no gate has ever stamped this file")]
    for gate, r in sorted(state.items()):
        if r["verdict"].upper().startswith("HALT"):
            findings.append(("STANDING-HALT",
                             f"{gate} last said HALT ({r['stamp']}): {r['detail'][:90]}"))
        stamped = r["md5"]
        if stamped and not HEX32.match(stamped):
            findings.append(("UNVERIFIABLE",
                             f"{gate} row at {r['stamp']} carries '{stamped[:24]}' in the md5 "
                             f"column, not a hash. This stamp can never be checked. Repair it."))
            continue
        if name in SELF_REFERENTIAL:
            continue
        if current_md5 and stamped and stamped != current_md5:
            findings.append(("STALE-STAMP",
                             f"{gate} stamped md5 {stamped[:8]} at {r['stamp']}; "
                             f"live bytes are md5 {current_md5[:8]}. "
                             f"The verdict on record does not describe the shipped file."))
    return findings


def ledger_row(fname, gate, verdict, detail, commit="", hexmd5=""):
    """Emit a well-formed row. Pipes in the detail would silently corrupt the table."""
    import datetime
    stamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ")
    clean = detail.replace("|", "/")
    return f"| {stamp} | {fname} | {gate} | {verdict} | {clean} | {commit} | {hexmd5} |"


# ---------------------------------------------------------------------------
# RESOLVE - unchanged behaviour, preserved for every existing caller
# ---------------------------------------------------------------------------
def resolve(name, probe_netlify=True):
    """Check EVERY lane. Never short-circuit - 'found in one' is not 'checked all'."""
    found = {}
    for fn, lane in ((in_repo, "repo"), (on_shelf, "shelf")):
        r = fn(name)
        if r:
            found[lane] = r
    if probe_netlify:
        r = in_netlify(name)
        if r:
            found["netlify"] = r

    if not found:
        return {"verdict": "NOT_FOUND", "found_in": [], "name": name,
                "note": "Absent from repo and shelf. Netlify may be UNREACHABLE from this "
                        "container (egress block) - that is NOT proof of absence. Check by hand."}

    canon_lane = next((l for l in PRECEDENCE if l in found), None)
    canon = found[canon_lane]

    out = {
        "name":        name,
        "found_in":    sorted(found.keys()),
        "canon_lane":  canon_lane,
        "address":     canon["address"],
        "bytes":       canon["bytes"],
        "md5":         canon["md5"],
        "single_lane": len(found) == 1,
        "fossils":     [],
        "verdict":     "OK",
    }

    for lane, r in found.items():
        if lane == canon_lane:
            continue
        if r["md5"] != canon["md5"]:
            delta = r["bytes"] - canon["bytes"]
            flag = ""
            # THE WARRIORS RULE: the repo held a 2,277 B empty stub while the shelf held the
            # real 19,577 B game. NEVER auto-default to the smaller file. If a non-canon lane
            # is substantially BIGGER, canon may be the stub - stop and diff.
            if delta > 2000:
                flag = ("  *** LARGER THAN CANON - canon may be a STUB. DIFF BEFORE ANYTHING. "
                        "(warriors-fantasy-arcade: repo had a 2,277 B stub, shelf had the real "
                        "19,577 B game) ***")
                out["verdict"] = "CHECK_CANON"
            out["fossils"].append(f"{lane}: {r['bytes']} B ({delta:+d}) md5 {r['md5'][:8]}{flag}")

    if out["single_lane"] and out["verdict"] == "OK":
        out["verdict"] = "SINGLE_LANE"
        out["note"] = ("NO BACKUP. One account change and this is gone. "
                        "(Dad Energy lived only on Netlify for weeks - unaudited, unswept, "
                       "and shipping a broken offline floor nobody could see.)")
    return out


# ---------------------------------------------------------------------------
# RESOLVE_LANES - the Babel-wide version. AGREE / DIVERGED / STRANDED / BLIND.
# ---------------------------------------------------------------------------
def resolve_lanes(name, evidence=None, status=None, probe_netlify=False):
    evidence = evidence or {}
    status = status or lane_status(evidence)

    holdings = {}   # lane -> {"bytes":, "md5":, "address":}

    if status["repo"]["live"]:
        r = in_repo(name)
        if r:
            holdings["repo"] = {"bytes": r["bytes"], "md5": r["md5"], "address": r["address"]}
    if status["shelf"]["live"]:
        r = on_shelf(name)
        if r:
            holdings["shelf"] = {"bytes": r["bytes"], "md5": r["md5"], "address": r["address"]}
    if probe_netlify and status["netlify"]["live"]:
        r = in_netlify(name)
        if r:
            holdings["netlify"] = {"bytes": r["bytes"], "md5": r["md5"], "address": r["address"]}

    for lane, obs in (evidence.get("observations", {}).get(name, {}) or {}).items():
        holdings[lane] = {"bytes": obs.get("bytes"), "md5": obs.get("md5"),
                          "address": obs.get("address", "(from evidence)")}

    blind = [k for k in BABEL_KEYS if not status[k]["live"]]

    hashes = {h["md5"] for h in holdings.values() if h.get("md5")}

    # THE COMPARISON FLOOR - added 2026-08-06, after the first real run.
    #
    # STRANDED means "only one lane holds it, so there is no backup." That claim requires
    # at least TWO lanes you could actually have looked in. Run this from a clone with the
    # shelf unmounted and egress blocked, and every one of 533 repo files comes back
    # STRANDED. All 533 lines are arithmetically true and every one of them is noise: the
    # finding is not about the files, it is about the eight blind lanes already printed at
    # the top of the report. A check that fires on everything has told you nothing.
    #
    # Same for AGREE. One lane cannot agree with itself. "hashes are consistent" across a
    # set of size one is a pass the run did not earn, and printing it as clean is the
    # machine claiming ground it never walked.
    checkable = sorted({k for k in BABEL_KEYS if status[k]["live"]} |
                       set(evidence.get("observations", {}).get(name, {}) or {}))

    if not holdings:
        # THE ABSENCE RULE. A zero-result search is not evidence of absence. If ANY lane is
        # blind, the honest verdict is BLIND, not ABSENT. The studio has declared a finished
        # game lost this exact way.
        verdict = "BLIND" if blind else "ABSENT"
    elif len(checkable) < 2:
        # Held, but by the only lane we could see. Not stranded - unwitnessed.
        verdict = "UNWITNESSED"
    elif len(holdings) == 1:
        verdict = "STRANDED"
    elif len(hashes) <= 1:
        verdict = "AGREE"
    else:
        verdict = "DIVERGED"

    canon_lane = next((l for l in PRECEDENCE if l in holdings), None)
    if canon_lane is None and holdings:
        canon_lane = sorted(holdings)[0]

    return {
        "name": name,
        "verdict": verdict,
        "checkable_lanes": checkable,
        "held_by": sorted(holdings.keys()),
        "blind_lanes": blind,
        "canon_lane": canon_lane,
        "md5": holdings[canon_lane]["md5"] if canon_lane else None,
        "bytes": holdings[canon_lane]["bytes"] if canon_lane else None,
        "holdings": holdings,
    }


def check(name, local_path):
    """THE GATE. Is the file in my hand canon? If not: HALT."""
    r = resolve(name)
    if r["verdict"] == "NOT_FOUND":
        print(f"HALT  {name}: not found in any checked lane.")
        print(f"      {r['note']}")
        return 2

    local = open(local_path, "rb").read()
    lmd5, lb = md5(local), len(local)

    print(f"== resolve_canon: {name} ==")
    print(f"   canon  : {r['canon_lane']:8} {r['bytes']:>9,} B  {r['md5']}")
    print(f"   local  : {'(yours)':8} {lb:>9,} B  {lmd5}")

    rows = read_ledger()
    for kind, msg in ledger_check(rows, name, r["md5"]):
        print(f"   LEDGER {kind}: {msg}")

    if lmd5 == r["md5"]:
        print("   MATCH - you are holding canon. Proceed.")
        return 0

    delta = lb - r["bytes"]
    print()
    print("   *** HALT - YOU ARE NOT HOLDING CANON ***")
    print(f"   Your copy differs from {r['canon_lane']} by {delta:+,} bytes.")
    if delta < 0:
        print()
        print("   Your copy is SMALLER. This is the exact shape of the v34-over-v43 clobber:")
        print("   two hours of good work applied to a nine-version-stale file, then pushed")
        print("   over canon. DIFF BEFORE YOU DO ANYTHING ELSE.")
    print(f"   Canon: {r['address']}")
    return 1


def audit():
    """Every file, every lane. Where is the studio drifting RIGHT NOW?"""
    # BUG FOUND 2026-07-11: this used the GitHub CONTENTS API, which is rate-limited for
    # unauthenticated callers. When it 403'd, the repo file list came back EMPTY and every
    # shelf file was reported as an orphan - 111 instead of 48. An audit that lies is the
    # exact disease this whole day was spent curing. GIT IS AUTHORITATIVE. Use it.
    repo_files = set()
    try:
        # BUG FOUND 2026-07-13: this ls-tree was NOT recursive (-r missing). It read only the
        # repo ROOT, so every file living in /studio, /archive, /writerly-moves, /rescued was
        # invisible - 267 real files seen as 85, and 47 files that ARE deployed were reported
        # as shelf-only ORPHANS. Same disease as the Contents-API bug it replaced: an audit
        # that lies, just quieter. A file has a home if it lives ANYWHERE in the tree; match
        # on BASENAME, not on root-level path.
        out_ls = subprocess.run(["git", "ls-tree", "-r", "--name-only", "origin/main"],
                                capture_output=True, text=True, timeout=30)
        repo_paths = {l.strip() for l in out_ls.stdout.splitlines() if l.strip()}
        repo_files = {os.path.basename(p) for p in repo_paths}
    except Exception:
        pass
    if not repo_files:                      # git unavailable: FAIL LOUD, never guess
        print("HALT - cannot read the repo file list (no git). An audit without canon is a")
        print("       list of lies. Run this from a clone of the repo.")
        return 2

    names = set(repo_files)
    if os.path.isdir(SHELF):
        names |= set(os.listdir(SHELF))

    orphans, drift, singles, stubs = [], [], [], []
    for n in sorted(names):
        if n.startswith("."):
            continue
        if n not in repo_files and not os.path.exists(os.path.join(SHELF, n)):
            continue
        r = resolve(n, probe_netlify=False)
        if r["verdict"] == "NOT_FOUND":
            continue
        if r["found_in"] == ["shelf"]:
            orphans.append(f"  {n:<44} {r['bytes']:>9,} B   SHELF-ONLY - no home i