/* ============================================================================
   Confluence — application core
   ----------------------------------------------------------------------------
   A dependency-free SPA. Everything the task asks for lives here:

   • Role-adaptive UX  — nav, dashboards, actions and access all keyed off the
                         signed-in role. Switching role re-shapes the whole app.
   • Home / Back       — persistent controls in the top bar; Back uses real
                         history, Home is a guaranteed anchor for every role.
   • Breadcrumbs       — derived from the active route, with human labels
                         resolved from the data model.
   • Design elegance   — a single cohesive design system (see styles.css) with
                         consistent components, motion, and light/dark support.
   ========================================================================== */

import { icon } from "./icons.js";
import {
  ROLES, PROGRAMS, RUBRICS, SESSIONS, RATERS, ARTIFACTS, ACTIVITY,
  programName, rubricById, sessionById, statusBadge, agreementClass, agreementColor,
} from "./data.js";

/* ----------------------------------------------------------------------------
   State
   ---------------------------------------------------------------------------- */
const store = {
  get role() { return localStorage.getItem("cf.role") || "coordinator"; },
  set role(v) { localStorage.setItem("cf.role", v); },
};

/* ----------------------------------------------------------------------------
   Navigation model — the single source of truth for what each role can reach.
   `roles` gates both the sidebar item AND direct-URL access.
   ---------------------------------------------------------------------------- */
const NAV = [
  { id: "home",      path: "/",          label: "Home",       icon: "home",      roles: ["coordinator", "rater", "lead", "reviewer"] },
  { id: "sessions",  path: "/sessions",  label: "Sessions",   icon: "sessions",  roles: ["coordinator", "rater", "lead"], labelFor: { rater: "My Sessions" } },
  { id: "rubrics",   path: "/rubrics",   label: "Rubrics",    icon: "rubric",    roles: ["coordinator", "rater", "lead", "reviewer"] },
  { id: "raters",    path: "/raters",    label: "Raters",     icon: "raters",    roles: ["coordinator", "lead"] },
  { id: "analytics", path: "/analytics", label: "Reliability",icon: "analytics", roles: ["coordinator", "lead"] },
  { id: "reports",   path: "/reports",   label: "Reports",    icon: "report",    roles: ["coordinator", "lead", "reviewer"] },
  { id: "settings",  path: "/settings",  label: "Settings",   icon: "settings",  roles: ["coordinator"] },
];

/* A route's access is inherited from its section's NAV entry. */
const SECTION_OF = {
  "": "home",
  sessions: "sessions",
  rubrics: "rubrics",
  raters: "raters",
  analytics: "analytics",
  reports: "reports",
  settings: "settings",
};

function canAccess(section, role) {
  const nav = NAV.find((n) => n.id === (SECTION_OF[section] ?? section));
  return nav ? nav.roles.includes(role) : false;
}

/* ----------------------------------------------------------------------------
   Router — hash based so the site works from the file system with no server.
   ---------------------------------------------------------------------------- */
function parseRoute() {
  const raw = (location.hash || "#/").replace(/^#/, "");
  const parts = raw.split("/").filter(Boolean); // ["sessions","cs-2041","score","a5"]
  return { parts, section: parts[0] || "", path: "/" + parts.join("/") };
}

const go = (path) => { location.hash = path; };

/* ----------------------------------------------------------------------------
   Breadcrumb resolution — maps route parts to readable trail entries.
   ---------------------------------------------------------------------------- */
function buildCrumbs(route) {
  const crumbs = [{ label: "Home", path: "/" }];
  const [section, id, sub, subId] = route.parts;
  if (!section) return crumbs;

  const nav = NAV.find((n) => n.id === SECTION_OF[section]);
  const sectionLabel = nav ? navLabel(nav) : cap(section);
  crumbs.push({ label: sectionLabel, path: "/" + section });

  if (section === "sessions" && id) {
    const s = sessionById(id);
    crumbs.push({ label: s ? s.title : id, path: `/sessions/${id}` });
    if (sub === "score") {
      const art = (ARTIFACTS[id] || []).find((a) => a.id === subId);
      crumbs.push({ label: art ? art.label : "Score", path: null });
    }
  } else if (section === "rubrics" && id) {
    const r = rubricById(id);
    crumbs.push({ label: r ? r.title : id, path: null });
  }
  // Last crumb is never a link.
  if (crumbs.length) crumbs[crumbs.length - 1].path = null;
  return crumbs;
}

const navLabel = (nav) => (nav.labelFor && nav.labelFor[store.role]) || nav.label;
const cap = (s) => s.charAt(0).toUpperCase() + s.slice(1);

/* ----------------------------------------------------------------------------
   Small view helpers
   ---------------------------------------------------------------------------- */
const pct = (n) => Math.round(n * 100);
const meter = (a) =>
  `<span class="meter"><span class="meter__bar"><i style="width:${a == null ? 0 : pct(a)}%;background:${agreementColor(a)}"></i></span><span class="meter__val" style="color:${agreementColor(a)}">${a == null ? "—" : pct(a) + "%"}</span></span>`;

function sparkline(values, color = "var(--brand-500)") {
  const w = 120, h = 34, max = Math.max(...values), min = Math.min(...values);
  const span = max - min || 1;
  const pts = values.map((v, i) => {
    const x = (i / (values.length - 1)) * w;
    const y = h - ((v - min) / span) * (h - 6) - 3;
    return `${x.toFixed(1)},${y.toFixed(1)}`;
  });
  return `<svg class="stat__spark" viewBox="0 0 ${w} ${h}" width="${w}" height="${h}" preserveAspectRatio="none">
    <polyline points="${pts.join(" ")}" fill="none" stroke="${color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>`;
}

const badge = (label, cls) => `<span class="badge ${cls}"><span class="dot"></span>${label}</span>`;

/* ============================================================================
   VIEWS
   ========================================================================== */

/* ---- Home: fully role-adaptive ------------------------------------------- */
function viewHome() {
  const role = store.role;
  const who = ROLES[role];
  // Greet by role, not a fabricated name. The eyebrow already names the role.
  const greeting = `Good ${dayPart()}`;

  const head = `
    <div class="page-head">
      <div class="page-head__eyebrow">${who.label}${who.person.sample ? " · Sample view" : ""}</div>
      <h1>${greeting}</h1>
      <p class="page-head__sub">${homeIntro(role)}</p>
    </div>`;

  return head + ({
    coordinator: homeCoordinator,
    rater: homeRater,
    lead: homeLead,
    reviewer: homeReviewer,
  }[role])();
}

function homeIntro(role) {
  return {
    coordinator: "Three calibration sessions are active. Two programs are below the 85% agreement threshold and may need a norming discussion.",
    rater: "You have one session in progress and one waiting to start. Finish scoring to see how your judgements line up with the group.",
    lead: "Reliability for your program is trending up. One rubric is awaiting your approval before the next session opens.",
    reviewer: "Published calibration reports and outcome evidence are available for review below.",
  }[role];
}

function statTile(label, value, delta, spark) {
  return `<div class="card stat">
    <div class="stat__label">${label}</div>
    <div class="stat__value">${value}</div>
    ${delta ? `<div class="stat__delta ${delta.dir}">${delta.dir === "down" ? icon.arrowDown() : icon.arrowUp()}${delta.text}</div>` : ""}
    ${spark || ""}
  </div>`;
}

function homeCoordinator() {
  const open = SESSIONS.filter((s) => s.status === "Open");
  const stats = `<div class="grid grid--stats">
    ${statTile("Active sessions", open.length, { dir: "up", text: "1 opened this week" }, sparkline([2, 3, 2, 3, 4, 3, 3]))}
    ${statTile("Median agreement", "78%", { dir: "down", text: "4 pts vs. last cycle" }, sparkline([84, 82, 80, 79, 77, 78, 78], "var(--warn)"))}
    ${statTile("Raters engaged", "8", { dir: "up", text: "94% response rate" }, sparkline([5, 6, 6, 7, 7, 8, 8]))}
    ${statTile("Artifacts scored", "126", { dir: "up", text: "38 this week" }, sparkline([60, 72, 80, 95, 108, 118, 126]))}
  </div>`;

  const attention = open
    .filter((s) => s.agreement != null && s.agreement < 0.85)
    .map(
      (s) => `<div class="callout" style="margin-bottom:12px">
        ${icon.info()}
        <div><div class="callout__t">${s.title} is at ${pct(s.agreement)}% agreement</div>
        <div class="callout__d">Below the 85% reliability threshold. Consider a norming discussion before closing. ${linkBtn("Open session", `/sessions/${s.id}`)}</div></div>
      </div>`
    ).join("");

  return `${stats}
    <div class="section-head"><h2>Needs your attention</h2></div>
    ${attention || emptyInline("All sessions are on track.")}
    <div class="grid grid--two" style="margin-top:24px">
      <div>
        <div class="section-head"><h2>Active sessions</h2>${sectionLink("All sessions", "/sessions")}</div>
        ${sessionTable(open)}
      </div>
      <div>
        <div class="section-head"><h2>Recent activity</h2></div>
        ${activityCard()}
      </div>
    </div>`;
}

function homeRater() {
  const mine = SESSIONS.filter((s) => s.myProgress != null && s.status !== "Published" && s.status !== "Closed");
  const done = ARTIFACTS["cs-2041"].filter((a) => a.scored).length;
  const total = ARTIFACTS["cs-2041"].length;

  const cards = mine.map((s) => `
    <div class="card tile" data-nav="/sessions/${s.id}">
      <div class="tile__top">
        <div><div class="tile__title">${s.title}</div>
        <div class="tile__meta">${programName(s.program)} · due ${fmtDate(s.dueDate)}</div></div>
        ${badge(s.status, statusBadge(s.status))}
      </div>
      <div>
        <div class="util-row" style="justify-content:space-between;margin-bottom:6px">
          <span class="muted" style="font-size:13px">Your progress</span>
          <span style="font-weight:650;font-size:13px">${s.myProgress != null ? pct(s.myProgress) + "%" : "Not started"}</span>
        </div>
        <div class="progress"><i style="width:${pct(s.myProgress || 0)}%"></i></div>
      </div>
      <div class="tile__foot">
        <span class="muted" style="font-size:13px">${s.artifacts} artifacts</span>
        <span class="btn btn--primary">${s.myProgress ? "Continue scoring" : "Start"} ${icon.arrowRight()}</span>
      </div>
    </div>`).join("");

  return `
    <div class="grid grid--stats" style="margin-bottom:8px">
      ${statTile("Assigned to you", mine.length, null)}
      ${statTile("Your agreement", "86%", { dir: "up", text: "Above the 85% target" })}
      ${statTile("This session", `${done}/${total}`, null, `<div class="progress progress--thin" style="margin-top:12px"><i style="width:${pct(done/total)}%"></i></div>`)}
    </div>
    <div class="section-head"><h2>Continue where you left off</h2></div>
    <div class="grid grid--cards">${cards}</div>
    <div class="callout" style="margin-top:24px">${icon.target()}
      <div><div class="callout__t">Why calibration matters</div>
      <div class="callout__d">Scoring these shared samples first lets us measure how consistently the team applies the rubric — so program results reflect student learning, not who did the grading.</div></div>
    </div>`;
}

function homeLead() {
  const prog = PROGRAMS[1]; // English for this persona
  const progSessions = SESSIONS.filter((s) => s.program === prog.id);
  const pending = RUBRICS.filter((r) => r.status === "Draft");

  return `
    <div class="grid grid--stats">
      ${statTile(`${prog.name} agreement`, "84%", { dir: "up", text: "7 pts this cycle" }, sparkline([74, 76, 78, 80, 82, 83, 84]))}
      ${statTile("Sessions this year", progSessions.length, null)}
      ${statTile("Rubrics to approve", pending.length, pending.length ? { dir: "up", text: "Action needed" } : null)}
    </div>
    ${pending.length ? `<div class="section-head"><h2>Awaiting your approval</h2></div>
      ${pending.map((r) => `<div class="callout" style="margin-bottom:12px">${icon.rubric()}
        <div><div class="callout__t">${r.title} · v${r.version}</div>
        <div class="callout__d">Submitted for the next calibration cycle. ${linkBtn("Review rubric", `/rubrics/${r.id}`)}</div></div></div>`).join("")}` : ""}
    <div class="grid grid--two" style="margin-top:24px">
      <div>
        <div class="section-head"><h2>${prog.name} sessions</h2>${sectionLink("Reliability", "/analytics")}</div>
        ${sessionTable(progSessions)}
      </div>
      <div>
        <div class="section-head"><h2>Program outcome</h2></div>
        <div class="card card--pad">
          <div class="tile__ico">${icon.target()}</div>
          <h3 style="margin:12px 0 4px">${prog.outcome}</h3>
          <p class="muted" style="font-size:13.5px">Assessed through calibrated scoring of authentic student work. Current inter-rater agreement supports valid program-level reporting.</p>
          <div class="kv" style="margin-top:16px">
            <div class="kv__row"><span class="kv__k">Reliability</span><span class="kv__v">${meter(0.84)}</span></div>
            <div class="kv__row"><span class="kv__k">Evidence artifacts</span><span class="kv__v">28</span></div>
            <div class="kv__row"><span class="kv__k">Status</span><span class="kv__v">${badge("On track", "badge--ok")}</span></div>
          </div>
        </div>
      </div>
    </div>`;
}

function homeReviewer() {
  const published = SESSIONS.filter((s) => s.status === "Published" || s.status === "Closed");
  return `
    <div class="callout" style="margin-bottom:24px">${icon.lock()}
      <div><div class="callout__t">Read-only access</div>
      <div class="callout__d">You can view published calibration reports and outcome evidence. Scoring and session management are handled by faculty and coordinators.</div></div>
    </div>
    <div class="section-head"><h2>Published reports</h2>${sectionLink("All reports", "/reports")}</div>
    <div class="grid grid--cards">
      ${published.map((s) => `<div class="card tile" data-nav="/sessions/${s.id}">
        <div class="tile__top"><div class="tile__ico">${icon.report()}</div>${badge(s.status, statusBadge(s.status))}</div>
        <div class="tile__title">${s.title}</div>
        <div class="tile__meta">${programName(s.program)} · ${s.artifacts} artifacts · closed ${fmtDate(s.dueDate)}</div>
        <div class="tile__foot"><span>${meter(s.agreement)}</span><span class="btn btn--ghost">View ${icon.arrowRight()}</span></div>
      </div>`).join("")}
    </div>`;
}

/* ---- Sessions list ------------------------------------------------------- */
function viewSessions() {
  const role = store.role;
  let list = SESSIONS.slice();
  let intro = "Every calibration session across all programs.";
  if (role === "rater") {
    list = list.filter((s) => s.myProgress != null);
    intro = "Sessions you have been assigned to as a rater.";
  } else if (role === "lead") {
    list = list.filter((s) => s.program === "engl");
    intro = "Calibration sessions for the English Composition program.";
  }

  const canCreate = role === "coordinator";
  return `
    <div class="page-head"><div class="page-head__row">
      <div><div class="page-head__eyebrow">Calibration</div><h1>${role === "rater" ? "My Sessions" : "Sessions"}</h1>
      <p class="page-head__sub">${intro}</p></div>
      ${canCreate ? `<button class="btn btn--primary" data-toast="Session drafts open the setup wizard.">${icon.plus()} New session</button>` : ""}
    </div></div>
    <div class="toolbar"><div class="chips">
      <button class="chip is-active">All</button><button class="chip">Open</button><button class="chip">Published</button>
    </div></div>
    ${list.length ? sessionTable(list, true) : emptyInline("No sessions assigned to you yet.")}`;
}

function sessionTable(list, showProgram = true) {
  const role = store.role;
  const rows = list.map((s) => `
    <tr class="clickable" data-nav="/sessions/${s.id}">
      <td><div class="cell-strong">${s.title}</div><div class="cell-sub">${s.artifacts} artifacts · ${s.raters.length} raters</div></td>
      ${showProgram ? `<td>${programName(s.program)}</td>` : ""}
      <td>${badge(s.status, statusBadge(s.status))}</td>
      ${role === "rater"
        ? `<td>${s.myProgress != null ? `<div class="progress progress--thin" style="width:90px"><i style="width:${pct(s.myProgress)}%"></i></div>` : '<span class="muted">—</span>'}</td>`
        : `<td>${meter(s.agreement)}</td>`}
      <td class="nowrap muted">${fmtDate(s.dueDate)}</td>
    </tr>`).join("");
  return `<div class="table-wrap"><table class="data"><thead><tr>
    <th>Session</th>${showProgram ? "<th>Program</th>" : ""}<th>Status</th>
    <th>${role === "rater" ? "Your progress" : "Agreement"}</th><th>Due</th>
  </tr></thead><tbody>${rows}</tbody></table></div>`;
}

/* ---- Session detail ------------------------------------------------------ */
function viewSessionDetail(id) {
  const s = sessionById(id);
  if (!s) return notFound("session");
  const role = store.role;
  const rubric = rubricById(s.rubricId);
  const arts = ARTIFACTS[id];

  const raterList = s.raters.map((rid) => {
    const r = RATERS[rid];
    return `<div class="kv__row"><span class="kv__k">${r.name}<div class="cell-sub">${r.dept}</div></span><span class="kv__v">${meter(r.agreement)}</span></div>`;
  }).join("");

  const scoreCta = role === "rater" && s.myProgress != null
    ? `<button class="btn btn--primary" data-nav="/sessions/${id}/score/${(arts?.find(a=>!a.scored)||arts?.[0])?.id || "a1"}">${icon.score()} ${s.myProgress ? "Continue scoring" : "Start scoring"}</button>`
    : "";

  const artifactPanel = role === "rater" && arts ? `
    <div class="section-head"><h2>Artifacts</h2><span class="muted">${arts.filter(a=>a.scored).length}/${arts.length} scored</span></div>
    <div class="card"><div style="padding:6px">
      ${arts.map((a) => `<div class="kv__row" style="padding:12px 16px;align-items:center">
        <span class="util-row" style="gap:12px">
          <span class="tile__ico" style="width:32px;height:32px;background:${a.scored?'var(--ok-bg)':'var(--surface-3)'};color:${a.scored?'var(--ok)':'var(--ink-400)'}">${a.scored?icon.check():icon.score()}</span>
          <span><span class="cell-strong">${a.label}</span>${a.scored?`<div class="cell-sub">You scored ${a.myScore} · consensus ${a.consensus}${a.myScore!==a.consensus?' · <span style="color:var(--warn)">review</span>':''}</div>`:'<div class="cell-sub">Not scored</div>'}</span>
        </span>
        <button class="btn ${a.scored?'btn--ghost':'btn--primary'}" data-nav="/sessions/${id}/score/${a.id}">${a.scored?'Revisit':'Score'}</button>
      </div>`).join("")}
    </div></div>` : "";

  const reliabilityPanel = role !== "rater" ? `
    <div class="section-head"><h2>Reliability</h2></div>
    <div class="card card--pad">
      <div class="util-row" style="justify-content:space-between;margin-bottom:6px">
        <span class="muted">Exact-match agreement</span><span style="font-weight:700;font-size:20px;color:${agreementColor(s.agreement)}">${s.agreement==null?"—":pct(s.agreement)+"%"}</span>
      </div>
      <div class="progress"><i style="width:${s.agreement==null?0:pct(s.agreement)}%;background:${agreementColor(s.agreement)}"></i></div>
      <p class="muted" style="font-size:13px;margin-top:12px">${s.agreement==null?"No scores submitted yet.":s.agreement>=0.85?"Above the reliability threshold — results are ready to publish.":"Below the 85% threshold. A norming discussion is recommended."}</p>
      <div class="kv" style="margin-top:8px">
        <div class="kv__row"><span class="kv__k">Raters completed</span><span class="kv__v">${s.ratersDone}/${s.raters.length}</span></div>
        <div class="kv__row"><span class="kv__k">Artifacts</span><span class="kv__v">${s.artifacts}</span></div>
      </div>
    </div>` : "";

  const adminActions = role === "coordinator" ? `
    <div class="util-row" style="gap:8px;margin-top:16px">
      ${s.status==="Open"?`<button class="btn btn--primary" data-toast="Session closed. Report generated.">${icon.check()} Close & publish</button>`:""}
      <button class="btn btn--ghost" data-toast="Reminder sent to 2 pending raters.">Send reminders</button>
    </div>` : "";

  return `
    <div class="page-head"><div class="page-head__row">
      <div><div class="page-head__eyebrow">${programName(s.program)} · ${badgeInline(s.status)}</div>
      <h1>${s.title}</h1><p class="page-head__sub">Rubric: ${rubric ? rubric.title : "—"} · Due ${fmtDate(s.dueDate)}</p></div>
      ${scoreCta}
    </div></div>
    <div class="detail-grid">
      <div>
        ${artifactPanel}
        ${reliabilityPanel}
        ${role !== "rater" ? `<div class="section-head"><h2>Raters</h2></div><div class="card card--pad"><div class="kv">${raterList}</div></div>` : ""}
        ${adminActions}
      </div>
      <div>
        <div class="card card--pad">
          <h3 style="font-size:15px;margin-bottom:12px">Overview</h3>
          <div class="kv">
            <div class="kv__row"><span class="kv__k">Program</span><span class="kv__v">${programName(s.program)}</span></div>
            <div class="kv__row"><span class="kv__k">Status</span><span class="kv__v">${badge(s.status, statusBadge(s.status))}</span></div>
            <div class="kv__row"><span class="kv__k">Rubric</span><span class="kv__v">${linkBtn(rubric?rubric.title:"—", rubric?`/rubrics/${rubric.id}`:null)}</span></div>
            <div class="kv__row"><span class="kv__k">Due</span><span class="kv__v">${fmtDate(s.dueDate)}</span></div>
          </div>
        </div>
        ${role === "coordinator" ? `<div class="card card--pad" style="margin-top:16px">
          <h3 style="font-size:15px;margin-bottom:12px">Session progress</h3>
          ${["Set up","Invite raters","Scoring","Norming","Publish"].map((st,i)=>{
            const cls = i < (s.status==="Published"?5:s.status==="Open"?2:1) ? "done" : i === (s.status==="Open"?2:1) ? "active" : "";
            return `<div class="step ${cls}"><div class="step__rail"><div class="step__dot">${cls==="done"?"✓":i+1}</div><div class="step__line"></div></div><div class="step__body"><div class="step__t">${st}</div></div></div>`;
          }).join("")}
        </div>` : ""}
      </div>
    </div>`;
}

/* ---- Scoring flow (rater) ------------------------------------------------ */
function viewScore(sessionId, artifactId) {
  const s = sessionById(sessionId);
  const arts = ARTIFACTS[sessionId] || [];
  const art = arts.find((a) => a.id === artifactId) || arts[0];
  if (!s || !art) return notFound("artifact");
  const rubric = rubricById(s.rubricId);
  const idx = arts.indexOf(art);
  const next = arts[idx + 1];

  const criteria = rubric.criteria.map((c, ci) => `
    <div class="card card--pad" style="margin-bottom:16px">
      <h3 style="font-size:15px;margin-bottom:4px">${c.name}</h3>
      <p class="muted" style="font-size:13px;margin-bottom:14px">Select the level that best describes this sample.</p>
      <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(150px,1fr))">
        ${c.levels.map((l, li) => `<button class="card score-opt" data-score="${ci}-${li}" style="padding:14px;text-align:left;border-radius:10px;cursor:pointer">
          <b style="font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:var(--brand-600)">${l.label}</b>
          <div style="font-size:13px;margin-top:6px;color:var(--ink-700)">${l.text}</div>
        </button>`).join("")}
      </div>
    </div>`).join("");

  return `
    <div class="page-head"><div class="page-head__row">
      <div><div class="page-head__eyebrow">Scoring · Artifact ${idx + 1} of ${arts.length}</div>
      <h1>${art.label}</h1><p class="page-head__sub">Scoring against ${rubric.title}. Your score stays private until the session is normed.</p></div>
      <div class="util-row"><button class="btn btn--ghost" data-nav="/sessions/${sessionId}">${icon.back()} Back to session</button></div>
    </div></div>
    <div class="detail-grid">
      <div>${criteria}
        <div class="util-row" style="justify-content:space-between;margin-top:8px">
          <button class="btn btn--ghost" data-nav="/sessions/${sessionId}">Save & exit</button>
          <button class="btn btn--primary" ${next?`data-nav="/sessions/${sessionId}/score/${next.id}"`:`data-nav="/sessions/${sessionId}"`} data-toast="Score recorded.">${next?"Save & next artifact":"Save & finish"} ${icon.arrowRight()}</button>
        </div>
      </div>
      <div>
        <div class="card card--pad" style="position:sticky;top:80px">
          <div class="tile__ico">${icon.score()}</div>
          <h3 style="margin:12px 0 6px;font-size:15px">The artifact</h3>
          <p class="muted" style="font-size:13px">In a live hub this panel shows the student work — document, media, or code — beside the rubric so you can score without losing context.</p>
          <div style="height:120px;border-radius:10px;background:var(--surface-2);border:1px dashed var(--line-strong);margin-top:12px;display:grid;place-items:center;color:var(--ink-400);font-size:13px">Sample preview</div>
          <div class="kv" style="margin-top:14px">
            <div class="kv__row"><span class="kv__k">Progress</span><span class="kv__v">${idx + 1}/${arts.length}</span></div>
            <div class="kv__row"><span class="kv__k">Rubric</span><span class="kv__v">${linkBtn(rubric.title, `/rubrics/${rubric.id}`)}</span></div>
          </div>
        </div>
      </div>
    </div>`;
}

/* ---- Rubrics ------------------------------------------------------------- */
function viewRubrics() {
  const role = store.role;
  const canEdit = role === "coordinator";
  return `
    <div class="page-head"><div class="page-head__row">
      <div><div class="page-head__eyebrow">Standards</div><h1>Rubrics</h1>
      <p class="page-head__sub">${role === "reviewer" ? "Rubrics used to score the published calibration reports." : "Shared scoring guides. Calibration measures how consistently raters apply them."}</p></div>
      ${canEdit ? `<button class="btn btn--primary" data-toast="Opens the rubric builder.">${icon.plus()} New rubric</button>` : ""}
    </div></div>
    <div class="grid grid--cards">
      ${RUBRICS.map((r) => `<div class="card tile" data-nav="/rubrics/${r.id}">
        <div class="tile__top"><div class="tile__ico">${icon.rubric()}</div>${badge(r.status, statusBadge(r.status))}</div>
        <div class="tile__title">${r.title}</div>
        <div class="tile__meta">${programName(r.program)} · v${r.version} · ${r.criteria.length} criteria</div>
        <div class="tile__foot"><span class="muted" style="font-size:13px">${r.criteria.length * 4} levels</span><span class="btn btn--ghost">Open ${icon.arrowRight()}</span></div>
      </div>`).join("")}
    </div>`;
}

function viewRubricDetail(id) {
  const r = rubricById(id);
  if (!r) return notFound("rubric");
  const role = store.role;
  const canApprove = role === "lead" && r.status === "Draft";
  const canEdit = role === "coordinator";

  return `
    <div class="page-head"><div class="page-head__row">
      <div><div class="page-head__eyebrow">${programName(r.program)} · v${r.version} · ${badgeInline(r.status)}</div><h1>${r.title}</h1></div>
      <div class="util-row">
        ${canApprove ? `<button class="btn btn--primary" data-toast="Rubric approved for the next cycle.">${icon.check()} Approve</button>` : ""}
        ${canEdit ? `<button class="btn btn--ghost" data-toast="Opens the rubric builder.">Edit</button>` : ""}
      </div>
    </div></div>
    ${r.criteria.map((c) => `<div class="criterion">
      <div class="criterion__head"><h3 style="font-size:15px">${c.name}</h3><span class="muted" style="font-size:13px">${c.levels.length} levels</span></div>
      <div class="criterion__levels">${c.levels.map((l) => `<div class="criterion__lvl"><b>${l.label}</b>${l.text}</div>`).join("")}</div>
    </div>`).join("")}`;
}

/* ---- Raters -------------------------------------------------------------- */
function viewRaters() {
  const rows = Object.entries(RATERS).map(([id, r]) => `
    <tr>
      <td><span class="util-row" style="gap:10px"><span class="avatar" style="width:30px;height:30px;font-size:11px">${initials(r.name)}</span><span class="cell-strong">${r.name}</span></span></td>
      <td>${r.dept}</td>
      <td>${meter(r.agreement)}</td>
      <td>${r.artifacts}</td>
      <td>${r.agreement >= 0.85 ? badge("Calibrated", "badge--ok") : r.agreement >= 0.7 ? badge("Developing", "badge--warn") : badge("Needs norming", "badge--risk")}</td>
    </tr>`).join("");
  return `
    <div class="page-head"><div class="page-head__eyebrow">People</div><h1>Raters</h1>
    <p class="page-head__sub">Inter-rater agreement across all sessions. Raters below 70% are flagged for a norming conversation.</p></div>
    <div class="table-wrap"><table class="data"><thead><tr>
      <th>Rater</th><th>Department</th><th>Agreement</th><th>Artifacts</th><th>Status</th>
    </tr></thead><tbody>${rows}</tbody></table></div>`;
}

/* ---- Reliability / analytics --------------------------------------------- */
function viewAnalytics() {
  const scored = SESSIONS.filter((s) => s.agreement != null);
  const avg = scored.reduce((a, s) => a + s.agreement, 0) / scored.length;
  const bars = scored.map((s) => `
    <div style="margin-bottom:16px">
      <div class="util-row" style="justify-content:space-between;margin-bottom:6px">
        <span style="font-size:13.5px;font-weight:600">${s.title}</span>
        <span style="font-weight:700;color:${agreementColor(s.agreement)}">${pct(s.agreement)}%</span>
      </div>
      <div class="progress"><i style="width:${pct(s.agreement)}%;background:${agreementColor(s.agreement)}"></i></div>
    </div>`).join("");

  return `
    <div class="page-head"><div class="page-head__eyebrow">Reliability</div><h1>Inter-rater reliability</h1>
    <p class="page-head__sub">How consistently raters agree, by session. Sustained agreement above 85% supports valid program-level assessment.</p></div>
    <div class="grid grid--stats" style="margin-bottom:24px">
      ${statTile("Average agreement", pct(avg) + "%", { dir: "up", text: "Across scored sessions" }, sparkline([83, 64, 91, 78, 84], "var(--brand-500)"))}
      ${statTile("Sessions above 85%", scored.filter((s) => s.agreement >= 0.85).length + "/" + scored.length, null)}
      ${statTile("Lowest session", pct(Math.min(...scored.map((s) => s.agreement))) + "%", { dir: "down", text: "Clinical Reasoning — Cohort B" })}
    </div>
    <div class="grid grid--two">
      <div class="card card--pad"><h3 style="font-size:16px;margin-bottom:18px">Agreement by session</h3>${bars}</div>
      <div class="card card--pad">
        <h3 style="font-size:16px;margin-bottom:12px">Reading the numbers</h3>
        <div class="kv">
          <div class="kv__row"><span class="kv__k">${badge("≥ 85%", "badge--ok")}</span><span class="kv__v" style="font-weight:500;color:var(--ink-500);font-size:13px;text-align:right">Publish-ready</span></div>
          <div class="kv__row"><span class="kv__k">${badge("70–84%", "badge--warn")}</span><span class="kv__v" style="font-weight:500;color:var(--ink-500);font-size:13px;text-align:right">Norming recommended</span></div>
          <div class="kv__row"><span class="kv__k">${badge("< 70%", "badge--risk")}</span><span class="kv__v" style="font-weight:500;color:var(--ink-500);font-size:13px;text-align:right">Re-calibrate before use</span></div>
        </div>
        <div class="callout" style="margin-top:16px">${icon.info()}<div><div class="callout__d">Agreement here is the exact-match rate between raters. Live deployments can swap in Cohen's κ or intraclass correlation.</div></div></div>
      </div>
    </div>`;
}

/* ---- Reports ------------------------------------------------------------- */
function viewReports() {
  const published = SESSIONS.filter((s) => s.status === "Published" || s.status === "Closed");
  const rows = published.map((s) => `
    <tr class="clickable" data-nav="/sessions/${s.id}">
      <td><div class="cell-strong">${s.title}</div><div class="cell-sub">${programName(s.program)}</div></td>
      <td>${badge(s.status, statusBadge(s.status))}</td>
      <td>${meter(s.agreement)}</td>
      <td>${s.artifacts}</td>
      <td class="nowrap muted">${fmtDate(s.dueDate)}</td>
    </tr>`).join("");
  return `
    <div class="page-head"><div class="page-head__eyebrow">Evidence</div><h1>Calibration reports</h1>
    <p class="page-head__sub">Finalized sessions with their reliability evidence — suitable for program review and accreditation.</p></div>
    <div class="table-wrap"><table class="data"><thead><tr>
      <th>Report</th><th>Status</th><th>Agreement</th><th>Artifacts</th><th>Finalized</th>
    </tr></thead><tbody>${rows}</tbody></table></div>`;
}

/* ---- Settings ------------------------------------------------------------ */
function viewSettings() {
  return `
    <div class="page-head"><div class="page-head__eyebrow">Administration</div><h1>Settings</h1>
    <p class="page-head__sub">Configure calibration thresholds and program defaults for the hub.</p></div>
    <div class="card card--pad" style="max-width:640px">
      <div class="kv">
        <div class="kv__row"><span class="kv__k">Reliability threshold<div class="cell-sub">Sessions below this are flagged</div></span><span class="kv__v">85%</span></div>
        <div class="kv__row"><span class="kv__k">Agreement metric</span><span class="kv__v">Exact match</span></div>
        <div class="kv__row"><span class="kv__k">Default scoring scale</span><span class="kv__v">4-level (VALUE)</span></div>
        <div class="kv__row"><span class="kv__k">Institution</span><span class="kv__v">MassBay Community College</span></div>
      </div>
      <div class="util-row" style="margin-top:16px"><button class="btn btn--primary" data-toast="Settings saved.">Save changes</button></div>
    </div>`;
}

/* ---- Shared partials ----------------------------------------------------- */
function activityCard() {
  return `<div class="card"><div style="padding:6px">
    ${ACTIVITY.map((a) => `<div class="kv__row" style="padding:12px 16px;align-items:flex-start;gap:12px">
      <span class="avatar" style="width:30px;height:30px;font-size:11px;flex:none">${initials(a.who)}</span>
      <span style="flex:1;font-size:13.5px"><b>${a.who}</b> ${a.what} <span style="color:var(--brand-600)">${a.target}</span><div class="cell-sub">${a.when}</div></span>
    </div>`).join("")}
  </div></div>`;
}

const emptyInline = (msg) => `<div class="empty"><div class="empty__ico">${icon.check()}</div><h3>Nothing here</h3><p>${msg}</p></div>`;
const sectionLink = (label, path) => `<a class="link" data-nav="${path}">${label} ${icon.arrowRight()}</a>`;
const linkBtn = (label, path) => path ? `<a class="link" data-nav="${path}" style="font-weight:600">${label}</a>` : `<span>${label}</span>`;
const badgeInline = (status) => `<span style="color:${agreementColor(1)};font-weight:600">${status}</span>`;

function notFound(kind) {
  return `<div class="empty"><div class="empty__ico">${icon.info()}</div><h3>This ${kind} isn't available</h3>
    <p>It may have been removed, or you don't have access to it in your current role.</p>
    <button class="btn btn--primary" data-nav="/" style="margin-top:16px">${icon.home()} Back to home</button></div>`;
}

function accessDenied(section) {
  const nav = NAV.find((n) => n.id === SECTION_OF[section]);
  const label = nav ? nav.label : cap(section);
  return `<div class="empty"><div class="empty__ico">${icon.lock()}</div>
    <h3>${label} isn't part of your role</h3>
    <p>You're signed in as <b>${ROLES[store.role].label}</b>, which doesn't include access to ${label.toLowerCase()}.<br>Switch roles from the sidebar, or head back home.</p>
    <button class="btn btn--primary" data-nav="/" style="margin-top:16px">${icon.home()} Back to home</button></div>`;
}

/* ============================================================================
   Render pipeline
   ========================================================================== */
function renderView(route) {
  const { parts, section } = route;
  if (!canAccess(section, store.role)) return accessDenied(section);

  switch (section) {
    case "": return viewHome();
    case "sessions":
      if (parts[2] === "score") return viewScore(parts[1], parts[3]);
      if (parts[1]) return viewSessionDetail(parts[1]);
      return viewSessions();
    case "rubrics":
      return parts[1] ? viewRubricDetail(parts[1]) : viewRubrics();
    case "raters": return viewRaters();
    case "analytics": return viewAnalytics();
    case "reports": return viewReports();
    case "settings": return viewSettings();
    default: return notFound("page");
  }
}

function renderSidebar(route) {
  const role = store.role;
  const items = NAV.filter((n) => n.roles.includes(role)).map((n) => {
    const isActive = n.id === "home" ? route.section === "" : SECTION_OF[route.section] === n.id;
    return `<button class="nav__item ${isActive ? "is-active" : ""}" data-nav="${n.path}">${icon[n.icon]()}<span>${navLabel(n)}</span></button>`;
  }).join("");

  const who = ROLES[role];
  const options = Object.values(ROLES).map((r) => `<option value="${r.id}" ${r.id === role ? "selected" : ""}>${r.label}</option>`).join("");

  return `
    <div class="brand">
      <div class="brand__mark">${icon.logo()}</div>
      <div><div class="brand__name">Confluence</div><div class="brand__tag">Calibration Hub</div></div>
    </div>
    <nav class="nav">
      <div class="nav__label">Workspace</div>
      ${items}
    </nav>
    <div class="sidebar__foot">
      <div class="role-card">
        <div class="role-card__row">
          <span class="avatar">${who.person.initials}</span>
          <div><div class="role-card__name">${who.label}</div><div class="role-card__role">${who.person.sample ? "Sample account · MassBay" : "MassBay"}</div></div>
        </div>
        <label class="cell-sub" style="display:block;margin-top:12px;margin-bottom:2px;font-size:11px;text-transform:uppercase;letter-spacing:.06em">View the hub as</label>
        <select class="role-select" id="roleSelect">${options}</select>
      </div>
    </div>`;
}

function renderTopbar(route) {
  const crumbs = buildCrumbs(route);
  const trail = crumbs.map((c, i) => {
    const last = i === crumbs.length - 1;
    const sep = i > 0 ? `<span class="sep">${icon.chevron()}</span>` : "";
    if (last || !c.path) return `${sep}<span class="current">${c.label}</span>`;
    return `${sep}<a data-nav="${c.path}">${c.label}</a>`;
  }).join("");

  const canBack = history.length > 1;
  return `
    <button class="iconbtn menu-toggle" id="menuToggle" aria-label="Menu">${icon.menu()}</button>
    <button class="iconbtn" id="backBtn" aria-label="Back" ${canBack ? "" : "disabled"}>${icon.back()}</button>
    <button class="iconbtn" id="homeBtn" aria-label="Home" data-nav="/">${icon.home()}</button>
    <nav class="crumbs" aria-label="Breadcrumb">${trail}</nav>
    <div class="topbar__spacer"></div>
    <div class="searchbox">${icon.search()}<span>Search sessions, rubrics…</span></div>`;
}

function render() {
  const route = parseRoute();
  document.getElementById("sidebar").innerHTML = renderSidebar(route);
  document.getElementById("topbar").innerHTML = renderTopbar(route);
  const content = document.getElementById("content");
  content.innerHTML = renderView(route);
  content.scrollTo?.(0, 0);
  window.scrollTo(0, 0);
  document.title = titleFor(route);
  document.querySelector(".app").classList.remove("nav-open");
}

function titleFor(route) {
  const crumbs = buildCrumbs(route);
  const leaf = crumbs[crumbs.length - 1]?.label;
  return leaf && leaf !== "Home" ? `${leaf} · Confluence` : "Confluence — Calibration Hub";
}

/* ============================================================================
   Interaction wiring (event delegation)
   ========================================================================== */
function onClick(e) {
  const nav = e.target.closest("[data-nav]");
  if (nav) { e.preventDefault(); go(nav.getAttribute("data-nav")); return; }

  const toast = e.target.closest("[data-toast]");
  if (toast) { showToast(toast.getAttribute("data-toast")); }

  const opt = e.target.closest(".score-opt");
  if (opt) {
    opt.parentElement.querySelectorAll(".score-opt").forEach((o) => {
      o.style.borderColor = "var(--line)"; o.style.background = "var(--surface)";
    });
    opt.style.borderColor = "var(--brand-500)";
    opt.style.background = "var(--info-bg)";
  }

  if (e.target.closest("#backBtn")) history.back();
  if (e.target.closest("#menuToggle")) document.querySelector(".app").classList.toggle("nav-open");
  if (e.target.closest(".scrim")) document.querySelector(".app").classList.remove("nav-open");

  // Filter chips (visual only)
  const chip = e.target.closest(".chip");
  if (chip) { chip.parentElement.querySelectorAll(".chip").forEach((c) => c.classList.remove("is-active")); chip.classList.add("is-active"); }
}

function onChange(e) {
  if (e.target.id === "roleSelect") {
    store.role = e.target.value;
    // Adaptive redirect: if the current page isn't in the new role's world, go home.
    const route = parseRoute();
    if (!canAccess(route.section, store.role)) go("/");
    else render();
    showToast(`Now viewing as ${ROLES[store.role].label}`);
  }
}

let toastTimer;
function showToast(msg) {
  let el = document.getElementById("toast");
  if (!el) { el = document.createElement("div"); el.id = "toast"; el.className = "toast"; document.body.appendChild(el); }
  el.innerHTML = `${icon.check()}<span>${msg}</span>`;
  el.classList.add("show");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => el.classList.remove("show"), 2400);
}

/* ---- utilities ----------------------------------------------------------- */
function fmtDate(iso) {
  const d = new Date(iso + "T00:00:00");
  return d.toLocaleDateString("en-US", { month: "short", day: "numeric" });
}
function dayPart() {
  const h = new Date().getHours();
  return h < 12 ? "morning" : h < 18 ? "afternoon" : "evening";
}
const initials = (name) => name.split(" ").filter((w) => /[A-Za-z]/.test(w[0])).slice(-2).map((w) => w[0]).join("").toUpperCase();

/* ---- boot ---------------------------------------------------------------- */
window.addEventListener("hashchange", render);
document.addEventListener("click", onClick);
document.addEventListener("change", onChange);
render();
