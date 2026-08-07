# SIX-MONTH CONSULTATION — Aleph panel, 2026-08-07

*Five seats, run sequentially in one session against `CONSULT-GROUNDING-2026-08-07.md`. Not
five independent subagents — the parallel fleet hit the account's monthly spend limit before
producing output; this is the same panel run inline to fit a constrained budget. Grounded in
the repo's measured state and the repo's distillate of prior Claude-project chats
(`TSP_Ledger.md`, `HANDOFF-*`, `SESSION-*`, `rescued/shelf-*`) — the chats themselves are not
reachable from this container. Where a seat needed something it could not verify, it says so
rather than guessing.*

---

## SEAT 1 — STUDIO ARCHITECT

### Month-0 diagnosis

The architecture is sound in its bones and already showing the exact failure mode its own
literature predicted. `LANE-REGISTRY.md` (2026-07-11) opens: *"I told the founder Dad Energy
was lost... He replied with a URL."* That failure — a resolver that trusts a partial view —
is structurally the same failure this session found twice more: `STUDIO-GOVERNANCE.md`
asserting the belt was inert while it had run seven times, and three tools reporting clean
while silently dead (WeasyPrint uninstalled, two Chromium builds drifted). **The studio has
diagnosed this disease three times and built a different antibody each time** (`resolve_canon`,
the Tick Rule, Funes Tendrils, now the Aleph blind-spot register). None of the antibodies
retired the ones before them, so the studio is carrying four overlapping truth-verification
systems that were each built to fix the same wound.

Concretely:

1. **The hub was never on its own belt until today.** `belt.yml` was `workflow_call`-only
   with no stub. Five founder-ruled ticks existed as scripts nothing called. This is not a
   one-off miss — it is what "governance is veto, not optimization" (SWOT) looks like at the
   infrastructure layer: the enforcement mechanism itself needed the same discipline it enforces
   on games, and nobody pointed the gate at the gate.
2. **Canon has drifted lanes without retiring the old map.** `LANE-REGISTRY.md` and
   `cross-lane-manifest.md` (2026-07-10/11) describe a four-lane world — repo, Netlify, Drive,
   shelf — with `resolve_canon` required across all four before any edit. `COLD-START.md`
   (2026-07-13, "this file is law") narrows canon to **the repo alone**, Drive to "an address
   book," and never mentions Netlify. `FORKING-PATHS-PROTOCOL.md` (2026-08-03) then widens the
   lane list to **eleven** — repo, Netlify, two Drives, Dropbox, shelf, code sessions, chats,
   Cowork, iOS Notes, OneDrive. Three documents, three different lane counts, all currently
   "law," none marking the others superseded. A founder with RP cannot hold three overlapping
   maps in his head, and I could not verify from this session which one is actually followed —
   this session never checked Netlify, Dropbox, iOS Notes, or the second Drive for anything, and
   nothing HALTed for not doing so.
3. **`BUILD-DEBT.md`'s own ratio rule is being violated by the work that produced this
   consultation.** *"No session may add a governance artifact unless the prior session shipped
   a player-facing capability."* Today's session built: five belt ticks, the Aleph taxonomy, five
   lens briefs, a synthesis harness, a blind-spot register, a ledger, and now this document —
   zero player-facing capability shipped. I am not exempting myself from my own diagnosis: this
   consultation is itself evidence of the pattern it's describing.
4. **131 HTML surfaces, five gates, one person.** The SWOT's own line — "the moat is also a
   treadmill" — is arithmetic now: every new surface owes contrast, image floor, voice, entry
   grammar, and touch measurement. Nothing in the architecture currently makes a NEW surface
   cheaper to add than the 131st was.

### The phased plan

**Months 1–2 — collapse the truth-verification systems into one, and pay down the debt ratio.**
Do not build a sixth verification mechanism. Pick the one that's already closest to correct —
Funes Tendrils plus the Aleph ledger cover working-tree, unmerged branches, orphan pages, and
now assessment findings in one place — and fold `resolve_canon`'s four-lane check and the Tick
Rule's four ticks into it as *reports Tendrils already produces*, not separate scripts to
remember to run. Retire `LANE-REGISTRY.md` and `cross-lane-manifest.md` to `rescued/` with a
pointer, since `COLD-START.md` supersedes their canon claim and keeping three live "law" files
that disagree is the exact hazard COLD-START was written to kill. In parallel: no new gate, no
new taxonomy key, no new OS block ships until BUILD-DEBT's ratio is back in balance — pick one
of the 33 instruction-wall surfaces or the dead-button fixes found today and ship it first.

**Months 3–4 — make the belt cheap per surface, not just correct.** Right now every gate is a
subprocess launch against a fresh Chromium context. Batch the five ticks into one browser
session per file (open once, run all five probes, close) — this is an engineering cost, not a
governance one, and it is what keeps the treadmill from getting more expensive as the corpus
grows toward 200. Extend `studio-fingers.py` to drive transitions rather than probe load-only
(the corpus-wide touch blind spot found today) — this is the single highest-value gate fix
because it is currently zero coverage on every multi-screen game, not partial coverage.

**Months 5–6 — decide the lane question once, in writing, with the founder, and never again.**
Not a session's unilateral call — the SWOT names institutional adjacency and productizing the
gates as opportunities, both of which require a founder decision about whether Netlify/Drive
stay in the canon picture at all or get formally retired to "sharing only" as `CLAUDE.md`
already rules for Netlify. Land the decision as one file, retire the two/three that conflict
with it.

### What to stop building

- **No new OS block, gate, or taxonomy this quarter unless it retires an old one.** The studio
  has nine unmerged `os-block-*.md` files as of the 2026-07-14 manifest, claiming section
  numbers the OS text already uses. That merge was "founder call owed" three weeks ago and is
  still owed. Adding a tenth block without resolving the first nine is exactly the debt the
  ratio rule exists to stop.
- **Stop maintaining the four-lane and eleven-lane canon documents as if they're both live.**
  Pick one canon-resolution doctrine. `COLD-START.md`'s repo-only answer is simpler, more
  recent in spirit (2026-07-13 vs the earlier lane docs), and matches what this session actually
  did all day. Recommend it as the standing answer; recommend Forking Paths' eleven-lane sweep
  be scoped to *disputed-content* resolution only, not every session's default posture.
- **Do not build a sixth blind-spot/drift detector.** Fold new detection into Funes Tendrils and
  the Aleph ledger. Two is already one more than a solo studio can keep both green.

### The drift mechanism (concrete, checkable)

`STUDIO-GOVERNANCE.md` went stale within a day and nothing caught it because no check compares
a doc's *claims* against *live state* — every existing gate checks a *file*, never a *sentence
about infrastructure*. Concretely buildable: extend `funes-tendrils.py` with a **doc-staleness
tick** that greps governance docs (`STUDIO-GOVERNANCE.md`, `LANE-REGISTRY.md`, this file's own
successors) for dated status claims (`"as of 2026-...")`, `"currently ..."`, `"is inert"`) and
flags any such claim older than N days for re-verification, the same way the Instruction Wall
Queue flags stale defects. This is a report tick, not a blocker — consistent with Tendrils'
existing "always exits 0, never silently passes" contract.

### What I would refuse

I would refuse to add a sixth canon-resolution system, refuse to merge the nine unmerged OS
blocks without the founder present (the manifest already says the cross-references make a wrong
guess corrupt silently — that is not a call an agent should make alone), and refuse to recommend
"just check all eleven lanes every time" as the standing practice for a founder with limited
attention and RP — that is optimizing for completeness at the cost of the thing the studio says
it protects.

---

## SEAT 2 — FOUNDER OPERATIONS & ACCESS

### Month-0 diagnosis

`COLD-START.md` is already the correct answer to "how does the founder run the hub via
Claude" in its shape — compute, don't remember; four resident files; fetch the rest — and it
should not be reinvented. What costs the founder eyes and attention today is not the doctrine,
it's three things that sit *underneath* it:

1. **Auth friction has been solved three times in three weeks, and the fixes are not
   consolidated.** `TSP-GIT-LANE.md` (07-29) says get a 7-day PAT from Matt. `TSP-NOTOKEN-LANE.md`
   (08-06) supersedes it — Zapier OAuth, no token, ever. `HANDOFF.md` (07-16) documents a PAT
   that was **exposed in a transcript** and had to be rotated. This session found a fourth fact
   these three don't know: **an authenticated session container can push directly**, including
   to `.github/workflows/`, which the Zapier grant cannot reach. Four auth answers exist; only
   the newest (Zapier, no-token) is currently pointed to as the default, and it is *incomplete*
   — it cannot write workflow files, and nothing in the founder-facing docs says what to do when
   a workflow file needs to change. That's a real gap: the next time a belt tick needs adding,
   whoever is in the chat has to rediscover this session's finding from scratch.
2. **The single highest-friction moment for an RP phone user — approving a destructive or
   consequential action — has no fast path.** Every session in this transcript history that
   mattered (PAT rotation, the Confluence trunk merge, the nine unmerged OS blocks) required the
   founder to read and decide from a phone. `CLAUDE.md`'s own defaults say "one step at a time,
   no walls of steps" — but the *studio's* decision-owed items (nine section-number conflicts,
   a stale prospectus's PhD-adjacent framing, this session's INSTRUCTION-WALL-QUEUE) are not
   currently surfaced as single-decision cards; they sit in prose files a founder would have to
   read end to end to find.
3. **Session-stall survival depends on the operator remembering to run Tendrils, not on being
   forced to.** The Cold-Start doctrine is only followed if the session invokes it; this session
   did, because it happened to be primed with the CLAUDE.md defaults. Nothing structural prevents
   a future session from skipping straight to editing a resident-but-stale file.

### The operating loop recommended

Keep Cold Start's shape exactly. Add one layer on top of it, concretely:

```
SESSION OPEN
  1. Read the 4 resident files (unchanged from COLD-START.md).
  2. Run funes-tendrils.py . — report loose ends, never block.
  3. Run the doc-staleness tick proposed by Seat 1 — flag any governance
     doc whose dated claim predates the last belt run.
  4. Surface exactly ONE decision card if anything is founder-owed, phrased
     as a single yes/no/pick-one, not a document to read end to end.
     (Concretely: the nine unmerged OS-block section numbers become
     ONE card: "three files claim §12/§14, OS text already uses those —
     pick new numbers for the blocks, or I propose numbers, your call.")
SESSION WORK
  5. Mechanical work proceeds unasked, per the delegation default.
  6. Any destructive or consequential action gets ONE plain-language
     confirmation, never a menu.
SESSION CLOSE
  7. Land everything in git before the turn ends — never "ready to paste."
  8. Byte-verify what landed.
  9. Report in <150 words: what changed, what's owed, nothing else.
```

The auth layer should be one file, current, superseding the three that came before it:
**Zapier no-token for content; an authenticated session for `.github/workflows/`; a founder PAT
only for the "almost never" case `TSP-NOTOKEN-LANE.md` already names.** That's not a new
doctrine — it's `TSP-NOTOKEN-LANE.md` plus this session's one correction, landed as an edit, not
a fourth file.

### Phased plan

**Months 1–2:** consolidate the three auth docs into one current file (mechanical, unasked).
Add the doc-staleness tick to Tendrils' session-start report. Turn the founder-owed items already
sitting in prose (the nine section numbers, the ISLO gap brainstorm's un-decided items) into
single decision cards in `STUDIO-COMMAND-CENTER.md`'s "owed" section, one line each.

**Months 3–4:** arm branch protection so the belt has real agency (`STUDIO-GOVERNANCE.md`'s own
"Arming" section names this as owed to the founder's token — do it once, then it needs nothing
further from him). This is the single highest-leverage one-time action available: it turns five
ratcheted ticks from advisory into an actual wall, with zero ongoing founder attention after
setup.

**Months 5–6:** if the studio adopts Seat 5's productization recommendation, this is where a
second-user operating loop would need to exist — but not before there's a second user.

### What becomes a standing routine vs. stays ad hoc

**Standing:** Tendrils at every session open (already true). The doc-staleness tick (new).
Byte-verification after every push (already true, keep it).

**Ad hoc, deliberately:** which surface gets fixed next from the debt queues — that is craft
judgment, not a schedule. Do not automate "pick the next fix," only automate "here is the
ranked list."

### What I would refuse

I would refuse to build a founder-facing dashboard or app for this — `matt-radar` already exists
as the private lane and a second UI layer is exactly the kind of governance-without-shipping the
ratio rule forbids. I would refuse to put the eleven-lane Forking Paths sweep in the default
session-open path — it is disproportionate for a founder who needs *fewer* steps, not more
verification theater. And I would refuse to let auth documentation exist in three places again;
the next session that hits an auth question should find one current answer, not three dated ones
it has to arbitrate.

---

## SEAT 3 — LEARNING SCIENCE & EVIDENCE

### Month-0 diagnosis

The pedagogical spine is genuinely load-bearing, not decorative — Gee, Osterweil, Nunan, flow
theory, and the founder's own Pedagogy-of-Real-Talk lens are named with real design consequences
(the "spreadsheet of nouns" failure mode Real Talk forbids; Just-in-Time Expertise as a studio
practice, not just a game mechanic). That is unusually serious grounding for a solo studio at two
months.

The gap is not the theory. It is that **until 2026-08-07, nothing verified the theory actually
reached the build.** The first measurement found exactly the failure the theory predicts and
forbids: `the-tell.html`'s verdict logic (`mine.card===preset.card`, line 515) is a Nunan-task
betrayal in code — it grades *which card you picked*, never *the reasoning you wrote*, in a game
whose entire premise is defending a textual reading. Osterweil's "freedom to fail" requires the
failure to teach something; here, failing (or succeeding) produces the same templated response
regardless of what the student actually argued. This is not a small bug. It is the pedagogy
spine's own standard, unmet, and unmeasured until today.

### What evidence would actually count

To the founder: whether a student's *written reasoning* changes the outcome of a build, not just
whether the interaction is smooth. That is checkable per-build with the L5 lens now built — run
it before ship, not after.

To MassBay: the ISLO Gaps Brainstorm (2026-07-30, "living planning doc, not a commitment")
already named the two highest-value, lowest-cost measure-side builds independently from two
seats: the **EN Placement Skill-Scorer** (reuses the Norming Table engine, derives placement
from skill profile rather than entering it first — closes the founder's own named reflection gap
that EN98-vs-EN101 records no skill-level data) and **Rubric Forge** (unblocks four un-normed
outcomes at once). Both are ~80% built from existing engines per that doc. Neither needs a new
study — they need the existing scorer wired to real skill data from a real term.

To an outside adopter: one build where the L5 lens's `passed` list is long and its findings are
zero — proof the studio's own instrument, not just testimonial, certifies the pedagogy. That is
buildable in one iteration cycle on one file, not a multi-month research program.

### Phased plan

**Months 1–2:** run the L5 lens against every EN195 build already shipped (the ISLO suite, 11
pages, per the 2026-08-03 playtest fleet) and fix the `ASSESSMENT-MISALIGNED` /
`FEEDBACK-UNINFORMATIVE` class of findings first — these are the ones that most directly
contradict the pedagogy spine's own stated standard, and `the-tell.html` proves the class is
real, not hypothetical.

**Months 3–4:** wire one real term's data through the EN Placement Skill-Scorer as the ISLO
Gaps Brainstorm specifies. This produces the first real evidence artifact — per-skill placement
data — without inventing a new instrument.

**Months 5–6:** the oral-communication gap (ISLO 1, named by every seat in the 07-30 brainstorm
as the sharpest unbuilt outcome) is the one new build worth the governance cost, specifically
because the brainstorm already solved its hardest constraint: **capture prosody only — pace,
pauses, energy — never transcribe.** That keeps it offline-floor-compliant and sidesteps scoring
words/accent/dialect, which the dignity floor would otherwise forbid. This is the one place I'd
recommend genuinely new instrumentation, because the alternative (self-report only, current
state for ISLO 7 too) is not evidence at all.

### The instrumentation question

What should be captured: aggregate, per-skill signal (a placement level, a rubric dimension
score) — never a transcript of what a student wrote, never anything that could re-identify a
student outside the class roster the founder already controls. What must NOT be captured: raw
text sent anywhere off-device by default (the offline-first floor), any audio transcript (the
prosody-only design already exists for exactly this reason), and nothing that creates a FERPA
question the founder hasn't explicitly signed off on — the Workshop Vending Machine's live
Supabase backend is already the studio's one deliberate, RLS-verified, anon-insert-only exception
to offline-first; any new instrumentation should be held to that same bar, not a looser one.

### What I would refuse to claim

I would refuse to claim any of this "proves learning gains" without a real pre/post measure —
per-skill placement data and rubric-aligned scoring are evidence of *alignment*, not of *growth*,
and conflating them would be exactly the kind of inflated claim `CLAUDE.md` forbids. And per the
standing ruling, I would refuse — flatly — any framing that a build lets a blind student "play
the same game." There is no playtest behind that claim and the founder has never asserted it.
The defensible claim is narrower and still real: **this studio measures whether its own
pedagogy reached the build, and until today nothing did.**

---

## SEAT 4 — RISK, SUSTAINABILITY & SUCCESSION

### Month-0 diagnosis, ranked by likelihood × cost

1. **Silent tool failure — HIGHEST, because it has already happened three times.** WeasyPrint
   uninstalled (weeks of false-green render-proof), then two Chromium builds drifted
   (`playthrough-agent.py`, `studio-fingers.py`) on the same day. Each time the failure mode was
   identical: the tool errored, printed something, and continued — read downstream as "clean."
   This is not three unlucky incidents. It is one systemic gap: **nothing in the studio verifies
   that a gate actually ran before trusting its silence.** Likelihood: certain to recur, because
   the studio's tool count keeps growing and each one is a fresh chance to drift. Cost: it is the
   single failure mode that makes every OTHER measurement in this studio unreliable, because a
   gate you can't trust to fail loudly is a gate you can't trust at all.
2. **A governance doc asserting a false state — SECOND HIGHEST.** `STUDIO-GOVERNANCE.md` said
   the belt was inert; it had run seven times, one of them red for three days, unread.
   Likelihood: also near-certain to recur — every dated status claim in every governance doc
   decays the moment infrastructure moves and nobody re-checks it. Cost: lower per-incident than
   #1 (a wrong belief about the belt didn't break a build), but it compounds — a founder or a
   future session making a decision on a stale doc's authority is the exact shape of loss
   `LANE-REGISTRY.md` was written to stop.
3. **Bus factor — structurally the worst number in the studio, currently unaddressed.**
   Everything routes through one person's eyes, voice, and judgment (SWOT, named explicitly).
   That is a design choice with real upside (coherence, taste, honesty) and one catastrophic
   failure mode: if the founder is unavailable for a month, **nothing in the current
   architecture tells a cold session what to do next.** `COLD-START.md` tells a session how to
   *begin*; nothing tells it what's *owed* in priority order without reading prose end to end.
4. **Debt volume vs. debt visibility — currently an asset, but only because it's freshly
   counted.** 122 files carry entry-paint debt, 104 carry voice debt, 25 carry comfort debt, 131
   carry image-floor debt (post re-seed). That is a *lot* of carried debt for a two-month studio.
   It is currently an asset — visible, counted, ratcheted, shrink-only — specifically because
   every baseline was seeded today with a "why" and a date. The risk is not the debt; it's that
   an unmaintained baseline six months from now, seeded once and never revisited, becomes exactly
   the "permanent amnesty" this seat was asked to check for. A ratchet nobody looks at is a wall
   nobody remembers building.

### The silent-failure class — the general defence

The three tool failures share one shape: **exit code or continuation masked an unmet
precondition.** The studio's own rule — "if a rule can't be a check, it's a wish" — points
directly at the fix: every gate that depends on an external resource (a browser binary, a
network mount, a rendering engine) should assert that resource is present and *working* before
it claims to have measured anything, the same way `ratchet.py` already refuses to certify clean
on a sweep that exited 2. Concretely buildable, cheap, and general: a one-line self-check at the
top of every `sync_playwright()` call — launch, screenshot a blank page, confirm non-zero bytes
— before the gate trusts any subsequent probe. Three gates need this retrofitted today
(`studio-eyes-sweep.py`, and the two fixed this session already got the fallback but not a
loud self-check). This is worth doing before any new gate is added, because a sixth gate is a
sixth chance to drift silently.

### Debt strategy

The ratchets are an asset **conditionally** — the condition is that someone re-measures them on
a cadence, not once at seeding. Recommend: the doc-staleness tick Seat 1 proposed should also
flag a baseline file whose seed date is more than N weeks old with no `--init` re-run, the same
logic applied to debt as to prose claims. Otherwise six months from now these four baseline
files are indistinguishable from the "permanent amnesty" this seat was built to catch.

### Bus factor / succession

What must be true for a cold session to pick this up: it already mostly is, via `COLD-START.md`.
What's missing is a **priority-ordered owed list** that doesn't require reading nine prose files
end to end — this is the same fix as Seat 2's decision cards, viewed from the succession angle
instead of the attention angle. Recommend one file, machine-generated (not hand-maintained,
because a hand-maintained "what's owed" list is itself a staleness risk): a script that greps
every governance doc for "owed," "founder call," and dated status claims, and emits one ranked
list. That is the actual bus-factor fix — not more documentation, a query over the documentation
that already exists.

### Phased plan

**Months 1–2:** the self-check retrofit on every Playwright-dependent gate. The doc-staleness
tick. The machine-generated "owed" query. All three are cheap, all three close the failure class
that has already cost real time three times.

**Months 3–4:** a debt re-measurement cadence — re-run `--init` on all four ratchet baselines
monthly, diff against the prior baseline, and report growth vs. shrinkage as a single number in
`STUDIO-COMMAND-CENTER.md`.

**Months 5–6:** revisit whether the studio's governance-doc count itself needs consolidation
(this is Seat 1's finding, and it's a risk finding too — three "law" documents disagreeing about
the lane count is a bus-factor problem, not just an architecture one).

### What I would refuse

I would refuse to recommend more redundant verification layers as the fix for silent failure —
the fix is making the failure LOUD, not checking twice. I would refuse to let debt ratchets run
past six months without a re-measurement discipline attached, because an unaudited ratchet is
worse than no ratchet — it looks like governance while functioning as amnesty. And I would refuse
to treat "the founder is the bus factor" as solvable by anyone but the founder — no seat should
recommend diluting his judgment to reduce risk; the fix is making his judgment easier to exercise
with less reading, not replacing it.

---

## SEAT 5 — PROOF & POSITIONING

### Month-0 diagnosis

What a stranger encounters today at `index.html`, measured, not assumed: **174 words and 1.88
screens before a phone reader reaches the first action, 2% entry image against the studio's own
>50% floor.** The storefront itself carries the exact defect class (`INSTRUCTION-WALL`,
sub-floor image) the studio spent this session teaching its gates to catch. That is the first
finding, and it is uncomfortable on purpose: before any external claim gets made, the front door
should clear the studio's own floor.

What the studio can honestly claim right now: a working, theory-grounded, accessibility-first
game engine with genuine CI-grade craft enforcement — that much is real and verified. What it
cannot yet claim: any outcome, any adopter, any evidence that a student learned something because
of a build (Seat 3's finding — the pedagogy spine existed unmeasured until today, and the first
measurement found a build whose grading logic doesn't read what the student wrote).

### The one legible win

**Productize the gates, not a game.** Argued against the alternative (ship one flagship game as
proof): a single game's proof value is deniable — "it's one build, cherry-picked, made by its own
author." The gates' proof value is not deniable in the same way, because they are **arithmetic
run against the studio's own corpus, output already exists, and the finding pattern (three
silently-blind tools, a governance doc stale within a day, 33 instruction walls, a grading bug
that ignores student reasoning) reads as rigor, not marketing.** This is also the SWOT's own
named opportunity ("productize the gates... a quality OS other educators/builders would want")
and it is honest in a way a single-game pitch cannot be: it does not require asserting the games
teach, only that the studio checks whether they do — which is demonstrably, freshly true.

Audience: not a general market. MassBay's AI Task Force and accessibility offices, where the
adjacency SWOT names is real and specific, and where "here is our own instrument finding our own
bugs, in public" is a credible pitch precisely because it is not a sales pitch.

Honest caveat this seat must state: **a one-person studio cannot support external users of a
gate suite.** Recommend the "product" be the methodology and findings, published (Seat 3 and the
paper-series-prospectus already name this lane — Paper I is drafted to exactly this audience),
not a supported tool. Selling support the studio can't staff would be the inflated claim
`CLAUDE.md` forbids, applied to capability rather than pedagogy.

### Phased plan

**Months 1–2:** fix the front door. `index.html` clearing its own >50% image floor and
`INSTRUCTION-WALL` is table stakes before anything gets shown to an outside reader — showing an
accessibility-first studio's own storefront failing its own accessibility gate is the single
easiest way to lose the room.

**Months 3–4:** write Paper I of the prospectus (already drafted, feeds from existing files) with
today's finding as its sharpest exhibit — not "we built gates," but "we built gates, ran them on
ourselves, and here is exactly what they found, including in our own governance docs." That is
the honesty differentiator made legible without a disclaimer wall: the proof is a receipt, not a
warning label.

**Months 5–6:** one MassBay-adjacent showing (not a launch, a conversation) using Paper I plus
the EN Placement Skill-Scorer's first real-term data (Seat 3's build) as the evidence pair —
engine rigor plus one real outcome artifact, together, which is exactly what the SWOT says the
studio currently lacks.

### The honesty constraint as positioning

The founder has already ruled: pull back on disclaimers, say the thing plainly. Applied here —
the finding that "our own governance doc was wrong within a day, and here's the arithmetic that
caught it" is not a caveat to bury, it is the pitch. A studio that can show its own quality
mechanism catching its own quality mechanism failing is more credible than one that claims
nothing ever goes wrong. That is legible without a wall of qualifiers because it's one story
(this session's), not a list of hedges.

### What I would refuse

I would refuse to launch or announce anything before `index.html` clears its own floors — showing
the storefront's own instruction wall to an outside reader as a live counter-example to the
studio's stated craft standard would be the opposite of positioning. I would refuse to claim
"the gates are field-tested" until they've run on a real second surface outside the founder's own
corpus — today's run is one file, one lens pass; that is a start, not a track record. And I would
refuse any adopter-facing claim about learning outcomes until Seat 3's evidence plan has produced
at least one real-term data point — the pedagogy spine is real, but "it works" is not yet a
claim this studio can back with evidence, only with theory.

---

## SYNTHESIS — where the five seats agree, and what that means

**Unanimous, all five seats, independently:** *the belt/gate/governance layer has been building
faster than it verifies itself, and the fix is making failure LOUD rather than adding more
verification.* Architect names it as overlapping truth-systems never retired. Operations names
auth docs multiplying without consolidation. Learning names the pedagogy spine existing
unmeasured for two months. Risk names three silent tool failures as one systemic gap. Proof names
the front door itself violating the floor it enforces on everyone else. Five different
vocabularies, one finding — by the Aleph's own logic, that is the highest-confidence signal in
this whole consultation.

**The uncomfortable convergence:** two seats (Architect, Risk) independently flagged that
**today's own session — the one that built the Aleph fleet, five belt ticks, and this document —
is itself governance-heavy and shipped no player-facing capability**, which is a direct violation
of the studio's own `BUILD-DEBT.md` ratio rule. I am not going to soften that. The work was real
and found real bugs (three dead buttons, a grading defect, a corpus-wide touch blind spot,
33 instruction walls) — but per the studio's own standing rule, the next session's obligation is
to ship one of those fixes before adding anything else to the governance layer, this consultation
included.

**Recommended immediate next action, synthesized from all five:** ship the highest-agreement
finding from today's Aleph run on `the-tell.html` — the dead buttons and the `state={}` wipe on
lens-switch — because it is small, player-facing, real, and pays down the exact debt Risk and
Architect both flagged. Do that before seating another panel.

**What genuinely conflicts across seats, and needs the founder's call, not mine:** Architect
recommends narrowing canon to repo-only and retiring the older lane docs; that is a real
decision, not a mechanical cleanup — Forking Paths was ratified by the founder on 2026-08-03,
so retiring any part of it is a founder call, not a session's unilateral edit.
