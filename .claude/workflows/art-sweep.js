export const meta = {
  name: 'art-sweep',
  description: 'Art department fleet: gate the studio, direct, source, mount, audit, refute',
  whenToUse: 'When any page fails art-gate.py, when new plates land, or on founder request for an art pass. Args: {files: ["a.html", ...]} to scope, or omit for a full sweep.',
  phases: [
    { title: 'Gate', detail: 'art-gate.py names the offenders' },
    { title: 'Direct', detail: 'Art Director writes the shot list per file' },
    { title: 'Mount', detail: 'Compositor mounts available plates / flags MJ asks' },
    { title: 'Audit', detail: 'Continuity (Mad Men seat) + Refuter verify' },
  ],
}

// THE LAW (art-department/CHARTER.md): scene art is founder-MJ or license-verified
// legal photo. Hand-authored SVG scene art never ships. art-gate.py is the check.

let A = args
if (typeof A === 'string') { try { A = JSON.parse(A) } catch (e) { A = null } }

phase('Gate')
const gateOut = await agent(
  `Run: cd /tmp/tsp && python3 art-gate.py ${A && A.files ? A.files.join(' ') : '--all'} ; return the full output verbatim as your final text, plus (second line block) the bare list of HALTing files, one per line. No git commands.`,
  { label: 'art-gate', effort: 'low' })
const files = [...new Set((gateOut.match(/^HALT\s+(\S+)/gm) || []).map(l => l.split(/\s+/)[1]))]
log(`${files.length} files HALT art-gate`)
if (!files.length) return { clean: true, gate: gateOut }

const SHOT = { type:'object', required:['file','shots'], properties:{ file:{type:'string'},
  shots:{type:'array', items:{type:'object', required:['screen','need','lane'], properties:{
    screen:{type:'string'}, need:{type:'string', description:'what the image must show, Mad Men period detail'},
    lane:{type:'string', enum:['existing-plate','mj-prompt','legal-photo']},
    detail:{type:'string', description:'the MJ prompt, the plate path, or the photo-search brief with license target'} }}}}}

const RESULT = { type:'object', required:['file','mounted','summary'], properties:{
  file:{type:'string'}, mounted:{type:'boolean'},
  summary:{type:'string'}, asks:{type:'string', description:'MJ prompts or photo briefs needing the founder'},
  gates:{type:'string'} }}

phase('Direct')
const results = await pipeline(files,
  f => agent(
`ART DIRECTOR, Tight Spiral Studios. Read /tmp/tsp/art-department/CHARTER.md then /tmp/tsp/${f} fully. The file HALTs art-gate (hand-authored SVG scene art). Write the shot list: for each offending scene, what should the screen show (Mad Men set-decoration detail — every object period-correct), and which lane fills it: an existing plate in /tmp/tsp/art/cyl/plates or elsewhere in the repo, an MJ prompt for the founder, or a legal-photo brief (LOC/NARA/Wikimedia, license target). Prefer existing plates. No file edits, no git.`,
    { label:`direct:${f}`, phase:'Direct', schema: SHOT }),
  (shots, f) => agent(
`COMPOSITOR + CONTINUITY, Tight Spiral Studios. Read /tmp/tsp/art-department/CHARTER.md. File: /tmp/tsp/${f}. Shot list: ${JSON.stringify(shots)}.
Mount every shot whose lane is existing-plate: replace the hand-drawn SVG with the plate (base64 embed, aspect-locked, provenance data-art attribute per art-doctrine.md, text on solid panels never raw over photos). Shots needing MJ or legal photos: leave the existing art in place but add an HTML comment ART-ASK at the site, and collect the asks. Keep mechanics untouched, single-file offline, no emoji.
Then REFUTE yourself: python3 /tmp/tsp/comfort-gate.py ${f} must pass; python3 /tmp/tsp/art-gate.py ${f} must pass OR halt only on sites you left as ART-ASK; headless Playwright load with zero pageerrors and the core loop intact; screenshot and LOOK at every changed screen. Iterate until true. No git commands.`,
    { label:`mount:${f}`, phase:'Mount', schema: RESULT })
)

phase('Audit')
const summary = results.filter(Boolean)
return {
  gated: files,
  mounted: summary.filter(r => r.mounted).map(r => r.file),
  asks: summary.flatMap(r => r.asks ? [{ file: r.file, asks: r.asks }] : []),
  detail: summary,
}
