#!/usr/bin/env bash
# Everything CI does, in one script.
#
# It lives here and not in the workflow file on purpose. The Zapier GitHub lane
# cannot write .github/workflows/ - that path needs the 'workflow' OAuth scope,
# which the Zapier grant does not carry (probed 2026-07-28: identical PUT, 404
# under .github/workflows/, 201 at the repo root). So the workflow file has to be
# created by hand, once, in the browser. Keeping it to a stub that calls this
# script means the hand-typed part stays small and everything real stays here,
# where it can be pushed normally and reviewed in a diff.
#
# Reporting, not blocking. Zapier commits straight to main, so failing hard here
# would only break the deploy lane. A red X on the commit is the signal.

set -uo pipefail

SURFACES=$(find . -name '*.html' \
  -not -path './.git/*' \
  -not -path './archive/*' \
  -not -path './rescued/*' \
  -not -name 'confluence-TRUNK.html' | sort)

fail=0

echo "=== gate: every surface against the ratchet ==="
for f in $SURFACES; do
  if python3 preship-gate-v4.py --ratchet "$f" > /tmp/gate.out 2>&1; then
    echo "SHIP  $f"
  else
    echo "HALT  $f"
    grep -E '^\s+[EH][A-Z0-9-]*' /tmp/gate.out | sed 's/^/        /' | head -20
    fail=1
  fi
done

echo
echo "=== every surface's JavaScript parses ==="
cat > /tmp/parsecheck.py <<'PY'
import re, sys, subprocess, tempfile, os
bad = 0
for path in sys.argv[1:]:
    s = open(path, encoding='utf-8', errors='ignore').read()
    js = '\n'.join(re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', s, re.S))
    if not js.strip():
        continue
    fd, p = tempfile.mkstemp(suffix='.js')
    os.write(fd, js.encode()); os.close(fd)
    r = subprocess.run(['node', '--check', p], capture_output=True, text=True)
    if r.returncode:
        print('PARSE FAIL', path)
        print(r.stderr)
        bad = 1
    else:
        print('parses', path)
sys.exit(bad)
PY
if [ -n "$SURFACES" ]; then
  python3 /tmp/parsecheck.py $SURFACES || fail=1
fi

echo
echo "=== no credential reaches the repo ==="
if grep -rIn --exclude-dir=.git -E 'sk-ant-[A-Za-z0-9]' . ; then
  echo "A credential is in the tree. Rotate it now."
  exit 1
fi
echo clean

echo
echo "=== recompute STUDIO-STATE.md from the tree ==="
python3 emit-state.py

if [ -n "${GITHUB_ACTIONS:-}" ]; then
  git config user.name  "studio gate"
  git config user.email "gate@tightspiral.local"
  git add STUDIO-STATE.md
  if git diff --staged --quiet; then
    echo "state unchanged"
  else
    git commit -m "state: recomputed from tree [skip ci]"
    git push
    echo "state committed"
  fi
fi

echo
if [ "$fail" -ne 0 ]; then
  echo "RESULT: one or more surfaces HALT against the ratchet. See STUDIO-STATE.md."
  exit 1
fi
echo "RESULT: every surface clean."
