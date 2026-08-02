/* ═══════════════ AGENTIC PLAYTESTER — the hands ═══════════════
   A studio instrument. It does NOT judge; it PLAYS and OBSERVES, so an agent
   (the brain — see claude_seat-agentic-playtester.md) can loop:
       observe (screenshot + interactive-element digest) -> decide -> act -> observe
   Target-agnostic: any local file or reachable URL. Offline-safe (file:// needs
   no network — the only way to run it in this egress-walled environment).

   USAGE
     node playtester-harness.mjs <target> [--out DIR] [--phone|--desktop]
                                          [--calm] [--actions actions.json]
     <target>  a path (-> file://) or an http(s) URL
     --actions a JSON array of steps; an observation is captured after each:
                 {"do":"click","sel":"#toCall"}
                 {"do":"drag","sel":"#bet","to":0.7}   // 0..1 along the track
                 {"do":"fill","sel":"#loadfield","text":"..."}
                 {"do":"key","key":"Enter"}
                 {"do":"wait","ms":600}
                 {"do":"shot"}                          // just snapshot
   OUTPUT (in --out, default ./playtest-out)
     step-00.png / step-00.json ... a screenshot + observation per step
     Each observation: { title, url, screen, text, controls[] } where a control
     is { tag, label, sel, box, pressed, disabled } — enough for an agent to
     choose the next tap the way a thumb would. */

import pkg from '/opt/node22/lib/node_modules/playwright/index.js';
const { chromium } = pkg;
import { mkdirSync, writeFileSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';

const argv = process.argv.slice(2);
if (!argv.length || argv[0].startsWith('--')) {
  console.error('usage: node playtester-harness.mjs <target> [--out DIR] [--phone|--desktop] [--calm] [--actions actions.json]');
  process.exit(2);
}
const target = argv[0];
const opt = (name, def) => { const i = argv.indexOf(name); return i >= 0 ? (argv[i+1] && !argv[i+1].startsWith('--') ? argv[i+1] : true) : def; };
const OUT = resolve(opt('--out', 'playtest-out'));
const PHONE = argv.includes('--phone') || !argv.includes('--desktop');
const CALM = argv.includes('--calm');
const actionsFile = opt('--actions', null);
const actions = actionsFile ? JSON.parse(readFileSync(resolve(actionsFile), 'utf8')) : [];

const url = /^https?:\/\//.test(target) ? target : 'file://' + resolve(target);
mkdirSync(OUT, { recursive: true });

/* what the agent "sees": every interactive element, the way a player scans a screen. */
const OBSERVE = () => {
  function vis(el){ const r=el.getBoundingClientRect(); const s=getComputedStyle(el);
    return r.width>0 && r.height>0 && s.visibility!=='hidden' && s.display!=='none' && el.offsetParent!==null; }
  function sel(el){ if(el.id) return '#'+el.id;
    const same=[...document.querySelectorAll(el.tagName)].filter(x=>x.className===el.className);
    const n=same.indexOf(el); return el.tagName.toLowerCase()+(el.className?('.'+el.className.trim().split(/\s+/).join('.')):'')+(n>0?`:nth-of-type(${n+1})`:''); }
  const sels='button, a, input, [role=button], [onclick], [tabindex]';
  const controls=[...document.querySelectorAll(sels)].filter(vis).map(el=>{
    const r=el.getBoundingClientRect();
    return { tag:el.tagName.toLowerCase(),
      label:(el.getAttribute('aria-label')||el.value||el.textContent||'').trim().replace(/\s+/g,' ').slice(0,80),
      sel:sel(el),
      box:{x:Math.round(r.x),y:Math.round(r.y),w:Math.round(r.width),h:Math.round(r.height)},
      pressed:el.getAttribute('aria-pressed'),
      disabled:el.disabled===true||el.getAttribute('aria-disabled')==='true' };
  });
  const onScreen=[...document.querySelectorAll('.screen, [class*=screen]')].find(vis);
  const bodyText=(document.body.innerText||'').replace(/\s+/g,' ').trim().slice(0,1200);
  return { title:document.title, url:location.href,
    screen: onScreen ? (onScreen.id||onScreen.className) : null,
    text: bodyText, controls };
};

const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const ctx = await browser.newContext({
  viewport: PHONE ? { width:390, height:844 } : { width:1200, height:900 },
  deviceScaleFactor: 1,
  userAgent: 'agentic-playtester (Tight Spiral Productions)'
});
const page = await ctx.newPage();
const errs = []; page.on('pageerror', e => errs.push(String(e).split('\n')[0]));

let step = 0;
async function snap(note){
  if (CALM) await page.evaluate(() => document.documentElement.setAttribute('data-motion','calm'));
  const pad = String(step).padStart(2,'0');
  await page.screenshot({ path: `${OUT}/step-${pad}.png` });
  const obs = await page.evaluate(OBSERVE);
  obs.step = step; obs.note = note || null; obs.errors = errs.slice();
  writeFileSync(`${OUT}/step-${pad}.json`, JSON.stringify(obs, null, 2));
  console.log(`step ${pad}: screen=${obs.screen} controls=${obs.controls.length}${note?(' — '+note):''}`);
  step++;
  return obs;
}

async function act(a){
  if (a.do === 'click') await page.click(a.sel, { timeout: 5000 });
  else if (a.do === 'fill') await page.fill(a.sel, a.text);
  else if (a.do === 'key') await page.keyboard.press(a.key);
  else if (a.do === 'wait') await page.waitForTimeout(a.ms || 300);
  else if (a.do === 'drag') {   /* slide a range input to a 0..1 fraction of its track */
    const box = await page.locator(a.sel).boundingBox();
    if (box){ const y=box.y+box.height/2;
      await page.mouse.move(box.x+2, y); await page.mouse.down();
      await page.mouse.move(box.x + Math.max(0,Math.min(1,a.to))*box.width, y, { steps:8 });
      await page.mouse.up(); }
  } else if (a.do === 'shot') { /* no-op; snapshot happens after */ }
}

await page.goto(url, { waitUntil: 'domcontentloaded' });
await snap('load');
for (const a of actions){ await act(a); if (a.after) await page.waitForTimeout(a.after); await snap(a.do + (a.sel?(' '+a.sel):'')); }

await browser.close();
console.log(`\nwrote ${step} observation(s) to ${OUT}${errs.length?`  [${errs.length} page error(s)!]`:''}`);
if (errs.length) console.log('errors: ' + errs.join(' | '));
