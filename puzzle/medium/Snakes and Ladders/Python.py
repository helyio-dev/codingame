from collections import deque
w,h=map(int,input().split())
n=int(input())
s,l=map(int,input().split())
m={}
for _ in range(s):
    a,b=map(int,input().split());m[a]=b
for _ in range(l):
    a,b=map(int,input().split());m[b]=a
goal=w*h
q=deque([(1,0)])
v={1}
while q:
    x,d=q.popleft()
    if x==goal:print(d);break
    for i in range(1,n+1):
        y=x+i
        if y>goal:continue
        if y in m:y=m[y]
        if y not in v:
            v.add(y)
            q.append((y,d+1))
