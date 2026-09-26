#!/usr/bin/env python3
"""
STUDIO SENSES · THE GRADER                                Tight Spiral Productions
-----------------------------------------------------------------------------
Scores every seat's predictions against what first human players actually did in
archive/playtest-room.html (shelved 2026-09-26). This is what makes a seat accountable instead of plausible.

  outcome     each prediction x each session: TRUE / FALSE / N/A
              N/A when the session is the wrong cohort (a screen_reader prediction
              on a player who answered "looking") or the answer was skipped.
  STALE       a session recorded against different build bytes (sha256 mismatch)
              is excluded and counted, never graded. A verdict on old bytes is not
              a verdict on this build.
  UNSTAMPED   a session with no sha256 (opened as a file) is graded but flagged.
  Brier       per seat, mean of (p - outcome)^2. 0 is perfect; 0.25 is a coin flip.
              A seat that files confident nonsense scores worse than one that says
              "I don't know" (p = 0.5). Confidence is priced.
  SILENT      a seat with zero gradeable outcomes, printed as SILENT, never as agreeing.

Target syntax (SEATS.md): #id  .class  tag  tag.class  name:words  text:words

Usage:
  python3 studio-senses/grade.py <predictions.json> <session.json> [session2.json ...]
  python3 studio-senses/grade.py --self-test
Writes a scorecard to stdout. Exit 0 (reporter).
"""
import sys, json, re, operator

OPS = {'==': operator.eq, '!=': operator.ne, '<': operator.lt, '<=': operator.le,
       '>': operator.gt, '>=': operator.ge}


def norm(s):
    return re.sub(r'\s+', ' ', (s or '').lower()).strip()


def matches(target, tap):
    if not target:
        return False
    if target.startswith('name:'):
        return norm(target[5:]) in norm(tap.get('name'))
    m = re.fullmatch(r'([a-z0-9]+)?(#[\w-]+)?(\.[\w-]+)?', target.strip(), re.I)
    if not m or not any(m.groups()):
        return False
    tag, idd, cls = m.groups()
    for node in tap.get('chain', []):
        t = node.split('#')[0].split('.')[0]
        ids = re.findall(r'#([\w-]+)', node); classes = re.findall(r'\.([\w-]+)', node)
        if tag and t != tag.lower(): continue
        if idd and idd[1:] not in ids: continue
        if cls and cls[1:] not in classes: continue
        return True
    return False


def observe(pred, s):
    """Return the observed value for this prediction in this session, or None."""
    meas, tgt = pred['measure'], pred.get('target') or ''
    taps = s.get('taps', [])
    if meas == 'tapped':
        return any(matches(tgt, t) for t in taps)
    if meas == 'taps_before':
        for i, t in enumerate(taps):
            if matches(tgt, t): return i
        return None                      # never tapped: "taps before" is undefined, not infinite
    if meas == 'time_to_tap':
        for t in taps:
            if matches(tgt, t): return t['t']
        return None
    if meas == 'saw':
        w = norm(tgt[5:] if tgt.startswith('text:') else tgt)
        return any(w in norm(x) for x in s.get('seen', []))
    if meas == 'dead_taps':
        return sum(1 for t in taps if t.get('dead'))
    if meas == 'sound_off_at_end':
        p = (s.get('sound') or {}).get('end_pressed')
        return None if p is None else (p == 'false')
    if meas == 'session_ms':
        return s.get('session_ms')
    if meas.startswith('answer:'):
        return (s.get('answers') or {}).get(meas.split(':', 1)[1])
    return None


def cohort_ok(pred, s):
    if pred.get('cohort', 'any') != 'screen_reader':
        return True
    return (s.get('answers') or {}).get('played_by') in ('a screen reader', 'both')


def outcome(pred, s):
    if not cohort_ok(pred, s):
        return None
    v = observe(pred, s)
    if v is None:
        return None
    want, op = pred.get('value'), OPS.get(pred.get('op', '=='), operator.eq)
    if isinstance(want, str) and isinstance(v, str):
        return op(norm(v), norm(want))
    try:
        return bool(op(v, want))
    except TypeError:
        return None


def grade(P, sessions):
    live, stale, unstamped = [], [], 0
    for s in sessions:
        if s.get('sha256') and P.get('sha256') and s['sha256'] != P['sha256']:
            stale.append(s.get('session_id')); continue
        if not s.get('sha256'): unstamped += 1
        live.append(s)
    card = {"build": P['build'], "sessions": len(sessions), "graded": len(live), "stale": stale,
            "unstamped": unstamped, "seats": []}
    for seat in P['seats']:
        rows, sq = [], []
        for pred in seat['predictions']:
            outs = [outcome(pred, s) for s in live]
            got = [o for o in outs if o is not None]
            rate = (sum(got) / len(got)) if got else None
            for o in got: sq.append((pred['p'] - (1.0 if o else 0.0)) ** 2)
            rows.append({"id": pred.get('id'), "claim": pred.get('claim', '')[:90], "p": pred['p'],
                         "n": len(got), "came_true": rate})
        card['seats'].append({"seat": seat['seat'], "brier": round(sum(sq) / len(sq), 3) if sq else None,
                              "graded_outcomes": len(sq), "rows": rows,
                              "verdict": "SILENT" if not sq else ("FLAG re-ground" if len(sq) >= 10 and sum(sq) / len(sq) > 0.25 else "OK")})
    return card


def render(c):
    L = [f"STUDIO SENSES · SEAT SCORECARD  {c['build']}",
         f"sessions {c['sessions']} · graded {c['graded']} · stale {len(c['stale'])} · unstamped {c['unstamped']}", ""]
    for s in sorted(c['seats'], key=lambda x: (x['brier'] is None, x['brier'] or 0)):
        b = 'n/a' if s['brier'] is None else f"{s['brier']:.3f}"
        L.append(f"{s['seat']:<16} Brier {b:>6}  outcomes {s['graded_outcomes']:>3}  {s['verdict']}")
        for r in s['rows']:
            ct = 'n/a' if r['came_true'] is None else f"{r['came_true']:.0%}"
            L.append(f"   {r['id']:<5} p {r['p']:.2f}  came true {ct:>5} of {r['n']}  {r['claim']}")
    return "\n".join(L)


def self_test():
    P = {"build": "t", "sha256": "A", "seats": [
        {"seat": "Right", "predictions": [{"id": "R1", "measure": "tapped", "target": "name:catch", "op": "==", "value": True, "p": 0.9},
                                          {"id": "R2", "measure": "dead_taps", "op": "<=", "value": 1, "p": 0.8}]},
        {"seat": "Wrong", "predictions": [{"id": "W1", "measure": "tapped", "target": "#never", "op": "==", "value": True, "p": 0.95}]},
        {"seat": "Ear", "predictions": [{"id": "E1", "measure": "answer:knew_next", "op": "<=", "value": 2, "p": 0.7, "cohort": "screen_reader"}]}]}
    s1 = {"session_id": "a", "sha256": "A", "taps": [{"name": "Catch line", "chain": ["button.c-catch"], "dead": False}],
          "answers": {"played_by": "looking", "knew_next": 4}}
    s2 = {"session_id": "b", "sha256": "OLD", "taps": [], "answers": {}}
    c = grade(P, [s1, s2])
    seats = {s['seat']: s for s in c['seats']}
    checks = [
        ("a right, confident seat scores near 0", seats['Right']['brier'] is not None and seats['Right']['brier'] < 0.05),
        ("a wrong, confident seat scores near 1", seats['Wrong']['brier'] is not None and seats['Wrong']['brier'] > 0.8),
        ("a screen_reader prediction on a looking player is not graded (SILENT)", seats['Ear']['verdict'] == 'SILENT'),
        ("a session on other bytes is STALE, not graded", c['stale'] == ['b'] and c['graded'] == 1),
        ("class selector matches the tap chain", matches('.c-catch', s1['taps'][0])),
        ("tag.class selector matches", matches('button.c-catch', s1['taps'][0])),
        ("wrong tag does not match", not matches('a.c-catch', s1['taps'][0])),
    ]
    bad = 0
    for name, ok in checks:
        print(("ok    " if ok else "FAIL  ") + name); bad += not ok
    print(f"self-test: {len(checks) - bad} of {len(checks)}")
    return 1 if bad else 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    if sys.argv[1] == '--self-test':
        sys.exit(self_test())
    P = json.load(open(sys.argv[1]))
    sessions = [json.load(open(f)) for f in sys.argv[2:]]
    print(render(grade(P, sessions)))
