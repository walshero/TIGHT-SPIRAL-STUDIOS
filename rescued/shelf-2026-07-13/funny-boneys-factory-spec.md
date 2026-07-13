# Funny Boney's Factory — Game Design Document (v2)

*Tight Spiral Studios · walshero@gmail.com*
*v1 captured 2026-06-30 from a founder voice session. **v2 revised 2026-06-30** against the current OS + pipeline + Studio Eyes. Read alongside `tight-spiral-studio-os.md` (governing) and `tight-spiral-pipeline.md` (sequencing).*

> **What changed v1 → v2, in one screen** (the rest of the doc is the detail):
> 1. **Floors re-sorted into the two tiers** (OS §5.6, revised 2026-06-30). v1 listed accessibility as one flat "always-on floor." It isn't anymore. Hard walls (emoji / trauma / FERPA) vs. best-practice defaults (contrast / motion / palette / type — ship safe, then a reachable toggle). This is the single biggest governance change and it reshapes how the build ships.
> 2. **"Human out of the loop" → resolved as maximum *agent autonomy on the mechanical*, human gate intact on judgment.** Optimized exactly as far as the OS allows and not one step further — see §0.5. This is a hard ruling, not a preference.
> 3. **Recursive interviewing: locked** (was "being locked" in v1). The prior linear-intake assumption is formally removed.
> 4. **Recursion loop wired in** (OS §6.2.5): the game now ships with a Harvest-back, an auto Probe Sweep on its own failure-class, and a one-graduates-per-build governor. The *game that teaches calibration* is itself governed by the studio's calibration loop — same shape, two scales.
> 5. **Look is not specified here** (OS Visibility correction). Palette/composition chosen fresh per build by the design seats from this game's rhetorical situation. v1 didn't over-specify look; v2 makes the silence deliberate and names who decides.
> 6. **Five-bin gate outcomes + PIVOT** replace go/stop throughout.

---

## 0. Origin

The seed came from **Peter** (FableVision — Matt's collaborator from his sabbatical residency and after, at Learning Games Network, the MIT spin-off). Matt described the whole Tight Spiral Studios system and said, in effect, *"a game that does X."* Peter answered: *"a game for kids that makes them laugh."*

So the design is a game that **makes kids laugh — and teaches them about laughter.** Underneath the laughter, it teaches calibration, collaboration, systems thinking, and real-world problem solving. The humor is the door; the calibration is the room.

---

## 0.5. The "human out of the loop" ruling (NEW — read before optimizing anything)

The founder's instruction was to **"optimize the specs for human out of the loop."** Run honestly through the OS, that instruction splits into a part the studio can do fully and a part it cannot do without breaking a locked floor. The optimization is legal up to a hard line, and the line is named so it isn't crossed by accident later.

**What "human out of the loop" legitimately means here, and is fully optimized for:**
The pipeline's standing shape is `agent pre-flight (mechanical, binary) → human gate (judgment) → emit` (OS §6 preamble; §8 delegation map). "Human out of the loop" = **push every mechanical, spec-able, no-judgment task off the founder's plate to the agent, so the founder's scarce attention touches only meaning.** That is the studio's own goal stated in §2 (attention scarcity) and §8 (delegate the mechanical). This spec maximizes it: every box in §6.5 below that *can* run agent-autonomous is marked and handed off.

**Where the line is, and why v2 does NOT cross it:**
Three things in this game make "remove the human entirely" illegal, and two of them are *hard walls* that cannot be toggled:

| The thing | Tier | Can it go human-out? |
|---|---|---|
| **No dirty data / opt-in transparency** (the game gathers real human laughter feedback) | Hard wall (FERPA-adjacent + the game's own locked floor §4) | **No.** A data-gathering game with no human accountable for what's gathered is the exact disease this studio walls off. |
| **Trauma-informed safety on surveyed humans** (kids are surveyed and survey each other) | Hard wall | **No.** Forced disclosure / ambush protection cannot run on autopilot. |
| **"Human-in-the-loop is visible. Label the moves."** (founder-locked floor, §4) | Founder floor | **No** — but it can be *cheaper*: the human gate stays, the mechanical prep around it goes fully to the agent. |

**The ruling (locked this revision):** the build is optimized for **maximum agent autonomy on the mechanical and zero founder labor on anything spec-able**, while the **judgment gate on data, safety, and "is this calibration signal real" stays human and stays visible.** This is not a hedge — it is the optimization the OS permits. Anything past it would require the founder to consciously unlock a hard wall, which a spec revision is not allowed to do on its own.

> Plain version for the founder: *I pushed everything I legally could off your plate. The agent now preps, drafts, codes, sources, and checks. You are left with exactly four judgment calls (§6.6) and the data/safety gate. I did not auto-remove the human from the data-gathering and child-safety seats, because those are walls, not preferences — and the spec can't unlock a wall for you. If you want them unlocked, that's a founder call you make on purpose, out loud.*

---

## 1. The one-sentence version

Kids build Rube Goldberg machines to make people laugh, survey real people on what landed and what didn't, use that feedback to redesign — and in doing so learn calibration, transparency, and systems thinking while modeling a solution to a genuine real-world problem.

*(Spine, unchanged. This is the line that PIVOT watches: if the one-sentence answer to "what is this?" changes, the build drops to a re-spine before anything else proceeds — OS pipeline.)*

---

## 2. The core loop

1. **Build** — the player assembles a Rube Goldberg machine meant to make someone laugh. They have tools, and can use tools to make the tools they need. Basic physics and sound are in play. The machine is built *for an audience*, never in silence.
2. **Test on people** — the machine is shown to others. What lands? What doesn't?
3. **Survey** — the player gathers real feedback: what made people laugh, what fell flat.
4. **Recalibrate** — the player uses that feedback to redesign — tightening the machine toward the best possible laugh.
5. **Share & stack** — an easy copy-paste path lets players socially share their machines, stack them, and combine them into giant collaborative Rube Goldberg machines.

The loop *is* calibration: predict what's funny → build → measure the gap → close it. Humor is empathy plus iteration, made playable.

**Persistence (the Carry-Out, NEW in v2 — was implied, now explicit):** the share/stack step is an **emit-and-carry**, not server storage. A single offline file can't store across sessions, so the player **chooses to copy their machine out** (a paste-able record), FERPA-clean and consent-first. Stacking is the player pasting one carried-out machine into another's. *Don't store; emit.* This also resolves §11's "how do stacks scale" without a backend.

---

## 3. What it teaches (and measures)

- **Calibration** — the core construct. Noticing the gap between predicted-funny and actually-funny.
- **Collaboration / team-building** — consensus and shared design.
- **Principles of science / basic physics** — momentum, cause-and-effect, chain reactions, sound.
- **Systems thinking** — a machine is a system; a stacked machine is a system of systems.
- **Real-world problem solving** — see §5.

The measurement maps to **grade-school principles teachers can love**, and the mapping **adapts to the viewer** (§6, the dashboards). The game is calibration practice *and* a live site for learning **how to build better calibration instruments.** Both layers run at once.

**Construct discipline (OS Stage 1 — sharpened in v2):** the construct that ships in MVP is **calibration, and only calibration.** Defined before content, measured by **computed evidence, never self-report**: the construct is the *delta between the player's predicted laugh-rating and the surveyed actual* — a number the game computes, not a feeling the player types. Collaboration and real-world-problem-solving are real teaches but **park until the calibration signal is proven clean** (the Drift Fork governs their return). This is the answer to v1's open "Claude" panel question.

---

## 4. Founder principles (the floors — RE-SORTED into two tiers, per OS §5.6 revised 2026-06-30)

> v1 listed these as one flat "locked floors" block. The OS no longer treats them flat. Sorting them correctly is what keeps the build from HALTing on a setting the user could simply change — and keeps the genuinely un-toggleable ones un-toggleable.

### Tier 1 — HARD WALLS (never optional; HALT production; protect *other people*)
- **No emoji. Ever.**
- **No dirty data.** The studio announces what it's doing at all times; players always know what is gathered and why. *(This is a wall because the game gathers real human feedback — it protects the surveyed people, not the player's comfort.)*
- **Opt-in on any data gathering**, and the **gate adapts rather than hardening into a barrier** — but the opt-in itself never disappears.
- **Trauma-informed safety** on every surveyed human: no ambush, no forced disclosure, always an exit. *(Kids survey kids — this is load-bearing.)*
- **Human-in-the-loop is visible. Label the moves, never hide the algorithm.** *(Founder-locked. The §0.5 ruling lives under this.)*

### Tier 2 — BEST-PRACTICE DEFAULTS (ship in the safe state, then let the person override)
- **Contrast / visibility:** ship high-contrast by default; offer a reachable contrast/palette toggle. **Green-free in any primary or structural role stays a requirement** (it's an accessibility fact about the founder's eyes, not a palette taste — OS Visibility floor).
- **Reduced-motion:** ship calm by default; let the person turn motion up or down. *(The joy-flourish clause: charm defaults on with a replay control; legibility/large-type/no-strobe still hold unconditionally.)*
- **Type size, palette, the sensory comfort settings:** safe default + reachable toggle. The control is discoverable, never hidden mid-screen, never a gate-first screen. Every reachable state still passes the usability floor (Bounded-Choice Law: toggles roam, the usability floor walls).

### Not a wall, a strong craft default
- **Scene-first / feeling-first opening:** the game opens by landing the player in a scene (a machine mid-chain, something about to be funny) — proven to land before the mechanic behind it is built. Strong default, craft guidance, not a production-stopping wall.

### The look is NOT specified here (OS Visibility correction, 2026-06-30)
Palette, composition, type personality, and overall look are decided **fresh, per build and per screen**, by the **Visual Designer, Rhetorical Grammarian, and Art Director**, driven by *this game's* rhetorical situation — a factory that makes laughs. The standing brief is **novelty and impact: surprise the founder, aim for the look that makes him laugh.** Reusing a prior build's look "because it's the studio style" fails the brief. This doc deliberately says nothing about what it looks like.

---

## 5. The real-world problem layer (the transfer move)

Under the hood, while learning these skills, players tackle a **complex real-world problem.** Launch example: **robotics + sustainable agriculture.**

Part of the spec: **identify a genuine real-world problem where robotics + agri-farming is problematic**, then have players design systems that help overcome it, grounded in a real situation. The Rube Goldberg machine they think they're building for laughs is secretly modeling a real systems-design challenge.

**Gee's open question (carried, with a v2 default proposed):** how explicit is the connection? **Proposed default for founder sign-off:** *hidden until noticed, then nameable.* The player builds to laugh; the real-world model runs underneath; a **"show the engine" ring** (the studio's Glass-Engine pattern) lets a curious player surface the connection on demand. This honors Freire (problem-posing, never depositing) and the Glass-Engine floor (label the move, never hide the algorithm) at once. **Founder call #3 in §6.6.**

---

## 6. The four user dashboards

Four users, four dashboards:
1. **Play** — build and laugh.
2. **Learn** — guided tutorial.
3. **Gather** — view the calibration signal.
4. **Design** — contribute to the spec (the recursive-design layer).

**MVP ships Play + Learn.** Gather and Design graduate once the calibration signal is proven clean.

**v2 adaptation (the viewer-adaptive mapping):** the same calibration data renders differently per dashboard — a kid sees "did people laugh?", a teacher sees grade-school physics + calibration principles, a designer sees the instrument. This is the studio's **adaptive-publishing method** (the artifact reshapes to the reader). One signal, four reads.

---

## 6.5. Pipeline placement + the agent-autonomy map (NEW — this is the "human out of the loop" optimization, made concrete)

The build's current pipeline position and **exactly who does each stage** under the §0.5 ruling. `A` = agent runs it autonomously (human-out of the mechanical). `H` = human judgment gate (stays). `A→H` = agent preps, founder judges meaning.

| Stage | What happens | Who |
|---|---|---|
| **−1 Intake** | Sorted **build now**. Displaces: the next content-heavy game (CYL stays the headline; this is the kids' lane). Names what it displaces ✓ | **A** (sort is mechanical; founder already greenlit) |
| **0 Medium & Novelty** | Medium Gate; name the one structural surprise | **A→H** — agent runs the gate + drafts the novelty claim; founder confirms |
| **0.5 Panel** | Convene the seats (done — §9) | **A** preps dossier, **H** already convened |
| **1 Construct** | Calibration = computed prediction-vs-actual delta; not self-report | **A** drafts the evidence model; **H** signs it's the real construct |
| **2 Task spine + Freedoms** | Build-a-machine = a Move-Things/Combo task (high transfer); freedom-to-fail non-negotiable | **A** |
| **3 Spec + Fidelity checklist** | Lock parameters, wireframe, sign the Fidelity checklist | **A→H** — agent drafts and signs the mechanical lines; **founder signs the meaning lines** |
| **4 MVP build (the hinge)** | One Rube Goldberg editor; the build→survey→gap→iterate loop; Play + Learn only | **A** builds against the signed spec |
| **5 Playtest (two ledgers)** | Ledger A Fidelity (binary, agent-run CLEAN/HALT). Ledger B Emergence (captured). | **A** runs Ledger A pre-flight; **H** plays once, two questions |
| **6 Work-up (Paper Craft)** | Graduates only behind a proven mechanic; C1–C5 | **A→H** — gated behind the §6.6 art-graduation calls |
| **7 Ship + Harvest + Harvest-back** | Name what it proved, what it got wrong, Probe Sweep, retire superseded files | **A** drafts harvest; **H** confirms |

**The Medium Gate result (Stage 0, run in v2):** three lanes, no default. A Rube Goldberg machine for kids is **physical, kinetic, sound-driven, and stackable** — **Lane A cut-paper SVG** is the load-bearing recommendation (skin-tone-neutral inclusive, the prop carries the role, fully buildable offline, and flat cut shapes read cleanly under the green-free contrast floor). Synthesized Web Audio (CC0-by-construction) carries the sound. Founder confirms (§6.6). *Never grind one medium toward what another does.*

---

## 6.6. The founder's judgment gates (THIS is your plate when you're back — everything else is handled)

Per §0.5, the agent has taken everything mechanical. You are left with judgment only. Four calls + the standing data/safety gate:

1. **Construct lock:** MVP ships calibration-only (collaboration + real-world-solving park). Confirm or re-sort. *(Agent recommends: yes. ~80% sure you'll agree — it's the only construct with a computed, non-self-report evidence model ready, and the OS forbids shipping more than one unproven construct at once. Below the 75% auto-threshold only because construct-choice is genuinely yours, so it's a real fork, not a rubber stamp.)*
2. **Medium lock:** Lane A cut-paper SVG + synthesized Web Audio. Confirm or override. *(Agent recommends Lane A. ~85% — it's the only lane that satisfies inclusive-default + green-free + offline + stackable at once.)*
3. **Transfer explicitness (Gee's question):** hidden-until-noticed + a "show the engine" ring. Confirm the default or pick build-to-laugh-first vs. solve-first. *(Real fork — ~60%. This one shapes the whole feel; bringing it to you, not deciding it.)*
4. **The real-world problem itself:** "robotics + agri-farming" is the *example*; the *specific genuine problem* still needs naming. Only you (or a sourced subject-matter expert via the Field Scout) should name it. *(Not auto-decidable — it's a content-truth call with real-world stakes.)*

**Standing gate (never auto):** the data-gathering + child-safety + human-in-the-loop-visible wall (§4 Tier 1, §0.5). Stays yours, stays visible.

---

## 7. Artist-in-the-loop + attribution (delegate to legal — Provenance Floor)

The game includes an **artist-in-the-loop intake** so artists contribute their own art, built to fit the OS, with transparent labeling of who made what. An **attribution system covering all legal content** is required — **for the lawyers, not the founder**; a legal-panel seat owns it.

- **License rule (founder, locked):** usable Creative Commons only. **No-Derivatives (ND) excluded.** Use what we legally can, sights and sounds.
- **Provenance Floor (OS):** no asset (art or sound) enters without recorded legal provenance — source, license, attribution, how it entered. No scraping. No guessed attribution. Enforced by `provenance-ledger.html` + a Studio Eyes check.
- **v2 note:** artist intake is **not in MVP** (§10). It graduates with Gather/Design. When it does, every contributed asset routes through the provenance ledger before it can render.

---

## 8. Recursive interviewing (studio method — NOW LOCKED into the OS)

The intake method is **recursive interviewing / recursive chatting**: founder surfaces ideas → fed to the panel → panel asks follow-ups based on what was said → the loop tightens each pass. Replaces linear Q&A.

**v2 status change:** v1 said "being locked into the OS." **It is now locked** as a studio decision, and the **prior linear-intake assumption is formally removed.** This very revision was produced by it: the founder's voice dump → panel review → follow-up questions surfaced as the §6.6 founder calls, not a flat questionnaire.

---

## 9. The panel (who reviewed this) + the v2 re-review

Convened 2026-06-30 for v1: **Claude** (studio/Conductor), **Scot Osterweil** (ludic design — Four Freedoms, no jargon on surface), **Jim Gee** (situated learning, the transfer move), **Horvath** (mechanics, physics fidelity), **Jane McGonigal** (social systems, stacking, consensus), **Sherry Turkle** (human-in-the-loop, transparency).

**Conductor frame:** ludic pedagogy + social transparency + consensus-based iteration. *Not* a skill-assessment game (assessment seat dormant — calibration lives in play first; a rubric comes later if Confluence adopts it). *Not* competitive (stacking is collaborative, not ranked).

**v2 re-review verdict (the seats run against the optimization itself):** see §12 for the full recursive pass. Headline: the panel passes the v2 optimization with **two CONDITIONAL GOs** and zero KILLs. The conditions are folded into §6.6.

### Open panel questions — status in v2
- **Gee** (explicitness of the real-world connection): **proposed default** = hidden-until-noticed + show-the-engine ring. Founder call #3.
- **Horvath** (physics fidelity vs. forgiveness): **v2 ruling** = abstracted-but-honest. Real cause-and-effect and momentum *feel*, but tuned so any kid's machine still does *something* — freedom-to-fail is a Tier-1-adjacent non-negotiable for a noticing game. Failure is funny, never punishing.
- **McGonigal** (remix ownership when machines stack): **founder answer holds** — calibration + consensus voting; the collaboration *is* the calibration; stack drift is the next iteration loop, not a problem to prevent. v2 adds: stacking is a Carry-Out paste, so provenance rides with the carried record.
- **Turkle** (does labeling "we measure calibration" kill play): **v2 ruling** = it deepens it — players are *in on the design* (the Design dashboard is the proof). Consistent with the Glass-Engine floor.
- **Claude** (which construct ships MVP): **answered** — calibration only; other two park (§3).

---

## 10. MVP — the build that ships first

**Stage: Mechanic Prototype** (art minimal, allowed to look plain — Lane A graduates later).

- One Rube Goldberg editor — drag-and-drop physics objects, basic gravity + collision, basic synthesized sound.
- The loop: build → survey peers ("what made you laugh?") → see the gap (predicted vs. actual, **computed**) → iterate.
- One real-world problem launches: **robotics + sustainable agriculture** (specific problem named at founder call #4).
- **Dashboards: Play + Learn only.**
- **Not in MVP:** artist intake, social stacking, Gather/Design dashboards, full Lane-A art. All graduate once the calibration signal is proven clean.

**Playtest (founder, one pass, two questions):** Does gap-noticing fire (does it still teach calibration)? Did anything surprise me?

**Drift fork:** clean signal → graduate to art, stacking, dashboards. Noisy signal → kill or reparent.

**Honest estimate:** ~3–5 days to a playable hinge.

---

## 11. Open decisions before art graduates

- The **specific** real-world problem (founder call #4; robotics + agri is the example, not the answer).
- Construct lock (founder call #1 — agent recommends calibration-only).
- How stackable machines scale → **resolved in v2:** Carry-Out paste, no backend (§2).
- Artist-intake legal framework (delegate to lawyer panel; not in MVP).
- Project name confirmed? ("Funny Boney's Factory" — misspelled on purpose. Clearance check is due diligence, not a panel taste call — run a name-collision check before it goes public.)

---

## 12. The recursive pipeline pass with Studio Eyes (NEW — the §6.2.5 loop, run on this build's own design)

*This is the studio's recursion loop (OS §6.2.5) applied to the v2 optimization itself: does the tighter spec drift, and does it hold the floors? Below the wall, fixes graduate automatically and one graduates per build; hard-wall items require a founder gate.*

### Studio Eyes pre-flight (the mechanical gate, agent-run — applied to the SPEC as a shippable artifact)
| Check | Result |
|---|---|
| Emoji anywhere | **CLEAN** — none. |
| Green in any primary/structural role | **CLEAN** — spec specifies no look; green-free named as a standing requirement for the build. |
| PII / real student data | **CLEAN** — no student data; the game's data layer is Carry-Out (consent-first, untransmitted). |
| Structural green-bail (the v1-era trap) | **CLEAN** — flagged forward to the build's Studio Eyes run, not decidable on a text spec. |
| Contrast / 44px / keyboard / focus | **N/A to a Markdown spec** — these are checked at the build's Stage-6 Studio Eyes gate; spec carries them as Tier-2 defaults (§4). |
| Reader lands on a raw text wall (Structure Floor) | **CLEAN** — the one-screen change summary + tables give every section an entry. |

### The recursive governance run (Probe Sweep + Harvest-back + decay)
**The probe the founder's instruction carried:** *"optimize for human-out-of-the-loop"* is structurally the test **"where does this build assume a human must act, and is that assumption load-bearing or just habit?"** Swept across the build (per §5.4.5.1, a founder instruction is a system-wide probe, not a narrow fix):

- **Intake sort** → was habit-human; **graduated to agent** (mechanical).
- **Fidelity checklist mechanical lines** → was habit-human; **graduated to agent**.
- **Ledger A playtest pre-flight** → was habit-human; **graduated to agent** (CLEAN/HALT is binary).
- **Data-gathering consent gate** → load-bearing human; **HELD at human, founder-gate, hard wall.** Cannot recurse.
- **Child-safety / trauma seat** → load-bearing human; **HELD, hard wall.** Cannot recurse.
- **"Is the calibration signal real" judgment** → load-bearing human; **HELD at human** (it's the construct; an agent computing the delta can't certify the delta *means* calibration).

**The rate governor (one graduates per build):** the probe surfaced several agent-graduations, but the OS caps graduation at **one load-bearing change per build** to prevent drift-by-accumulation. **The one that graduates this revision:** *the Fidelity-checklist mechanical/meaning split* — agent signs the mechanical lines, founder signs only the meaning lines — because it's the highest-leverage founder-attention saver and it generalizes to every future build, not just this one. The other agent-handoffs are already-permitted applications of the standing §8 delegation map, not new graduations, so they don't spend the governor.

**The decay twin (adding requires pruning):** this revision **prunes the v1 assumption that "accessibility is one flat always-on floor."** That single-tier framing is now retired in this spec, replaced by the two-tier sort (§4). One in, one out.

### Harvest (Stage 7 — what this build/spec proved)
A **data-gathering game can be optimized to maximum agent autonomy on the mechanical while keeping the human gate exactly where harm lives** (data + safety) — and the boundary between the two is nameable in a table, not a vibe. **Reusable candidate:** the **agent-autonomy map** (the `A / H / A→H` per-stage table in §6.5) as a Props Room component any future build fills in at Stage 0.

### Harvest-back (Stage 7 — what to watch / what the system should now catch)
**The failure-class this build could create:** a build that reads "human out of the loop" as license and quietly autopilots a *judgment* gate (data, safety, construct-truth) because the agent-autonomy map made handing-off feel frictionless. **The fix queued to the Recursion Ledger (promote-or-kill):** Studio Eyes (or the agent-autonomy map component itself) should **refuse to mark any Tier-1-wall row as `A`** — the map structurally cannot put a hard wall on autopilot, the same way the Recursion Ledger renders the wall un-crossable in UI. Queued, below-the-wall calibration reference = the existing collision power-order (hard floors win). **Founder gate not required** (it's a best-practice-tier enforcement of an existing wall, so it graduates automatically) — but flagged here so it's visible, per the human-in-the-loop-is-visible floor.

---

## 13. The five-bin outcome (replacing v1's implicit go/stop)

**Overall verdict on the v2 optimization: CONDITIONAL GO.**
- **Condition 1:** founder confirms calls #1 and #2 (§6.6) — construct lock + medium lock. Both are agent-recommended high-confidence; the gate just needs your "yes."
- **Condition 2:** founder names the specific real-world problem (#4) before art graduates (Stage 6). MVP can build the hinge without it; art can't ship without it.

Calls #3 (transfer explicitness) is a real fork left open for you. Nothing here is KILL, RECYCLE, HOLD, or PIVOT — the spine held all the way through, which is itself the finding: the optimization tightened the build without changing what it is.

---

*Captured from voice, optimized against the current OS, panel-re-reviewed, run through the recursion loop, and staged for the founder. Reconcile against the OS on next session open. Phone-save to the Project. This v2 displaces v1 (`funny-boneys-factory-spec.md`) — retire the v1 copy; same canonical name, superseded version retires (Stage-7 file rule).*
