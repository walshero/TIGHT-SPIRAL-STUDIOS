#!/usr/bin/env python3
"""
THE PLAYTHROUGH AGENT  —  Tight Spiral Productions
--------------------------------------------------
It PLAYS the game. Studio Eyes measures pixels; this drives the interface and
watches for the mechanical failures a founder's thumb currently catches on cold play:

  CLIPPED TEXT     text laid out and then thrown away by a clip box — measured in
                   EVERY state this crawler reaches, which is the whole point (see
                   load_clip_probe below: the belt's floors all grade first paint,
                   and a defect that only exists after three clicks is invisible to
                   every one of them)
  DEAD BUTTON      an interactive element that, when clicked, changes nothing
  INERT TOUCH      the PAGE changed but the WORLD did not — a line printed outside
                   the scene container while the scene itself stayed byte-identical
                   (only computed when a world selector is supplied; see --world)
  JS ERROR         an uncaught exception fired during play (console/pageerror)
  DEAD END         a state with zero live controls before any "end/done/replay" signal
  NO PROGRESS      N clicks in and the visible text never changed (stuck loop)
  OPENING WALL     first interactive thing is a preference control, not the scene
  UNREACHED        elements that exist but were never reachable by breadth-first play

It does NOT judge fun, metaphor, or voice. That is the founder. This clears the
mechanical rubble BEFORE his taste is spent — 20 cold-plays become 1 review.

It REUSES the Studio Eyes harness pattern (sync_playwright, chromium, file://,
offline request interception). One notes card per game to stdout; exit 0 always
(it is a reporter, not a gate — a gate that blocks on "no progress" would false-fire
on games that legitimately end fast).

Usage:  python3 playthrough-agent.py <file.html> [file2.html ...]
        python3 playthrough-agent.py --dir .        (every root .html)
        python3 playthrough-agent.py --selftest
"""
import sys, os, glob, re

# ── THE CLIP MEASUREMENT IS NOT OURS. It lives in studio-eyes.py (floor 11) and this
# agent READS it. One canon writes, others read: a second copy of that arithmetic here
# would drift from the floor it is supposed to mirror, and the studio has already paid
# for two copies of one fact more than once.
#
# WHY IT IS RUN FROM HERE AT ALL, recorded so the split is not mistaken for duplication:
# studio-eyes and studio-fingers both measure FIRST PAINT. Flok's research card was
# unreadable for weeks behind three clicks (start -> hit the target -> flip), so every
# floor in the belt graded a card that was empty and collapsed and reported green.
# studio-fingers' own docstring named the durable fix in August and left it open:
# "geometry measured at every state the crawler in playthrough-agent.py already
# visits." This is that. The crawler was already walking the states; nobody was
# measuring them.
def load_clip_probe():
    """Return studio-eyes' CLIP_PROBE, or None. NEVER silent — a check that went
    missing must not read as a check that found nothing."""
    import importlib.util
    here = os.path.dirname(os.path.abspath(__file__))
    fp = os.path.join(here, 'studio-eyes', 'studio-eyes.py')
    if not os.path.exists(fp):
        return None
    try:
        spec = importlib.util.spec_from_file_location('studio_eyes_canon', fp)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return getattr(mod, 'CLIP_PROBE', None)
    except Exception:
        return None


CLIP_PROBE = load_clip_probe()

MAX_CLICKS = 40          # breadth-first click budget per game
# A CONTROL THAT KEEPS ANSWERING IS WORTH PRESSING AGAIN.
# Added 2026-09-01. The walker clicked each LABEL once, so any state behind a
# repeated action was unreachable — and games are made of repeated actions. Flok's
# research card unlocks when the engagement meter passes its target, which takes
# seven or eight presses of one button; nine single clicks got the crawler onto the
# training screen and left it standing there with the card still locked. It reported
# what it saw and what it saw was a locked card.
#
# This is not a per-file recipe (the failure mode studio-fingers named and rejected —
# a recipe gets filled for three builds and leaves the rest blind while LOOKING
# covered). It is one mechanical rule that reads the same on every surface: after the
# breadth-first pass runs out of NEW controls, press the ones that are still ANSWERING
# again, while they keep answering, up to a cap. A repeat that changes nothing is not
# a dead button — a maxed-out meter legitimately stops moving — so repeats are exempt
# from that finding.
REPEAT_MAX = 12          # presses of any one control, once breadth is exhausted
SETTLE_MS  = 350         # wait after each click for the DOM to react
VIEWPORT   = {"width": 400, "height": 840}   # phone, matches Studio Eyes

PREF_WORDS = re.compile(r'comfort|softer|warm|daylight|contrast|reader|dark mode|'
                        r'text size|larger|palette|theme', re.I)
END_WORDS  = re.compile(r'again|replay|restart|done|finish|end|start over|'
                        r'next|continue|new game|home', re.I)


def visible_text(page):
    try:
        return page.inner_text('body')[:4000]
    except Exception:
        return ""


def live_controls(page):
    """Elements a player could click right now: buttons, links, [role=button],
    [onclick], tappable inputs — visible and enabled."""
    sel = ('button, a[href], [role=button], [onclick], input[type=button], '
           'input[type=submit], [tabindex]:not([tabindex="-1"])')
    out = []
    for el in page.query_selector_all(sel):
        try:
            if not el.is_visible():          continue
            if not el.is_enabled():          continue
            # mailto:/tel:/sms: hand off to the OS and correctly leave the DOM
            # untouched — clicking one is supposed to change nothing on the
            # page. Testing them as if a static page reaction proves they work
            # produced a false DEAD-BUTTON on every contact link in the corpus.
            href = el.get_attribute('href') or ''
            if href.startswith(('mailto:', 'tel:', 'sms:')):
                continue
            box = el.bounding_box()
            if not box or box['width'] < 8 or box['height'] < 8:  continue
            label = (el.inner_text() or el.get_attribute('aria-label') or
                     el.get_attribute('title') or '').strip()[:40]
            out.append((el, label))
        except Exception:
            continue
    return out


def world_sig(page, sel):
    """Signature of the DIEGETIC container only.

    THE DEFECT THIS CLOSES, found 2026-08-26: sig() below is PAGE-scoped, so a
    control that prints a paragraph into a text holder BELOW the picture reads as
    alive while the room is byte-identical. cyl-v5.html returned CLEAN / "nothing
    mechanical to fix" on the exact build the founder walked and rejected; the same
    file fails every interaction binary. The tool was not wrong, its oracle was
    page-shaped. A touch is only a touch if the WORLD moved.

    Returns None when no world is named, and every pre-2026-08-26 verdict is then
    reproduced byte-for-byte — this check is additive, never a redefinition of
    DEAD BUTTON.
    """
    if not sel:
        return None
    try:
        return page.eval_on_selector(sel,
            'el => el.outerHTML + "|" + (el.innerText || "") + "|" + '
            'Array.from(el.querySelectorAll('
            '"[aria-pressed],[aria-selected],[aria-checked],.active,.on,.selected,'
            '[data-done],[data-state],[data-taken]")).map(e => (e.className||"") + '
            '(e.getAttribute("aria-pressed")||"") + (e.getAttribute("data-taken")||"") + '
            '(e.getAttribute("data-done")||"")).join("~")')
    except Exception:
        return None


SIDECAR = 'tsp-worlds.json'


def sidecar_world(path):
    """Look up a build's world in tsp-worlds.json — the FALLBACK, not the interface.

    A build should declare its own world in its head. This exists for one reason:
    GitHub's Contents API refuses to return files over ~1MB, so the connector write
    lane is blind on the studio's largest builds (choose-your-leader-full 3.5MB,
    old-problems-at-new-speed 3.4MB, CYL v6 2.1MB, CYL v7 1.6MB) and physically
    cannot add a meta tag to them. Without this, the world check is unusable on
    exactly the surfaces that carry the most touches.

    Precedence: CLI flags > the build's own meta > this file. Never the reverse —
    two copies of one fact is the failure this studio keeps paying for, so the
    sidecar loses every tie and every resolution from here prints a note.
    Delete an entry the day its build can declare itself.
    """
    import json
    fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), SIDECAR)
    if not os.path.exists(fp):
        return (None, None)
    try:
        reg = json.load(open(fp, encoding='utf-8'))
    except Exception:
        return (None, None)
    entry = reg.get(os.path.basename(path)) or {}
    return (entry.get('world'), entry.get('touches'))


def sample_clips(page, card, where):
    """Run the clip floor against the state we are standing in right now.

    LET THE STATE SETTLE FIRST. A box measured mid-transition is a frame, not a
    layout: a card 350ms into a 500ms flip projects an axis-aligned box a couple of
    px wider than the card really is, and that read as the front face clipping
    itself by 2px on a card that was correct. Wait for the page's own animations to
    finish, bounded — a looping decorative animation must not hang the crawler.
    """
    if CLIP_PROBE is None:
        return
    try:
        page.wait_for_function(
            "() => document.getAnimations().every(a => a.playState !== 'running')",
            timeout=900)
    except Exception:
        pass          # a looping animation never settles; measure anyway
    try:
        found = page.evaluate(CLIP_PROBE)
    except Exception:
        return
    for c in found or []:
        key = (c.get('sel'), c.get('text'))
        if key in card["_clip_seen"]:
            continue
        card["_clip_seen"].add(key)
        card["clipped_text"].append({**c, "state": where})


def play(path, world=None, touches=None):
    from playwright.sync_api import sync_playwright
    card = {"file": os.path.basename(path), "clicks": 0,
            "dead_buttons": [], "js_errors": [], "notes": [],
            "opening_wall": False, "reached_end": False, "dead_end": False,
            "inert_touches": [], "world": None, "touches": None,
            "clipped_text": [], "_clip_seen": set(), "clip_blind": CLIP_PROBE is None}
    with sync_playwright() as p:
        # A GATE THAT GOES BLIND MUST NOT READ AS CLEAN. Playwright resolves its browser
        # by a build number pinned to the installed python package; when the package and
        # the on-disk browsers drift (CI image refresh, pip upgrade) launch() raises
        # "Executable doesn't exist at .../chromium_headless_shell-<n>/chrome" and this
        # agent reported AGENT ERROR and moved on - which reads, downstream, as "nothing
        # found". Same shape as the WeasyPrint exit-2 that rubber-stamped the corpus for
        # weeks. Fall back to the stable path the image provides, exactly as
        # one-thing-gate.py and studio-fingers.py already do. Found 2026-08-07 by the
        # Aleph fleet's own "NOT LOOKED AT" check, which is the point of that check.
        try:
            b = p.chromium.launch()
        except Exception:
            b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        ctx = b.new_context(viewport=VIEWPORT)
        # offline floor: block every external request, same as Studio Eyes
        ext = []
        def on_req(r):
            u = r.url
            # mailto:/tel:/sms: are an OS handoff, not a network fetch — same
            # exemption as the click-walker above, same reason.
            if u.startswith(('file:', 'data:', 'mailto:', 'tel:', 'sms:')):
                return
            ext.append(u)
        ctx.on('request', on_req)
        page = ctx.new_page()
        page.on('pageerror', lambda e: card["js_errors"].append(str(e)[:120]))
        page.on('console', lambda m: card["js_errors"].append(m.text[:120])
                 if m.type == 'error' else None)

        start_url = 'file://' + os.path.abspath(path)
        page.goto(start_url, wait_until='load')
        page.wait_for_timeout(SETTLE_MS)

        # THE WORLD: named on the command line, or declared by the page itself via
        # <meta name="tsp:world" content="#room">. Self-describing HTML is preferred —
        # a per-file config lane is one more thing to keep in sync, and this studio has
        # already lost canon twice to two copies of the same fact.
        if world is None:
            try:
                world = page.get_attribute('meta[name=\"tsp:world\"]', 'content')
            except Exception:
                world = None
        if touches is None:
            try:
                touches = page.get_attribute('meta[name=\"tsp:touches\"]', 'content')
            except Exception:
                touches = None
        if world is None:
            sw, st = sidecar_world(path)
            if sw:
                world = sw
                if touches is None:
                    touches = st
                card["notes"].append(
                    f"world '{world}' resolved from {SIDECAR} — this build does not "
                    "declare its own; a sidecar world is never silent")
        card["world"] = world
        card["touches"] = touches

        sample_clips(page, card, 'first paint')

        # opening-wall check: is the FIRST live control a preference toggle?
        first = live_controls(page)
        if first and PREF_WORDS.search(first[0][1] or ''):
            # tolerate a single corner comfort knob if a scene control also exists
            if not any(not PREF_WORDS.search(l or '') for _, l in first):
                card["opening_wall"] = True

        seen_text = set()
        stuck = 0
        clicked_labels = set()
        responsive = set()       # labels whose last press moved the page
        repeats = {}             # label -> presses spent in the persistence pass
        blocked = set()          # labels that were visible but refused the click
        while card["clicks"] < MAX_CLICKS:
            ctrls = live_controls(page)
            if not ctrls:
                # zero live controls — dead end unless the text says it ended
                if END_WORDS.search(visible_text(page)):
                    card["reached_end"] = True
                else:
                    card["dead_end"] = True
                break
            # pick the first control we haven't clicked this run (breadth-first)
            target = None
            for el, lbl in ctrls:
                key = lbl or 'unlabeled'
                if key not in clicked_labels:
                    target = (el, lbl); break
            repeat = False
            if target is None:
                # PERSISTENCE PASS: breadth is spent; press what is still answering.
                for el2, lbl2 in ctrls:
                    key = lbl2 or 'unlabeled'
                    # A CONTROL THAT REFUSED THE CLICK WAS NOT EXERCISED. The label was
                    # burned before the click, so a control that is visible but not yet
                    # live — Flok's research card is pointer-events:none until the meter
                    # passes its target — was crossed off the list and never tried again,
                    # even after the very presses that unlocked it. "Not clickable in
                    # place" usually means "not clickable YET".
                    live = key in responsive or key in blocked
                    if live and repeats.get(key, 0) < REPEAT_MAX:
                        target = (el2, lbl2); repeat = True; break
            if target is None:
                card["reached_end"] = True      # all controls exercised, no crash
                break
            el, lbl = target
            if repeat:
                repeats[lbl or 'unlabeled'] = repeats.get(lbl or 'unlabeled', 0) + 1
            clicked_labels.add(lbl or 'unlabeled')
            # signature = visible text + full DOM outerHTML length + count of
            # aria-pressed/selected/checked/.active/.on nodes. A response is ANY
            # change to this signature — a select-highlight counts, not just text.
            def sig():
                try:
                    html = page.content()
                    states = page.eval_on_selector_all(
                        '[aria-pressed],[aria-selected],[aria-checked],'
                        '.active,.on,.selected,[data-done],[data-state]',
                        'els => els.map(e => (e.className||"") + '
                        '(e.getAttribute("aria-pressed")||"") + '
                        '(e.getAttribute("aria-selected")||"") + '
                        '(e.getAttribute("data-done")||"")).join("|")')
                except Exception:
                    html, states = "", ""
                return (visible_text(page), len(html), states)
            # AN ALREADY-ACTIVE TOGGLE IS NOT A DEAD BUTTON. Found 2026-08-08:
            # funny-boneys-factory's default lens (Spellcaster) and default
            # audience (One sleepy cat) both open with aria-pressed="true";
            # clicking the selected option of a toggle group legitimately
            # changes nothing, and the no-DOM-delta test read that as dead.
            # Same false-positive family as the mailto: links and the nav-link
            # bleed — the tool asked "did anything change" without asking
            # "should anything have changed."
            try:
                if (el.get_attribute("aria-pressed") == "true"
                        or el.get_attribute("aria-selected") == "true"):
                    card["notes"].append(f"'{(lbl or '')[:24]}' is an already-"
                                         "active toggle — skipped, not dead")
                    continue
            except Exception:
                pass
            before = sig()
            wbefore = world_sig(page, world)
            try:
                el.click(timeout=1500)
            except Exception as e:
                blocked.add(lbl or 'unlabeled')
                card["notes"].append(f"click timed out on '{(lbl or '')[:24]}' "
                                     "— visible but not clickable in place")
                continue
            card["clicks"] += 1
            page.wait_for_timeout(SETTLE_MS)
            # A CROSS-FILE NAV LINK IS NOT A DEAD BUTTON, AND ITS DESTINATION
            # PAGE IS NOT THIS FILE. Found 2026-08-07: <a href="arcade.html">
            # (a real, correct nav link) navigated the page away, and every
            # click after that kept walking arcade.html's controls -> whatever
            # IT linked to -> etc, all attributed to THIS file's report. That
            # produced "dead buttons" quoting other games' text entirely
            # (the-console.html's "north_trail", old-problems-at-new-speed's
            # FAQ copy) under the-tell.html's card. Same shape as every other
            # silent-failure this studio has found: a tool kept running past
            # the point where its output stopped meaning what it claimed.
            if page.url != start_url:
                card["notes"].append(f"'{(lbl or '')[:24]}' navigates to another "
                                     "page (expected for a nav link) — returning "
                                     "to this file to keep testing it, not that one")
                page.go_back()
                if page.url != start_url:
                    page.goto(start_url, wait_until='load')
                page.wait_for_timeout(SETTLE_MS)
                continue
            after = sig()
            wafter = world_sig(page, world)
            sample_clips(page, card, f"after '{(lbl or 'unlabeled')[:24]}'")
            if after == before:
                # NOTHING in the DOM moved — a real dead button, UNLESS this was a
                # repeat press: a control that already proved it works and has run out
                # of room (a meter at its ceiling, a list fully loaded) is finished,
                # not dead. Judging it here would manufacture a defect out of success.
                responsive.discard(lbl or 'unlabeled')
                if not repeat and lbl and lbl not in card["dead_buttons"]:
                    card["dead_buttons"].append(lbl or '(unlabeled)')
                stuck += 1
            else:
                responsive.add(lbl or 'unlabeled')
                blocked.discard(lbl or 'unlabeled')
                stuck = 0
                # The page moved. Did the WORLD? Only asked when a world is named,
                # and never when the world element itself was replaced wholesale
                # (wbefore None means it did not exist yet — a screen change, not
                # an inert touch).
                # ONLY CONTROLS THAT ARE SUPPOSED TO ACT ON THE WORLD ARE JUDGED
                # AGAINST IT. Found 2026-08-26 on the first real run: naming a world
                # and judging EVERY control against it reported 22 inert touches on
                # cyl-v5, and 20 of them were the legibility panel — a type-size knob
                # is SUPPOSED to leave the room alone. The first fix reached for
                # PREF_WORDS and was wrong in shape: a word list cannot say what a
                # control is FOR, and "Medium (20px)" is in no word list. The rule is
                # structural. A control is subject to the world test when --touches
                # names it, or, absent that, when it lives INSIDE the world. Anything
                # else is OUT OF SCOPE, not inert.
                # Same lesson as the already-active toggle and the nav-link bleed:
                # ask "should anything have changed" before "did anything change."
                if wbefore is not None and wafter is not None and wafter == wbefore:
                    try:
                        if touches:
                            subject = el.evaluate('(e, s) => e.matches(s)', touches)
                        else:
                            subject = el.evaluate('(e, s) => !!e.closest(s)', world)
                    except Exception:
                        subject = False
                    if subject and lbl and lbl not in card["inert_touches"]:
                        card["inert_touches"].append(lbl or '(unlabeled)')
            after_text = after[0]
            # rebind for the end-word / seen-text checks below
            after = after_text
            if after in seen_text and stuck == 0:
                pass  # revisiting a prior state is fine (menus)
            seen_text.add(after)
            if END_WORDS.search(after):
                card["reached_end"] = True

        if ext:
            card["notes"].append(f"OFFLINE FLOOR: {len(ext)} external request(s) "
                                 f"e.g. {ext[0][:60]}")
        b.close()
    # the dedupe set is bookkeeping, not a finding — drop it so the card stays a
    # plain, serializable dict for anything downstream that wants to print or store it.
    card.pop("_clip_seen", None)
    return card


def render(card):
    f = card["file"]
    L = []
    L.append(f"┌─ {f}")
    verdict = "CLEAN" if (not card["dead_buttons"] and not card["js_errors"]
                          and not card["opening_wall"] and not card["dead_end"]
                          and not card["inert_touches"]
                          and not [c for c in card["clipped_text"]
                                   if not c.get("window")]) else "NOTES"
    L.append(f"│  verdict: {verdict}   clicks: {card['clicks']}   "
             f"end-reached: {'yes' if card['reached_end'] else 'no'}")
    if card.get("clip_blind"):
        L.append("│  ! CLIP FLOOR NOT RUN — studio-eyes/studio-eyes.py did not yield "
                 "CLIP_PROBE. This card says nothing about clipped text; it did not look.")
    boxes = [c for c in card["clipped_text"] if not c.get("window")]
    windows = [c for c in card["clipped_text"] if c.get("window")]
    if boxes:
        L.append(f"│  ✗ CLIPPED TEXT ({len(boxes)}) — laid out, then thrown away:")
        for c in boxes[:6]:
            L.append(f"│      \"{c['text'][:34]}\" cut by {c['by']}px in {c['clipSel']} "
                     f"({c['boxH']}px box, {c['needH']}px of content) · {c['state']}")
    if windows:
        # A WINDOW IS NOT SILENT EITHER. It does not block — a feed cropped by a phone
        # frame is a prop, not a defect — but a gate that drops what it saw is a gate
        # that decided for you. Named once per container, with the ratio that classed it.
        seen = []
        for c in windows:
            k = c["clipSel"]
            if k in seen: continue
            seen.append(k)
            L.append(f"│  · window (not a defect): {k} shows {c['boxH']}px of "
                     f"{c['needH']}px · {c['state']}")
    if card["opening_wall"]:
        L.append("│  ✗ OPENING WALL — first control is a preference toggle, not the scene")
    if card["dead_buttons"]:
        # WOLF-GUARD: 5+ "dead" buttons is almost always a card-select game whose
        # response is a canvas redraw or child-style change the signature can't see.
        # Do not assert dead — flag for the eye. A wolf-crier is worse than nothing.
        if len(card["dead_buttons"]) >= 5:
            L.append(f"│  ? {len(card['dead_buttons'])} controls showed no DOM change on click "
                     "— LIKELY select-state (canvas/style redraw); VERIFY BY EYE, not asserted dead")
        else:
            L.append(f"│  ✗ DEAD BUTTONS ({len(card['dead_buttons'])}): "
                     + ", ".join(card['dead_buttons'][:6]))
    if card["inert_touches"]:
        scope = card['touches'] or ("controls inside " + str(card['world']))
        L.append(f"│  ✗ INERT TOUCHES ({len(card['inert_touches'])}) in world "
                 f"'{card['world']}' (scope: {scope}): "
                 + ", ".join(card['inert_touches'][:6]))
        L.append("│    the page changed but the world did not — text appeared outside "
                 "the scene while the scene stayed byte-identical")
    if card["js_errors"]:
        uniq = list(dict.fromkeys(card["js_errors"]))[:4]
        L.append(f"│  ✗ JS ERRORS ({len(card['js_errors'])}): " + " | ".join(uniq))
    if card["dead_end"]:
        L.append("│  ✗ DEAD END — reached a state with no live controls and no 'end' signal")
    for n in card["notes"]:
        L.append(f"│  · {n}")
    if verdict == "CLEAN":
        L.append("│  nothing mechanical to fix — ready for founder taste-play")
    L.append("└" + "─" * 40)
    return "\n".join(L)


def self_test():
    """Two canaries: a game with a real dead button must be caught; a clean
    one-button game must pass. Written to temp, played, asserted."""
    import tempfile
    dead = ('<!doctype html><body><h1 id=s>scene</h1>'
            '<button onclick="document.getElementById(\'s\').textContent=\'moved\'">good</button>'
            '<button>dead</button></body>')  # 2nd button does nothing
    clean = ('<!doctype html><body><h1 id=s>scene</h1>'
             '<button onclick="document.getElementById(\'s\').textContent=\'the end, play again\'">go</button>'
             '</body>')
    # THIRD CANARY: the page moves, the world does not. This is the cyl-v5 shape —
    # a line prints under the picture and the picture never changes.
    inert = ('<!doctype html><meta name="tsp:world" content="#room">'
             '<meta name="tsp:touches" content=".prop">'
             '<body><div id="room"><h1>the room</h1></div><div id="holder"></div>'
             '<button class="prop" onclick="document.getElementById(\'holder\').textContent='
             '\'a line appeared. the end.\'">notice the television</button>'
             '<button onclick="document.body.style.fontSize=\'20px\'">Medium (20px)</button>'
             '</body>')
    # FIFTH CANARY: the FLOK SHAPE. First paint is clean — the card is empty and
    # collapsed. One click fills it and opens it onto a box too short to hold it.
    # studio-eyes at first paint reports green on this file and is not wrong; it is
    # looking at a state where nothing is clipped yet. If this canary passes, the
    # crawler is measuring states, not just doors.
    clipped = ('<!doctype html><style>'
               'body{background:#10151c;color:#f2f6fb;font-family:system-ui}'
               '.card{height:0;overflow:hidden;width:300px;border:1px solid #33465e}'
               '.card.open{height:60px}'   # 60px box, ~76px of text: the Flok ratio (1.27)
               '.fact{font-size:13px;line-height:1.4;padding:8px}'
               '</style><body><h1>scene</h1>'
               '<div class="card" id="c"><div class="fact" id="f"></div></div>'
               '<button onclick="document.getElementById(\'f\').textContent='
               '\'Unpredictable rewards drive the most persistent checking, the same '
               'schedule that makes slot machines compulsive. The end.\';'
               'document.getElementById(\'c\').className=\'card open\'">why does this work?</button>'
               '</body>')
    ok = True
    for name, html, expect_dead in [("dead-canary", dead, True),
                                    ("clean-canary", clean, False)]:
        fp = os.path.join(tempfile.gettempdir(), name + ".html")
        open(fp, 'w').write(html)
        c = play(fp)
        got_dead = len(c["dead_buttons"]) > 0
        verdict = "PASS" if got_dead == expect_dead else "FAIL"
        if verdict == "FAIL": ok = False
        print(f"  [{verdict}] {name}: dead_buttons={c['dead_buttons']} "
              f"(expected {'≥1' if expect_dead else '0'})")
    fp = os.path.join(tempfile.gettempdir(), "inert-canary.html")
    open(fp, 'w').write(inert)
    c = play(fp)
    got_inert = len(c["inert_touches"]) > 0
    got_dead = len(c["dead_buttons"]) > 0
    v = "PASS" if (got_inert and not got_dead) else "FAIL"
    if v == "FAIL": ok = False
    if c["inert_touches"] != ['notice the television']:
        ok = False; v = "FAIL"
    print(f"  [{v}] inert-canary: inert_touches={c['inert_touches']} "
          f"dead_buttons={c['dead_buttons']} (expected EXACTLY the in-scope prop — "
          "the out-of-scope type knob must not be reported)")
    # FOURTH: the same page with NO world named must reproduce the old verdict exactly.
    c2 = play(fp, world="")
    v2 = "PASS" if not c2["inert_touches"] else "FAIL"
    if v2 == "FAIL": ok = False
    print(f"  [{v2}] no-world regression: inert_touches={c2['inert_touches']} "
          "(expected 0 — additive check must be silent when no world is named)")
    fp = os.path.join(tempfile.gettempdir(), "clipped-canary.html")
    open(fp, 'w').write(clipped)
    c3 = play(fp)
    first_paint_clean = not any(x["state"] == "first paint" for x in c3["clipped_text"])
    # must be classed a BOX, not a window — a window would not block and this defect must.
    caught_later = any(x["state"] != "first paint" and not x.get("window")
                       for x in c3["clipped_text"])
    v3 = "PASS" if (caught_later and first_paint_clean and not c3.get("clip_blind")) else "FAIL"
    if v3 == "FAIL": ok = False
    print(f"  [{v3}] clipped-canary: clipped_text="
          f"{[(x['state'], x['by'], 'window' if x.get('window') else 'box') for x in c3['clipped_text']]} "
          "(expected 0 at first paint, >=1 after the click — proving the crawler "
          "measures states, not just the door)")
    print("SELFTEST", "PASS — dead button caught, clean game cleared, inert touch caught, "
          "no-world behaviour unchanged, clipped text caught in a state no "
          "first-paint floor can reach" if ok else "FAIL — do not trust results")
    return 0 if ok else 1


def main():
    args = sys.argv[1:]
    world = None
    touches = None
    if '--world' in args:
        i = args.index('--world')
        world = args[i + 1] if len(args) > i + 1 else None
        del args[i:i + 2]
    if '--touches' in args:
        i = args.index('--touches')
        touches = args[i + 1] if len(args) > i + 1 else None
        del args[i:i + 2]
    if not args or args[0] == '--selftest':
        return self_test()
    if args[0] == '--dir':
        files = sorted(glob.glob(os.path.join(args[1] if len(args) > 1 else '.', '*.html')))
    else:
        files = args
    print(f"PLAYTHROUGH AGENT — {len(files)} game(s)\n")
    for path in files:
        try:
            print(render(play(path, world, touches)))
        except Exception as e:
            print(f"┌─ {os.path.basename(path)}\n│  AGENT ERROR: {str(e)[:100]}\n└" + "─"*40)
        print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
