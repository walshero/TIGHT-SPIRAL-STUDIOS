# SITE SWEEP — walshero.github.io/TIGHT-SPIRAL-STUDIOS
*Full TSP sweep, 2026-07-02. Repo cloned; every finding below is verified on the actual deployed bytes.*

## VERDICT
The site works, the FERPA wall held, and three lost files came home. But the repo publishes the whole studio shelf — the IP-shielded tier and the public tier are currently the same URL. That's the one finding that changes what you do this week.

## SCORECARD

| Check | Result | Detail |
|---|---|---|
| Student PII | PASS | No student names, rosters, or student emails anywhere in the repo. |
| Faculty/institutional exposure | FLAG | `confluence-TRUNK` carries 18 MassBay faculty emails + internal routing/deployment notes. Directory-grade, not FERPA — but internal department infrastructure on a personal public repo. |
| IP tier | HALT | Public repo contains: full Studio OS, session handoffs, decision trees, Claude + ChatGPT pipeline instructions, CYL period bibles + rebuild spec, capstone paper draft + prospectus, MassBay fact book, sabbatical report. Your view-mode direction says this is the tier you hold, not the tier you street. |
| Emoji wall | PASS* | One ✓ glyph in `tight-spiral-patterns.md`. Text dingbat, not an emoji face — swap to "PASS" text when convenient. |
| Green ban | FLAG | Green hexes in `confluence-TRUNK` (pre-ban build; deferred-reskin rule applies, but it's public now). |
| Muted-ink token | FLAG | 10 files carry `--ink2`/muted patterns — all pre-visibility-floor builds. Deferred reskin as opened. |
| Offline floor | FLAG | 3 files load external resources: `confluence-TRUNK`, `play-the-studio`, `what-this-is`. |
| Front door | OPEN | 317-byte redirect → work desk. The splash gap you already named; build queued behind this cleanup. |
| OS generation | SLIP | Repo OS = 144,174 bytes — a THIRD generation. Missing both July 1 rules. Three surfaces now hold three different OSes (repo 144,174 / Project 141,906 / phone 147,663 = truth). |
| Superseded dupes public | FLAG | `sandbags.html`, `flash-ballast.html` live beside their replacements. |
| Recovered files | WIN | `funnyboney-factory.html` (28,122) · `elves-house.html` (24,657) · `provenance-ledger.html` (19,513) — pulled from repo, handed back for phone-save. Loss ledger drops to: timing-belt, legibility-optimizer, semester-arcade, en195-syllabus-game. |

## THE FIX — your decision format

**1. Recommended:** split the tiers. The repo keeps only the public face: `index`, `tight-spiral-studio-face`, `tight-spiral-system-map`, `what-this-is`, and the shipped games (`sandbags-joy`, `review-bench`, `workshop-wall`, `course-river`, `play-the-semester-flash`, `en195-last-week`, `choose-your-leader-full`, `funnyboney-factory`, `elves-house`). Everything else comes down. Fastest execution: create a GitHub fine-grained token (repo scope, this repo only), paste it here, and I push the whole cleanup as one commit — zero file-by-file hunting for your eyes. Then revoke the token.

**2. Why:** one commit fixes ~30 exposures at once; the alternative is thirty individual delete-file walks through GitHub's web UI, which is exactly the screen-hunting RP work to avoid.

**3. Tradeoffs:** token creation is itself a settings walk (I'll give exact steps, desktop only); and anything already crawled by a search engine may persist in caches a while — the sooner it's down, the less that matters.

**4. Simpler (good enough today, ~10 min):** delete only the five most sensitive files via GitHub web — `tight-spiral-studio-os.md`, `claude-project-instructions.md`, `chatgpt-pro-instructions.md`, `massbay-fact-book-word.docx`, `confluence-TRUNK-2026-06-23.html`. Steps per file, on the Mac: repo page → click the filename in the list → top-right of the file view, click the three-dot menu (right of the pencil) → "Delete file" → green "Commit changes" button, top right. Watch for the commit dialog opening below the fold on the second monitor.

**5. Advanced (ideal future state):** two-repo architecture — a private repo as the true shelf mirror, the public repo as the curated site; plus the splash front door and, eventually, the Confluence River as the public system view. All parked behind Rule H and the amendment review.

## WHAT TO IGNORE
The muted-ink and green flags in old builds (deferred-reskin rule already covers them), the ✓ glyph, and the dupes — they ride along in whichever cleanup you pick. Nothing else on this list needs a separate trip.
