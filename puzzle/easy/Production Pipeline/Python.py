from heapq import heappush, heappop
N=int(input())
K=int(input())
g=[[] for _ in range(N+1)]
deg=[0]*(N+1)
for _ in range(K):
    a,b=map(int,input().split('<'))
    g[a].append(b)
    deg[b]+=1
h=[]
for i in range(1,N+1):
    if deg[i]==0:heappush(h,i)
res=[]
while h:
    x=heappop(h)
    res.append(x)
    for y in g[x]:
        deg[y]-=1
        if deg[y]==0:heappush(h,y)
print("INVALID" if len(res)<N else ' '.join(map(str,res)))
