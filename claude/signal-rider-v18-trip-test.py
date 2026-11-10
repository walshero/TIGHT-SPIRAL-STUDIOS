import asyncio
from playwright.async_api import async_playwright
exec(open('/home/claude/art/t12.py').read().split('async def go():')[0])
async def g():
    async with async_playwright() as p:
        b=await p.chromium.launch();errs=[];pg=await b.new_page(viewport={'width':390,'height':844});pg.on('pageerror',lambda e:errs.append(str(e)))
        await to_tray(pg);await pg.click('#bRide');await pg.wait_for_timeout(3000)
        print('after 3 s:',await pg.evaluate("()=>document.getElementById('tripv').textContent"))
        # ride the whole course: jump through legs with a perfect aimer, then read the end card
        await pg.evaluate(AIMER,{'delay':0})
        await pg.evaluate("()=>{var r=window.__dtn.run,L=window.__dtn.legs();r.realM=0;r.realMs=0;}")
        for leg in range(4):
            await pg.evaluate("(i)=>{var r=window.__dtn.run,L=window.__dtn.legs();r.s=Math.max(r.s,L[i].end-30);}",leg)
            for k in range(80):
                await pg.wait_for_timeout(250)
                st=await pg.evaluate("()=>({leg:window.__dtn.run.leg,over:window.__dtn.run.over})")
                if st['over'] or st['leg']>leg:break
        await pg.wait_for_timeout(900)
        print('end card:',await pg.evaluate("()=>document.getElementById('endStats').textContent"))
        print('errors',errs);await b.close()
asyncio.run(g())
