# Tight Spiral Productions — Type & Contrast Standard
**Version 1.1** · authored 2026-07-26 · amended 2026-08-08 (founder ruling on the font floor; see §1)

This is the single source for how every TSP surface handles type, tap targets, contrast,
and dark mode. It is written in arithmetic so a gate can enforce it. A rule that can't be a
check is a wish — every clause here maps to a check in `preship-gate-v5.py`.

Accessibility is not a section of this document. It IS this document. The founder has
retinitis pigmentosa; contrast and size are computation, not judgment.

---

## 1. FONT FLOOR (mobile-first, RP-first)

**AMENDED 2026-08-08. The separate 20px body line is RETIRED. One floor now.**

- **Every rendered text node: 18px absolute minimum.** Body, nav, kickers, footers,
  captions, labels, chips, tags. Everything a human reads. Nothing below 18px ships.
- **The reader's own browser text setting supplies the base.** Declare `font-size:100%`
  on `:root` and scale with rem. A hardcoded px root overrides the one accessibility
  control the reader already owns, and 69 of 75 root-level files already defer correctly.
- Line-height for body >= 1.5.
- Rationale unchanged: 18px is the smallest a phone-held screen stays readable with low
  vision. The floor is set by the hardest case.

**Why the 20px line went.** On 2026-08-08 v1.0's font floor was measured against live
surfaces for the first time in the eighteen days it had existed. Body text ran 14.4px to
19px; chrome ran 10px to 13px; the share of visible text nodes rendering under 18px was
43% to 96% depending on the surface, 243 of 289 on the front door. The comfort control's
own panel labelled itself at 10.5px. Neither number in v1.0 had ever been met anywhere.

The reason was not laxity, it was instrumentation. The only check pointed at this clause
measured ONE value, the body base, as a SOFT warning (Studio Eyes E1). Between 84 and 96
percent of what actually rendered was never looked at. Two numbers where nothing counted
even one is not a stricter standard, it is a longer wish. Founder ruling: keep the floor
that can be checked on every node, drop the one that cannot, and let the reader's own
setting do the work the second number was reaching for.

**This clause is now enforced.** `type-census.py` renders each surface at 390x844 and
counts every visible leaf text node against the 18px floor, ratcheted per surface in
`type-baseline.json`. Today's debt is carried; a RISE blocks. The count may fall or hold,
never rise. Reach zero and the surface leaves the baseline forever.

## 2. TAP-TARGET FLOOR
- **Interactive targets: 44x44px minimum** (buttons, toggles, choices, nav).
- min-height AND min-width both >= 44px on anything clickable.
- Rationale: a missed button is a wall. RP means you can't hunt for a 30px target.

## 3. TOKEN LAW (atmosphere OR text, never both)
- A color token is EITHER a surface/atmosphere fill OR a text color. Never reused as both.
- Text tokens: --ink, --ink2, --band-ink, --paper (only as text ON a dark band).
- Surface tokens: --paper, --card, --shade, --band, --rule.
- Accent tokens (--dusk, --field, --pick, --alarm, --leaf) are ATMOSPHERE / art fills only.
  They may NOT be used as a text color unless they independently pass the contrast floor
  against their actual background. The amber-as-text bug lived because an accent was used
  as text and eyeballed. Arithmetic kills it.

## 4. CONTRAST FLOOR (AAA, not AA)
- **Body text: 7:1 minimum** against its actual rendered background (WCAG AAA).
- **Large text (>=24px bold or >=30px regular): 4.5:1 minimum.**
- Contrast is measured on token PAIRS THAT ACTUALLY CO-OCCUR on screen, not every
  hypothetical combination. The gate must model real foreground/background pairs.
- Both palettes (default + dark) measured independently.

## 5. DARK MODE (measured, not hoped)
- Every surface must define a dark palette the gate can find AND measure.
- Convention: `body.warm { --token:… }` is the TSP dark palette (comfort-corner toggle).
- **AND** a `@media (prefers-color-scheme: dark)` path must exist so a phone forcing dark
  mode hits MEASURED tokens, not the browser force-darkening an unmeasured light palette.
  Force-darkened light pages are how your-rp-world.html rendered at 1.17:1 after "passing."
- If only one dark path exists, the gate HALTS with H-DARK-MISSING until both are present.

## 6. OFFLINE / SINGLE-FILE
- No external font hosts (no Google Fonts link, no CDN). System font stacks only.
- Single file, works offline. No external anything.

## 7. STUDIO TYPEFACE PAIR
- **Reading (body, prompts, headings): serif** — `"Iowan Old Style","Palatino Linotype",Georgia,serif`.
  Warm, high-legibility, on-brand. All system fonts.
- **Interface (buttons, nav, kickers, labels, chips): sans** —
  `system-ui,-apple-system,"Segoe UI",Roboto,sans-serif`.
- **Monospace is retired from product surfaces.** It reads as "code," not "product."
  Monospace allowed only inside actual code/telemetry displays where the content IS code.
- Two families, deliberately. Serif reads; sans operates.

## 8. ENFORCEMENT
- No file's own comment is trusted as proof of passing. Only a live gate run is proof.
- **The belt is the enforcement layer, not a single gate.** `studio-belt.sh <repo>` runs
  every armed tick and blocks on any HALT. As of 2026-08-08 that is seven ticks, and
  `floor.yml` re-coupled deploy the same day, so a HALT now stops the site publishing.
- This clause's own check is `type-census.py` (see §1). It is not yet mounted as a belt
  tick; mounting it is a founder call, because it would arm an eighth tick.

### RETRACTED, 2026-08-08, same day. The section immediately below is WRONG on its first
### bullet. Left standing rather than deleted. See CORRECTION at the end of this file.

### STALE NUMBERS IN THIS DOCUMENT, recorded 2026-08-08, NOT silently changed

Two clauses here disagree with what the studio actually ships. Recording the drift rather
than editing it, because both are founder calls, and a standard quietly rewritten to match
practice stops being a standard.

- **§2 says 44x44px. The belt ships 48px.** `studio-fingers.py` cites the stricter of
  Apple 44 and Material 48 and calls 48 the house floor, with 24px flagged separately as
  the WCAG 2.5.8 AA LAW line. Ninety-seven of 133 surfaces carry debt against 48 today and
  75 of those sit below the 24px legal line. That 75 is the number that must reach zero.
- **§5's convention line says `body.warm`.** The corpus uses `html[data-light="night"]`
  on 101 surfaces. `preship-gate-v4.py` parses neither; it looks for `:root` inside an
  `@media (prefers-color-scheme: dark)` block and for `html[data-comfort]`, which is why
  it has stood a false H-DARK-MISSING against `index.html` since 2026-08-03.

---

### CORRECTION, 2026-08-08, hours after the amendment above

The bullet claiming section 2's 44x44px was stale and that "the belt ships 48px" is
**retracted**. It was backwards.

`studio-fingers.py` at repo root was retired the same day and its own postmortem is
explicit: the 48px "house floor" was DERIVED FROM APPLE by an agent, while the founder's
own 44x52 ruling had been sitting in `PLAYTEST-REPORT.md` and three rescued design docs
since July. That invented number manufactured 66 surfaces and 121 halts of debt that never
existed. Section 2 was right the whole time. The gate was wrong, this document was
correct, and the amendment trusted the machine over the founder.

The failure is the interesting part, which is why the wrong text stays visible above. The
studio's own rule says that when the founder and a machine-produced number disagree, the
machine is the suspect. An hour earlier this file was amended to say the opposite, on the
authority of a gate that was retired before the ink dried.

**Which touch gate is canon:** `studio-eyes/studio-fingers.py`, which RENDERS at a 412x915
touch viewport. The root `studio-fingers.py` parsed source, shipped four false positives
against one build in a single afternoon, and now exits 2 loudly rather than 0, because a
gate that has gone blind must never read as clean.

**Still genuinely uncovered, and still a founder call:** non-text contrast. WCAG 1.4.11
wants 3:1 for control boundaries. Measured on the comfort block's own controls: border
against fill 1.50 to 1.68, border against panel 1.91 to 2.07, across day, dusk and night.
Only the high-contrast day stop clears. No clause in this document covers it and no gate
in the studio checks it.

