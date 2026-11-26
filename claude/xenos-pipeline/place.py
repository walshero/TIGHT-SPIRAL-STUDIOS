import json,numpy as np,cv2
I=json.load(open('isle.json'));D=json.load(open('props.json'))
TW,TH=25.0,10.4   # brick lattice: one iso step = 12.5 x 5.2
OLD={'M':(1700,420),'U':(620,420),'P':(760,1130)}
def off(k,dx,dy,c=None,kc=1.0,**kw):
    s=D[k]['src'];d=D[k]
    if c:  # compress cluster spacing toward its centre (props keep their size): move the footprint centre, not the corner
        fx=sum(p[0] for p in d['fp'])/len(d['fp']);fy=sum(p[1] for p in d['fp'])/len(d['fp'])
        cx,cy=s[0]+fx,s[1]+fy;ox,oy=OLD[c];nx,ny=ox+(cx-ox)*kc,oy+(cy-oy)*kc
        return dict(p=k,x=round(nx-fx+dx,1),y=round(ny-fy+dy,1),**kw)
    return dict(p=k,x=round(s[0]+dx,1),y=round(s[1]+dy,1),**kw)
DC=I['districts'];DC['University']=[DC['University'][0]+102,DC['University'][1]+12];DC['Pier']=[DC['Pier'][0]+126,DC['Pier'][1]-30]
def rel(c,old):return (DC[c][0]-old[0],DC[c][1]-old[1])
M=rel('Market',(1700,420));U=rel('University',(620,420));P=rel('Pier',(760,1130))
mk=DC['Market'];un=DC['University'];lb=DC['Lobby']
inst=[off('pagoda',*M,c='M',kc=0.9),off('lampM1',*M,c='M',kc=0.9),off('cartM',*M,c='M',kc=0.9),off('crates',*M,c='M',kc=0.9),off('board',*M,c='M',kc=0.9),
 dict(p='train',x=mk[0]-640,y=mk[1]-250),off('emptyH',mk[0]-560-D['emptyH']['src'][0],mk[1]+10-D['emptyH']['src'][1]),
 dict(p='lampS2',x=mk[0]-430,y=mk[1]-60),dict(p='treeS',x=mk[0]+520,y=mk[1]-160),
 off('news',*U,c='U',kc=0.62),off('planter',*U,c='U',kc=0.62),off('clock',*U,c='U',kc=0.62),dict(p='glyphs',x=un[0]+340,y=un[1]-250),dict(p='lampM1',x=un[0]-160,y=un[1]-300,flip=1),
 off('aquarium',*P,c='P',kc=0.55),off('iowcart',*P,c='P',kc=0.55),off('fishhouse',*P,c='P',kc=0.55),off('bucket',*P,c='P',kc=0.55),
 dict(p='treeS',x=lb[0]-330,y=lb[1]-40,flip=1),dict(p='treeS',x=lb[0]+230,y=lb[1]-380)]
DIS=['Market']*9+['University']*5+['Pier']*4+['Lobby']*2+['Palace gardens']*5+['Windmill Hill']*2
K=0.6   # v0.14: spacing shrinks with the world; buildings keep their size
from shapely.geometry import Polygon, Point
from shapely.ops import unary_union
pg=DC['Palace gardens'];wh=DC['Windmill Hill']
inst+=[dict(p='treeS',x=pg[0]-260,y=pg[1]-180),dict(p='treeS',x=pg[0]+60,y=pg[1]-260,flip=1),dict(p='treeS',x=pg[0]-120,y=pg[1]+20),
       off('planter',pg[0]-60-D['planter']['src'][0],pg[1]-90-D['planter']['src'][1]),off('planter',pg[0]+120-D['planter']['src'][0],pg[1]-30-D['planter']['src'][1]),
       dict(p='treeS',x=wh[0]-240,y=wh[1]-120),dict(p='treeS',x=wh[0]+40,y=wh[1]-160,flip=1)]
def fpw(i):
    d=D[i['p']];pts=[]
    for x,y in d['fp']:
        if i.get('flip'):x=d['w']-x
        pts.append([round(i['x']+x,1),round(i['y']+y,1)])
    return pts
LAND=np.array([c=='1' for c in I['LAND']]).reshape(I['gh'],I['gw']);C=I['cell']
bad=[]
for i in inst:
    i['fp']=fpw(i)
    for x,y in i['fp']:
        if not (0<=int(y)//C<I['gh'] and 0<=int(x)//C<I['gw']) or not LAND[int(y)//C,int(x)//C]:bad.append((i['p'],x,y))
print('footprint corners on sea:',bad)
# v0.14 packer: pull each building toward its district centre by K, then nudge to the nearest clear spot on land
landpoly=unary_union([Polygon(p).buffer(0) for p in I['land']]).buffer(-36)
placed=[]
import math
for idx,i in enumerate(inst):
    c=DC[DIS[idx]];fp=fpw(i);fx=sum(p[0] for p in fp)/len(fp);fy=sum(p[1] for p in fp)/len(fp)
    tx,ty=c[0]+(fx-c[0])*K,c[1]+(fy-c[1])*K;i['x']+=tx-fx;i['y']+=ty-fy
    best=None
    for r in range(0,520,10):
        for k in range(max(1,int(2*math.pi*r/14))):
            a_=k/max(1,int(2*math.pi*r/14))*2*math.pi;dx,dy=r*math.cos(a_),r*math.sin(a_)*.6
            P=Polygon([(x+dx,y+dy) for x,y in fpw(i)]);G=P.buffer(22)
            if landpoly.contains(P) and all(not G.intersects(q) for q in placed):best=(dx,dy,G);break
        if best:break
    if not best:print('NO SPOT',i['p']);continue
    i['x']=round(i['x']+best[0],1);i['y']=round(i['y']+best[1],1);placed.append(best[2])
    if abs(best[0])+abs(best[1])>0:print('nudged',i['p'],round(best[0]),round(best[1]))
for i in inst:i['fp']=fpw(i)

# plazas: iso diamonds around each cluster (uv space = brick lattice)
def uv(x,y):return (x/TW+y/TH, y/TH-x/TW)
def xy(u,v):return ((u-v)*TW/2,(u+v)*TH/2)
def plaza(ids,margin,kind):
    pts=[p for i in inst if i['p']+str(i['x']) in ids for p in i['fp']]
    U_=[uv(*p) for p in pts];u0=min(a for a,b in U_)-margin;u1=max(a for a,b in U_)+margin;v0=min(b for a,b in U_)-margin;v1=max(b for a,b in U_)+margin
    return dict(kind=kind,p=[list(map(lambda t:round(t,1),xy(*c))) for c in [(u0,v0),(u1,v0),(u1,v1),(u0,v1)]])
key=lambda i:i['p']+str(i['x'])
grp={'Market':[key(i) for i in inst[:9]],'University':[key(i) for i in inst[9:14]],'Pier':[key(i) for i in inst[14:18]]}
plazas=[plaza(grp['Market'][:5],3,'brick'),plaza(grp['Market'][5:8],3,'brick'),plaza(grp['University'][:3],3,'flag'),plaza(grp['University'][3:4],2,'flag'),plaza(grp['Pier'][:2],3,'deck'),plaza(grp['Pier'][2:],3,'deck')]
lob=I['districts']['Lobby'];plazas.append(dict(kind='brick',p=[list(xy(*c)) for c in [(uv(*lob)[0]-12,uv(*lob)[1]-12),(uv(*lob)[0]+12,uv(*lob)[1]-12),(uv(*lob)[0]+12,uv(*lob)[1]+12),(uv(*lob)[0]-12,uv(*lob)[1]+12)]]))
I.update(props=inst,plazas=plazas)
json.dump(I,open('isle_world.json','w'))
# preview
m=cv2.imread('isle_map.jpg');S=I['S'];vis=cv2.resize(m,(m.shape[1]*2,m.shape[0]*2))
for pz in plazas:cv2.polylines(vis,[(np.array(pz['p'])/S*2).astype(np.int32)],True,(0,200,255),2)
for i in inst:cv2.polylines(vis,[(np.array(i['fp'])/S*2).astype(np.int32)],True,(255,0,255),2)
cv2.imwrite('place_vis.jpg',vis)
