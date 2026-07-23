/* ============================================================================
   Confluence — domain data
   ----------------------------------------------------------------------------
   "Calibration assessment" here is the academic-assessment sense: faculty score
   the same samples of student work against a shared rubric, then compare scores
   to build inter-rater reliability before program-level assessment begins.

   This module is intentionally a static, in-memory model so the hub can be
   reviewed as a self-contained static site with no backend.
   ========================================================================== */

export const ROLES = {
  coordinator: {
    id: "coordinator",
    label: "Assessment Coordinator",
    blurb: "Designs sessions, manages rubrics, and monitors reliability across programs.",
    // Personas are positions, not real individuals. `sample: true` surfaces a
    // "Sample account" marker in the UI so no placeholder is mistaken for a
    // real person. Swap in an actual roster when one is provided.
    person: { initials: "AC", sample: true },
  },
  rater: {
    id: "rater",
    label: "Faculty Rater",
    blurb: "Scores assigned artifacts and calibrates against the group consensus.",
    person: { initials: "FR", sample: true },
  },
  lead: {
    id: "lead",
    label: "Program Lead",
    blurb: "Reviews outcomes and reliability for their program and approves rubrics.",
    person: { initials: "PL", sample: true },
  },
  reviewer: {
    id: "reviewer",
    label: "Accreditation Reviewer",
    blurb: "Read-only access to published calibration reports and outcome evidence.",
    person: { initials: "AR", sample: true },
  },
};

export const PROGRAMS = [
  { id: "nurs", name: "Nursing", outcome: "Clinical Reasoning" },
  { id: "engl", name: "English Composition", outcome: "Written Communication" },
  { id: "biot", name: "Biotechnology", outcome: "Lab Documentation" },
  { id: "busn", name: "Business", outcome: "Quantitative Analysis" },
];

export const RUBRICS = [
  {
    id: "rb-writ",
    title: "Written Communication (AAC&U VALUE)",
    program: "engl",
    version: "2.1",
    status: "Approved",
    criteria: [
      {
        name: "Context & Purpose",
        levels: [
          { label: "Benchmark", text: "Minimal attention to context, audience, and purpose." },
          { label: "Milestone 2", text: "Awareness of context and audience is developing." },
          { label: "Milestone 3", text: "Adequate consideration of context and audience." },
          { label: "Capstone", text: "Thorough, responsive attention to context and purpose." },
        ],
      },
      {
        name: "Content Development",
        levels: [
          { label: "Benchmark", text: "Uses appropriate content at a basic level." },
          { label: "Milestone 2", text: "Uses content to develop simple ideas." },
          { label: "Milestone 3", text: "Uses content to explore ideas within the work." },
          { label: "Capstone", text: "Uses compelling content to master the subject." },
        ],
      },
      {
        name: "Sources & Evidence",
        levels: [
          { label: "Benchmark", text: "Attempts to use sources to support ideas." },
          { label: "Milestone 2", text: "Uses relevant sources with some credibility." },
          { label: "Milestone 3", text: "Uses credible, relevant sources appropriately." },
          { label: "Capstone", text: "Skillfully integrates high-quality, credible sources." },
        ],
      },
    ],
  },
  {
    id: "rb-clin",
    title: "Clinical Reasoning Scorecard",
    program: "nurs",
    version: "3.0",
    status: "Approved",
    criteria: [
      {
        name: "Assessment",
        levels: [
          { label: "Novice", text: "Collects incomplete patient data." },
          { label: "Advanced Beginner", text: "Collects data with prompting." },
          { label: "Competent", text: "Collects relevant data independently." },
          { label: "Proficient", text: "Anticipates and prioritizes relevant data." },
        ],
      },
      {
        name: "Clinical Judgement",
        levels: [
          { label: "Novice", text: "Draws conclusions unsupported by data." },
          { label: "Advanced Beginner", text: "Links some data to conclusions." },
          { label: "Competent", text: "Draws sound conclusions from data." },
          { label: "Proficient", text: "Integrates data into nuanced judgement." },
        ],
      },
    ],
  },
  {
    id: "rb-lab",
    title: "Lab Documentation Rubric",
    program: "biot",
    version: "1.4",
    status: "Draft",
    criteria: [
      {
        name: "Reproducibility",
        levels: [
          { label: "Emerging", text: "Procedure cannot be reproduced from notes." },
          { label: "Developing", text: "Procedure partially reproducible." },
          { label: "Proficient", text: "Procedure reproducible with minor gaps." },
          { label: "Exemplary", text: "Procedure fully reproducible and precise." },
        ],
      },
    ],
  },
];

/* Calibration sessions.
   agreement = exact-match rate across raters (0–1); a proxy for reliability. */
export const SESSIONS = [
  {
    id: "cs-2041",
    title: "Fall Norming — Written Communication",
    program: "engl",
    rubricId: "rb-writ",
    status: "Open",
    dueDate: "2026-07-24",
    artifacts: 8,
    raters: ["r1", "r2", "r3", "r4", "r5"],
    ratersDone: 3,
    agreement: 0.78,
    myProgress: 0.5, // for the rater view
  },
  {
    id: "cs-2039",
    title: "Clinical Reasoning Calibration — Cohort B",
    program: "nurs",
    rubricId: "rb-clin",
    status: "Open",
    dueDate: "2026-07-21",
    artifacts: 6,
    raters: ["r1", "r3", "r6", "r7"],
    ratersDone: 2,
    agreement: 0.64,
    myProgress: 0.0,
  },
  {
    id: "cs-2035",
    title: "Lab Documentation Pilot",
    program: "biot",
    rubricId: "rb-lab",
    status: "Draft",
    dueDate: "2026-08-05",
    artifacts: 4,
    raters: ["r2", "r6"],
    ratersDone: 0,
    agreement: null,
    myProgress: null, // not assigned to current rater
  },
  {
    id: "cs-2028",
    title: "Spring Norming — Written Communication",
    program: "engl",
    rubricId: "rb-writ",
    status: "Published",
    dueDate: "2026-05-30",
    artifacts: 10,
    raters: ["r1", "r2", "r3", "r4", "r5", "r8"],
    ratersDone: 6,
    agreement: 0.91,
    myProgress: 1.0,
  },
  {
    id: "cs-2019",
    title: "Quantitative Analysis Calibration",
    program: "busn",
    rubricId: "rb-writ",
    status: "Closed",
    dueDate: "2026-04-18",
    artifacts: 6,
    raters: ["r3", "r5", "r7"],
    ratersDone: 3,
    agreement: 0.83,
    myProgress: null,
  },
];

/* Sample roster — placeholder rater labels, not real people. Replace with an
   actual roster (real names/titles) when available. */
export const RATERS = {
  r1: { name: "Rater A", dept: "English", agreement: 0.86, artifacts: 22 },
  r2: { name: "Rater B", dept: "English", agreement: 0.79, artifacts: 18 },
  r3: { name: "Rater C", dept: "Nursing", agreement: 0.71, artifacts: 26 },
  r4: { name: "Rater D", dept: "English", agreement: 0.9, artifacts: 15 },
  r5: { name: "Rater E", dept: "Business", agreement: 0.88, artifacts: 20 },
  r6: { name: "Rater F", dept: "Biotech", agreement: 0.62, artifacts: 9 },
  r7: { name: "Rater G", dept: "Nursing", agreement: 0.75, artifacts: 14 },
  r8: { name: "Rater H", dept: "English", agreement: 0.84, artifacts: 11 },
};

/* Artifacts inside the open Written-Communication session, for the rater flow. */
export const ARTIFACTS = {
  "cs-2041": [
    { id: "a1", label: "Sample 01 — Argumentative Essay", scored: true, myScore: 3, consensus: 3 },
    { id: "a2", label: "Sample 02 — Reflective Memo", scored: true, myScore: 2, consensus: 3 },
    { id: "a3", label: "Sample 03 — Research Brief", scored: true, myScore: 4, consensus: 4 },
    { id: "a4", label: "Sample 04 — Lab Report", scored: true, myScore: 3, consensus: 2 },
    { id: "a5", label: "Sample 05 — Op-Ed", scored: false, myScore: null, consensus: 3 },
    { id: "a6", label: "Sample 06 — Case Analysis", scored: false, myScore: null, consensus: 4 },
    { id: "a7", label: "Sample 07 — Literature Review", scored: false, myScore: null, consensus: 3 },
    { id: "a8", label: "Sample 08 — Proposal", scored: false, myScore: null, consensus: 2 },
  ],
};

export const ACTIVITY = [
  { who: "Rater D", what: "submitted 8 scores in", target: "Fall Norming — Written Communication", when: "12m ago", role: "rater" },
  { who: "You", what: "opened session", target: "Clinical Reasoning Calibration — Cohort B", when: "1h ago", role: "coordinator" },
  { who: "Program Lead", what: "approved rubric", target: "Clinical Reasoning Scorecard v3.0", when: "3h ago", role: "lead" },
  { who: "Rater C", what: "flagged a discrepancy in", target: "Sample 04 — Lab Report", when: "yesterday", role: "rater" },
  { who: "System", what: "published report for", target: "Spring Norming — Written Communication", when: "2 days ago", role: "coordinator" },
];

/* ---- helpers ---- */
export const programName = (id) => (PROGRAMS.find((p) => p.id === id) || {}).name || id;
export const rubricById = (id) => RUBRICS.find((r) => r.id === id);
export const sessionById = (id) => SESSIONS.find((s) => s.id === id);

export function statusBadge(status) {
  const map = {
    Open: "badge--info",
    Draft: "badge--warn",
    Published: "badge--ok",
    Closed: "badge",
    Approved: "badge--ok",
  };
  return map[status] || "badge";
}

export function agreementClass(a) {
  if (a == null) return "badge";
  if (a >= 0.85) return "badge--ok";
  if (a >= 0.7) return "badge--warn";
  return "badge--risk";
}
export function agreementColor(a) {
  if (a == null) return "var(--ink-400)";
  if (a >= 0.85) return "var(--ok)";
  if (a >= 0.7) return "var(--warn)";
  return "var(--risk)";
}
