# v0.17: stone planter beds along the back (NW and NE) edges of every district plaza, gaps where roads enter.
import json, math
from shapely.geometry import Polygon, LineString
from shapely.ops import unary_union
W=json.load(open('isle_world.json'));P=json.load(open('props.json'))
K=0.42
obst=[Polygon(p['fp']).buffer(10) for p in W['props']]
roads=unary_union([LineString(r).buffer(46) for r in W['roads'] if len(r)>1])
land=unary_union([Polygon(p).buffer(0) for p in W['land']]).buffer(-20)
placed=[];n=0;ri=0;REASONS={}
def fit(name,anchor_local,Q):
    m=P[name];lx,ly=anchor_local;x=Q[0]-lx;y=Q[1]-ly
    fp=[[round(x+a,1),round(y+b,1)] for a,b in m['fp']];pg=Polygon(fp)
    why=('sea' if not land.contains(pg) else 'road' if pg.intersects(roads) else 'prop' if any(pg.intersects(o) for o in obst) else 'bed' if any(pg.buffer(6).intersects(q) for q in placed) else '')
    REASONS[why]=REASONS.get(why,0)+1
    if why:return None
    return dict(p=name,x=round(x,1),y=round(y,1),fp=fp),pg
PU=unary_union([Polygon(z['p']).buffer(0) for z in W['plazas']])
inner=PU.buffer(-4)
def fit2(name,anchor_local,Q):
    m=P[name];lx,ly=anchor_local;x=Q[0]-lx;y=Q[1]-ly
    fp=[[round(x+a_,1),round(y+b_,1)] for a_,b_ in m['fp']];pg=Polygon(fp)
    why=('sea' if not land.contains(pg) else 'plaza' if pg.intersects(inner) else 'road' if pg.intersects(roads) else 'prop' if any(pg.intersects(o) for o in obst) else 'bed' if any(pg.buffer(8).intersects(q) for q in placed) else '')
    REASONS[why]=REASONS.get(why,0)+1
    return None if why else (dict(p=name,x=round(x,1),y=round(y,1),fp=fp),pg)
geoms=getattr(PU,'geoms',[PU])
for g in geoms:
    ring=g.exterior;Lr=ring.length;d=0
    while d<Lr:
        p0=ring.interpolate(d);p1=ring.interpolate(min(Lr,d+4));tx,ty=p1.x-p0.x,p1.y-p0.y;nn=math.hypot(tx,ty) or 1
        nx,ny=ty/nn,-tx/nn   # outward normal for a counter-clockwise ring
        if not ring.is_ccw:nx,ny=-nx,-ny
        ok=False
        if ny<-.35:
            for kind in (('R',) if nx<0 else ('L',)):
                name='bed%s%d'%(kind,1+(ri%2));fp=P[name]['fp']
                anc=fp[0]  # front corner sits on the paving edge; bed extends back onto the grass
                r=fit2(name,anc,(p0.x+(-4 if kind=='R' else 4),p0.y-3))
                if r:W['props'].append(r[0]);placed.append(r[1]);n+=1;ri+=1;ok=True;break
        d+=150 if ok else 12
json.dump(W,open('isle_world.json','w'));print('beds placed',n,REASONS)
