import asyncio,json
from playwright.async_api import async_playwright
async def main():
  async with async_playwright() as pw:
    b=await pw.chromium.launch(executable_path="/usr/bin/google-chrome",headless=True)
    pg=await b.new_page(viewport={"width":390,"height":844});errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    await pg.goto("file:///home/claude/v21t/hook.html");await pg.evaluate("()=>localStorage.setItem('dtn.comfort',JSON.stringify({roll:0}))");await pg.reload();await pg.wait_for_timeout(500)
    await pg.mouse.click(195,500);await pg.wait_for_timeout(300)
    t0=await pg.evaluate("()=>window.__dtn.run.theta")
    await pg.keyboard.down("ArrowRight");await pg.wait_for_timeout(300);await pg.keyboard.up("ArrowRight")
    t1=await pg.evaluate("()=>window.__dtn.run.theta")
    print('STEER right: theta',round(t0,2),'->',round(t1,2),'cos',round(__import__('math').cos(t0),2),'->',round(__import__('math').cos(t1),2),'(x grows = moves right)')
    # skip warm-up: jump
    await pg.evaluate("()=>{window.__b2=setInterval(()=>{var r=window.__dtn.run;if(r.lm)r.theta=r.lm.tgt;},16)}")
    for i in range(120):
      if await pg.evaluate("()=>getComputedStyle(document.getElementById('tray')).display")!='none':break
      await pg.wait_for_timeout(200)
    await pg.evaluate("()=>clearInterval(window.__b2)")
    print('tray open',await pg.evaluate("()=>getComputedStyle(document.getElementById('tray')).display"),'pred shown first time:',await pg.evaluate("()=>getComputedStyle(document.getElementById('pred')).display"))
    rr=await pg.evaluate("()=>{var r=document.getElementById('rideRow').getBoundingClientRect();return [Math.round(r.top),Math.round(r.bottom),innerHeight]}")
    print('ride row box (top,bottom,viewport)',rr)
    await pg.screenshot(path='tray.png')
    # calm road: pink cards
    await pg.click('#bCalm');await pg.wait_for_timeout(300)
    ids=await pg.evaluate("()=>[...new Set(window.__dtn.pickups().filter(p=>!p.good).map(p=>p.card.id))]")
    print('CALM pink ids',ids)
    # group load: find a red group with n>=2, place spark on it
    print('reds',await pg.evaluate("()=>[window.__dtn.run.s,window.__dtn.pickups().filter(p=>!p.good).map(p=>Math.round(p.s))]"))
    g=await pg.evaluate("()=>{var r=window.__dtn.run,A=window.__dtn.pickups(),P=A.filter(p=>!p.good&&p.s>r.s+5&&p.s<220).sort((a,b)=>a.s-b.s);var q=P[0];A.push(Object.assign({},q,{a:q.a+0.5,s:q.s+0.6,n:2,hit:false}));q.n=2;var gp=q.grp,G=A.filter(p=>p.grp===gp);return {grp:gp,n:G.length,s:G[0].s,a:G.map(p=>p.a)}}")
    print('group',g)
    await pg.evaluate("(g)=>{var r=window.__dtn.run;r.s=g.s-2;window.__fix=setInterval(()=>{var rr=window.__dtn.run;rr.theta=(g.a[0]+g.a[1])/2;},5)}",g)
    
    for i in range(40):
      if await pg.evaluate("(g)=>window.__dtn.run.s>g.s+2",g):break
      await pg.wait_for_timeout(100)
    st=await pg.evaluate("()=>{var r=window.__dtn.run;return {load:r.load||0,hits:r.hits,hud:document.getElementById('hits').innerText}}")
    print('after crossing group between two blocks:',st)
    await pg.evaluate("()=>clearInterval(window.__fix)")
    # end the ride quickly and open tray to see prediction
    await pg.evaluate("()=>{var r=window.__dtn.run;r.s=300}");await pg.wait_for_timeout(300)
    await pg.evaluate("()=>document.querySelectorAll('.sheet').forEach(s=>s.style.display='none')")
    await pg.evaluate("()=>document.getElementById('bFadeWeek').click()");await pg.wait_for_timeout(300)
    print('pred after a ride:',await pg.evaluate("()=>getComputedStyle(document.getElementById('pred')).display"),await pg.evaluate("()=>document.getElementById('fxp').style.visibility"))
    await pg.evaluate("()=>window.__dtn.setWeek({night:1,phone:1,rent:1})")
    await pg.click('#pred button[data-p=fewer]');await pg.wait_for_timeout(200)
    print('pred result:',await pg.evaluate("()=>document.getElementById('predRes').textContent"))
    await pg.screenshot(path='pred.png')
    # lightning cap check & settings
    print('errors',errs);await b.close()
asyncio.run(main())
