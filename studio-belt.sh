#!/usr/bin/env bash
# STUDIO BELT — the timing belt, one runner for all five TSP repos.
# Lives in the hub (walshero/TIGHT-SPIRAL-STUDIOS). Spokes MOUNT it (checkout) and RUN it.
# ONE CANON WRITES, OTHERS READ: the ticks live here; every repo runs the same ones.
# Every tick BLOCKS (exit 1) — a tick with agency, not a wish.
#
# THE TICKS — each one is a founder ruling with teeth:
#   1  accessibility floor           comfort-gate.py         (flat)
#   2  student attribution standard  inline grep             (ratchet, decided 2026-08-03,
#                                                              ratcheted 2026-08-08 — see below)
#   3  >50% image floor + render     preship-gate-v4.py      (ratchet, founder canon C7)
#   4  founder voice                 studio-voice-gate.py    (ratchet, ruling 2026-08-05)
#   5  entry paint / one invitation  one-thing-gate.py       (ratchet, locked 06-27 + 07-12)
#   6  retired lines (founder bans)  retired-lines-gate.py   (flat, zero tolerance, 2026-08-08)
#   7  touch floor / thumb reach     studio-fingers.py       (ratchet, 48px house floor, 2026-08-08)
#      REPOINTED same day -> studio-eyes/studio-fingers.py   (ratchet, RENDERS, 44px founder floor)
#   8  scope / what a doc reaches for scope-gate.py           (A flat + B ratchet, 2026-08-09)
#   9  number sense / layout         number-sense-gate.py    (flat, zero tolerance, 2026-08-11)
#
# Ticks 3-5 added 2026-08-07. Until then the belt carried two ticks and none of the
# four things the founder had actually ruled on: the image floor, the voice, the entry
# grammar. Each had a working gate sitting in the hub that nothing ever called.
#
# Tick 6 added 2026-08-08 for the same reason ticks 3-5 were: a founder ruling (CYL's
# spine line, objected 2026-07-18) sat in TSP_Ledger.md with no gate checking for it,
# and the line it killed kept shipping live for three weeks because nothing looked.
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
# ---------------------------------------------------------------------------
# TWO MODES. Added 2026-08-08 after the belt failed to prevent the exact thing
# it exists for.
#
# WHAT WENT WRONG. comfort-v3.html was landed after running SIX of the seven
# ticks by hand, one command each. The seventh, tick 5, exited 1. Deploy had
# re-coupled that same day, so one unshipped file stopped the entire site
# publishing, and nobody knew until a seven-lens review went looking hours
# later. The gate that would have caught it in one line already existed.
#
# WHY IT WAS SKIPPED, and this is the whole point: the belt only accepted a
# DIRECTORY and always walked all 133 surfaces. A full run is minutes. So the
# complete check was too slow to use as a preflight, and every author fell back
# to running gates one at a time from memory. A checklist you run from memory is
# not a checklist. The completeness was real and it was never applied to the one
# moment that needed it, which is the moment before a push.
#
# So: the belt now takes FILES. Same ticks, same baselines, same teeth, scoped
# to what actually changed. Seconds instead of minutes. There is no longer a
# reason to run a tick by hand, and no excuse for running six of seven.
#
#   studio-belt.sh                     the whole repo. CI does this.
#   studio-belt.sh <dir>               another repo. Spokes do this.
#   studio-belt.sh a.html b.html       PREFLIGHT. Do this before every push.
#
# Deliberately NOT a separate preflight script. Two runners of one belt is how
# this repo got two studio-fingers gates in one day, and one of them shipped a
# 48px floor that contradicted a founder ruling and manufactured 121 phantom
# halts. One canon, extended.
# ---------------------------------------------------------------------------
MODE=dir
if [ -f "${1:-}" ]; then
  MODE=file
  _abs=""
  for _a in "$@"; do
    [ -f "$_a" ] || { echo "studio-belt: no such file: $_a" >&2; exit 2; }
    _abs="$_abs $(cd "$(dirname "$_a")" && pwd)/$(basename "$_a")"
  done
  cd "$(git rev-parse --show-toplevel 2>/dev/null || echo .)"
  SURFACES=$(for _f in $_abs; do
    case "$_f" in *.html) printf './%s\n' "${_f#$PWD/}";; esac
  done | sort)
  CHANGED=$(for _f in $_abs; do printf './%s\n' "${_f#$PWD/}"; done | sort)
else
  TARGET="${1:-.}"
  # A BELT THAT CANNOT FIND ITS TARGET MUST NOT READ AS A PASS.
  # Found by this file's own self-test, 2026-08-08: `studio-belt.sh nope.html`
  # failed the -f test, fell through to directory mode, ran `cd nope.html`, got a
  # shell error nobody reads, then belted the CURRENT directory and exited 0. A
  # typo'd filename returned a green belt for a file that does not exist. This
  # predates file mode; the original `cd "$TARGET"` was unguarded too.
  if [ ! -d "$TARGET" ]; then
    echo "studio-belt: '$TARGET' is neither an existing file nor a directory. REFUSING." >&2
    echo "             Exit 2, loud. A gate that has gone blind must never read as clean." >&2
    exit 2
  fi
  cd "$TARGET" || exit 2
  # studio-eyes/canary/ holds DELIBERATELY BROKEN gate fixtures (t01-t11, p01-p07)
  # — each exists to make a gate's own self-test bite. They are exercised by
  # --selftest, not by the corpus sweep. Sweeping them as corpus is how CI went
  # red for four straight runs on 2026-08-09: tick 7's baseline was frozen
  # against the 113 real surfaces, the find handed it 131 including 18 fixtures
  # with baseline 0, and every fixture read as NEW debt. A fixture that STOPS
  # failing is caught where it belongs: the owning gate's self-test.
  SURFACES=$(find . -name '*.html' -not -path './.git/*' -not -path './archive/*' \
    -not -path './rescued/*' -not -path '*/node_modules/*' -not -path './studio-eyes/canary/*' \
    -not -name 'confluence-TRUNK*.html' | sort)
  CHANGED=""
fi

fail=0
echo "======================================================================"
if [ "$MODE" = file ]; then
  echo "STUDIO BELT  ·  PREFLIGHT  ·  $(printf '%s' "$CHANGED" | grep -c . ) file(s)  ·  all 8 ticks"
else
  echo "STUDIO BELT  ·  canon = hub@${STUDIO_CANON_SHA:-unknown}  ·  target = $(basename "$(pwd)")"
fi
echo "======================================================================"

# The repo name qualifies every baseline key. Three of the five repos ship an
# index.html; keyed by basename alone they collide into one entry and the last
# one written silently grants or denies the other two.
REPO="$(basename "$(pwd)")"
# ...but the CHECKOUT DIRECTORY is not the repo. Every ratchet baseline in this
# hub is keyed `TIGHT-SPIRAL-STUDIOS/<path>`, written from a checkout that
# happened to be named that. Clone the same repo into `tsp-repo` and every
# lookup misses, every surface reads baseline 0, and ticks 3/4/5 go red on files
# nobody touched. Measured 2026-08-09: index.html and arcade.html HALTed all
# three ticks under REPO=tsp-repo and passed all three under
# REPO=TIGHT-SPIRAL-STUDIOS, same bytes, same gates, same run. The inverse is
# worse than noise - two repos cloned into same-named directories would grant
# each other's debt. So the key comes from the REMOTE, which is the repo's
# actual name, and falls back to the directory only when there is no remote.
_remote="$(git remote get-url origin 2>/dev/null || true)"
if [ -n "$_remote" ]; then
  REPO="$(basename "${_remote%.git}")"
fi

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
# RATCHETED 2026-08-08 (was flat). Founder's call, re-coupling deploy to the belt: "real
# teeth, not passive lip service." A flat tick would have frozen deploy on day one over 23
# pre-existing lines nobody was checking, because the deploy this tick has always fired
# under was decoupled until today - the same discovery that made ticks 1/3/4/5 ratchet
# in the first place. Baseline: attribution-baseline.json, hub-owned, same shape as the
# other four. Carried, not resolved.
echo; echo "-- tick 2: student attribution standard --"
if [ "$MODE" = file ]; then
  HITS=$(printf '%s\n' $CHANGED | xargs -r grep -InE 'EN[0-9]{3}' 2>/dev/null || true)
else
  HITS=$(grep -rInE 'EN[0-9]{3}' --include=*.html --include=*.md . 2>/dev/null | grep -vE '/(archive|rescued|node_modules)/' || true)
fi
# a violation = a course code on a line that ALSO carries a SECTION token or a TERM-YEAR (e.g. "Summer 2026").
# generic course lines ("EN195 Creative Writing (summer 6-week online)") and changelog dates ("2026-07-11") do NOT match.
# only CREDIT lines count; drop source/provenance citations (a syllabus citation legitimately names a term)
CRED=$(printf '%s\n' "$HITS" | grep -viE 'syllabus|quoted|source|cite|policy|licen|per the|from the|\\bnote\\b' || true)
VIOL=$(printf '%s\n' "$CRED" | grep -Ei 'sec(tion)?[ .#_-]?[0-9]|(spring|summer|fall|winter|autumn)[a-z]* 20[0-9]{2}' || true)
if [ -n "${VIOL//[$'\n']/}" ]; then
  NEW=""; DEBT_N=0
  while IFS= read -r line; do
    [ -z "$line" ] && continue
    key="$(printf '%s\n' "$line" | cut -d: -f1,2 | sed 's#^\./##')"
    if [ -f "$BELT_DIR/attribution-baseline.json" ] && \
       python3 -c "import json,sys; d=json.load(open('$BELT_DIR/attribution-baseline.json')); sys.exit(0 if sys.argv[1] in d['debt'] else 1)" "$key" 2>/dev/null; then
      DEBT_N=$((DEBT_N+1))
    else
      NEW="$NEW$line"$'\n'
    fi
  done <<< "$VIOL"
  if [ -n "${NEW//[$'\n']/}" ]; then
    echo "  HALT — a NEW course credit carries a year or section token (not in attribution-baseline.json):"
    printf '%s' "$NEW" | sed 's/^/        /' | head -8; fail=1
  else
    echo "  pass (debt carried)  $DEBT_N pre-existing line(s), 0 new — see attribution-baseline.json"
  fi
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
    if python3 "$BELT_DIR/preship-gate-v4.py" --ratchet --repo="$REPO" "$f" >/tmp/pg.out 2>&1; then echo "  pass  $f"
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

# TICK 6 — retired lines (added 2026-08-08). Zero tolerance, no ratchet: a founder
# objection that only lives in a ledger entry is a wish, not a rule. Checks every
# live surface's RENDERED text (a player must never see a retired line again) and
# every *.html/*.md SOURCE line for regeneration risk (a stale spec could put one
# back), with a citation carve-out so the historical record in TSP_Ledger.md etc.
# stays legible. Add an objection: append one entry to retired-lines.json.
echo; echo "-- tick 6: retired lines (founder objections with teeth) --"
if [ ! -f "$BELT_DIR/retired-lines-gate.py" ]; then echo "  (gate not mounted — skipped)"
elif [ -n "$SURFACES" ] && ! python3 -c "import playwright" >/dev/null 2>&1; then
  echo "  SKIPPED LOUD — playwright absent, the render pass is BLIND. Not a pass."
else
  if python3 "$BELT_DIR/retired-lines-gate.py" $SURFACES >/tmp/rl.out 2>&1; then
    echo "  pass  no retired line found live or uncited in source"
  else
    echo "  HALT  a retired line resurfaced:"; grep -E '^\s+HALT' /tmp/rl.out | sed 's/^/        /' | head -10; fail=1
  fi
fi

echo; echo "-- tick 7: touch floor (studio-fingers) --"

# REPOINTED 2026-08-08. Two sessions in one lane built two gates of this name; the merged
# survivor is studio-eyes/studio-fingers.py, which RENDERS on a 412x915 touch viewport.
# The source-parsing rival at repo root is RETIRED and now exits 2 — so the old block below
# is held inert rather than deleted, because a retired gate that returns nothing would have
# made this tick print "pass" forever. A silent pass is worse than no tick.
# RATCHET: 31 of 113 surfaces carry real debt (fingers-baseline.json, re-frozen).
if [ ! -f "$BELT_DIR/studio-eyes/studio-fingers.py" ] || [ ! -f "$BELT_DIR/fingers-baseline.json" ]; then
  echo "  (gate or baseline not mounted — skipped)"
elif ! python3 -c "import playwright" >/dev/null 2>&1; then
  echo "  SKIPPED LOUD — playwright absent, this gate is BLIND. Not a pass."
else
  python3 "$BELT_DIR/studio-eyes/studio-fingers.py" $SURFACES >/tmp/sf.out 2>&1
  if python3 - "$BELT_DIR/fingers-baseline.json" <<'PYSF'
import json,re,sys
base=json.load(open(sys.argv[1]))["counts"]
cur={}; f=None
for line in open('/tmp/sf.out',encoding='utf-8',errors='replace'):
    m=re.match(r'\s+[\u2717\u2713] (\S+)',line)
    if m: f=m.group(1); cur.setdefault(f,0); continue
    if f and re.match(r'\s+F-',line): cur[f]+=1
bad=[(k,v,base.get(k,0)) for k,v in cur.items() if v>base.get(k,0)]
for k,v,w in bad: print(f"  HALT  {k}: {v} untouchable finding(s), baseline {w} — new debt")
sys.exit(1 if bad else 0)
PYSF
  then echo "  pass  no new untouchable targets"; else fail=1; fi
fi

if false; then   # ---- OLD TICK 7 (source-parsing gate) RETIRED 2026-08-08, held inert ----
# Added 2026-08-08. STUDIO EYES answered "can this be SEEN" from the first belt; nothing
# ever answered "can this be TOUCHED." A player holds the thing one-handed, with a thumb,
# at arm's length. That is the shipping condition for every game the studio makes and it
# was ungated. RATCHET, not flat: 97 of 133 surfaces fail the 48px house floor today
# (fingers-baseline.json), and a flat tick would freeze deploy on day one over debt nobody
# was checking -- the same discovery that made ticks 1/3/4/5 ratchet.
if [ ! -f "$BELT_DIR/studio-fingers.py" ] || [ ! -f "$BELT_DIR/fingers-baseline.json" ]; then
  echo "  (gate or baseline not mounted — skipped)"
else
  rc=0
  for f in $SURFACES; do
    n=$(python3 "$BELT_DIR/studio-fingers.py" "$f" 2>/dev/null | grep -oE '## HALT +\[[0-9]+\]' | grep -oE '[0-9]+' | head -1)
    n=${n:-0}
    was=$(python3 -c "import json,sys;print(json.load(open('$BELT_DIR/fingers-baseline.json'))['counts'].get('${f#./}',0))" 2>/dev/null || echo 0)
    if [ "$n" -gt "$was" ]; then
      echo "  HALT  ${f#./}: $n untouchable target(s), baseline $was — new debt"; rc=1
    fi
  done
  if [ "$rc" -eq 0 ]; then echo "  pass  no new untouchable targets"; else fail=1; fi
fi
fi               # ---- end inert old tick 7 ----

# TICK 8 — scope: what a document reaches for (added 2026-08-09).
# TWO CLAUSES, ONE QUESTION. A says do not reach past what you were asked for; B says do
# not point at what you cannot touch.
#   A (FLAT, zero tolerance): no wide-corpus retrieval baked into an artifact. An errand
#     hunting a studio FILE ran an unfenced Drive full-text query and came back
#     holding three students' course portfolios, because "floor" matched "floor-to-ceiling
#     windows". A name-contains query has no reach into a document body — arithmetic, not
#     judgment. At zero today and there is no reason to ever add one. (This comment says
#     "full-text" on purpose: spelled the other way it trips its own tick, which is how
#     preflight caught it here before the push. Only the ruling itself is allowlisted.)
#   B (RATCHET): a governance doc may not name a file the trunk cannot reach. On the day
#     this armed, the project instructions ordered every session to read three files and
#     NONE of the three resolved. A rule pointing at an unreachable file fails silently and
#     forever — which is exactly how claude/FERPA-SCOPE-RULING.md went unread twice in one
#     day by the agent whose enforcement clause names it. Baseline: 5. That number is debt.
# WORKTREE, not origin/main: preflight must grade what is ABOUT to ship, not what shipped.
# The baseline is keyed to the REMOTE name, so a spoke without its own baseline prints
# UNMEAS and does not block — but clause A still halts everywhere, baseline or not.
echo; echo "-- tick 8: scope (what a document reaches for) --"
if [ ! -f "$BELT_DIR/scope-gate.py" ]; then
  echo "  (gate not mounted — skipped)"
elif ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "  SKIPPED LOUD — not a git checkout, this gate is BLIND. Not a pass."
else
  if SCOPE_BASELINE="$BELT_DIR/scope-baseline.json" \
     python3 "$BELT_DIR/scope-gate.py" worktree >/tmp/scope.out 2>&1; then
    echo "  pass  no wide retrieval, no new dangling citation"
    grep -E '^   (debt now|BASELINE MISMATCH)' /tmp/scope.out | sed 's/^   /        /'
  else
    grep -E '^   (HALT|NEW)|^HALT' /tmp/scope.out | sed 's/^/  /' | head -12
    fail=1
  fi
fi

echo; echo "----------------------------------------------------------------------"
if [ "$fail" -ne 0 ]; then
  echo "BELT: HALT — a tick refused. This build does not ship."
  [ "$MODE" = file ] && echo "       PREFLIGHT caught it before the push. That is the whole point."
else
  echo "BELT: PASS — all ticks clear."
  [ "$MODE" = file ] && echo "       Preflight only. Run the full belt before trusting a corpus-wide claim."
fi
exit $fail
