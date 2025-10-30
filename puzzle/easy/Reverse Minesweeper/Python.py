w = int(input())
h = int(input())
grid = [list(input()) for _ in range(h)]

res = [['.' for _ in range(w)] for _ in range(h)]
dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

for y in range(h):
    for x in range(w):
        if grid[y][x] == 'x':
            for dy, dx in dirs:
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] != 'x':
                    res[ny][nx] = str(int(res[ny][nx]) + 1) if res[ny][nx].isdigit() else '1'

for row in res:
    print(''.join(row))
