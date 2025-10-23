from math import floor
W,H,t1,t2,t3=map(int,input().split())
p1,p2={},{}
for y in range(H):
    a,b=input().split()
    for x,c in enumerate(a): 
        if c!='.': p1[c]=(x,y)
    for x,c in enumerate(b): 
        if c!='.': p2[c]=(x,y)
res=[['.']*W for _ in range(H)]
for k in p1:
    x1,y1=p1[k]
    x2,y2=p2[k]
    x3=floor(x1+(x2-x1)*(t3-t1)/(t2-t1))
    y3=floor(y1+(y2-y1)*(t3-t1)/(t2-t1))
    if 0<=x3<W and 0<=y3<H:
        if res[y3][x3]=='.' or k<res[y3][x3]: res[y3][x3]=k
for r in res: print(''.join(r))
