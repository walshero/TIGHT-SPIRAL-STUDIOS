#!/usr/bin/env python3
# LANE FIDELITY - does the file that LANDED match the file I MEANT to push?
# =============================================================================
# The problem this exists for (2026-07-21): the Zapier GitHub write path is
# FUNCTIONAL-EXACT, NOT BYTE-EXACT. It strips CSS/HTML comment lines and blank
# lines in transit. For working code that's harmless; for canon (specs,
# annotated OS blocks, a Python gate whose comments ARE the rationale) it is
# silent data loss. Worse: the raw CDN caches ~5min and will hand back a STALE
# copy that looks like a failed push, and the authenticated read can markdown-
# mangle the body into one line. Three different readbacks, three different lies.
#
# THE ONE CHECK THAT CANNOT LIE: the git blob sha.
# git stores every file as  sha1(b"blob <len>\0" + raw_bytes).
# It is deterministic. Compute it locally on the exact bytes you are about to
# push; after the push, ask git for the blob sha of what it stored. If they
# match, the file is byte-identical - proven, not hoped. No CDN, no cache, no
# renderer in the loop. If they differ, the lane altered it in transit: HALT
# and decide (re-push, or accept the functional-exact strip on purpose).
#
# "If a rule can't be a check, it's a wish." The rule "verify every push landed"
# was a wish - done by hand, differently each time, sometimes skipped. This is
# the check.
# =============================================================================
import hashlib, sys, os

def blob_sha(data: bytes) -> str:
    """The exact sha1 git assigns to a blob. Deterministic."""
    header = b"blob " + str(len(data)).encode() + b"\x00"
    return hashlib.sha1(header + data).hexdigest()

def blob_sha_of_file(path: str) -> str:
    with open(path, "rb") as f:
        return blob_sha(f.read())

def classify(local_path: str) -> str:
    """Which lane law applies, so the caller pushes the right way."""
    size = os.path.getsize(local_path)
    comments = 0
    try:
        txt = open(local_path, encoding="utf-8", errors="replace").read()
        for line in txt.splitlines():
            s = line.strip()
            if s.startswith(("#", "//", "/*", "*", "<!--")):
                comments += 1
    except Exception:
        pass
    over = size > 15000
    canon_comments = comments >= 5
    return (
        "  size: " + str(size) + " B  (" + ("OVER" if over else "under")
        + " the ~15KB inline ceiling)\n"
        "  comment lines: " + str(comments)
        + ("  <- COMMENTS ARE AT RISK: Zapier strips them. If they're canon,\n"
           "     the blob sha WILL differ after a Zapier push. Use a PAT git-push\n"
           "     when the comments must be byte-exact, or accept the strip on\n"
           "     purpose and record it." if canon_comments else "")
    )

USAGE = """LANE FIDELITY - verify a push landed byte-identical, deterministically.

  # BEFORE pushing: get the blob sha of the exact bytes you intend to send.
  lane-fidelity.py plan <local_file>
      -> prints the blob sha git WILL assign if the bytes arrive intact,
         plus which lane law applies (size, comment-risk).

  # AFTER pushing: the Zapier create_file / get_file_contents call RETURNS a
  # blob sha in its result. Compare it to the planned one - no readback needed.
  lane-fidelity.py check <local_file> <sha-git-returned>
      -> MATCH  = byte-identical, the push is honest. Ship.
         DIFFER = the lane rewrote it in transit. HALT: decide re-push (PAT for
                  byte-exact) or accept the functional-exact strip deliberately.

  # Compare any two local files (e.g. what I built vs. what I read back).
  lane-fidelity.py diff <file_a> <file_b>

The blob sha is git's own content address. Matching it is proof of byte-identity
that no CDN cache, no markdown renderer, and no "success: true" can fake.
"""

def main(argv):
    if len(argv) < 2:
        print(USAGE); return 2
    cmd = argv[1]
    if cmd == "plan" and len(argv) == 3:
        p = argv[2]
        print("  planned blob sha: " + blob_sha_of_file(p))
        print(classify(p))
        print("  After the push, run:  lane-fidelity.py check " + os.path.basename(p) + " <sha-git-returned>")
        return 0
    if cmd == "check" and len(argv) == 4:
        p, returned = argv[2], argv[3].strip().lower()
        mine = blob_sha_of_file(p)
        print("  intended blob sha: " + mine)
        print("  git returned sha : " + returned)
        if mine == returned:
            print("  MATCH - byte-identical. The push is honest. Ship.")
            return 0
        print("  DIFFER - the lane rewrote the file in transit.")
        print("  HALT. Either the Zapier strip ate canon (re-push via PAT for")
        print("  byte-exact), or the strip was harmless (accept it on purpose,")
        print("  and re-verify the LOGIC by running the artifact's own gate on")
        print("  the repo copy).")
        return 1
    if cmd == "diff" and len(argv) == 4:
        a, b = blob_sha_of_file(argv[2]), blob_sha_of_file(argv[3])
        print("  " + argv[2] + ": " + a)
        print("  " + argv[3] + ": " + b)
        print("  " + ("IDENTICAL" if a == b else "DIFFER"))
        return 0 if a == b else 1
    print(USAGE); return 2

if __name__ == "__main__":
    sys.exit(main(sys.argv))
