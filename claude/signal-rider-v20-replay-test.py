import asyncio
from playwright.async_api import async_playwright
exec(open('/home/claude/art/t12.py').read().split('async def go():')[0])
async def g():
    async with async_playwright() as p:
        b=await p.chromium.launch();errs=[];pg=await b.new_page(viewport={'width':390,'height':844},device_scale_factor=2);pg.on('pageerror',lambda e:errs.append(str(e)))
        await to_tray(pg);await pg.click('#bRide');await pg.wait_for_timeout(400)
        # ride: grab two greens, take one pink, then a perfect landing run through all four gaps
        await pg.evaluate("""()=>new Promise(res=>{var r=window.__dtn.run,P=window.__dtn.pickups().filter(x=>x.s>r.s+3).sort((a,b)=>a.s-b.s);var G=P.filter(x=>x.good).slice(0,2),R=P.filter(x=>!x.good).slice(0,1),T=G.concat(R).sort((a,b)=>a.s-b.s),i=0,n=0;
          var iv=setInterval(()=>{var t=T[i];if(!t||n++>2000){clearInterval(iv);res();return;}r.theta=t.a;if(t.hit||r.s>t.s+1)i++;},16);})""")
        await pg.evaluate(AIMER,{'delay':0})
        for leg in range(4):
            await pg.evaluate("(i)=>{var r=window.__dtn.run,L=window.__dtn.legs();r.s=Math.max(r.s,L[i].end-25);}",leg)
            for k in range(80):
                await pg.wait_for_timeout(250)
                st=await pg.evaluate("()=>({leg:window.__dtn.run.leg,over:window.__dtn.run.over,faded:window.__dtn.run.faded})")
                if st['over'] or st['faded'] or st['leg']>leg:break
            if st['over'] or st['faded']:break
        await pg.wait_for_timeout(1200)
        txt=await pg.evaluate("()=>{var e=document.getElementById('endWeek'),f=document.getElementById('fadeWeek');return (e&&e.innerText)||(f&&f.innerText)||'(empty)';}")
        print(txt)
        await pg.evaluate("()=>{var e=document.getElementById('endWeek');if(e)e.scrollIntoView({block:'start'});}");await pg.wait_for_timeout(200)
        await pg.screenshot(path='v20-replay.png');print('errors',errs);await b.close()
asyncio.run(g())
