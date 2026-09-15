from collections import deque

w, h = map(int, input().split())
k = int(input())

grid = [[" " for _ in range(w)] for _ in range(h)]

grid[0][0] = "#"
grid[h - 1][w - 1] = "#"


def bfs(i, j):
    queue = deque([(i, j)])
    seen = {(i, j)}

    while queue:
        y, x = queue.popleft()

        if y == h - 1 and x == w - 1:
            return True

        for dy, dx in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            ny = y + dy
            nx = x + dx

            if (
                0 <= ny < h
                and 0 <= nx < w
                and grid[ny][nx] == "#"
                and (ny, nx) not in seen
            ):
                seen.add((ny, nx))
                queue.append((ny, nx))

    return False


moves = 0

for _ in range(k):
    x, y = map(int, input().split())

    grid[y][x] = "#"
    moves += 1

    if bfs(0, 0):
        break

print(moves)