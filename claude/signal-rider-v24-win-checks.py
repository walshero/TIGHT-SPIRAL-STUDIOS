import asyncio
from playwright.async_api import async_playwright
async def main():
  async with async_playwright() as pw:
    b=await pw.chromium.launch(executable_path="/usr/bin/google-chrome",headless=True)
    pg=await b.new_page(viewport={"width":390,"height":844},device_scale_factor=2);errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    await pg.goto("file:///home/claude/v21t/hook.html");await pg.wait_for_timeout(500);await pg.mouse.click(195,500);await pg.wait_for_timeout(500)
    for kind,times in [('cortex',[0.6,1.6,2.6,3.6,4.8,6.0]),('alarm',[1.2,2.6,4.2])]:
      await pg.evaluate("(k)=>window.__dtn.win(k)",kind)
      for t in times:
        while await pg.evaluate("()=>window.__dtn.wt()")<t: await pg.wait_for_timeout(30)
        await pg.screenshot(path=f'win-{kind}-{t}.png')
      while await pg.evaluate("()=>window.__dtn.wt()")>=0: await pg.wait_for_timeout(100)
      await pg.wait_for_timeout(400);await pg.screenshot(path=f'win-{kind}-card.png')
      await pg.evaluate("()=>document.querySelectorAll('.sheet').forEach(s=>s.style.display='none')")
    print('errors',errs);await b.close()
asyncio.run(main())
