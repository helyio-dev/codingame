import sys

n = int(sys.stdin.readline())
original_lines = [sys.stdin.readline().rstrip('\n') for _ in range(n)]

pattern_cells = set()
for r in range(n):
    for c in range(len(original_lines[r])):
        if original_lines[r][c] != ' ':
            pattern_cells.add((r, c, original_lines[r][c]))

grid = {}

for r, c, char in pattern_cells:
    grid[(r, c)] = char

for r, c, char in pattern_cells:
    if (r + 1, c + 1) not in grid:
        grid[(r + 1, c + 1)] = '-'

for r, c, char in pattern_cells:
    if (r + 2, c + 2) not in grid:
        grid[(r + 2, c + 2)] = '`'

if not grid:
    sys.exit()

max_r = max(r for r, c in grid.keys())
max_c = max(c for r, c in grid.keys())

for r in range(max_r + 1):
    row = []
    for c in range(max_c + 1):
        row.append(grid.get((r, c), ' '))
    print("".join(row).rstrip())