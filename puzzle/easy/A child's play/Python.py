w,h=map(int,input().split())
n=int(input())
grid=[list(input()) for _ in range(h)]
dirs=[(0,-1),(1,0),(0,1),(-1,0)]
for y,row in enumerate(grid):
    if 'O' in row:
        x,y0=row.index('O'),y
        break
d=0
seen={}
steps=0
while steps<n:
    state=(x,y0,d)
    if state in seen:
        cycle_len=steps-seen[state][0]
        rem=(n-steps)%cycle_len
        x,y0,d=seen[state][1]
        n=steps+rem
    else:
        seen[state]=(steps,(x,y0,d))
    nx,ny=x+dirs[d][0],y0+dirs[d][1]
    while grid[ny][nx]=='#':
        d=(d+1)%4
        nx,ny=x+dirs[d][0],y0+dirs[d][1]
    x,y0=nx,ny
    steps+=1
print(x,y0)
