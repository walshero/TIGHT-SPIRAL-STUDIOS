import json
from itertools import combinations
I=json.load(open('isle_world.json'))
TW,TH=25.0,10.4
def uv(x,y):return (x/TW+y/TH, y/TH-x/TW)
def xy(u,v):return ((u-v)*TW/2,(u+v)*TH/2)
G={'pagoda':('brick',4),'lampM1':('brick',2),'cartM':('brick',2),'crates':('brick',3),'board':('brick',2),'train':('brick',3),'emptyH':('brick',3),'lampS2':('brick',2),'treeS':(None,0),
'news':('flag',3),'planter':('flag',2),'clock':('flag',4),'glyphs':('flag',4),'aquarium':('deck',3),'iowcart':('deck',3),'fishhouse':('deck',4),'bucket':('deck',1),'lampX':(None,0),'treeX1':(None,0),'treeX2':(None,0),'maildrop':('brick',2),'loteria':('brick',2),'bedR1':(None,0),'bedR2':(None,0),'bedL1':(None,0),'bedL2':(None,0)}
plz=[]
for i in I['props']:
    kind,m=G[i['p']]
    if i['p']=='lampM1': kind='flag' if i.get('flip') else 'brick'
    if not kind:continue
    U=[uv(*p) for p in i['fp']];u0=min(a for a,b in U)-m;u1=max(a for a,b in U)+m;v0=min(b for a,b in U)-m;v1=max(b for a,b in U)+m
    plz.append(dict(kind=kind,p=[[round(c,1) for c in xy(*q)] for q in [(u0,v0),(u1,v0),(u1,v1),(u0,v1)]]))
DC=I['districts'];DC['University']=[DC['University'][0]+102,DC['University'][1]+12];DC['Pier']=[DC['Pier'][0]+126,DC['Pier'][1]-30]
for name,kind,r in [('Market','brick',10),('University','flag',9),('Pier','deck',8),('Lobby','brick',7)]:
    u,v=uv(*DC[name]);plz.append(dict(kind=kind,p=[[round(t,1) for t in xy(*q)] for q in [(u-r,v-r),(u+r,v-r),(u+r,v+r),(u-r,v+r)]]))
I['plazas']=plz;json.dump(I,open('isle_world.json','w'))
def bb(p):xs=[a for a,b in p];ys=[b for a,b in p];return min(xs),min(ys),max(xs),max(ys)
ov=[(a['p'],b['p']) for a,b in combinations(I['props'],2) if (lambda A,B:A[0]<B[2] and B[0]<A[2] and A[1]<B[3] and B[1]<A[3])(bb(a['fp']),bb(b['fp']))]
print('overlaps',ov)
