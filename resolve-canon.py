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
    GIT IS AUTHORITATIVE, AND IT IS RECURSIVE. Read the tree, once, and match