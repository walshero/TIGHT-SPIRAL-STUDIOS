# MOBILE BUILD QUEUE — the all-aleph convening + Studio Fingers sweep (2026-07-27)

**How this was made.** Studio Fingers swept 50 pages (43 fail, 7 pass). Five industry
lenses were convened — mobile game design, accessibility/assistive-tech, consumer-platform
HIG, attention-economy ergonomics, safety-critical HMI — and the Aleph synthesized. The
striking result: **five fields, one spine.** The 225 defects are not 225 problems; they are
~three shared-component fixes plus a short game-specific tail.

---

## WHAT THE FIVE LENSES AGREED ON

- **★★★★★ Fix the ONE shared nav component first.** Root cause pinned: `.tsp-nav a` ≈ 28px,
  `.tsp-barnav a` ≈ 26px, no `min-height`, injected on ~43 pages. Fix once → most of the
  206 F-TAP close in a single change. (All five.)
- **★★★★★ Hit-area ≠ visual size.** Decouple the tappable region from the paint ("hit-slop"):
  grow the hit area with padding / `::before{inset:-8px}`, keep the art small. This is how
  every field reconciles *scene-first / minimal chrome* with big targets — you don't choose.
- **★★★★ 44px is the FLOOR, not the target.** Add **≥8px spacing** (Material) as a co-equal
  rule; safety-critical raises the *working target to ~56px* for global controls because the
  founder's RP and low vision are **degraded conditions, permanently** — so design for the
  degraded case as the center, not the edge.
- **★★★★ Reachability is a second floor the size rule can't see.** The nav sits **top-left —
  the "ow-zone,"** the hardest one-handed reach AND the first region an RP tunnel-field loses.
  A 44px button in the bottom zone beats an 88px button in the top corner. **Reachability and
  accessibility point at the same fix.** Move primary reach targets (Back) to a bottom bar.
- **★★★★ Comfort walls → adopt the knob you already built.** `comfort-control.html` is the
  canonical settings-behind-an-affordance pattern done right. F-WALL 15 is *adoption, not
  invention* — migrate those pages to it. Keep the exit sign lit: the comfort button needs a
  spoken accessible name, ≥44px, and ≥3:1 contrast **in the default theme** (else the control
  that fixes visibility is itself invisible).
- **★★★ Machine-enforce it.** Define `--tap` once as a default in the shared component and make
  "control resolves ≥44px effective hit area" a hard gate HALT, like contrast. The floor lives
  in one component and a machine enforces it at ship — so the fleet can't climb back to 206.

## THE ETHICAL LINE (attention-economy lens)
Adopt the ergonomics, refuse the compulsion. *An ergonomic technique that makes the user's
CHOSEN action easier is ours; one that manufactures a NEXT action they didn't choose is theirs.*
- **Adopt:** thumb-zone reachability, bottom-anchored primary action, ≤100ms multi-channel
  press feedback (visual pressed-state + `navigator.vibrate(10)`), whole-region tap targets.
- **Reject:** variable-reward schedules, streaks/loss nags, exit friction ("are you sure?"),
  red-dot pressure, autoplay, scarcity timers.
- **Codify:** Back/exit must be **at least as reachable and as large as any "continue / play
  again"** control. The dark studios build only the door in; we build the door out too.

---

## THE CONTROL KIT (the fix-once primitive — clears ~80%)
Rebuild the shared nav/control in `tsp-mobile.js`, then re-inline across the fleet:
- `--tap: 44px` floor, **56px working target** for global nav; `min-height`/`min-width` set.
- **≥8px spacing** between adjacent targets.
- **Hit-slop:** touch area exceeds visual via padding / pseudo-element.
- **Bottom-anchored** bar (`bottom:0; padding-bottom:env(safe-area-inset-bottom)`), Back
  biggest and closest. (The pad in `dad-energy.html` already does this — the nav never got
  the memo.) *[OPEN DECISION — this changes every page's chrome; needs founder OK.]*
- **Press feedback** baked in (pressed state + optional haptic).

---

## RANKED QUEUE

**Tier 0 — Control kit** (one component → clears most of F-TAP 206 across ~43 pages).
**Tier 1 — Comfort knob** (migrate the 15 F-WALL pages to `comfort-control.html`; light the exit sign).
**Tier 2 — Viewport sweep** (F-METAVIEW 1 + F-VIEWPORT 3): add `<meta viewport … viewport-fit=cover>`, never disable zoom, fix horizontal overflow.
**Tier 3 — Small-button tail** (hit-slop + whole-region targets, routed through `--tap`).
**Tier 4 — Harden the gate**: make ≥44px a HALT; add checks for spacing, reachability (nav in bottom zone), legibility (≥12px actionable text + labels scale), and the ethical inversion (exit ≥ continue). Note: focus-order (2.4.3) / focus-visible (2.4.7) need a separate keyboard/switch wing — touch sweeps miss them.

### Per-file punch-list (from the sweep)
| Tier | File | Defects |
|---|---|---|
| T3 | sandbags.html | F-TAP ×58 |
| T3 | confluence-TRUNK.html | F-TAP ×21, F-VIEWPORT |
| T3 | advantage-intake.html | F-TAP ×15 (form controls) |
| T3 | tsp-spiral-studio.html | F-TAP ×13 |
| T3 | sticker-price.html | F-TAP ×11 |
| T1/T3 | confluence-massbay-assessment.html | F-TAP ×10, F-WALL |
| T1/T3 | index.html (the face) | F-TAP ×10, F-WALL, F-VIEWPORT |
| T1/T3 | cliche-city / cliche-field / cliche-line | F-TAP ×5 each |
| T1/T3 | funny-boneys-factory.html | F-TAP ×4, F-WALL |
| T1/T3 | choose-your-leader-v5-slice.html | F-TAP ×4, F-WALL |
| T3 | your-rp-world / reading-the-fireground | F-TAP ×4 each |
| T1 | course-river, flash-ballast, review-bench, workshop-wall, the-compound-capstone | F-TAP + F-WALL |
| T1 | en195-last-week, en195-what-counts-now, motion-specimen, play-the-semester-flash, tsp-intake, trail-notes | F-WALL (+ trail-notes F-VIEWPORT) |
| T0 | arcade, behind-this-door, choose-your-leader-v6, cliche-cowpaths, en195, en195-hub, fys_fys-treasure-trove, how-an-idea-travels, islo-hub, play-the-semester, table-four, the-tell, the-viscosity, tight-spiral-runbook, warriors-fantasy-arcade, workshop-in-a-box | F-TAP ×1–3 (shared nav only — Tier 0 clears these outright) |
| T2 | comfort-control.html | F-METAVIEW |

**Already passing (7):** the-console (Flok), dad-energy, old-problems-at-new-speed,
choose-your-leader-v5, choose-your-leader-nixon-slice, leeder-intake, tsp-opportunity-bridge.

---

## THE ONE DECISION FOR THE FOUNDER
Every lens recommends **moving the shared nav from the top corners to a bottom bar** — it's
the strongest single upgrade (reachability + RP field both favor it), but it changes the chrome
on every page. Bottom-anchor the nav, or keep it top and only fix size/spacing/hit-slop?
