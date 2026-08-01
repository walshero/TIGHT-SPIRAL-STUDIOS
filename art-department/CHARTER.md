# THE ART DEPARTMENT — standing agentic suite
*Founder ruling, 2026-08-01. Recorded the day the founder saw hand-drawn SVG scene art one time too many: "I never want to again."*

## THE LAW

Scene art comes from exactly two lanes. There is no third lane.

1. **MJ** — founder Midjourney generations (his subscription, his eye). Shipped as
   raster plates or vector traces, provenance-marked, SSG teaspoon imprint until an
   artist takes the chair.
2. **LEGAL PHOTO** — CC-BY, public-domain, or official government photography.
   US federal works (Library of Congress, NARA, presidential libraries, official
   White House photos) are public domain and are the first stop for period material.
   Every mount records source, license, and the URL it was verified at. License
   unverified = does not ship.

Hand-authored SVG scene art is dead. **The check is `art-gate.py`** — wired into
safe-push, exit 1 does not ship. Exemptions are earned in markup, not argued in chat:
`data-art-class="instrument"` for charts/maps/meters that display data (Fathom),
provenance strings for MJ traces. UI glyphs under 2.5KB pass silently.

## THE STANDARD: MAD MEN DETAIL

The founder's bar is set-decoration grade period fidelity. Every object in frame is
period-correct or it goes. A 1962 room contains nothing designed after 1962. The
household reads its class register (a family feeling the '69 squeeze has a '59
kitchen). Wear, grime, and light match the era's film stock. "Close enough" is the
enemy; the audit names the object, the year it shipped, and the source that dates it.

## THE ROLES (spawn per need; the workflow `art-sweep` runs them as a fleet)

**Art Director** — owns the shot list. Reads the game's beats, decides what each
screen needs, writes the MJ prompt or the photo-search brief. Never draws.

**Period Librarian** — the legal-photo lane. Searches LOC / NARA / presidential
libraries / Wikimedia Commons, verifies license on the source page (not the search
result), records source-URL + license string per asset. A zero-result search is not
evidence of absence: try the era's own vocabulary.

**Compositor** — mounts plates. Measures screen regions in plate pixels, aspect-locks
containers, composites inserts (broadcast figures into TV glass), embeds base64,
keeps files single-file offline. Never touches mechanics.

**Continuity (the Mad Men seat)** — adversarial period audit of every frame: names
each visible object, dates it, kills anachronisms. Also holds the withholding rule:
no real faces, ever — ID by outline, posture, props.

**Refuter** — tries to break every claim the others make: reproduces mounts headless,
re-checks licenses, re-runs gates. Nothing counts until it survives the Refuter.

## STANDING ORDERS

- Every mount passes comfort-gate AND art-gate before push. No exceptions.
- Play links are COMMIT-PINNED (raw.githack.com/walshero/TIGHT-SPIRAL-STUDIOS/<commit>/<file>) —
  a pinned URL cannot serve a stale game. The branch URL is for bookmarks only.
- Provenance travels in the file: data-art attribute + aria-label, per art-doctrine.md.
- The open chair stands: any human artist replaces any machine mark, credited, permanently.

## THE FIX QUEUE (art-gate sweep, 2026-08-01 — 11 live files HALT)

dad-energy (9 scenes) · fys-treasure-trove (x2 copies) · funny-boneys-factory ·
studio/funny-boneys-oops · leeder-intake · studio/paper-craft-ceiling ·
studio/the-village · studio/tsp-home · the-compound-capstone ·
old-problems-at-new-speed (1 unmarked stray) — plus confluence-TRUNK reported to its
own lane. Worked highest-traffic first: dad-energy, then the face-linked games, then
studio bench pages.
