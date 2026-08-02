# Tight Spiral Productions — Type & Contrast Standard
**Version 1.0** · authored 2026-07-26 · supersedes scattered per-file font rules and the memory-only nav/font floors

This is the single source for how every TSP surface handles type, tap targets, contrast,
and dark mode. It is written in arithmetic so a gate can enforce it. A rule that can't be a
check is a wish — every clause here maps to a check in `preship-gate-v5.py`.

Accessibility is not a section of this document. It IS this document. The founder has
retinitis pigmentosa; contrast and size are computation, not judgment.

---

## 1. FONT FLOOR (mobile-first, RP-first)
- **Body text: 20px minimum.** Reading copy, prompts, card bodies, reveal text.
- **Any on-screen text: 18px absolute minimum.** Nav buttons, kickers, footers, captions,
  labels, chips, tags — everything a human reads. Nothing below 18px ships. Ever.
- Line-height for body >= 1.5.
- Rationale: 18px is the smallest a phone-held screen stays readable with low vision.
  Desktop can go bigger; the floor is set by the hardest case, not the easiest.

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
- `preship-gate-v5.py <file>` is the single gate. Exit 0 = SHIP. Exit 1 = HALT.
- No file's own comment is trusted as proof of passing. Only a live gate run is proof.
- The gate supersedes preship-contrast-gate.py, preship-gate-v3.py, preship-gate-v4.py.
- Corpus sweep: `preship-gate-v5.py --sweep` runs every HTML file and prints a scorecard.
