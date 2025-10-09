from collections import deque

n = int(input())
grid = [list(input().strip()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def neighbors(x, y):
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n:
            yield nx, ny

islands = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == '#' and not visited[i][j]:
            q = deque([(i,j)])
            visited[i][j] = True
            water = set()
            while q:
                x, y = q.popleft()
                for nx, ny in neighbors(x, y):
                    if grid[nx][ny] == '~':
                        water.add((nx, ny))
                    elif grid[nx][ny] == '#' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
            islands.append(len(water))

max_coast = max(islands)
idx = islands.index(max_coast)+1
print(f"{idx} {max_coast}")
