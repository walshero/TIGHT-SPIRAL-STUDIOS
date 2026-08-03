# Reading the Fireground — Licensed-Photo Lane Manifest
*Fireground-lane spec. Grounded 2026-08-03 via Funes (studio canon) + an Aleph panel (image provenance · learning sciences · fire-domain + dignity). This is the OS §3.2 licensed-photo lane: **spec'd in-sandbox, photos produced/verified in a capable session.***

---

## MEDIUM GATE — settled
A documentary of real LODD incidents is the **licensed-photo lane** (OS §3.2, Q1: "does genuine real-world realism carry the meaning?"). Studio-drawn cut-paper art here was a **gate violation** ("jamming everything through cut-paper" — the failure §3.2 names) **and** a dignity breach: real firefighters died in these incidents; they are not rendered as stylized art. Studio art is removed. Slots now render real-photo placements (image + mandatory source credit) with a dignified "placement pending" plate until verified photos land.

## DIGNITY CONSTRAINTS (hard — every slot obeys)
- **Allowed:** investigation/forensic photos, training/size-up stills, exterior structure · smoke · construction · air-track · roofline · spalling/rebar, aftermath/rubble **without victims**.
- **Never:** victims, bodies, identifiable casualties or families; flames-as-spectacle ("fire porn"); any image whose purpose is shock rather than a size-up cue.
- **Framing:** the fire service treats LODD material as **memorial + instruction**, not entertainment. The lessons were paid for in these lives; the imagery serves prevention. Never imply death is "part of the job."
- **Provenance:** caption every image with source (+ photographer/agency where known). Never crop out credit, never launder provenance, never present a render/reconstruction as an actual scene photo.

## SOURCING RULES (provenance seat)
- **Self-host — do NOT hotlink.** (USFA gallery 403s bots; hotlinks are unstable.) Download → commit to `fireground-assets/`.
- **Tier 1 (zero-risk, carries the demo):** **USFA Fire Service Image Gallery** (copyright-free federal; courtesy "U.S. Fire Administration") · **DVIDS** (PD federal; credit "Photo by [Rank Name], [Unit]", no endorsement implied — per-asset copyright check).
- **Tier 2 (named-incident authenticity):** **NIST** (Charleston, Champlain) + **NIOSH** LODD reports (truss) — **only figures authored by NIST/NIOSH staff.** Drop any figure captioned "courtesy of [a fire dept / individual / media]" (third-party copyright, not clearable by the federal-work rule).
- **Excluded:** **UL FSRI** (permission-gated). **San Diego "Reading Smoke" drill** — its imagery is **Dave Dodson's copyrighted "Art of Reading Smoke"** material: a **study reference for the schema, NOT an image source.**
- Credit lines: NIST → "Reprinted courtesy of the National Institute of Standards and Technology, U.S. Department of Commerce." · NIOSH → "Source: NIOSH." · USFA → "U.S. Fire Administration." · DVIDS → "Photo by [Name], [Unit]."

## PEDAGOGY (learning-sciences seat) — the engine this reskin serves
Perceptual-classification engine, not a quiz. **image → predict (private, under uncertainty) → reveal the record.** An image earns its slot only when the **size-up cue is in the frame** (no decorative/aftermath shots the learner couldn't have predicted).
- **Read schema = B-SAHF** (Building · Smoke · Air track · Heat · Flame; Hartin) + **Dodson's Reading Smoke** (volume · velocity · density · color). The learner's read AND "what the record shows" answer the **same** dimensions → like-for-like reveal.
- **Confidence → calibration:** capture the read + a confidence; on reveal, surface the gap ("you read X at Y% confidence; the record shows Z") — no score, ever.
- **Contrasting cases + faded scaffolding:** name the cue frame early, strip prompts later; pair look-alike incidents that read differently.
- Sources: Kellman PALMs (kellmanlab.psych.ucla.edu/files/kellman_2013.pdf) · Dodson, Art of Reading Smoke (fireengineering.com) · Hartin B-SAHF (cfbt-us.com/wordpress/?p=878) · calibration (lifescied.org/doi/10.1187/cbe.18-10-0202).

## PER-SLOT IMAGE SPEC (source · cue-in-frame · credit)
**Charleston — Sofa Super Store, 2007 · NIST SP-1118** (9 LODD)
- `charleston-1` — **Building/fuel load.** Exterior of a big-box furniture showroom, open plan, no sprinklers. Source: NIST fig (staff) or USFA commercial-structure exterior. Credit: NIST / USFA.
- `charleston-2` — **Smoke + Air track.** Under-ventilated, pressurized smoke banking down; front windows failing (~24 min) admitting air → vent-induced flashover. Source: USFA/DVIDS reading-smoke still or NIST fig. Credit accordingly.
- `charleston-3` — **Flame/spread.** Rapid fire spread across the open fuel load post-ventilation. Source: NIST fig / USFA. Credit accordingly.

**Hackensack — Ford dealership, 1988 · NIOSH FACE (bowstring truss)** (5 LODD)
- `hackensack-1` — **Building (construction ID).** The humped/curved **bowstring-truss** roofline over a long-span service bay — recognizing the profile is the lesson. Source: NIOSH fig / USFA truss building. Credit: NIOSH / USFA.
- `hackensack-2` — **Smoke from the void.** Smoke pushing from the truss loft/eaves, not the occupied floor — fire in the concealed cockloft. Source: NIOSH / USFA. 
- `hackensack-3` — **Collapse.** Collapsed bowstring-truss roof section over the service bay (no victims). Source: NIOSH FACE figure (staff). Credit: NIOSH.

**Champlain Towers South, 2021 · NIST NCST** (structural read — NOT smoke)
- `champlain-1` — **Pre-collapse distress.** Garage/pool-deck: spalling concrete, exposed/corroded rebar, cracking at column–slab connections, standing water. Source: NIST NCST staff photo. Credit: NIST.
- `champlain-2` — **The structure.** The high-rise in context (night/exterior) — the read is structural, not smoke. Source: NIST/USFA (no victims). 
- `champlain-3` — **Progressive collapse.** Punching-shear-initiated partial collapse / rubble field (no victims). Source: NIST NCST staff. Credit: NIST.

## INGEST (per OS §3.2 — produced in a capable session)
Self-hosted binaries can't be committed from this sandbox (proven: MCP passes strings that corrupt binary; Zapier's binary-safe transfer only fires inside a real multi-step Zap). Two ways the verified photos land in `fireground-assets/`:
1. **GitHub web upload** (fastest) — drag the file into the repo on the fireground branch.
2. **Drive→GitHub Zap** (one-time, then automatic): *[Google Drive: Find/Retrieve File] → [GitHub: Create or Update File]*, mapping the Drive **File** output into GitHub's **File Content** field (server-side hydration, tokenless via the OAuth connection). See `DECISION-zapier-auth-lane.md`.
- **Ready now:** `nist-charleston-image.jpg` sits verified-clean in the studio Drive (`walshero`, id `1xX9EGKjgb2jWePDpLO5M4nS6Dm_FhHIQ`, 34,459 B, 325×221) — the first drop-in for a `charleston-*` slot once its NIST-staff provenance is confirmed against the report caption.

## WIRING
Each moment's `art:{label, img, credit}` — set `img:"fireground-assets/<slug>.jpg"` when the verified file lands; empty `img` renders the pending plate. `label` is the cue description (already pedagogically load-bearing). Credit is mandatory and shown in the caption.
