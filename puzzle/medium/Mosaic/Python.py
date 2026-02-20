import sys

def solve():
    line = sys.stdin.readline()
    if not line: return
    n = int(line)
    grid = [sys.stdin.readline().strip() for _ in range(n)]
    
    board = [[-1] * n for _ in range(n)]
    
    constraints = []
    for r in range(n):
        for c in range(n):
            if grid[r][c] != '.':
                cells = []
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if 0 <= r+dr < n and 0 <= c+dc < n:
                            cells.append((r+dr, c+dc))
                constraints.append((int(grid[r][c]), cells))

    def update():
        changed = True
        while changed:
            changed = False
            for target, cells in constraints:
                filled = sum(1 for r, c in cells if board[r][c] == 1)
                empty = sum(1 for r, c in cells if board[r][c] == 0)
                unknown = [ (r, c) for r, c in cells if board[r][c] == -1 ]
                
                if unknown:
                    if filled == target:
                        for r, c in unknown:
                            board[r][c] = 0
                            changed = True
                    elif filled + len(unknown) == target:
                        for r, c in unknown:
                            board[r][c] = 1
                            changed = True
                
                if filled > target or filled + len(unknown) < target:
                    return False
        return True

    def backtrack():
        if not update(): return False
        
        best_cell = None
        min_unknown = 10
        
        for r in range(n):
            for c in range(n):
                if board[r][c] == -1:
                    best_cell = (r, c)
                    break
            if best_cell: break
            
        if not best_cell: return True
        
        r, c = best_cell
        old_board = [row[:] for row in board]
        
        board[r][c] = 1
        if backtrack(): return True
        
        for i in range(n): board[i] = old_board[i][:]
        
        board[r][c] = 0
        if backtrack(): return True
        
        return False

    backtrack()
    for row in board:
        print("".join('#' if x == 1 else '.' for x in row))

if __name__ == "__main__":
    solve()