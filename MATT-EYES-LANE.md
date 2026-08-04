# THE MATT-EYES LANE — private parking lot (sharing/privacy canon)
*2026-08-04. Added when the studio grew a private lane for Matt's own material.*

The Lane Registry answers **where a file lives** (repo / Netlify / Drive / shelf).
This file answers a different question: **who is it for.** Most studio work is
shared — a public face, shared lanes. Some is not. The Matt-eyes lane is the
private one.

---

## THE NEAR-MISS THAT PRODUCED THIS FILE
Setting up Matt's private "parking lot" dashboard, the first plan was to keep
personal material (creative drafts in progress, personal bills & receipts, the
ADA credit appeal) simply **unlinked** from the studio face.

**"Unlinked" is not "private."** The studio deploys to GitHub Pages, so an
unlinked page in a *public* repo is still reachable by URL and indexable by
search engines. Personal bills on a public URL is unrecoverable — cached and
indexed even after deletion. The plan was one push away from a leak.

So the lane is real, it has a **private home**, and it has an **enforcer**.

---

## WHAT IS MATT-EYES (routes to the private lane)
- Creative writing drafts **in progress** (until Matt chooses to ship one)
- Personal **bills, receipts, statements, scans** → the private cloud folder
- Personal **admin & appeals** (e.g. the Anthropic ADA credit appeal)
- Anything **parked**: "later, not now, not public"

## WHAT IS NOT
- Studio deliverables, engine / OS / quality tooling, anything meant to ship —
  those go to the **shared** studio lanes and the public face.

---

## THE HOME
| Piece | Where | Why |
|---|---|---|
| **Dashboard + text/drafts** | `walshero/matt-radar` (**private** repo) | No public Pages. Its `index.html` is the private dashboard; `parking-lot/` holds parked items. Carries a `.matt-eyes-home` marker at root. |
| **Bills / receipts / scans** | a **private cloud folder** (Drive/Dropbox) | Financial files stay in the cloud folder, **never committed to any repo**; the dashboard links to the folder. |
| **Creative drafts** | `walshero/-writerly-moves-game` (private) + matt-radar links | Already off the public street. |

## HOW A FILE DECLARES THE LANE
- HTML: `<meta name="tsp:lane" content="matt-eyes">`
- text/markdown: a line `tsp:lane: matt-eyes`

## THE ENFORCER (`matt-eyes-lane-check.py`) — fool-me-once teeth
- A repo is the **home** if a `.matt-eyes-home` file sits at the scan root (or
  `MATT_EYES_HOME=1`). Home => Matt-eyes files are allowed.
- Any **shared/public** repo containing a Matt-eyes file => **HALT** (exit 1).
  Wired into the hub gate (`floor.yml`) as a fast, blocking step **before** the
  Studio-Eyes install — a leak never reaches the Pages deploy.
- Self-testing: a Matt-eyes file must HALT out-of-home and pass in-home, and a
  plain file must be ignored in both; if a fixture lies the tool exits 2 and
  refuses to certify.

## THE ORPHAN RULE IS MOOT HERE (no exemption needed)
CLAUDE.md: "`index.html` accounts for every page in the repo — nothing is
orphaned." That is a **public-repo** rule and it stays intact. Matt-eyes pages
are never in the public repo (the gate guarantees it), and in the private home
the dashboard is its own face and links its own pages. The tension resolves
itself — no special-case in the orphan checker.

## THE STANDING RULE
> If a page or file is personal, in-progress, or nobody-else's-business, it goes
> to the Matt-eyes lane — the private `matt-radar` home (and the private cloud
> folder for financial docs) — **never** to a shared or public lane. Tag it
> `tsp:lane: matt-eyes` and the gate keeps it honest.
