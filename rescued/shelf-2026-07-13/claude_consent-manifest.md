# Consent Manifest — Tight Spiral / Confluence
*The record that makes named student work publishable. One row per person per work. Portable Markdown, HITL-owned by Matt. Draft scaffold — fill and verify before anything relies on it.*
*Created 2026-07-13. Not legal advice; the assessment-data rows in particular route through the Chair + Provost before publishing, per the TSP Ledger gate.*

## Why this file exists
The guard used to treat any student name on a public page as CRITICAL. That was too blunt — a published Lumière author or a public award winner is not a leaked education record. But "Matt says it's fine" is not a FERPA basis either. This manifest is the middle: it records, per name, *why* the appearance is allowed, so the claim is documented and checkable instead of asserted. It also survives tool changes — it's just text.

## The rule the guard checks (arithmetic, not judgment)
For every personal name that appears on a public Confluence/Tight Spiral page:

- **GREEN — publishable** if the name has a manifest row with a consent basis of `published-lumiere`, `public-award`, `directory-info`, or `signed-release`, AND the on-page use stays within that row's Scope.
- **RED — CRITICAL** if the name is joined to assessment data (a score, ISLO level, calibration rating, grade) — *regardless of any award or publication*, because a public award never makes a private score public. Assessment-joined names need `signed-release` + Chair/Provost sign-off, or they get de-identified.
- **RED — CRITICAL** if the name has no manifest row at all.

A published author is green as an author. The same student wired to an assessment result is red until a signed release says otherwise. Name alone ≠ exposure; name + score = education record.

## Consent-basis legend
- `published-lumiere` — work the student submitted to and had published in Lumière (public creative publication, author participated). Lowest risk. Source = the public issue URL.
- `public-award` — publicly announced honor (CCHA placement, Lumière award). FERPA "honors and awards" category; cleanest when the college has designated it directory info and the student hasn't opted out. Route recognition through the Chair to confirm no opt-out.
- `directory-info` — item the college formally designates as directory information and the student has not suppressed. Institutional determination, not personal — confirm via the registrar/Chair, don't self-certify.
- `signed-release` — a dated permission form on file from the student (see `lumiere-release-and-consent.md`). Required for anything beyond the three above — unpublished classwork, assessment excerpts, name-to-score joins.
- `assessment-data` — NOT a consent basis. A flag meaning this row touches protected performance data; blocks publish until a `signed-release` + Provost conversation exists, or the data is de-identified.

## Manifest

| Student | Work / how they appear | Type | Consent basis | Obtained (date) | Source / file | Scope — what may appear | Revocable? | Notes |
|---|---|---|---|---|---|---|---|---|
| Georgia Oakley | Lumière award | public-award | UNVERIFIED — confirm no directory opt-out via Chair | — | (Lumière issue URL) | Name + award + published piece only. No scores. | Yes | Likely green once opt-out checked |
| Nathan Desmarias | Lumière award | public-award | UNVERIFIED — confirm no directory opt-out via Chair | — | (Lumière issue URL) | Name + award + published piece only. No scores. | Yes | Likely green once opt-out checked |
| Peter Kistner | CCHA First Place essay | public-award | UNVERIFIED — confirm public announcement + no opt-out | — | (CCHA announcement URL) | Name + award only. No scores. | Yes | |
| Nick Giancioppo | CCHA award | public-award | UNVERIFIED | — | (CCHA announcement URL) | Name + award only. No scores. | Yes | |
| Chelsea Dow | CCHA award | public-award | UNVERIFIED | — | (CCHA announcement URL) | Name + award only. No scores. | Yes | |
| Gabriela Moreno | CCHA award | public-award | UNVERIFIED | — | (CCHA announcement URL) | Name + award only. No scores. | Yes | |
| Sarah Courchesne | (student writer) | signed-release | NEEDED — basis unclear; hold until confirmed | — | — | Nothing until basis established | Yes | Was not on faculty roster; treat as student |
| Lena Sebugwawo | Alum, founded Suubi magazine | public-award / self-public | UNVERIFIED — alumni bio, likely OK with a note | — | — | Public bio facts only | Yes | Alumni ≠ current-student FERPA, but confirm |
| David Earl | Alum, MFA candidate | public / self-public | UNVERIFIED | — | — | Public bio facts only | Yes | |
| Faisal Murad | Alum, teaches writing | public / self-public | UNVERIFIED | — | — | Public bio facts only | Yes | |
| Diego Rocha | Alum, visiting professor | public / self-public | UNVERIFIED | — | — | Public bio facts only | Yes | |
| JayJay Conrad | Alum, teaching poetry | public / self-public | UNVERIFIED | — | — | Public bio facts only | Yes | |

*Faculty/staff (Codrington, McCarthy, Donato, McGrath, Adeyemi, Lyons, Walsh) are a separate question from student consent — that's a "publish work emails on a personal repo?" decision, not FERPA. Handle in the page-cleanup pass, not here.*

## How to use
1. Fill a row before a name goes on any public page. Empty/UNVERIFIED = not yet publishable.
2. For `public-award`/`directory-info`, one email to the Chair confirms no opt-out — that's the whole cost, and it's delegable.
3. For anything touching classwork or scores, use the release form in `lumiere-release-and-consent.md` and log the signed-copy location here.
4. Keep this file walshero-owned (the durable shelf), never the post/MassBay account.
