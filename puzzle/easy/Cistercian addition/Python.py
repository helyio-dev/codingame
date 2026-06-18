import sys


def parse_symbol(grid):
    lines = [grid[i] + " " * (5 - len(grid[i])) for i in range(5)]

    def has_char(r, c, ch):
        if 0 <= r < len(lines) and 0 <= c < len(lines[r]):
            return lines[r][c] == ch
        return False

    d0, d1, d2, d3 = 0, 0, 0, 0

    if has_char(0, 3, "_") and has_char(1, 3, "_") and has_char(1, 4, "|"):
        d0 = 9
    elif has_char(1, 3, "_") and has_char(1, 4, "|"):
        d0 = 8
    elif has_char(0, 3, "_") and has_char(1, 4, "|"):
        d0 = 7
    elif has_char(1, 4, "|"):
        d0 = 6
    elif has_char(0, 3, "_") and has_char(1, 3, "/"):
        d0 = 5
    elif has_char(1, 3, "/"):
        d0 = 4
    elif has_char(1, 3, "\\"):
        d0 = 3
    elif has_char(1, 3, "_"):
        d0 = 2
    elif has_char(0, 3, "_"):
        d0 = 1

    if has_char(0, 1, "_") and has_char(1, 1, "_") and has_char(1, 0, "|"):
        d1 = 9
    elif has_char(1, 1, "_") and has_char(1, 0, "|"):
        d1 = 8
    elif has_char(0, 1, "_") and has_char(1, 0, "|"):
        d1 = 7
    elif has_char(1, 0, "|"):
        d1 = 6
    elif has_char(0, 1, "_") and has_char(1, 1, "\\"):
        d1 = 5
    elif has_char(1, 1, "\\"):
        d1 = 4
    elif has_char(1, 1, "/"):
        d1 = 3
    elif has_char(1, 1, "_"):
        d1 = 2
    elif has_char(0, 1, "_"):
        d1 = 1

    if has_char(2, 3, "_") and has_char(3, 3, "_") and has_char(3, 4, "|"):
        d2 = 9
    elif has_char(2, 3, "_") and has_char(3, 4, "|"):
        d2 = 8
    elif has_char(3, 3, "_") and has_char(3, 4, "|"):
        d2 = 7
    elif has_char(3, 4, "|"):
        d2 = 6
    elif has_char(3, 3, "\\") and has_char(4, 3, "‾"):
        d2 = 5
    elif has_char(3, 3, "\\"):
        d2 = 4
    elif has_char(3, 3, "/"):
        d2 = 3
    elif has_char(2, 3, "_"):
        d2 = 2
    elif has_char(3, 3, "_"):
        d2 = 1

    if has_char(2, 1, "_") and has_char(3, 1, "_") and has_char(3, 0, "|"):
        d3 = 9
    elif has_char(2, 1, "_") and has_char(3, 0, "|"):
        d3 = 8
    elif has_char(3, 1, "_") and has_char(3, 0, "|"):
        d3 = 7
    elif has_char(3, 0, "|"):
        d3 = 6
    elif has_char(3, 1, "/") and has_char(4, 1, "‾"):
        d3 = 5
    elif has_char(3, 1, "/"):
        d3 = 4
    elif has_char(3, 1, "\\"):
        d3 = 3
    elif has_char(2, 1, "_"):
        d3 = 2
    elif has_char(3, 1, "_"):
        d3 = 1

    return d3 * 1000 + d2 * 100 + d1 * 10 + d0


def render_symbol(val):
    d0 = val % 10
    d1 = (val // 10) % 10
    d2 = (val // 100) % 10
    d3 = (val // 1000) % 10

    grid = [[" " for _ in range(5)] for _ in range(5)]
    for r in range(1, 4):
        grid[r][2] = "|"

    if d0 == 1:
        grid[0][3] = "_"
    elif d0 == 2:
        grid[1][3] = "_"
    elif d0 == 3:
        grid[1][3] = "\\"
    elif d0 == 4:
        grid[1][3] = "/"
    elif d0 == 5:
        grid[0][3] = "_"
        grid[1][3] = "/"
    elif d0 == 6:
        grid[1][4] = "|"
    elif d0 == 7:
        grid[0][3] = "_"
        grid[1][4] = "|"
    elif d0 == 8:
        grid[1][3] = "_"
        grid[1][4] = "|"
    elif d0 == 9:
        grid[0][3] = "_"
        grid[1][3] = "_"
        grid[1][4] = "|"

    if d1 == 1:
        grid[0][1] = "_"
    elif d1 == 2:
        grid[1][1] = "_"
    elif d1 == 3:
        grid[1][1] = "/"
    elif d1 == 4:
        grid[1][1] = "\\"
    elif d1 == 5:
        grid[0][1] = "_"
        grid[1][1] = "\\"
    elif d1 == 6:
        grid[1][0] = "|"
    elif d1 == 7:
        grid[0][1] = "_"
        grid[1][0] = "|"
    elif d1 == 8:
        grid[1][1] = "_"
        grid[1][0] = "|"
    elif d1 == 9:
        grid[0][1] = "_"
        grid[1][1] = "_"
        grid[1][0] = "|"

    if d2 == 1:
        grid[3][3] = "_"
    elif d2 == 2:
        grid[2][3] = "_"
    elif d2 == 3:
        grid[3][3] = "/"
    elif d2 == 4:
        grid[3][3] = "\\"
    elif d2 == 5:
        grid[3][3] = "\\"
        grid[4][3] = "‾"
    elif d2 == 6:
        grid[3][4] = "|"
    elif d2 == 7:
        grid[3][3] = "_"
        grid[3][4] = "|"
    elif d2 == 8:
        grid[2][3] = "_"
        grid[3][4] = "|"
    elif d2 == 9:
        grid[2][3] = "_"
        grid[3][3] = "_"
        grid[3][4] = "|"

    if d3 == 1:
        grid[3][1] = "_"
    elif d3 == 2:
        grid[2][1] = "_"
    elif d3 == 3:
        grid[3][1] = "\\"
    elif d3 == 4:
        grid[3][1] = "/"
    elif d3 == 5:
        grid[3][1] = "/"
        grid[4][1] = "‾"
    elif d3 == 6:
        grid[3][0] = "|"
    elif d3 == 7:
        grid[3][1] = "_"
        grid[3][0] = "|"
    elif d3 == 8:
        grid[2][1] = "_"
        grid[3][0] = "|"
    elif d3 == 9:
        grid[2][1] = "_"
        grid[3][1] = "_"
        grid[3][0] = "|"

    return ["".join(row) for row in grid]


lines = sys.stdin.read().splitlines()
grid_a = lines[:5]
grid_b = lines[5:10]

val_a = parse_symbol(grid_a)
val_b = parse_symbol(grid_b)

total = val_a + val_b
res_grid = render_symbol(total)

for row in res_grid:
    print(row)