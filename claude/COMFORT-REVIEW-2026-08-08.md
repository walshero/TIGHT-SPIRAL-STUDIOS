# COMFORT — studio-wide review, 2026-08-08

Supersedes `claude/COMFORT-KERNEL-REVIEW-2026-08-08.md` (deleted same day). That file
used a name the founder does not use. See the naming ruling below; it is the reason
this document exists at a new path.

Every number here is measured in headless Chromium at 390x844, not asserted.

---

## NAMING — founder ruling, 2026-08-08

**"Comfort kernel" is not the founder's language.** Provenance: the phrase enters the
repo in a machine-written commit message, `3fa29e7`, 2026-07-28 ("comfort kernel v1"),
and spreads from there to 81 files. It appears in no founder-voice document.

Founder's actual vocabulary, stated 2026-08-08:

> **Comfort** is how you view content. It includes font size, contrast, modes like
> warm and dark, motion stop, and screen reader options.

So the settled terms are:

    COMFORT       the founder's word. The whole capability: how content is viewed.
    STUDIO EYES   the founder's name for the control that operates it.
    "kernel"      machine coinage for the shared code block. Internal at best.

Per the studio's own authority rule (`AUTHORITY DEPENDS ON THE CLAIM TYPE` — working
vocabulary and current practice go to the founder, who is in the room), this is not a
preference. It is the correct name, and the previous one was drift.

**Exposure, measured.** 81 files contain the phrase. Render-visible to a reader: **4**.

    index.html            reader-visible
    studio-aleph.html     reader-visible
    comfort-kernel.html   the demo file itself
    comfort-kernel-v2.html the demo file itself

The other 77 are source comments, commit-adjacent docs, gate baselines, and the ledger.
The reader-facing bleed is two real surfaces. That is a cheap fix, not a migration.

This has the same shape as the "Studio Eyes" vocabulary entry already armed in
`retired-lines.json` (`render_only`, banned on player surfaces, permitted on `studio/`).
Proposal in OPEN CALLS below. Not fired yet, deliberately: tick 6 is zero-tolerance with
no ratchet, and deploy re-coupled on 2026-08-08, so arming this before fixing the two
live surfaces would stop the whole site from publishing.

---

## THE PANEL, SCORED AGAINST THE FOUNDER'S OWN DEFINITION

| founder's list | in the control? | state |
|---|---|---|
| font size | yes, A / A+ / A++ | **broken at A++** — see Finding 5 |
| contrast | yes, High contrast toggle | works |
| modes like warm and dark | yes, Default / Dusk / Warm-dark | works, and measures well |
| motion stop | yes, Reduce motion toggle | **dead** — see Finding 1 |
| screen reader options | **no** | **removed 2026-07-29** — see Finding 7 |
|  |  |  |
| colorblind cues | present, not on the founder's list | works |

Three of five items the founder names as comfort are either broken or absent. The
control also carries one item he did not name.

---

## MOUNT STATE

    total HTML surfaces                    133
      mount the shared block (data-light)  101
      old data-stop vocabulary               3   en195-arcade, its preview, one canary
      neither                               29   ~19 of them deliberate canaries/labs

    of the 101:
      reserved-chrome grid                  95
      zoom-based text size                  87
      broken motion selector                 9

This is already the studio standard on 101 of 133 surfaces. The findings below are live
defects at scale, not design notes. The arcade is the outlier; folding it in is small.

---

## GOOD, LEAVE ALONE

**Contrast.** Every text-carrying token pair, all three modes:

    pair                          day     dusk    night
    ink on bg                    14.26   12.62   13.66
    ink-2 on bg                   9.35    8.10   10.24
    ink-2 on surface             10.11    8.86    9.55
    accent-strong on bg           8.41    8.92    8.93
    accent-strong on surface      9.09    9.75    8.33
    ink-2 on surface-2            8.70    6.82    7.75
    on-accent on accent-strong    9.89   12.07    9.69

Floor 4.5, house AAA target 7. All clear AA; all but one clear AAA. Night body luminance
0.010 against a 0.2 ceiling, so warm-dark is genuinely dark. This is the part that was
done right.

**Tap targets.** 62 to 65px against a 48px house floor. Nothing to fix.

---

## FINDING 1 — MOTION STOP IS DEAD

    html.se-reduce *,@media (prefers-reduced-motion:reduce){ *{ animation:none!important; ... } }

An `@media` block cannot appear inside a selector list. The parser discards the whole
declaration. Counted in the CSSOM:

    comfort-kernel-v2.html    0 motion rules parsed of 47 total
    comfort-kernel.html       0 motion rules parsed of 34 total

Both reference files. Zero. Two failures stacked: the Reduce motion button flips
`aria-pressed`, announces "Reduce motion on" to a screen reader, and moves zero pixels;
and the operating system's own reduced-motion setting is not respected either, because it
went down with the same rule. A control that reports success and does nothing is worse
than no control — it stops the reader looking for another way.

Seven other live surfaces carry the identical selector: `arcade.html`, `tsp-intake.html`,
`floor-status.html`, `choose-your-leader-nixon-slice.html`,
`studio/laughter-foundry-spec-and-log.html`, `studio/founder-compass.html`,
`studio/legibility-optimizer.html`, `studio/studio-intake.html`.

Already documented once as a v4 gate finding, then reintroduced into the shared block —
the exact failure the project instructions name: a rule that is prose instead of a check.

**Fix.** Two separate rules, never merged:

    html.se-reduce *{ animation:none!important; transition:none!important; scroll-behavior:auto!important; }
    @media (prefers-reduced-motion:reduce){ *{ animation:none!important; transition:none!important; scroll-behavior:auto!important; } }

---

## FINDING 2 — THE TYPE FLOOR HAS NEVER BEEN MET

`studio-type-contrast-standard.md` v1.0: body 20px minimum, 18px absolute, "Nothing below
18px ships. Ever."

Measured, ten real surfaces, visible text nodes rendering below 18px:

    surface                      body text   under 18px
    studio-aleph.html              18.0px    289 of 300     96%
    studio/tsp-home.html           14.4px     48 of  50     96%
    cliche-city.html               15.0px     21 of  22     95%
    who-holds-the-room.html        17.0px     32 of  34     94%
    play-the-semester.html         18.0px     27 of  31     87%
    index.html                     18.0px    243 of 289     84%
    the-tell.html                  18.0px     12 of  15     80%
    comfort-kernel-v2.html         16.8px     10 of  11     91%
    en195-hub.html                 19.0px      9 of  21     43%

Body runs 14.4 to 19px. Chrome runs 10 to 13px. The Studio Eyes panel labels its light
modes at 12.5px and heads itself at 10.5px: the control built to make text readable
carries the least readable text on the page.

This answers the founder's question of 2026-08-07 — "body text 20 min seems large, what
are you using with me here." Measured answer: the studio has never used 20px, and has
never used 18px either. Studio Eyes E1 measured **one** number, the body base, as a soft
warning. 84 to 96 percent of what renders was never looked at.

The standard is not too strict. It is unenforced, which is a different problem with a
different fix. Lowering the number changes nothing while nothing checks the number that
is already there.

---

## FINDING 3 — COMFORT DOES NOT PERSIST

    files mounting the shared block: 101     with comfort persistence: 0

No `localStorage`, no cookie, no URL param. Every navigation resets to Day.

For a founder with retinitis pigmentosa moving across 101 surfaces: set warm-dark, follow
a link, land back in daylight. Repeat. The colors are excellent and he has to re-request
them on every page.

Highest-friction defect in the review, cheapest to fix, roughly six lines. Compatible with
the offline and single-file floors — `localStorage` is same-origin local storage, not a
network call.

---

## FINDING 4 — REACH REGRESSED

    comfort-kernel.html    (v1)  control at 95.3% of viewport height   bottom
    comfort-kernel-v2.html (v2)  control at  3.9% of viewport height   top

    live surfaces measured: 3.7% to 11.1%, i.e. all top

Studio Fingers' REACH check: the comfortable one-hand thumb arc is the bottom 40%; a
primary action up top is a regrip. v1 had the control in the thumb arc. v2 moved it into
the chrome to fix a real overlap bug and took the reach hit silently.

Neither version has both. They are not actually in conflict once separated: the chrome can
stay top and reserved, and the comfort control can be a bottom-anchored corner element.
Project instruction already says it in words — "comfort is a live corner control."

Bears directly on the open arcade header question. Header at the very top, scrolling away,
is right. The measurement says the comfort button should not have been in the header.

---

## FINDING 