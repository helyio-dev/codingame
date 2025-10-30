h = int(input())
w = int(input())
grid = [input().split() for _ in range(h)]

def dfs(y, x, visited):
    if x == w-1:
        return True
    visited.add((y, x))
    for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
        ny, nx = y+dy, x+dx
        if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == '+' and (ny,nx) not in visited:
            if dfs(ny, nx, visited):
                return True
    return False

count = 0
for y in range(h):
    if grid[y][0] == '+':
        if dfs(y, 0, set()):
            count += 1

print(count)
