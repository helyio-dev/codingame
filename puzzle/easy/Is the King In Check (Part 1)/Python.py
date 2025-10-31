board = [input().split() for _ in range(8)]
kx = ky = px = py = 0
piece = ""
for y in range(8):
    for x in range(8):
        if board[y][x] == "K":
            kx, ky = x, y
        elif board[y][x] != "_":
            px, py, piece = x, y, board[y][x]

check = False
dx, dy = kx - px, ky - py
adx, ady = abs(dx), abs(dy)

if piece == "R":
    check = (dx == 0 or dy == 0)
elif piece == "B":
    check = adx == ady
elif piece == "Q":
    check = (dx == 0 or dy == 0 or adx == ady)
elif piece == "N":
    check = (adx, ady) in [(1, 2), (2, 1)]

print("Check" if check else "No Check")
