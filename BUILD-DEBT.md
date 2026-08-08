# BUILD-DEBT.md — the governance rate-limiter

**One job:** stop the studio from shipping governance faster than product.

The named failure mode (already in memory): **SPEC-RICH, BUILD-POOR.** Every
session ends cleaner and adds one more rule, and that *feels* like progress. It
isn't. A player gained nothing.

This file makes the anti-rabbit-hole rule itself a check. "If a rule can't be a
check, it's a wish" — here is the check.

---

## THE RATIO RULE (the only rule in this file)

> **No session may add a governance artifact — a rule, an OS block, a seat, a
> gate, a tick, a script — unless the PRIOR session shipped a player-facing
> capability.**

Governance is rate-limited by shipping. Debt must be paid before more is drawn.

- **Ship** = a player/student/institution can now DO something they could not do
  before, AND it passed the ship gate (GATE 1 founder cold phone play → GATE 2
  Studio Eyes), AND it rendered on Matt's actual device.
- **Governance** = anything in the meta-layer: rules, OS blocks, seats, gates,
  ticks, sweep scripts, manifests, canon docs.
- A spec is **not** a ship. A parked artifact is **not** a ship. "Basically done"
  is **not** a ship.

---

## THE PUSH RULE (fidelity is a check, not a wish)

Every file written to the repo through the Zapier lane is verified by blob sha,
because that lane is **functional-exact, not byte-exact** — it strips comment and
blank lines in transit, and the CDN cache + markdown reads both lie on readback.
The blob sha is the one readout that cannot be faked.

> **Before an oversized or canon-comment push: `lane-fidelity.py plan <file>`.
> After: `lane-fidelity.py check <file> <sha-git-returned>`. MATCH = ship.
> DIFFER = HALT and decide (PAT re-push for byte-exact, or accept the strip on
> purpose and re-run the artifact's own gate on the repo copy to prove logic
> survived).**

`"created: true"` is never proof. The blob sha is.

---

## SESSION-OPEN CHECK (fires with the three seats)

Read the last two lines below. If the most recent line is `GOV` and the one
before it is not `SHIP`, then **THIS SESSION BUILDS. Full stop.** No new
governance until a capability ships.

## SESSION-CLOSE LOG (one line, append-only, newest at bottom)

Format: `DATE | SHIP or GOV | what a player can now do (or what governance was added) | FAC:N`

**FAC = Founder Attention Cost** (instrument adopted 2026-08-08, from the OpenAI
lane's independent assessment — its best original finding). Count the founder's
actual *judgment calls* this session required: decisions only he could make
(merge this, kill that line, approve this spend). Not messages, not approvals of
mechanical work, not Claude operations. The studio's stated goal is quality ×
originality × throughput UP while founder-judgment-per-shipped-unit goes DOWN —
this is the first instrument that measures it instead of asserting it. A session
whose FAC climbs while its SHIP count doesn't is inverting the architecture.

```
2026-07-19 | GOV | added BUILD-DEBT.md ratio rule. DEBT +1. Next session owes a build.
2026-07-19 | SHIP | preship-gate-v4.py render-proof teeth: the gate now catches the class where a screen passes at 13:1 and renders unreadable on Matt's retina (opacity floor + RP warm-hue floor). A builder can no longer ship a gold-on-unpainted screen the old gate green-lit. Canaried: your-rp-world HALTs, viscosity SHIPs. DEBT paid.
2026-07-19 | SHIP | choose-your-leader-v6.html (the assessment flagship, worst file in the corpus sweep) now renders legible in all three comfort modes: default label cooled off gold, softer+daylight teal/rust darkened to clear 4.5, a malformed daylight hex removed. Gate v4 SHIP, worst pair 4.87, verified on the repo copy after push. A student can now read the CYL scene in every comfort stop.
2026-07-19 | SHIP | the-console.html role clarity + Post→Boost verb fix (the standing coherence-gate blocker named in the opportunity bridge / GALA workback). Round 1's button no longer reads "Post" (which implied the player posts content); it reads "Boost" and every tap now lights a heart on a feed post, so the operator's act reads as acting ON the feed. Each scene now carries a job-posting-style assignment brief ("Growth Operator · Assignment N / 5") naming what the player is doing to users that round. Telemetry label updated to match. Verified end-to-end in headless Chromium (brief renders, Boost fires, hearts light, no JS errors). A player now knows their role in every scene.
2026-07-21 | SHIP | preship-gate-v4.py v4.1 flip-check contrast guard: the gate stopped false-halting correctly-inverted mid-tone palettes (it was banding lum-0.30–0.48 grounds as "mid" and flagging good work). Now it asks the real question — does the text clear 4.5 on any surface in that mode — before crying H-FLIP. Verified byte-exact on the repo copy via blob sha 52edb293, canary suite 4/4 correct. A builder's clean inverted palette no longer gets blocked by a phantom.
2026-07-21 | GOV | lane-fidelity.py + THE PUSH RULE: file-fidelity is now a deterministic check (git blob sha), not a hand-done readback that got skipped. plan-before / check-after. Self-verified its own push byte-exact (blob 5f72b7be). Permitted: prior three lines are SHIP.
2026-07-22 | SHIP | the-console.html (Flok) mobile-first pass: comfort is now a single "Comfort" button that opens the display options ON TAP and is never shown unasked (founder floor "comfort is a knob, not a wall," sharpened — even the knobs stay hidden until summoned; panel dismisses on outside-tap/Escape). Home/back nav raised to the 44px touch floor — fixed in the shared tsp-mobile.js source too, so every game inherits it on re-inline. Verified on a 412px touch viewport: panel hidden→opens→closes, options toggle, Boost fires, 0 console errors; ratchet floor holds. A thumb can now run Flok.
2026-07-22 | SHIP | dad-energy.html play fixes: (1) the "Stall" scene no longer contradicts itself — the castle is finished and its paint just needs ten untouchable minutes to dry, so keeping the child busy (read/negotiate/spin a tale) is the whole job, not building-while-reading; (2) collapsed the redundant per-stage flow — the choice feedback and the castle's next piece now share ONE screen instead of a feedback screen followed by a separate build screen; (3) raised its inlined home nav to the 44px touch floor. Verified: full 5-scene playthrough, castle rides each choice screen, ending "The castle held." renders, passes Studio Fingers, 0 console errors, ratchet floor holds. Fewer taps to the same ending.
2026-07-22 | GOV | studio-eyes/studio-fingers.py — the touch wing of Studio Eyes. Renders each page on a 412px phone and HALTs on sub-44px tap targets (F-TAP), sideways scroll (F-VIEWPORT), missing meta-viewport (F-METAVIEW), and comfort options shown unasked (F-WALL). Self-test discriminates: GOOD canary clean, two bad canaries catch all four codes. It caught Flok's own 28–31px nav links before this pass fixed them. Permitted: prior line is SHIP.
2026-07-26 | SHIP | old-problems-at-new-speed.html repaired via the 3-lens diagnostic (TSP tools + game-heuristics agent + media-frameworks agent). Unanimous fix: comfort is now a single button that opens the display options on tap, never a wall (was 4 controls front-loaded before the scene). Plus: garden logic bug fixed (exactly one path taken, never both), scene switched to dvh. Verified: passes Studio Fingers, comfort knob works, 0 console errors, ratchet holds.
2026-07-26 | GOV | studio-fingers.py F-WALL hardened + os-block-aleph-diagnose-repair.md. The paper exposed a blind spot (F-WALL matched label-words only, missed "Warm-dark/Dim the room/Default"); added container-based wall detection (comfort/theme container, 2+ controls, no toggle). Re-verified: catches the paper, still passes Flok/Dad Energy real toggles, self-test green. Protocol doc captures the 3-lens diagnose->synthesize->repair loop. Permitted: prior line is SHIP.
2026-08-07 | GAP | this log went unappended for 12 days and 58 commits (found by the Aleph consultation panel's architect seat, re-measured via `git log --oneline --since=2026-07-26`) - the ratio rule cannot fire on a log it was never updated to read. Not backfilled commit-by-commit; that would be presumptuous reconstruction of sessions this one wasn't present for. What's true and checkable: real capability shipped in that window (en195-arcade icon set + differentiated coin/token feedback, ISLO touch-floor fixes, softer-stop contrast root-cause fixes) alongside real governance (FUNES ledger tooling, TSP-NOTOKEN-LANE, comfort-audit.mjs's dark-stop blind-spot fix). The honest state: mixed, unlogged, un-auditable until now.
2026-08-07 | GOV | ticks 3-5 on the studio belt (image floor, founder voice, entry paint - each a founder ruling with a working gate that nothing had wired into CI), the Aleph Fleet (aleph-fleet.py, aleph-taxonomy.json, 5 lens briefs, os-block-aleph-fleet.md), and two six-month consultation panels (one inline, one true-blind 5-agent rerun) - the heaviest GOV stretch on record. Named plainly by two independent panel seats as itself in violation of this file's own ratio rule. The next entry is the debt paid.
2026-08-07 | SHIP | playthrough-agent.py's cross-page navigation bug fixed - it clicked <a href> nav links and kept walking whatever page they led to, attributing everything found there to the ORIGINAL file's report (the-tell.html was reported with "3 dead buttons" that were actually the-console.html's and old-problems-at-new-speed.html's content, bleeding in). Also fixed: mailto:/tel:/sms: links falsely flagged as dead buttons and offline-floor violations (they correctly leave the DOM untouched - that's not a defect). Verified: self-test still catches a real dead button and clears a clean game; the-tell.html re-run now reports CLEAN. Corrected the false DEAD-CONTROL entry this bug produced in aleph-ledger.json rather than leave it standing. the-tell.html's real bug (found independently by 3 Aleph lenses) fixed too: "Read it the other way" called state={}, silently wiping every tagged read and typed why with no confirm on every lens switch. Now per-lens state (ALL_STATE{writerly,workshop}), never reassigned. Verified behaviorally in a live browser: tag a spot, switch lenses twice, "1 of 3" survives - was "0 of 3" before. Gates still pass (preship-gate-v4 SHIP, one-thing-gate PASS debt-carried). en195-apps' offline-floor break also fixed (Google Fonts link removed, existing fallback stacks already declared on every rule now render instead) - its belt had been red since 2026-08-04; verified green. A player can now switch reading lenses on The Tell without losing their work, and three fewer tools in the corpus report defects that were never there.
2026-08-08 | GOV | CI merged into one workflow with real teeth (floor.yml absorbed studio-belt.yml, `if: always() &&` removed so a failing floor actually blocks deploy), all 13 os-block-*.md files reconciled into the OS text with two real numbering collisions found and fixed, STUDIO-COMMAND-CENTER.md refreshed after three-plus weeks stale, and canon-freshness.py added (report-only, wired into floor.yml) so the exact bug class hand-fixed three times tonight - a resident doc's own status header asserting a state reality had already moved past - gets caught mechanically next time instead of by manual re-discovery. Permitted: the next line is SHIP.
2026-08-08 | SHIP | islo-hub.html's instruction-wall paid down worst-tractable-first: the "how to read a station" explainer and coverage-key legend moved below the seven stations instead of stacked above them - same content, nothing cut, just reordered so the real game links come first. 301->193 words before the first action, 2.56->1.98 screens on phone (INSTRUCTION-WALL-QUEUE.md updated to match; fys_fys-treasure-trove.html, the worst entry, left alone and annotated - it's a 9-chapter instructional resource where the wall IS the content, not misplaced chrome, and cutting it is the founder's editorial call, not a layout fix). While diagnosing this file also found and fixed a real bug in one-thing-gate.py: its EMOJI check matched the copyright and registered-trademark signs (a genuine Unicode Extended_Pictographic quirk), false-flagging legitimate AAC&U rubric attribution as emoji on 5 corpus files. Re-baselined all 5. Verified against a full belt run before landing (BELT: PASS, all ~130 surfaces) since the gate itself changed. A faculty reader on islo-hub.html now reaches the first game roughly a third sooner.
2026-08-08 | SHIP | CYL's retired spine line ("you don't judge the leader...") removed from all four live surfaces it was still shipping on, three weeks after the founder's objection was recorded-but-unenforced; specs that would regenerate it corrected; merged to main, belt-gated deploy verified green end to end (first live run of the re-coupled CI). A player no longer reads a line the founder never approved. | FAC:4 (merge call, "both" on the open items, the tagline kill, "build to last")
2026-08-08 | GOV | belt tick 6 (retired-lines-gate.py, zero tolerance, self-tested) - a founder objection is now a mechanical check, not a ledger memory; + cross-lane tendrils (lane-tendrils.json, funes-tendrils now names the 5 lanes no CI sweep can walk, loudly, every run); + the Panelist Union Rep seated in the OS (seats must scrub in or draw grievances - the pruning signal panels lacked); + FAC instrument adopted into this log's own format. Permitted: prior line is SHIP. | FAC:2 (union-rep design call, lane-tendrils scope call)
2026-08-08 | GOV | EXTERNAL-ASSESSOR-BRIEF.md - the anti-stale handoff for outside consultants, built from the failure the first external assessment (OpenAI lane) demonstrated: it graded July's studio in August because nothing told it where truth lives or how to check freshness. The brief is method-not-state (freshness check first, ignore-list of known stale caches, 8-file reading order, delta table against the July grades, engagement rules: cite-or-decline, test enforcement not documentation, respect the founder gate, weigh cost). Registered in canon-freshness.py's resident-doc roster so its own pointers are CI-checked. Founder-ordered; prior SHIP stands. | FAC:1 (the order itself)
2026-08-08 | GOV | Union Rep advocacy weight raised (founder-ordered - this and the prior line are founder governance spends, not Claude's reflex; the ratio rule limits the reflex, the founder's gate is his own). The Rep's charter grows from participation-integrity watchdog to informed advocate: CAUCUS duty (consult the OS benches, patterns, ledger, the standing wings - prop room, Elves' House, eyes/fingers, tendrils - and the grievance record before any bench is proposed), ADVOCACY WITH AGENCY (the Rep proposes the bench and argues for underused talent and mountable standing assets, accountably - Rep-seated seats are recorded so the ledger can show whether they scrub in at a higher rate), plus the existing roll call and grievances. Designated agent form created at .claude/agents/union-rep.md - a real spawnable agent definition, caucus sources and hard boundaries in its own prompt (one agent never a fleet, no craft verdict, cite-or-decline, cost discipline binding). | FAC:1 (the weight-raise order)
2026-08-08 | GOV | HITL producer packet (HITL-REVIEW-2026-08-08.md, founder-ordered delivery verification, not new capability - hence GOV not SHIP; the SHIP is GATE 1's to confirm): CYL (for Scot) and Funny Boneys (for Peter) candidates run through all six ticks + Fingers + the playthrough walk, everything green; the Union Rep's first real convening (inline, bench-and-scrub-in table in the packet, zero grievances); the Funny Boneys fork divergence caught (root v6 = the deliverable, studio/ fork has the newer kernel but fails the touch floor); and a third playthrough-agent false-positive class (already-active toggles read as dead buttons) caught by refusing to take the tool's word, fixed at source with selftest proof. PENDING founder: which CYL build(s) to Scot; kernel-port-to-root call; GATE 1 verdicts - FAC for those accrues when the calls come in. | FAC:3 (the delivery order; the phone-first rule; the make-work-stick rule)
```

---

## SUNSET CLAUSE (Chesterton's Fence, inverted)

Before adding any governance artifact, remove one that never fired. Any rule,
seat, or gate that has not triggered in 5 logged sessions is archived to
`governance-attic/`. A rule nobody runs trains everyone to ignore the ones that
matter.

---

## WHY THIS IS THE FORCING FUNCTION

Memory already says NEXT SESSION OWES A BUILD. This file is that sentence with
teeth: it survives the chat, it fires at open, and it blocks the reflex that
keeps winning — ending the session with a tidier OS instead of a played game.

Borrowed from: Kanban WIP limits (cap governance-in-progress), Scrum Definition
of Done (DONE = rendered on Matt's phone, not gate exit 0).
