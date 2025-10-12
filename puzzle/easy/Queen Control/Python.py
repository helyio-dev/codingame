import sys

def solve():
    
    queen_color_str = sys.stdin.readline().strip()
    board = [sys.stdin.readline().strip() for _ in range(8)]

    if queen_color_str == "white":
        queen_color = 'w'
        opponent_color = 'b'
    else:
        queen_color = 'b'
        opponent_color = 'w'

    queen_pos = None
    for r in range(8):
        for c in range(8):
            if board[r][c] == 'Q':
                queen_pos = (r, c)
                break
        if queen_pos:
            break

    if queen_pos is None:
        print(0)
        return

    qr, qc = queen_pos
    controlled_squares = 0

    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    for dr, dc in directions:
        r, c = qr, qc
        while True:
            r += dr
            c += dc

            if not (0 <= r < 8 and 0 <= c < 8):
                break

            piece = board[r][c]

            if piece == '.':
                controlled_squares += 1
                continue

            if piece == queen_color or (piece == 'Q' and (r, c) != (qr, qc)):
                break
            
            if piece == opponent_color:
                controlled_squares += 1
                break

    print(controlled_squares)

if __name__ == "__main__":
    solve()