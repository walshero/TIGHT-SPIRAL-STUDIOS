# BRANCH TRIAGE, 2026-08-17

*The 26 stranded branches the tendrils sweep reported once a real `git fetch`
revealed the true remote. Triaged mechanically, not by name or vibe.*

## THE HEADLINE: do not merge any of them

Every one of the 22 non-dead branches shows **tens of thousands of deletions**
against main (70,000+ lines on most). They are old snapshots that predate most of
main's current content. Merging any of them does not add work, it removes it.
Merge is the wrong verb for this pile. The right verbs are **harvest** and
**delete**.

## HOW THEY WERE TRIAGED

Three measurements per branch, all local and cheap:

1. `git cherry origin/main <branch>`, marks each commit `+` if its patch is NOT
   upstream, `-` if an equivalent patch already is.
2. `git diff --shortstat origin/main <branch>`, what merging would actually change.
3. `git diff --name-status origin/main <branch> | awk '$1=="A"'`, **the decisive
   one**: files that exist on the branch and not in main. This is the only real
   "would we lose something" test.

**Why commit counts lie here.** Most of these branches report 200 to 550 "unlanded
patches" while holding **zero** files main lacks. That is the squash-merge
artifact: a GitHub squash merge gives main a single commit whose patch-id matches
none of the branch's individual commits, so the branch reads as massively unlanded
forever. `git cherry` said 289 for `art-skins-redo`; its unique-file count is 0.
Count commits and you panic. Count files and you can act.

## TIER 1, DELETE NOW, ZERO RISK (5 refs)

Zero unlanded patches; content fully in main. Dead refs from merged PRs.

| Branch | Why safe |
|---|---|
| `claude/adopt-funes` | 0 unlanded, 1 commit, content in main |
| `claude/companion-floor-fix` | 0 unlanded (PR #49) |
| `claude/playtest-team` | 0 unlanded (PR #48) |
| `claude/trunk-fix` | 0 unlanded |
| `claude/en195-poetry-arcade-1aunsp` | merged 2026-08-17, now 0 ahead / 0 behind |

## TIER 2, HARVEST THE NAMED FILES, THEN DELETE (6 branches)

These hold files main genuinely lacks. **Harvest file-by-file
(`git checkout <branch> -- <path>`), review, commit. Never merge the branch.**

| Branch | Files only there | Note |
|---|---|---|
| `claude/studio-viscosity-comfort-controls-k3272n` | 14, incl. `canon-guard.py`, `axe-audit.py`, `canon-manifest.json`, `canon-vocab.json` | **Highest value on the list.** Governance and accessibility tooling the studio keeps rebuilding from scratch. |
| `claude/funny-bones-cold-opening-pn51ay` | 17, incl. `bonkyard-transferable-mechanics.md`, bench reviews | Craft docs and a transferable-mechanics harvest |
| `claude/massbay-islo-games-hub-rtoifc` | 4, incl. `ISLO-CAREER-WORKFORCE-LANE.md`, `claude_seat-studio-voice.md` | ISLO lane work |
| `claude/tsp-accessibility-design-review-w55xa0` | 3, incl. an accessibility-lane harvest | Accessibility record |
| `tsp-doc-cleanup` | `ENFORCER-MANIFEST.md` | |
| `writerly-moves/review-2026-08-10` | `FUNES-SCRUB-josh-2026-07-29.md` | |
| `claude/firefighting-char-inventory-tsp-t1xaxk` | `fireground-photo-manifest.md` | Ties to the fireground image lane |

`claude/choose-leader-content-febnzi` also carries `live.html`, which is not in
main. Check what it is before harvesting; a stray `live.html` may be a deploy
artifact rather than canon.

## TIER 3, DELETE WITHOUT HARVEST (the rest)

Zero unique files, or the only "unique" file is a duplicate under an older path:

- `claude/art-skins-redo-zgphl0`, `claude/cyl-design-b`,
  `claude/cyl-history-search-supplements-yx10w5`, `claude/flok-round-1-role-uzn6uw`,
  `claude/operating-with-matt-defaults-f8z84o`, `claude/pages-403-config-bbnkan` , 
  0 unique files.
- `claude/cyl-image-lane`, `claude/cyl-mechanic-peak`, `claude/cyl-reconcile`,
  `claude/bring-in-confluence-hub`, `tsp-git-handoff-studio-wide`, the only unique
  file is `studio/dad-energy.html` at **72,829 bytes**, an older pre-move copy of
  main's root `dad-energy.html` at **95,384 bytes**. Main's is larger and newer.
  Nothing to save.
- `claude/floor-hotfix`, `claude/studio-front-door`, same, plus
  `rescued/borges-pipeline-paper.md`, which main already holds at
  `rescued/drive-2026-07-13/borges-pipeline-paper.md`.
- `claude/tsp-mobile-controls-ui-6r4moh`, only `fireground-assets/.lane-test`, a
  test artifact.

## THE PROCESS FIX THIS EXPOSES

`funes-tendrils.py` reports **commit counts against whatever remote-tracking ref it
happens to find**, and does not fetch. Both halves of that are wrong in the same
direction as the error retracted in `claude/FINDING-UNRELATED-HISTORIES-2026-08-12.md`:

1. **It should fetch first, or say out loud that it did not.** A clone-time ref can
   be arbitrarily stale; this sweep reported 1 loose end when the true number was 27.
2. **It should count unique FILES, not commits.** Commit counts across squash merges
   are noise, and noise that screams every session trains the founder to ignore the
   alarm. That is the comfort-gate doctrine applied to the sweep itself.

Until that lands, read every "N commits not in origin/main" as unverified.

## RECOMMENDED ORDER

1. Delete Tier 1 (5 refs). Nothing to review, nothing to lose.
2. Harvest `studio-viscosity-comfort-controls` first: `canon-guard.py` and
   `axe-audit.py` are standing tools, not documents.
3. Harvest the rest of Tier 2 file-by-file.
4. Delete Tier 3.
5. Fix the sweep so this does not silently rebuild.

**Nothing in this document has been executed.** Deleting remote branches is
destructive and outward-facing; it waits on the founder.
