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

---
<!-- SOURCES (house rule: cite, don't guess), web-verified 2026-07-26:
 - LLM agents as automated game testers: arXiv 2509.22170; emergentmind.com/topics/llm-agents-as-game-testers.
 - Persona-based testing surfaces role/expertise/a11y friction generic scripts miss: Tessary; Testriq; Xray.
 - RP = reduced contrast sensitivity, peripheral + night loss; low-vision-primary -> prefer 7:1: Smashing Magazine; PSU Accessibility.
 - WCAG 2.2 SC 1.4.3 (4.5:1 AA), 1.4.6 (7:1 AAA), 1.4.11 (3:1 non-text), 2.5.5 (44px AAA), 2.5.8 (24px AA),
   1.4.10 reflow 320px, 2.3.3 / 2.2.2 motion: w3.org/TR/WCAG22 (numbers from established knowledge; direct fetch 403 via proxy this session).
 Persona internal assignments = Matt directive 2026-07-26; ADA Officer (Section 5.10) and Skeptical Adopter (Section 5.12) reused as players. -->
