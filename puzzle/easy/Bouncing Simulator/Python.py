import sys

line1 = sys.stdin.readline().split()
line2 = sys.stdin.readline().split()
line3 = sys.stdin.readline().split()

if not line1 or not line2 or not line3:
    sys.exit()

w = int(line1[0])
h = int(line2[0])
n = int(line3[0])

grid = [[0 for _ in range(w)] for _ in range(h)]

x, y = 0, 0
dx, dy = 1, 1
hits = 0

grid[y][x] += 1

while hits < n:
    nx, ny = x + dx, y + dy
    hit_x = False
    hit_y = False

    if nx < 0 or nx >= w:
        hit_x = True
    if ny < 0 or ny >= h:
        hit_y = True

    if hit_x or hit_y:
        hits += 1
        if hit_x: dx *= -1
        if hit_y: dy *= -1
        
        if hits == n:
            break

    x += dx
    y += dy
    grid[y][x] += 1

print('#' * (w + 2))
for row in grid:
    line = '#'
    for cell in row:
        line += str(cell) if cell > 0 else ' '
    line += '#'
    print(line)
print('#' * (w + 2))