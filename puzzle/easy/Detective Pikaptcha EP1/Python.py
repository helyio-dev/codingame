w, h = map(int, input().split())
grid = [list(input()) for _ in range(h)]
res = [["#"] * w for _ in range(h)]
for y in range(h):
    for x in range(w):
        if grid[y][x] == "0":
            c = 0
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < w and 0 <= ny < h and grid[ny][nx] == "0":
                    c += 1
            res[y][x] = str(c)
for r in res:
    print("".join(r))
