#!/usr/bin/env python3
"""
STUDIO FINGERS · PLAY MODE                               Tight Spiral Productions
-----------------------------------------------------------------------------
Rebuilt 2026-10-13. A September session reported "studio-fingers-play.py" built and
committed; it is in neither repo's history. CHECKED IS NOT SHIPPED. This version
reads the senses-crawl v2 bundle instead of driving its own browser, so Fingers,
Eyes, Ears and the seats all judge the same play-through.

Static Fingers (studio-eyes/studio-fingers.py) measures FIRST PAINT. It could not
see that Flok v25 pushed the core verb (Boost) to y=930 on every phone, or that the
win button (Next) landed 250-320px below the fold. This reads every tap the crawl
made, as a thumb made it.

THE FLOORS
  P1 VERB IN VIEW     a control tapped 2+ times in a row (the level's core verb)     HALT
                      needed a scroll again after its first tap. (Amended 2026-10-14:
                      the screen opens at its brief; one scroll to the verb is allowed.) [LAW] founder 2026-09-24, "the
                      phone is the scene": the thing you act on and the action
                      are on screen together.
  P2 PATH IN VIEW     a control that moved the game to a different screen needed   HALT
                      a scroll, on the game's main path (first pass through each
                      screen). Screens the build marks data-secondary (credits,
                      about) or lists in --secondary are WARN, not HALT.
  P3 SHALLOW CRAWL    the crawl did not reach every screen the build declares.     HALT
                      A gate that did not look must never read as clean.
  P4 DEAD TAPS        a control that changed nothing 3 times running.               WARN

Usage:
  python3 studio-senses/fingers-play.py reports/senses/<build> [--secondary sc-about,sc-flip-seat]
  python3 studio-senses/fingers-play.py --self-test
"""
import json, os, sys

def judge(m, secondary=()):
    halts, warns = [], []
    states = {s['n']: s for s in m['states']}
    steps = [s for s in m['steps'] if 'label' in s and 'to' in s]
    # P1: repeated verbs
    runs, prev = {}, None
    for s in steps:
        runs[s['label']] = runs.get(s['label'], 0) + 1 if prev == s['label'] else max(runs.get(s['label'], 0), 1)
        prev = s['label']
    verbs = {k for k, v in runs.items() if v >= 2}
    # A verb tap AFTER the win does not count: once an exit to another screen (Next) is
    # live in the state, the player's job there is done (2026-10-13, Flok v29: the Ears
    # one-shot mute test pressed Release past the target and the crawl kept tapping).
    exits = {s['label'] for s in steps
             if states.get(s['from'], {}).get('screen') != states.get(s['to'], {}).get('screen')}
    def post_win(st):
        return any(c.get('name') in exits and not c.get('chrome') for c in states.get(st['from'], {}).get('controls', []))
    # Founder 2026-10-14 (Flok v33): "the lesson brief is at top and scrollable to the feed".
    # The screen may open at its brief, so ONE scroll to reach the verb is allowed: the first
    # tap of each run. Any LATER tap in the run that needed a scroll means the page moved
    # under the thumb, and that still HALTs.
    first = set(); prev_l = None
    for i, s in enumerate(steps):
        if s['label'] != prev_l: first.add(i)
        prev_l = s['label']
    for v in sorted(verbs):
        if any(s['label'] == v and s.get('needs_scroll') and not post_win(s) and i not in first
               for i, s in enumerate(steps)):
            halts.append(f"P1 verb in view: core verb '{v}' needed a scroll again after the first tap")
    # P2: progression controls, first pass only
    # the screen you load on is already seen; returning to it is not a first pass
    seen = {m['states'][0].get('screen')} if m['states'] else set()
    secondary = set(secondary) | set(m.get('screens_secondary') or [])
    for s in steps:
        a, b = states.get(s['from'], {}).get('screen'), states.get(s['to'], {}).get('screen')
        if a and b and a != b and b not in seen:
            seen.add(b)
            if s.get('needs_scroll'):
                (warns if b in secondary or a in secondary else halts).append(
                    f"P2 path in view: '{s['label']}' ({a} -> {b}) needed a scroll")
    # P3
    tot = m.get('screens_total') or []
    got = set(m.get('screens_seen') or [])
    miss = [x for x in tot if x not in got]
    if not tot: halts.append("P3 shallow: the bundle predates crawl v2 (no screen census); re-crawl")
    elif miss: halts.append(f"P3 shallow: never reached {', '.join(miss)}")
    # P4
    run, last = 0, None
    for s in m['steps']:
        if s.get('label') == last and not s.get('text_changed', True): run += 1
        else: run = 1 if not s.get('text_changed', True) else 0
        last = s.get('label')
        if run == 3: warns.append(f"P4 dead taps: '{last}' changed nothing 3 times running")
    return halts, warns

def report(bundle, secondary):
    m = json.load(open(os.path.join(bundle, 'manifest.json')))
    h, w = judge(m, secondary)
    print(f"STUDIO FINGERS · PLAY  {m['build']}  md5 {m['md5']}  ({len(m['steps'])} taps, {len(m['states'])} states)")
    for x in h: print("HALT ", x)
    for x in w: print("WARN ", x)
    print("VERDICT", "HALT" if h else "PASS")
    return 1 if h else 0

def self_test():
    st = lambda n, scr: {"n": n, "screen": scr}
    base = {"build": "canary", "md5": "-", "screens_total": ["sc-a", "sc-b"], "screens_seen": ["sc-a", "sc-b"],
            "states": [st(0, "sc-a"), st(1, "sc-a"), st(2, "sc-b")]}
    good = dict(base, steps=[{"label": "Boost", "from": 0, "to": 1, "text_changed": True},
                             {"label": "Boost", "from": 1, "to": 1, "text_changed": True},
                             {"label": "Next", "from": 1, "to": 2, "text_changed": True}])
    verb = dict(base, steps=[dict(s, needs_scroll=(s['label'] == 'Boost')) for s in good['steps']])
    nxt = dict(base, steps=[dict(s, needs_scroll=(s['label'] == 'Next')) for s in good['steps']])
    shallow = dict(good, screens_seen=["sc-a"])
    st2 = [st(0, "sc-a"), dict(st(1, "sc-a"), controls=[{"name": "Next"}]), st(2, "sc-b")]
    after = dict(base, states=st2, steps=[{"label": "Boost", "from": 0, "to": 1, "text_changed": True},
                                          {"label": "Boost", "from": 1, "to": 1, "text_changed": True, "needs_scroll": True},
                                          {"label": "Next", "from": 1, "to": 2, "text_changed": True}])
    once = dict(base, steps=[dict(good['steps'][0], needs_scroll=True)] + good['steps'][1:])
    cases = [("clean play", good, False), ("verb below fold (Flok v25)", verb, True),
             ("win button below fold (Flok v27)", nxt, True), ("shallow crawl (crawl v1)", shallow, True),
             ("verb tapped after the win, off screen", after, False),
             ("one scroll to the verb, then it stays (Flok v33 brief-first)", once, False)]
    ok = True
    for name, m, want in cases:
        got = bool(judge(m)[0]); ok &= got == want
        print(f"  {'ok ' if got == want else 'BAD'} {name}: {'HALT' if got else 'PASS'}")
    print("SELF-TEST", "PASSED" if ok else "FAILED"); return 0 if ok else 1

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(2)
    if a[0] == '--self-test': sys.exit(self_test())
    sec = a[a.index('--secondary') + 1].split(',') if '--secondary' in a else []
    sys.exit(report(a[0], sec))
