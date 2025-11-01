from itertools import product
from math import comb

H,W,N=map(int,input().split())

Ls=[]
base=[(0,0),(0,1),(1,0),(2,0)]
for flip in [1,-1]:
    for rot in range(4):
        shape=[]
        for x,y in base:
            for _ in range(rot):
                x,y=y,-x
            shape.append((x*flip,y))
        minx=min(x for x,y in shape)
        miny=min(y for x,y in shape)
        shape=[(x-minx,y-miny) for x,y in shape]
        if shape not in Ls:
            Ls.append(shape)

def fits(L):
    masks=[]
    for x0 in range(H):
        for y0 in range(W):
            mask=0
            ok=True
            for dx,dy in L:
                xi,yi=x0+dx,y0+dy
                if xi<0 or xi>=H or yi<0 or yi>=W:
                    ok=False
                    break
                mask|=1<<(xi*W+yi)
            if ok:
                masks.append(mask)
    return masks

L_masks=[]
for L in Ls:
    L_masks+=fits(L)

configs=0
for r,b in product(L_masks,L_masks):
    if r&b: continue
    free_cells=H*W - bin(r|b).count('1')
    if free_cells>=N:
        configs+=comb(free_cells,N)

print(configs)
