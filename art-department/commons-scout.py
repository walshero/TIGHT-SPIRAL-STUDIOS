#!/usr/bin/env python3
"""commons-scout.py — find and fetch open-licensed Wikimedia Commons photos.

Why this exists: the session sandbox cannot reach Wikimedia, but GitHub Actions can.
Push a request JSON to art-department/commons-requests/ and the commons-scout workflow
runs this script and commits the results to art-department/commons-scout/<request>/.

Request shapes
  {"mode":"search","per_query":12,"queries":{"basil":"basil pot windowsill", ...}}
      -> candidates.json + sheet-<key>.jpg (numbered contact sheet per query)
  {"mode":"fetch","width":640,"files":{"basil":"File:Some_photo.jpg", ...}}
      -> <key>.jpg (resized JPEG) + credits.json (artist, license, page URL)

The arithmetic, not the vibe:
  - license must be CC0 / PD / CC BY / CC BY-SA (anything else is dropped)
  - candidates are ranked phone-camera first (EXIF Make in PHONE_MAKES), because the
    feed is supposed to look like people's own posts, not stock or specimen shots.
"""
import json, sys, os, io, re, time, urllib.parse, urllib.request
from PIL import Image, ImageDraw, ImageFont

API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "TightSpiralStudios-commons-scout/1.0 (https://github.com/walshero/TIGHT-SPIRAL-STUDIOS)"}
OK_LIC = re.compile(r"^(CC0|Public domain|PD|CC BY(-SA)? \d(\.\d)?)", re.I)
PHONE_MAKES = ("apple", "samsung", "google", "huawei", "xiaomi", "oneplus", "motorola",
               "lg electronics", "sony mobile", "htc", "nokia", "oppo", "vivo", "realme", "hmd global")

def get(params):
    params = dict(params, format="json", origin="*")
    url = API + "?" + urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return json.load(r)
        except Exception as e:
            time.sleep(2 + attempt * 3)
    raise SystemExit("API failed: " + url)

def fetch_bytes(url):
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                return r.read()
        except Exception:
            time.sleep(2 + attempt * 3)
    return None

def strip(html):
    return re.sub(r"<[^>]+>", "", html or "").strip()

def info_for(pages, width):
    out = []
    for p in pages:
        ii = (p.get("imageinfo") or [{}])[0]
        em = ii.get("extmetadata") or {}
        lic = strip(em.get("LicenseShortName", {}).get("value", ""))
        if not OK_LIC.match(lic):
            continue
        make = ""
        for m in ii.get("commonmetadata") or []:
            if m.get("name") == "Make":
                make = str(m.get("value", "")).strip()
        out.append({
            "title": p["title"],
            "page": "https://commons.wikimedia.org/wiki/" + urllib.parse.quote(p["title"].replace(" ", "_")),
            "w": ii.get("width"), "h": ii.get("height"),
            "license": lic,
            "artist": strip(em.get("Artist", {}).get("value", ""))[:120],
            "make": make,
            "phone": any(make.lower().startswith(m) for m in PHONE_MAKES),
            "thumb": ii.get("thumburl"),
            "index": p.get("index", 999),
        })
    return out

PROPS = dict(prop="imageinfo", iiprop="url|size|extmetadata|commonmetadata",
             iiextmetadatafilter="LicenseShortName|Artist")

def search(q, n):
    d = get(dict(PROPS, action="query", generator="search", gsrnamespace=6,
                 gsrsearch=q + " filetype:bitmap", gsrlimit=max(n * 3, 30), iiurlwidth=360))
    cands = info_for((d.get("query") or {}).get("pages", {}).values(), 360)
    cands.sort(key=lambda c: (not c["phone"], c["index"]))
    return cands[:n]

def sheet(cands, path):
    W, H, PAD = 360, 270, 30
    cols = 4
    rows = (len(cands) + cols - 1) // cols or 1
    im = Image.new("RGB", (cols * W, rows * (H + PAD)), "white")
    d = ImageDraw.Draw(im)
    try:
        f = ImageFont.truetype("DejaVuSans-Bold.ttf", 20)
    except Exception:
        f = ImageFont.load_default()
    for i, c in enumerate(cands):
        b = fetch_bytes(c["thumb"]) if c.get("thumb") else None
        x, y = (i % cols) * W, (i // cols) * (H + PAD)
        if b:
            try:
                t = Image.open(io.BytesIO(b)).convert("RGB"); t.thumbnail((W - 6, H - 6))
                im.paste(t, (x + 3, y + 3))
            except Exception:
                pass
        d.text((x + 6, y + H + 4), f"{i}  {'PHONE ' if c['phone'] else ''}{c['license']}", fill="black", font=f)
    im.save(path, quality=80)

def main(req_path):
    req = json.load(open(req_path))
    name = os.path.splitext(os.path.basename(req_path))[0]
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "commons-scout", name)
    os.makedirs(out, exist_ok=True)
    if req["mode"] == "search":
        allc = {}
        for key, q in req["queries"].items():
            c = search(q, req.get("per_query", 12))
            allc[key] = {"query": q, "candidates": c}
            sheet(c, os.path.join(out, f"sheet-{key}.jpg"))
        json.dump(allc, open(os.path.join(out, "candidates.json"), "w"), indent=1, ensure_ascii=False)
    elif req["mode"] == "fetch":
        width = req.get("width", 640)
        credits = {}
        for key, title in req["files"].items():
            d = get(dict(PROPS, action="query", titles=title, iiurlwidth=width))
            c = info_for((d.get("query") or {}).get("pages", {}).values(), width)
            if not c:
                credits[key] = {"title": title, "error": "missing or license not allowed"}
                continue
            c = c[0]
            b = fetch_bytes(c["thumb"])
            img = Image.open(io.BytesIO(b)).convert("RGB")
            img.thumbnail((width, width))
            img.save(os.path.join(out, key + ".jpg"), quality=78, optimize=True, progressive=True)
            credits[key] = c
        json.dump(credits, open(os.path.join(out, "credits.json"), "w"), indent=1, ensure_ascii=False)
    print("wrote", out)

if __name__ == "__main__":
    for p in sys.argv[1:]:
        main(p)
