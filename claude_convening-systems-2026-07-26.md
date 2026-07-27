# FULL-STAFF CONVENING — the studio's reliability & build systems
*2026-07-26. Object: the reliability + build machinery — `canon-guard.py`/`canon-manifest.json`, the Playtest Table, the gates and pipeline — where to harden it, drawing on software-industry practice and instructional-design (ID) models. Seats: Aleph (canon vantage), Funes (memory/index), Eagle Eye (strategy/leverage), Props Room (reuse). Findings are MOVES, not verdicts (tableau-gate law, 2026-07-12). No emoji; every move is verb · owner · when, or WISH.*

*Reading "ID models" as INSTRUCTIONAL DESIGN (ADDIE/SAM, backward design, Kirkpatrick, UDL, cognitive load). If the founder meant identity/config models, the ID section re-aims; the industry section stands either way.*

---

## FUNES OPENS — the standing weakness the new tools inherit (memory-cited)
OS finding, 2026-06-29 (os.md ~L932): the question *"does this component accumulate but never shed?"* was load-bearing across FIVE systems at once — the parking lot (no decay), memory (write-only, hit its ceiling), the panel roster (seats added, never culled), the Props Room (fills by promotion, no retirement), the shelf (retires *superseded*, never *dead*).

**The anti-stale tools I just built inherit the same gap.** `canon-manifest.json` roles/siblings/superseded only grow; `claude_playtest-heuristics.md` says "never delete a row"; `claude_FUNES-INDEX.md` accretes corrections. An anti-stale system that itself only accumulates becomes the next stale artifact.
- **MOVE:** every accumulating store gets a `last_fired` stamp + a decay/retirement rule (archive, never delete) — the BUILD-DEBT sunset clause (retire what hasn't fired in N logged sessions) applied to the manifest, the heuristics ledger, and the seat roster. · build · v-next

---

## INDUSTRY PRACTICES we can benefit from (each mapped to a move, not a citation)
- **Single Source of Truth / config-as-code.** The manifest is the SSOT for role-canon; the prose index is a derived view. **MOVE:** generate the `FUNES-INDEX` canon-pointer rows FROM `canon-manifest.json` — a hand-typed index is what went stale and mis-pointed Studio Eyes twice. · build · v-next
- **Schema validation / config linting.** A malformed manifest silently under-enforces. **MOVE:** add a JSON Schema for `canon-manifest.json` and validate it in `--self-test` (refuse on invalid, per the teeth rule). · build · v-next
- **Provenance / content-addressing.** Git is already content-addressed ("cannot lie"); `lane-fidelity.py` has blob-sha. **MOVE:** identify canon by blob-sha where it matters, not by name/prose — the whole session's error was trusting prose over the artifact. · build · v-next
- **Poka-yoke (mistake-proofing).** `canon-guard` is poka-yoke; it only bites if it runs. **MOVE:** wire `--wiring` + `--refs` into `floor.yml` so a prose-declared or stale-referenced canon cannot merge (founder's paste — workflow scope). · founder · v-next
- **Deprecation policy with sunset dates.** **MOVE:** every `superseded` entry carries a `retire_by` date; feeds the decay rule above. · build · v-next
- **Tripwire observability (earn-its-keep evidence).** **MOVE:** when the guard catches a stale reference, log it (date, what, where) — this is the BUILD-DEBT proof that the GOV tool made a build ship cleaner. · build · v-next

## INSTRUCTIONAL-DESIGN MODELS we can benefit from (mapped to moves)
- **UDL (Universal Design for Learning).** The comfort stops + RP floor + the five playtest personas ARE UDL — multiple means of representation, action/expression, engagement; learner variability made testable. **MOVE:** name the UDL mapping in the OS so the accessibility floor reads as a positive design system, not only a HALT list; it is portable, teachable studio IP. · build/founder · v-next
- **Backward Design (Wiggins & McTighe) + Constructive Alignment (Biggs).** Start from the outcome; align activity and assessment to it. **MOVE:** every instrument's Fidelity checklist opens with the named ISLO/outcome it targets, so the playtest's "does it do its job" is measured against that outcome, not a vibe. · build · v-next
- **SAM vs ADDIE.** The playtest loop (agent pre-flight → founder cold play → Drift Fork) is Successive Approximation, not a waterfall. **MOVE:** name it as SAM so the loop is defended as iterative-by-design; the Drift Fork is its evaluation gate. · founder · doc
- **Kirkpatrick's four levels of evaluation.** The studio evaluates at Level 1 (reaction — GATE 1 cold play) and Level 2 (learning — does the reveal reconsolidate, Horvath). It does NOT yet reach Level 3 (behavior/transfer) or 4 (results). **MOVE:** state this honestly; Diagnose-mode / transfer (already on the finishing list) is the Level-3 build. · founder · names a gap
- **Cognitive Load Theory (Sweller).** The <50-words-per-screen floor + one-idea-per-beat (Horvath) manage intrinsic/extraneous load. **MOVE:** make it a *measured* check (words/screen in the sweep), not a guideline. · build · v-next

---

## EAGLE EYE — leverage (where one small move buys a large return)
1. **Generate the index from the manifest.** Highest leverage: it kills the ROOT cause (hand-typed index rots) for every future session, cheaply. Do this first.
2. **Wire the guard into CI.** Turns the whole stale-read class from "a session's vigilance" into "a build that fails." One paste, permanent.
3. **Reuse/impact angle:** `canon-guard` + the Playtest Table + the UDL mapping are portable "reliable single-file instrument" methodology — the thing other educators and institutions would license or adopt. The reliability work is not overhead; it is the product's moat.

## PROPS ROOM — reuse (what should become a reusable prop)
- **The self-test-teeth pattern** (a gate that refuses if it can't grade its own canary) now recurs in `studio-eyes-sweep.py`, `playthrough-agent.py`, and `canon-guard.py`. **MOVE:** promote it to one named, referenced prop so every new gate inherits "refuse if the teeth don't bite." · build · v-next
- **The output contract** (verb·owner·date / WISH · no emoji · yes/no) recurs across the Bench, the Table, and the gates. **MOVE:** one referenced spec, cited, not re-typed per seat. · build · v-next
- **Funes' warning applies here too:** the Props Room fills by promotion and never retires — the decay rule covers it.

## WEAK SPOTS in the new tools (my self-audit; independent red-team appending below)
- `--refs`/`count_refs` match by substring → false-positive on a mention in a comment/JSON, false-negative on indirection (`SWEEP="studio-eyes-sweep.py"; python3 $SWEEP`, or the `/tmp` copy in `safe-push.sh:48`). **MOVE:** match real call sites (import/subprocess/`$VAR` expansion) or at least word-boundaries; widen REF_GLOBS or accept the gap out loud. · build · v-next
- **Unknown-sibling blind spot:** a NEW `studio-eyes-v5.py` is invisible until a human lists it. **MOVE:** `--wiring` also flags repo files matching a role's name-family that aren't in the manifest (triage). · build · v-next
- **Idle by design:** `superseded=[]` today, so the guard enforces nothing until declarations land — armed, not yet biting. Honest; noted.

---

## OPEN FOUNDER CALLS
1. **v3 Studio Eyes disposition** — retire `studio-eyes/studio-eyes.py`, or seat it as the JS/dynamic-state role v4 can't cover (then it becomes a second declared role, wired into the JS-state check).
2. **"ID models"** — confirm instructional-design (above) vs identity/config.
3. **First leverage move** — generate-index-from-manifest, or wire the guard into CI (your paste)?

*Independent red-team weak spots to be appended when they land.*
