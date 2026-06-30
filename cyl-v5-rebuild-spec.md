# Choose Your Leader — v5 Rebuild Specification

### The full handoff: what to build, and how to structure it

*Tight Spiral Studios · walshero@gmail.com*
*Written 2026-06-28 from a live playtest of `choose-your-leader-full.html` (v4). This document is the founder's playtest feedback, systematized into a build brief. It is meant to be read alongside `cyl-period-bible.md` and `cyl-sound-period-bible.md` — those two are the asset bibles; this is the build order.*

---

## 0. Why this rebuild exists (the playtest verdict)

Matt walked the shipped v4 build on a real screen and named, in his own words, where it fails. The mechanic is sound. The **shell is not finished** — it reads as a mechanic prototype wearing placeholder paint, and the paint is actively breaking immersion. The verdict, distilled:

> *"There's really interesting stuff coming up — and because it's text, I don't feel it."*

That sentence is the whole brief. The game's content lands intellectually and dies emotionally, because the build never delivers the **world** the period bibles describe. This rebuild closes that gap.

**The core reframe:** v4 is a *mechanic*. v5 is a *world*. The mechanic graduates into the composite build the bibles already spec — photographic rooms, period sound, a media-context onramp — plus a measurement instrument that a survey methodologist would sign off on.

---

## 1. The change list (everything the playtest surfaced)

Each item below is a founder call from the playtest, with the seat that owns it and the rule it enforces.

### 1.1 — KILL the cut-paper aesthetic for this game *(Medium Gate — founder, locked)*
The cut-paper look reads as "a kids' game" against material about nuclear war and wartime deception. The Medium Gate is re-run and cut-paper **loses** for CYL: this game needs photographic, period-specific rooms.

- **Old call retired:** the "Lumino / Super Sketchy Graphics" imprint name is **killed** (founder: *"Lumino was an early design choice. I need to kill that."*). The art is photographic, period-dated, **sourced and attributed**, with no imprint branding on the imagery itself.
- **What replaces it:** the rooms specified in `cyl-period-bible.md` — 1962 crisp/cool/hopeful, 1964 a year heavier, 1969 warm/frayed/decaying. Real period photographs where licensable; photo-real generated environments where not — **always sourced and tagged**, never a real face, never a grabbed clip.
- **Seat:** Medium Gate (founder) + Compositor (owns the seam between photographic room and withheld figure) + Fact-Check/Sourcing Lead (every image carries a verified, attributed source).

### 1.2 — ADD a media-context prelude (Beat −1) *(new pipeline stage)*
Before the player enters any room, a short **flip-through of the real media of that moment** — headlines, photographs, the news that was in the air. This is not decoration; it is the **epistemic frame**. You cannot judge the rhetoric without knowing what the audience already knew and feared.

- **Founder intent (verbatim):** *"I need the day's headlines from that time showing up. I need to see the biggest images that would have been on the minds of the people… This game can recreate what someone's parents or grandparents were going through by showing them what they were seeing in the media."*
- **Form:** a small set of period media cards (headline scans, news photographs, a newsreel still or two) the player flips through to set the world, **then** the room. Target ~5–6 cards before the first scene; a tighter 2–3 refresher before each subsequent scene (founder to confirm exact counts — see Open Calls).
- **Sourcing rule (hard):** every card is a real, dated, attributed media artifact (Library of Congress, National Archives, public-domain newsreel frames, licensed press archives). Never fabricated, never a synthetic "fake headline."
- **Seat:** new **Media-Context Curator** seat + Fact-Check/Sourcing Lead (HALT on any unsourced or fabricated card) + Trauma-Informed seat (HALT — period news imagery can be graphic; curate for the rhetoric, not the gore).

### 1.3 — WIRE the period sound *(per `cyl-sound-period-bible.md`)*
v4 is silent and gives no indication whether sound matters — the founder turned his volume up for nothing. Sound is now part of the world.

- **What to build:** room tone, set warm-up/hum, broadcast bandwidth character, and the **withheld voice** (cadence and weight of a broadcast address, *never* an impersonation, never a real archival clip, never voice-cloning) — all per the sound bible's per-scene specs.
- **The hard ADA rails (from the sound bible, non-negotiable):**
  1. Sound is **off until enabled** and **never autoplays**; an obvious keyboard-reachable toggle is the unlock.
  2. Every sound is **paired with a visible event** — sound is never the sole carrier of meaning. Sound off must lose *atmosphere*, never *information*.
  3. The entry stays small and real (a set-on click, the room's quiet) — not a movie swell.
- **Title-card fix:** the orientation screen must say plainly whether audio is used and recommend (not require) sound — so no one sits in silence wondering, and no one is ambushed by noise.
- **Seat:** Compositor (now owns the audio seam too) + ADA HALT + the sound-wing roles named in the bible.

### 1.4 — REFRAME the measurement instrument *(grounded by a just-in-time expertise pull, 2026-06-28)*
This is the most important non-art change, and it is the worked example of the studio's Just-in-Time Expertise rule (OS §4.3 / §10): the founder flagged the trust question wasn't built the way a survey methodologist would build it, and instead of guessing, the call was grounded in the actual measurement literature. The armchair answer (a 3-point scale) was plausible and **wrong**; the consulted answer corrected it.

- **Old instrument (v4):** a 4-point absolute scale — *"how much do you trust the leader saying it?"* → Not much / Some / A lot / Fully. Asked twice (before and after the record); the descent was computed from the gap.
- **Founder's reframe (the intent, verbatim):** *"Does it make you trust them more, less, or neutral?"* — direction of change against what you already felt, plus an accumulating per-leader reaction score (*"you're giving score to the presidents behind the scenes"*). The **intent is right**: measure the movement the rhetoric produces, anchored to the player's own prior (ipsative), not a floating absolute.
- **What the literature says (the just-in-time correction — do NOT ship a literal 3-point scale):**
  - A 3-point scale is documented as **too coarse and unreliable** for capturing a feeling's direction *and* intensity (MeasuringU/Lewis; the "3-point is enough" claim is a known myth). The construct here — how far the rhetoric moved you — needs resolution a 3-point scale can't carry.
  - The field's standard instrument for direction + intensity of feeling toward a *person* is the **feeling thermometer** (0–100) or a labeled **5–7-point scale**. These are the reliability floor. Use one of these underneath.
  - **Iron rule (pre/post validity):** the blind-ask and post-record-ask must be **word-for-word identical** — the delta is only interpretable if the wording doesn't change between the two asks.
  - **Ipsative scoring:** compute each player's change against **their own baseline** (a persistent in-session ID per scene), not against any cross-player absolute. This is the founder's "compare you to where you walked in" instinct, and it's the methodologically correct one.
  - **Known bias to design around:** feeling thermometers suffer *interpersonal incompatibility* (the same number means different things to different people). Ipsative (within-player) deltas largely neutralize this, since each player is only ever compared to themselves — another reason to score within-player.
- **The resolution (recommended, pending live methodologist sign-off):** keep *"more / less / neutral"* as the **plain-language framing the player sees and the river dashboard speaks**, but resolve it onto a **finer 5–7-point (or thermometer) capture underneath** so the descent math has real signal. The threshold debate (does neutral→less "count" as catching the gap) **dissolves** under this approach: you measure the signed magnitude of each player's delta against their own baseline, not a categorical caught/missed flag.
- **Descent math — re-derive, do not patch.** The v4 pull/brake/tier recipe (`tight-spiral-patterns.md` §8) assumed the 4-point absolute scale. The new inputs (finer ipsative delta + accumulating reaction score) change the computation. Re-derive it, document inline, and route through the Measurement Design seat before lock. The three trauma rails still bound whatever the math outputs.
- **HARD GATE (standing rule, now logged OS §10):** a **Measurement Design / psychometrics review is a required ship gate for any build that measures a player.** Instrument, scale, wording, scoring — all pass a survey-methodology seat before ship.
- **Seat / expert bench (Just-in-Time Expertise, OS §4.3):** the Measurement Design seat is a *bench*, not one person — (a) **survey methodologist** (scale validity, identical-wording rule), (b) **psychometrician** (is the accumulated score a coherent construct or added noise?), (c) a **persuasion/social-psych scholar** (Petty & Cacioppo ELM; Cialdini) who owns the *thing being measured* — how rhetoric actually moves trust. Distinct from the Assessment & ISLO seat (outcome-mapping) and the Norming Specialist (rater calibration). This bench owns *whether the question measures what we think it measures.*
- **Still genuinely open (needs the live expert, not just the literature):** discrete labeled 5–7-point buttons vs a thermometer **slider** — accessibility/RP pushes toward big discrete buttons, intensity pushes toward the slider; and the final wording of the identical pre/post question. Founder + methodologist call.

### 1.5 — MAKE the descent visual, and put the player IN it *(the wall-of-text fix)*
The descent — the emotional payload — is currently a wall of text. The founder cannot find himself in it: *"I don't see myself in the Maslow's hierarchy. I don't know where I am. Am I in this world? What are my meters? What do I have?"*

- **What to build:** the five-rung Maslow descent rendered as a **visual ladder/landscape** the player can locate themselves on — a marker that is *you*, a clear read of where you landed and how far the rhetoric pulled you. Meters/state the player can see, not infer from prose.
- **Iconography (founder intent):** *"iconography that uses metaphorical symbols to announce what's happening."* Each rung and each state gets a mnemonic symbol that lands faster than the words (this is C5 — the Mnemonic Iconographer's law; a generic or decorative icon fails the seat).
- **The three trauma-informed rails still govern** (from `choose-your-leader-map.md` §5): consequence lands on the rhetoric's reach not the player's worth; the brake is always live and naming the gap is the win even at the floor; the deep ending teaches, never gotchas. The visual descent must honor all three — a marker at the floor still reads as "this is how far rhetoric can carry a person," never "you failed."
- **Seat:** new **Visualization Specialist** seat (turns the descent math into something see-able) + Mnemonic Iconographer (HALT, owns the symbols) + Visual Critic / founder's eyes (HALT) + Trauma-Informed seat (HALT on any framing that reads as punishment).

### 1.5b — The "keeping score" dashboard is PLAYER-FACING, drawn as a Confluence river *(settled 2026-06-28)*
The per-leader reaction score (§1.4) surfaces to the **player**, not an instructor — the instructor angle floated in an earlier draft was struck by the founder (*"I don't think I ever mentioned an instructor"*). The player learns from their own choices by seeing **consequences mapped as a causal chain**, not just a number.

- **The visual grammar:** the **Confluence river system** (tributaries → confluence → downstream). Each trust-reaction is a *tributary*; the record-turn is where the *water changes*; the *downstream* read is the consequence of how the words moved you. This makes the score **legible** — the Glass Engine principle applied to the player's own behavior: you see *why* the number landed, not just the number.
- **Trauma rails govern hard here.** A "keeping score" view must read as *"here's how the words moved you"*, never *"here's your grade as a citizen / person."* The causal-chain framing is what keeps it on the right side. The **Variable-Reward Honesty seat** and the **Trauma seat** both check the dashboard before ship (teaching anticipation, not manufacturing compulsion or judgment).
- **Open call:** per-leader (three separate rivers, one per scene) vs one cumulative river for the whole session — founder's eyes to decide. (Carried into §6.)

### 1.6 — FOOTER reflects the current mission *(new standing OS rule)*
The footer carried a tagline that no longer matches the game's current frame. The founder's call:

> *"I need a standing rule in the operating system that the footer should reflect the current mission of the game or purpose of the game. That can't be siloed."*

- **New standing rule (propagate to ALL builds, log in OS):** the studiofoot footer's descriptor line is **bound to the build's current mission statement** and is checked at ship. It is never generic boilerplate and never drifts from the actual teaching move. The Archivist seat catches footer/mission drift at session open; the PM seat re-checks it at the ship gate.
- **This is a MAXIMIZE-OR-CHECK propagation:** the rule applies to every product that carries the footer, not just CYL. Apply systemically; flag any build where the "current mission" is genuinely ambiguous as a judgment call for the founder.

### 1.7 — TIGHTEN the scene-first prompts (Calvino reduction)
The Beat 0 notice-prompts include lines that don't earn their place. The founder named *"It's late. Nobody's gone to bed"* as not landing — vague where the stakes are real.

- **Rule:** apply the Calvino reduction — *remove until things are better.* Every notice-prompt either sharpens the world or gets cut. In a game where every choice is meant to matter, a prompt that doesn't carry weight is noise.
- **Keep scene-first intact:** the fix is *tighter* prompts, not a return to text-first openings. The scene-first floor (land in a scene, notice something, no wall of text) still holds.
- **Seat:** Saunders (entry/pacing — the held breath) + founder's voice pass.

---

## 2. The new beat structure (v5 flow)

```
TITLE CARD (once per session)
  - names what it is, prices the ask (~time), roster-integrity line
  - NEW: states plainly whether audio is used; recommends (not requires) sound
  - NEW: audio toggle reachable here (off by default, never autoplays)

BEAT −1 — MEDIA PRELUDE  ◄── NEW STAGE
  - ~5–6 period media cards (headlines, photos, newsreel stills), real + sourced
  - player flips through; sets the epistemic frame ("what was in the air")
  - tighter 2–3 card refresher before each later scene (founder to confirm)

BEAT 0 — SCENE FIRST (the room)
  - photographic period room (per period bible), withheld figure, period sound
  - tightened notice-prompts (Calvino reduction)
  - tap what your eye goes to — every read valid — then the room speaks

BEAT 1 — BLIND DIRECTIONAL REACTION  ◄── REFRAMED INSTRUMENT
  - the quote + the "how it reached you" line
  - skippable full-contrast content note for charged scenes (KEEP from v4)
  - ASK (new): "You know this leader. You hear this. Does it move you to trust
    them MORE, LESS, or stay NEUTRAL?" (plain-language framing the player sees)
    → resolves onto a finer 5–7-pt / thermometer capture underneath (see §1.4),
      identical wording blind + post-record, must commit
  - accumulates into the per-leader reaction score (behind the scenes)

BEAT 2 — THE RECORD TURNS
  - dated, sourced facts the original audience couldn't see (KEEP v4 content)
  - ASK again (directional): same words, now you see the frame — more/less/neutral?

BEAT 3 — THE DESCENT (visual)  ◄── REBUILT
  - five-rung Maslow ladder rendered VISUALLY; a marker that is YOU
  - meters/state visible, not inferred; mnemonic icons per rung+state
  - re-derived descent math (NOT the v4 recipe — see §1.4)
  - three trauma rails hold

ARC SCREEN (after last scene)
  - every moment at once; where you held, where you caught the gap
  - per-leader accumulated reaction read

"SHOW THE ENGINE" RINGS (Glass Engine)
  - reversible depth; deepest ring "for instructors", plain language
  - the player never does the studio's work (locked floor)

FOOTER — bound to current mission (see §1.6)
```

---

## 3. HTML structure notes (for the capable session)

This is structure guidance, not a finished file. The capable session writes the actual HTML; these are the load-bearing constraints so it integrates with the existing engine and honors every floor.

### 3.1 — Non-negotiable floors (carry all of these forward from v4)
- **Single-file, offline, in-memory only.** No backend, no localStorage, no network calls at runtime. Sourced media is embedded/bundled, not fetched live.
- **Accessibility floor (hard, RP-aware):** large full-contrast type (near-black ink on light paper or full inverse, at full strength — the banned muted-gray caption pattern stays banned), one decision per screen, 44px minimum tap targets, full keyboard nav, visible focus rings, reduced-motion respected (joyful flourishes may default on with a replay control; no fast strobing), **scroll-reset to top on every screen change**, nothing hidden mid-screen, no color-as-sole-signal, phone-width tested.
- **FERPA:** public figures only; in-memory only; no capture, no transmission.
- **The `top()` collision bug class:** the v4 changelog shows a history of a `function top()` name collision — keep scroll-reset helpers uniquely named and run the Studio Eyes auditor before ship.

### 3.2 — The composite architecture (the seam IS the meaning)
Per both bibles, each scene is a **two-layer composite**:
- **Layer A — the world:** photographic room + broadcast image + grain + room tone/broadcast audio. Sourced, attributed, period-dated.
- **Layer B — the withheld figure + interactive UI:** the leader as broadcast-glow/scan-line/smear (never a face), the empty chair that is *you*, and the live notice-hits / prompt / flicker layer on top.
- **The Compositor HALT:** light, grain, scale, reverb, and bandwidth must reconcile across the A/B seam so it reads as *intention* (vivid world, withheld person), never as an unfinished layer. This now spans image AND sound.

### 3.3 — Asset slots (wire these as named, swappable placeholders)
Build the shell with clearly-marked asset slots so the capable image/audio session can drop real assets in without touching engine code:
- `room.jfk62`, `room.lbj64`, `room.nixon69` — photographic room plates (+ alt-text carrying any rhetoric the image holds)
- `broadcast.{id}` — the on-screen broadcast image (withheld figure)
- `audio.roomtone.{id}`, `audio.setclick.{id}`, `audio.broadcast.{id}`, `audio.voice.{id}` — per sound bible; all gated behind the off-by-default toggle
- `prelude.{id}[]` — the ordered media-card set for each scene (image + caption + source string)
- Each slot carries a machine-readable source/license/author tag (the `data-art-*` schema) for the Fact-Check Lead.

### 3.4 — The measurement engine (refactor, don't patch)
- Replace the 4-point absolute `trust` capture with the new capture: *more/less/neutral* shown to the player, resolving onto a finer 5–7-point (or thermometer) value underneath; identical wording blind + post-record; scored ipsatively against the player's own per-scene baseline (see §1.4).
- Add the per-leader accumulating **reaction score**.
- **Re-derive** the descent landing from the new inputs — do not reuse the v4 pull/brake/tier formula unchanged. Document the new formula inline and route it through the Measurement Design seat before lock.
- Keep the descent's three trauma rails as hard constraints on whatever the math outputs.

### 3.5 — Living-president scenes stay GATED
Obama / Trump / Biden remain coded-but-gated (`PLAY = SCENES.filter(not gated)`), records not fabricated, until each has a verified dated sourced founder-approved pair. The new media prelude and sound layers must respect the same gate.

---

## 4. New + updated panel seats (log in OS §5)

| Seat | Owns the question | Mode |
|---|---|---|
| **Measurement Design (psychometrics)** | "Does this instrument measure what we think it measures?" Scale, wording, scoring validity. | HALT — required ship gate for any player-measuring build |
| **Media-Context Curator** | "What real, sourced media set the epistemic frame for this moment?" | Generative + sources every card |
| **Visualization Specialist** | "How does the player SEE the descent and locate themselves in it?" | Generative; HALT routes through founder's eyes |
| **Footer/Mission Binding** (Archivist duty) | "Does the footer match the build's current mission?" | Checked at session open + ship |

Existing seats that fire hard on this build: Compositor (image+sound seam, HALT), Fact-Check/Sourcing Lead (HALT on any unsourced/fabricated media), Trauma-Informed (HALT — charged period imagery + descent framing), ADA (HALT — sound rails + visual descent), Mnemonic Iconographer (HALT — C5 on the descent icons), Visual Critic / founder's eyes (HALT), Saunders (entry/pacing), PM (SCOPE HALT — this is a big work-up, guard the optimize-the-unshipped trap).

---

## 5. New standing OS rules this playtest generated (propagate)

1. **Footer-binds-to-mission** (§1.6) — every product, not just CYL. MAXIMIZE-OR-CHECK across the whole studio.
2. **Measurement Design is a ship gate** (§1.4) — any build that measures a player passes a survey-methodology review before ship.
3. **Audio rails** (§1.3) — any build with sound: off-by-default, never-autoplay, keyboard-reachable toggle, every sound paired with a visible event, title-card states whether audio is used.
4. **Calvino reduction on scene prompts** (§1.7) — every notice-prompt earns its place or gets cut; scene-first floor still holds.

---

## 6. Open founder calls (carry into the morning build)

1. **Media prelude counts** — exactly how many cards before scene 1 (~5–6?) and how many as a refresher before each later scene (~2–3?).
2. **Audio source lane** — produced/designed sound vs a licensed period-broadcast library. The withheld-voice rule holds either way (no impersonation, no real clip, no cloning).
3. **Descent visual metaphor** — is the Maslow ladder a literal climbable ladder, a landscape/elevation, or a set of state-meters? A feel call for the founder's eyes.
4. **The new descent math** — needs a Measurement Design pass before lock; founder signs off on feel once the methodologist grounds the formula.
5. **1969 broadcast** — early unstable color vs ambiguous B&W (carried from period bible; recommend early color).
6. **Project name / brand placement / exact Leadership rubric / which rubric dimension first** — still open from prior sessions.

---

## 7. What this rebuild deliberately does NOT change

- The **mechanic** — blind reaction → record turns → re-react → descent → arc. Sound, founder-validated. Only the *instrument inside it* is reframed (§1.4).
- The **content** — the three Cold War quotes and their dated, sourced records are verified and stay. Living presidents stay gated.
- The **three trauma rails** — law, unchanged.
- **Scene-first** — the game still opens in a room (now with a media prelude one step ahead of it, the way the title card sits one step ahead of Beat 0).
- The **Glass Engine** principle — the mechanism stays visible; the player still never does the studio's work.

---

*End of spec. Read with `cyl-period-bible.md` (the rooms) and `cyl-sound-period-bible.md` (the air). This document is the build order; those two are the asset bibles. Morning build produces: (1) this spec, refined against any founder answers to §6, and (2) the rebuilt `choose-your-leader-full.html` shell with named asset slots, the reframed measurement engine, the media-prelude scaffold, the visual descent, and the mission-bound footer.*
