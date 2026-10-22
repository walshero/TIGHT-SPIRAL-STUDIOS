#!/usr/bin/env bash
# TSP-GAME-BUILD PRESHIP — one command, every gate, in order.
# Owns no gates. Calls the hub's own scripts so there is one canon for each check.
#   1. studio-belt.sh <file>         ticks 1-14, one-file preflight mode
#   2. preship-contrast-gate.py      text-token contrast arithmetic (not in the belt)
# Exit 0 = SHIP. Exit 1 = HALT, does not ship. Exit 2 = refused (bad input / gate missing).
# A gate that is missing is a HALT, never a skip: a blind gate must not read as clean.
set -uo pipefail

HUB="$(git -C "$(dirname "${BASH_SOURCE[0]}")" rev-parse --show-toplevel 2>/dev/null)"
if [ -z "${HUB}" ] || [ ! -f "${HUB}/studio-belt.sh" ]; then
  echo "PRESHIP: cannot find the hub (studio-belt.sh). REFUSING. Exit 2."; exit 2
fi
if [ $# -lt 1 ]; then
  echo "usage: preship.sh <file.html> [more.html ...]"; exit 2
fi

cd "${HUB}"
verdict=0
for f in "$@"; do
  if [ ! -f "$f" ]; then
    echo "PRESHIP: $f does not exist. REFUSING. Exit 2."; exit 2
  fi
  md5=$(md5sum "$f" | cut -c1-8); bytes=$(wc -c < "$f" | tr -d ' ')
  echo "======================================================================"
  echo "PRESHIP  $f   md5 ${md5}   ${bytes} B"
  echo "======================================================================"

  echo "-- 1/2 belt, one-file mode --"
  bash studio-belt.sh "$f" > /tmp/preship-belt.$$ 2>&1; belt=$?
  # One line per tick: HALT or pass. Tick 12 STALE-HALT is "reported, not armed" per the
  # belt's own arming rule, so it is shown as REPORT, not counted as a refusal.
  awk '
    function emit() { if (t!="") print (h ? "  HALT    " : (r ? "  REPORT  " : "  pass    ")) t }
    /^-- tick/   { emit(); t=$0; sub(/^-- /,"",t); sub(/ --$/,"",t); h=0; r=0; next }
    /^BELT:/     { emit(); t=""; print "  " $0; next }
    /STALE-HALT/ { r=1; next }
    /HALT/       { h=1 }
  ' /tmp/preship-belt.$$
  echo "  (full belt detail: bash studio-belt.sh $f)"
  rm -f /tmp/preship-belt.$$

  echo "-- 2/2 preship-contrast-gate --"
  python3 preship-contrast-gate.py "$f" 2>&1 | tail -4; contrast=${PIPESTATUS[0]}

  if [ $belt -ne 0 ] || [ $contrast -ne 0 ]; then
    echo "VERDICT  HALT  $f  (belt=$belt contrast=$contrast). Does not ship."
    verdict=1
  else
    echo "VERDICT  SHIP  $f  md5 ${md5}"
  fi
done
exit $verdict
