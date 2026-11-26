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
