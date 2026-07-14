#!/usr/bin/env python3
"""
THE STRUCTURAL GATE — floors that were prose, made arithmetic.

WHY THIS EXISTS
---------------
2026-07-14. The founder opened Funny Boney's Factory and said "ugggh."

He was right. The game opened on a control panel: a brand mark, three lens buttons,
and two dropdowns ("View: Arcade" / "Motion: Full") — and BELOW that, finally, the
actual scene and the line "Make the cat laugh."

The studio retired that pattern on 2026-06-29 and wrote it into law:

    NO OPENING WALL — the first screen is the SCENE, never a preference gate.

The file had been shipping the retired pattern for SIX WEEKS. Studio Eyes waved it
through every single time — because Studio Eyes only knows ARITHMETIC. It can prove
a colour is unreadable. It has no idea whether a game opens on a joke or on a
settings panel.

The file's own CSS comments said "never a gate; always reachable" and "scene-first
opening." BOTH WERE TRUE AS INTENTIONS AND FALSE AS FACTS. A comment is not a check.

And the founder asked the right question: "I won't have to retell you asks and floors
from previous rounds? Enforcement at what level?"

    THE HONEST ANSWER: the floors live at three levels, and only one had teeth.

      ARITHMETIC  contrast, external hosts, emoji     -> the ratchet REFUSES. Real.
      STRUCTURAL  no opening wall, no dead buttons    -> NOTHING CHECKED THESE. Prose.
      JUDGMENT    is it fun? is the metaphor right?   -> never automatable. That is Matt.

This file moves the middle row into the top row. "If a rule cannot be a check, it is
a wish" — so stop wishing and write the check.

THE CALIBRATION PROBLEM (read this before changing anything)
------------------------------------------------------------
The first draft of this gate flagged 22 of 33 files. That was WRONG, and it was
wrong in the most dangerous way: it looked like a finding.

A COMFORT TOGGLE IS NOT A WALL. It is the corner control the law explicitly requires
("comfort is a live corner control"). the-tell.html and sandbags.html each show ONE
control before their first paragraph — a Comfort button. That is the law being OBEYED,
and an auditor that reports it as a violation is training the founder to ignore it.

    TICK 4: an auditor that cries wolf is worse than no auditor.

So the check distinguishes:
    LEGAL    comfort / theme / motion / text-size toggles, and the scene's own CTA
    A WALL   a cluster of MODE or PREFERENCE controls the player must get past first

The threshold is not "any control." It is "controls that ask the player to CONFIGURE
something before they have seen anything worth configuring."

USAGE
-----
    python3 structure-gate.py <file.html>     # one file
    python3 structure-gate.py .               # the corpus

EXIT
----
    0  clean
    1  HALT — an opening wall, or a dead control
"""

import sys, os, re, glob

# Controls that are ALWAYS legal before content. Comfort is a corner control, by law.
COMFORT = re.compile(
    r'comfort|theme|dark|light|warm|contrast|motion|reduce|text\s*size|font|'
    r'\bA\+|\bAa\b|sound|audio|mute|volume|zoom|still',
    re.I)

# Words that mean "you are being asked to CONFIGURE before you PLAY."
CONFIG = re.compile(
    r'\bview:|\bmode:|\blens\b|\bdifficulty\b|\blevel:|\bchoose your\b|'
    r'\bselect your\b|\bpick your\b|\bsettings\b|\bpreferences\b|\bplayer name\b',
    re.I)


def visible_body(src):
    m = re.search(r'<body[^>]*>([\s\S]*)</body>', src, re.I)
    b = m.group(1) if m else src
    return re.sub(r'<(script|style)[\s\S]*?</\1>', '', b, flags=re.I)


def opening_wall(src):
    """Does the player meet a CONFIGURATION PANEL before they meet the work?

    Legal: a comfort toggle. A theme switch. The scene's own call to action.
    Illegal: lens pickers, mode selectors, 'View: Arcade', 'choose your X' —
             anything that asks the player to configure a thing they have not seen.
    """
    body = visible_body(src)
    # SVG is content (a scene is often an SVG) — keep it, but don't read its innards
    flat = re.sub(r'<svg[\s\S]*?</svg>', '<SCENE>', body, flags=re.I)

    # first real content: a heading, a paragraph, or a scene
    cm = re.search(r'<h1\b|<h2\b|<p\b|<SCENE>', flat, re.I)
    if not cm:
        return None
    pre = flat[:cm.start()]

    findings = []
    for m in re.finditer(r'<(button|select)\b([^>]*)>([\s\S]{0,120}?)</\1>', pre, re.I):
        attrs = m.group(2)
        label = re.sub(r'<[^>]+>', ' ', m.group(3))
        label = ' '.join(label.split())[:40]
        aria  = re.search(r'aria-label="([^"]*)"', attrs)
        text  = label + ' ' + (aria.group(1) if aria else '') + ' ' + attrs

        if COMFORT.search(text) and not CONFIG.search(text):
            continue                      # a comfort toggle. Legal. Required, even.
        if CONFIG.search(text):
            findings.append(('CONFIG', label or '(unlabeled)'))
        else:
            findings.append(('CONTROL', label or '(unlabeled)'))

    # One stray control is a CTA or a skip-link. A CLUSTER is a panel.
    configs = [f for f in findings if f[0] == 'CONFIG']
    if configs:
        return ("opens on a CONFIGURATION panel — the player is asked to set up a thing "
                "they have not seen yet: " + ', '.join(l for _, l in configs[:4]))
    if len(findings) >= 3:
        return ("opens on a control cluster (%d controls before any content): %s"
                % (len(findings), ', '.join(l for _, l in findings[:4])))
    return None


def dead_controls(src):
    """A button that does nothing is a lie told to a player's finger."""
    dead = []
    for m in re.finditer(r'<button\b([^>]*)>([\s\S]*?)</button>', src, re.I):
        attrs = m.group(1)
        label = ' '.join(re.sub(r'<[^>]+>', ' ', m.group(2)).split())[:32]
        rest  = src.replace(m.group(0), '')          # the file, minus this button

        if 'onclick' in attrs.lower():           continue
        if 'type="submit"' in attrs.lower():     continue
        if 'disabled' in attrs.lower():          continue   # honestly dead, on purpose

        wired = False
        idm = re.search(r'id=["\']([^"\']+)', attrs)
        if idm and re.search(r'["\']' + re.escape(idm.group(1)) + r'["\']', rest):
            wired = True
        if not wired:
            for c in re.findall(r'class=["\']([^"\']+)', attrs):
                for one in c.split():
                    if re.search(r'[."\']' + re.escape(one) + r'["\'\s.,)\]]', rest):
                        wired = True; break
        if not wired:
            for d in re.findall(r'data-(\w+)', attrs):
                if 'data-' + d in rest or f'"{d}"' in rest:
                    wired = True; break
        # a delegated listener on a container catches everything inside it
        if not wired and re.search(r'addEventListener\(\s*["\']click', src):
            if re.search(r'closest\(|matches\(|target\.', src):
                wired = True
        if not wired:
            dead.append(label or '(no label)')
    return dead


def sweep(path):
    src = open(path, encoding='utf-8', errors='replace').read()
    out = []
    w = opening_wall(src)
    if w:
        out.append(("OPENING WALL", w))
    for d in dead_controls(src):
        out.append(("DEAD CONTROL", f'"{d}" — a button that does nothing is a lie '
                                    f'told to a finger'))
    return out


def main():
    t = sys.argv[1] if len(sys.argv) > 1 else '.'
    files = [t] if t.endswith('.html') else sorted(glob.glob(os.path.join(t, '*.html')))
    halts = 0
    for f in files:
        r = sweep(f)
        if not r:
            continue
        halts += 1
        print(f"\nHALT  {os.path.basename(f)}")
        for kind, msg in r[:6]:
            print(f"   {kind}: {msg}")
    print(f"\n=== {halts} files at HALT of {len(files)} swept ===")
    print("\nNO OPENING WALL (locked 2026-06-29): the first screen is the SCENE.")
    print("Comfort is a live CORNER control, never a gate. A settings panel you must")
    print("scroll past IS a gate — it does not stop being one because it is pretty.")
    return 1 if halts else 0


if __name__ == '__main__':
    sys.exit(main())
