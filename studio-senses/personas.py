#!/usr/bin/env python3
"""
STUDIO SENSES · THE PAIRED PERSONAS                       Tight Spiral Productions
-----------------------------------------------------------------------------
Splits one evidence bundle into two transcripts that must NOT see each other:

  sighted.md   screenshots, headings, visible text, controls in view.
               Read by: the sighted persona, Hitchcock (Eyes Layer 2), Fingers.
  ear.md       NO PIXELS. The accessibility tree, live announcements, a plain
               description of every sound and vibration, and the cold Tab walk.
               Read by: the ear persona (plays by ear and screen reader), Murch
               (Ears Layer 2).

Horvath reads both, because the cognitive work asked of a player does not change
with the channel it arrives on, and a gap between the two IS his finding.

The split is the point. A seat agent handed screenshots cannot report what a
low-vision player misses; it will fill the gap from the picture without knowing it
did. The ear persona's transcript is built so that the picture is not there to lean on.

Also writes fingers-states.json: tap-target geometry at EVERY state, not first paint
(studio-eyes/studio-fingers.py is canon for first paint and owns the floors; this
reads its constants rather than restating them).

Usage:  python3 studio-senses/personas.py <bundle-dir>
"""
import sys, os, json, re, importlib.util
from collections import Counter


def fingers_consts():
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fp = os.path.join(here, 'studio-eyes', 'studio-fingers.py')
    src = open(fp).read() if os.path.exists(fp) else ''
    get = lambda k, d: float(re.search(rf'^{k}\s*=\s*([0-9.]+)', src, re.M).group(1)) if re.search(rf'^{k}\s*=', src, re.M) else d
    return {"TAP_FLOOR": get('TAP_FLOOR', 44), "REACH_ARC": get('REACH_ARC', 0.60),
            "source": "studio-eyes/studio-fingers.py" if src else "DEFAULTS (fingers canon not found)"}


def describe_sounds(s):
    n = len(s.get('oneshot_sounds', []))
    bits = []
    if n: bits.append(f"{n} short sound(s)")
    if s.get('loops_started'): bits.append(f"{s['loops_started']} looping sound(s) begin")
    if s.get('vibrate'): bits.append("the phone vibrates")
    return ", ".join(bits) or "no sound"


def build(bundle):
    m = json.load(open(os.path.join(bundle, 'manifest.json')))
    ears = {}
    ep = os.path.join(bundle, 'ears.json')
    if os.path.exists(ep):
        ears = json.load(open(ep))
    stamp = f"build {m['build']} · md5 {m['md5']} · crawled {m['crawled']} · viewport {m['viewport']['width']}x{m['viewport']['height']}"

    # ---------- sighted ----------
    S = [f"# SIGHTED TRANSCRIPT — {m['build']}", "", stamp, "",
         "You can see. You play by looking. Each state below has a screenshot path; open it.", ""]
    for st in m['states']:
        inview = [c['name'] for c in st['controls'] if c['inView']][:14]
        S += [f"## State {st['n']}  (reached by: {st['reached_by']})", f"screenshot: {st['png']}",
              f"headings: {st['headings']}", f"controls in view: {inview}",
              "visible text (first 600 chars):", "> " + st['text'][:600].replace('\n', ' / '), ""]
    S += ["## Steps (what was tapped, where it led)", ""]
    for s in m['steps']:
        if 'label' in s and 'to' in s:
            S.append(f"- step {s['n']}: tap \"{s['label']}\" at y={s['box'][1]} -> state {s['to']}"
                     + (" (new)" if s['new_state'] else "") + ("" if s['text_changed'] else " — screen text did not change"))
    # ---------- ear ----------
    E = [f"# EAR TRANSCRIPT — {m['build']}", "", stamp, "",
         "You cannot see the screen. You play with a screen reader and your ears.",
         "You get the accessibility tree (what a screen reader would read), what was announced aloud,",
         "and a plain description of every sound. There are no pictures in this transcript on purpose.", "",
         "## Cold keyboard walk from load (Tab, Tab, Tab...)", ""]
    walk = [t['name'] if t else '(focus on page body)' for t in m.get('tab_walk', [])]
    cycle = None
    for L in range(1, 12):
        if len(walk) >= 2 * L and walk[:L] == walk[L:2 * L]:
            cycle = L; break
    E.append("Tab stops: " + " -> ".join(walk[:16]) + (" ..." if len(walk) > 16 else ""))
    if cycle:
        E.append(f"The walk CYCLES every {cycle} stops from a cold load: only these are reachable by keyboard before any tap.")
    E.append("")
    for st in m['states']:
        aria = open(os.path.join(bundle, st['aria'])).read()
        E += [f"## State {st['n']}  (reached by: {st['reached_by']})", "```", aria[:2200], "```", ""]
    E += ["## Steps: what you pressed, what you heard", ""]
    for s in m['steps']:
        if 'label' in s and 'to' in s:
            said = " | ".join(s.get('live', [])) or "nothing announced"
            E.append(f"- step {s['n']}: pressed \"{s['label']}\" -> state {s['to']}. Heard: {describe_sounds(s)}. Announced: {said}")
    if ears:
        E += ["", "## Studio Ears Layer 1 verdict on this build", f"VERDICT {ears.get('verdict')}"]
        E += ["- HALT " + h for h in ears.get('halt', [])] + ["- WARN " + w for w in ears.get('warn', [])]
    # ---------- fingers, every state ----------
    k = fingers_consts()
    H = m['viewport']['height']
    fs = []
    for st in m['states']:
        small = [c for c in st['controls'] if c['inView'] and min(c.get('hw', c['w']), c.get('hh', c['h'])) < k['TAP_FLOOR']]
        high = [c for c in st['controls'] if c['inView'] and (c['y'] + c['h'] / 2) < H * (1 - k['REACH_ARC'])]
        fs.append({"state": st['n'], "controls_in_view": sum(1 for c in st['controls'] if c['inView']),
                   "under_tap_floor": [(c['name'][:30], c.get('hw', c['w']), c.get('hh', c['h'])) for c in small],  # hit area, pseudo-elements included
                   "above_thumb_arc": [(c['name'][:30], c['y']) for c in high]})
    taps_to = {}
    for s in m['steps']:
        if 'label' in s:
            taps_to.setdefault(s['label'][:40], s['n'] + 1)
    fingers = {"stamp": stamp, "floors_from": k, "per_state": fs, "taps_to_first_press_of": taps_to}
    open(os.path.join(bundle, 'sighted.md'), 'w').write("\n".join(S))
    open(os.path.join(bundle, 'ear.md'), 'w').write("\n".join(E))
    json.dump(fingers, open(os.path.join(bundle, 'fingers-states.json'), 'w'), indent=1)
    return m, len(S), len(E), fs


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    m, s, e, fs = build(sys.argv[1])
    small = sum(len(x['under_tap_floor']) for x in fs)
    print(f"PERSONAS  {m['build']}  md5 {m['md5']}")
    print(f"  sighted.md {s} lines · ear.md {e} lines · fingers-states.json: {small} under-floor targets across {len(fs)} states")
