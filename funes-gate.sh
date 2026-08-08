#!/usr/bin/env bash
# funes-gate.sh - run any gate and route its verdict to the Funes ledger.
# Wire every gate through this (or add the CI step) so no verdict is silent.
#
#   ./funes-gate.sh comfort-gate.py index.html
#   ./funes-gate.sh preship-gate-v5.py index.html
#
# Exit code is the gate's own exit code. The ledger line is written either way.
set -u
GATE="$1"; TARGET="$2"
OUT="$(python3 "$GATE" "$TARGET" 2>&1)"; CODE=$?
SHA="$(git rev-parse --short HEAD 2>/dev/null || echo '')"
MD5="$(md5sum "$TARGET" 2>/dev/null | cut -d' ' -f1)"
VERDICT="SHIP"; [ "$CODE" -ne 0 ] && VERDICT="HALT"
# one-line summary: last non-empty line of the gate output
SUMMARY="$(printf '%s' "$OUT" | grep -v '^[[:space:]]*$' | tail -1 | cut -c1-180)"
python3 "$(dirname "$0")/funes-ledger.py" --file "$TARGET" --gate "$(basename "$GATE" .py)" \
  --verdict "$VERDICT" --detail "$SUMMARY" --commit "$SHA" --md5 "$MD5" >/dev/null
printf '%s\n' "$OUT"
exit "$CODE"
