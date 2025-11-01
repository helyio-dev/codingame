size=int(input())
grid=[list(input()) for _ in range(size)]
words=input().split()
found=[[False]*size for _ in range(size)]

dirs=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def in_grid(r,c):
    return 0<=r<size and 0<=c<size

for r in range(size):
    for c in range(size):
        for dr,dc in dirs:
            for w in words:
                L=len(w)
                if all(in_grid(r+dr*i,c+dc*i) and grid[r+dr*i][c+dc*i]==w[i].upper() for i in range(L)):
                    for i in range(L):
                        found[r+dr*i][c+dc*i]=True

for r in range(size):
    print(''.join(grid[r][c] if found[r][c] else ' ' for c in range(size)))
