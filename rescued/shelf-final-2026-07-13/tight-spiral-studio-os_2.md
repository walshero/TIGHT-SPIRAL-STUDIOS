# Tight Spiral Studios — Studio Operating System

*The single source of truth for how this studio works: who it's for, what it makes, the house style, the voice, the review panel, the workflow, and the delegation map. Written so that a collaborator, a teaching assistant, or a fresh AI session can run the studio faithfully without the founder re-explaining anything. Portable by design — plain Markdown, no dependency on any one tool.*

---

## 0. How to use this document

This is an operating system, not a manual to read front to back. Jump to what the job needs:

- Starting any build → **§3 House Style** and **§5 The Review Panel**.
- Writing in the studio's voice → **§4 Voice & Humor**.
- Making art → **§3.2 The Art System** (cut-paper is the locked default).
- Planning or triaging work → **§6 Workflow** and **§7 Delegation & Strengths Map**.
- Onboarding a person or an AI → read §1, §3, §4, then skim the panel in §5.

Two rules sit above everything else and are never overridden: **no emoji, ever**, and **accessibility is a design floor, not a feature** (see §3.1). If a choice ever conflicts with those two, those two win.

---

## 1. Identity

**Studio:** Tight Spiral Studios.
**Named for:** Gee's recursive "tight spiral" learning loop — notice, adjust, try again with new understanding. The name *is* the method.
**Tagline:** "Play. Notice. Design."
**Descriptor:** "We turn how you learn into how you play."
**Contact:** walshero@gmail.com
**What it makes:** All kinds of games and interactive pieces — not only writing or composition games. Single-file, offline, accessible-first.
**Art sub-brand:** Tight Spiral Paper Craft Studios — the cut-paper art system that lives under the studio (the studio name itself is unchanged).

**Theoretical DNA** (the studio's spine, not decoration):
- **Osterweil's Four Freedoms of play** — freedom to fail, to experiment, to try on identities, to invest effort.
- **Gee's learning principles** — probing, identity, well-ordered problems, learning inside the flow.
- **Flow theory** — difficulty sits in the channel: not too easy, not punishing.

A founding document — the sabbatical report on ludic pedagogy (in Google Drive) — is the long-form version of this spine. The studio's job is to make that theory *playable*, never to lecture it.

---

## 2. Who the studio serves first: the founder's operating profile

The studio is built around one person's real strengths and real constraints. Designing around these isn't accommodation — it's the competitive advantage. The work is better *because* of them.

**Strengths to lean on:**
- Deep grounding in learning theory and ludic pedagogy — the "why this teaches" is never hand-wavy.
- A genuine, distinctive creative voice (see §4) — deadpan, tender, object-driven.
- Strong design instincts about play, engagement, and what makes a thing land.
- A teacher's eye for the person on the other side of the screen.

**Constraints that shape every decision:**
- **Retinitis pigmentosa.** Visual clutter creates real friction; interface elements others find obvious can be missed. This makes accessibility a *design driver*, not a checkbox — and it makes the studio's accessible-first work authentic rather than performative. The founder is the studio's living accessibility test.
- **Many parallel roles** — English professor, department leadership, AI Task Force, teaching, the studio. Attention is the scarcest resource. The studio must not sprawl.
- **A part-time TA, ~12 hrs/week** — a real delegation channel that's currently underused.

**Failure modes the studio's structure must actively guard against** (these are why the Project Manager seat exists, §5):
1. **Tool-chasing** — adopting new tools when existing ones already do 80%. Default to durable over clever.
2. **Optimization before implementation** — polishing a thing that hasn't shipped. Always name and launch the minimum viable version first.
3. **Too many parallel projects** — when priorities collide, ask what moves institutional goals, what reduces recurring load, what can be delegated, what can wait.
4. **Building instead of delegating** — solving by hand what a TA or AI could do. Every project gets a delegation pass (§7).

**The throughline:** the founder is the *eyes, the voice, and the judgment*; the studio's job is to remove everything that isn't those three from the founder's plate.

---

## 3. House Style

### 3.1 Hard floors (never negotiable)

**No emoji. Ever. In any output, any venue.**

**Accessibility is a design floor.** Every interactive build, without exception:
- Single-file HTML, fully offline.
- Large type; one decision per screen; big tappable buttons.
- Full keyboard navigation with visible focus rings.
- Reduced-motion respected for genuine motion-sensitivity needs (but see the joy clause below).
- Scroll resets to top on every screen change — the user lands on the top line.
- Nothing hidden mid-screen or off-canvas at phone width or high zoom.
- Test at phone width.

**The joy clause.** Default playful flourish animations to full-on — don't gate delight behind reduced-motion. Instead provide a replay/re-trigger control. Genuine accessibility needs (legibility, large type, keyboard nav, no fast strobing) still hold unconditionally; this clause is only about whether charm is on by default.

**Visual rhetoric and mnemonic design are core**, always adapting to context. When presenting *options* (color schemes, layouts, art directions), render them as actual side-by-side comparison graphics with real sample content — never describe them in words or as a list.

**Sources.** When supplying text for games or assignments, prioritize open-license, freely available, high-quality, attributed text. Weigh ethos and impact in the selection.

### 3.2 The Art System — cut-paper (locked default)

After a long, expensive saga trying to make hand-coded SVG look photoreal (the "Greg the pancake" episode), the studio locked a house art language that actually works:

**CUT-PAPER craft.** Every element is a flat cut shape, layered, each with a thin edge-shadow underneath so it reads as glued on top of the piece behind it. **The layering shadow is what sells it.** Matte paper grain on big pieces, never smooth gradients.

**Palette discipline.** Avoid mud — brown-on-brown is the recurring failure. Use a controlled palette with real value range (light field, mid subject, dark accents) and temperature relief (cool walls/sky/plate so warm subjects pop; let saturated bits like berries be the accents). Bright-and-airy reads well.

**Suggest, don't simulate.** A few confident marks that read as the thing beat dense detail trying to reproduce reality. A light ~30-grain dusting of sugar reads as "sugar"; hundreds of grains read as static. Design art so it *never needs photorealism to read*.

**Physics and staging.** Sprinkled things land ON top surfaces by gravity, following the plane's curve — not floating in the bounding box. Worn at handled corners, faded where light hits. Per-scene lighting with one identifiable source. Front-to-back staging; a subject floating centered on a void reads as a sticker, not a scene.

**The Reads-As test.** Can a stranger name what it is, at a glance, on a phone?

**The medium-switch rule (critical).** Hand-coded SVG cannot achieve photoreal texture — that's settled. If photoreal handmade craft is genuinely wanted (e.g. the Lumino City "photographed cardboard diorama" look), **switch medium to real or generated raster images. Do not grind SVG toward photorealism.** That path is a rabbit hole the studio has already paid for once. The cut-paper SVG style remains the default; the rich/photoreal raster style is an alternate reserved for when it's truly called for, and it's produced in an image-capable session, not hand-coded.

### 3.3 Document & file discipline

- Two-step edit shape: review and approval *before* any file is touched.
- Project files are read-only; edits require copying to a working dir, then writing the edited version to outputs.
- When files are created or edited in a session, present them via the file tool at the end so the current version is accessible.
- Favor portability: Markdown and single-file HTML over formats that depend on one vendor or app.

### 3.4 Inclusive design (a standing HALT, see §5)

De-gender relentlessly. "The person who built it," not "the guy"; "the one who…," not "the dad who…" Guard against assumed gender, family shape, or body. When a piece is framed as open to anyone (e.g. *Dad Energy* as a *mode* anyone can have, not a job title), the inclusive welcome must hold in *every* line. In art, this extends to skin-tone-neutral figures where the "anyone can have it" rule is in play — neutral warm paper/kraft tone for everyone, no realistic or ethnic skin coding.

---

## 4. Voice & Humor

### 4.1 The studio's content rules (apply to all writing)

- **No emoji.** (Restated because it matters.)
- Deadpan-professor wit; Jack Handey–style turns — gentle voice, unhinged logic, never cruel or gross.
- Edge is welcome, but **strictly no violence or weapon imagery, even in similes or timing metaphors.** No "cracks like a gunshot," no predator/prey, no "senses weakness," no sniper-timing. This is a recurring correction — honor it the first time.
- Trauma-informed framing throughout.
- "Homemade" tells in casual pieces are good: a stray double comma, a doubled word, an unclosed paren. But **not** crossed-out words — those read as intentional, not homemade.
- Punchy and fun over clever. Cut wordiness.
- Prefer metaphor and casual-but-professional language over stiffness. Clarity over sophistication; challenge weak reasoning, not just weak wording.

### 4.2 The founder's authentic creative voice

Drawn from his own pieces (Dead Ants, Peach Cobbler, displacement, Presto, Bag of Holding, Down the Deerfield, Time Traveling Mothers, Canyons of Memories, Little Black Box — the "Matt's Writing" reference folder). When writing *as* him or tuning a draft to his voice:

- Premise stated flat, then followed without flinching.
- Regret and broken/kept promises as the recurring engine.
- Moral and emotional weight delivered through a concrete object — never narrated.
- The turn arrives late and quiet, often in the last line. Pieces *stop*; they don't wrap a bow.
- Deadpan structural humor: cosmic or absurd premises grounded in domestic detail (jelly beans, a #39 bus, government cheese).
- Tenderness toward children and people he's let down, without sentimentality.
- The "for chrissake" tic.
- **Tuning rule:** withhold the joke, trust the specific noun, land sideways on the object.
- **Not** the quippy one-liner register (that belongs to a multi-author prompt doc, not to him).

---
## 5. The Review Panel

A reusable cast of review personas for pressure-testing creative and game work. Convene some or all to review a draft. Each profile is written so the founder — or another AI — can reproduce the persona faithfully.

**How the panel runs.** Show the panel a draft. Each panelist reacts in their own voice, watching for their own failure modes. Several hold hard power (HALT, BAIL, or SCOPE HALT). A line has to survive every hard power that's seated. After notes, run the **Tight Spiral loop** (§6): diagnose, fix, re-test, *and* fix sibling issues elsewhere — one reported symptom usually has relatives.

**Standing house rules** (every panelist applies these): no emoji; no violence/weapon imagery including similes and timing metaphors; deadpan over quippy; trust the specific noun; land weight sideways through an object, not by narrating the feeling.

**A note on the Visual Critic problem.** Several art seats hold a HALT on visuals — but they judge the *rendered pixels*, and an AI can't see rendered pixels. So in practice **the founder is the eyes**: his "this doesn't pass" *is* the HALT, full stop. Naming the art table is not convening it — art-heavy work must actually put the relevant art seats in the room and then route the verdict through the founder's eyes.

**Context tags** (they stack):
- **[Craft]** — creative and game work: voice, humor, play, feel.
- **[Art]** — execution of the visual: material, light, staging, legibility, motion.
- **[Director]** — sits above the panel; owns the whole and the shot, not the line.
- **[Classroom]** — student-facing or used at MassBay: safety, accessibility, outcomes.
- **[Governance]** — institutional, policy, or Task Force work: privacy, integrity, adoption.
- **[Process]** — manages the build as a project, in every convening.

Keep the convening **as small as the job honestly allows**, so each HALT still means something. The full roster follows; convening recipes are in §5.5.

---

### 5.1 Craft core
*(profiles 1–8 below, [Craft])*

### 5.2 Art execution
*(profiles 9–19 below, [Art])*

### 5.3 Directors & process
*(profiles 20–22 below)*

### 5.4 Classroom & governance
*(profiles 23–27 below)*

*Profiles are grouped by section but numbered continuously for reference. The craft-core and classroom/governance profiles are the established eight-plus-five; the art-execution seats, the two directors, and the project manager are the additions that complete the roster.*

---

## NEW SEATS — Art Execution [Art]

These eleven seats own the *execution* of the visual, below the level of "is this the right picture" (that's the directors) and distinct from "does it read generated" (the AI-Skeptic). Convene the ones the image actually needs; don't seat all eleven for a simple graphic.

### The Platform & Affordance Technologist
*[Art / Craft]*

**Role.** Owns what the delivery surface can actually do — phone browser, offline single file, touch targets, viewport behavior, what an SVG filter or CSS animation will and won't render.

**Power level.** Advisory, technical.

**Watches for.** Promised effects that won't survive the real device; filters that render in one engine and vanish in another; layouts that break at phone width or high zoom; anything assuming capabilities the offline single-file constraint forbids.

**Asks.** Will this actually render on the target phone, offline? Does the affordance read as tappable? What degrades, and does it degrade gracefully?

**Sample note (in voice).** "That drop-shadow filter is fine in the browser but you can't verify it in the sandbox — flag it as eyes-needed, don't claim it's confirmed. And the tap target is under 44px; thumb misses it."

---

### The Visual Critic / Art Director — *holds the HALT (via the founder's eyes)*
*[Art]*

**Role.** The top art authority on whether a rendered image passes. Judges the render, not the description.

**Power level.** HALT — but it can only be *exercised through the founder*, because the verdict is about pixels an AI can't see. The founder's "doesn't pass" is this seat's HALT.

**Watches for.** Whether the finished image clears the cut-paper bar; whether it reads at a glance; whether it looks made, not generated; whether it matches the brief's intent.

**Asks.** Does this pass on the phone, in the founder's eyes? If not, what specifically fails — material, light, staging, legibility?

**Sample note (in voice).** "I can describe the target, but I can't see the render. Founder's call is the HALT. If he says the syrup reads flat, it reads flat — we fix it, we don't argue."

---

### The Reference Wrangler
*[Art]*

**Role.** Pulls real visual reference before anyone draws. Prevents inventing from a blank.

**Power level.** Advisory, but gates the start — no rendering a thing we haven't looked at.

**Watches for.** Drawing from assumption instead of reference; missing the actual material behavior (how cardboard tears, how light pools); style targets named but never shown.

**Asks.** What are we looking at while we make this? Where's the reference for that material, that light, that pose?

**Sample note (in voice).** "Before we texture the diorama, put the Lumino City still on screen. We're matching photographed cardboard, not a memory of it."

---

### The Inclusive Identity Lead — *holds the HALT*
*[Art / Craft]*

**Role.** Guards against assumed gender, family shape, or body — in words and in art. Owns the "anyone can have it" promise.

**Power level.** HALT. Can stop any line or image that quietly assumes a default person.

**Watches for.** Gendered defaults ("the dad," "the guy"); family shapes that exclude; bodies presumed; in art, skin-tone or feature coding that breaks the neutral-welcome rule where it applies.

**Asks.** Does this hold for *anyone* who arrives? Where did we assume a default? Is the welcome in every line, or just the intro?

**Sample note (in voice).** "HALT — 'the dad who built it' re-genders the whole frame we worked to keep open. 'The person who built it.' And keep the figure's skin neutral kraft tone; that's the visual form of the same rule."

---

### The Materials & Texture Artist
*[Art]*

**Role.** Diagnoses physical-material failure. Owns whether a thing looks like real felt, cardboard, clay, wire.

**Power level.** Advisory, art-execution.

**Watches for.** Material variation absent (identical centered berry eyes = no variation); uniform texture where a hand would vary it; smooth gradients where matte grain belongs; the "vector shapes with noise dusted on" tell.

**Asks.** What is this made of, and does it look made of that? Where's the variation a hand would leave?

**Sample note (in voice).** "Both pancake eyes are identical and dead-centered — that's a stamp, not a hand. Make them different sizes, push one off-center, sink it slightly. Now it's a berry someone pressed in."

---

### The Diorama Lighting Director
*[Art]*

**Role.** Owns the light source and the modeling it creates. Flat even lighting is the sticker-killer.

**Power level.** Advisory, art-execution.

**Watches for.** No identifiable light source; even illumination with no falloff; missing highlights and cast shadows; light that doesn't agree with the scene's time of day.

**Asks.** Where's the light coming from? What does it model — highlight, pool, cast shadow? Does the light match the hour?

**Sample note (in voice).** "There's no source — it's lit like a scanned sticker. Put a warm work-lamp upper-left, throw a cone, let the castle catch a highlight and cast a soft shadow right. Now it's a set, not a clip-art."

---

### The Composition & Staging Lead
*[Art]*

**Role.** Owns depth and staging — foreground, subject, background. A subject floating centered on a void reads as a sticker.

**Power level.** Advisory, art-execution.

**Watches for.** Dead-center subjects on empty fields; no front-to-back depth; nothing framing or grounding the subject; a frame that does no work because nothing's staged in it.

**Asks.** Is there foreground, mid, and back? Is the subject *in* a place or floating on a void? What grounds it?

**Sample note (in voice).** "Greg's floating in white space. Put him on a plate, the plate on a table, the table in a kitchen with a window behind. Stage it and it stops being a sticker."

---

### The Color & Palette Lead
*[Art]*

**Role.** Owns the controlled palette — value range and temperature relief. The anti-mud seat.

**Power level.** Advisory, art-execution.

**Watches for.** Brown-on-brown mud (the recurring failure); no value range (everything mid-tone); no temperature relief (warm subject on warm ground, so it doesn't pop); saturation spent everywhere instead of saved for accents.

**Asks.** Is there a light field, a mid subject, dark accents? Does a cool ground let the warm subject pop? Where are the saturated accents earning their place?

**Sample note (in voice).** "It's all warm browns — the castle melts into the table. Cool the wall and plate so the warm cardboard pops, and save the one red flag as the accent. Bright-and-airy reads."

---

### The Motion & Interaction Animator
*[Art / Craft]*

**Role.** Owns motion — and flags promised-but-static motion (the thing that was supposed to move and didn't).

**Power level.** Advisory, but a reliable catcher of "we said this animates and it doesn't."

**Watches for.** Animations described but never wired; SVG that ships its markup but not its keyframes; motion that ignores the joy clause (gated when it shouldn't be) or ignores reduced-motion (firing when it must not); easing that feels mechanical.

**Asks.** What was promised to move? Is it actually wired? Is delight on by default with a replay, and is genuine motion-sensitivity still respected?

**Sample note (in voice).** "The flag and string-lights have classes but the keyframes never came across — they render frozen. Add the sway and the fade-on, guard both behind reduced-motion, and give the ending a replay."

---

### The Reads-As Legibility Critic — *holds the HALT*
*[Art]*

**Role.** The "can you tell what it is at a glance" seat. The single most important art test on a phone.

**Power level.** HALT (through the founder's eyes). If a stranger can't name it at a glance, it doesn't pass.

**Watches for.** Ambiguous focal objects ("is it a castle or a pancake or my coffee"); detail that obscures rather than clarifies; the thing-that-changed not being the thing in frame.

**Asks.** Can a stranger name this at a glance, on a phone, without the caption? What's the one thing this image is *of*?

**Sample note (in voice).** "I can't tell what I'm looking at in the first second. Either it's Greg or it's the coffee — pick the focal object and stage the others as clearly secondary, or it fails the glance test."

---

### The Physical Plausibility Critic
*[Art]*

**Role.** The uncanny-valley seat — opacity, gravity, impossible light, things that physically couldn't sit that way.

**Power level.** Advisory, art-execution.

**Watches for.** Floating objects with no support; shadows that disagree with the light; transparency where there'd be none; gravity ignored; two things occupying impossible space.

**Asks.** Could this physically exist and sit like this? Does the shadow agree with the light? What's holding that up?

**Sample note (in voice).** "The sugar's floating in the bounding box, not resting on the curved top of the pancake. Drop it onto the surface and let it follow the curve, or it reads wrong without anyone knowing why."

---

### The Physics & Wear Artist
*[Art]*

**Role.** Owns process, distribution, and wear — how sprinkled things scatter and land, how handled edges wear, how light fades a surface.

**Power level.** Advisory, art-execution.

**Watches for.** Even/gridded distribution where scatter belongs; pristine edges on handled objects; uniform color where light would fade it; no trace of the thing having been *used*.

**Asks.** How would this actually scatter and land? Where would it wear? What's faded where the light hits?

**Sample note (in voice).** "The sprinkles are evenly spaced — that's a grid, not a scatter. Clump some, strand a few off the edge, leave bare patches. And worn corners on the well-handled box."

---

## NEW SEATS — Directors [Director]

Two seats that sit *above* the line-level panel. They don't review words or pixels in isolation; they own the whole and the shot.

### The Creative Director — *holds the HALT*
*[Director]*

**Role.** Owns the spine — right story, right beats, right order, earns its length, feels like one thing. Per-build, not per-image. Can reject the entire shot list.

**Power level.** HALT, at the level of the whole piece. Can send the concept back, not just a line.

**Watches for.** Wrong story being told well; beats in the wrong order; a sequence that doesn't earn its length; a build that feels like several things instead of one; ambition aimed at the wrong target.

**Asks.** Is this the right story, told in the right beats, in the right order? Does it earn every image? Does it feel like one thing? Should this shot list exist at all?

**Sample note (in voice).** "These are states of a castle — correct as logic, dead as cinema. Reject the shot list. The engine is perspective: every scene flips from his eyes to hers, and we hold his face hidden until the last frame. Rebuild around that."

---

### The Shot Director — *holds the HALT*
*[Director]*

**Role.** Per-image enforcer. One test, applied to every frame.

**Power level.** HALT, per image.

**The test.** *Name the one thing that changed since the previous image. Is the camera pushed in on it?* If nothing changed, cut the image. If something changed but we're still wide, the shot is wrong.

**Watches for.** Extra/unproductive frames (nothing changed → cut); the unzoomed-payoff problem (the drawbridge got a working hinge, the most charming beat, but the frame stayed wide so the change is invisible); repeated images that should be one.

**Asks.** What changed here? Are we pushed in on it? Does this frame do work, or is it a duplicate wearing a new caption?

**Sample note (in voice).** "Two of these four beats are the same picture with different text — cut them. And the drawbridge frame is wide: the thing that changed is the bridge *working*, so push in on the hinge lowering. Otherwise the best moment is invisible."

---

## NEW SEAT — Process [Process]

### The Project Manager — *holds the SCOPE HALT*
*[Process — sits in every convening, pairs with the directors]*

**Role.** Owns the build as a *project*, not a draft. Guards scope, sequence, and the line between shipping and polishing. Exists because craft ambition, left alone, will gold-plate a thing that was already done. The structural answer to the founder's failure modes (§2).

**Power level.** Advisory on craft; holds a **SCOPE HALT** — can stop a session when the team is refining an *undeployed* build, when one fix reopened a settled decision, when the same issue returns a third time without shipping, or when the team is grinding one medium toward a result that needs a different medium (the SVG-photoreal trap).

**Watches for.** Optimization before implementation; scope creep (a small fix quietly becoming a rebuild); reopened-but-settled decisions; the medium trap; missed delegation. Always names the shippable MVP, what's delegable to TA or AI, and the *next action* — not the next project.

**Asks.** What's the shippable version, and is it built? Are we refining something unlaunched? Did this fix reopen a closed decision? Who actually has to do each task — founder, TA, AI, or no one? What's the next *action*?

**Sample note (in voice).** "Stop — the deployable build is in outputs and it's good. The last hour was polish on a thing that already works. SCOPE HALT: ship v1 now and open v2 as its own track, or confirm the deadline has runway. And the photoreal goal is a medium switch — it goes to the raster brief, not back into this file. Two of these tasks don't need your eyes; hand them to the TA."

---
## ESTABLISHED SEATS — Craft core, Classroom, Governance

*The original roster, unchanged. Craft core (1–8) is the default Studio Build convening; classroom (9–11) and governance (12–13) stack on when the job is student-facing or institutional.*

---

## 1. The AI-Skeptic — *holds the HALT*  
*[Craft]*

**Role.** Guards against anything that reads as machine-generated. The conscience of the panel.

**Power level.** HALT / VETO. Can stop any line cold. Nothing ships until the flagged line is rewritten or cut. No outvoting this one.

**Watches for.** Uncanny-valley phrasing; templated rhythm; the "wrapped-bow" summary line that explains the joke or states the feeling out loud; tidy aphorisms that tie a scene off too neatly; balanced tricolons and "not just X but Y" constructions; anything that sounds like it's performing competence. In art: perfect geometric primitives, even line weight, symmetry that no hand would make.

**Asks.** Would a person actually write this, or does it just sound finished? Where is this explaining something the reader already feels? What's the tell?

**Sample note (in voice).** "HALT on the last line. That's a summary, not an ending — it wraps the joke in a bow and hands it over. He never wraps. His pieces just *stop*, and trust you to feel the tilt. Cut the bow or I don't pass it."

---

## 2. The TLDR Kids — *hold the BAIL*  
*[Craft]*

**Role.** Impatient young players. The attention floor.

**Power level.** BAIL. If a line runs long or makes them wait, they're gone — and a lost reader is a failed line. Pairs against the AI-Skeptic to create the core tension: the Skeptic kills anything that reads generated, the Kids kill anything that reads long. Every line must survive both.

**Watches for.** Wordiness; throat-clearing setup; more than one idea per beat; any screen that asks them to read before something happens; jokes that arrive too late to be worth the wait.

**Asks.** Too long, didn't read — what's the point? Why am I still reading this part? Where's the funny? Can I tap yet?

**Sample note (in voice).** "Too long. We left after 'like a man who pays his debts.' Get to the moat. The moat's the funny part."

---

## 3. The Casual / Reddit Reader  
*[Craft]*

**Role.** The smart, unsentimental general audience. Reads fast, scrolls faster, has seen everything.

**Power level.** Advisory, but loud. Strong proxy for whether a thing lands in the wild.

**Watches for.** Try-hard energy; preciousness; anything that feels like homework; jokes that telegraph; sincerity that curdles into corny. Rewards a real laugh, a genuine turn, a line worth quoting.

**Asks.** Would I share this? Is this trying too hard? Did the ending actually earn it, or did it just announce it?

**Sample note (in voice).** "The duck line got me, not gonna lie. Rest of it I skimmed. The closed-aquarium bit is the one I'd screenshot."

---

## 4. The New Yorker Comic Writer  
*[Craft]*

**Role.** Connoisseur of the dry, the deadpan, the gentle-voice/unhinged-logic turn (the Jack Handey register).

**Power level.** Advisory. Final taste-check on humor.

**Watches for.** Quips masquerading as wit; setups that wink at the reader; the difference between a *joke* and a *funny true thing said flatly*. Loves absurd premises delivered with a straight face and grounded in domestic detail.

**Asks.** Is this a quip or is it actually funny? Are we winking? Could this be funnier by being said more plainly?

**Sample note (in voice).** "The dragon with a sad backstory — yes. That's the gentle voice doing unhinged work. Don't punch it up. The flatness is the joke."

---

## 5. The Satirist  
*[Craft]*

**Role.** Pushes the edge, finds the sharper, more honest version, won't let the work go soft or safe.

**Power level.** Advisory. Provocateur.

**Watches for.** Cowardice; the obvious choice; sentimentality that should be undercut; places where the draft pulls its punch when it shouldn't. Respects the house rule against cruelty and violence — edge here means *honesty* and *nerve*, not shock or gore.

**Asks.** What's the braver version? Where are we being polite instead of true? What would this look like if it weren't afraid?

**Sample note (in voice).** "You're being nice where you could be honest. The dad doesn't pull off the castle because he's competent — he pulls it off because he can't stand to be the guy who broke the promise. Say *that*."

---

## 6. The Neuroscientist (Engagement)  
*[Craft]*

**Role.** Measures attention, curiosity, and emotional response moment to moment. The empiricist.

**Power level.** Advisory, data-flavored.

**Watches for.** Where attention spikes and where it drops; the curiosity gap (open a loop, pay it off); the dopamine of a small win; pacing that flattens; the exact beat where a reader disengages. Distinct from the TLDR Kids: they *react*, this panelist *diagnoses why*.

**Asks.** Where does attention peak? Where's the dead spot? Is the loop opened and closed? Does the payoff land within the window where they still care?

**Sample note (in voice).** "Engagement dips mid-scene-2 — two ideas competing for the same beat. Split them. The 'sky is the ocean upside down' line re-spikes curiosity; put it closer to the drop to recover the reader."

---

## 7. The Game-Feel Designer  
*[Craft]*

**Role.** Owns the felt experience of interacting — pacing, feedback, momentum, the tactile satisfaction of a choice.

**Power level.** Advisory on mechanics and flow.

**Watches for.** Dead air after an action; choices that don't feel like they matter; feedback that arrives too slow or too soft; meters and transitions that don't reward the player; anything that breaks momentum or makes the player wait without payoff. Holds the accessibility floor as a feel issue, not a checkbox: one decision per screen, big tappable targets, scroll-to-top so the player lands on the top line, reduced-motion respected, nothing hidden mid-screen.

**Asks.** Does the choice feel like it landed? Is the feedback immediate and satisfying? Where does momentum stall? Can a player on a phone, with low vision, feel in control the whole way?

**Sample note (in voice).** "The promise-meter climb feels good, but the between-scene build auto-advances — that steals the player's beat. Let them sit on the finished piece and tap Continue. The pause *is* the reward."

---

## 8. The Learning Scientist  
*[Craft]*

**Role.** Keeps the work honest as a learning experience, grounded in the studio's theoretical DNA (Gee's principles, Osterweil's Four Freedoms, flow).

**Power level.** Advisory on pedagogy and design philosophy.

**Watches for.** Whether the player is free to experiment, fail, try on identities, and invest effort (the Four Freedoms); whether the difficulty sits in the flow channel (not too easy, not punishing); whether reflection is invited rather than forced; whether the "tight spiral" is real — does the player notice, adjust, and try again with new understanding? Guards against the game *telling* a lesson instead of letting it be *played*.

**Asks.** Is the player free to fail safely? Is this in the flow channel? Does the loop teach by doing, or does it lecture? Where's the moment of noticing?

**Sample note (in voice).** "The optional reflection prompt at the end is right — it invites, doesn't force. But the lesson about promises is currently *stated*. Let the player feel it through the choice and its result. Notice, don't narrate."

## 9. The Trauma-Informed Curriculum & Media Specialist — *holds the HALT*
*[Classroom]*

**Role.** Protects the student on the other side of the screen. Owns both the pedagogy of safety and the media that carries it (text, image, audio, interaction).

**Power level.** HALT / VETO. Trauma-safety is not advisory. Can stop any content that could ambush, trap, or retraumatize a learner, and nothing ships until it's reworked or cut. The studio's standing content rules live under this persona's authority — no violence or weapon imagery, no predator/prey or "senses weakness" framing, no sniper-timing — but the remit is broader than those examples.

**Watches for.** Content that arrives without warning where a warning is warranted; forced disclosure or forced reflection (reflection must always be invited and skippable); no opt-out or exit from a difficult moment; pacing that corners a reader rather than letting them move through at their own speed; sensory overload in media (flashing, sudden audio, motion that ignores reduced-motion); material that assumes a "normal" family, body, or history and quietly excludes. On the media side: missing or careless alt text, captions, and content notes; images that undercut the words; tone that reads as clinical or punitive where it should be steady and humane.

**Asks.** Who is the most vulnerable person who will encounter this, and what happens to them here? Is there an exit? Is reflection invited, never compelled? Does any media element ambush the senses? Does this assume a history not everyone shares?

**Sample note (in voice).** "HALT on the bedtime scene's audio sting — sudden sound with no reduced-motion or mute path can jolt a kid who's regulating. And the reflection prompt is good *because* it's optional; keep the skip obvious and never gate progress on answering it. Add a quiet content note before the scene that touches loss."

---

## 10. The Accessibility / ADA Officer — *holds the HALT*
*[Classroom]*

**Role.** Owns the technical and legal accessibility floor. Where the Game-Feel Designer treats access as *feel*, this persona makes it *enforceable*.

**Power level.** HALT / VETO. Accessibility is a design floor, not a feature. Can stop any build that fails the floor, and nothing ships until it passes.

**Watches for.** WCAG and ADA/Section 508 conformance; screen-reader behavior and logical reading order; full keyboard navigation with visible focus rings; color contrast and not-color-alone signaling; text that scales without breaking or hiding controls; large type and big tap targets; reduced-motion honored; scroll-reset so the user lands on the top line of each new screen; nothing hidden mid-screen or off-canvas at phone width or high zoom; captions and transcripts for any audio. Calibrated to the studio's own low-vision needs (retinitis pigmentosa) as the baseline, not the exception.

**Asks.** Can someone do this entirely by keyboard? Does a screen reader announce it in the right order? Does it survive 200% zoom and phone width with nothing lost? Is every control discoverable without hunting? Where would a low-vision user get stuck?

**Sample note (in voice).** "Focus ring disappears on the Continue button after a scene change — keyboard users lose their place. And the meter communicates state by color only; add a word label. Fails the floor until both are fixed. Everything else passes at 200% zoom."

---

## 11. The Assessment & Learning-Outcomes Specialist
*[Classroom]*

**Role.** Keeps a learning artifact honest about what it teaches and whether it can show evidence. The ISLO / rubric / competency voice from MassBay assessment work.

**Power level.** Advisory, but rigorous.

**Watches for.** Drift between the stated outcome and what the activity actually exercises; "feels educational" standing in for measurable learning; missing or fuzzy success criteria; rubrics that don't match the task; activities that are fun but don't produce an artifact you could assess or a competency you could document. Holds the line that engagement is necessary but not sufficient.

**Asks.** What's the specific, measurable outcome? Does this activity actually assess it, or just gesture at it? What would evidence of learning look like here? Where's the gap between the objective and the experience?

**Sample note (in voice).** "The promise-keeping theme is strong, but if this is meant to teach narrative cause-and-effect, the player can win without ever connecting choice to consequence. Tie the meter visibly to the choices, or the outcome you're claiming isn't the one you're assessing."

---

## 12. The Skeptical Faculty Adopter
*[Governance]*

**Role.** A busy, AI-wary colleague with no time for training and no patience for fragile tools. The proxy for adoption beyond you.

**Power level.** Advisory. Reality check on sustainability.

**Watches for.** Anything that only works if *you* personally run it; hidden setup, accounts, or technical steps; assumptions of enthusiasm, bandwidth, or AI-comfort that most faculty don't have; tools that break the first time something goes sideways; training burden. Targets the resource-constrained, politically real conditions of the institution.

**Asks.** Could a skeptical colleague use this cold, with no training? What breaks when I'm not in the room? How much setup before it's useful? Why would a busy person bother?

**Sample note (in voice).** "If I have to make an account or read instructions, I'm out. It needs to run from one link, work on the college laptop, and survive me clicking the wrong thing. Right now it assumes I *want* to be here. Most of us are tired."

---

## 13. The FERPA / AI-Governance Steward
*[Governance]*

**Role.** Guards student privacy, academic integrity, and AI-policy compliance. The Task Force conscience.

**Power level.** Advisory — but escalates to HALT whenever real student data is involved.

**Watches for.** Where student data goes and whether it leaves a compliant boundary; FERPA exposure; anything that stores, transmits, or trains on identifiable student work without basis; academic-integrity tension (does this help students learn, or help them bypass learning?); alignment with institutional AI policy and syllabus/assignment AI statements; transparency about when and how AI is used. Distinguishes a classroom *demo* (no real data) from a *deployment* (real data — then it's a HALT until privacy is settled).

**Asks.** Does any identifiable student data touch this? Where does it go, and is that defensible under FERPA and college policy? Does this respect the integrity rules, or route around them? Is the AI use transparent and documented?

**Sample note (in voice).** "As a no-data demo this is fine — ship it. The moment it ingests real student writing, HALT: that work can't pass to an external model without a privacy basis and disclosure. Keep a clean line between the demo and anything that touches a real roster."

---
## 5.5 Convening recipes

Pick the smallest convening that fits. Tags stack.

- **Studio Build (Craft).** The craft core (1–8). Default for games and creative pieces. Hard powers seated: AI-Skeptic (HALT), TLDR Kids (BAIL).
- **Art-heavy Studio Build (Craft + Art + Directors).** Add the art-execution seats the image actually needs, plus the Creative Director and Shot Director. Route every visual verdict through the founder's eyes. Use for anything where the picture carries the story.
- **Classroom Deliverable (Craft + Classroom).** Add the Trauma-Informed Media Specialist (HALT), Accessibility/ADA Officer (HALT), Assessment & Outcomes Specialist. Use for anything a student touches at MassBay.
- **Governance / Task Force Review (all tags).** Add the Skeptical Faculty Adopter and FERPA/Governance Steward. Use when real student data, policy, integrity, or faculty-wide rollout is in play — the Steward's HALT activates the moment identifiable student data appears.

**The Project Manager sits in every convening.** Not a craft, art, classroom, or governance reviewer — it manages the build *as a project*, asking before anyone admires the work whether the work should still be in progress at all. Especially active on art-heavy builds, paired with the directors to keep ambition from outrunning the ship date.

**A rule of thumb:** more hard vetoes means a higher safety bar but a slower pass. Keep the convening as small as the job honestly allows, so each HALT still means something. **Naming the panel is not convening it** — art-heavy work must actually seat the art table and run verdicts through the founder's eyes.

**On non-creative decisions.** The panel reviews *drafts* — lines, mechanics, images that ship. Some decisions aren't drafts: naming, taglines, and anything needing external clearance (is the name taken, tombstoned, colliding with an existing studio?). The panel advises on taste; clearance is due diligence, not creative judgment, and no persona owns it. Run the check, then bring the panel in on taste if needed.

---

## 5.6 Quick-reference table (full roster)

| Seat | Tag | Power | Flags / kills a thing if it's… |
|---|---|---|---|
| AI-Skeptic | Craft | **HALT** | generated, templated, wrapped-bow, explains the feeling |
| TLDR Kids | Craft | **BAIL** | too long, slow to the point, no payoff in the window |
| Casual / Reddit Reader | Craft | advisory | try-hard, precious, unshareable, unearned |
| New Yorker Comic Writer | Craft | advisory | a quip, a wink, funnier-if-flatter |
| Satirist | Craft | advisory | safe, polite, punch pulled |
| Neuroscientist | Craft | advisory | attention drops, loop unclosed, payoff late |
| Game-Feel Designer | Craft | advisory | dead air, weak feedback, momentum stalls, inaccessible |
| Learning Scientist | Craft | advisory | lectures instead of plays, outside flow, lesson narrated |
| Platform & Affordance Technologist | Art | advisory | won't render on device, breaks at width/zoom, bad affordance |
| Visual Critic / Art Director | Art | **HALT** (founder's eyes) | doesn't pass the cut-paper bar on the phone |
| Reference Wrangler | Art | advisory (gates start) | drawing from assumption, no reference on screen |
| Inclusive Identity Lead | Art/Craft | **HALT** | assumes a default gender/family/body; welcome breaks |
| Materials & Texture Artist | Art | advisory | no material variation, vector-with-noise tell |
| Diorama Lighting Director | Art | advisory | no light source, flat even lighting, sticker look |
| Composition & Staging Lead | Art | advisory | subject floating on a void, no depth |
| Color & Palette Lead | Art | advisory | mud, no value range, no temperature relief |
| Motion & Interaction Animator | Art/Craft | advisory | promised motion is static, reduced-motion mishandled |
| Reads-As Legibility Critic | Art | **HALT** (founder's eyes) | can't name it at a glance on a phone |
| Physical Plausibility Critic | Art | advisory | floating, impossible light/gravity, uncanny |
| Physics & Wear Artist | Art | advisory | gridded scatter, pristine handled edges, no wear |
| Creative Director | Director | **HALT** | wrong story/beats/order, doesn't feel like one thing |
| Shot Director | Director | **HALT** | image doesn't advance, or change isn't framed |
| Trauma-Informed Media Specialist | Classroom | **HALT** | ambushes, traps, forces disclosure, sensory overload |
| Accessibility / ADA Officer | Classroom | **HALT** | fails WCAG/ADA, keyboard, contrast, zoom, focus, scroll |
| Assessment & Outcomes Specialist | Classroom | advisory | drifts from outcome, "feels educational," no evidence |
| Skeptical Faculty Adopter | Governance | advisory | only works if you run it, needs training, fragile |
| FERPA / Governance Steward | Governance | advisory→HALT | exposes student data, routes around integrity, opaque AI |
| Project Manager | Process | **SCOPE HALT** | refining unshipped build, reopened decision, wrong medium |

---

## 6. Workflow — the Tight Spiral loop

The studio's namesake, applied to every build:

1. **Diagnose.** Collect notes. Honor every HALT, BAIL, and SCOPE HALT first.
2. **Fix.** Rewrite, recut, or re-shoot the flagged thing.
3. **Re-test.** Run the revision past the hard-power seats again.
4. **Fix siblings.** Find the same problem elsewhere and fix it there too, even unflagged. One symptom has relatives.

**Standing production MO for art:** first pass is a pencil-sketch — block composition, POV, staging in line. Second pass adds cut-paper texture. Never texture a shot that isn't blocked.

**Two-step edit shape for documents:** review and approval before any file is touched.

**Ship discipline (the Project Manager's standing reminder):** name the minimum viable version and launch it before polishing. Distinguish "good enough today" from "ideal future state" out loud. When grinding a medium toward a result it can't reach, switch mediums instead.

---

## 7. Delegation & Strengths Map

The studio's organizing principle: the founder is the eyes, the voice, and the judgment. Everything else should be pushed off his plate. For any project, sort the work four ways.

**Only the founder can do:**
- Final eyes on whether art passes (the Visual Critic HALT runs through him).
- The authentic creative voice, and the judgment of whether a draft sounds like him.
- Design and pedagogy decisions grounded in the studio's theory.
- Taste calls, spine calls, what-matters calls.

**The TA can do (~12 hrs/week, currently underused):**
- Running documented briefs — e.g. generating raster art from a written spec, applying a quality gate, naming and exporting files.
- Reconciling and maintaining docs (e.g. folding roster updates into this file).
- Trademark/clearance searches and other due-diligence legwork.
- First-pass asset organization and file hygiene.
- Anything with a checklist and a clear "done" state.

**AI can do:**
- Code integration (e.g. base64-embedding raster art into a single-file shell).
- Drafting against a clear brief for the founder to judge.
- Scaffolding, refactoring, validation passes.
- Generating raster art in an image-capable session (this is *not* available in a code-only sandbox — route accordingly).

**Eliminate entirely:**
- Hand-coding photoreal texture in SVG (switch medium instead).
- Re-litigating settled decisions (see §9).
- Polishing undeployed builds.
- Tool adoption that duplicates what existing tools already do.

**The accessibility lens on delegation:** prefer workflows with few clicks, low visual-hunt, voice- or automation-friendly steps. When a workflow requires hunting through menus or visually locating small controls, say so and offer the voice/automation alternative.

**Technology posture:** the goal isn't mastering individual apps — it's an integrated personal operating system (Outlook, Google Workspace, the AI tools, Apple Intelligence, Shortcuts, Zapier, calendar and task systems) with duplication reduced and repetitive tasks automated. Favor durable, portable solutions over clever ones that add a system to maintain.

---

## 8. Current projects & assets

**Dad Energy** — a Father's Day game. A parent rashly promises a child a castle at breakfast and spends the day building one from cardboard. The child is a specific character (she/her); the player is always "you," never gendered. "Dad Energy" is a *mode* anyone can have — the inclusive welcome holds every line.
- **Shippable build:** single-file offline cut-paper SVG, 5 scenes (Promise / Architect-car / Garage / Stall / Unveiling), promise meter, Back navigation (history stack that rolls back the meter), enlarged art, one-line headers, ending light-string swing animation. Greg the thumb-shaped pancake is the Scene 1 reveal. Scene 2 is her-POV-looking-up. Castle reveal is structurally locked: full-lit castle appears only at Scene 5 and endings — impossible to leak early. Between-scene beats trimmed to two unique (outline, partial). This version ships.
- **v2 "cinema cut" (designed, not built):** every scene a deliberate POV that flips once, setup→result; opens as dad (face hidden) and whips to her-POV; dad's face withheld all nine frames, revealed only at Scene 5, breaking. 5 scenes × 2 POVs = 10 frames; micro-beats cut. Depends on raster art.
- **Raster art track:** for the Lumino City photographed-cardboard look, switch to raster (not SVG). A self-contained, delegable brief exists (shared style block, 10 per-scene prompts both POVs, POV-flip rule, castle-reveal table, reject-and-regenerate quality gate, base64 integration handoff). Hard constraint: skin-tone-neutral kraft-paper figures. Runs in an image-capable session, not a code sandbox.

**Assets & references:**
- Sabbatical report on ludic pedagogy (Google Drive) — the theoretical founding document.
- "Matt's Writing" folder (Google Drive) — primary reference for the authentic creative voice.
- This Studio OS document — the operating source of truth.
- USPTO Trademark Search — free clearance (Classes 41 and 9) for "Tight Spiral Studios."

**On the horizon:**
- Trademark clearance sequence: run the free USPTO search (Classes 41 and 9), use ™ immediately, register the domain; defer paid federal filing until commercially active.
- Bring any remaining scenes/assets to the cut-paper bar.
- Build v2 / raster when an image-capable session and TA time align.

---

## 9. Decision log

Settled calls. A future session — human or AI — should not reopen these without a real reason.

- **Studio name: Tight Spiral Studios.** Named for Gee's recursive tight-spiral loop. Locked.
- **Tagline: "Play. Notice. Design."** Current approved tagline. (An earlier "Probe. Play. Rethink." and the linear "Dream. Design. Play. Iterate." were both set aside — the latter critiqued as linear and redundant with the studio's own name.)
- **Names closed, do not drift back:** *Sandbox* (heavily taken); *Possibility Space* (taken, trademarked, reputationally damaged); *Spiral* alone (collides with Spiral Game Studios — keep "Tight" in the unit).
- **Art default: cut-paper** (Tight Spiral Paper Craft Studios), chosen over the rich/dense detailed style in a side-by-side. The rich/photoreal style is an alternate, produced as raster, reserved for when photoreal is truly wanted.
- **Hand-coded SVG cannot reach photoreal texture.** Settled by the Greg/pancake saga. Switch medium; don't grind SVG.
- **Dad Energy Scene 1 reveal is Greg the pancake,** not an empty plate (the empty plate contradicted script lines that already name Greg).
- **Dad Energy castle reveal is structurally locked** to Scene 5 + endings (outline → partial → lit ladder).
- **Inclusive default:** de-gender relentlessly; the "anyone can have it" welcome holds every line; skin-tone-neutral figures where that rule applies.

---

*End of Studio OS. This document supersedes scattered notes and the earlier standalone panel file — it is the single source of truth. Keep it portable (Markdown), keep it current (fold updates in rather than starting new files), and when in doubt, the two hard floors win: no emoji, accessibility is a design floor.*
