#!/usr/bin/env python3
"""
RESOLVE_CANON — the enforcer.

Built 2026-07-11, after a session spent editing a nine-version-stale file.

THE FAILURE THIS EXISTS TO PREVENT
----------------------------------
An agent read `confluence-TRUNK.html` off the project shelf (v34), applied two hours of
good work to it, and pushed it over canon (v43). Nine versions clobbered. It was caught
ONLY because someone happened to run a byte-check AFTER the push. Luck.

Six studio rules should have caught it. ONE did — the byte-check, because it is arithmetic.
Every rule that required *remembering* failed: the pointer file (never opened), the
fork-diff rule, the source-first lock, OS §12.

The studio had already written the diagnosis on 2026-06-29, twelve days earlier:

    "Rich in rules, thin in enforcers. A written floor without an enforcer fails."

This is the enforcer. It is not a rule. It is a REFUSAL.

USAGE
-----
    python3 resolve-canon.py <name>            # where does this live? what is canon?
    python3 resolve-canon.py <name> --check <local-file>   # is my copy canon? HALT if not.
    python3 resolve-canon.py --audit           # every file, every lane, all drift

EXIT CODES
----------
    0  OK — your copy matches canon, or the file is clean
    1  HALT — hash mismatch, you are holding a fossil
    2  HALT — not found in any lane (or lanes unchecked)
"""

import sys, os, re, json, hashlib, subprocess, urllib.request, urllib.error

REPO_RAW   = "https://raw.githubusercontent.com/walshero/TIGHT-SPIRAL-STUDIOS/main"
REPO_API   = "https://api.github.com/repos/walshero/TIGHT-SPIRAL-STUDIOS/contents"
NETLIFY    = "https://relaxed-gaufre-a0c223.netlify.app"
SHELF      = "/mnt/project"
OUTPUTS    = "/mnt/user-data/outputs"

# ---------------------------------------------------------------------------
# LANE PRECEDENCE — earned the hard way, 2026-07-11
#
#   repo    : CANON. Content-addressed. It cannot lie about what it contains.
#   netlify : canon ONLY if the file lives nowhere else (then: SINGLE_LANE, no backup).
#   drive   : holds ADDRESSES, not files. A Drive pointer is a CACHE TO VERIFY, never an
#             oracle to trust — confluence-TRUNK-POINTER.md went stale in under 24 hours.
#   shelf   : NEVER canon. It is a cache and it LAGS. If shelf != repo, the SHELF is wrong.
#   outputs : NOT A LANE. A staging bench that evaporates. Every loss came from here.
# ---------------------------------------------------------------------------
PRECEDENCE = ["repo", "netlify", "shelf"]


def md5(b: bytes) -> str:
    return hashlib.md5(b).hexdigest()


def fetch(url, timeout=20):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "tsp-resolve-canon"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read()
    except Exception:
        return None


def in_repo(name):
    b = fetch(f"{REPO_RAW}/{name}")
    if not b:
        return None
    return {"lane": "repo", "bytes": len(b), "md5": md5(b),
            "address": f"{REPO_RAW}/{name}", "blob": b}


def in_netlify(name):
    # NOTE: the container's egress blocks *.netlify.app. This will fail from inside the
    # sandbox and succeed from a machine with open egress. A failure here is NOT proof of
    # absence — that is exactly how a finished game (Dad Energy) got declared lost.
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


def resolve(name, probe_netlify=True):
    """Check EVERY lane. Never short-circuit — 'found in one' is not 'checked all'."""
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
                        "container (egress block) — that is NOT proof of absence. Check by hand."}

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
            # is substantially BIGGER, canon may be the stub — stop and diff.
            if delta > 2000:
                flag = ("  *** LARGER THAN CANON — canon may be a STUB. DIFF BEFORE ANYTHING. "
                        "(warriors-fantasy-arcade: repo had a 2,277 B stub, shelf had the real "
                        "19,577 B game) ***")
                out["verdict"] = "CHECK_CANON"
            out["fossils"].append(f"{lane}: {r['bytes']} B ({delta:+d}) md5 {r['md5'][:8]}{flag}")

    if out["single_lane"] and out["verdict"] == "OK":
        out["verdict"] = "SINGLE_LANE"
        out["note"] = ("NO BACKUP. One account change and this is gone. "
                       "(Dad Energy lived only on Netlify for weeks — unaudited, unswept, "
                       "and shipping a broken offline floor nobody could see.)")
    return out


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

    if lmd5 == r["md5"]:
        print("   MATCH — you are holding canon. Proceed.")
        return 0

    delta = lb - r["bytes"]
    print()
    print("   *** HALT — YOU ARE NOT HOLDING CANON ***")
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
    # shelf file was reported as an orphan — 111 instead of 48. An audit that lies is the
    # exact disease this whole day was spent curing. GIT IS AUTHORITATIVE. Use it.
    repo_files = set()
    try:
        # BUG FOUND 2026-07-13: this ls-tree was NOT recursive (-r missing). It read only the
        # repo ROOT, so every file living in /studio, /archive, /writerly-moves, /rescued was
        # invisible — 267 real files seen as 85, and 47 files that ARE deployed were reported
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
        print("HALT — cannot read the repo file list (no git). An audit without canon is a")
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
            orphans.append(f"  {n:<44} {r['bytes']:>9,} B   SHELF-ONLY — no home in any lane")
        if r["verdict"] == "CHECK_CANON":
            stubs.append(f"  {n:<44} {r['fossils'][0]}")
        elif r["fossils"]:
            drift.append(f"  {n:<44} canon={r['canon_lane']}  {r['fossils'][0][:60]}")
        if r["verdict"] == "SINGLE_LANE" and r["canon_lane"] == "netlify":
            singles.append(f"  {n:<44} NETLIFY ONLY — no backup")

    print("=" * 74)
    print("RESOLVE_CANON — FULL AUDIT")
    print("=" * 74)
    for title, rows, why in (
        ("CANON MAY BE A STUB — DIFF THESE FIRST", stubs,
         "A non-canon lane holds a MUCH bigger file. Never default to the smaller one."),
        ("ORPHANS — shelf-only, no deploy lane", orphans,
         "The shelf is a cache. These have no home and no gate can see them."),
        ("SINGLE LANE — no backup", singles,
         "One account change and it is gone."),
        ("DRIFT — lanes disagree", drift,
         "The shelf lags. If shelf != repo, the shelf is wrong."),
    ):
        print(f"\n## {title}  [{len(rows)}]")
        print(f"   {why}")
        for row in rows[:25]:
            print(row)
        if not rows:
            print("   (clean)")
    print("\n" + "=" * 74)
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    if a[0] == "--audit":
        sys.exit(audit())
    if len(a) >= 3 and a[1] == "--check":
        sys.exit(check(a[0], a[2]))

    r = resolve(a[0])
    print(json.dumps(r, indent=2, default=str))
    sys.exit(0 if r["verdict"] in ("OK", "SINGLE_LANE") else 1)
