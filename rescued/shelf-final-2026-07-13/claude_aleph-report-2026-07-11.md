# ALEPH REPORT — full-corpus review, 2026-07-11
*16 panel readers across 115 unique project docs before the "One Room living landscape" front-door build. Evidence over characterization.*

## Coverage (receipts)
- 16 thematic clusters, one reader each; all 16 returned. ~1.4M subagent tokens.
- Full-read: governance/OS, ledgers, guards, art docs, sabbatical, EN195, rooms, faces, funny-boney, cliche, CYL specs, auditors, handoffs.
- Scanned only (large, by design): confluence-TRUNK.html, choose-your-leader-full.html, warriors, behind-this-door, the-compound-capstone, confluence-walkthrough.html.
- NOT read this pass (coverage gap): the two PDFs (`learningoutcomes…pdf`, `funnyboneysfactoryspec.pdf`), `massbay-fact-book-word.docx`, `AY 2627 Student Assessment of Learning.docx`.

## State of the studio (from evidence)
Tight Spiral is a one-person game + assessment-design studio. Origin is in the 2012 sabbatical report: "In games, the recursive process is a **tight spiral**, an active feedback loop of hypothesis testing, reflection and learning." Theory base: Gee's learning principles, Osterweil's Four Freedoms of Play, Squire (systems/design thinking), Csikszentmihalyi (flow), Shaffer (epistemic frames). Output is single-file, offline, accessibility-first HTML games and assessment tools. Public site live at walshero.github.io/TIGHT-SPIRAL-STUDIOS (14 pages, verified 200 on 2026-07-11).

## Matt's thoughts on art (the brief that governs the build)
- Thesis: use AI to become a better *traditional* studio, not to invent an AI visual language. Target = a thoughtful late-20th-century independent studio. Failure test: "if a viewer notices AI before they notice the idea, the work has failed."
- Craft over spectacle. Every image authored, never manufactured. The studio is the artist; AI is a production assistant. HITL closes every asset — "generator output is raw stock, never a ship."
- Function gate: nothing exists only because it is attractive; every object must teach, guide, foreshadow, navigate, or record.
- Fixed mnemonic vocabulary: water wheel = continuous improvement, bridge = connection, switch track = decision, station = knowledge category, tunnel = future work, lighthouse = orientation, spiral = reflection, timing belt = coordination. An icon must beat the word or it is decoration.
- Richard Scarry catalog density; no wasted space unless emptiness is the lesson; one primary idea per screen (quiet complexity).
- Material rule: producible pre-digital — cut paper, letterpress, gouache, cel. "Traditional technique is a creative constraint, not nostalgia."
- When AI is used, the house look is: "pre-steampunk circus Dada meets BioShock brass-machine — Victorian letterpress, woodtype, riveted brass, hand-built diorama, warm paper, true cast shadows, matte, slightly worn." Hard rules: no text in the image (added in code), no realistic skin or faces (kraft-paper neutral forms only), flat/transparent background, center clear for UI.
- Medium Gate, three lanes: A cut-paper SVG · B raster/Lumino AI-assisted · C licensed photo/audio. Reusing the last build's look is a failure; the brief is novelty + impact. **`paper-craft-ceiling.html` concluded Lane A (hand-cut SVG) is the proven ceiling and no Midjourney subscription is needed.**
- Provenance floor: no asset enters without recorded source + license + attribution + how-it-entered. Five legal lanes; no scraping; CC0 or own-work; own work is money-walled.
- From the sabbatical: games as an art form; ludonarrative consonance/dissonance; Bioshock as playable critique of Objectivism; Journey as narrative without language. Art-games ludography (thatgamecompany, Tale of Tales, Shadow of the Colossus). Elegant design, intuitive mechanics, meaningful play; students as producers not consumers; anti-gamification, anti-points.

## Blockers before building (ranked — these gate the build)

1. **The OS is forked, not versioned — SSOT is broken.** The panel found byte-variant copies of the operating system cited at 141,906 / 147,663 / 151,450 / 158,117 / 161,666 / 164,925 / 166,001. Different copies hold different rules. The **FERPA strip-before-save rule (§13.1) exists in only ONE copy (147,663) — which is on the delete list.** The manifest names 161,666 as canonical; unreconciled. You cannot build to a constitution that exists in seven conflicting copies.

2. **FERPA / repo-exposure contradiction — unresolved.** Command Center v5.1 and the live-links map (both mine, 2026-07-11) say `confluence-TRUNK.html` = 404 RESOLVED, from a single live probe. But `TSP Ledger` Zone B logs the IP-tier exposure as still open, "stuck 3+ belts," and `site-sweep-2026-07-02` records the whole public repo publishing the OS, handoffs, fact book, and sabbatical report. **One file being 404 is not the tier being clean.** See correction below.

3. **Studio Integrity Guard is not completing unattended.** `studio-guard-report.md` records consecutive failed runs: WebFetch requires per-URL approval in an unattended session (PROVENANCE_REQUIRED). The guard as built cannot sweep while you sleep. See correction below.

4. **Confluence trunk version fork:** v33 (Drive / command center) vs v40 (Ledger 07-11, "canonical base") vs v34 phantom vs v42 "unrecoverable." Live build state unstable. Founder gate.

5. **Palette undecided while builds moved on.** `palette-chooser.html` still awaits your A/B/C eye-verdict, but `ts-hin-v1.html` already ships slate as decided. **Name collision:** Visual Constitution §15 "Palette B = High Lumen amber"; palette-chooser "Option B = slate." Two different "B"s.

6. **The green rule is mis-stated in my canon.** Command Center Ruling 8 and Constitution §15 say "studio green = Confluence only." The assessment docs (`confluence-project-directions`, revised 2026-07-02) say green is banned studio-wide in any structural/state role, with one decorative moderation-accent exception. These disagree.

7. **Name migration incomplete.** "Tight Spiral Productions" (decided 2026-07-02) vs "Tight Spiral Studios" — headers, footers, and the project title still say Studios. Pervasive.

8. **Heavy duplication with no canon markers:** the compression game exists as three files under three names (`sandbags.html` / `sandbags-joy.html` / `flash-ballast.html`); `en195-last-week.html` ≈ `en195-what-counts-now.html`; `funny-boneys-factory.html` and `funnyboney-factory.html` are *different games* with colliding names; multiple OS copies; Confluence trunk duplicates in Drive.

9. **Comfort-gate rule unreconciled:** scene-first "required first beat" (§3.1) vs "strong default, not a wall" (§5.6). Some shipped builds still use the retired blocking gate (`sandbags.html`, `flash-ballast.html`).

## The front door already partly exists
`studio-river.html` (2026-07-02) self-declares the canonical front door — "an animated river past three docks (Games / Papers / Tools)" — and states it supersedes `tight-spiral-studio-face.html`. The panel judged it the closest existing thing to a "One Room living landscape" (highest image-to-text ratio, cut-paper SVG, offline). But `index.html` (newer, 2026-07-06) still points "Start here" at the work desk and does not link the river. So three live front doors disagree. The Village dashboard design (in the delete-list handoffs) carries unharvested grammar worth keeping: buildings = hubs, trains = projects, stall/rolling shown by position+shape+label (never color), Peak-End banners, the CYL Rube-Goldberg contraption as a reusable Props Room asset.

## Two corrections to my earlier claims this session (receipts)
- I patched the Command Center to say the FERPA flag was RESOLVED, based on `confluence-TRUNK.html` returning 404. Aleph shows that was too broad: the *tier* exposure (whole shelf public) is logged as still-open in the Ledger and site-sweep. Accurate statement: that one file is 404; the repo-tier exposure is unverified and possibly still open.
- I described the weekly Integrity Guard as running unattended. The guard-report shows it cannot — WebFetch needs per-URL approval in an unattended run. The guard is scheduled but currently blocked.

## Readiness verdict
**Not ready to build the front door.** The gate is Blocker 1: the OS must be reconciled to a single source of truth (preserving the FERPA rule that lives only in a delete-listed copy) before anything is built to it. Blockers 2 and 3 (FERPA tier + guard) gate *publishing* the result. Blockers 5, 6, 8 gate the *look*.

## Adobe note
Your instruction is "use adobe." The studio's own evidence (`paper-craft-ceiling.html`) concluded Lane A hand-cut SVG is the proven ceiling and no paid raster generator is needed. Adobe (Firefly/Express) is available and fits Lane B if you want richer raster assets, but it is a choice against the studio's stated default, not a default. This is a decision, not an override.

## Coverage gaps to close (GREEN follow-up)
Read the two PDFs, `massbay-fact-book-word.docx`, `AY 2627 Student Assessment of Learning.docx`, and full-read `confluence-walkthrough.html`. None are expected to change the build gate; flagged for completeness.
