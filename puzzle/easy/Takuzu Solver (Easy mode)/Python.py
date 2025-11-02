n = int(input())
board = [list(input()) for _ in range(n)]

def is_valid(r, c, val):
    if c >= 2 and board[r][c-1] == board[r][c-2] == val:
        return False
    if c >= 1 and c + 1 < n and board[r][c-1] == board[r][c+1] == val:
        return False
    if c + 2 < n and board[r][c+1] == board[r][c+2] == val:
        return False
    if r >= 2 and board[r-1][c] == board[r-2][c] == val:
        return False
    if r >= 1 and r + 1 < n and board[r-1][c] == board[r+1][c] == val:
        return False
    if r + 2 < n and board[r+1][c] == board[r+2][c] == val:
        return False
    return True

def solve(r=0, c=0):
    if r == n:
        return True
    if c == n:
        return solve(r+1, 0)
    if board[r][c] != '.':
        return solve(r, c+1)
    for val in '01':
        if is_valid(r, c, val):
            board[r][c] = val
            if solve(r, c+1):
                return True
            board[r][c] = '.'
    return False

solve()
for row in board:
    print("".join(row))
