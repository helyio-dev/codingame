w, h = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]

def good_rectangles(r0, c0, n):
    res = []
    for height in range(1, n+1):
        if n % height != 0:
            continue
        width = n // height
        for r in range(max(0, r0-height+1), min(h-height+1, r0+1)):
            for c in range(max(0, c0-width+1), min(w-width+1, c0+1)):
                ok = True
                for i in range(r, r+height):
                    for j in range(c, c+width):
                        if grid[i][j] > 0 and (i != r0 or j != c0):
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    res.append((r, c, width, height))
    return sorted(res)

for r in range(h):
    for c in range(w):
        if grid[r][c] > 0:
            n = grid[r][c]
            rects = good_rectangles(r, c, n)
            if rects:
                print(f"{r} {c} {n}")
                for rect in rects:
                    print(f"{rect[0]} {rect[1]} {rect[2]} {rect[3]}")
