# Confluence — Calibration Assessment Hub

A role-adaptive hub for running **calibration (norming) sessions** and measuring
**inter-rater reliability** in academic assessment. Faculty score the same
samples of student work against a shared rubric; Confluence surfaces how
consistently they agree — so program-level results reflect student learning,
not who did the grading.

The name is the idea: a *confluence* is where streams merge. Many raters'
judgements converge into one calibrated result.

## What this delivers

The interface is built around four principles:

- **Adaptive to role** — the entire experience reshapes around who is signed in.
  Navigation, the home dashboard, available actions, and access are all keyed
  off the current role. Switch roles from the sidebar to see the hub change.
- **Coherent navigation** — a persistent **Home** anchor, a **Back** control
  wired to real browser history, and **breadcrumbs** derived from the active
  route on every page.
- **Design elegance** — one cohesive design system: a considered type scale,
  spacing tokens, consistent components, subtle motion, full light/dark support,
  and a responsive layout that collapses the sidebar into a drawer on mobile.

## Roles

| Role | Sees | Can do |
| --- | --- | --- |
| **Assessment Coordinator** | Everything | Create sessions, manage rubrics, monitor reliability, publish reports, configure thresholds |
| **Faculty Rater** | Only assigned sessions + rubrics | Score artifacts, compare to consensus, track personal agreement |
| **Program Lead** | Their program | Review reliability, approve rubrics, view outcome evidence |
| **Reviewer** | Published reports (read-only) | View calibration evidence for program review / accreditation |

Access is enforced, not just hidden: navigating directly to a route outside your
role shows a graceful "not part of your role" state, and switching into a role
that can't see the current page returns you Home automatically.

## Running it

It is a fully self-contained static site — no build step, no dependencies, no
network calls.

```bash
# any static server works; hash-based routing means no server config needed
python3 -m http.server 8000
# then open http://localhost:8000
```

## Deployment (GitHub Pages)

The site deploys to GitHub Pages automatically via
[`.github/workflows/deploy-pages.yml`](.github/workflows/deploy-pages.yml).
Every push to the default branch uploads the repo root as the Pages artifact
and publishes it — no build, no server config. Because the app uses
hash-based routing, deep links resolve on refresh without a 404 fallback.

**One-time setup** (repo owner, only needed the first time):

1. Open **Settings → Pages**.
2. Under **Build and deployment → Source**, choose **GitHub Actions**.

That's it — the committed workflow handles the rest. You can also trigger a
deploy manually from the **Actions** tab (**Deploy to GitHub Pages →
Run workflow**). Once a run finishes, the live URL appears on that run's
`deploy` job and in **Settings → Pages**:
`https://walshero.github.io/confluence-calibration-assessment-hub/`.

> **Note:** publishing a Pages site from a **private** repository requires
> GitHub Pro (or Team/Enterprise). On a Free plan, either upgrade or make the
> repository public before the deploy can go live.

## Structure

```
index.html        App shell (sidebar · top bar · content)
css/styles.css    Design system + component styles (design tokens, light/dark)
js/data.js        In-memory domain model (sessions, rubrics, raters, artifacts)
js/icons.js       Inline SVG icon set
js/app.js         Router, role model, breadcrumbs, views, interactions
```

The data layer is intentionally static so the hub can be reviewed as a
self-contained prototype. Swapping `js/data.js` for a real API is the natural
next step; the reliability metric (currently exact-match agreement) is designed
to be replaced with Cohen's κ or an intraclass correlation.

### A note on names

All personas are **positions**, not real individuals (Assessment Coordinator,
Faculty Rater, Program Lead, Accreditation Reviewer), and every account is
marked **"Sample account"** in the UI. The rater roster and activity feed use
obvious placeholders (Rater A, Rater B, …). No real MassBay staff names are
included — provide an actual roster (names + titles) and it drops straight into
`js/data.js`.
