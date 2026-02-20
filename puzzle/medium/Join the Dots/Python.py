import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    h, w = map(int, input_data[0].split())
    grid_input = input_data[1:]
    
    dots = {}
    for r in range(h):
        for c in range(w):
            char = grid_input[r][c]
            if char != '.':
                if '1' <= char <= '9':
                    val = int(char)
                else:
                    val = ord(char) - ord('A') + 10
                dots[val] = (r, c)
    
    sorted_keys = sorted(dots.keys())
    board = [[' ' for _ in range(w)] for _ in range(h)]
    
    lines_per_cell = [[set() for _ in range(w)] for _ in range(h)]

    for i in range(len(sorted_keys) - 1):
        r1, c1 = dots[sorted_keys[i]]
        r2, c2 = dots[sorted_keys[i+1]]
        
        dr = 0 if r1 == r2 else (1 if r2 > r1 else -1)
        dc = 0 if c1 == c2 else (1 if c2 > c1 else -1)
        
        char = ''
        if dr == 0: char = '-'
        elif dc == 0: char = '|'
        elif dr == dc: char = '\\'
        else: char = '/'
        
        curr_r, curr_c = r1 + dr, c1 + dc
        while (curr_r, curr_c) != (r2, c2):
            lines_per_cell[curr_r][curr_c].add(char)
            curr_r += dr
            curr_c += dc

    for r, c in dots.values():
        board[r][c] = 'o'

    for r in range(h):
        for c in range(w):
            if board[r][c] == 'o':
                continue
                
            chars = lines_per_cell[r][c]
            if not chars:
                continue
            
            if len(chars) == 1:
                board[r][c] = list(chars)[0]
            elif len(chars) == 2:
                if '-' in chars and '|' in chars:
                    board[r][c] = '+'
                elif '/' in chars and '\\' in chars:
                    board[r][c] = 'X'
                else:
                    board[r][c] = '*'
            else:
                board[r][c] = '*'

    for row in board:
        print("".join(row).rstrip())

if __name__ == "__main__":
    solve()