from collections import deque
n=int(input())
v=int(input())
m=int(input())
g=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    g[a].append(b);g[b].append(a)
def spread(block):
    seen={v}
    q=deque([v])
    while q:
        x=q.popleft()
        for y in g[x]:
            if y not in seen and y!=block:
                seen.add(y);q.append(y)
    return len(seen)
best,ans=n+1,0
for i in range(n):
    if i==v:continue
    s=spread(i)
    if s<best:best,ans=s,i
print(ans)
