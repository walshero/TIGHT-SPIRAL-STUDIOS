---
name: fireground-image-scout
description: >-
  Sources verified public-domain fireground imagery (fire behavior, smoke reads,
  structural collapse / USAR) for a TSP build and embeds it. USE WHEN a case has a
  scene tagged NIST-SOURCE-PENDING or carries authored-SVG placeholders; when the
  user says "find/scout/source images" for smoke, fire, flashover, or collapse; or
  when a new fireground case is scaffolded. Also `/scout`. DO NOT use for generated
  art, for non-fireground imagery, or when the user has already supplied the exact
  files (embed those directly). Produces a verified per-scene shortlist and, when the
  fetch loop is live, the embedded images themselves.
---

# Fireground Image Scout — TSP's first forward-researcher

A single-purpose agentic researcher. It explores the **semiotic domain of fireground
imagery** — the sign-system of what *reads as* a given fire/collapse condition, and the
licensing grammar around it — and returns real, public-domain, correctly-credited stills
mapped to specific build scenes. Built on the Anthropic orchestrator–worker pattern,
tailored to TSP's seats, gates, and kernel track.

## Launch gate (when optimal — do not fire on everything)
Launch only when ALL hold: (1) a scene is genuinely unfilled (`NIST-SOURCE-PENDING` or an
SVG placeholder), (2) public-domain sourcing is plausible for that condition, (3) the value
is worth a fan-out. Otherwise answer inline or keep the authored SVG. This is the Aleph seat
pointed at research spend: *finish this scene, don't sweep for its own sake.*

## Method — orchestrator → workers → verify → synthesize
1. **Decompose** the need into per-scene briefs (the exact fire behavior / collapse
   condition each screen must show — pull these from the case's `known` items and prompts).
2. **Fan out workers on orthogonal source axes** (each blind to the others; this IS the
   domain map):
   - **by agency** — NIST, FEMA, USFA, DHS/US&R
   - **by artifact** — report/technical-note figures · press & image galleries · burn-cell series
   - **by condition** — does it depict *this* read (pushing smoke / dropping neutral plane /
     banked ceiling / leaning wall over pile / debris void / multi-crew site)
   Use `WebSearch` (works from the sandbox) to find and locate; triangulate across axes.
3. **Verify — adversarial, and SEPARATE from discovery.** Two lenses that HALT:
   - **License (Registrar seat):** is it *genuinely* public domain — federal-employee work,
     not a third-party image merely reproduced inside a federal PDF? Name the source + the
     credit line (`Madrzykowski/NIST`, `FEMA/<photographer>`) + as-of date. Unattributed →
     HALT.
   - **Fidelity (Hand + Stranger seats):** does it actually show the diagnostic condition,
     not a generic card? **View it** (see the pipeline below — the scout CAN see images) and
     confirm by eye. A firefighter must not learn the wrong read. Fabricated/AI fire → HALT.
4. **Synthesize to kernels.** Per scene: chosen URL, license verdict, credit line, why-it-fits,
   one honest doubt, confidence tier. Provenance-chained, decay-clocked — feeds the Kernel Track.

## The mechanical pipeline (fetch + read-back + embed)
Egress note: the sandbox proxy 403s the open web; `WebSearch` works but `curl`/`web_fetch`
of assets do not. Bring bytes in via Zapier (server-side fetch). See
`LANE-REGISTRY.md § THE ASSET-INGEST LANE`.

1. **Fetch:** Zapier Google Drive **Upload File** with `file`=<verified URL>, **`convert=false`**,
   and **an explicit `folder`=<a native-visible Drive folder ID>**.
   ⚠️ **READ-BACK FIX (verify on first live run):** uploads that OMIT the folder land in a
   space the native Drive connector cannot see; the one upload with an explicit folder landed
   visibly. Always set `folder`. Confirm the file then appears via native `search_files`
   (`parentId = '<folder>'`) — if it does, read-back is solved end-to-end.
2. **Read back:** native `search_files` to get the real file ID → `download_file_content`
   (base64) → decode to a local file.
3. **View + verify:** open the decoded image with the **Read tool** (proven: the scout can see
   images) and confirm it matches the scene brief. Reject and re-scout on mismatch.
4. **Optimize + embed:** resize/compress to the **≤400KB/room** budget, base64-embed as a
   `data:` URI into the single-file build, replacing that scene's placeholder. Keep the
   authored SVG as fallback for any scene left unfilled. Credit line in the scene caption +
   footer.
5. **Gate + HITL:** run `preship-gate-v4.py` (SHIP required) and the Studio Eyes sweep;
   surface the result to the founder before ship. Human confirms the fidelity call — HITL is
   the hub.

## Guardrails (bounded autonomy)
- **Budget / loop-until-dry:** cap the sweep; stop after 2 rounds with nothing new; **log what
  was dropped** — no silent truncation.
- **No generated imagery** for anything a trainee reads (Registrar/Hand HALT). Firefly/MJ never
  enter a diagnostic scene.
- **RP floor holds:** the embedded photo is scene art behind the dark vignette; text tokens keep
  their arithmetic contrast. Alt text = the scene brief.
- **Provenance always:** every embedded image carries source + credit + as-of; decay-clock for
  re-verification.

## One honest rung (MVV)
Do NOT build the advance team. Run the scout on **one case's four scenes** (smoke first — the
NIST flashover lane is already located), embed the confirmed stills, gate, ship — and route the
"the read this image teaches" claim as one kernel through the full loop. Prove the loop turns,
*then* generalize the scout into the standing forward-agents crew (OS §6.4).
