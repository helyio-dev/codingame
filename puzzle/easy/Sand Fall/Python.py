import sys

def solve():
    data = sys.stdin.read().split()
    w = int(data[0])
    h = int(data[1])
    n = int(data[2])
    
    grains_info = []
    for i in range(n):
        s = data[3 + 2 * i]
        p = int(data[4 + 2 * i])
        grains_info.append((s, p))

    grid = [[' ' for _ in range(w)] for _ in range(h)]

    def is_valid(r, c):
        return 0 <= r < h and 0 <= c < w

    def drop_grain(grain_char, start_col):
        r, c = -1, start_col
        
        while True:
            next_r = r + 1
            if not is_valid(next_r, c):
                break 

            moves = []
            if grain_char.islower():
                moves = [(0, 0), (0, 1), (0, -1)] 
            else:
                moves = [(0, 0), (0, -1), (0, 1)] 

            moved = False
            for dr, dc in moves:
                target_r = r + 1 + dr
                target_c = c + dc
                
                if is_valid(target_r, target_c) and grid[target_r][target_c] == ' ':
                    r, c = target_r, target_c
                    moved = True
                    break
            
            if not moved:
                break
        
        if is_valid(r, c):
            grid[r][c] = grain_char

    for grain_char, start_col in grains_info:
        drop_grain(grain_char, start_col)

    output = []
    for row in grid:
        output.append('|' + ''.join(row) + '|')
    
    output.append('+' + '-' * w + '+')

    sys.stdout.write('\n'.join(output) + '\n')

solve()