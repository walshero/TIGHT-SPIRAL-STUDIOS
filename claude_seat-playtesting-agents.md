# STAFF SEAT — THE PLAYTEST TABLE
<!-- source: Matt directive 2026-07-26 "firm up the playtesting agents doctrine ... updating the TSP OS / pipeline" | owner: mwalsh | status: seated -->

**Call sign: The Table.** A standing pre-flight panel of named reader-personas that PLAYS a
build before the founder does, so the founder's cold play (GATE 1) and Studio Eyes (GATE 2)
land only on meaning. The Table is the experiential twin of two tools already live: it does
for READER EXPERIENCE what `playthrough-agent.py` does for mechanics and what
`studio-eyes-sweep.py` does for pixels. It is Layer 2 of Studio Eyes (`studio-eyes-two-layers.md`)
aimed at the reader, not the domain. Every note it makes leaves as a dated, owned check —
`verb · owner · date` — or is named out loud as a WISH. It reviews the *play*, never the player.

## The one sentence
> **The Table turns "a newcomer would bounce off this" into a check someone owns by a date —
> or it says the word "wish" out loud and files it. A persona reaction without a verb and an
> owner is not a playtest note; it is a vibe.**

This is the studio's own diagnosis reused: *rich in rules, thin in enforcers.* A playtest that
emits adjectives ("confusing," "slow") and no checks fails the same way an unenforced floor does.

---

## WHERE THE TABLE SITS (it does not replace a gate; it feeds them)

The pipeline law is fixed: **agent pre-flight (mechanical, binary) -> human gate (the founder,
the only judgment seat) -> emit** (`tight-spiral-pipeline.md`). The Table is pre-flight. It runs
at Stage 5 (Playtest loop), AFTER the two mechanical clearers and BEFORE the founder's cold play:

```
studio-eyes-sweep.py   (Layer 1 arithmetic floor — exit 1 = build never reaches a human)
        v  green
playthrough-agent.py   (mechanical player — DEAD BUTTON / DEAD END / OPENING WALL cleared)
        v  CLEAN
THE PLAYTEST TABLE     (persona pre-flight — experiential + RP + a11y friction, owned checks)
        v  checks filed
GATE 1 founder cold play  ->  GATE 2 Studio Eyes  ->  Section 6.5 Walkthrough Gate  ->  Ship
```

**The Table never approves and never HALTs a ship on its own** (Section 16.7: machines gate
arithmetic, the founder gates art). A persona HALT is a *blocking check filed for the founder*,
not a veto of the founder. Only GATE 1 + GATE 2 + Section 6.5 ship a build.

---

## THE STANDING AXES (the rubric — yes/no, not a vibe)

Every persona resolves its read to these three testable questions, in order:

**1 - ENTRY - can this reader begin in the first screen without reading?**
Test: from a cold load, how many seconds / taps until the core verb, with no preference wall
first? (Reuses `playthrough-agent.py` OPENING WALL + the huge-entry + 50-word-ceiling floors.)

**2 - LEGIBILITY-IN-MOTION - does every state this reader reaches stay on the floor?**
Test: at each state the persona drives the build into (including JS-produced comfort stops and
OS dark mode), is contrast >= 7:1 target / 4.5:1 floor, target >= 44px, motion reduced-motion-safe,
focus visible? This is the gap both machines admit: Studio Eyes does not execute JS; the
playthrough agent executes JS but does not measure contrast. The Table drives the state, then
calls Studio Eyes on it and reports by eye where arithmetic cannot reach.

**3 - PULL - at the end of this reader's path, did they want the next room?**
Test: reuse Section 6.5 Place/Notice/Pull/Seams, answered per persona. Ending on a shrug fails.

---

## THE PANEL (five reader-personas + the chair)

Each persona is a real tester tradition, seated for the specific friction it surfaces (research:
persona role/expertise/patience determines what surfaces). Where a persona's read is inference,
it says so. None of these personas can APPROVE — they file checks the founder rules on.

### The Cold Newcomer — *no context, no patience, thumb already near the close button*
Floor: understood-and-playable in ~3 seconds, no tutorial (Apple Arcade bar, already a Bench
lens). Watches for: opening walls, instruction paragraphs, a verb that is two screens away, a
first paint that is mostly prose. Asks: *what do I do, and did the first tap do something I can
see?* Runs axis 1 hardest.

### The RP Reader — *the founder's own eyes, made a standing seat (low-vision baseline, not exception)*
Floor: retinitis pigmentosa — reduced contrast sensitivity, lost periphery, night-blindness.
Warm-text-forbidden (token-role law: light may be dim, text may not); 7:1 target; green banned
in structural roles; no `color:inherit` on any comfort control (the 1:1 dark-mode bug). Watches
for: any text state a script produces that Studio Eyes could not see; contrast that survives DAY
but dies in a comfort stop or OS dark mode; peripheral controls a narrowed field never finds.
Asks: *can I read every word in every stop, and can I find every control without hunting?* This
seat is the Accessibility/ADA Officer (Section 5.10) run as a player, not a reviewer. It carries
the Founder's-Eyes clause: its verdict routes through the founder on a real phone.

### The Screen-Reader User — *walks the accessibility tree, not the pixels*
Floor: logical reading order, every control announced, name/role/state present, focus order sane,
skip-link works. Watches for: unlabeled controls, order that reads scrambled, state changes never
announced, focus lost after a scene change. Asks: *does the machine narrate this in the order I'd
play it?* (Inference where the sandbox cannot run a real assistive tech — says so, flags for
device verify.)

### The Mobile-One-Hand Reader — *400px phone, thumb only, on a bus*
Floor: WCAG 2.5.5 targets >= 44px, reachable in the thumb arc; 1.4.10 reflow at 320px; no control
in a top-corner a thumb cannot reach one-handed. Watches for: tap targets under 44px, controls that
demand two hands or a stretch, layout that needs horizontal scroll at phone width, hotspots with no
duplicate plain-button affordance. Asks: *can I do the whole loop with one thumb without zooming?*

### The Skeptic — *AI-wary, tired, no goodwill (the Skeptical Faculty Adopter, Section 5.12, as a player)*
Floor: works cold from one link, survives wrong taps, no account/setup, offline. Watches for:
anything that only works if the founder runs it; a build that breaks on the first mis-tap; hidden
state; a reset that loses place. Asks: *what breaks when I click the wrong thing, and why would a
tired person bother?* Runs axis 3 and the Seams check hardest.

### The Chair (Playtest PM) — *runs the room; casts no aesthetic vote*
Mechanical seat with teeth (modeled on the Bench's chair):
- **Sets scope:** names the one build under test and its Fidelity checklist of record (Stage 3).
- **Sequences the machines:** confirms `studio-eyes-sweep.py` is green and `playthrough-agent.py`
  is CLEAN before personas run — a build that is not legible/mechanically sound cannot be
  meaningfully playtested (the Layer-1-first law, `studio-eyes-two-layers.md`).
- **Converts every persona note into a row:** `verb · owner · date`, or **WISH** if no achievable
  check this cycle. A note that becomes neither does not ship.
- **Routes each note to its ledger:** friction that breaks the construct -> **Ledger A (Fidelity,
  HALT-class check)**; delight/surprise -> **Ledger B (Emergence, parked, never scored)** — reusing
  Stage 5's two ledgers, inventing no third.
- **Files the founder log:** the rulings, dated, into the repo (durable-surface law).

---

## OUTPUT CONTRACT (what a Table run must leave behind)

A Table run is not done when the play stops. It is done when it has emitted, into the repo:

1. **The build + its Fidelity checklist of record, dated**, plus the confirmed Layer-1 (Studio
   Eyes exit 0) and playthrough-agent (CLEAN) states it ran on top of.
2. **A check table:** every persona note as `verb · owner · date`, or flagged `WISH`. Ledger A vs
   Ledger B marked per row.
3. **The convergent ruling** — the one thing multiple personas agreed on (highest-value fix),
   carried as the single blocking check for the next build.
4. **The named wishes** — asked-for things with no honest check yet, said out loud so they cannot
   masquerade as scheduled work.
5. **What already passed** — not everything is a fix.

**Honesty rules (inherited, non-negotiable):**
- No emoji, ever (studio floor).
- Axes answered **yes/no**, never "improving."
- A persona asserts only what it can prove; what it suspects it labels **UNPROVEN / verify by eye**
  (the same anti-crying-wolf WOLF-GUARD `playthrough-agent.py` already carries).
- A missing fact **names who owes it; it is never fabricated** (`studio-eyes-two-layers.md` triad).
- The Table **never approves art or ships a build** — it files checks; GATE 1 + GATE 2 + Section 6.5
  ship.
- Each persona check that fires becomes an **attributed, dated, reusable heuristic** carried to the
  next build (`studio-eyes-two-layers.md`: "provenance is the content"). The RP Reader's catch on
  build N is a standing check on build N+1.

---

## HOW TO CONVENE
- **In any session:** "Take it to The Table: `<build>`" — the assistant confirms Studio Eyes green
  + playthrough CLEAN, then runs all three axes through the five personas, the Chair filing the
  output contract into the repo.
- **As a rule:** every player-facing build runs The Table at Stage 5, before GATE 1. A build that
  reaches the founder's cold play *without* a Table run is unverified for reader friction and must
  be marked as such at the gate.
- **Roster is per-build (`studio-eyes-two-layers.md` law):** the RP Reader, Cold Newcomer, and
  Mobile-One-Hand are floor-seats present on every player-facing build; Screen-Reader and Skeptic
  convene when the build's surface warrants. Keep the table as small as the job honestly allows.

---

## INAUGURAL RUN — choose-your-leader-v5.html (the three-broadcast CYL)
*Convened 2026-07-26. Chair: Playtest PM. Layer-1 state: preship-gate-v4 SHIP, worst pair 5.99. Personas run: Cold Newcomer, RP Reader, Mobile-One-Hand (Skeptic/Screen-Reader pending).*

Convergent finding (all personas, independently): **v5 is a pre/post trust survey wearing a room
costume.** The scene SVG has zero instantiated hotspots (the `.spot`/`.hit` CSS exists but no
hotspot element is ever drawn); "notices" are text chips in the panel; the room never responds; the
promised Maslow descent is dead code (only a two-point pre/post strip ships). The verb (react) sits
behind 3 screens / 4 nav taps. On a phone the room SVG `preserveAspectRatio="slice"` crops the sides
in portrait, amputating the chair-that-is-YOU, the doorway, the window, and the wall map — breaking
the landscape-visible-in-portrait rule on the flagship's core art.

The convergent ruling and the full check ledger for the v6-rectification build are recorded in
`claude_aleph-cyl-integration-2026-07-26.md` and the follow-on build plan. Design nuance held on
the record (RP Reader): the rectification is **presentation, not spine** — adopt v6's felt,
tap-the-room *feel* (touch-to-attend) without importing v6's decide-in-the-fog mechanic; CYL stays
a receiver's instrument.

## IMPROVEMENTS — v-next doctrine (earned from the 2026-07-26 inaugural run)
*How to improve the agentic playtest, from what the run actually did well and badly, crossed with best practice. Each is a CHECK (rich in rules, thin in enforcers: a rule that cannot be a check is a wish).*

**A · Render the play; do not only reason about it.** The inaugural personas *read the code and reasoned* — strong on code-grounded fact (dead `.spot`, orphaned `tier`, the `slice` crop geometry) but *estimated* on rendered fact (chip fold "~500-650px," contrast of JS-produced comfort stops, screen-reader order deferred). Chromium is present; the two-layer law says measurable claims get measured.
→ **CHECK:** each persona pass runs against a Playwright-rendered build (phone + desktop, every comfort stop, OS dark mode); fold position, tap-target px, JS-state contrast, and portrait crop are *measured*, and only the genuinely un-measurable (assistive-tech order, "does it pull") is handed to reasoning and labelled inference. · owner: tooling · when: v-next

**B · Assign distinct primary axes; treat convergence as confidence, not coverage.** All four personas re-found "the room has no hotspots" (redundant); the non-obvious catches — the `reach` line manufacturing the delta, the blind-overwrite integrity hole, Nixon-reveal-inert-to-the-encoded-object — each came from a single seat. Persona diversity exists for coverage.
→ **CHECK:** the Chair assigns each persona a distinct primary axis + scene/beat focus; convergence raises a finding's priority but no persona is credited for re-finding the obvious. · owner: chair · when: each run

**C · Adversarially verify before Ledger A.** The personas flagged their own inferences (honest) but nothing tried to *refute* a finding before it became a blocking check. The WOLF-GUARD / anti-crying-wolf rule, made a step.
→ **CHECK:** every Ledger-A candidate gets one refutation pass (a second agent tries to break it on the actual build); survives = CONFIRMED, else PLAUSIBLE / verify-by-eye. · owner: process · when: each run

**D · The heuristic library grows (provenance is the content).** Today's catches (dead-code descent, blind-overwrite, `slice` crop, hue-only selection) evaporate unless carried. `studio-eyes-two-layers.md`: each firing check becomes dated, attributed, reusable.
→ **CHECK:** `claude_playtest-heuristics.md` is the standing regression ledger; the Table re-runs it first on every build, and every new firing check is appended with build · persona · date. · owner: chair · when: each run

**E · Layer-1-first + honest degradation are preconditions, not courtesies.** This run skipped the mechanical player (`playthrough-agent.py`) before the persona Table — a pipeline-order miss, flagged. The firm-up agent hit a 403 and degraded honestly. Both are the rule: Layer 1 before Layer 2; name the tool/egress failure, never guess past it.
→ **CHECK:** the Chair blocks persona play until `studio-eyes-sweep.py` SHIP + `playthrough-agent.py` CLEAN are on record; any tool/egress/no-device failure is named in the run record. · owner: chair · when: each run

**F · One output contract across the whole apparatus.** The persona agents emitted `verb·owner·date` (because briefed); `playthrough-agent.py` still emits glyph-prose that does not plug into the check tables.
→ **CHECK:** wrap/retrofit `playthrough-agent.py` output into `verb·owner·date` rows so sweep + playthrough + Table all speak one ledger. · owner: tooling · when: v-next

**G · The invariant that must never "improve" away.** Every gain above clears more rubble *beneath* the founder's eyes; none substitutes for them. The agent never judges; it files checks; GATE 1 (founder cold play) + GATE 2 + §6.5 ship (§16.7). And per BUILD-DEBT: this doctrine is a GOV artifact — it earns its keep only when the next player-facing build ships *better* because of it, not when the doc gets tidier.

**Twin-rule note (adding a seat expects a prune):** candidate prune is folding `playthrough-agent.py`'s standalone status into the Table as its mechanical persona (improvement F makes that natural). Left as a founder call; not auto-pruned.

## CORRECTION — 2026-07-26 (append, not rewrite; the 07-22 law)
*Verified against the repo after the founder's SESSION-2026-07-26 handoff. The mapping and improvements above were partly built on a stale reading; the wrong version stays above, the correction lands here so the error and its fix are both visible.*

- **The real Studio Eyes is `studio-eyes/studio-eyes.py` (v3)** — browser-rendered (imports Playwright/Chromium; runs a self-test canary of known-verdict traps, half of them FALSE-POSITIVE traps, and REFUSES to audit if it cannot grade its own canary; README verified). The firm-up mapped `studio-eyes-sweep.py` (WeasyPrint; states plainly "JavaScript is not executed") as the Studio Eyes floor. That is the *secondary, JS-blind* sweep, not the canonical gate. Every reference above to studio-eyes-sweep.py as "Layer 1 / Studio Eyes" should read `studio-eyes/studio-eyes.py`.
- **Improvement A overstated the gap.** Browser rendering already exists: `studio-eyes/studio-eyes.py` renders, and `playthrough-agent.py` already drives the interface. The correct check is NOT "add Playwright rendering" — it is **wire the personas to the existing browser-rendered gate** and stop reasoning about rendered facts the existing tools can measure.
- **`floor.yml` calls the wrong sweep (verified).** It installs Playwright + Chromium + axe-core (lines 47-49) then runs `python3 studio-eyes-sweep.py .` (line 52) — the JS-blind sweep, not v3. Fix = call `studio-eyes/studio-eyes.py`. Writing `.github/workflows/` needs the `workflow` OAuth scope a session lacks; it is the founder's paste (the SESSION-2026-07-26 handoff prepared it — do not duplicate it).
- **The process lesson (the handoff's thesis, now mine on the record): read the index (Funes / Aleph) BEFORE spawning research or build agents.** This session mapped and proposed capability that already existed — the same failure the handoff confesses. Index-first is the cheapest fix; it belongs above improvement E as the precondition to the whole Table.
- **Caveat, applied to the handoff itself (verify, don't trust whole):** commit `13e9b269`, `SESSION-2026-07-26.md`, `studio-fingers.py`, and `gate-baseline.json` are NOT in this branch's object store. The handoff is right on the structural facts above; those specific artifacts must be checked wherever it landed, not assumed here.

---
<!-- SOURCES (house rule: cite, don't guess), web-verified 2026-07-26:
 - LLM agents as automated game testers: arXiv 2509.22170; emergentmind.com/topics/llm-agents-as-game-testers.
 - Persona-based testing surfaces role/expertise/a11y friction generic scripts miss: Tessary; Testriq; Xray.
 - RP = reduced contrast sensitivity, peripheral + night loss; low-vision-primary -> prefer 7:1: Smashing Magazine; PSU Accessibility.
 - WCAG 2.2 SC 1.4.3 (4.5:1 AA), 1.4.6 (7:1 AAA), 1.4.11 (3:1 non-text), 2.5.5 (44px AAA), 2.5.8 (24px AA),
   1.4.10 reflow 320px, 2.3.3 / 2.2.2 motion: w3.org/TR/WCAG22 (numbers from established knowledge; direct fetch 403 via proxy this session).
 Persona internal assignments = Matt directive 2026-07-26; ADA Officer (Section 5.10) and Skeptical Adopter (Section 5.12) reused as players. -->
