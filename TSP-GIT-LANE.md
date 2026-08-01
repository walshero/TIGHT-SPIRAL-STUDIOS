# TSP-GIT-LANE

The Cowork/Claude session designated as the studio's **git writer**. Renamed to
`TSP-GIT-LANE` on 2026-07-29 to stop two sessions from clobbering one file.

## THE RULE THIS LANE EXISTS TO ENFORCE

**ONE CANON WRITES, OTHERS READ** (`cross-lane-manifest.md`). Exactly one session
pushes to the repo at a time. If you are not TSP-GIT-LANE, you **read** the repo; you do
not push. Two sessions editing one file is structural, not careless — it happened this
session on `index.html` (a concurrent "contrast-paydown" session held it open) and cost
two rebuild-on-their-base cycles to avoid a clobber. Matt owns the face; the *lane*
decides who currently has hands on it.

## THIS LANE IS MORTAL. GIT IS NOT.

The session's container is **ephemeral** — reclaimed on inactivity or close. On every cold
start the next operator has nothing: re-clone, re-auth, rediscover. Nothing in the
container survives. The only durable substrates are:

- **the repo** (GitHub `walshero/TIGHT-SPIRAL-STUDIOS`) — canon
- **the Project** (TIGHT SPIRAL STUDIOS) — docs, across all sessions

*Nothing survives a chat unless it's pushed.* The chat is disposable hands; the repo is
the studio. A session name (even this one) does not grant permanence — git does.

## COLD-START CHECKLIST

1. `git clone https://github.com/walshero/TIGHT-SPIRAL-STUDIOS.git`
2. **Auth to push:** the container's env `GITHUB_TOKEN` is **read-only**. To push you need a
   fine-grained PAT from Matt — Repository: TIGHT-SPIRAL-STUDIOS, Permissions → **Contents:
   Read and write**. It expires (7 days typical). Wire it into the push URL, **scrub it from
   git config after**, never echo it.
3. **Before editing any named file:** run `resolve-canon.py <file>`. Repo is canon; the shelf
   lags; Drive can hold newer strays — a **v48 Confluence trunk sat in Drive** while the
   manifest still called the repo (v43) canon. Diff from content, never default to newer/older.

## PUSH DISCIPLINE (earned 2026-07-29)

- **Fast-forward only.** `git fetch origin main`; if origin advanced, rebase onto it. Never
  blind force-push over a concurrent writer.
- **Collision → rebuild on THEIR base and preserve their work.** Supersede only what the
  founder explicitly directed. (The kernel mount preserved the other session's `tsp:surface`
  tag + decoration tokens and superseded only `cft-soft`.)
- **Byte-verify every push.** `HEAD == origin/main`, md5 match. `success:true` is never proof.
  The raw CDN caches ~5 min and will lie — git is authoritative.
- **Gates:** `safe-push.sh` runs the static studio-eyes gate on HTML; `comfort-gate.py` is the
  real-pixel / real-network gate (contrast per mode, dark-required, true offline, no emoji).
  studio-eyes false-positives on light-on-dark and on `<a href>`/SVG-namespace — trust
  comfort-gate's measurement over studio-eyes' guessing.

## LINK TO PLAY, ALWAYS (founder ruling, 2026-07-30)

Every delivery that lands or changes a playable or viewable file ENDS with a
click-ready link. Matt never constructs a URL, never gets a bare filename,
never gets "it's in the repo." Verbatim: "Link to play. Always. It's easy
for me so do it as rule."

Link table (until GitHub Pages is switched on):
- Pages and games (HTML): COMMIT-PINNED, always —
  https://raw.githack.com/walshero/TIGHT-SPIRAL-STUDIOS/<full-commit-hash>/<file>.html
  A pinned URL cannot serve a stale game (founder got a cached pre-mount CYL on
  2026-08-01 from a branch URL; that never happens again). Branch URLs are for
  bookmarks only, with the ~5-min caveat said aloud.
- Docs and images: https://github.com/walshero/TIGHT-SPIRAL-STUDIOS/blob/main/<path>
- githack CDN lags ~5 min after push, same as raw. Say so if the push is fresh.

Durable upgrade, one switch, Matt's hands: repo Settings -> Pages -> Source
"Deploy from a branch" -> main / root -> Save. After that every push
auto-publishes and links become https://walshero.github.io/TIGHT-SPIRAL-STUDIOS/<file>.html
(.nojekyll is already in the repo so underscore-prefixed files survive).
Blocked from this lane three ways, all verified 2026-07-30: Netlify MCP proxy
403s this sandbox, the GitHub Pages API path is blocked by the egress proxy,
and the PAT lacks workflow scope for an Actions publish. The switch is the fix.

## SAY IT ONCE (founder ruling, 2026-07-29)

Matt is solo staff. Security and hygiene items — token revocation, expiry, cleanup chores —
get said ONCE, at the moment they arise, and never again. No standing-reminder lists, no
"still owed" refrains at the end of reports. He heard you. A repeated reminder is nagging,
not diligence. If an item is genuinely blocking, say it is blocking; otherwise it is his
to schedule, not yours to repeat.

## COMPUTED > TYPED (the hollow-claim rule)

Anything you **type** as a fact about state — a version, a date, a deployment status — is
suspect by construction and rots. **Compute it.** This session shipped three hollow claims
before catching them: "running for a Manhattan relocation firm" (→ "designed for"), and a
hardcoded "Last updated July 14" (→ `document.lastModified`). The fixes that stick compute
the value; the ones that fail remember it.

## WHAT THIS LANE PRODUCED (2026-07-29)

- `comfort-kernel.html` — the studio comfort standard: Day/Dusk/Night ladder + High-contrast /
  Larger-text / Reduce-motion / Colorblind toggles. Harvested from `studio/tsp-home.html` +
  Confluence, gated in all modes.
- `comfort-gate.py` + `comfort-gate-canary-*.html` — real-pixel/real-network enforcement with
  TICK-4 canaries (proves it catches white-on-white / no-dark / loaded-CDN and passes
  hyperlinks + SVG namespaces).
- `index.html` — mounted the kernel: control moved bottom-right (fixes the title overlap),
  last-updated stamp under the title, `cft-soft` superseded. Hollow "Manhattan" claim
  reconciled.
- `cross-lane-manifest.md` — reopened the Confluence founder gate (repo = stale v43; Drive
  holds the real v48). **Confluence has its OWN repo — TSP does not write Confluence trunk
  files.**

## DONE SINCE (2026-07-29, later the same day)

- **Comfort Kernel v2** (`comfort-kernel-v2.html`) — the reconciled standard: Studio Eyes
  (Default/Dusk/Warm-dark + A/A+/A++ + contrast/motion/colorblind) in a reserved chrome
  header (Home · teaspoon · Studio Eyes) that cannot overlap content; bottom Back+Home rail.
- **Phase 3, top level: DONE.** All 50 deployable top-level pages migrated to v2, gate-or-revert,
  independently re-gated 0 HALT, copy-audited against `docs-voice-rubric.md` (one hollow claim
  corrected). The three comfort dialects are dead at top level.
- **Version stamps:** every page opens with "Last updated <computed> · vN <hash>" — version
  derived from git by `version-stamp.py`, never typed. Measured: 0 of 50 below the fold.
- **Copy Auditor seat** (`docs-voice-rubric.md`) — audits agent-added text before push.
- **Games text bank** (`games-text-bank.md`) — games draw base text from Matt's own writing;
  student work and client manuscripts excluded; 4 entries flagged VERIFY.
- **safe-push.sh now blocks on `comfort-gate.py` + `version-stamp.py --check`** (replaced the
  false-positiving studio-eyes contrast/offline checks; canary-proven).

## OPEN

- **Phase 3, subdirs:** `studio/` + `fys/` pages (34) — migration in flight this session; land
  gated results. `archive/` and `rescued/` are dead lanes, not migrated by design.
- **Art:** full C-games / A-client mark-set pass awaits the founder's eye (only clearly-generic
  glyphs were redrawn). Pitches live in `art-pitches.html`.
- **Founder calls pending:** 4 VERIFY flags in the text bank · comfort persistence (no-storage
  floor vs remembering the light choice across pages) · `db/confluence-schema.sql` (only Matt
  has it) · face-copy reconcile vs his Drive original.
- **Face coordination:** TSP-GIT-LANE writes `index.html`; any concurrent session must stay
  read-only on it, or hand off explicitly. This is the standing traffic rule.

---
*Written by TSP-GIT-LANE, 2026-07-29. If you are a cold start reading this: you are the
hands, not the studio. Push, or it is gone.*
