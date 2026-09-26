#!/usr/bin/env python3
"""
STUDIO EARS · LAYER 1, THE ARITHMETIC FLOOR              Tight Spiral Productions
-----------------------------------------------------------------------------
Seated 2026-09-26 (founder: "now I want studio ears"). Same two-layer shape as
Studio Eyes (studio-eyes-two-layers.md): this file is Layer 1 only, things true or
false by measurement. Layer 2, whether the sound is RIGHT for the scene, is a seat
(studio-senses/SEATS.md, Murch) and never leaks in here.

It reads the evidence bundle from senses-crawl.py. It does not play the game.

Every number declares where it came from:
  [LAW]      the studio OS
  [CITED]    a published standard
  [PROXY]    a measurement standing in for a standard it cannot compute exactly

THE FLOORS
  E1 GESTURE-FIRST   audible output or a started source before the first trusted   HALT
                     gesture. [LAW] OS §2, locked 2026-06-27: the first tap is the
                     user gesture that unlocks audio, "permission-clean and
                     ambush-free."
  E2 MUTE WORKS      a sound control exists, pressing it drops the speaker below    HALT
                     -70 dBFS, pressing again restores it. [CITED] WCAG 2.2 SC 1.4.2
                     Audio Control. A mute is only a mute if the level drops.
  E3 MUTE REACHABLE  the sound control is in view in every state where audio ran.   HALT
                     [CITED] WCAG 1.4.2 requires the mechanism be available; a
                     control that scrolled away is not available to a thumb.
  E4 SOUND ALONE     a click produced a one-shot sound and nothing on screen and    WARN
                     nothing announced. Information carried by sound only.
                     [CITED] Xbox Accessibility Guideline 104 (captions/cues).
  E5 SIGHT ALONE     a click moved the game to a new state with no sound, no        WARN
                     vibration and no live announcement. For a low-vision player
                     this is a change they can miss. [CITED] XAG 103, important
                     cues in more than one channel. This is the founder's channel.
  E6 CLIP            speaker peak at or above 0 dBFS.                               HALT
  E7 LEVEL BAND      loudest short-term RMS outside -36..-12 dBFS.                  WARN
                     [PROXY] unweighted RMS, NOT K-weighted LUFS; ASWG-R001 sets
                     program loudness targets this approximates. A proxy never HALTs.
  SILENT             no audio at all. Printed SILENT, never PASS: "did not make a
                     sound" and "made sound correctly" must not share a word
                     (NO-LOOK-NO-TEETH-2026-09-12.md).

Exit 1 = a HALT. Exit 0 = PASS or SILENT. Exit 2 = no bundle (blind is never clean).

Usage:
  python3 studio-senses/ears.py <bundle-dir>
  python3 studio-senses/ears.py --self-test
"""
import sys, os, json, re

SOUND_CTL = re.compile(r'\b(sound|mute|unmute|audio|volume)\b', re.I)
MUTE_FLOOR_DBFS = -70
AUDIBLE_DBFS = -60
BAND = (-36.0, -12.0)


def judge(m):
    a = m.get('audio', {})
    steps = [s for s in m.get('steps', []) if 'label' in s and 'to' in s]
    out = {"build": m.get('build'), "md5": m.get('md5'), "halt": [], "warn": [], "facts": {}}
    any_audio = a.get('sources_total', 0) + a.get('media_total', 0) > 0
    if not any_audio:
        out['verdict'] = 'SILENT'
        out['facts']['note'] = 'No audio source and no media element started in the crawl.'
        return out

    # E1
    g = a.get('first_gesture_ms')
    # A source started into a SUSPENDED context makes no sound: that is a page preparing,
    # not an ambush. Only a running context or a measured level before the touch counts.
    pre = [e for e in a.get('pre_gesture_sources', []) if e.get('state', 'running') == 'running' or e.get('k') == 'media']
    pre_loud = [w for w in a.get('level_windows', []) if g is not None and w[0] < g and w[1] > AUDIBLE_DBFS]
    if pre or pre_loud:
        lvl = max((w[1] for w in pre_loud), default=None)
        out['halt'].append(f"E1 GESTURE-FIRST  {len(pre)} source(s) started before the first gesture"
                           + (f"; speaker reached {lvl} dBFS before any touch" if lvl is not None else "")
                           + ". [LAW] OS §2: the first tap unlocks audio, ambush-free.")

    # E2
    mt = m.get('mute_test') or {}
    if not mt.get('found'):
        out['halt'].append("E2 MUTE WORKS  no sound control found. [CITED] WCAG 2.2 SC 1.4.2.")
    else:
        off, back = mt.get('after_press_dbfs'), mt.get('after_second_press_dbfs')
        before = mt.get('before_dbfs')
        ok_off = off is not None and off <= MUTE_FLOOR_DBFS
        ok_back = back is not None and before is not None and back >= before - 6
        out['facts']['mute'] = mt
        if not ok_off:
            out['halt'].append(f"E2 MUTE WORKS  pressing \"{mt['control']}\" left the speaker at {off} dBFS "
                               f"(floor {MUTE_FLOOR_DBFS}). [CITED] WCAG 2.2 SC 1.4.2.")
        if not ok_back:
            out['warn'].append(f"E2 MUTE RESTORE  second press gave {back} dBFS against {before} before muting.")

    # E3
    states = m.get('states', [])
    audio_states = {s['to'] for s in steps if s.get('oneshot_sounds') or s.get('loops_started')} | {0}
    missing = [st['n'] for st in states if st['n'] in audio_states and
               not any(SOUND_CTL.search(c['name']) and c['inView'] for c in st['controls'])]
    if missing:
        out['halt'].append(f"E3 MUTE REACHABLE  sound control not in view in state(s) {missing}. [CITED] WCAG 1.4.2.")

    # E4 / E5
    alone = [s for s in steps if s.get('oneshot_sounds') and not s.get('text_changed')
             and not s.get('new_state') and not s.get('live')]
    for s in alone:
        out['warn'].append(f"E4 SOUND ALONE  step {s['n']} \"{s['label'][:40]}\": sound, no visible change, "
                           "no announcement. [CITED] XAG 104.")
    changes = [s for s in steps if s.get('new_state')]
    silent = [s for s in changes if not s.get('oneshot_sounds') and not s.get('vibrate') and not s.get('live')]
    chan = {"state_changes": len(changes),
            "with_sound": sum(1 for s in changes if s.get('oneshot_sounds')),
            "with_vibration": sum(1 for s in changes if s.get('vibrate')),
            "with_announcement": sum(1 for s in changes if s.get('live')),
            "sight_only": len(silent)}
    out['facts']['channels'] = chan
    if silent:
        out['warn'].append(f"E5 SIGHT ALONE  {len(silent)} of {len(changes)} state changes carry no sound, "
                           f"vibration or announcement: " + "; ".join(f"step {s['n']} \"{s['label'][:28]}\"" for s in silent[:6])
                           + (" ..." if len(silent) > 6 else "") + ". [CITED] XAG 103.")

    # E6 / E7
    pk, rms = a.get('peak_linear', 0), a.get('rms_max_dbfs')
    out['facts']['level'] = {"peak_linear": pk, "rms_max_dbfs": rms}
    if pk >= 0.99:
        out['halt'].append(f"E6 CLIP  speaker peak {pk} (0 dBFS is 1.0).")
    if rms is not None and not (BAND[0] <= rms <= BAND[1]):
        out['warn'].append(f"E7 LEVEL BAND  loudest short-term RMS {rms} dBFS, outside {BAND[0]}..{BAND[1]}. "
                           "[PROXY] unweighted RMS standing in for ASWG-R001 loudness.")
    out['verdict'] = 'HALT' if out['halt'] else 'PASS'
    return out


def card(r):
    lines = [f"STUDIO EARS · LAYER 1  {r['build']}  md5 {r['md5']}", f"VERDICT  {r['verdict']}"]
    for h in r['halt']: lines.append("  HALT  " + h)
    for w in r['warn']: lines.append("  WARN  " + w)
    for k, v in r['facts'].items(): lines.append(f"  fact  {k}: {v}")
    return "\n".join(lines)


def self_test():
    base = {"build": "canary", "md5": "x", "states": [{"n": 0, "controls": [{"name": "Sound on", "inView": True}]}],
            "mute_test": {"found": True, "control": "Sound on", "before_dbfs": -30, "after_press_dbfs": -90,
                          "after_second_press_dbfs": -30},
            "audio": {"sources_total": 3, "media_total": 0, "first_gesture_ms": 1000, "pre_gesture_sources": [],
                      "level_windows": [[500, -120, 0], [1500, -30, .2]], "peak_linear": .3, "rms_max_dbfs": -24},
            "steps": [{"n": 0, "label": "Start", "to": 0, "new_state": True, "oneshot_sounds": [{}], "text_changed": True}]}
    import copy
    cases = []
    cases.append(("clean canary PASSES", base, 'PASS', None))
    c = copy.deepcopy(base); c['audio'] = {"sources_total": 0, "media_total": 0}
    cases.append(("no audio reads SILENT, not PASS", c, 'SILENT', None))
    c = copy.deepcopy(base); c['audio']['level_windows'] = [[400, -40, .1]]; c['audio']['pre_gesture_sources'] = [{"k": "src"}]
    cases.append(("sound before a gesture HALTs", c, 'HALT', 'E1'))
    c = copy.deepcopy(base); c['audio']['pre_gesture_sources'] = [{"k": "src", "state": "suspended"}]
    cases.append(("a source prepared in a suspended context before a touch PASSES", c, 'PASS', None))
    c = copy.deepcopy(base); c['mute_test']['after_press_dbfs'] = -40
    cases.append(("a mute that does not drop the level HALTs", c, 'HALT', 'E2'))
    c = copy.deepcopy(base); c['states'][0]['controls'][0]['inView'] = False
    cases.append(("a mute scrolled out of view HALTs", c, 'HALT', 'E3'))
    c = copy.deepcopy(base); c['audio']['peak_linear'] = 1.0
    cases.append(("clipping HALTs", c, 'HALT', 'E6'))
    c = copy.deepcopy(base); c['steps'][0]['oneshot_sounds'] = []
    cases.append(("a silent state change WARNs (E5), never HALTs", c, 'PASS', 'E5'))
    c = copy.deepcopy(base); c['audio']['rms_max_dbfs'] = -5
    cases.append(("a proxy level outside band WARNs, never HALTs", c, 'PASS', 'E7'))
    bad = 0
    for name, m, want, code in cases:
        r = judge(m)
        ok = r['verdict'] == want and (code is None or any(x.startswith(code) for x in r['halt'] + r['warn']))
        print(("ok    " if ok else "FAIL  ") + name)
        bad += not ok
    print(f"self-test: {len(cases) - bad} of {len(cases)}")
    return 1 if bad else 0


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    if sys.argv[1] == '--self-test':
        sys.exit(self_test())
    fp = os.path.join(sys.argv[1], 'manifest.json')
    if not os.path.exists(fp):
        print(f"BLIND  no evidence bundle at {fp}. Run senses-crawl.py first. Blind is never clean.")
        sys.exit(2)
    r = judge(json.load(open(fp)))
    with open(os.path.join(sys.argv[1], 'ears.json'), 'w') as f:
        json.dump(r, f, indent=1)
    print(card(r))
    sys.exit(1 if r['verdict'] == 'HALT' else 0)


if __name__ == '__main__':
    main()
