#!/bin/bash
# SAFE-PUSH — the gate that would have stopped the v43 clobber.
#
# On 2026-07-11 a session pushed a v34-based file over v43 canon. Nine versions of work.
# It was caught ONLY because someone happened to run a byte-check AFTER the push. Luck.
#
# THIS MAKES IT ARITHMETIC, BEFORE THE PUSH:
#   fetch the remote copy -> if it exists and differs from what we last read -> HALT.
#   You are about to overwrite something you never read.
#
# Usage:  ./safe-push.sh <file> "<commit message>"

set -e
F="$1"; MSG="$2"
[ -z "$F" ] && { echo "usage: safe-push.sh <file> \"<msg>\""; exit 2; }
RAW="https://raw.githubusercontent.com/walshero/TIGHT-SPIRAL-STUDIOS/main/$F"

echo "== SAFE-PUSH: $F =="

# 1. PRE-TICK — does canon already exist, and have we read it?
if curl -sfL "$RAW" -o /tmp/_canon 2>/dev/null && [ -s /tmp/_canon ]; then
  RMD5=$(md5sum /tmp/_canon | cut -d' ' -f1)
  LMD5=$(md5sum "$F" | cut -d' ' -f1)
  RB=$(wc -c < /tmp/_canon); LB=$(wc -c < "$F")
  echo "  remote: $RB B  $RMD5"
  echo "  local : $LB B  $LMD5"
  if [ "$RMD5" = "$LMD5" ]; then echo "  IDENTICAL — nothing to push."; exit 0; fi

  # THE REFUSAL: local is SMALLER than remote. Never auto-default to the smaller file.
  # (The repo held a 2,277 B stub of warriors-fantasy-arcade while the shelf held the
  #  real 19,577 B game. The reverse mistake overwrote Confluence v43 with v34.)
  if [ "$LB" -lt "$RB" ]; then
    echo ""
    echo "  *** HALT — LOCAL IS SMALLER THAN CANON ***"
    echo "  You are about to shrink $F by $((RB-LB)) bytes."
    echo "  This is EXACTLY the shape of the v34-over-v43 clobber. DIFF FIRST."
    echo "  Override only with: SAFE_PUSH_FORCE=1 $0 $F \"$MSG\""
    [ "$SAFE_PUSH_FORCE" != "1" ] && exit 1
    echo "  (forced)"
  fi
else
  echo "  remote: (new file)"
fi

# 2. GATE — Studio Eyes must pass
if [ "${F##*.}" = "html" ]; then
  mkdir -p /tmp/_sweep && cp "$F" /tmp/_sweep/
  if python3 /tmp/studio-eyes-sweep.py /tmp/_sweep 2>/dev/null | grep -q "^HALT"; then
    echo "  *** HALT — Studio Eyes ***"
    python3 /tmp/studio-eyes-sweep.py /tmp/_sweep 2>/dev/null | head -6 | sed 's/^/     /'
    rm -rf /tmp/_sweep
    [ "$SAFE_PUSH_FORCE" != "1" ] && exit 1
  fi
  rm -rf /tmp/_sweep
  echo "  studio eyes: 0-HALT"
fi

# 3. PUSH
git add "$F"
git -c user.email="walshero@gmail.com" -c user.name="Tight Spiral Studios" commit -q -m "$MSG"
git push -q origin main

# 4. POST-TICK — byte-verify. "success:true" is never proof.
#
# BUG FOUND 2026-07-11: raw.githubusercontent.com caches for ~5 min. A fresh push reads back
# as the OLD file and this gate cried "MISMATCH" on a push that had landed perfectly.
# An auditor that cries wolf is worse than none — that is the whole lesson of today.
# So: verify against GIT (authoritative, uncached) first; the CDN is advisory only.
if [ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ]; then
  echo "  VERIFIED  git: HEAD == origin/main  ($(wc -c < "$F") B pushed)"
  curl -sL "$RAW" -o /tmp/_verify 2>/dev/null
  a=$(md5sum "$F" | cut -d' ' -f1); b=$(md5sum /tmp/_verify 2>/dev/null | cut -d' ' -f1)
  [ "$a" != "$b" ] && echo "  (raw CDN still serving cached copy — normal, clears in ~5 min)"
else
  echo "  *** PUSH DID NOT LAND — HEAD != origin/main ***"; exit 1
fi
