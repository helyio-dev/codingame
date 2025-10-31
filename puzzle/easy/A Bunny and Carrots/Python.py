M, N = map(int, input().split())
T = int(input())
choices = list(map(int, input().split()))

grid = [[1]*N for _ in range(M)]

def perimeter(g):
    p = 0
    for y in range(M):
        for x in range(N):
            if g[y][x] == 1:
                if y == 0 or g[y-1][x] == 0:
                    p += 1
                if y == M-1 or g[y+1][x] == 0:
                    p += 1
                if x == 0 or g[y][x-1] == 0:
                    p += 1
                if x == N-1 or g[y][x+1] == 0:
                    p += 1
    return p

for c in choices:
    col = c - 1
    for row in range(M):
        if grid[row][col] == 1:
            grid[row][col] = 0
            break
    print(perimeter(grid))
