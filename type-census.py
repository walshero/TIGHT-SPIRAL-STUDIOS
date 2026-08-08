#!/usr/bin/env python3
"""
TYPE-CENSUS - the studio's type floor, measured on every rendered text node.

WHY THIS EXISTS
---------------
studio-type-contrast-standard.md v1.0 says: body 20px minimum, 18px absolute,
"Nothing below 18px ships. Ever."

On 2026-08-08 that claim was measured against ten live surfaces for the first
time. Result: body text ran 14.4px to 19px, chrome ran 10px to 13px, and the
share of visible text nodes rendering under 18px was 43% to 96%. On the front
door, 243 of 289. The comfort control's own panel labelled itself at 10.5px.

The floor had never been met anywhere, and nobody knew, because the only
instrument pointed at it - Studio Eyes E1 - measured ONE number, the body base,
as a SOFT warning. 84 to 96 percent of what actually rendered was never looked
at. Six documents asserted a floor and no gate counted.

That is the failure mode the project instructions name outright: IF A RULE
CAN'T BE A CHECK, IT'S A WISH. This is the check. It does not argue about what
the number should be; it counts what the number IS, on every node a reader can
actually see, and refuses to let that count rise.

WHAT IT MEASURES
----------------
Renders the file in headless Chromium at 390x844 (the founder's phone) and walks
every leaf element carrying visible text. For each, the RENDERED font-size, not
the declared one - a rem value inside a scaled ancestor is a different number by
the time it reaches an eye, and the declared value is the one that lies.

Counted as a violation: rendered size < 18px (FLOOR_ABS).
Reported separately, never blocking: the body-text size, for the open founder
question about whether the separate 20px body line survives at all.

Deliberately NOT counted:
  - nodes with no layout box, display:none, visibility:hidden, opacity < 0.3
  - nodes whose text is under 2 characters (icon glyphs, punctuation spans)
  - <code>/<kbd>/<samp> are counted like everything else. Monospace reads
    smaller at equal size, so exempting it would be exempting the case that
    hurts most.

WHY A RATCHET AND NOT A FLAT GATE
---------------------------------
Flat, this HALTs essentially the whole corpus on day one - measured, not
guessed. A tick that is red on every push is a tick everyone learns to scroll
past, and that is precisely how floor.yml lost its teeth in July. So today's
debt is CARRIED in type-baseline.json and only NEW debt blocks. The baseline
may only shrink. Fix a surface, it leaves forever.

The baseline stores a COUNT per surface, not a list of nodes. A count is stable
across copy edits; a node list churns on every prose change and would produce a
baseline nobody can read and everybody re-seeds.

Usage:
  type-census.py --init [--repo=NAME] <file.html> [...]   seed/refresh the baseline
  type-census.py --ratchet [--repo=NAME] <file.html> [...] block NEW debt
  type-census.py <file.html> [...]                        report only, never blocks

Exit 0 = clear or debt-carried · 1 = new debt · 2 = harness error
"""
import sys, os, json

FLOOR_ABS = 18.0          # studio-type-contrast-standard.md v1.0, absolute floor
VIEWPORT  = {"width": 390, "height": 844}   # the founder's phone, not a desktop guess

BASELINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'type-baseline.json')

WALK = """() => {
  const out = {nodes: 0, under: 0, worst: null, sizes: {}, offenders: []};
  let bodyPx = null, bodyArea = 0;
  const els = document.querySelectorAll('*');
  for (const el of els) {
    if (el.childElementCount) continue;              // leaves only; a parent double-counts
    const t = (el.textContent || '').trim();
    if (t.length < 2) continue;                       // icon glyphs, stray punctuation
    const r = el.getBoundingClientRect();
    if (!r.width || !r.height) continue;              // no layout box = not on screen
    const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none') continue;
    if (parseFloat(cs.opacity) < 0.3) continue;
    const px = Math.round(parseFloat(cs.fontSize) * 10) / 10;
    out.nodes++;
    out.sizes[px] = (out.sizes[px] || 0) + 1;
    if (px < 18) {
      out.under++;
      if (out.offenders.length < 12) {
        out.offenders.push({px, sel: String(el.className || el.tagName).slice(0, 34),
                            text: t.slice(0, 34)});
      }
      if (out.worst === null || px < out.worst) out.worst = px;
    }
    // body text = the largest block of running prose, same rule the review used
    if (['P','LI','DD','BLOCKQUOTE'].includes(el.tagName) && t.length >= 60) {
      const a = r.width * r.height;
      if (a > bodyArea) { bodyArea = a; bodyPx = px; }
    }
  }
  out.bodyPx = bodyPx;
  return out;
}"""


def census(pg, path):
    pg.goto("file://" + os.path.abspath(path))
    pg.wait_for_timeout(400)
    return pg.evaluate(WALK)


def load_baseline():
    if os.path.exists(BASELINE):
        with open(BASELINE) as f:
            return json.load(f).get('counts', {})
    return None


def key_for(path, repo):
    rel = os.path.relpath(os.path.abspath(path), os.getcwd())
    if rel.startswith(os.pardir):
        rel = os.path.basename(path)
    return repo + '/' + rel.replace(os.sep, '/')


def main(argv):
    do_init = '--init' in argv
    ratchet = '--ratchet' in argv
    repo    = next((a.split('=', 1)[1] for a in argv if a.startswith('--repo=')),
                   os.path.basename(os.getcwd()))
    files   = [a for a in argv if not a.startswith('--')]
    if not files:
        print(__doc__.strip().splitlines()[-6]); return 2

    base = load_baseline()
    if ratchet and not do_init and base is None:
        print("HALT - --ratchet asked for but type-baseline.json is missing.\n"
              "       A gate that cannot find its baseline does not pass; it stops.")
        return 2

    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print("type-census: playwright unavailable:", e); return 2

    frozen = dict(base or {}) if do_init else {}
    halted = carried = clean = 0

    print("=" * 74)
    print("TYPE CENSUS  ·  floor %.0fpx  ·  viewport %dx%d  ·  %s"
          % (FLOOR_ABS, VIEWPORT["width"], VIEWPORT["height"],
             "RATCHET" if (ratchet and not do_init) else ("INIT" if do_init else "REPORT")))
    print("=" * 74)

    with sync_playwright() as pw:
        try:
            br = pw.chromium.launch()
        except Exception:
            br = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        pg = br.new_context(viewport=VIEWPORT).new_page()

        for path in files:
            name = path.split('/')[-1]
            try:
                r = census(pg, path)
            except Exception as e:
                print("  ERROR %s: %s" % (name, str(e)[:70])); halted += 1; continue

            k = key_for(path, repo)
            n, tot = r['under'], r['nodes']
            body = r['bodyPx']
            bodytxt = ("body %.1fpx" % body) if body else "no body block"

            if do_init:
                frozen[k] = n
                print("  seed  %-42s %3d of %-4d under %.0fpx  (%s)"
                      % (name, n, tot, FLOOR_ABS, bodytxt))
                continue

            was = (base or {}).get(k)
            if n == 0:
                clean += 1
                print("  PASS  %-42s every visible node >= %.0fpx  (%s)"
                      % (name, FLOOR_ABS, bodytxt))
            elif ratchet and was is not None and n <= was:
                carried += 1
                print("  debt  %-42s %3d of %-4d under %.0fpx  (baseline %d, %s)"
                      % (name, n, tot, FLOOR_ABS, was, bodytxt))
            elif ratchet:
                halted += 1
                shown = "baseline %d" % was if was is not None else "NOT IN BASELINE"
                print("  HALT  %-42s %3d of %-4d under %.0fpx  (%s)"
                      % (name, n, tot, FLOOR_ABS, shown))
                for o in r['offenders'][:6]:
                    print("          %5.1fpx  %-32s %s" % (o['px'], o['sel'], o['text']))
            else:
                print("  ----  %-42s %3d of %-4d under %.0fpx  (%s)"
                      % (name, n, tot, FLOOR_ABS, bodytxt))
                for o in r['offenders'][:6]:
                    print("          %5.1fpx  %-32s %s" % (o['px'], o['sel'], o['text']))
        br.close()

    if do_init:
        with open(BASELINE, 'w') as f:
            json.dump({
                'created': '2026-08-08',
                'floor_px': FLOOR_ABS,
                'viewport': VIEWPORT,
                'why': ('Type-floor debt frozen the day the floor was first measured. '
                        'studio-type-contrast-standard.md v1.0 has asserted an 18px '
                        'absolute since 2026-07-26; nothing ever counted. Carried, not '
                        'forgiven. Any surface whose count RISES blocks.'),
                'rule': 'A count may fall or hold, never rise. Reach zero and the surface leaves.',
                'unit': 'visible text nodes rendering below the floor, per surface',
                'counts': dict(sorted(frozen.items())),
            }, f, indent=1)
            f.write('\n')
        total = sum(frozen.values())
        print("\nBASELINE WRITTEN - %d surface(s), %d carried node(s) under the floor."
              % (len(frozen), total))
        print("These do not block. Any RISE does. The ratchet turns one way.")
        return 0

    print("-" * 74)
    print("%d clean · %d debt-carried · %d HALT" % (clean, carried, halted))
    return 1 if halted else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
