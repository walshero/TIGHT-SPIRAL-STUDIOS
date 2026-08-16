# THE STUDIO ART BIBLE

*The executable statement of house style. The OS names this as the Direction
layer's standing tool and as "the standing upgrade" that did not exist (§5.2);
this is it. Founder-affirmed 2026-08-14: the studio needs processes and assets
for producing quality art, and that conclusion is correct.*

**Status:** v1, written the day the conclusion was affirmed. Per-build bibles
(CYL's Period Bible, Sound Period Bible) stay authoritative for their own builds;
this governs everything without one.

---

## 1. THE MATERIAL LAW: where art comes from

Two lanes, and Midjourney is not one of them any more.

| Lane | Standing | Rule |
|---|---|---|
| **Studio execution** | Open, and the default | Ships when it clears the execution bar in §3. Made in-file, offline, single-file. |
| **Legal photo** | Open | CC-BY, public domain, or official government photography. Source, licence, and the URL it was verified at are recorded in the mount. Licence unverified = does not ship. |
| **Midjourney** | **CLOSED 2026-08-13** | Founder: *"No MJ in studio as we can do better than we have so far with proper execution."* Closed on a quality argument, not a cost one. |

**What the closure changed.** The 2026-08-01 charter allowed exactly MJ and legal
photo, and killed hand-authored scene art on a quality complaint: *"I never want
to again."* Closing MJ leaves that law permitting one lane, which cannot be what
"we can do better with proper execution" means. The resolution is not that
hand-made art is fine again, it is that **hand-made art is now accountable**.
The 08-01 complaint was never about the medium. It was about art that had no bar
to clear. §3 is that bar, and it is mechanical.

**PENDING, and it is a founder call:** `art-gate.py` still enforces the old
two-lane text and still HALTs inline scene SVG at its byte floor. That is why
`en195-arcade.html` fails its own gate today on the 2026-08-09 Samorost art. The
proposed amendment is in `claude/RULING-NO-MJ-AND-SKIN-B-2026-08-13.md` and needs
the founder's own words before any teeth move. Until then: **CSS scene art ships
freely; inline SVG scene art at or above 2,500 bytes still HALTs.**

---

## 2. THE PIPELINE: the order the work goes in

From OS §5.2, with the stage that keeps getting skipped named first.

1. **DIRECTION.** What it should be. Creative Director owns the spine, Shot
   Director owns the frame. This bible is their standing tool.
2. **CONCEPT / BLOCKOUT.** *The stage the studio keeps skipping, at real cost.*
   Rough the composition, ground value, light source and where the type sits, in
   flat shape. Show the founder. **Nothing gets textured before a blockout is
   signed.** `enjambment-skins.html` is the worked example of what a blockout
   deliverable looks like: four options, identical mechanics in identical
   positions, so the comparison is ground and light rather than layout.
3. **CRAFT.** Make it good. Materials, lighting, staging, palette, motion,
   legibility, wear.
4. **TECHNICAL.** Make it run. Renders, performs, stays accessible, on a real
   device at the reader's own font size.
5. **DIRECTION AGAIN.** The founder's eyes are the Visual Critic HALT. A render
   an AI cannot see is a render only he can rule on.

**The rule this pipeline exists to enforce:** a rejected blockout costs minutes, a
rejected finished skin costs a day. The studio has now paid the day version twice
(the woods in ENJAMBMENT; the Samorost pass in the arcade). Both were built
without a signed blockout.

---

## 3. THE EXECUTION BAR: what "proper execution" means

Not adjectives. These are the rules that replaced the MJ lane, and three of them
are enforced by `art-execution-gate.py` (run `--selftest` to see the teeth bite).

### Mechanically checked

- **TYPE DOMINANCE.** Text on a scene is the brightest thing in that scene. It is
  what the reader is reading and often what they are tapping. Instruments marked
  `data-art-class="instrument"` are exempt: a lamp or a meter reports state and is
  allowed to be brighter than body type.
- **NO CROSS-HATCH TEXTURE.** Two repeating gradients crossed to fake detail
  produce a grid, and a grid reads as a grid. Texture is direction and interval,
  never intersection.
- **NO FLAT LAYER.** A layer of four or more painted shapes at one identical value
  is a band, not a scene. Depth needs at least two values.

### Held by eye, stated so they can be argued

- **SILHOUETTE BEFORE DETAIL.** If the shapes do not read as themselves in
  solid black, no amount of window-lights will save them. Roof lines, edges and
  value steps first.
- **RANK LUMINANCE, DO NOT JUST SEPARATE HUE.** Real neon at distance is
  chromatic but *dark*. Colour difference does not protect legibility; luminance
  difference does.
- **DEPTH IS BUILT, NOT FILTERED.** Layer sky glow, far mass, near mass, ground.
  Do not reach for `blur()` to fake distance behind anything that moves: it is
  priced per frame, and a static paint costs nothing.
- **THE FRAME SERVES THE MECHANIC.** If the game is a machine, the scene is a
  machine room. ENJAMBMENT spent a version with industrial mechanics standing in
  a pastoral forest; the Creative Director's finding was that the skin and the
  mechanics were telling different stories, and it was right.
- **A DARK BEZEL AROUND TYPE.** Where bright scenery is wanted, put hard dark
  between it and the words. This is what makes an otherwise hostile skin legible.

---

## 4. THE ACCESSIBILITY FLOOR: not a separate pass

Every floor below is already mechanical somewhere in the belt. Art does not get to
negotiate with them.

- **18px minimum on every rendered text node**, at the reader's own base. The base
  is `font-size:100%` plus rem multipliers; never override the reader's setting.
- **44px minimum tap target**, including anything in a scene that can be tapped.
- **7:1 contrast** on co-occurring text and background pairs (4.5:1 large).
- **A real dark path**, measured, not asserted.
- **Motion stop is a design, not a deletion.** Reduced motion is about vestibular
  triggers: travel, scroll, parallax, zoom, spin. It was never about removing
  feedback. Everything stops by default; elements marked `.mo-safe` keep a narrow
  non-vestibular vocabulary (opacity, colour, background, border, shadow) with the
  allow-list *enforced* so a marked element cannot animate a transform by
  accident. **The still version gets the same instruments and the same teaching as
  the moving one.** Founder ruling 2026-08-14.
- **No emoji, ever. Offline, single-file, no external hosts.**

---

## 5. THE ASSETS: mount these, do not reinvent them

The Union Rep's standing complaint is that the studio rebuilds what it already
owns. Before authoring a scene, check this list.

| Asset | What it gives you |
|---|---|
| `studio/props-room.html` | The carry-out: comfort kernel source to paste into any build |
| `studio/legibility-optimizer.html` | Tune a surface against the legibility floors |
| `studio/palette-chooser.html` | Studio palette options, green-free |
| `enjambment.html` | **Night-city scene primitives**: layered sky glow, tower silhouettes with per-tower window columns, far-plane neon, wet-ground reflection, steel sign housing with a dark bezel, LED type. All CSS, all gate-clean. |
| `enjambment-skins.html` | The blockout format: identical mechanics across options so only ground and light vary |
| `art-execution-gate.py` | The bar in §3, with canaries |
| `art-gate.py` | The material law in §1 (pending amendment) |

---

## 6. PROVENANCE: unchanged

Every artwork carries its chain: who generated, who traced, who redrew. Studio
execution is studio work. Human redraws are the artist's, credited permanently.
The open chair stands: **any machine-originated mark in this studio is an open
invitation to an artist.** Take it over, and your authorship replaces the
machine's, in the file, for good. Machine art never blocks a human artist and is
never defended against one.

Student work and client materials never enter the art corpus.

---

## 7. WHAT THIS BIBLE STILL OWES

Written down rather than left implied, so the next session inherits the question
instead of the silence.

- **The `art-gate.py` amendment** (§1). Founder call, still open.
- **`en195-arcade.html` is in violation** of its own gate and has been since
  2026-08-09. Nothing has been decided about it.
- **`one-thing-gate`'s SUB-50-TABLEAU cannot be cleared by CSS**, however well
  executed: it counts real image elements. Only the legal-photo lane clears it.
  The Period Librarian seat is seated and unused.
- **No studio-wide palette is fixed here.** `studio/palette-chooser.html` holds
  options; nothing has been ruled.
