grid = [list(input()) for _ in range(6)]
rows, cols = len(grid), len(grid[0])

player1, player2 = [], []

def check_sequence(seq, coords):
    if seq.count("1") == 3 and seq.count(".") == 1:
        idx = seq.index(".")
        x, y = coords[idx]
        if x == rows - 1 or grid[x + 1][y] != ".":
            player1.append(y)
    elif seq.count("2") == 3 and seq.count(".") == 1:
        idx = seq.index(".")
        x, y = coords[idx]
        if x == rows - 1 or grid[x + 1][y] != ".":
            player2.append(y)

for i in range(rows - 3):
    for j in range(cols):
        seq = [grid[i + k][j] for k in range(4)]
        coords = [(i + k, j) for k in range(4)]
        check_sequence(seq, coords)

for i in range(rows):
    for j in range(cols - 3):
        seq = [grid[i][j + k] for k in range(4)]
        coords = [(i, j + k) for k in range(4)]
        check_sequence(seq, coords)

for i in range(rows - 3):
    for j in range(cols - 3):
        seq = [grid[i + k][j + k] for k in range(4)]
        coords = [(i + k, j + k) for k in range(4)]
        check_sequence(seq, coords)

for i in range(3, rows):
    for j in range(cols - 3):
        seq = [grid[i - k][j + k] for k in range(4)]
        coords = [(i - k, j + k) for k in range(4)]
        check_sequence(seq, coords)

print(*player1 if player1 else ["NONE"])
print(*player2 if player2 else ["NONE"])