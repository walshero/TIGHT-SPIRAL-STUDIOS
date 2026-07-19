# SELF-DIAGNOSIS — TSP, 2026-07-19

**Written after five days of a site-wide 403 that was never a delivery bug,
a cache, or a bad file — it was the accessibility gate biting the front door.**

---

## THE DIAGNOSIS IN ONE LINE

**We wired the accessibility ratchet onto the deploy path with Pages Source set
to "GitHub Actions," and then pushed regressions straight to `main` — so a single
failing check did not fail a check, it took the entire live site OFFLINE with a
403, and every "nudge" re-ran the thing that was holding the door shut.**

---

## PART 1 — WHAT ACTUALLY WENT WRONG

The symptom was a consistent `403 Forbidden` across **every** URL on
`walshero.github.io/TIGHT-SPIRAL-STUDIOS/`, returning the same GitHub error page
(md5 `1f5fcbc`) for days. It looked like a Pages-delivery or config failure.
Empty-commit "nudges" (e.g. `445b21a`) were pushed to force a rebuild. None worked.

They could not work. Here is the real chain:

1. **Pages Source was switched from "Deploy from a branch" to "GitHub Actions."**
   The branch builder (`pages-build-deployment`, the `dynamic` event) last ran
   **2026-07-11** and never again — while `main` kept receiving pushes. That is
   the fingerprint of the source flip: under "GitHub Actions," the automatic
   branch build stops and a workflow must publish instead.

2. **`floor.yml` became the only publisher**, via its `deploy` job
   (`configure-pages` → `upload-pages-artifact` → `deploy-pages`).

3. **`deploy` was chained to the gate**: `needs: floor` + the default success
   requirement. `deploy` runs only if the `floor` job SUCCEEDS.

4. **The ratchet armed 2026-07-14** (`ratchet.py`, no `continue-on-error`). From
   that day, any push carrying a NEW halt made `floor` exit 1.

5. **We push regressions straight to `main`** (the failing runs are `event=push`
   on `main`, not PRs). So: regression on main → `floor` fails → `deploy` skipped
   → no fresh Pages deployment under the Actions source → the endpoint served the
   GitHub error page. Not a 404 (missing) — a 403, the "nothing valid is
   published here" face.

6. **The nudge made it worse, not better.** An empty commit re-runs `floor`,
   which re-runs the same `ratchet.py`, which fails on the same files, which
   re-skips `deploy`. The instinct to "re-trigger the build" fed the exact
   mechanism holding the site down.

The five regressions that were actually blocking the door (run on `445b21a`):

| File | Halt the ratchet caught |
|---|---|
| `dad-energy.html` | `.arcade-foot` contrast 4.3:1 (low) |
| `leeder-intake.html` | conflicting version banners v1/v2/v3 (H8, file disagrees with itself) |
| `motion-specimen.html` | dark class referenced, no parseable dark palette (H3, untested stop) |
| `tsp-opportunity-bridge.html` | `.status.wait` = 1.0:1 INVISIBLE; external resources |
| `your-rp-world.html` | external hosts (clinicaltrials.gov, …); offline floor broken (H7) |

**The gate was not wrong. The arithmetic was right.** `.status.wait` really was
invisible; `your-rp-world` really did reach off-box. The ratchet did its job.
The failure was in the *blast radius*: a per-file accessibility miss detonated
the whole site.

---

## PART 2 — HOW IT CLEARED (and it was not a "fix" typed at the 403)

Nobody found a Pages setting to toggle. The site came back because the **debt got
paid on the pages themselves**, which let the coupled gate finally pass:

- **PR #3** (`ee010c8`, "Studio front door … clear CYL v5 regression").
- **PR #4** (`43fcbae`, "inline mobile module into each page — single-file-offline
  law"). Inlining the mobile module removed the external hosts, which killed the
  H4/H7 halts on `your-rp-world` and `tsp-opportunity-bridge`.

On `43fcbae` the ratchet returned **0 regressions**, `floor` **passed**, `deploy`
ran, and `actions/deploy-pages` logged **"Reported success!"** with
`Evaluated environment url: https://walshero.github.io/TIGHT-SPIRAL-STUDIOS/` at
**2026-07-19 14:27 UTC**. The site was restored — by the ratchet turning one way,
exactly as designed, once the corpus was clean.

**Verified from source, not from faith:** cloned the repo, reproduced the sweep
with `bs4` ABSENT (matching CI, which installs only `playwright` + `axe-core`),
`python3 ratchet.py` → exit 0 on the current `main`. Confirmed the `deploy` job
(id `88203200016`) all-green and the deploy-pages liveness report.

**One honesty caveat:** the diagnosing sandbox's egress proxy blocks `*.github.io`
(every fetch returns a proxy-level 403, not GitHub's), so the live page could not
be eyeballed from inside the box. The *pipeline* proves a live deployment; the
human confirmation is a hard-refresh.

---

## PART 3 — THE LESSON (and it is not "the gate is bad")

The 2026-07-11 comment in `floor.yml` said "A gate that does not block is not a
gate." True. But we learned the other half the hard way:

> **A blocking gate placed on the DEPLOY-of-the-live-site, fed by direct pushes to
> `main`, is not a quality gate. It is a site-wide kill switch wired to a tripwire
> anyone can step on.**

Under "Deploy from a branch," a failed check leaves the last good build serving —
the site degrades to *stale*, never to *gone*. Under "GitHub Actions" with the
deploy gated on the check, a failed check makes the site *gone*. We moved the
chokepoint to the worst possible place: between the user and the whole front door.

And nothing told us the site was DOWN. The signal read "a check is failing" — a
yellow, routine-looking thing — when the truth was "every visitor gets a 403."
The studio ate a **5-day outage** (armed 07-14 → restored 07-19) with no alarm
that said *outage*. This is the same class as TICK 4 / "the gate went blind":
a monitor reporting the wrong severity is a monitor that lies.

This was even foreshadowed: the 2026-07-18 ledger's STILL-OPEN line — *"wire the
gates into GitHub Actions on push"* — is exactly the thing that, done without
decoupling liveness, produced this 403.

---

## PART 4 — THE FIX FORWARD (a decision, not an invention)

Three ways to guarantee an accessibility regression can never again take the live
site down. They are not equal.

**(a) RECOMMENDED — keep the teeth, move the chokepoint to the MERGE, not the
deploy.** Require pull requests into `main`, with the `floor` check as a required
status check (branch protection). A regression then fails the *PR* and never lands
on `main` — so `main` stays green, and deploy is never asked to publish broken
work. This is the studio's own PEP philosophy ("a chokepoint every request must
pass through") put in the right place: the gate guards *entry to canon*, not
*delivery to the public*. Cost: stop pushing straight to `main`.

**(b) Decouple deploy from the gate.** One line — `deploy: if: always() &&
github.ref == 'refs/heads/main'`. The site ships regardless of the ratchet; the
ratchet still runs and reports RED. Cost: an inaccessible page *can* go live —
which, for a founder losing vision, is the wrong default. Use only as an emergency
escape hatch. (Patch below; NOT applied.)

**(c) Switch Pages Source back to "Deploy from a branch → `main` → /root."** The
last good build always serves; the gate becomes advisory. Most durable against
outage, weakest teeth. A Settings-only change.

**Also, regardless of a–c: give the site its own liveness probe.** The hourly
Integrity Guard already runs; extend one probe to assert **HTTP 200** on the Pages
URL and shout if it is 403/404. "The site is down" must be detectable AS ITSELF,
not inferred three layers down from a red check. A 5-day outage with no alarm is
the real bug here.

### The (b) escape-hatch patch, for the record — NOT applied

```yaml
  deploy:
    needs: floor
    if: always() && github.ref == 'refs/heads/main'   # was: github.ref == 'refs/heads/main'
```

Recommendation stands at **(a) + the liveness probe.** The ratchet earned its
keep this week — it did not fail, it fired. It just needs to fire at the door to
canon, with the live site wired somewhere it cannot be held hostage.
