#!/usr/bin/env node
/* THE COMFORT AUDITOR — Chromium ground-truth for dark comfort stops.
 *
 * WHY: the WeasyPrint Studio-Eyes sweep under-reports light-on-light in the
 * dark stops (it rendered the-tell.html "clean" while it was visibly broken).
 * This renders each page in a REAL browser — the same engine as the phone and
 * the CI screenshots — applies every dark comfort stop the file defines, and
 * measures text-vs-background contrast for every visible element.
 *
 * A dark stop that leaves a background token at a light root value produces
 * light-on-light (or dark-on-dark) text. That is what this catches.
 *
 * Usage: node comfort-audit.mjs [file.html ...]   (default: all *.html)
 * Exit 1 if any dark-stop contrast failure is found.
 */
import { readFileSync, readdirSync } from 'node:fs';
import { createRequire } from 'node:module';
// Resolve Playwright from local node_modules, the global npm root, or the known
// sandbox path — so the tool runs in CI, on a dev box, or in the agent sandbox.
const require = createRequire(import.meta.url);
let chromium;
for (const p of ['playwright', process.env.PLAYWRIGHT_PATH,
                 '/opt/node22/lib/node_modules/playwright/index.js']) {
  if (!p) continue;
  try { ({ chromium } = require(p)); break; } catch {}
}
if (!chromium) { console.error('HALT — Playwright not found. `npm i playwright` or set PLAYWRIGHT_PATH.'); process.exit(2); }

const DARK_CLASSES = ['warmdark','warm','dark','night','warm-dark'];
const DARK_ATTRS   = ['warm','dark','warm-dark','night'];

const files = process.argv.slice(2).length
  ? process.argv.slice(2)
  : readdirSync('.').filter(f=>f.endsWith('.html')).sort();

function darkStops(src){
  const stops=[];
  for(const c of DARK_CLASSES){
    if(new RegExp('body\\.'+c.replace('-','\\-')+'\\s*[{,]').test(src)) stops.push({kind:'class',val:c});
  }
  for(const a of DARK_ATTRS){
    if(src.includes(`data-comfort="${a}"`)) stops.push({kind:'attr',val:a});
  }
  return stops;
}

const AUDIT = () => {
  function parse(c){const m=c && c.match(/[\d.]+/g); if(!m) return null; const [r,g,b,a]=m.map(Number); return [r,g,b,a==null?1:a];}
  function lum([r,g,b]){const f=v=>{v/=255;return v<=.03928?v/12.92:((v+.055)/1.055)**2.4};return .2126*f(r)+.7152*f(g)+.0722*f(b);}
  function over(fg,bg){const a=fg[3];return [0,1,2].map(i=>fg[i]*a+bg[i]*(1-a));}
  function ratio(a,b){const L1=lum(a),L2=lum(b),hi=Math.max(L1,L2),lo=Math.min(L1,L2);return (hi+.05)/(lo+.05);}
  function bgOf(el){
    let chain=[], n=el;
    while(n){const c=parse(getComputedStyle(n).backgroundColor); if(c&&c[3]>0) chain.push(c); n=n.parentElement;}
    // also page default:
    let base=[255,255,255];
    for(let i=chain.length-1;i>=0;i--) base=over(chain[i],base);
    return base;
  }
  const vis=el=>{const s=getComputedStyle(el);if(s.display==='none'||s.visibility==='hidden'||+s.opacity===0)return false;
    const r=el.getBoundingClientRect(); if(r.width<1||r.height<1) return false;
    // off-screen (skip-links parked at left:-9999px / top:-9999px show only on :focus) — not a resting-state defect
    if(r.right<=0||r.bottom<=0||r.left>=innerWidth) return false; return true;};
  const fails=[];
  const all=document.querySelectorAll('body *');
  for(const el of all){
    // element with its own direct text
    const t=[...el.childNodes].filter(n=>n.nodeType===3&&n.textContent.trim()).map(n=>n.textContent.trim()).join(' ');
    if(!t) continue;
    if(el.closest('.sr, [aria-hidden="true"], .comfort, .cstop')) continue;
    // must be in an active screen (skip inactive .screen panels)
    const scr=el.closest('.screen'); if(scr && !scr.classList.contains('on')) continue;
    if(!vis(el)) continue;
    const cs=getComputedStyle(el);
    const fg=parse(cs.color); if(!fg) continue;
    const bg=bgOf(el);
    const eff=over(fg,bg);
    const R=ratio(eff,bg);
    const size=parseFloat(cs.fontSize), bold=(+cs.fontWeight)>=700;
    const large=(size>=24)||(size>=18.66&&bold);
    const thr=large?3.0:4.5;
    if(R<thr){
      fails.push({sel:el.tagName.toLowerCase()+(el.className&&typeof el.className==='string'?'.'+el.className.trim().split(/\s+/).join('.'):''),
        text:t.slice(0,42), ratio:+R.toFixed(2), thr, color:cs.color, bg:'rgb('+bg.map(x=>Math.round(x)).join(',')+')'});
    }
  }
  return fails;
};

const browser = await chromium.launch();
let totalFail=0; const report={};
for(const f of files){
  const src=readFileSync(f,'utf8');
  const stops=darkStops(src);
  if(!stops.length) continue;
  const page=await browser.newPage({viewport:{width:390,height:844}});
  await page.goto('file://'+process.cwd()+'/'+f);
  for(const st of stops){
    await page.evaluate(({kind,val})=>{
      document.documentElement.removeAttribute('data-comfort');
      document.body.className=document.body.className.split(/\s+/).filter(c=>!['warmdark','warm','dark','night','warm-dark','softer','daylight'].includes(c)).join(' ');
      if(kind==='class') document.body.classList.add(val);
      else document.documentElement.setAttribute('data-comfort',val);
    }, st);
    await page.waitForTimeout(550);
    const fails=await page.evaluate(AUDIT);
    if(fails.length){
      const key=`${f} [${st.kind}:${st.val}]`;
      report[key]=fails; totalFail+=fails.length;
    }
  }
  await page.close();
}
await browser.close();

const keys=Object.keys(report);
if(!keys.length){ console.log('CLEAN — no dark-stop contrast failures across',files.length,'files.'); process.exit(0); }
console.log('=== DARK-STOP CONTRAST FAILURES ===\n');
for(const k of keys){
  console.log(k+' — '+report[k].length+' fail(s)');
  for(const x of report[k].slice(0,6)) console.log(`   ${x.ratio}:1 (need ${x.thr})  ${x.sel}  "${x.text}"  ${x.color} on ${x.bg}`);
  if(report[k].length>6) console.log(`   … +${report[k].length-6} more`);
  console.log('');
}
console.log('TOTAL:',totalFail,'failures in',keys.length,'file/stop combos.');
process.exit(1);
