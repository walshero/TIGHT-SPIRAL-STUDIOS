#!/usr/bin/env bash
# STUDIO BELT — the timing belt, one runner for all five TSP repos.
# Lives in the hub (walshero/TIGHT-SPIRAL-STUDIOS). Spokes MOUNT it (checkout) and RUN it.
# ONE CANON WRITES, OTHERS READ: the ticks live here; every repo runs the same ones.
# Every tick BLOCKS (exit 1) — a tick with agency, not a wish.
#
# THE TICKS — each one is a founder ruling with teeth:
#   1  accessibility floor           comfort-gate.py         (flat)
#   2  student attribution standard  inline grep             (flat, decided 2026-08-03)
#   3  >50% image floor + render     preship-gate-v4.py      (ratchet, founder canon C7)
#   4  founder voice                 studio-voice-gate.py    (ratchet, ruling 2026-08-05)
#   5  entry paint / one invitation  one-thing-gate.py       (ratchet, locked 06-27 + 07-12)
#
# Ticks 3-5 added 2026-08-07. Until then the belt carried two ticks and none of the
# four things the founder had actually ruled on: the image floor, the voice, the entry
# grammar. Each had a working gate sitting in the hub that nothing ever called.
#
# WHY 3-5 RATCHET AND 1-2 DO NOT: measured before arming — voice HALTed 101 of 131
# surfaces, entry-paint 31 of 38 builds (Tableau Sweep #2, 2026-08-03). A tick that
# is red on every push is a tick everyone learns to scroll past; that is how floor.yml
# lost its teeth in July. So today's debt is CARRIED in a hub-owned baseline and only
# NEW debt blocks. Baselines may only SHRINK. Fix a file, it leaves forever.
#
# Usage: studio-belt.sh <target-repo-dir>   (defaults to .)
# Env:   STUDIO_CANON_SHA (optional) — hub commit the belt was mounted from, for provenance.
set -uo pipefail
BELT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"   # hub scripts live beside this file
TARGET="${1:-.}"; cd "$TARGET"
fail=0
echo "======================================================================"
echo "STUDIO BELT  ·  canon = hub@${STUDIO_CANON_SHA:-unknown}  ·  target = $(basename "$(pwd)")"
echo "======================================================================"

SURFACES=$(find . -name '*.html' -not -path './.git/*' -not -path './archive/*' \
  -not -path './rescued/*' -not -path '*/node_modules/*' -not -name 'confluence-TRUNK*.html' | sort)

# The repo name qualifies every baseline key. Three of the five repos ship an
# index.html; keyed by basename alone they collide into one entry and the last
# one written silently grants or denies the other two.
REPO="$(basename "$(pwd)")"

# TICK 1 — accessibility floor (comfort-gate: real-pixel contrast · dark · offline · no emoji)
echo; echo "-- tick 1: accessibility floor (comfort-gate) --"
if [ -n "$SURFACES" ] && [ -f "$BELT_DIR/comfort-gate.py" ]; then
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    if python3 "$BELT_DIR/comfort-gate.py" --ratchet --repo="$REPO" "$f" >/tmp/cg.out 2>&1; then
      grep -q '^DEBT' /tmp/cg.out && echo "  debt  $f" || echo "  pass  $f"
    else echo "  HALT  $f"; grep -iE 'HALT|emoji|contrast|light-on' /tmp/cg.out | sed 's/^/        /' | head -6; fail=1; fi
  done <<< "$SURFACES"
else echo "  (no HTML surfaces / gate not mounted — skipped)"; fi

# TICK 2 — student attribution standard (mechanical: a course code must not carry a year or section token)
echo; echo "-- tick 2: student attribution standard --"
HITS=$(grep -rInE 'EN[0-9]{3}' --include=*.html --include=*.md . 2>/dev/null | grep -vE '/(archive|rescued|node_modules)/' || true)
# a violation = a course code on a line that ALSO carries a SECTION token or a TERM-YEAR (e.g. "Summer 2026").
# generic course lines ("EN195 Creative Writing (summer 6-week online)") and changelog dates ("2026-07-11") do NOT match.
# only CREDIT lines count; drop source/provenance citations (a syllabus citation legitimately names a term)
CRED=$(printf '%s\n' "$HITS" | grep -viE 'syllabus|quoted|source|cite|policy|licen|per the|from the|\\bnote\\b' || true)
VIOL=$(printf '%s\n' "$CRED" | grep -Ei 'sec(tion)?[ .#_-]?[0-9]|(spring|summer|fall|winter|autumn)[a-z]* 20[0-9]{2}' || true)
if [ -n "${VIOL//[$'\n']/}" ]; then
  echo "  HALT — a course credit carries a year or section token (standard: generic course, no year/section):"
  printf '%s\n' "$VIOL" | sed 's/^/        /' | head -8; fail=1
else echo "  pass  no year/section token beside a course code"; fi

# TICKS 3-5 all RATCHET against a hub-owned baseline. Measured before arming:
# voice 101/131 surfaces, entry-paint 31/38 builds (Tableau Sweep #2, 2026-08-03).
# Armed flat they would paint every repo red on every push and be disarmed inside
# a week — that is precisely how floor.yml lost its teeth in July. So today's debt
# is CARRIED and only NEW debt blocks. The ratchet turns one way.

# TICK 3 — the >50% image floor + the rest of the render-proof ratchet (founder canon C7)
echo; echo "-- tick 3: image floor + render-proof ratchet (founder rule C7) --"
if [ -n "$SURFACES" ] && [ -f "$BELT_DIR/preship-gate-v4.py" ]; then
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    if python3 "$BELT_DIR/preship-gate-v4.py" --ratchet "$f" >/tmp/pg.out 2>&1; then echo "  pass  $f"
    else echo "  HALT  $f"; grep -E '^\s+H-|^\s+E1' /tmp/pg.out | sed 's/^/        /' | head -6; fail=1; fi
  done <<< "$SURFACES"
else echo "  (no HTML surfaces / gate not mounted — skipped)"; fi

# TICK 4 — founder voice (founder ruling 2026-08-05: "the general voice here is not mine")
echo; echo "-- tick 4: founder voice (unmarked em/en dashes) --"
if [ -n "$SURFACES" ] && [ -f "$BELT_DIR/studio-voice-gate.py" ]; then
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    if python3 "$BELT_DIR/studio-voice-gate.py" --ratchet --repo="$REPO" "$f" >/tmp/vg.out 2>&1; then echo "  pass  $f"
    else echo "  HALT  $f"; grep -E 'HALT|dash' /tmp/vg.out | sed 's/^/        /' | head -6; fail=1; fi
  done <<< "$SURFACES"
else echo "  (no HTML surfaces / gate not mounted — skipped)"; fi

# TICK 5 — the entry paint: scene-first, ONE invitation (locked 2026-06-27 / 2026-07-12)
# Needs a real browser. If playwright is absent the tick SKIPS LOUDLY — a gate that
# has gone blind must never read as a pass (the ratchet.py exit-2 lesson).
echo; echo "-- tick 5: entry paint — scene-first, one invitation --"
if [ -z "$SURFACES" ]; then echo "  (no HTML surfaces — skipped)"
elif [ ! -f "$BELT_DIR/one-thing-gate.py" ]; then echo "  (gate not mounted — skipped)"
elif ! python3 -c "import playwright" >/dev/null 2>&1; then
  echo "  SKIPPED LOUD — playwright absent, the entry gate is BLIND. Not a pass."
else
  if python3 "$BELT_DIR/one-thing-gate.py" --ratchet --repo="$REPO" $SURFACES >/tmp/ot.out 2>&1; then
    echo "  pass  every entry clears the ratchet"
  else
    echo "  HALT  an entry regressed:"; grep -E '^\s+\[X\]|SHIP-BLOCK' /tmp/ot.out | sed 's/^/        /' | head -10; fail=1
  fi
fi

echo; echo "----------------------------------------------------------------------"
if [ "$fail" -ne 0 ]; then echo "BELT: HALT — a tick refused. This build does not ship."; else echo "BELT: PASS — all ticks clear."; fi
exit $fail
