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

## OPEN

- **Phase 3:** mount the kernel across the remaining ~130 files — start with the `softer/warm`
  cohort (kills the shared white-on-white bug at the root), then the 83 files with no comfort
  system. Each file must pass `comfort-gate.py` before it ships.
- **Face coordination:** TSP-GIT-LANE writes `index.html`; any concurrent session must stay
  read-only on it, or hand off explicitly. This is the standing traffic rule.

---
*Written by TSP-GIT-LANE, 2026-07-29. If you are a cold start reading this: you are the
hands, not the studio. Push, or it is gone.*
