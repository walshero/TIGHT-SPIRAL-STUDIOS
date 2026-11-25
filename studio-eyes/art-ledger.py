#!/usr/bin/env python3
"""Art ledger gate: exit 1 if any asset in a manifest lacks source, license, url and sha256, or is still missing."""
import json,sys
m=json.load(open(sys.argv[1]));bad=[]
for a in m["assets"]:
    if a.get("status")=="in-house":
        if not a.get("author") or not a.get("sha256"):bad.append((a["card"],"in-house without author/sha256"))
        continue
    for k in ("source","author","license","license_url","url","sha256"):
        if not a.get(k):bad.append((a["card"],"no "+k));break
for c,w in bad:print("BLOCK",c,"-",w)
print(("SHIP" if not bad else "BLOCK"),len(m["assets"])-len(bad),"/",len(m["assets"]),"assets cleared")
sys.exit(1 if bad else 0)
