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

---

## RED TEAM — weak spots in canon-guard (independent adversary, all reproduced against the live repo)
*Ranked by how badly each undermines trust. Moves, not verdicts.*

1. **The enforcement doesn't exist yet.** The docstring + manifest CLAIMED "the manifest cannot rot / enforced in CI" — but canon-guard is **not wired into CI** (`grep -rn canon-guard .github/` → none). It re-creates the "runs only if the agent remembers" disease it was built to kill. Over-claim corrected in the manifest + docstring this session. **MOVE:** add `canon-guard --refs && --wiring` to floor.yml. · founder (workflow scope) · v-next
2. **Subdir + non-code blindness.** `REF_GLOBS` is non-recursive and code-only, so `studio-eyes/studio-eyes.py`, `founder-gate/pre-push` (hook), `.md`/`.html`/`.js` callers are invisible — a real caller in a subdir reads as UNWIRED, a stale ref in a runbook passes `--refs` clean. **MOVE:** recursive globs + hook/`.js` inclusion (and document that prose `.md`/`.html` mentions are intentionally out). · build · v-next
3. **Self-test grades nothing that ships.** `self_test()` exercises only `superseded_map` + `wiring_verdict` on synthetic data — never `count_refs`/`scan_refs`/`wiring`/glob/IO, never validates the real manifest. A role missing `canonical` → uncaught `KeyError` traceback (exit 1, not the exit-2 "do not trust" contract); empty/`roles:[]` → exit 0 (silent under-enforcement); duplicate role → last-wins silently. **MOVE:** temp-fixture canary that runs the real scan + a schema validator (exit 2 on violation) + reject empty as "unconfigured, NOT enforcing." · build · v-next
4. **Substring matching.** `supbase in line` / `basename in text` — no boundary. `count_refs("gate.py")==3` (matches `founder-gate.py` etc.); a stray comment mention flips a wiring verdict HALT→OK, **defeating the guard's protection against its own founding error.** **MOVE:** word/path-boundary regex; magnitude-dominant wiring verdict, not `!=0`. · build · v-next
5. **Wiring only sees manifest-listed siblings; a new unlisted duplicate is invisible.** **MOVE:** enumerate the real duplicate set from disk (name-family), not just the hand-listed siblings. · build · v-next
6. **/tmp copy + indirect invocation evade it.** `safe-push.sh` runs `python3 /tmp/studio-eyes-sweep.py` (a copy — could be a stale v3); `ratchet.py` uses `SWEEP="…"` then `$SWEEP`. The guard vouches for the repo file, not the one that runs. **MOVE:** canonicalize/resolve paths; flag `/tmp/<managed>` and dynamic-path invocations as un-vouchable; document "name appears" ≠ "canonical executes." · build · WISH
7. **Accumulate-never-shed (Funes' gap, in the anti-stale tool itself).** `REF_EXEMPT` is hardcoded and ever-growing — and it permanently exempts `claude_FUNES-INDEX.md`, the very stale-prone map. `families_awaiting_declaration` is a limbo array that grows and enforces nothing. **MOVE:** `last_verified` stamps + decay; turn limbo into failing WARNs so it has a cost. · founder · v-next
8. **No byte/hash cross-check.** The guard never hashes; byte-identical dupes and shelf-vs-repo copies (which the manifest CLAIMS it will HALT) are undetectable in code — the claimed shelf-HALT does not exist. **MOVE:** call `resolve-canon.py`/blob-sha for declared roles; flag unnamed byte-identical duplicates. · build · WISH

## THE CANON CONTRADICTION the red-team surfaced (bigger than any bug)
The verified reason the Studio Eyes canon kept flipping: **the docs and the wiring disagree.** `tight-spiral-studio-os.md:1650` + `studio-eyes/README.md` document **v3** (`studio-eyes/studio-eyes.py`, Playwright, executes JS) as the gate; `ratchet.py` + `safe-push.sh` + `floor.yml` execute **v4** (`studio-eyes-sweep.py`, render-proof, no JS). Documented gate ≠ executed gate. **MOVE (the root fix):** reconcile — one canon (fix the other source), or two roles (render-proof floor = v4 wired; JS/dynamic-state gate = v3, then WIRE it). And `--wiring` should itself learn to flag *documentation that names a different file than the wiring runs*. · founder + build · v-next

## HONEST STANDING (as of this convening)
canon-guard is a **working, self-proving mechanism with real weak spots**, not yet an enforcer. Its highest-value hardening (in order): wire it into CI (#1), recursive+bounded matching (#2/#4), a self-test that runs the shipping code (#3). Its highest-value *use* is still generate-index-from-manifest (Eagle Eye) — but only after the Studio Eyes contradiction is reconciled, or the generated index would encode the contradiction.

---

## ACCESSIBILITY STANDARDS MAP — the gates vs industry (2026-07-27)
*Verified against the code. WCAG SC numbers from established knowledge (w3.org 403'd via proxy).*

**MEET / EXCEED:**
- WCAG 2.x contrast ratio, correct math, in every gate. Target **7:1 (SC 1.4.6 AAA)**, above the 4.5:1 AA floor (SC 1.4.3) — right for low vision.
- **Render-proof** (v4 pixel-crosscheck, v3 real browser) is the industry direction (test the rendered result, not the source). Retiring the regex contrast-gate is this move.
- **Anti-halation** (never #000 on #fff) is AHEAD of WCAG 2.x — and is APCA's own rationale. Early, not behind.

**CLOSED THIS SESSION (all report-mode; blocking once proven):**
- axe-core was installed and never invoked → `axe-audit.py` invokes it (one shared browser, offline-injected, pinned `axe-core@4.10.2`).
- SC **1.4.11 non-text contrast** (3:1 for focus/border/graphics) was unchecked → `contrast-plus.py` checks it (index passes; `--strict` gates once the corpus is clean).
- No perceptual second opinion → `contrast-plus.py` adds **APCA** (Lc), self-tested against published reference (#000/#fff = 106.0, #fff/#000 = -107.9). It already flagged `--ink-3` at Lc 71.2 in the softer stop — a body-text weakness WCAG 2.x passes at 5:1.

**STILL OPEN (moves):**
- axe + v3 are report-mode until proven green in CI (no browser in the authoring sandbox; honest).
- `contrast-plus.py` is token-based (a secondary lens); the render-proof primary stays the sweep. A *rendered* APCA/1.4.11 (focus states need a browser) is the next rigor step.
- Declare `axe-audit.py` / `contrast-plus.py` in the canon-manifest once they've earned a role.
