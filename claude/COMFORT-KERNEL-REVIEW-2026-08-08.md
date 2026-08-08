# COMFORT KERNEL REVIEW — studio-wide, 2026-08-08

Founder asked for a whole-studio review of the comfort kernel before more surfaces
get built on it. This is that review. Every number below is measured in headless
Chromium at 390x844 (Matt's phone), not asserted.

Harness: `/tmp/kreview.py`, `/tmp/k2.py` (throwaway). Method is reproducible from
the findings; the permanent instrument this review argues for is in RECOMMENDATION 1.

---

## MOUNT STATE — how much of the studio is on the kernel

    total HTML surfaces                  133
      mount the kernel (html[data-light]) 101
      data-stop vocabulary (old)            3   en195-arcade, its layout preview, one canary
      neither                              29   of which ~19 are deliberate canaries/labs

    of the 101 kernel files:
      v2 reserved-chrome grid              95
      v2 zoom-based text size              87
      merged reduce-motion selector bug     9

The kernel is not a proposal. It is already the studio's standard, on 101 of 133
surfaces. The three findings below are therefore not design notes, they are live
defects at scale.

The arcade is the outlier, not a competing standard. Folding it onto the kernel is
a small job; there is no vocabulary war to settle.

---

## WHAT IS GOOD, AND SHOULD NOT BE TOUCHED

**Contrast.** Every token pair that carries text, in all three modes:

    pair                          day     dusk    night
    ink on bg                    14.26   12.62   13.66
    ink-2 on bg                   9.35    8.10   10.24
    ink-2 on surface             10.11    8.86    9.55
    accent-strong on bg           8.41    8.92    8.93
    accent-strong on surface      9.09    9.75    8.33
    ink-2 on surface-2            8.70    6.82    7.75
    on-accent on accent-strong    9.89   12.07    9.69

Floor is 4.5. Studio's own AAA target is 7. Every pair clears AA; all but one clear
AAA. Night body luminance measures 0.010 against a 0.2 ceiling, so warm-dark is
genuinely dark, not a dimmed light mode. This is the part of the kernel that was
done right and it is why the corpus survives the comfort gate at all.

**Tap targets.** Every control in the chrome and panel measures 62 to 65px against
a 48px house floor. Studio Fingers has nothing to say about the kernel's own
controls. Also done right.

---

## FINDING 1 — THE REDUCE-MOTION TOGGLE IS A LIE

The kernel writes this rule:

    html.se-reduce *,@media (prefers-reduced-motion:reduce){ *{ animation:none!important; ... } }

An `@media` block cannot appear inside a selector list. The CSS parser discards the
entire declaration. Measured in the CSSOM:

    comfort-kernel-v2.html    0 reduce-motion rules parsed of 47 total
    comfort-kernel.html       0 reduce-motion rules parsed of 34 total

Both reference implementations. Zero. The consequence is two failures stacked:

1. The "Reduce motion" button in the Studio Eyes panel changes nothing. It flips
   `aria-pressed`, announces "Reduce motion on" to a screen reader, and moves zero
   pixels. A control that reports success and does nothing is worse than no control,
   because it stops the user from looking for another way.
2. The operating system's own `prefers-reduced-motion` setting is not respected on
   these files either, since it went down with the same rule.

Seven other live surfaces carry the identical broken selector: `arcade.html`,
`tsp-intake.html`, `floor-status.html`, `choose-your-leader-nixon-slice.html`,
`studio/laughter-foundry-spec-and-log.html`, `studio/founder-compass.html`,
`studio/legibility-optimizer.html`, `studio/studio-intake.html`.

This is the same two-rule regression already documented as a v4 gate finding. It was
written down and then reintroduced into the kernel itself, which is the exact failure
mode the project instructions name: a rule that is prose instead of a check.

**Fix.** Two separate rules, never merged:

    html.se-reduce *{ animation:none!important; transition:none!important; scroll-behavior:auto!important; }
    @media (prefers-reduced-motion:reduce){ *{ animation:none!important; transition:none!important; scroll-behavior:auto!important; } }

---

## FINDING 2 — THE TYPE FLOOR HAS NEVER BEEN MET, ANYWHERE

`studio-type-contrast-standard.md` v1.0 states: body 20px minimum, 18px absolute,
"Nothing below 18px ships. Ever."

Measured, ten real surfaces, count of visible text nodes rendering below 18px:

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

Body text across the studio runs 14.4px to 19px. Chrome text runs 10px to 13px. The
kernel's own Studio Eyes panel labels the light modes at 12.5px and heads the panel
at 10.5px. The control built to make text readable has the least readable text on
the page.

This answers the founder's question from 2026-08-07 directly. He asked "body text
20 min seems large, what are you using with me here." The measured answer: the studio
has never used 20px. It has never used 18px either. The 20px line is aspirational
text in a document, and Studio Eyes E1 only ever measured **one** number, the body
base, as a soft warning. 84 to 96 percent of what actually renders was never looked at.

The standard is not too strict. It is unenforced, which is a different problem and
has a different fix. Writing a lower number into the standard would change nothing,
because nothing is checking the number that is already there.

**This is the finding that matters most.** Everything else on this page is a bug.
This is a governance hole: six documents assert a floor and the one instrument that
could have caught it was pointed at a single value.

---

## FINDING 3 — THE KERNEL DOES NOT REMEMBER

    kernel files: 101     with comfort persistence: 0

No `localStorage`, no cookie, no URL param. Every navigation resets to Day.

For a founder with retinitis pigmentosa moving across 101 surfaces, this means
setting warm-dark, clicking a link, and landing back in daylight. Then doing it again.
The kernel's colors are excellent and he has to re-request them on every page.

This is the highest-friction defect in the review and the cheapest to fix. It is
roughly six lines, and it is compatible with the offline and single-file floors
because `localStorage` is same-origin local storage, not a network call.

---

## FINDING 4 — v2 REGRESSED REACH AGAINST v1

    comfort-kernel.html    (v1)  control at 95.3% of viewport height   bottom
    comfort-kernel-v2.html (v2)  control at  3.9% of viewport height   top

    live surfaces measured, control position: 3.7% to 11.1%, i.e. all top

Studio Fingers' REACH check states the comfortable one-hand thumb arc is the bottom
40% of the screen and that a primary action up top is a regrip. v1 had the comfort
control in the thumb arc. v2 moved it into the chrome to fix a real overlap bug, and
took the reach hit silently.

Both versions solved one problem and created the other. Neither has both. The fix is
not to pick a version, it is to notice that "reserved chrome that never overlaps" and
"reachable by a thumb" are not in conflict once they are separated: the chrome can
stay top and reserved, and the comfort control can be a bottom-anchored corner
element. The project instruction already says this in words: "comfort is a live
corner control."

Directly relevant to the open arcade header question. The founder asked for the header
at the very top, scrolling away. That is right for the header. The measurement says
the comfort button should not have been in the header to begin with.

---

## FINDING 5 — TEXT SIZE USES `zoom`, WHICH BREAKS THE PANEL

    html.se-a1{ zoom:1.15; }
    html.se-a2{ zoom:1.3; }

`zoom` is non-standard, scales layout rather than type, and does not participate in
the `calc()` the panel is positioned with. The panel is pinned at
`top:calc(var(--tap) + 14px)`, a hardcoded 62px guess at the chrome's height.

Measured at A++ (`zoom:1.3`), panel open, 390x844:

    chrome bottom     90.2px
    panel top         80.6px
    OVERLAP            9.6px

At the largest text setting, which is the setting a low-vision reader is most likely
to choose, the Studio Eyes panel slides under the header and its first row is
covered. The accessibility control breaks hardest for the person who needs it most.

**Fix.** Drive text size with `font-size` on `:root` rather than `zoom`, and position
the panel from the chrome's measured height rather than a hardcoded constant. This
also restores the reader's own browser text-size preference as the base, which is the
convention 69 of 75 root-level files already follow.

---

## FINDING 6 — `--focus` IS A DUAL-ROLE TOKEN

Project instruction: "A color token is atmosphere OR text, never both."

`--focus` is the focus-ring color AND the `.eyebrow` text color. Measured as text:

    day    6.20:1     clears AA, fails the studio's 7:1 AAA body target
    dusk   4.93:1     clears AA by 0.43
    night 10.46:1     fine

It is the only pair in the whole kernel that misses AAA, and it misses because it is
being asked to be two things. Split it: `--focus` for rings, `--eyebrow` for the
eyebrow, tuned independently.

---

## RECOMMENDATION

**1. Recommended — fix the kernel in one pass, and build the check that would have
caught Finding 2.**

Six edits to `comfort-kernel-v2.html` (motion split, persistence, bottom-corner
comfort control, `font-size` instead of `zoom`, measured panel offset, token split),
then propagate. Alongside it, extend the type check from one number to every rendered
text node: a gate that reports "N of M visible text nodes below 18px" per surface,
ratcheted against a baseline so today's debt is carried and only new debt blocks.

Why this is the right call: five of the six defects are small and mechanical, and the
sixth is not a defect at all but a missing instrument. Fixing the kernel without
building the check leaves the studio in the same position it is in now, which is a
floor asserted in six documents and measured in none. The ratchet shape is already
proven on five other ticks, so this is mounting a known pattern, not inventing one.

Tradeoff: propagating to 101 surfaces is the expensive part, and the type baseline
will be large and ugly on day one. That is the honest state of the corpus, and a
baseline that reflects reality is worth more than a floor that does not.

**2. Simpler alternative — fix only Findings 1 and 3, skip the rest.**

The dead motion toggle and the missing memory are the two that actually cost the
founder something every day. Both are small. This buys most of the daily relief for
a fraction of the work and leaves the type question open.

**3. More advanced — kernel v3 as a single shared file the surfaces link.**

The single-file offline floor currently forces the kernel to be copy-pasted into
every surface, which is why nine files carry a bug fixed elsewhere and why 87 of 101
have the zoom version and 14 do not. A v3 that is one file, referenced, would make
"fix once" true. It is a real change to the offline floor and a founder call, not a
cleanup, so it is listed here rather than recommended.

**What to ignore for now:** the contrast palette and the tap-target sizing. Both were
measured and both are clean. Do not spend a pass on them.

---

## OPEN, NEEDS A FOUNDER CALL

- **The 20px line in `studio-type-contrast-standard.md` v1.0.** Measured reality is
  14.4 to 19px body, 10 to 13px chrome. Either the number moves to something the
  studio will actually hold, or the corpus moves to the number. Recommendation: keep
  18px as the enforced absolute for every rendered node, drop the separate 20px body
  line, and let the reader's own browser setting supply the base. That is a floor
  that can be checked, which is the only kind that is real.
- **Comfort control: bottom corner (thumb arc, v1) vs top chrome (reserved, v2).**
  Recommendation: bottom corner, chrome stays top.
- Whether kernel v3 becomes a linked shared file (Recommendation 3).

---

Measured 2026-08-08. Nothing in this review is an opinion about how it looks.
