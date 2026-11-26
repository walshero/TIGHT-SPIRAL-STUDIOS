# v0.19: block every ground cell where a standing avatar would be mostly hidden behind a prop.
import json, base64, numpy as np
from PIL import Image
W=json.load(open('isle_world.json'));P=json.load(open('props.json'))
A=np.array(Image.open('props_atlas.webp').convert('RGBA'))[...,3].astype(np.float32)/255
CELL=8;GW=-(-W['W']//CELL);GH=-(-W['H']//CELL);mask=np.zeros((GH,GW),bool)
AVW,AVH=18,74   # avatar box: 18 wide, from 6 to 80 above the feet
for q in W['props']:
    d=P[q['p']];fp=q['fp'];ox,oy,w,h=q['x'],q['y'],d['w'],d['h'];flip=bool(q.get('flip'))
    spr=A[int(d['ay']):int(d['ay']+d['ah']),int(d['ax']):int(d['ax']+d['aw'])]
    if flip:spr=spr[:,::-1]
    sy=spr.shape[0]/h;sx=spr.shape[1]/w
    # front chain of the footprint (lower boundary from leftmost to rightmost), as in the engine
    L=min(range(len(fp)),key=lambda i:(fp[i][0],-fp[i][1]));R=max(range(len(fp)),key=lambda i:(fp[i][0],fp[i][1]))
    def walk(step):
        out=[fp[L]];i=L
        while i!=R:i=(i+step)%len(fp);out.append(fp[i])
        return out
    a,b=walk(1),walk(-1);front=a if np.mean([p[1] for p in a])>np.mean([p[1] for p in b]) else b
    fx0,fx1=front[0][0],front[-1][0]
    def frontY(x):
        x=max(fx0,min(fx1,x))
        for i in range(1,len(front)):
            if x<=front[i][0]:
                ax,ay=front[i-1];bx,by=front[i];return ay+(by-ay)*((x-ax)/((bx-ax) or 1))
        return front[-1][1]
    for j in range(max(0,int(oy//CELL)),min(GH,int((oy+h+80)//CELL)+1)):
        for i in range(max(0,int((ox-10)//CELL)),min(GW,int((ox+w+10)//CELL)+1)):
            px,py=i*CELL+CELL/2,j*CELL+CELL/2
            if py>=frontY(px):continue
            x0,x1=int((px-AVW/2-ox)*sx),int((px+AVW/2-ox)*sx);y0,y1=int((py-80-oy)*sy),int((py-6-oy)*sy)
            X0,X1,Y0,Y1=max(0,x0),min(spr.shape[1],x1),max(0,y0),min(spr.shape[0],y1)
            if X1<=X0 or Y1<=Y0:continue
            cov=spr[Y0:Y1,X0:X1].sum()/max(1,(x1-x0)*(y1-y0))
            if cov>.45:mask[j,i]=True
bits=np.packbits(mask.ravel());W['hide']=base64.b64encode(bits.tobytes()).decode();W['hideDim']=[GW,GH,CELL]
json.dump(W,open('isle_world.json','w'));print('hidden cells',int(mask.sum()),'of',mask.size)
Image.fromarray((mask*255).astype(np.uint8)).save('/tmp/hide.png')
