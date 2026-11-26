import cv2,numpy as np,json,heapq
S=3  # world px per map px (v0.14: was 5; founder took the 40% shrink)
m=cv2.imread('isle_map.jpg');H,W=m.shape[:2]
hsv=cv2.cvtColor(m,cv2.COLOR_BGR2HSV)
sea=((hsv[...,0]>=85)&(hsv[...,0]<=112)&(hsv[...,1]>90))|(hsv[...,2]<40)
land=(~sea).astype(np.uint8)
land=cv2.morphologyEx(land,cv2.MORPH_OPEN,np.ones((3,3),np.uint8));land=cv2.morphologyEx(land,cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
n,lab,st,_=cv2.connectedComponentsWithStats(land);keep=[i for i in range(1,n) if st[i,4]>400]
land=np.isin(lab,keep).astype(np.uint8)
# fill bay-side holes in land (lakes inside land) except real bay (huge)
inv=(1-land);n2,lab2,st2,_=cv2.connectedComponentsWithStats(inv)
for i in range(1,n2):
    x,y,w,h,a=st2[i]
    if a<1500 and x>0 and y>0 and x+w<W and y+h<H:land[lab2==i]=1
cv2.imwrite('land_map.png',land*255)
# upscale to world grid at 8px cells
CELL=8;GW,GH=W*S//CELL,H*S//CELL
L=cv2.resize(land.astype(np.float32),(GW,GH),interpolation=cv2.INTER_LINEAR)
L=(cv2.GaussianBlur(L,(0,0),2.5)>0.5).astype(np.uint8)
def contours(mask,scale,eps=1.2,minA=50):
    cs,_=cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE);out=[]
    for c in cs:
        if cv2.contourArea(c)<minA:continue
        c=cv2.approxPolyDP(c,eps,True)[:,0,:].astype(float)
        # chaikin smoothing x2
        for _ in range(2):
            q=np.roll(c,-1,0);c=np.vstack([np.c_[0.75*c[:,0]+0.25*q[:,0],0.75*c[:,1]+0.25*q[:,1]],np.c_[0.25*c[:,0]+0.75*q[:,0],0.25*c[:,1]+0.75*q[:,1]]]).reshape(2,-1,2).transpose(1,0,2).reshape(-1,2)
        out.append([[round(x*scale+scale/2),round(y*scale+scale/2)] for x,y in c])
    return out
landP=contours(L,CELL)
grass=cv2.erode(L,np.ones((7,7),np.uint8));grassP=contours(grass,CELL)
D={'University':(186,118),'Lobby':(330,190),'Market':(547,180),'Pier':(118,292),'Palace gardens':(568,328),'Windmill Hill':(292,48)}  # v0.14: districts spread to use the NE lobe and the south peninsula
DW={k:[x*S,y*S] for k,(x,y) in D.items()}
for k,(x,y) in DW.items():print(k,x,y,'land' if L[y//CELL,x//CELL] else 'SEA')
# roads: A* on land grid preferring distance from shore
dist=cv2.distanceTransform(L,cv2.DIST_L2,5)
cost=np.where(L>0,1+12/(1+dist),1e9)
def astar(a,b):
    a=(a[1]//CELL,a[0]//CELL);b=(b[1]//CELL,b[0]//CELL);g={a:0};pq=[(0,a)];prev={}
    while pq:
        _,u=heapq.heappop(pq)
        if u==b:break
        for dy,dx in((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
            v=(u[0]+dy,u[1]+dx)
            if not(0<=v[0]<GH and 0<=v[1]<GW) or cost[v]>=1e9:continue
            nd=g[u]+cost[v]*(1.414 if dy and dx else 1)
            if nd<g.get(v,1e18):g[v]=nd;prev[v]=u;heapq.heappush(pq,(nd+abs(v[0]-b[0])+abs(v[1]-b[1]),v))
    p=[b]
    while p[-1]!=a:p.append(prev[p[-1]])
    p=p[::-1];pts=np.array([[x*CELL+CELL/2,y*CELL+CELL/2] for y,x in p],np.float32)
    pts=cv2.approxPolyDP(pts.reshape(-1,1,2),10,False)[:,0,:]
    for _ in range(3):
        q=pts;n=[q[0]]
        for i in range(len(q)-1):n+= [0.75*q[i]+0.25*q[i+1],0.25*q[i]+0.75*q[i+1]]
        n.append(q[-1]);pts=np.array(n)
    return [[round(float(x)),round(float(y))] for x,y in pts]
R=[('Pier','University'),('University','Lobby'),('Lobby','Market'),('Market','Palace gardens'),('University','Windmill Hill'),('Lobby','Pier')]
roads=[astar(DW[a],DW[b]) for a,b in R]
json.dump({'S':S,'W':W*S,'H':H*S,'cell':CELL,'gw':GW,'gh':GH,'land':landP,'grass':grassP,'districts':DW,'roads':roads,
  'LAND':''.join('1' if v else '0' for v in L.ravel())},open('isle.json','w'))
vis=cv2.resize(m,(W*2,H*2));
for P in landP:cv2.polylines(vis,[(np.array(P)/S*2).astype(np.int32)],True,(0,255,255),1)
for r in roads:cv2.polylines(vis,[(np.array(r)/S*2).astype(np.int32)],False,(0,0,255),2)
for k,(x,y) in DW.items():cv2.circle(vis,(x*2//S,y*2//S),6,(255,0,255),-1);cv2.putText(vis,k,(x*2//S+8,y*2//S),0,0.5,(255,255,255),2)
cv2.imwrite('layout_vis.jpg',vis);print('world',W*S,H*S,'land polys',len(landP))
