W,H=map(int,input().split())
sr,sc=map(int,input().split())
N=int(input())
maps=[]
for _ in range(N):
    grid=[input() for _ in range(H)]
    maps.append(grid)

def path_length(grid):
    r,c=sr,sc
    visited=set()
    steps=0
    while True:
        if not (0<=r<H and 0<=c<W): return None
        if (r,c) in visited: return None
        visited.add((r,c))
        cell=grid[r][c]
        if cell=='T': return steps+1
        if cell=='#' or cell=='.': return None
        steps+=1
        if cell=='^': r-=1
        elif cell=='v': r+=1
        elif cell=='<': c-=1
        elif cell=='>': c+=1
        else: return None

best_len=float('inf')
best_idx=-1
for i,g in enumerate(maps):
    l=path_length(g)
    if l is not None and l<best_len:
        best_len=l
        best_idx=i

print(best_idx if best_idx!=-1 else 'TRAP')
