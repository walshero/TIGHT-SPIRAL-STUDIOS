import json,sys,statistics as st,collections as C
R=json.load(open(sys.argv[1]))
def q(v):
    v=[x for x in v if x is not None]
    if not v: return "none"
    v=sorted(v); return f"n={len(v)} med={st.median(v):.0f}s p10={v[len(v)//10]:.0f} p90={v[min(len(v)-1,len(v)*9//10)]:.0f}"
by=C.defaultdict(list)
for r in R: by[r['persona']].append(r)
for p,rs in by.items():
    print(f"\n== {p} ({len(rs)} runs, level {rs[0]['level']})")
    print(" level finished:",sum(r['finishAt'] is not None for r in rs),"| finish time:",q([r['finishAt'] for r in rs]))
    print(" grown at end (of first 5):",C.Counter(r['end']['grown'] for r in rs))
    print(" KOs/run:",q([r['kos'] for r in rs]).replace('s ',' ').replace('s',''),"| repaved/run:",q([r['end']['paved'] for r in rs]).replace('s',''))
    sites=sorted({k for r in rs for k in r['siteT']})
    for k in sites:
        print(f"  {k:12s} down: {q([r['siteT'].get(k,{}).get('collapsing') for r in rs])} | grown: {q([r['siteT'].get(k,{}).get('grown') for r in rs])}")
    H=C.Counter()
    for r in rs:
        for k,v in r['hurts'].items(): H[k.split('/')[-1]]+=v
    print(" damage by source (total):",dict(H.most_common(6)))
    S=C.Counter((s['tgt'],s['who'],s['climb'] is not None,s['swim']) for r in rs for s in r['stuck'])
    print(" 45s-no-progress spots (target,who,climbing,swimming):",S.most_common(6))
    E=C.Counter(e for r in rs for e in r['errors']+r['pageerrors'])
    print(" errors:",E.most_common(5))
    B=C.Counter(e[2] for r in rs for e in r['events'] if e[1]=='baron'); print(" baron spawns by need:",dict(B))
    P=C.Counter();[P.update(r['picks']) for r in rs]; print(" picks:",dict(P.most_common(8)))
    T=C.Counter();[T.update(r['toasts']) for r in rs]; print(" messages shown:",T.most_common(8))
    print(" end states:",C.Counter(' '.join(r['end']['sites']) for r in rs).most_common(3))
