#!/usr/bin/env bash
# STUDIO BELT — the timing belt, one runner for all five TSP repos.
# Lives in the hub (walshero/TIGHT-SPIRAL-STUDIOS). Spokes MOUNT it (checkout) and RUN it.
# ONE CANON WRITES, OTHERS READ: the ticks live here; every repo runs the same ones.
# Every tick BLOCKS (exit 1) — a tick with agency, not a wish.
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

# TICK 1 — accessibility floor (comfort-gate: real-pixel contrast · dark · offline · no emoji)
echo; echo "-- tick 1: accessibility floor (comfort-gate) --"
if [ -n "$SURFACES" ] && [ -f "$BELT_DIR/comfort-gate.py" ]; then
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    if python3 "$BELT_DIR/comfort-gate.py" "$f" >/tmp/cg.out 2>&1; then echo "  pass  $f"
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

echo; echo "----------------------------------------------------------------------"
if [ "$fail" -ne 0 ]; then echo "BELT: HALT — a tick refused. This build does not ship."; else echo "BELT: PASS — all ticks clear."; fi
exit $fail
