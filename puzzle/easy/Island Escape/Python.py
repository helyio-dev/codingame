import sys
from collections import deque

N = int(input())
elevation_map = [list(map(int, input().split())) for _ in range(N)]

start_x, start_y = N // 2, N // 2

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_reachable():
    queue = deque([(start_x, start_y)])
    visited = set()
    visited.add((start_x, start_y))

    while queue:
        x, y = queue.popleft()

        if x == 0 or x == N - 1 or y == 0 or y == N - 1:
            return True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                if abs(elevation_map[nx][ny] - elevation_map[x][y]) <= 1:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    return False

if is_reachable():
    print("yes")
else:
    print("no")
