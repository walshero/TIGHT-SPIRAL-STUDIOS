# OS BLOCK — TIMING BELT v2 (§12 fold-in candidate)
*Tight Spiral Productions · drafted 2026-07-03 evening · status: HELD in the Command Center fold-in queue until the canonical OS settles. Do not fold early.*
*Research-grounded: Google SRE postmortem culture (blameless PIR, action-item tracking), aviation just-culture and checklist discipline (read-do, killer items only), config-drift detection practice, WCAG 2.2 / WCAG 3 status review. Sources named inline.*

---

## WHY v2 (one paragraph)

The v1 belt (six beats, locked 2026-07-03 PM) found things but couldn't yet *prevent* things. Today's first corpus sweep proved the gap: five offline-floor breaks, seven pure-#000/#fff files, and a class-name drift (95 `body.warm` vs. 10 `body.warmdark`) that was silently blinding the auditor — all invisible until a machine looked at everything at once. The industries that solved this (SRE, aviation, healthcare) converge on the same four mechanisms: **automated sweeps, blameless system-focused reviews, tracked-to-done action items, and short read-do checklists.** v2 imports all four.

---

## THE v2 BELT — twelve beats, read-do

*Read-do means: do each beat as it's read, in order, every session close. Killer items only — a beat that stops mattering gets cut at the next belt, not padded around.*

1. **INVENTORY** — what shipped, what's scratch, what's parked. *(v1, unchanged)*

2. **CORPUS FLOOR SWEEP** *(NEW — locked by founder 2026-07-03)* — automated tier-1 pass across every HTML file on the shelf: offline-floor breaks (fetch/localStorage/external resources), pure #000/#fff in any stop (the charcoal floor), banned visibility tokens, missing `:focus-visible`, missing scroll-reset, comfort-gate screens, emoji. Findings triage into: HALT-class (queue for fix), drift-class (beat 3), noise (allowlist). **Known false-positive class:** auditor files that *name* banned tokens self-flag; allowlist them by hand, never by pattern.

3. **DRIFT CHECK** *(NEW)* — compare the corpus against a small canon block: the dark-stop class name (canon call needed: `warm` vs `warmdark` — 95:10 today, founder picks one), palette variable names (`--paper/--ink` vs `--bg/--ink`), file-naming law. Config drift is a named contributing factor in incident analysis; here it literally blinded Studio Eyes. One drift class gets migrated per belt, never bulk.

4. **PHASE-SLIP → BLAMELESS PIR** *(v1 beat, upgraded)* — anything that died between sessions gets the five-question form: what happened / why (system conditions only) / how we responded / what we learned / what changes. **House just-culture rule: the founder is never the root cause.** "Phone-save didn't complete" is a system condition — the fix is environmental (fewer saves needed, an auth that removes the ferry), never "try harder." This is the SRE/aviation import verbatim: fix the environment, not the person.

5. **TWO-LANE LANDING CHECK** *(NEW)* — every artifact produced this session confirmed present in BOTH lanes: outputs (phone-save lane) and Drive Claude_files (autonomous lane). Byte counts reported. An artifact in one lane is not landed.

6. **PIPELINE LANES VERIFY** — which lanes moved, which stalled. *(v1, unchanged)*

7. **ACTION-ITEM AGING** *(NEW)* — every open item carries a last-touched stamp. The documented failure mode across industries: postmortems produce action items that quietly dissolve into a backlog. House rule (extends the accumulator decay rule, OS §5.4.5.1): an item untouched for **three belts** goes to promote-or-kill — no third state. Action items are owned and dated at creation, split mitigative (fixes this instance) vs. preventative (fixes the class).

8. **76%+ AUTO-FIXES** — one improvement graduates per belt. *(v1, unchanged; the rate governor holds)*

9. **RESEARCH-FIRST GATE** *(NEW — founder order 2026-07-03: "Again, research first")* — extends Just-in-Time Expertise (OS §, standing law) from *build* decisions to *system* decisions: no new standard, threshold, or process is adopted at the belt without a live pull of current domain practice first. **Worked example, same day:** APCA contrast nearly became a Studio Eyes gate on training-data priors; the pull showed W3C removed APCA from the WCAG 3 spec in July 2023 and it remains exploratory — so it entered as an advisory low-vision lens only, with WCAG 2.2 AA as the sole HALT. The armchair answer was plausible and would have been wrong law.

10. **ALEPH ONE-PAGER** — "why aren't builds moving?" *(v1, unchanged)*

11. **MEMORY SYNC** *(NEW)* — belt close writes the delta to Claude memory (memory = index) and the Command Center on Drive (files = truth). A ruling that lives only in a chat is not a ruling.

12. **RECOVERY DRILL** *(NEW, every fifth belt)* — pick one thing believed "lost" or "somewhere," prove it findable via conversation_search or Drive search, time it. Imported from SRE disaster role-play: a recovery muscle that's never exercised fails when needed. Tests the lost-thread rule under load.

---

## FIRST CORPUS SWEEP RECORD — 2026-07-03 (the evidence base)

- **Offline-floor breaks (5):** confluence-TRUNK.html, confluence-TRUNK-2026-06-23.html, confluence-walkthrough.html, recursion-ledger.html, studio-eyes-auditor.html *(auditor = false positive — it names the tokens it hunts; allowlisted)*. Confluence family verdict needed: institutional-lane tools may be exempt from the offline floor by design — founder call.
- **Pure #000/#fff (7):** assignment-auditor, confluence family (3), paper-1-draft, studio-tour-for-massbay, tight-spiral-studio-face. Charcoal floor has no enforcer until Studio Eyes v2 ships.
- **Dark-stop drift:** `body.warm` 95 occurrences vs. `body.warmdark` 10. Canon pick queued (beat 3).
- **Comfort-gate screens (grep-class):** behind-this-door *(shelf copy is stale v1 — v3 in hand removes the gate)*, the-compound-capstone, network-strategy-spec, confluence family. Probe Sweep list confirmed.
- **Scroll-reset missing:** 12+ files including choose-your-leader-full and elves-house.

## QUEUED BUILDS THIS BLOCK CREATES
1. **Studio Eyes v2** (single-file auditor rebuild): both dark-stop class names, silent-skip HALT, charcoal-floor check, 44px targets, APCA advisory lens, sweep-in-one-paste. *(Next belt's graduated improvement — commissioned, not yet cut.)*
2. **TSP Academy** (per-seat retraining charter against the corpus): folds into the belt as a periodic beat — every N belts, one seat re-trains on the full shelf and files an upgraded charter + one optimal-pathway recommendation. The corpus sweep above is the Academy's tier-1 curriculum, already running.
3. **Canon block** (machine-readable: dark-stop class, palette tokens, naming law) — small file the drift check reads.

## PROVENANCE
Blameless PIR, action-item ownership, and disaster role-play: Google SRE Book & Workbook (postmortem culture chapters). Just culture: aviation/healthcare origin of blamelessness. Read-do checklist discipline: aviation practice (Gawande's account). Config drift as contributing factor: standard incident-analysis taxonomy. WCAG 2.2 AA as current legal standard and APCA's removal from the WCAG 3 spec (July 2023, still exploratory): W3C + April 2026 status analyses. All pulled live 2026-07-03 per the Research-First Gate this block creates.

*End of block. Folds as OS §12 (or merges into the belt section) in one pass at the canonical settle — it does not touch the OS before then.*
