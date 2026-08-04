#!/usr/bin/env bash
# EGRESS PROBE — a "fool me once" check. Tight Spiral Productions.
# WHY: 2026-08-03 a session asserted "egress blocked" from a single denied host
# (nist.gov) and treated the whole lane as impossible. Egress is SELECTIVE, not
# binary: the studio face (raw.githubusercontent) is reachable; external image
# hosts are policy-denied. Rule: never claim "egress blocked" without this probe.
# Usage: ./egress-probe.sh [extra-url ...]
set -u
probe(){ local u="$1"; local code
  code=$(curl -sS -o /dev/null -w "%{http_code}" --max-time 20 "$u" 2>/dev/null)
  local host; host=$(printf '%s' "$u" | sed -E 's#https?://([^/]+).*#\1#')
  if [ "$code" = "000" ]; then printf "  DENIED   %-34s (no connection)\n" "$host"
  else printf "  REACH %s  %s\n" "$code" "$host"; fi
}
echo "EGRESS PROBE — reachable vs policy-denied:"
probe "https://raw.githubusercontent.com/walshero/TIGHT-SPIRAL-STUDIOS/main/index.html"   # studio face
probe "https://upload.wikimedia.org/wikipedia/commons/9/99/Question_book-new.svg"          # external image host
probe "https://www.nist.gov/robots.txt"                                                     # federal (expected denied)
for u in "$@"; do probe "$u"; done
echo "Rule: cite this probe before any 'egress blocked' claim. Reachable != all hosts."
