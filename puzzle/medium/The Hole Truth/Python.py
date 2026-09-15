from collections import deque

grid = []
w, h = [int(i) for i in input().split()]
for i in range(h):
    grid.append(list(input()))

total_holes = 0
for i, row in enumerate(grid):
    for j, char in enumerate(row):
        if char != ".":
            continue
        
        queue = deque([(i,j)])
        hole = True
        while queue:
            y, x = queue.popleft()

            if y == 0 or y == h - 1 or x == 0 or x == w - 1:
                hole = False

            for dy, dx in [[0,1],[-1,0],[0,-1],[1,0]]:
                ny, nx = y + dy, x + dx

                if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == ".":
                    grid[ny][nx] = "#"
                    queue.append((ny, nx))

        if hole:
            total_holes += 1

print(total_holes)