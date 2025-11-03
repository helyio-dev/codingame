from collections import deque
from itertools import product

n=int(input())
sizes=list(map(int,input().split(',')))
start=tuple(map(int,input().split(',')))
end=tuple(map(int,input().split(',')))
b=int(input())
blocked=set()
for _ in range(b):
    a,bb=input().split()
    c1=tuple(map(int,a.split(',')))
    c2=tuple(map(int,bb.split(',')))
    ranges=[range(c1[i],c2[i]+1) for i in range(n)]
    for cell in product(*ranges):blocked.add(cell)
if start==end:print(0);exit()
q=deque([(start,0)])
seen={start}
dirs=[]
for i in range(n):
    d=[0]*n;d[i]=1;dirs.append(tuple(d))
    d[i]=-1;dirs.append(tuple(d))
while q:
    pos,dist=q.popleft()
    for d in dirs:
        nxt=tuple(pos[i]+d[i] for i in range(n))
        if any(nxt[i]<0 or nxt[i]>=sizes[i] for i in range(n)):continue
        if nxt in blocked or nxt in seen:continue
        if nxt==end:print(dist+1);exit()
        seen.add(nxt)
        q.append((nxt,dist+1))
print("NO PATH")
