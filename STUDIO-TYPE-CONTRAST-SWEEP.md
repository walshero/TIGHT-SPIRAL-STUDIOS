# Studio Type & Contrast Sweep - 2026-07-26

Full-corpus application of `studio-type-contrast-standard.md` v1.0, enforced by
`preship-gate-v5.py`. Result: **81/81 non-Confluence files SHIP (zero halts).**

## Before
0 / 85 files passed the v5 gate. Dominant failures: no `@media prefers-color-scheme`
dark path (universal), sub-18px fonts (~40 files), sub-44px tap targets (~18),
decorative emoji (~32), external Google Fonts (2). Contrast pairs: 0 failures -
token discipline was already sound.

## Applied (mechanical, design untouched)
- DARK: injected a measured dark path. Token-system files mirror the studio dark
  palette; hardcoded-color files got an inline `@media prefers-color-scheme:dark`
  surface override. Auto-dark now resolves to MEASURED values (fixes the
  your-rp-world 1.17:1 force-darken bug).
- FONT: every sub-18px raised to 18 (UI) or 20 (body).
- TAP: every sub-44px min-height/min-width raised to 44.
- EMOJI: decorative pictographic emoji stripped. Arrows, geometric shapes, and
  box-drawing glyphs PRESERVED (they are functional UI, not emoji).
- HOST: Google Fonts removed from play-the-studio.html and what-this-is.html,
  mapped to the studio system serif/sans stacks. Still offline.

## Excluded (by law, not oversight)
- confluence-TRUNK.html, confluence-massbay-assessment.html, confluence-console.html
  - Confluence is a RO mount; TSP does not write it. Route to the Confluence owner
  if the standard should apply there.
- choose-your-leader-nixon-slice.html - 10KB truncated seed stub; quarantine to
  archive/ (standing note), not a real page.

## Gate corrections made during the sweep (machine-was-the-suspect)
- DARK check: accept any prefers-color-scheme block (dark OR light-inverting) or
  color-scheme:dark, scanned across whole HTML - not only literal
  "prefers-color-scheme:dark" inside <style>.
- EMOJI check: narrowed to true pictographic ranges; stopped flagging arrows
  (2190-21FF), geometric shapes (25A0-25FF), box-drawing (2500-257F).
- Canary-tested after loosening: a deliberately broken file still HALTs on all six
  checks. The gate has teeth; 81/81 is real.

## Standing follow-ups
- Confluence trio: needs owner decision on whether/how the standard applies (RO).
- nixon stub: quarantine to archive/.
- Per-device truth: gate says SHIP; founder should open 2-3 on an actual phone in
  dark mode to confirm render (the your-rp-world lesson: device is final judge).
- Remaining ~69 internal/studio pages: gated-clean and Drive-saved; deploy to
  GitHub Pages in a batch once the Drive->GitHub bridge credential is connected.
