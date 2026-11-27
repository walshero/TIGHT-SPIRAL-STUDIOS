import asyncio,json,base64
from playwright.async_api import async_playwright
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch();pg=await b.new_page()
    errs=[];pg.on("pageerror",lambda e:errs.append(str(e)))
    await pg.goto("file:///home/claude/art14/landmarks.html");await pg.wait_for_timeout(1500)
    out=await pg.evaluate("window.__OUT");print("errors",errs)
    meta={}
    for k,v in (out or {}).items():
      open(f"/home/claude/art14/{k}.png","wb").write(base64.b64decode(v.pop('png').split(',')[1]));meta[k]=v
    old=json.load(open('/home/claude/art14/meta.json'));old.update({k:{**v,'fp':v.get('fp',[[0,0],[1,0],[1,1],[0,1]])} for k,v in meta.items()})
    json.dump(old,open('/home/claude/art14/meta.json','w'));print(list(meta))
    await b.close()
asyncio.run(main())
