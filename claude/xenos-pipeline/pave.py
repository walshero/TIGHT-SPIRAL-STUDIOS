# v0.18: districts and lanes become one continuous cobbled surface (2013 Market), with smooth organic edges.
import json
from shapely.geometry import Polygon, LineString
from shapely.ops import unary_union
W=json.load(open('isle_world.json'))
pl=[Polygon(z['p']).buffer(14) for z in W['plazas'] if z['kind']!='deck']
rd=[LineString(r).buffer(36,cap_style=1) for r in W['roads'] if len(r)>1]
land=unary_union([Polygon(p).buffer(0) for p in W['land']]).buffer(-26)
U=unary_union(pl+rd).buffer(34,join_style=1).buffer(-34,join_style=1).intersection(land).simplify(1.5)
rings=[]
for g in getattr(U,'geoms',[U]):
    rings.append([[round(x,1),round(y,1)] for x,y in g.exterior.coords])
    for h in g.interiors:rings.append([[round(x,1),round(y,1)] for x,y in h.coords])
W['pave']=rings;json.dump(W,open('isle_world.json','w'));print('pave rings',len(rings),'area',round(U.area))
# v0.20 terraces: districts sit raised; a stone retaining wall drops from every south-facing edge of the district cores,
# with steps wherever a lane leaves the terrace.
from shapely.geometry import MultiLineString, Point
import math
core=unary_union([Polygon(z['p']).buffer(14) for z in W['plazas'] if z['kind']!='deck']).buffer(34,join_style=1).buffer(-34,join_style=1).intersection(land)
lanes=unary_union([LineString(r).buffer(40) for r in W['roads'] if len(r)>1])
walls=[];steps=[];WH=18
for g in getattr(core,'geoms',[core]):
    ring=g.exterior;cw=not ring.is_ccw;pts=list(ring.coords);cur=[]
    for (x0,y0),(x1,y1) in zip(pts,pts[1:]):
        tx,ty=x1-x0,y1-y0;n=math.hypot(tx,ty) or 1;nx,ny=ty/n,-tx/n
        if cw:nx,ny=-nx,-ny
        mid=Point((x0+x1)/2,(y0+y1)/2)
        face=ny>.25 and U.buffer(2).contains(mid) is False or ny>.25
        if face and not lanes.contains(mid):cur.append((x1,y1)) if cur else cur.extend([(x0,y0),(x1,y1)])
        else:
            if len(cur)>1:walls.append(cur)
            cur=[]
            if ny>.25 and lanes.contains(mid):steps.append([round((x0+x1)/2,1),round((y0+y1)/2,1),round(math.atan2(ty,tx),3)])
    if len(cur)>1:walls.append(cur)
# keep walls long enough to read; thin out step markers to one per crossing
walls=[[[round(x,1),round(y,1)] for x,y in w] for w in walls if LineString(w).length>40]
st2=[]
for s in steps:
    if all(math.hypot(s[0]-t[0],s[1]-t[1])>60 for t in st2):st2.append(s)
W['walls']=walls;W['steps']=st2;W['wallH']=WH
json.dump(W,open('isle_world.json','w'));print('walls',len(walls),'wall length',round(sum(LineString(w).length for w in walls)),'steps',len(st2))
