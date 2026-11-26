import asyncio,json,base64
from playwright.async_api import async_playwright
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch();pg=await b.new_page()
    errs=[];pg.on("pageerror",lambda e:errs.append(str(e)))
    await pg.goto("file:///home/claude/art14/art.html");await pg.wait_for_timeout(800)
    out=await pg.evaluate("window.__OUT");print("errors",errs)
    meta={}
    for k,v in out.items():
      open(f"/home/claude/art14/{k}.png","wb").write(base64.b64decode(v['png'].split(',')[1]));meta[k]={'w':v['w'],'h':v['h'],'fp':v['fp']}
    json.dump(meta,open('/home/claude/art14/meta.json','w'));print(list(meta))
    await b.close()
asyncio.run(main())
