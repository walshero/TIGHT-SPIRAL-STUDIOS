#!/usr/bin/env python3
"""
STUDIO VOICE - PRE-SHIP GATE  v1.1
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
A flagged dash is not automatically wrong - it means a human clears it:
rewrite without it, or confirm it is Matt's own language and mark it.

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
import re, sys, os

def strip_comments_track_founder(text):
    """Walk the file once. Blank out HTML comments and JS comments (so their
    dashes never trigger a HALT - they're invisible to users), but if an HTML
    comment or JS comment carries a founder-verbatim marker, blank out the
    NEXT string/text run instead of flagging it. Returns the scannable text
    with founder-verbatim spans replaced by spaces (cleared) and ordinary
    comments replaced by spaces (irrelevant), everything else left intact."""
    out = []
    i = 0
    n = len(text)
    pending_founder_clear = False
    while i < n:
        if text.startswith('<!--', i):
            end = text.find('-->', i)
            end = end + 3 if end != -1 else n
            comment_body = text[i:end]
            if re.search(r'data-founder-(quote|verbatim|source)|FOUNDER-VERBATIM', comment_body, re.I):
                pending_founder_clear = True
            out.append(' ' * (end - i))
            i = end
            continue
        if text.startswith('/*', i):
            end = text.find('*/', i)
            end = end + 2 if end != -1 else n
            comment_body = text[i:end]
            if re.search(r'FOUNDER-VERBATIM', comment_body, re.I):
                pending_founder_clear = True
            out.append(' ' * (end - i))
            i = end
            continue
        if text.startswith('//', i):
            end = text.find('\n', i)
            end = end if end != -1 else n
            out.append(' ' * (end - i))
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
            out.append(' ' * (j - i))
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

def run(path):
    raw = open(path, encoding='utf-8', errors='replace').read()
    halts = em_dash_floor(raw)

    print()
    print('  STUDIO VOICE - PRE-SHIP GATE v1.1 - ' + os.path.basename(path))
    print('  ' + '-' * 60)
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

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: studio-voice-gate.py <file.html> [more.html ...]')
        sys.exit(2)
    sys.exit(max(run(p) for p in sys.argv[1:]))
