import asyncio
from playwright.async_api import async_playwright
exec(open('/home/claude/art/t12.py').read().split('async def go():')[0])
async def g():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required']);errs=[]
        pg=await b.new_page(viewport={'width':390,'height':844},device_scale_factor=2);pg.on('pageerror',lambda e:errs.append(str(e)))
        await to_tray(pg);await pg.click('#bRide');await pg.wait_for_timeout(2500)
        st=await pg.evaluate("()=>({ac:!!window.__dtnAC||null,step:window.__sr.mus().step})")
        print('music steps after 2.5s:',st)
        # curves: sample tube centre offset across the course; straightness near events vs open
        cv=await pg.evaluate("""()=>{var L=window.__dtn.legs(),out=[];for(var u=0;u<L[3].end;u+=1)out.push(Math.abs(window.__sr.curveX(u)));
          var feats=window.__dtn.feats(),near=[],open=[];for(var u=5;u<L[3].end-5;u++){var dmin=Math.min.apply(null,feats.map(f=>Math.abs(f.s-u)));(dmin<2?near:dmin>9?open:[]).push(window.__sr.strAt(u));}
          var avg=a=>a.length?a.reduce((x,y)=>x+y,0)/a.length:null;return {maxX:Math.max.apply(null,out).toFixed(2),strNear:avg(near).toFixed(2),strOpen:avg(open).toFixed(2)};}""")
        print('curves:',cv)
        for i,ds in enumerate([40,90,150]):
            await pg.evaluate("(d)=>{var r=window.__dtn.run;r.s=d;}",ds);await pg.wait_for_timeout(700);await pg.screenshot(path=f'v19-curve{i}.png')
        # landing keeps the music running
        await pg.evaluate("()=>{var r=window.__dtn.run,sy=window.__dtn.syns();r.s=sy[0].s-1.5;}");await pg.wait_for_timeout(600)
        s0=await pg.evaluate("()=>window.__sr.mus().step");await pg.wait_for_timeout(1500);s1=await pg.evaluate("()=>({step:window.__sr.mus().step,landing:window.__sr.mus().landing})")
        print('landing music steps',s0,'->',s1)
        print('errors',errs);await b.close()
asyncio.run(g())
