#!/usr/bin/env python3
"""
ALEPH FLEET - the studio's agentic assessment harness.
Tight Spiral Productions.

WHAT THIS IS
------------
os-block-aleph-diagnose-repair.md defined the Aleph: point independent lenses at a
build, merge their findings, rank by agreement, repair in confidence order, and
harden any gate that missed something. It worked (old-problems-at-new-speed,
2026-07-26) and it ran again as an 11-aleph fleet on the iSLO suite (2026-08-03).

Both runs were done BY HAND. That is the thing this file fixes. Three specific
holes, each of which cost real work:

  1. AGREEMENT WAS JUDGEMENT. Three lenses describing one defect in three
     vocabularies cannot be compared by string match, so the merge was a person
     reading three lists. A person who is not in the next session. Now every aleph
     returns a key from aleph-taxonomy.json and agreement is a count.

  2. THE FEEDBACK TOOTH WAS A SENTENCE. "If a TSP gate missed something the other
     lenses caught, harden the gate" happened once, was written down once, and had
     nowhere to live. It kept happening anyway and kept being forgotten: comfort-gate
     missing fill-tokens-used-as-text (2026-08-03), studio-eyes-sweep not
     contrast-checking inside a viewBox (2026-08-07). Now a non-L1 lens naming a
     FLOOR key on a surface L1 passed is written to a blind-spot register, with a
     status, automatically.

  3. THERE WAS NO ITERATION. Findings landed in a dated markdown file and that was
     the end of them. Nothing knew whether a finding had been seen before, fixed, or
     had come back. Now every finding has a stable id and every run diffs against
     the ledger: NEW / REPEAT / FIXED / REGRESSED.

WHAT IT DOES NOT DO
-------------------
It does not judge. It does not run the alephs. It is the spine they hang findings
on: schema out, synthesis in. The alephs are the intelligence; this is the memory
and the arithmetic. Funes' rule - it forgets nothing and it re-measures every time.

USAGE
  aleph-fleet.py --schema                    the JSON every aleph must return
  aleph-fleet.py --brief L5                  the brief for one lens (hand to an aleph)
  aleph-fleet.py --lenses                    list the lenses
  aleph-fleet.py --synthesize <dir>          synthesize a run dir of *.json findings
  aleph-fleet.py --synthesize <dir> --commit update the ledger with this run
  aleph-fleet.py --selftest                  prove the teeth

EXIT  0 = ran · 1 = blockers survived synthesis · 2 = cannot run (never a silent pass)
"""
import sys, os, json, glob, hashlib, datetime

ROOT      = os.path.dirname(os.path.abspath(__file__))
TAXONOMY  = os.path.join(ROOT, 'aleph-taxonomy.json')
LEDGER    = os.path.join(ROOT, 'aleph-ledger.json')
BLINDSPOT = os.path.join(ROOT, 'aleph-blindspots.json')
LENSDIR   = os.path.join(ROOT, 'aleph-lenses')

LENSES = {
    'L1': ('TSP tools',        'the studio gates, run literally. Concrete and runnable.'),
    'L2': ('Play',             'does it PLAY - game heuristics, FTUE, game-feel.'),
    'L3': ('Media',            'does the message LAND - comprehension, disclosure, provenance.'),
    'L4': ('Aesthetic',        'does it READ as one made thing - composition, palette, voice.'),
    'L5': ('Learning science', 'does anyone LEARN - alignment, load, practice, feedback, transfer.'),
}

# A lens may only be BLIND to a floor key, never the reverse. L1 owns the floor;
# when another lens sees a floor defect L1 passed, the tool is the thing at fault.
FLOOR_OWNER = 'L1'


def die(msg, code=2):
    print('HALT - ' + msg, file=sys.stderr)
    sys.exit(code)


def load_taxonomy():
    try:
        return json.load(open(TAXONOMY, encoding='utf-8'))
    except Exception as e:
        die('aleph-taxonomy.json unreadable (%s). A synthesis with no vocabulary '
            'cannot compare lenses; it stops rather than guess.' % e)


def valid_keys(tax):
    out = {}
    for group, blk in tax['keys'].items():
        for k, desc in blk['items'].items():
            out[k] = (group, blk.get('owner'), desc)
    return out


def finding_id(surface, key, anchor):
    """Stable across runs so the ledger can say REPEAT rather than NEW.

    Deliberately NOT hashed over the prose: an aleph rewording the same defect must
    not mint a new id, or every run reads as all-new and iteration is impossible.
    anchor is the element/selector/line the finding is pinned to - normalise it or
    a reflow renumbers history."""
    anchor = (anchor or '').strip().lower()
    raw = '%s|%s|%s' % (surface.strip().lower(), key.strip().upper(), anchor)
    return hashlib.sha1(raw.encode('utf-8')).hexdigest()[:12]


SCHEMA = {
    "type": "object",
    "required": ["lens", "surface", "findings"],
    "properties": {
        "lens":    {"enum": sorted(LENSES.keys())},
        "surface": {"type": "string", "description": "file the aleph assessed, repo-relative"},
        "passed":  {"type": "array", "items": {"type": "string"},
                    "description": "taxonomy keys this lens explicitly CHECKED and found clean. "
                                   "Load-bearing: a key that is neither found nor passed reads as "
                                   "NOT LOOKED AT, and silence must never score as clean."},
        "findings": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["key", "severity", "anchor", "problem", "fix"],
                "properties": {
                    "key":       {"type": "string", "description": "EXACT key from aleph-taxonomy.json"},
                    "severity":  {"enum": ["blocker", "major", "minor"]},
                    "anchor":    {"type": "string", "description": "element, selector, or line it is pinned to"},
                    "problem":   {"type": "string", "description": "what is wrong, concretely. No generic advice."},
                    "fix":       {"type": "string", "description": "the specific change to make"},
                    "framework": {"type": "string", "description": "the published framework invoked, if any"},
                    "evidence":  {"type": "string", "description": "the measurement or quote that proves it"}
                }
            }
        }
    }
}


def cmd_schema():
    print(json.dumps(SCHEMA, indent=2))
    return 0


def cmd_lenses():
    tax = load_taxonomy()
    print('\n  ALEPH LENSES')
    print('  ' + '-' * 66)
    for lid in sorted(LENSES):
        name, what = LENSES[lid]
        owned = [g for g, b in tax['keys'].items() if b.get('owner') == lid]
        print('  %s  %-17s %s' % (lid, name, what))
        if owned:
            print('  %s  owns: %s' % (' ' * 2, ', '.join(sorted(owned))))
    print()
    return 0


def cmd_brief(lid):
    lid = lid.upper()
    if lid not in LENSES:
        die('unknown lens %s. Known: %s' % (lid, ', '.join(sorted(LENSES))))
    path = os.path.join(LENSDIR, lid + '.md')
    if not os.path.exists(path):
        die('brief missing: %s. A lens with no brief is a lens that re-derives itself '
            'every run, and two runs of a re-derived lens are not comparable.' % path)
    sys.stdout.write(open(path, encoding='utf-8').read())
    return 0


# ---------- synthesis ----------
def read_run(rundir):
    tax  = load_taxonomy()
    keys = valid_keys(tax)
    files = sorted(glob.glob(os.path.join(rundir, '*.json')))
    if not files:
        die('no aleph findings in %s. An empty run is not a clean run.' % rundir)
    reports, bad = [], []
    for f in files:
        try:
            d = json.load(open(f, encoding='utf-8'))
        except Exception as e:
            bad.append('%s: unparseable (%s)' % (os.path.basename(f), e)); continue
        if d.get('lens') not in LENSES:
            bad.append('%s: lens %r not one of %s' % (os.path.basename(f), d.get('lens'),
                                                      ', '.join(sorted(LENSES)))); continue
        if not d.get('surface'):
            bad.append('%s: no surface named' % os.path.basename(f)); continue
        for fd in d.get('findings', []):
            k = (fd.get('key') or '').upper()
            if k not in keys:
                bad.append('%s: key %r not in the taxonomy' % (os.path.basename(f), fd.get('key')))
        reports.append(d)
    return reports, bad, keys


def synthesize(rundir):
    reports, bad, keys = read_run(rundir)

    # cluster: (surface, key) -> the lenses that named it, and their findings
    clusters = {}
    checked  = {}          # (surface, key) -> set of lenses that LOOKED, found or not
    for r in reports:
        surf, lid = r['surface'], r['lens']
        for k in [x.upper() for x in r.get('passed', [])]:
            checked.setdefault((surf, k), set()).add(lid)
        for fd in r.get('findings', []):
            k = (fd.get('key') or '').upper()
            if k not in keys:
                continue
            c = clusters.setdefault((surf, k), {'lenses': {}, 'items': []})
            c['lenses'][lid] = True
            c['items'].append(dict(fd, lens=lid))
            checked.setdefault((surf, k), set()).add(lid)

    rows = []
    for (surf, k), c in clusters.items():
        lens_set = sorted(c['lenses'])
        sev = min((f.get('severity', 'minor') for f in c['items']),
                  key=lambda s: {'blocker': 0, 'major': 1, 'minor': 2}.get(s, 2))
        anchor = c['items'][0].get('anchor', '')
        group, owner, _ = keys[k]
        rows.append({
            'id': finding_id(surf, k, anchor),
            'surface': surf, 'key': k, 'group': group, 'severity': sev,
            'agreement': len(lens_set), 'lenses': lens_set, 'anchor': anchor,
            'items': c['items'],
            # the tooth: a floor defect that L1 did not name is a gate blind spot,
            # whether L1 explicitly passed it or never looked.
            'blindspot': (group == 'floor' and FLOOR_OWNER not in lens_set),
        })

    rank = {'blocker': 0, 'major': 1, 'minor': 2}
    rows.sort(key=lambda r: (-r['agreement'], rank.get(r['severity'], 2), r['surface'], r['key']))
    return rows, bad, checked


def stars(n):
    return '*' * min(n, 3) + ' ' * (3 - min(n, 3))


def load_json(path, default):
    if os.path.exists(path):
        try:
            return json.load(open(path, encoding='utf-8'))
        except Exception:
            return default
    return default


def cmd_synthesize(rundir, commit=False, stamp=None):
    rows, bad, checked = synthesize(rundir)
    ledger = load_json(LEDGER, {'created': stamp, 'runs': 0, 'findings': {}})
    known  = ledger.get('findings', {})
    seen_now = {r['id'] for r in rows}

    for r in rows:
        prev = known.get(r['id'])
        if prev is None:
            r['state'] = 'NEW'
        elif prev.get('state') == 'FIXED':
            r['state'] = 'REGRESSED'
        else:
            r['state'] = 'REPEAT'
            r['runs_open'] = prev.get('runs_open', 1) + 1

    # FIXED is scoped to what THIS RUN actually looked at. `checked` holds every
    # (surface, key) a lens opened, found or not -- the same load-bearing `passed`
    # discipline applied one level up. Without this scope a run stamps every OTHER
    # surface's open findings FIXED purely by absence, and the ledger reads as a
    # ratchet that moved while nothing was even opened.
    # Found 2026-09-01 by the flash-blockout run: it assessed one new file and
    # reported 30 the-tell.html defects "fixed". A surface nobody opened has no
    # news, and no news is never good news.
    fixed = [dict(v, id=i) for i, v in known.items()
             if i not in seen_now and v.get('state') != 'FIXED'
             and checked.get((v.get('surface'), v.get('key')))]

    print()
    print('=' * 74)
    print('  ALEPH FLEET - synthesis   run dir: %s' % rundir)
    print('=' * 74)
    if bad:
        print('\n  REJECTED INPUT (not counted, not forgiven):')
        for b in bad:
            print('     ' + b)
        print('     A malformed aleph is a lens that did not report. It is never a pass.')

    lenses_present = sorted({i['lens'] for r in rows for i in r['items']}) or ['(none)']
    print('\n  lenses reporting: %s' % ', '.join(lenses_present))
    print('  surfaces: %d   clustered defects: %d' %
          (len({r['surface'] for r in rows}), len(rows)))

    if rows:
        print('\n  RANKED BY AGREEMENT (agreement is the trust metric)')
        print('  ' + '-' * 70)
        for r in rows:
            flag = ' [BLIND SPOT]' if r['blindspot'] else ''
            print('  %s %-9s %-26s %-8s %s%s' %
                  (stars(r['agreement']), r['state'], r['key'], r['severity'],
                   r['surface'], flag))
            print('        lenses: %s   anchor: %s   id: %s'
                  % ('+'.join(r['lenses']), r['anchor'] or '(none)', r['id']))
            print('        %s' % r['items'][0].get('problem', '')[:150])
            print('        FIX: %s' % r['items'][0].get('fix', '')[:150])

    if fixed:
        print('\n  FIXED SINCE LAST RUN (%d) - the ratchet moved' % len(fixed))
        for f in fixed:
            print('     %-26s %s' % (f.get('key'), f.get('surface')))

    blind = [r for r in rows if r['blindspot']]
    if blind:
        print('\n  TOOL BLIND SPOTS (%d) - a lens saw a FLOOR defect the gates did not' % len(blind))
        print('  Repair the TOOL, not just the file. This is the ratchet applied to the')
        print('  diagnostics themselves: every escaped defect becomes a permanent check.')
        for r in blind:
            print('     %-26s %-34s named by %s' %
                  (r['key'], r['surface'], '+'.join(r['lenses'])))

    # unexamined: a key no lens either found or explicitly passed on a seen surface
    surfaces = sorted({r['surface'] for r in rows})
    if surfaces:
        floor_keys = [k for k, v in valid_keys(load_taxonomy()).items() if v[0] == 'floor']
        gaps = []
        for s in surfaces:
            for k in floor_keys:
                if not checked.get((s, k)):
                    gaps.append((s, k))
        if gaps:
            print('\n  NOT LOOKED AT (%d floor key/surface pairs) - silence is not a pass' % len(gaps))
            shown = {}
            for s, k in gaps:
                shown.setdefault(s, []).append(k)
            for s, ks in list(shown.items())[:6]:
                print('     %-34s %s' % (s, ', '.join(sorted(ks)[:6]) + (' ...' if len(ks) > 6 else '')))

    blockers = [r for r in rows if r['severity'] == 'blocker']
    print('\n' + '-' * 74)
    print('  RESULT: %d blocker(s), %d major, %d minor  ·  %d new, %d repeat, %d regressed, %d fixed'
          % (len(blockers),
             sum(1 for r in rows if r['severity'] == 'major'),
             sum(1 for r in rows if r['severity'] == 'minor'),
             sum(1 for r in rows if r['state'] == 'NEW'),
             sum(1 for r in rows if r['state'] == 'REPEAT'),
             sum(1 for r in rows if r['state'] == 'REGRESSED'),
             len(fixed)))

    if commit:
        for r in rows:
            known[r['id']] = {
                'surface': r['surface'], 'key': r['key'], 'severity': r['severity'],
                'anchor': r['anchor'], 'agreement': r['agreement'], 'lenses': r['lenses'],
                'state': 'OPEN', 'runs_open': r.get('runs_open', 1), 'last_seen': stamp,
            }
        for f in fixed:
            known[f['id']]['state'] = 'FIXED'
            known[f['id']]['fixed_on'] = stamp
        ledger.update({'findings': known, 'runs': ledger.get('runs', 0) + 1,
                       'last_run': stamp})
        json.dump(ledger, open(LEDGER, 'w', encoding='utf-8'), indent=1, sort_keys=True)
        reg = load_json(BLINDSPOT, {'created': stamp, 'why': (
            'Every time a non-tool lens catches a FLOOR defect the studio gates passed, '
            'the gate has a hole. Recorded here with a status so it cannot be forgotten '
            'between sessions. open -> hardened when the gate grows the tooth.'),
            'spots': {}})
        for r in blind:
            sid = '%s:%s' % (r['key'], r['surface'])
            ent = reg['spots'].get(sid, {'status': 'open', 'first_seen': stamp, 'times': 0})
            ent.update({'key': r['key'], 'surface': r['surface'],
                        'named_by': r['lenses'], 'last_seen': stamp,
                        'times': ent.get('times', 0) + 1})
            reg['spots'][sid] = ent
        json.dump(reg, open(BLINDSPOT, 'w', encoding='utf-8'), indent=1, sort_keys=True)
        print('  ledger updated: %s (%d findings tracked)' % (LEDGER, len(known)))
        if blind:
            print('  blind-spot register updated: %s' % BLINDSPOT)
    else:
        print('  DRY RUN - ledger untouched. Re-run with --commit to record this run.')
    print()
    return 1 if blockers else 0


def cmd_selftest():
    """Prove the three teeth: agreement counts, blind spots surface, ids are stable."""
    import tempfile, shutil
    d = tempfile.mkdtemp()
    try:
        # two lenses name the same defect -> agreement 2
        json.dump({'lens': 'L2', 'surface': 'x.html', 'passed': [],
                   'findings': [{'key': 'OPENING-WALL', 'severity': 'blocker',
                                 'anchor': '#gate', 'problem': 'p', 'fix': 'f'}]},
                  open(os.path.join(d, 'a.json'), 'w'))
        json.dump({'lens': 'L3', 'surface': 'x.html', 'passed': [],
                   'findings': [{'key': 'OPENING-WALL', 'severity': 'major',
                                 'anchor': '#gate', 'problem': 'p', 'fix': 'f'},
                                {'key': 'CONTRAST-FLOOR', 'severity': 'blocker',
                                 'anchor': '.cap', 'problem': 'p', 'fix': 'f'}]},
                  open(os.path.join(d, 'b.json'), 'w'))
        rows, bad, _ = synthesize(d)
        by = {r['key']: r for r in rows}
        ok_agree = by['OPENING-WALL']['agreement'] == 2
        ok_sev   = by['OPENING-WALL']['severity'] == 'blocker'   # worst wins
        ok_blind = by['CONTRAST-FLOOR']['blindspot'] is True     # floor key, no L1
        ok_nob   = by['OPENING-WALL']['blindspot'] is False      # play key, never a blind spot
        ok_id    = finding_id('x.html', 'OPENING-WALL', '#gate') == \
                   finding_id(' X.HTML ', 'opening-wall', ' #GATE ')
        # a bad key must be REJECTED, never silently dropped
        json.dump({'lens': 'L4', 'surface': 'x.html',
                   'findings': [{'key': 'NOT-A-REAL-KEY', 'severity': 'minor',
                                 'anchor': 'a', 'problem': 'p', 'fix': 'f'}]},
                  open(os.path.join(d, 'c.json'), 'w'))
        _, bad2, _ = synthesize(d)
        ok_reject = any('NOT-A-REAL-KEY' in b for b in bad2)
    finally:
        shutil.rmtree(d, ignore_errors=True)

    checks = [('agreement counts distinct lenses', ok_agree),
              ('worst severity wins the cluster', ok_sev),
              ('floor key without L1 is a blind spot', ok_blind),
              ('non-floor key is never a blind spot', ok_nob),
              ('finding ids are normalised and stable', ok_id),
              ('an off-taxonomy key is rejected, not dropped', ok_reject)]
    print('\n  ALEPH FLEET SELF-TEST')
    for name, ok in checks:
        print('   %s  %s' % ('ok  ' if ok else 'FAIL', name))
    bad_n = [n for n, o in checks if not o]
    if bad_n:
        print('\n  SELF-TEST FAILED - the harness is not biting. Refusing to certify.\n')
        return 3
    print('\n  teeth verified.\n')
    return 0


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    stamp = datetime.datetime.utcnow().strftime('%Y-%m-%d')
    if '--schema'   in argv: return cmd_schema()
    if '--lenses'   in argv: return cmd_lenses()
    if '--selftest' in argv: return cmd_selftest()
    if '--brief'    in argv:
        i = argv.index('--brief')
        if i + 1 >= len(argv): die('--brief needs a lens id (L1..L5)')
        return cmd_brief(argv[i + 1])
    if '--synthesize' in argv:
        i = argv.index('--synthesize')
        if i + 1 >= len(argv): die('--synthesize needs a run directory')
        return cmd_synthesize(argv[i + 1], commit='--commit' in argv, stamp=stamp)
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
