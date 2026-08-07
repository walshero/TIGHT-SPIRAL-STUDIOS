# ALEPH A5 — PROOF & POSITIONING
### Six-month consultation, Tight Spiral Studios · 2026-08-07
*Seat brief: the studio has a beautiful engine and no external proof. One legible win, for whom, without breaking the 9:1 bet. Run independently — no visibility into the other four seats.*

**Method note.** Every number below marked "measured" was re-run against live bytes in this session, not recalled from the grounding packet. Where I'm citing the repo's own record rather than something I checked myself, I say so.

---

## 1. Month 0 diagnosis

### What a stranger actually encounters

I ran the studio's own entry gate against its own front door:

```
$ python3 one-thing-gate.py index.html
TIGHT-SPIRAL-STUDIOS/index.html   ->  SHIP-BLOCK
   phone   390px:   2% image · 1 invite · 2 ctrl ·  174 words before first action · 1.88 screens to act
     [X] CRITICAL INSTRUCTION-WALL: 174 words of directions sit above the first control on phone
     [X] CRITICAL ACTION-BELOW-FOLD: first control is 1.88 screens down on phone
     [X] CRITICAL WALL: 105 words of prose, no real scene (largest visual only 2% of entry)
     [!] WARN SUB-50-TABLEAU: entry tableau 2% image (<50%; studio-eyes owns the hard gate)
RESULT: SHIP-BLOCK - a build did not clear the entry gate
```

This matches the brief exactly and I confirmed it live: the studio's own storefront fails the studio's own `TABLEAU_FLOOR = 0.50` and its own instruction-wall/action-below-fold thresholds (`one-thing-gate.py` lines 28–37). Every other room in the house is gated to this standard; the front door is not. That is the positioning problem in miniature — not "the engine is invisible," but "the one page a stranger is guaranteed to load is the one page currently failing the studio's own craft law."

### What can be honestly claimed right now

- **A self-testing quality-enforcement system that doesn't ask to be trusted.** `studio-eyes.py` refuses to run if it cannot grade its own 20-canary self-test first; `studio-fingers.py` and the five-tick belt (`studio-belt.sh`) are inspectable, not asserted. This is unusual and it is real — a stranger can clone the repo and run the canary themselves rather than take the founder's word.
- **33 shipped, single-file, offline HTML builds, 0 trackers** (index.html's own count widget) — a claim made as arithmetic, already the studio's best rhetorical habit.
- **A real course running real tools this term.** EN195 and the iSLO Suite are not demos — MassBay students in the founder's own class use them. That is genuine, current usage.
- **A verifiable founder record**: 20 years of portfolio-assessment work, MassBay AI Task Force membership, Pedagogy-of-Real-Talk PD, an authentic primary-source reflection on the college's own ISLO scoring initiative (`ISLO-SCORING-REFLECTION-2026-mwalsh.md`) naming the real institutional gap Confluence addresses.
- **Retinitis pigmentosa as a lived, not performed, accessibility driver** — the contrast/touch floors trace to the founder's own eyes, arithmetically (4.5:1 gated, not "accessible-feeling").

### What cannot be claimed right now

- **Any adopter outside the founder's own orbit.** The "sit the bench" playtest call has been live on index.html and nothing in the repo shows a human response to it — every playtest pass on file (`PLAYTEST-REPORT.md`, `FUNES-PLAYTEST-*`) is agent-driven (Studio Eyes, Studio Fingers, `playthrough-agent.py`), not a human stranger.
- **Any learning outcome.** The grounding packet's own finding stands: "nothing assessed learning" until the most recent pass, which found the CYL win condition is `mine.card===preset.card` — a three-character string compare, not a read of the student's actual reasoning. No iSLO title has efficacy data. "Builds and measures the seven ISLOs" (the suite's own proposal language) is a design claim, not an outcome claim, and needs to stay one.
- **Any blind-player claim** — categorically ruled out already; I found nothing in this session that would change that.
- **MassBay institutional endorsement.** `studio-tour-for-massbay.html` reads "an invitation to make MassBay the first pilot" — present tense, unresolved. No CTL, Assessment Committee, or Task Force confirmation exists yet.
- **External competition or award traction.** `tsp-opportunity-bridge.html` (pulled 16 Jul 2026) named "GALA Serious Games Competition 2026, submit by Aug 2, 2026" as *"the one move this month, across all four lanes."* `BUILD-DEBT.md` confirms the blocking verb-fix landed 2026-07-19 — the gate was clean for two weeks before the deadline. Today is 2026-08-07. The deadline has passed. Nothing in the ledger shows an EasyChair submission. Separately, `founder-canon.md` records the Borges paper as "2,100 words. Chronicle-shaped. 14-venue submission strategy **written**... sitting in a folder, never sent." Two independent, finished, ready-to-go assets, two missed windows to get them in front of outside eyes.

That last pattern is the real diagnosis. The belt has five ticks and all of them fire on `git push` — on whether a build is *good enough to ship*. None of them fire on whether a finished, gate-clean asset actually got **sent**. The studio has a SHIP problem solved and a SEND problem unsolved.

---

## 2. The one legible win

**Pick: land the MassBay Confluence norming pilot as a completed, attributable event** — not the invitation currently sitting on `studio-tour-for-massbay.html`, but an actual session, with named participants, real (de-identified) student work, and a reported result.

**Audience:** not a general public, not a competition jury. The people the founder already has standing with and meets in the ordinary course of his job — assessment-day colleagues, MassBay's CTL, the AI Task Force he already sits on. Nobody has to be found. A date has to be set.

**What they'd have to see:** one thing, not the whole studio. Raters open Confluence, score four to six real de-identified portfolio excerpts against the actual ISLO #1 or #5 rubric (both live, verbatim, per `ISLO-GAME-SUITE-PROPOSAL.md`), compare against the normed score, and someone who is not Matt Walsh writes one attributed sentence about whether it helped. That sentence is the asset the studio doesn't have and can plausibly get in this window.

### Argued against the alternatives

**Against "productize the gates" as the near-term win** — assessed in full below; the short version is that it asks strangers to trust a solo maintainer's support capacity, which is exactly the asset a proof point is supposed to be building, not spending.

**Against "ship the season" to a competition or grant (Flok→GALA, CYL→Games for Change, NEH Digital Projects)** — this is not a bad idea, and I'd keep NEH's Sep 1, 2026 deadline (named fit: "funds humanities games, simulations, and interactive tools by name," per `tsp-opportunity-bridge.html`) queued as the *next* move, since an application is controllable in a way a jury verdict isn't. But it is not the primary bet, for three reasons:
1. The nearest catchable deadline already passed unsubmitted — chasing the next one without first fixing why the last one didn't ship just reproduces the pattern.
2. Competitions are judged by strangers on strangers' criteria (production values, game craft) — precisely the terrain where "beautiful engine, no proof" is weakest, because a jury has no natural reason to also see the accessibility/assessment story.
3. It's higher-variance. A pilot the founder convenes himself is close to entirely within his control; a jury may simply pass.

**Against the adaptive-accessibility-profiles work as *the* win** — this is real, already substantially coded per the SWOT, and it should feed the pilot (raters or students select a profile) rather than stand alone as evidence. Nobody outside the studio experiences "the system adapts" as proof unless an outside person reports using it — which routes back to the same pilot.

---

## 3. Productizing the gates — an honest assessment

**Is the quality OS the actual product?** Not yet, and I'd be specific about why rather than wave at "solo-studio risk" in the abstract.

**Real strength as IP:** `studio-eyes.py`'s self-audit is a genuinely uncommon discipline — the tool ships with a canary corpus and refuses to run if it cannot grade its own known-verdict traps. That is inspectable, not asserted: a stranger can run `--self-test` themselves.

**Real barriers to being a product for others, today:**

1. **It's welded to this studio's own vocabulary.** `image_floor()`, `studio-voice-gate.py`, and the CSS custom-property names it checks (`--ink`, `--paper`, `--brass-ink`) are TSP-specific. `studio-voice-gate.py` checks for *the founder's* voice. Someone else's site fails on category mismatch, not a real defect, until the tool is generalized — a real engineering project, not a packaging exercise.
2. **The toolchain itself has already silently broken once.** This session's own grounding found `playthrough-agent.py` and `studio-fingers.py` both failed on a Chromium build drift and kept printing success — the same shape of failure the belt exists to catch, happening inside the belt's own tooling. If the founder's own environment drifts silently, a stranger's will too, with no support desk to catch it.
3. **The mount model assumes the mounting party is the founder's own spoke repo.** "Mount, never copy" (`studio-belt.sh`) is a real architectural insight for five repos one person owns. It is not yet a story for an unrelated third party's CI.
4. **The support model is one person.** The SWOT's own weakness — "single point of judgment = bottleneck and bus factor" — is exactly what breaks the moment an external user files an issue. A one-person PoC cannot absorb being someone else's dependency without the 9:1 ratio inverting.

**Verdict:** the gates are the studio's strongest moat, not yet its product. The right move for this window is **"look, don't install"** — publish the runbook, let people read `studio-eyes.py`'s self-audit doctrine and the ratchet's actual numbers (already partly done: `tight-spiral-runbook.html` is live and says exactly this) — rather than offering installable support the studio cannot back at month two.

---

## 4. Phased plan

### Months 1–2 — fix the front door, then schedule the pilot; build nothing new for productizing
- Bring `index.html` to the studio's own SHIP standard (≥50% entry image, first control within ~1 screen, no instruction wall) before sending anyone to it. Right now, any colleague the founder invites lands on a page that fails the same gate the founder is about to demonstrate. This has to go first — it is the cheapest, highest-leverage fix available and it undercuts every other proof move until it's done.
- Convert the standing MassBay invitation into a calendar entry: a named date, named colleagues, real de-identified excerpts. This is a scheduling move, not a build.
- No new work on packaging the gates for outside use in this window.

### Months 3–4 — run the pilot, report it in the studio's own arithmetic idiom, and clear the "written, never sent" backlog
- Run the actual norming session on Confluence. Report the real result, whatever it is — if agreement tightens, by how much, on how many excerpts; if it doesn't, that is still real information and more credible than an unmeasured claim.
- Get one sentence, attributed, from a participant who is not Matt Walsh. That sentence is this phase's deliverable, not a new feature.
- In parallel, zero-build: send the Borges paper — already finished, per the studio's own record — to its Tier 1 venue. It has been ready since before this window opened.

### Months 5–6 — write up the win, and close the productize-the-gates question in writing
- One page, in the founder's own voice: who was in the room, what was scored, what the rater-agreement number was, quoted. This is the "one legible win" the SWOT asked for — an institutional-assessment result, not a game or a competition placement, because assessment is the domain where the founder's 20 years make the claim need zero inflation to be interesting.
- Make a written founder decision on the gates' external future — "look, don't install" as policy, or stay wholly internal. Either answer is fine; leaving it open past month six is not.
- If the pilot lands before the NEH Sep 1 deadline, its write-up becomes the grant's centerpiece evidence — the actual payoff of sequencing the pilot ahead of the application.

---

## 5. The honesty constraint as positioning

"No inflated claims" is already coded as engineering discipline in this studio, not a marketing posture. `tight-spiral-studio-os.md` §15 (the hollow-claim doctrine, locked 2026-07-11) states the law plainly: *"NO CLAIM OF SUCCESS MAY BE EMITTED THAT IS NOT DERIVED FROM THE ARTIFACT ITSELF,"* backed by four documented specimens of the studio catching its own false success reports — including one where an assistant echoed `WORKFLOW PUSHED` over a git push that had actually been rejected, in the same session that wrote the rule. That's not disclaimer language. It's a discipline the studio already applies to itself before it ever reaches a claim about a user, and it is the honest differentiator the seat brief is asking for.

**Made legible without a disclaimer wall** — the founder has ruled that out, correctly, so the fix isn't a trust badge or a paragraph of caveats bolted onto every page. It's to let the receipts that already exist do the talking, in the places a stranger already looks:

- The count widget on `index.html` ("33 builds, live · 0 servers · 0 trackers · 4.5:1 contrast floor, gated") is already the pattern — a claim as arithmetic, not adjective. Keep it once the entry-paint fix lands; it's the honesty signature, not overhead to trim.
- `tight-spiral-runbook.html` is already published with the line *"a shop that hides its method is asking you to trust it instead of check it."* That sentence doesn't need a caveat added to it — it already invites the check instead of asking for trust, which is the whole positioning move.
- The one addition worth making: when the pilot lands, report the actual number next to the claim, the same arithmetic-not-adjective move the count widget already makes. "Agreement improved" is an adjective claim. "Agreement moved from X% to Y% on N excerpts" is the studio's own established idiom, and it needs no extra hedge to be believed.
- Do not add a "we don't inflate our claims" banner anywhere. Asserting your own honesty is itself a claim, and it would need the same proof standard as any other — which defeats the point. Let the arithmetic carry it, the way it already does.

---

## 6. What I would refuse to claim or ship

- **I will not claim GALA was submitted, that the Borges paper was sent, or that the MassBay pilot happened, until the bytes confirm it.** Per the studio's own hollow-claim law, and because none of the three is confirmed in the ledger as of this session.
- **I will not ship "productize the gates" as an external offering in this six-month window.** A one-person studio at month two cannot carry external support without breaking the 9:1 bet. Show the gates; don't sell them yet.
- **I will not write any version of "students learn X from this game" for any iSLO title.** No learning has been measured for any of them; the most recent scan found the CYL pass condition is a string compare, not a read of the student's reasoning. Craft is not evidence of outcome, and the studio doesn't have outcome data.
- **I will not claim or imply blind players can play these games.** The standing ruling holds without qualification. "Accessibility-first design intent," framed around the founder's RP and the measured contrast/touch floors, is the only defensible language — never an outcome claim about a blind player's experience.
- **I will not send anyone — a colleague, the AI Task Force, a funder — to `index.html` as the front door before the entry-paint fix lands.** Directing a proof-seeking outsider to a page that fails the studio's own SHIP gate is the single most self-defeating move available right now, and I would not greenlight outreach until it's fixed.
- **I will not recommend the GALA/Games for Change competition lane as the primary evidence bet.** The missed Aug 2 deadline is a live, measured instance of a pattern — alongside the unsent Borges paper — of finished work not reaching outside eyes. The fix for that pattern isn't a new deadline; it's finding out why the last one was missed before setting the next one.

---
