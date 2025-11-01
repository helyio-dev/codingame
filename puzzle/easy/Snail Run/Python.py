from collections import deque

n = int(input())
speeds = [int(input()) for _ in range(n)]
h = int(input())
w = int(input())
grid = [list(input().strip()) for _ in range(h)]
snails = {}
for i in range(h):
    for j in range(w):
        c = grid[i][j]
        if c.isdigit():
            snails[int(c)] = (i, j)
for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            goal = (i, j)
            break
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(start):
    q = deque([(start[0], start[1], 0)])
    seen = {start}
    while q:
        x,y,d = q.popleft()
        if (x,y)==goal:
            return d
        for dx,dy in dirs:
            nx,ny=x+dx,y+dy
            if 0<=nx<h and 0<=ny<w and grid[nx][ny] in ('*','#') and (nx,ny) not in seen:
                seen.add((nx,ny))
                q.append((nx,ny,d+1))
times=[]
for i in range(1,n+1):
    d=bfs(snails[i])
    t=d/speeds[i-1]
    times.append((t,i))
times.sort()
print(times[0][1])
