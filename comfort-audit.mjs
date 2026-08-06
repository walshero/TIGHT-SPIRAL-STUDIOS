#!/usr/bin/env node
/* THE COMFORT AUDITOR — real-browser contrast check for every comfort/dark stop.
 *
 * WHY THIS EXISTS
 * ---------------
 * The founder hit "text disappears" twice — The Tell and The Viscosity — where a
 * dark comfort stop only remapped background/text color and left every other
 * surface token at its LIGHT value, producing light-on-light. The WeasyPrint
 * Studio-Eyes sweep did not catch it: it reported the whole corpus clean while
 * two pages were visibly broken on the phone. A gate blind to the live dark stop
 * is not a gate.
 *
 * UPSTREAM FIX — 2026-08-06, a second blind spot in the same tool
 * -----------------------------------------------------------------
 * v1 of this tool detected stops by a hardcoded name list (`data-comfort="warm"`,
 * `body.dark{`, etc). The studio's actual convention had already moved on to
 * attribute selectors on <html> or <body> — `html[data-light="night"]`,
 * `body[data-stop="warmdark"]` — which the name list never matched. Checked
 * against the live corpus: 67 of 74 pages use the attribute-selector convention,
 * 0 use `data-comfort=`, 1 matches a `body.CLASS{` selector. The old detector's
 * `if (!stops.length) continue` meant this tool silently skipped 67 pages —
 * INCLUDING The Tell and The Viscosity, the two pages that motivated building it
 * — and still printed "CLEAN". Confirmed live: en195-arcade.html has a real,
 * visible light-on-light bug on its "softer" comfort stop (a non-"dark"-named
 * stop that only remapped --paper, leaving --ink at whatever the OS dark-mode
 * media query had already set it to) and v1 reported this file CLEAN.
 *
 * The fix does not add "data-light" to a name list — that just moves the
 * staleness to the next naming convention someone invents. Instead it PARSES
 * the page's own CSS for every `html[data-X="Y"]` / `body[data-X="Y"]`
 * attribute-selector rule and every `body.CLASS{` rule, and tests ALL of them,
 * not just ones that sound dark. "softer" broke contrast despite not being
 * named like a dark stop — guessing by name is exactly the mechanism that
 * missed it. Legacy `data-comfort="X"` support stays for any old file still
 * using it. No registry, no name list: the arithmetic is "what stops does this
 * page actually define," read from the page, every time.
 *
 * HOW — borrow the known solution, don't hand-roll it
 * ---------------------------------------------------
 * The checker is axe-core (already a CI dependency) — the industry-standard
 * accessibility engine. Its `color-contrast` rule composites alpha, applies the
 * WCAG font-size thresholds, and skips hidden/off-screen nodes far more reliably
 * than bespoke luminance math (an earlier hand-rolled pass false-flagged
 * mid-transition colors and off-screen skip-links). This tool is only the
 * HARNESS: it drives a real Chromium (the same engine as the phone and the CI
 * screenshots) through every stop each page defines, lets colour transitions
 * settle, and asks axe to judge. axe JUDGES; we just aim the eyes.
 *
 * Usage:
 *   node comfort-audit.mjs                 # audit every *.html
 *   node comfort-audit.mjs a.html b.html   # audit specific files
 * Exit 0 = clean · 1 = at least one stop contrast violation · 2 = cannot run.
 */
import { readFileSync, readdirSync } from 'node:fs';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);

// --- resolve deps from local node_modules, global npm root, or sandbox path ---
let chromium;
for (const p of ['playwright', process.env.PLAYWRIGHT_PATH,
                 '/opt/node22/lib/node_modules/playwright/index.js']) {
  if (!p) continue;
  try { ({ chromium } = require(p)); break; } catch {}
}
if (!chromium) { console.error('HALT — Playwright not found. `npm i playwright` or set PLAYWRIGHT_PATH.'); process.exit(2); }
let axe;
try { axe = require('axe-core'); } catch { console.error('HALT — axe-core not found. `npm i axe-core`.'); process.exit(2); }

// Legacy name list, kept only for any old file still using data-comfort= or a
// bare body.CLASS{ selector. Not the primary detection path anymore.
const LEGACY_DARK_CLASSES = ['warmdark','warm','dark','night','warm-dark'];
const LEGACY_DARK_ATTRS   = ['warm','dark','warm-dark','night'];

// Primary detection: read every (html|body)[data-X="Y"]{ ... } attribute
// selector straight out of the page's own CSS. This is how the studio's actual
// convention (data-light="day/dusk/night", data-stop="default/softer/warmdark",
// etc) is written, and it needs no name list — whatever stops a page defines,
// this finds them.
const ATTR_SELECTOR_RE = /\b(html|body)\[\s*data-([\w-]+)\s*=\s*["']([\w-]+)["']\s*\]/g;

function findStops(src){
  const seen = new Set();
  const stops = [];

  let m;
  ATTR_SELECTOR_RE.lastIndex = 0;
  while ((m = ATTR_SELECTOR_RE.exec(src))) {
    const [, el, attr, val] = m;
    const key = `attr:${el}:${attr}:${val}`;
    if (seen.has(key)) continue;
    seen.add(key);
    stops.push({ kind:'attr', el, attr:'data-'+attr, val });
  }

  for (const c of LEGACY_DARK_CLASSES) {
    if (new RegExp('body\\.'+c.replace('-','\\-')+'\\s*[{,]').test(src)) {
      const key = `class:${c}`;
      if (!seen.has(key)) { seen.add(key); stops.push({ kind:'class', val:c }); }
    }
  }
  for (const a of LEGACY_DARK_ATTRS) {
    if (src.includes(`data-comfort="${a}"`)) {
      const key = `legacy-attr:${a}`;
      if (!seen.has(key)) { seen.add(key); stops.push({ kind:'legacy-attr', el:'html', attr:'data-comfort', val:a }); }
    }
  }
  return stops;
}

const files = process.argv.slice(2).length
  ? process.argv.slice(2)
  : readdirSync('.').filter(f=>f.endsWith('.html')).sort();

const browser = await chromium.launch();
const report = {};
let totalViol = 0;
let totalStopsTested = 0;

for (const f of files) {
  let src; try { src = readFileSync(f,'utf8'); } catch { continue; }
  const stops = findStops(src);
  if (!stops.length) continue;

  // Test every stop under BOTH OS colour-scheme preferences. en195-arcade.html's
  // "softer" stop is the reason this matters: it only remaps --paper, so it
  // reads fine when the OS prefers light (--ink stays at its light-mode dark
  // value) and goes light-on-light the moment the OS prefers dark (the
  // `@media (prefers-color-scheme: dark)` block on :root has already swapped
  // --ink to a light value before the page-level toggle's partial override
  // lands on top of it). A stop tested against only one OS preference cannot
  // see that interaction — this is the bug that let v1's "test all stops" fix
  // still miss it.
  for (const scheme of ['light','dark']) {
    const page = await browser.newPage({ viewport:{ width:390, height:844 }, colorScheme: scheme });
    await page.goto('file://'+process.cwd()+'/'+f);
    await page.addScriptTag({ content: axe.source });

    for (const st of stops) {
      await page.evaluate((st) => {
        // Clear every attribute this page's own CSS showed us can be set on
        // html or body, plus the legacy class names, before applying one stop.
        document.documentElement.removeAttribute(st.attr && st.el==='html' ? st.attr : 'data-comfort');
        document.body.removeAttribute(st.attr && st.el==='body' ? st.attr : 'data-stop');
        if (st.kind === 'class') {
          document.body.className = document.body.className.split(/\s+/)
            .filter(c=>!['warmdark','warm','dark','night','warm-dark','softer','daylight'].includes(c)).join(' ');
          document.body.classList.add(st.val);
        } else {
          const target = st.el === 'html' ? document.documentElement : document.body;
          target.setAttribute(st.attr, st.val);
        }
      }, st);
      await page.waitForTimeout(600); // let colour transitions come to rest
      totalStopsTested++;

      const res = await page.evaluate(async () =>
        await axe.run(document, {
          runOnly:{ type:'rule', values:['color-contrast'] },
          resultTypes:['violations'],
        }));

      const rows = [];
      for (const v of res.violations)
        for (const n of v.nodes) {
          const d = (n.any && n.any[0] && n.any[0].data) || {};
          rows.push({
            target: Array.isArray(n.target)? n.target.join(' ') : String(n.target),
            ratio: d.contrastRatio, need: d.expectedContrastRatio,
            fg: d.fgColor, bg: d.bgColor,
            snip: (n.html||'').replace(/\s+/g,' ').slice(0,70),
          });
        }
      const label = st.kind === 'class' ? `class:${st.val}` : `${st.el}[${st.attr}="${st.val}"]`;
      if (rows.length) { report[`${f} [OS:${scheme}] [${label}]`] = rows; totalViol += rows.length; }
    }
    await page.close();
  }
}
await browser.close();

const keys = Object.keys(report);
if (!keys.length) {
  console.log(`CLEAN — ${totalStopsTested} stop(s) tested across ${files.length} file(s), no colour-contrast violations. [axe-core ${axe.version}]`);
  process.exit(0);
}
console.log('=== STOP CONTRAST VIOLATIONS (axe-core '+axe.version+') ===\n');
for (const k of keys) {
  console.log(`${k} — ${report[k].length} violation(s)`);
  for (const r of report[k].slice(0,8))
    console.log(`   ${r.ratio}:1 (need ${r.need})  ${r.target}  ${r.fg} on ${r.bg}  ${r.snip}`);
  if (report[k].length>8) console.log(`   … +${report[k].length-8} more`);
  console.log('');
}
console.log(`TOTAL: ${totalViol} violation(s) in ${keys.length} file/stop combo(s), ${totalStopsTested} stop(s) tested across ${files.length} file(s).`);
console.log('Matt has retinitis pigmentosa. A stop that hides its own text does not ship.');
process.exit(1);
