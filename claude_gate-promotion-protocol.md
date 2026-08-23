# Gate Promotion Protocol — report → blocking

Tight Spiral Productions. Written 2026-07-27.

A gate that runs `continue-on-error` **spins but does not drive**: it reports findings but
cannot stop a bad commit. Promotion turns a report gate into a blocking one. This is the system
for **approving and implementing** that promotion, so it is a ratified, wired act — never a silent
flag flip.

## The bar: BOTH must hold

A gate may go **blocking** only when:

1. **Objective readiness** — it is green on the builds it will block (its `blocking_scope`), with
   the evidence recorded in `canon-manifest.json → gates[].promotion.evidence`.
2. **Founder go ≥ 70%** — `promotion.founder_go: true` with `promotion.confidence >= 0.70`.

Founder-go alone is **not** enough (the corpus can still be red); green alone is **not** enough
(the founder owns the risk of blocking). Both, or it stays report.

## The ratchet

A gate blocks **where it is green** and reports **where it is not** — per build. `staging-sandbox`
went blocking on `index.html` (0 FLAGs) while the other three corpus builds, which still carry
landmark/tap-target debt, stay in `report_scope` until cleared. Debt can only shrink; a build joins
`blocking_scope` when it earns it.

## How it is enforced (the coupling)

`canon-guard --gates` (blocking, in `floor.yml`) couples the **approval ledger** to the **actual
wiring**:

- a gate declared `blocking` **must** carry founder-go ≥ 0.70 **and** be wired in `floor.yml` as a
  **non-`continue-on-error` `--strict` step** covering its `blocking_scope` — *approval without
  enforcement HALTs*;
- a gate declared `report` **must** run under `continue-on-error` — *a report gate that secretly
  blocks HALTs*.

So the manifest and the workflow cannot drift: you cannot claim a gate blocks without wiring it,
and you cannot wire a block the founder has not ratified. Self-tested — the guard HALTs on a
sub-0.70 confidence and on a ratified-but-unwired scope (canaries, 2026-07-27).

## To promote a gate (the steps)

1. Get it green on the target build(s); capture the evidence (e.g. `staging-sandbox.py <build>` →
   0 FLAGs, or a green CI run).
2. Get founder go — record `founder_go: true`, `confidence: >= 0.70`, `by`, `date`, `evidence` in
   the gate's `promotion`. Add the build(s) to `blocking_scope`.
3. Wire it: add/extend a non-`continue-on-error` `--strict` step in `floor.yml` over that scope.
4. Run `canon-guard --gates` locally — it must say `ok` for that gate. Commit; CI re-affirms.

Currently ratified blocking: **staging-sandbox** on `index.html`. Report, awaiting readiness +
go: **studio-eyes-v3**, **axe-audit**, **contrast-plus** (see the ledger for each one's evidence gap).
