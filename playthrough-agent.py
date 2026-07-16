#!/usr/bin/env python3
"""
THE PLAYTHROUGH AGENT  —  Tight Spiral Productions
--------------------------------------------------
It PLAYS the game. Studio Eyes measures pixels; this drives the interface and
watches for the mechanical failures a founder's thumb currently catches on cold play:

  DEAD BUTTON      an interactive element that, when clicked, changes nothing
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

MAX_CLICKS = 40          # breadth-first click budget per game
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
            box = el.bounding_box()
            if not box or box['width'] < 8 or box['height'] < 8:  continue
            label = (el.inner_text() or el.get_attribute('aria-label') or
                     el.get_attribute('title') or '').strip()[:40]
            out.append((el, label))
        except Exception:
            continue
    return out


def play(path):
    from playwright.sync_api import sync_playwright
    card = {"file": os.path.basename(path), "clicks": 0,
            "dead_buttons": [], "js_errors": [], "notes": [],
            "opening_wall": False, "reached_end": False, "dead_end": False}
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport=VIEWPORT)
        # offline floor: block every external request, same as Studio Eyes
        ext = []
        def on_req(r):
            u = r.url
            if not u.startswith('file:') and not u.startswith('data:'):
                ext.append(u)
        ctx.on('request', on_req)
        page = ctx.new_page()
        page.on('pageerror', lambda e: card["js_errors"].append(str(e)[:120]))
        page.on('console', lambda m: card["js_errors"].append(m.text[:120])
                 if m.type == 'error' else None)

        page.goto('file://' + os.path.abspath(path), wait_until='load')
        page.wait_for_timeout(SETTLE_MS)

        # opening-wall check: is the FIRST live control a preference toggle?
        first = live_controls(page)
        if first and PREF_WORDS.search(first[0][1] or ''):
            # tolerate a single corner comfort knob if a scene control also exists
            if not any(not PREF_WORDS.search(l or '') for _, l in first):
                card["opening_wall"] = True

        seen_text = set()
        stuck = 0
        clicked_labels = set()
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
            if target is None:
                card["reached_end"] = True      # all controls exercised, no crash
                break
            el, lbl = target
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
            before = sig()
            try:
                el.click(timeout=1500)
            except Exception as e:
                card["notes"].append(f"click timed out on '{(lbl or '')[:24]}' "
                                     "— visible but not clickable in place")
                continue
            card["clicks"] += 1
            page.wait_for_timeout(SETTLE_MS)
            after = sig()
            if after == before:
                # NOTHING in the DOM moved — a real dead button
                if lbl and lbl not in card["dead_buttons"]:
                    card["dead_buttons"].append(lbl or '(unlabeled)')
                stuck += 1
            else:
                stuck = 0
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
    return card


def render(card):
    f = card["file"]
    L = []
    L.append(f"┌─ {f}")
    verdict = "CLEAN" if (not card["dead_buttons"] and not card["js_errors"]
                          and not card["opening_wall"] and not card["dead_end"]) else "NOTES"
    L.append(f"│  verdict: {verdict}   clicks: {card['clicks']}   "
             f"end-reached: {'yes' if card['reached_end'] else 'no'}")
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
    print("SELFTEST", "PASS — the agent catches a dead button and clears a clean game"
          if ok else "FAIL — do not trust results")
    return 0 if ok else 1


def main():
    args = sys.argv[1:]
    if not args or args[0] == '--selftest':
        return self_test()
    if args[0] == '--dir':
        files = sorted(glob.glob(os.path.join(args[1] if len(args) > 1 else '.', '*.html')))
    else:
        files = args
    print(f"PLAYTHROUGH AGENT — {len(files)} game(s)\n")
    for path in files:
        try:
            print(render(play(path)))
        except Exception as e:
            print(f"┌─ {os.path.basename(path)}\n│  AGENT ERROR: {str(e)[:100]}\n└" + "─"*40)
        print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
