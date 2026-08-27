#!/usr/bin/env python3
"""
STUDIO VOICE - PRE-SHIP GATE  v1.2
Tight Spiral Studios

Sibling to studio-eyes-sweep.py ("Studio Eyes" - verifies founder VISION in the
sandbox). This one is "Studio Voice" - verifies founder LANGUAGE.

WHY THIS EXISTS
---------------
Founder ruling, 2026-08-05: "the general voice here is not mine and needs to
be closer or not have voice at all." Machine-generated copy on studio surfaces
had drifted into generic AI prose - most visibly, liberal em dashes used as a
decorative comma-replacement, several per screen. Checked against the actual
founder corpus (EN195-025 syllabus, live Google Doc, read in full 2026-08-05):
Matt DOES use an em dash in his own real writing - twice in ~2500 words, both
times marking a genuine pivot ("...it means coming to class prepared for the
day's activities", "...more evidence is certainly needed"). That is sparing
and load-bearing. Machine prose was using it as a tic, ten times the rate,
doing none of the work. The gap is not "founder never uses dashes" - it is
"the machine was using a founder move without having earned it."

V1 -> V1.1, LOGGED NOT HIDDEN
------------------------------
v1 stripped <script> blocks before scanning, on the theory that code should
be checked separately from markup. That was wrong for THIS check specifically:
most of a single-file game's visible text is JS string literals rendered via
textContent/innerHTML at runtime, not static HTML. v1 caught 16 dashes on
en195-arcade.html. The real count, scanning the whole file, is 60. Same shape
of blind spot studio-eyes-sweep.py's image-floor check has on JS-built art
(documented in that file's own history) - a static scan that skips anything
built by script undercounts, and an undercount reads as "mostly fine" when it
is not. v1.1 scans the whole file and excludes only genuine comments (HTML
<!-- -->, JS // and /* */), which are never visible to a user.

WHAT THIS GATE CHECKS
----------------------
Every em dash (—) or spaced en dash (word – word) in the file HALTS, UNLESS:
  (a) it falls inside an HTML comment (<!-- -->) - never visible, not voice
  (b) it falls inside a JS comment (// or /* */) - same reasoning
  (c) it sits inside a block explicitly marked founder-verbatim
      (data-founder-quote / data-founder-source / data-founder-verbatim on
      an ancestor tag, or a same-line marker comment /* FOUNDER-VERBATIM */
      immediately before a JS string literal)
  (d) it sits between /* SOURCE-VERBATIM-BEGIN */ and /* SOURCE-VERBATIM-END */
      (or the HTML-comment forms). See below.

QUOTED SOURCE TEXT (v1.2, 2026-08-27)
--------------------------------------
A poem is not studio voice. Dickinson's dashes and Crane's dashes are the poems;
rewriting one to clear this gate would be falsifying a text the studio is putting
in front of students to read closely. The founder-verbatim marker already encodes
the right idea - "this is quoted, not ours, and not editable" - but it clears one
string literal at a time and it is named for Matt. A poem bank is dozens of lines.

So v1.2 adds a REGION marker with an honest name:

    /* SOURCE-VERBATIM-BEGIN  Sandburg 1916, Dickinson 1891 - public domain */
    ... poem data, rendered exactly as published ...
    /* SOURCE-VERBATIM-END */

Everything between is blanked before the dash scan, the same way a comment is.

The teeth that keep this from becoming a loophole:
  - It is a REGION, so it is visible in a diff as a region. Wrapping the whole
    file would be obvious on sight, and reviewable.
  - It does not nest and it does not span files. An unclosed BEGIN blanks to end
    of file, which is exactly the kind of thing a reviewer notices.
  - It clears nothing by itself. A human still has to decide that the text inside
    really is quoted source, and write down which source, in the marker.
The alternative - writing the dash as a \\u2014 escape so the regex stops seeing the
character - would pass silently with nobody deciding anything. That is a gate gone
blind, which this repo has a standing rule against.

A flagged dash is not automatically wrong - it means a human clears it: rewrite
without it, confirm it is Matt's own language and mark it, or mark the region as
quoted source.

WHAT THIS GATE DOES NOT DO (v1.1 known gaps, stated not hidden)
------------------------------------------------------------------
- Cannot judge whether non-dash prose actually sounds like Matt. That needs
  a real founder corpus and a human ear, not regex.
- The founder-verbatim JS-comment marker is a convention this gate invented
  today: nothing in the corpus uses it yet, so until content is marked, every
  dash in script will HALT. That is correct behavior, not a bug - it means
  the founder-verbatim allowlist starts empty and grows by explicit marking,
  never by assumption.
- This gate is internal-governance-log-exempt by design: TSP_Ledger.md and
  similar dev logs are not student- or public-facing voice surfaces and are
  not swept by this tool. Scope is deliberately student/public-facing HTML.

exit 0 = ship. exit 1 = HALT.
"""
import re, sys, os, json

# ---- the ratchet -------------------------------------------------------------
# Measured 2026-08-07 before mounting this gate on the belt: 101 of 131 surfaces
# HALT. Armed flat, this gate would paint every repo red on every push and be
# disarmed inside a week — the floor.yml lesson from July, repeated. So it
# ratchets, and its unit is a per-file COUNT: the dash count may fall or hold,
# never rise. Debt is carried, never forgiven, and the list only shrinks.
BASELINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'voice-baseline.json')

def load_baseline():
    if os.path.exists(BASELINE):
        with open(BASELINE) as f:
            return json.load(f).get('debt', {})
    return None

def key_for(p, repo):
    """Baseline key = <repo>/<path relative to the repo root>.

    NOT the bare basename. Three of the five repos ship an index.html; keyed by
    basename they collide into one entry and the last one written silently grants
    or denies the other two. The belt runs one gate against many repos, so the key
    has to name the repo."""
    ap = os.path.abspath(p)
    rel = os.path.relpath(ap, os.getcwd())
    if rel.startswith(os.pardir):
        rel = os.path.basename(ap)
    return repo + '/' + rel.replace(os.sep, '/')

def strip_comments_track_founder(text):
    """Walk the file once. Blank out HTML comments and JS comments (so their
    dashes never trigger a HALT - they're invisible to users), but if an HTML
    comment or JS comment carries a founder-verbatim marker, blank out the
    NEXT string/text run instead of flagging it. Returns the scannable text
    with founder-verbatim spans replaced by spaces (cleared) and ordinary
    comments replaced by spaces (irrelevant), everything else left intact."""
    def blank(seg):
        # blank to spaces but KEEP newlines, so reported line numbers stay true.
        # Without this every halt after the first comment is reported on the wrong
        # line, which has been the case since v1 and is fixed here in v1.2.
        return re.sub(r'[^\n]', ' ', seg)
    out = []
    i = 0
    n = len(text)
    pending_founder_clear = False
    # SOURCE-VERBATIM regions are blanked wholesale. Cheapest correct way to do
    # that in a single pass: find the spans first, then blank as we walk over them.
    src_spans = []
    for m in re.finditer(r'SOURCE-VERBATIM-BEGIN', text, re.I):
        e = re.search(r'SOURCE-VERBATIM-END', text[m.end():], re.I)
        # an unclosed BEGIN blanks to end of file, on purpose: loud, not silent
        src_spans.append((m.start(), m.end() + e.end() if e else n))
    def in_source(pos):
        return any(a <= pos < b for a, b in src_spans)
    while i < n:
        if in_source(i):
            end = next(b for a, b in src_spans if a <= i < b)
            out.append(blank(text[i:end]))
            i = end
            continue
        if text.startswith('<!--', i):
            end = text.find('-->', i)
            end = end + 3 if end != -1 else n
            comment_body = text[i:end]
            if re.search(r'data-founder-(quote|verbatim|source)|FOUNDER-VERBATIM', comment_body, re.I):
                pending_founder_clear = True
            out.append(blank(text[i:end]))
            i = end
            continue
        if text.startswith('/*', i):
            end = text.find('*/', i)
            end = end + 2 if end != -1 else n
            comment_body = text[i:end]
            if re.search(r'FOUNDER-VERBATIM', comment_body, re.I):
                pending_founder_clear = True
            out.append(blank(text[i:end]))
            i = end
            continue
        if text.startswith('//', i):
            end = text.find('\n', i)
            end = end if end != -1 else n
            out.append(blank(text[i:end]))
            i = end
            continue
        # not a comment start - check if we owe a founder-verbatim clear on
        # the next quoted string literal or tag's text content
        if pending_founder_clear and text[i] in ("'", '"'):
            quote = text[i]
            j = i + 1
            while j < n and text[j] != quote:
                if text[j] == '\\':
                    j += 2
                else:
                    j += 1
            j = min(j + 1, n)
            out.append(blank(text[i:j]))
            i = j
            pending_founder_clear = False
            continue
        out.append(text[i])
        i += 1
    return ''.join(out)

def em_dash_floor(raw):
    scannable = strip_comments_track_founder(raw)
    halts = []
    for m in re.finditer(r'—|(?<=\w)\s–\s(?=\w)', scannable):
        snippet = scannable[max(0, m.start()-35):m.start()+35].strip()
        snippet = re.sub(r'\s+', ' ', snippet)
        if not snippet:
            continue
        line_no = scannable.count('\n', 0, m.start()) + 1
        halts.append('H-VOICE-DASH line ' + str(line_no) + ': "...' + snippet + '..."')
    return halts

def run(path, ratchet=False, base=None, repo=''):
    raw = open(path, encoding='utf-8', errors='replace').read()
    halts = em_dash_floor(raw)
    name  = key_for(path, repo) if ratchet else os.path.basename(path)
    n     = len(halts)

    print()
    print('  STUDIO VOICE - PRE-SHIP GATE v1.2 - ' + name +
          ('  ·  RATCHET' if ratchet else ''))
    print('  ' + '-' * 60)

    if ratchet:
        # A file the baseline never saw is NEW WORK and must meet the standard.
        allowed = (base or {}).get(name)
        if allowed is None:
            if n:
                print('  HALT - do not ship (NEW FILE - new work meets the standard):')
                for h in halts:
                    print('     ' + h)
                print()
                print('  ' + str(n) + ' unmarked dash(es), and this file carries no baseline debt.')
                print()
                return 1
            print('  SHIP - no unmarked em/en dashes anywhere in the file.')
            print()
            return 0
        if n > allowed:
            print('  HALT - do not ship (REGRESSION - the ratchet turns one way):')
            for h in halts:
                print('     ' + h)
            print()
            print('  ' + str(n) + ' unmarked dash(es); the baseline carries ' +
                  str(allowed) + '. A dash count may fall or hold, never rise.')
            print()
            return 1
        if n:
            print('  PASS (debt carried) - ' + str(n) + ' of ' + str(allowed) +
                  ' baselined dash(es). Counted, not forgiven.')
            if n < allowed:
                print('  The ratchet moved: re-run --init to lock the gain in.')
            print()
            return 0
        print('  SHIP - no unmarked em/en dashes anywhere in the file.')
        print()
        return 0

    if halts:
        print('  HALT - do not ship:')
        for h in halts:
            print('     ' + h)
        print()
        print('  ' + str(len(halts)) + ' unmarked dash(es) found (comments excluded).')
        print()
        return 1
    print('  SHIP - no unmarked em/en dashes anywhere in the file.')
    print()
    return 0


def init(paths, repo='', merge=None):
    """Freeze today's dash debt. This is the ONLY time the baseline may grow."""
    debt = dict(merge or {})
    for p in paths:
        raw = open(p, encoding='utf-8', errors='replace').read()
        n = len(em_dash_floor(raw))
        if n:
            debt[key_for(p, repo)] = n
    with open(BASELINE, 'w') as f:
        json.dump({
            'created': '2026-08-07',
            'why': ('Founder-voice debt frozen the day this gate was mounted on the studio '
                    'belt. 101 of 131 surfaces carried unmarked dashes. These are CARRIED - '
                    'counted, not forgiven. Any NEW dash blocks. The list may only shrink.'),
            'rule': ("A file's dash count may fall or hold, never rise. Clear a file and it "
                     'leaves the baseline forever.'),
            'debt': dict(sorted(debt.items())),
        }, f, indent=1)
        f.write('\n')
    print('BASELINE WRITTEN - ' + str(len(debt)) + ' file(s) carry known voice debt.')
    print('These do not block. Everything else does. The ratchet is armed.')
    return 0


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    repo = next((a.split('=', 1)[1] for a in sys.argv[1:] if a.startswith('--repo=')),
                os.path.basename(os.getcwd()))
    if not args:
        print('usage: studio-voice-gate.py [--ratchet|--init] [--repo=NAME] '
              '<file.html> [more.html ...]')
        sys.exit(2)
    if '--init' in sys.argv:
        # --merge keeps entries already frozen for OTHER repos; the belt seeds one
        # repo at a time and a plain rewrite would drop the others' debt.
        sys.exit(init(args, repo,
                      load_baseline() if '--merge' in sys.argv else None))
    ratchet = '--ratchet' in sys.argv
    base = load_baseline() if ratchet else None
    if ratchet and base is None:
        print('HALT - --ratchet asked for but voice-baseline.json is missing.\n'
              '       A gate that cannot find its baseline does not pass; it stops.',
              file=sys.stderr)
        sys.exit(2)
    sys.exit(max(run(p, ratchet, base, repo) for p in args))
