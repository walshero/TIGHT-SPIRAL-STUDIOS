#!/bin/bash
# FOUNDER GATE CANARY — every case is a real event from 2026-07-13.
cd /home/claude/tsp
pass=0; fail=0
t() { # t <expect 0|1> <label> <args...>
  want=$1; label=$2; shift 2
  python3 founder-gate.py "$@" >/dev/null 2>&1; got=$?
  [ "$got" = "$want" ] && { echo "  ok   $label"; pass=$((pass+1)); } \
                       || { echo "  FAIL $label (want $want got $got)"; fail=$((fail+1)); }
}
echo "  FOUNDER GATE · CANARY"
echo "  ----------------------------------------------"
# MUST HALT — the real failures
t 1 "THE failure: 'Lumiere names ok' -> rm 3 files" rm claude-project-instructions.md chatgpt-pro-instructions.md massbay-fact-book-word.docx --authorized-by "Lumiere names are ok. What you got?"
t 1 "bare assent 'Go'"                              rm arcade.html --authorized-by "Go"
t 1 "bare assent 'Make it so'"                      rm arcade.html --authorized-by "Make it so"
t 2 "no authorization at all"                       rm arcade.html
t 1 "category, not a path"                          rm chatgpt-pro-instructions.md --authorized-by "delete the IP files"
t 1 "smuggled 2nd path"                             rm massbay-fact-book-word.docx chatgpt-pro-instructions.md --authorized-by "delete the massbay fact book"
t 1 "ambiguous single word"                         rm chatgpt-pro-instructions.md --authorized-by "delete the instructions"
# MUST PASS — genuine authorization. friction here = founder kills the gate
t 0 "founder names the fact book"                   rm massbay-fact-book-word.docx --authorized-by "delete the massbay fact book"
t 0 "founder names the zip"                         rm GitHubDesktop-arm64.zip --authorized-by "remove GitHubDesktop-arm64.zip"
t 0 "founder names a game"                          rm the-viscosity.html --authorized-by "kill the-viscosity, it never shipped"
t 0 "full filename"                                 rm chatgpt-pro-instructions.md --authorized-by "delete chatgpt-pro-instructions.md"
# institutional strings
t 1 "kmcgath / massby stale strings"                claim "kmcgath@massbay.edu jdonato@massby.edu"
t 0 "correct strings pass"                          claim "kmcgrath@massbay.edu jdonato@massbay.edu"
echo "  ----------------------------------------------"
if [ $fail -eq 0 ]; then echo "  CANARY PASSED — $pass/$((pass+fail))"; exit 0
else echo "  CANARY FAILED — $fail of $((pass+fail))"; exit 1; fi
