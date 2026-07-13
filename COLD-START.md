# THE COLD START

**The pathway for walking into the studio with nothing in your hands.**

Locked 2026-07-13. This file is law. It lives in the repo because the repo is home.

---

## THE NAME

Every prior session began **warm** — a 200-file shelf preloaded into context, most of
it stale, all of it indistinguishable from canon by inspection. The machine walked in
holding nine-version-old copies and could not tell. That is not memory. That is a
cache with delusions.

**The Cold Start is the opposite: walk in holding nothing, and fetch what you need
from the one lane that cannot lie.**

Cold is not ignorance. Cold is *refusing to trust a copy.* A cold Claude knows exactly
four things and computes the rest. A warm Claude knows two hundred things and half of
them are wrong.

> **Canon is computed, not remembered.**
> The shelf is a cache and it lags. Drive is an address book, not an archive.
> Git is the only lane with a mechanism that prevents two versions of the truth.

---

## WHY COLD BEATS WARM (the arithmetic)

This is not preference. It was measured on 2026-07-13.

| lane | files | can it tell canon from fossil? |
|------|-------|-------------------------------|
| **Repo (git)** | 288 | **Yes.** Content-addressed. One canon per path. History. |
| Shelf | 163 | No. A filename and a date. `sandbags.html` was the *retired comfort-gate build* and looked identical to canon. |
| Drive | ~250 + 20 subfolders | No. Eighteen copies of `confluence-TRUNK`. Six of `choose-your-leader-full`. Seven of `studio-eyes-sweep.py` — one of them **20 bytes**, a stub sitting next to the real 9,608 B tool. |

A big shelf does not make the machine smarter. It makes it **confidently wrong**, which
is worse than empty-handed. The 2026-07-13 audit found:

- Two "possible stubs" that were the opposite — the *shelf* held the old walled builds.
- 44 files reported as homeless orphans that were deployed all along.
- Both findings came from tools that were *lying*, and the lies were only visible
  because someone computed instead of trusted.

**An audit that lies is the disease.** A shelf you cannot verify is the same disease,
one layer up.

---

## THE FOUR FILES

A new project shelf holds **four files**. Not the rescued folder. Not two hundred.

`rescued/` is a **morgue** — it is where files went that were about to die in a single
lane. It is provenance, not working canon. **Do not start a project from a morgue.**

| file | what it is | why it must be resident |
|------|-----------|------------------------|
| `tight-spiral-studio-os.md` | The constitution. Identity, floors, medium gate, panel, pipeline, patterns. | It is the law. It cannot be a fetch, because you must know the law *before* you know you needed it. |
| `STUDIO-COMMAND-CENTER.md` | Live state. What is gated, what is shipped, what is blocked, what is owed. | Answers "where are we" without a tool call. Rewritten at every belt close. |
| `LANE-REGISTRY.md` + `cross-lane-manifest.md` | Who owns what. RW vs RO. The addresses. | Prevents the concurrent-writer class of failure. TSP does not build Confluence; this is where that is enforced. |
| `COLD-START.md` | This file. | A pathway that must be remembered is a wish. It has to be readable on arrival. |

Everything else — **all 284 other files** — is **fetched on demand from git**, verified,
and dropped. That is not slower in any way a human notices. It is *correct by default*,
which the alternative never was.

---

## THE PATHWAY (do these in order)

**1. Fetch before you touch.**
Any named file, any edit, any claim about its contents:
```
git ls-tree -r --name-only origin/main | grep <name>
git show origin/main:<path>
```
Never the raw CDN — it caches ~5 minutes and **will lie to you**. Never the shelf copy.
Never a remembered byte count.

**2. Diff before you decide.**
If two lanes disagree, do not default to newer, older, larger, or smaller.
**Decide from content.** The `claude_cliche-*` forks were newer by commit date and
*older by content*. `sandbags.html` was larger on the shelf because it held the
**retired comfort-gate wall**, not more game. Size is not a signal. Date is not a signal.
Content is the only signal.

**3. Absence of a hit is not evidence of absence.**
A zero-result search means you searched wrong. List the container and look.
This rule exists because a search miss once got `confluence-TRUNK v42` declared a phantom.
It was not a phantom.

**4. Land it in the same turn.**
`outputs/` evaporates. `"success: true"` is never proof.
Push, then **fetch it back from git and match the hash**. If it isn't in a real lane
before the turn ends, it does not exist.

**5. Run the audit; do not trust it.**
`resolve-canon.py --audit`, from inside a clone. It HALTs (exit 2) rather than guess.
But it has lied twice — once via a rate-limited API that returned an empty list, once
via a non-recursive `ls-tree` that hid 182 files. **The auditor is in the critical path,
so the auditor gets audited.** When it says something surprising, verify the tool before
you act on the finding.

**6. If a rule can't be a check, it's a wish.**
There are already ~30 rules. Do not answer a failure by writing rule 31.
When six rules should have caught something and only the arithmetic one did, the answer
is **more arithmetic**, not more prose.

---

## WHAT THIS COSTS

Honest accounting:

- **A few seconds per file.** Fetching from git instead of reading a resident copy.
- **You lose the illusion** that the machine already knows. It does — it knows the law,
  the state, and the map. It does not pretend to know the contents of 288 files it
  hasn't opened.

## WHAT THIS BUYS

- The machine cannot edit a nine-version-stale file, because it never holds one.
- The machine cannot report a fossil as canon, because it never has a fossil resident.
- **Accessibility.** Four files is a shelf a person with retinitis pigmentosa can
  actually scan. Two hundred is a wall. This is not a side benefit — it is the point.

---

## THE SUCCESSION

- **Repo** — home. Canon. Git prevents two truths. *Everything lands here.*
- **Shelf** — a four-file working set. Resident law and state only.
- **Drive** — an address book. Useful for finding things and for phone access.
  **Never canon.** It has no mechanism to prevent eighteen copies.
- **`rescued/`** — the morgue. Provenance for files that once lived in one lane.
  Read it to know what nearly died. Do not build from it.

---

*A studio that is yours does not keep its constitution on an employer's server,
and does not keep its canon in a folder that cannot tell a stub from a tool.*
