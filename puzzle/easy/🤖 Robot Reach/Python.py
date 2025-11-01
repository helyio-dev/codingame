from collections import deque
R=int(input())
C=int(input())
T=int(input())
def s(x):return sum(map(int,str(x)))
v=[[0]*C for _ in range(R)]
q=deque([(0,0)])
v[0][0]=1 if s(0)+s(0)<=T else 0
c=0
while q:
    x,y=q.popleft()
    if s(x)+s(y)>T or v[x][y]==2:continue
    v[x][y]=2;c+=1
    for dx,dy in[(1,0),(-1,0),(0,1),(0,-1)]:
        nx,ny=x+dx,y+dy
        if 0<=nx<R and 0<=ny<C and not v[nx][ny] and s(nx)+s(ny)<=T:
            v[nx][ny]=1;q.append((nx,ny))
print(c)
