#!/usr/bin/env node
/* THE COMFORT AUDITOR — real-browser contrast check for the dark comfort stops.
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
 * HOW — borrow the known solution, don't hand-roll it
 * ---------------------------------------------------
 * The checker is axe-core (already a CI dependency) — the industry-standard
 * accessibility engine. Its `color-contrast` rule composites alpha, applies the
 * WCAG font-size thresholds, and skips hidden/off-screen nodes far more reliably
 * than bespoke luminance math (an earlier hand-rolled pass false-flagged
 * mid-transition colors and off-screen skip-links). This tool is only the
 * HARNESS: it drives a real Chromium (the same engine as the phone and the CI
 * screenshots) through every dark comfort stop each page defines, lets colour
 * transitions settle, and asks axe to judge. axe JUDGES; we just aim the eyes.
 *
 * Usage:
 *   node comfort-audit.mjs                 # audit every *.html
 *   node comfort-audit.mjs a.html b.html   # audit specific files
 * Exit 0 = clean · 1 = at least one dark-stop contrast violation · 2 = cannot run.
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

// A stop is DARK if its background token drops to a charcoal value. We apply the
// class/attribute the page's own toggle uses; detection stays name-based so new
// pages are covered without a registry.
const DARK_CLASSES = ['warmdark','warm','dark','night','warm-dark'];
const DARK_ATTRS   = ['warm','dark','warm-dark','night'];
const STOP_CLASSES = ['warmdark','warm','dark','night','warm-dark','softer','daylight'];

function darkStops(src){
  const stops=[];
  for(const c of DARK_CLASSES)
    if(new RegExp('body\\.'+c.replace('-','\\-')+'\\s*[{,]').test(src)) stops.push({kind:'class',val:c});
  for(const a of DARK_ATTRS)
    if(src.includes(`data-comfort="${a}"`)) stops.push({kind:'attr',val:a});
  return stops;
}

const files = process.argv.slice(2).length
  ? process.argv.slice(2)
  : readdirSync('.').filter(f=>f.endsWith('.html')).sort();

const browser = await chromium.launch();
const report = {};
let totalViol = 0;

for (const f of files) {
  let src; try { src = readFileSync(f,'utf8'); } catch { continue; }
  const stops = darkStops(src);
  if (!stops.length) continue;

  const page = await browser.newPage({ viewport:{ width:390, height:844 } });
  await page.goto('file://'+process.cwd()+'/'+f);
  await page.addScriptTag({ content: axe.source });

  for (const st of stops) {
    await page.evaluate(({kind,val,STOP_CLASSES})=>{
      document.documentElement.removeAttribute('data-comfort');
      document.body.className = document.body.className.split(/\s+/)
        .filter(c=>!STOP_CLASSES.includes(c)).join(' ');
      if (kind==='class') document.body.classList.add(val);
      else document.documentElement.setAttribute('data-comfort', val);
    }, {kind:st.kind, val:st.val, STOP_CLASSES});
    await page.waitForTimeout(600); // let colour transitions come to rest

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
    if (rows.length) { report[`${f} [${st.kind}:${st.val}]`] = rows; totalViol += rows.length; }
  }
  await page.close();
}
await browser.close();

const keys = Object.keys(report);
if (!keys.length) {
  console.log(`CLEAN — no dark-stop colour-contrast violations across ${files.length} file(s). [axe-core ${axe.version}]`);
  process.exit(0);
}
console.log('=== DARK-STOP CONTRAST VIOLATIONS (axe-core '+axe.version+') ===\n');
for (const k of keys) {
  console.log(`${k} — ${report[k].length} violation(s)`);
  for (const r of report[k].slice(0,8))
    console.log(`   ${r.ratio}:1 (need ${r.need})  ${r.target}  ${r.fg} on ${r.bg}  ${r.snip}`);
  if (report[k].length>8) console.log(`   … +${report[k].length-8} more`);
  console.log('');
}
console.log(`TOTAL: ${totalViol} violation(s) in ${keys.length} file/stop combo(s).`);
console.log('Matt has retinitis pigmentosa. A dark stop that hides its own text does not ship.');
process.exit(1);
