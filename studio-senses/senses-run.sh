#!/usr/bin/env bash
# STUDIO SENSES · ONE COMMAND                             Tight Spiral Productions
# Added 2026-10-13 after the Flok SWOT (claude/STUDIO-SENSES-SWOT-2026-10-13.md).
# A session shipped Flok v27 on a HAND-PICKED list of three gates and called it
# "all gates green"; Studio Eyes, not on that list, HALTed the same file. The cure is
# not a rule saying "run all the gates". It is one command that IS all the senses.
#
#   crawl (v2: stays in the build, plays every screen, census of coverage)
#   -> ears.py          Layer 1 sound floors          (SILENT is printed, never PASS)
#   -> fingers-play.py  every tap as a thumb made it  (verb in view, path in view, coverage)
#   -> feedback-floor.py the subject in its window, the result still on screen (builds with #receipt)
#   -> studio-eyes.py   real-pixel contrast + clip     (first paint, every light mode)
#   -> personas.py      sighted.md / ear.md / fingers-states.json for the seats
#
# Usage: studio-senses/senses-run.sh <build.html> [--secondary sc-about,sc-credits]
# Exit 1 if any sense HALTs. The bundle lands in reports/senses/<build-stem>/.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"; ROOT="$(cd "$HERE/.." && pwd)"
B="$1"; shift || true
SEC=""; [ "${1:-}" = "--secondary" ] && SEC="--secondary $2"
STEM="$(basename "${B%.html}")"; OUT="$ROOT/reports/senses/$STEM"
# Clear only what the crawl regenerates. predictions.json, pred-*.json and SEAT-FINDINGS.md
# are the seats' work and survive a re-run (a v1 of this script wiped them, 2026-10-13).
mkdir -p "$OUT"; rm -rf "$OUT/states" "$OUT/manifest.json" "$OUT/sighted.md" "$OUT/ear.md" "$OUT/fingers-states.json" "$OUT/ears.json"; fail=0
echo "== STUDIO SENSES  $B"
python3 "$HERE/senses-crawl.py" "$B" --out "$OUT" --clicks "${SENSES_CLICKS:-200}" | sed 's/^/  /' || fail=1
grep -q '"screens_total": \[\]' "$OUT/manifest.json" 2>/dev/null && echo "  (no .screen census: single-scene build, coverage not judged)"
echo "-- ears";          python3 "$HERE/ears.py" "$OUT" | sed 's/^/  /';            [ "${PIPESTATUS[0]}" -ne 0 ] && fail=1
echo "-- fingers play";  python3 "$HERE/fingers-play.py" "$OUT" $SEC | sed 's/^/  /'; [ "${PIPESTATUS[0]}" -ne 0 ] && fail=1
# feedback floor (2026-10-13, Flok v32): builds with a result receipt are played tap by tap
if grep -q 'id="receipt"' "$B"; then
echo "-- feedback floor"; python3 "$HERE/feedback-floor.py" "$B" | sed 's/^/  /'; [ "${PIPESTATUS[0]}" -ne 0 ] && fail=1
fi
echo "-- top floor";     python3 "$HERE/top-floor.py" "$B" | sed 's/^/  /'; [ "${PIPESTATUS[0]}" -ne 0 ] && fail=1
echo "-- eyes";          python3 "$ROOT/studio-eyes/studio-eyes.py" "$B" 2>/dev/null | grep -E 'HALT|CONTRAST|CLIP|of [0-9]+ at HALT' | grep -v 'SELF-TEST' | sed 's/^/  /'
                         python3 "$ROOT/studio-eyes/studio-eyes.py" "$B" >/dev/null 2>&1 || fail=1
echo "-- personas";      python3 "$HERE/personas.py" "$OUT" | sed 's/^/  /'
echo "== SENSES: $([ $fail -eq 0 ] && echo PASS || echo HALT)  (seats read $OUT; they predict, the founder's play grades)"
exit $fail
