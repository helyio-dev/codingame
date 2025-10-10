from collections import deque

def bfs(start, end, grid, W, H):
    queue = deque([(start[0], start[1], [start])])
    visited = set([start])
    while queue:
        x, y, path = queue.popleft()
        if (x, y) == end:
            return path
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H and grid[ny][nx] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, path + [(nx, ny)]))
    return []

W = int(input())
H = int(input())
xBase = int(input())
yBase = int(input())
E = int(input())
nbDeliveries = int(input())
deliveries = [tuple(map(int, input().split())) for _ in range(nbDeliveries)]
grid = [list(input()) for _ in range(H)]

current = (xBase, yBase)
unvisited = deliveries.copy()
route = [current]

while unvisited:
    nearest = min(unvisited, key=lambda d: abs(d[0]-current[0]) + abs(d[1]-current[1]))
    path = bfs(current, nearest, grid, W, H)
    if path:
        route += path[1:]
        current = nearest
    unvisited.remove(nearest)

path_back = bfs(current, (xBase, yBase), grid, W, H)
if path_back:
    route += path_back[1:]

if len(route) - 1 > E:
    route = route[:E+1]

for x, y in route:
    print(x, y)
