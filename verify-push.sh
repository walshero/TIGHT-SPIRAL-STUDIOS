#!/usr/bin/env bash
# VERIFY-PUSH - did the thing you checked become the thing that shipped?
#
# THE INCIDENT (2026-08-27). Funnybonies v9.1 was verified hard: belt clean on all
# eleven ticks, full flow driven in a headless browser, zero JS errors, screenshots
# read by eye. Then it was pushed to main through the GitHub connector with the
# literal string PLACEHOLDER as the file content. The write SUCCEEDED. The connector
# returned a commit sha and a green result. funnybonies/index.html on main became an
# 11-byte file and stayed destroyed until someone happened to look.
#
# WHY NOTHING CAUGHT IT. Every check in this repo grades a FILE IN A WORKING TREE.
# The belt reads the worktree. Studio Eyes renders the worktree. The gates all ask
# "is this file good." Not one of them can see the moment of TRANSMISSION, because
# the connector write is a separate hand-composed act: git push is blocked from the
# session sandbox, so bytes do not move mechanically, they are RETYPED into a tool
# call. Verification and transmission were decoupled, and the gap between them was
# unwatched.
#
# THE FAILURE CLASS, which this repo has now hit four times in four costumes:
#   * 2026-08-06 to 08-24  the belt passed locally while Pages served an 18 day old
#     site. Checked the commit result, not the live URL.
#   * 2026-08-23  site-watch.yml ran git with no checkout, so it tested liveness and
#     never freshness, and reported SUCCESS over a stale site.
#   * 2026-08-22  seven Funnybonies builds passed every tick while being the wrong
#     game for the wrong player. The gates graded the artifact, never the intent.
#   * 2026-08-27  PLACEHOLDER. The gates graded the local file, never the bytes sent.
# One sentence covers all four: THE THING THAT WAS CHECKED WAS NOT THE THING THAT
# SHIPPED. A green result is a claim about what a tool did, never proof of what
# arrived.
#
# WHAT THIS DOES. One mechanical comparison, no judgment: fetch the remote and diff
# the named paths against the verified local file. Byte-identical or it HALTS. This
# is the cheapest possible closing move and it would have caught PLACEHOLDER in the
# same second it happened.
#
# WHY IT IS NOT A BELT TICK. The belt reads files in a tree; it cannot see a tool
# call. Not every lesson becomes a tick. This one lives in the deploy lane, and it
# runs AFTER a write instead of before, which is the whole point.
#
# Usage (invoke with bash, never ./ - see the mode note below):
#   bash verify-push.sh funnybonies/index.html [more paths...]
#   bash verify-push.sh --self-test        prove it bites
#
# FILE MODE. Every script in this repo is committed 100644, because the connector is
# the only write lane out of the session sandbox and it cannot set an exec bit. So
# nothing here may DEPEND on being executable. Found 2026-08-27 by the stop hook:
# a local chmod +x showed as the only uncommitted change in the tree, and chasing it
# revealed that this file's own self-test invoked $SELF directly and would therefore
# have failed on any fresh clone. The gate's canary was broken for everyone but me.
#
# Exit: 0 remote matches local · 1 DRIFT · 2 usage or unreadable
set -uo pipefail

self_test(){
  # a gate with no canary is a gate nobody has tested.
  tmp="$(mktemp -d)"; ok=1
  (
    cd "$tmp" || exit 2
    git init -q .; git config user.email t@t; git config user.name t
    printf 'real content\n' > a.txt
    git add a.txt; git commit -qm one
    git branch -q -M main
    git init -q --bare ../origin.git 2>/dev/null || true
    git remote add origin ../origin.git 2>/dev/null
    git push -q origin main 2>/dev/null
  ) || { echo "  self-test could not build a fixture"; exit 2; }

  echo "-- canary 1: local matches remote --"
  if ( cd "$tmp" && bash "$SELF" a.txt >/dev/null 2>&1 ); then
    echo "   PASS  clean tree reads as verified"
  else echo "   FAIL  clean tree should pass"; ok=0; fi

  echo "-- canary 2: THE INCIDENT, remote holds a placeholder --"
  ( cd "$tmp" && printf 'PLACEHOLDER' > a.txt && git commit -qam wreck && git push -q origin main )
  ( cd "$tmp" && printf 'real content\n' > a.txt )   # local is the good copy
  if ( cd "$tmp" && bash "$SELF" a.txt >/dev/null 2>&1 ); then
    echo "   FAIL  a destroyed remote read as verified"; ok=0
  else echo "   PASS  drift HALTs"; fi

  rm -rf "$tmp" "${tmp%/*}/origin.git" 2>/dev/null
  echo; echo "SELF-TEST $( [ "$ok" = 1 ] && echo PASS || echo FAIL )"
  [ "$ok" = 1 ]
}

SELF="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/$(basename "${BASH_SOURCE[0]}")"
[ "${1:-}" = "--self-test" ] && { self_test; exit $?; }

[ $# -ge 1 ] || { echo "usage: verify-push.sh <path> [path...]" >&2; exit 2; }
git rev-parse --git-dir >/dev/null 2>&1 || {
  echo "verify-push: not a git checkout. REFUSING, loud." >&2; exit 2; }

REF="${VERIFY_PUSH_REF:-origin/main}"
git fetch -q "${REF%%/*}" "${REF#*/}" 2>/dev/null || {
  echo "verify-push: cannot reach ${REF}. BLIND, and blind is not clean." >&2; exit 2; }

fail=0
for p in "$@"; do
  [ -f "$p" ] || { echo "  HALT  $p is not a local file. Nothing to compare."; fail=1; continue; }
  lb=$(wc -c < "$p" | tr -d ' ')
  if ! git cat-file -e "$REF:$p" 2>/dev/null; then
    echo "  HALT  $p exists locally ($lb bytes) and NOT at $REF. The push did not land."
    fail=1; continue
  fi
  rb=$(git cat-file -s "$REF:$p")
  # CONTENT hash, not `git diff`. Corrected on this gate's own first live run,
  # 2026-08-27: `git diff` also reports index state and file mode, so it HALTed on
  # a file whose bytes were identical and whose only difference was a local chmod.
  # A gate that cries wolf is a gate somebody disarms inside a week. Compare what
  # the rule is actually about, which is content.
  lh=$(git hash-object "$p")
  rh=$(git rev-parse "$REF:$p" 2>/dev/null)
  if [ "$lh" = "$rh" ]; then
    echo "  ok    $p  $lb bytes, content-identical at $REF"
  else
    echo "  HALT  $p DRIFT. local $lb bytes, $REF $rb bytes."
    echo "        local  $lh"
    echo "        remote $rh"
    echo "        The bytes you verified are NOT the bytes that shipped."
    fail=1
  fi
done

echo
if [ "$fail" -ne 0 ]; then
  echo "VERIFY-PUSH: HALT. Do not report this as shipped."
  echo "  A connector returning a commit sha is a claim about what it did,"
  echo "  never proof of what arrived. Re-push from the verified local file."
else
  echo "VERIFY-PUSH: clean. What was checked is what shipped."
fi
exit $fail
