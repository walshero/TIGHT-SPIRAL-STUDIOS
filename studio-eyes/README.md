# STUDIO EYES v3

The accessibility auditor for a founder with retinitis pigmentosa.
**Contrast is arithmetic, not judgment.**

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

## What it checks (eleven floors, all HALT)

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
11. **CLIPPED TEXT** — text laid out and then thrown away by a clip box

## Floor 11, and the limit it does not hide

Added 2026-09-01. Flok's research card shipped unreadable for weeks with floors
1-10 green: `Why does this work?` flipped open onto a 68px box holding 85px of
research, so the first line was sliced through the x-height and the citation was
cut in half. Contrast 12:1. Target 340x68. Focus ring present. **Nothing here had
ever been asked whether you can actually read it** — every floor graded the glyphs
it could see, and none looked for the glyphs the compositor had thrown away.

A box and a window both clip; only one is broken. The separation is a ratio, not a
judgment: measured on that file, the broken card held 76px in a 68px box (1.12) and
the diegetic phone feed held 699px in 150px (4.66). Under `CLIP_WINDOW_RATIO` (2.0)
the box was meant to fit and HALTs; over it, the shape is a window and the finding
is reported without blocking. Scroll windows, closed disclosures, sr-only text and
ellipsis truncation are forgiven, and `canary/p09-legit-clips.html` is the trap that
keeps them forgiven.

**This floor would not have caught the bug that caused it, and says so.** Studio Eyes
measures first paint. Flok's card sits behind three clicks (start, hit the target,
flip), so at first paint it is empty and collapsed and the floor correctly finds
nothing. The measurement itself is exported as `CLIP_PROBE` and run by
`playthrough-agent.py` at **every state its crawler already visits** — which is where
the real card was found, and where a regression in the first fix was caught the same
afternoon. One canon writes, others read.
