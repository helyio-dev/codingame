steps = int(input())
h = int(input())
w = int(input())
grid = [list(input().strip()) for _ in range(h)]

for _ in range(steps):
    col_weights = [sum(ord(grid[r][c]) for r in range(h)) for c in range(w)]
    new_grid = [[None]*w for _ in range(h)]
    for c in range(w):
        shift = col_weights[c] % h
        for r in range(h):
            new_grid[(r + shift) % h][c] = grid[r][c]
    grid = new_grid
    row_weights = [sum(ord(ch) for ch in grid[r]) for r in range(h)]
    new_grid = [[None]*w for _ in range(h)]
    for r in range(h):
        shift = row_weights[r] % w
        for c in range(w):
            new_grid[r][(c + shift) % w] = grid[r][c]
    grid = new_grid

for row in grid:
    print("".join(row))
