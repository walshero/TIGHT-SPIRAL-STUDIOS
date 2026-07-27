# STUDIO EYES v3

The accessibility auditor for a founder with retinitis pigmentosa.
**Contrast is arithmetic, not judgment.**

> **STATUS 2026-07-26 (reconciled).** This v3 is NOT the wired live floor — `studio-eyes-sweep.py`
> (v4, WeasyPrint render-proof) is what `floor.yml`/`ratchet.py`/`safe-push.sh` actually run. The two
> were documented and wired against different files, which burned two sessions. Their roles are now
> split: **v4 = the wired render-proof floor** (every push, no browser). **v3 (this tool) = the
> real-browser JS/dynamic-state gate** — it EXECUTES JS and re-reads computed styles per comfort stop,
> which v4 cannot. Kept per the v3 review; still to be WIRED for JS-driven builds. Needs the
> `playwright` pkg + a matching Chromium at runtime (CI installs both; a bare sandbox may not).

## Run it

    pip install playwright pillow && playwright install chromium
    python3 studio-eyes.py --self-test        # gate the auditor
    python3 studio-eyes.py <file.html>        # gate a file

Exit 0 = ship. Exit 1 = HALT.

## Why v3 exists

v2 parsed CSS with regex and **guessed** what the browser would do.
It was wrong seven times — and every one produced FALSE HALTS on files that
were correct. It nearly made us break working code. It taught the founder to
distrust the one tool that cannot be distrusted.

    v2:  read CSS text -> guess cascade -> guess ground -> compute
    v3:  RENDER PAGE   -> ASK for ground              -> compute

The middle column is where all seven bugs lived. It is deleted.

## The self-test is the point

Every v2 bug was found by a human. **That was the real failure.**

v3 ships with 18 canaries of known verdict — and **7 of them are
false-positive traps**: correct files that v2 wrongly HALTed. If the auditor
cannot grade its own canary, **it refuses to audit anything.**

A tool that gates the studio must first gate itself.

## What it checks (ten floors, all HALT)

1. CONTRAST — every text node vs its **actually rendered** ground, in every stop
2. **Text on images/gradients** — samples the real pixels under the glyphs
3. TOKEN-ROLE LAW — no token is both text and decoration
4. STOP SEPARATION — comfort stops differ >=0.12 luminance
5. NO OPENING WALL — first paint must be a scene, never a preference gate
6. NO EMOJI — in rendered text, so JS-injected ones are caught too
7. OFFLINE — intercepts every request; any external host is a HALT
8. FOCUS VISIBLE — tabs to every control, checks for a real ring
9. TOUCH TARGETS — 44px floor, measured on the rendered box
10. DARK MODE — re-runs everything under `prefers-color-scheme: dark`
