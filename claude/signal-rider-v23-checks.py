import asyncio,math
from playwright.async_api import async_playwright
exec(open('play.py').read().split('async def main')[0])
async def main():
  async with async_playwright() as pw:
    b=await pw.chromium.launch(executable_path="/usr/bin/google-chrome",headless=True)
    pg=await b.new_page(viewport={"width":390,"height":844});errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    await pg.goto("file:///home/claude/v21t/hook.html");await pg.wait_for_timeout(500);await pg.mouse.click(195,500)
    await pg.evaluate("()=>{window.__b2=setInterval(()=>{var r=window.__dtn.run;if(r.lm)r.theta=r.lm.tgt;},16)}")
    for i in range(150):
      if await pg.evaluate("()=>getComputedStyle(document.getElementById('tray')).display")!='none':break
      await pg.wait_for_timeout(200)
    await pg.click('#bRide');await pg.wait_for_timeout(200)
    print('bare',await pg.evaluate("()=>window.__dtn.run.bare"))
    caps=[];spd=[];shot=0
    for i in range(130):
      st=await pg.evaluate("()=>({s:window.__dtn.run.s,v:document.getElementById('spd').textContent,c:document.getElementById('passed').style.display==='block'?document.getElementById('passed').innerText:'',ms:window.__dtn.run.realMs})")
      if st['c'] and (not caps or caps[-1]!=st['c']):caps.append(st['c'])
      if i%10==0:spd.append((round(st['s'],1),st['v'],round(st['ms'],2)))
      if shot==0 and 8<st['s']<14: await pg.screenshot(path='bare.png');shot=1
      if shot==1 and st['s']>24: await pg.screenshot(path='myelin.png');shot=2
      if st['s']>30:break
      await pg.wait_for_timeout(100)
    print('speed samples (s, m/s, ms)',spd);print('captions',caps)
    # leak test: jump to relay 1, deliberately miss after one match
    await pg.evaluate("()=>clearInterval(window.__b2)")
    await pg.evaluate("()=>{var r=window.__dtn.run,L=window.__dtn.legs();r.s=Math.max(r.s,L[0].end-18)}")
    hist=[];phase=0
    for i in range(140):
      v=await pg.evaluate("()=>{var r=window.__dtn.run;if(!r.lm)return null;return {k:r.lm.k,h:r.lm.hits}}")
      if v:
        if v['k']==0: await pg.evaluate("()=>{var r=window.__dtn.run;if(r.lm)r.theta=r.lm.tgt}")
        else: await pg.evaluate("()=>{var r=window.__dtn.run;if(r.lm)r.theta=r.lm.tgt+Math.PI}")
        if not hist or hist[-1]!=(v['k'],v['h']):hist.append((v['k'],v['h']))
      elif hist: break
      await pg.wait_for_timeout(60)
    print('leak (beat, charge)',hist)
    # second ride: ghost present, no bare
    await pg.evaluate("()=>{var r=window.__dtn.run;r.s=Math.max(r.s,60)}")
    await pg.evaluate("()=>document.querySelectorAll('.sheet').forEach(s=>s.style.display='none')")
    await pg.evaluate("()=>document.getElementById('bFadeWeek').click()");await pg.wait_for_timeout(300)
    await pg.click('#bRide');await pg.wait_for_timeout(1500)
    print('ride2 bare',await pg.evaluate("()=>window.__dtn.run.bare"),'ghost samples',await pg.evaluate("()=>window.__dtn.run.ghost?window.__dtn.run.ghost.filter(x=>x!==undefined).length:0"))
    await pg.evaluate("()=>{window.__b3=setInterval(()=>{var r=window.__dtn.run;r.theta=Math.PI/2+1.2},16)}")
    await pg.wait_for_timeout(1500);await pg.screenshot(path='ghost.png')
    print('errors',errs);await b.close()
asyncio.run(main())
