# PRD — Choose Your Leader (CYL)

> **Status:** living document, v1 drafted 2026-08-10 (ISLO-hub lane); **v1.1 updated same day** (this lane) after the v7 build shipped. **Owner:** founder (Matt Walsh). **Studio:** Tight Spiral Productions.
>
> **v1.1 CHANGELOG (2026-08-10, post-ship):** `choose-your-leader-v7.html` SHIPPED the same day this PRD was drafted, executing a founder build order given after v1 (verbatim in `TSP_Ledger.md` 2026-08-10): cohesive full six-president 20+ minute build, the Maslow drop felt as Jenova Chen flow, **"Not politics, wealth and power"** — the frame is class. Sections 6, 9, and 10 below carry dated UPDATE notes where the ship changed their state. Everything else stands as drafted.
> **What this is:** the product requirements for Choose Your Leader — what it is for, who it serves, how it plays, what it must do, what it must never do, and what is still the founder's to decide. Written so a collaborator or a new build session can pick it up without re-explanation.
> **Grounded in canon (not invented):** `cyl-v7-founder-ruling-2026-08-08.md` (binding direction), `choose-your-leader-map.md` (build map), `cyl-full-bible.md`, `cyl-v5-rebuild-spec.md`, `cyl-period-bible.md` + `cyl-v5-image-lane.md` (art lane), `CYL_Harvest…md` (three-homes finding), `tight-spiral-patterns.md` §8 (the descent recipe), `TSP_Ledger.md` (rulings). Where a claim isn't in his docs, it isn't here (studio law). **Last-verified against canon:** 2026-08-10.

---

## 1. Summary

Choose Your Leader is a short, single-file, offline, accessibility-gated game that trains one reflex: **noticing the gap between what a leader said and what was true at the time.** It hands the player a real, dated quote from a U.S. president, asks how much they trust the person who said it, *then* turns over the facts the original audience could not see, and asks again — so the player feels how far the words pulled them before they knew the whole story. The measure is the distance between the two trust ratings. The win is catching the gap, not distrusting everyone.

It is **not** a game about who was a good or bad president. It is a game about the gap, and about the habit of noticing it. House method: **Play. Notice. Design.**

---

## 2. The problem it solves

Most media-literacy instruction tells students *that* they should be skeptical; it rarely lets them **feel** themselves being moved by a message and only afterward see the frame they were inside. CYL closes that loop:

1. **It makes you commit before you know.** You rate trust with only the quote in front of you. The commitment is real and on the record before the facts arrive.
2. **It shows you the cost.** Once the full record turns over, the game shows how far the rhetoric carried you — as a felt descent, not a scold.
3. **It rewards noticing, not cynicism.** One scene deliberately has almost no gap; noticing *that* is also a win. The skill is calibration, not suspicion.

---

## 3. Users & contexts

- **Primary: students** (MassBay and beyond) building the noticing reflex — phone-first, no account, no tutorial. Fits a commuter, part-time, mobile student body.
- **Secondary: faculty / instructors** who need to *see the mechanism* to trust it in a classroom (the Glass Engine depth rings, §6) and who may map its output to an assessment rubric.
- **Collaborator / producer** (e.g. a build partner) who needs the full picture to extend it responsibly.
- **The three-homes lens (class representation, binding — v7 order #7):** the same broadcast lands in different rooms — a suburban TV household, a city apartment reading the Black press (Chicago Defender, Jet), a rural weekly-paper household — all hearing October 1962 differently. Different class positions, different media apertures, different stakes. This is a design mechanic, not a demographic checkbox: the descent (§5) is **not uniform** across these rooms.

---

## 4. Goals & non-goals

**Goals**
- Teach gap-noticing as a transferable, felt habit — in one short sitting, on a phone.
- Make the consequence of rhetoric *felt* (the descent-in-world), never merely told.
- Stay defensibly truthful: every record real, dated, sourced, founder-approved.
- Emit measurable constructs (gap-noticing, landing tier) that can roll up to the iSLO / Confluence layer.

**Non-goals**
- Not a verdict on any president's character or worth.
- Not a "gotcha" — the descent never blames the player (§8 rails).
- Not a claim about outcomes for any specific audience the studio has not evidenced.
- Not a widening-before-depth build: ship one dimension real before adding tracks.

---

## 5. The product experience

### 5.1 The spine (the mechanic, not a sentence)
The spine is the **re-rate delta**: rate blind → the record turns → rate again → *see the gap between your two readings.* The game design panel (Romero, Blow, Chen, Meier; Hocking on ludonarrative fit) ruled the mechanic — not a thesis line — is the spine (TSP_Ledger 2026-07-23).

> **Retired, do not reinstate:** the earlier one-sentence framings ("You don't judge the leader. You judge what you were allowed to see." and the 2026-07-21 "corrected pitch" variant) were objected and **removed from every live surface 2026-08-08** (belt tick 6 guards them). No thesis line exists for CYL today; if one is ever needed, the founder writes it. This PRD cites them only to mark them dead.

### 5.2 The core loop (four beats per scene)
Every scene runs the same four beats; the repetition is the point — learn the move, then practice it across presidents and eras.

- **Beat 0 — Scene first.** Land inside a room (a 1962 living room lit by a TV; a Depression parlor with a radio; a hearth with a folded newspaper). No instructions. *Tap whatever your eye goes to* — every read is valid. Then the room speaks.
- **Beat 1 — Blind trust.** The quote, plus how it would have reached you ("Three networks. One message. This is all you get."). *With only this, how much do you trust the leader?* Four buttons, Not much → Fully. You must commit before continuing. This commitment is the measurement.
- **Beat 2 — The record turns.** The facts the original audience could not see arrive, dated and sourced. Then: *same words, but now you can see the frame — how much do you trust them?*
- **Beat 3 — The descent.** The game compares the two ratings and shows how far the rhetoric pulled you, and whether you braked it by noticing the gap.

After the last scene, an **arc screen** shows every moment at once: how high you held each time, where you caught the gap versus missed it.

### 5.3 The descent (the felt payload) and the v7 direction
The descent is a Maslow hierarchy turned into felt consequence: you start at the top (rung 5 — your own judgment) and rhetoric pulls you down toward the floor (rung 1 — where consent stops mattering); noticing the gap is the brake.

| Rung | Label in the game | What it represents |
|---|---|---|
| 5 | Your own judgment — becoming who you could be | You kept your footing |
| 4 | Standing, respect, a voice | Lightly moved, still mostly yours |
| 3 | A people, a side, a we | Pulled toward belonging — one safe message |
| 2 | Safety — survive the threat | Pulled toward fear and protection |
| 1 | The floor — where consent stops mattering | Carried all the way |

**The descent math (canonical recipe: `tight-spiral-patterns.md` §8):**
- `pull = (blind trust) − 1`
- `brake = max(0, blind trust − trust after the record)`
- `landing tier = clamp(5 − pull + brake, 1, 5)`
- `noticed = (trust dropped after the record)` — reported on the arc screen.

The game **never asks the player to rate themselves.** It only watches the distance between two commitments. That distance *is* the measure.

**v7 DRIFT RULING — the binding direction that retired the tag and named the drift (founder, verbatim below; the objected line is quoted only as retired, 2026-08-08):**

> "RE CYL, we have drift. There is a standalone game named viscosity but no movement in the CYL game is a Maslow affected world created by the powers that were enabled by your leader. That isn't showing up. The tag about 'you don't judge your leaders but what you were allowed to see' has to go. Use just my words in this game where possible from chats and docs AND assets from world tagged. Make the screens image first. One thing at a time. Build up when player skill is needed. A full room with TV broadcast, radio, etc is ok. I need class representation and different perspectives repped. Cold War 3 President. Current date (truth) 3 presidents."

Unpacked into product requirements:
- **Descent-in-world (the named drift, first job).** The player must *move through* a Maslow-affected world whose viscosity — the felt cost of scarcity, the drag on every move — is created by the powers their leader was enabled to use. Three months of builds paint the descent as a readout (v5/v5-b), a static ladder (v6), or text beats (full) — the world never thickens under the player's feet. That absence is the drift. `the-viscosity.html` is the proven felt-renderer prototype (the honeycomb stretches; legibility never drops; the crossing costs) and is CYL's descent renderer, **not** a standalone peer game (reconciled 2026-08-05). The intended Jenova Chen flow layer (leader impact → viscosity; drop-downs / pull-ups) is founder-gated.
- **Image-first, every screen.** The picture leads; words follow. The entry gate's scene-first law (>50% image) applies to *every* screen, not just the entry.
- **One thing at a time; build up when skill is needed.** Each screen asks exactly one thing. Complexity is earned scaffolding, never front-loaded controls.
- **A full room is allowed.** Density in the *scene* (TV, radio, period furniture) is fine. The one-thing rule governs what the player is *asked*, not how alive the world is.
- **Class representation, repped** via the three-homes rooms (§3), with a non-uniform descent across them.

---

## 6. Roster & content

**Roster: 3 + 3.**
- **Cold War trio — LIVE, records web-verified and dated:**
  - **Kennedy, Oct 22 1962** (Cuban Missile Crisis address). Gap: the calm public address was day eight of six days of private deliberation.
  - **Lyndon Johnson, Aug 4 1964** (Gulf of Tonkin). Gap: the second attack the speech leaned on most likely never happened (later NSA study); the war-powers resolution was drafted months earlier.
  - **Nixon, Nov 3 1969** ("silent majority" / Vietnamization). Gap: the same administration had been secretly bombing neutral Cambodia since March.
- **Current-era trio — at today's truth, records REAL and sourced before entering play, never fabricated (standing rule, OS §9):**
  - **Obama — already un-gated** (2026-06-27; the May 23 2013 NDU drone-war scene, sourced). Four scenes are LIVE today.
  - **Trump and Biden — gated, even-handedness condition binding:** both need identically rigorous, identically critical sourced gaps before un-gating. Sourcing them is a research task for a network-capable session.

> **UPDATE 2026-08-10 (v1.1):** that research task ran. Trump and Biden records were sourced and web-verified the same day (Trump: "cost me a fortune," St. Charles MO, Nov 29 2017, vs. JCT/TPC/PolitiFact/FactCheck.org record of permanent corporate cuts and expiring individual cuts; Biden: the middle-class-ticket promise, Aug 24 2022, vs. Pelosi July 28 2021 and *Biden v. Nebraska*, 600 U.S. 477 (2023)). Even-handedness held by construction: both scenes are the same shape — an economic promise vs. the documented record of where wealth and power landed. All six scenes are **in play** in `choose-your-leader-v7.html` by direct founder order ("Cohesive full 6 President"); the founder's cold play remains the final record-approval gate, and the sources ride in-file per scene.

**Gating rule (functional):** the engine deliberately excludes any scene from play until its quote-and-record pair is real, dated, sourced, and founder-approved (`PLAY = SCENES.filter(not gated)`; placeholders read `[QUOTE PENDING]` / `[RECORD PENDING]`). Records are never fabricated. The gate is visible to the player in the "for instructors" depth panel.

**The Glass Engine (end of game):** reversible depth rings let a curious player or a skeptical faculty member descend from "what was this measuring?" down to the raw readout — constructs, instrument, scenes played, gaps noticed, mean landing tier, ship-gate status. The learning mechanism is shown, not hidden.

---

## 7. Requirements

### 7.1 Functional
- Four-beat scene loop (scene-first → blind trust → record turns → descent) with a forced commitment at Beat 1.
- Re-rate delta captured per scene; descent math per §5.3; arc screen aggregating all scenes.
- Gating engine per §6; no fabricated records; founder-approval gate on every living-president record.
- Glass Engine depth rings at end of game.
- Descent-in-world rendering (viscosity as space) as the v7 core, replacing the readout/ladder.
- Class-perspective rooms: same broadcast, different homes, non-uniform descent.

### 7.2 Non-functional (studio floors — hard gates)
- **Single-file HTML, fully offline, in-memory only.** Zero external hosts. Nothing is collected.
- **Accessibility floor:** contrast-gated 4.5:1 (RP-safe), 48px house touch floor, full keyboard nav with visible focus rings, one decision per screen, scroll-resets-to-top on screen change, a working "leave the game" exit that clears state. Passes the studio belt (comfort, voice, art, one-thing, retired-lines, touch).
- **Voice — founder's words only, wherever possible.** Copy comes from his authored texts (`games-text-bank.md` and its extraction policy), his verbatim rulings, and the quoted-founder lines in canon. Chats are machine-unreachable (the CYL-harvest access boundary): anything needed from a chat, the founder pastes or it does not exist. Studio-drafted placeholder copy must be **tagged** placeholder-awaiting-founder-words, never passed off as his.
- **Art lane (mount, do not reinvent):** `cyl-period-bible.md` owns direction — photographic room + **withheld figure, no real faces, ever**; `cyl-v5-image-lane.md` owns operations — magazine collage IS photoreal (real period print, cut and composited), AI as labeled finishing assist only, provenance carried per art-doctrine. The legal-photo lane is authorized (2026-08-08) under named PD-first sources; note the archives were network-blocked in some sessions, so mounts may stage as asks.
- **No invented or inflated claims; pull back on disclaimers; no dark patterns.**

### 7.3 The three safety rails (LAW — locked 2026-06-27, trauma-informed)
1. **The consequence lands on the rhetoric's reach, never on the player's worth** ("This is how far rhetoric can carry a person," not "you failed").
2. **The brake is always live; naming the gap is the win, even at the floor** ("All the way down… but you named the gap on the way. That's the whole skill."). No dead end.
3. **The deep ending teaches; it never ambushes.**

---

## 8. Measurement & success

- **Constructs emitted:** gap-noticing (did trust drop after the record) and landing tier (1–5).
- **Feeds Confluence** (the studio's rater-norming / calibration discipline): the game teaches what to notice; Confluence measures whether the noticing happened and whether raters would agree.
- **Rolls up to iSLOs** as evidence at the assessment layer (candidate map: Critical Thinking; Written & Oral Communication; Personal/Social/Civic Responsibility — instrument TBD, §9).
- **Product success:** a player completes a sitting, can name a real gap they were moved by, and the mechanism is legible enough that a faculty member trusts it.

---

## 9. Scope & roadmap

> **UPDATE 2026-08-10 (v1.1): the next ship SHIPPED.** `choose-your-leader-v7.html` landed the same day (branch `claude/cyl-history-search-supplements-yx10w5`, ledger entry same date): six presidents in one 20+ minute arc; the descent walked, not read — between addresses the player crosses a household whose three rooms (the shift, the shelf, the back room) stretch apart by altitude spent, steps shrinking as the world thickens (`the-viscosity` vocabulary mounted; altitude accumulates across scenes, so scenes now alter each other — the first real answer to the Zimmerman integration note). Every record turns twice: what was hidden, then **who paid, by household** (the class frame, per founder order). Full belt preflight PASS, all seven ticks; playwright click-walk clean on a phone viewport. Items 1 and 4 below are done; 2 is partially done (plates carry the Cold War rooms; modern rooms are CSS-composed pending the photo lane); 3 (multi-home rooms — same broadcast, different houses) remains the maturation build. Touch floor note: the belt's founder floor is **44px** (repointed 2026-08-08), which v7 meets; the 48px figure in §7.2 was the earlier house floor.

**Next ship as drafted (v1, for the record — order of work the founder's words implied):**
1. Descent-in-world first (the named drift) — wire the viscosity felt-renderer as CYL's descent.
2. Image-first screen grammar second — apply scene-first to every interior screen.
3. Class-perspective rooms third — the same broadcast in different homes.
4. Current-trio record sourcing in parallel, when a network-capable session is available (Trump + Biden, even-handedness binding).

Every increment lands through the belt like everything else. Seating follows the Union Rep process; the caucus has a head start (CYL disciplinary bench, the Compositor/period-bible seat, the three-homes finding, the Viscosity build as the descent's proven interaction vocabulary).

**MVP discipline:** ship one rubric dimension real before building the visual and socioeconomic content tracks. Do not widen before the first dimension is real.

**Current surfaces (build audit, v1.1):** **`choose-your-leader-v7.html` (SHIPPED 2026-08-10 — the current flagship: full six, felt descent, class frame; linked from the face)**, `choose-your-leader-full.html` (v2, mapped; content-complete for the four historical scenes), `choose-your-leader-v5.html` / `-v5-b.html` / `-v5-slice.html`, `choose-your-leader-v6.html`, `choose-your-leader-nixon-slice.html`, and `the-viscosity.html` (felt-renderer prototype, now mounted inside v7). The descent "planes" art is not built yet — it waits on descent-math sign-off (§10). One canon note for any reader: the Obama NDU scene's copy exists in **no earlier build** despite the OS's "live" roster line (verified 2026-08-10 — the un-gating session's build never reached the repo); v7 reconstructed it from the OS's named sources.

---

## 10. Open decisions (founder-only — none can be delegated)

1. **Descent-math feel.** Does the pull/brake formula *feel* right in play — is the drop dramatic enough, the brake satisfying enough? Descent-planes art waits on this.
2. **The protection function (v7 open note).** The retired tag was, per the Salen & Zimmerman seat, *load-bearing* — the thing that kept real presidents and real deaths playable without real-world spillover collapsing the game. The line is dead; what carries the protective function now — a new founder-written line, the content-note screen, or the mechanic itself — is the founder's call **before the current-era trio expands.**
3. **Project name.** "Choose Your Leader" is the working title.
4. **Brand placement.** Where the Tight Spiral / imprint credit sits.
5. **The rubric instrument** the measurement maps to, and **which dimension ships first.**
6. **Approve the three modern records at cold play** *(v1.1: sourcing is done — all three modern scenes are sourced and in play in v7 by founder order; the founder's cold play is the remaining approval gate on the records themselves).*
7. **Which CYL build goes to the producer** (the "which build goes to Scot" call, `HITL-REVIEW-2026-08-08.md`) — the v7 drift ruling is a fourth input, and **v7 itself is now a live candidate** (see `osterweil-demo-brief.md`: it is the studio's closest relative to Scot's own Quandary — no right answers, consequences not verdicts, perspective-taking).
8. **The spine fork (2026-08-09, `TSP_Ledger.md`):** did the founder select a spine line on ~Aug 6 (shelf `cyl-modern/SPINE-RULING-2026-08-06.md`)? His 2026-08-10 word: he doesn't love that line as written — so no line ships either way; what remains open is only whether the stranded modern-period dossier work on the Mac is real and worth recovering.

---

## 11. Canon sources (this PRD synthesizes, does not replace)

| Doc | Role |
|---|---|
| `cyl-v7-founder-ruling-2026-08-08.md` | **Binding** direction; supersedes contrary earlier framing |
| `choose-your-leader-map.md` | Build map: vision, core loop, descent, rails, audit, open decisions |
| `cyl-full-bible.md` | Full beat/spec bible (correction-noted where v7 conflicts) |
| `cyl-v5-rebuild-spec.md` | Rebuild spec + the felt-descent open problem |
| `cyl-period-bible.md`, `cyl-sound-period-bible.md`, `cyl-v5-image-lane.md` | Art + sound + image-ops lanes |
| `cyl-policy-gap-bible.md` | Policy-gap / record research bible |
| `CYL_Harvest…md` | Three-homes finding; the chat access boundary |
| `tight-spiral-patterns.md` §8 | The reusable descent recipe (math, rails, a11y) |
| `TSP_Ledger.md` | Binding rulings (spine, retired tag, viscosity reconcile, legal-photo lane) |

*Update this PRD in place as the build changes; do not fork a second one. Where the studio floors and this PRD ever seem to conflict, the floors win. The retired tag stays retired.*
