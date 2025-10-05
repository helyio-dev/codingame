import sys
import math

def char_to_radius(c):
    if '0' <= c <= '9':
        return int(c)
    elif 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 10
    return 0

def brightness_to_char(b):
    if b < 0:
        b = 0
    if b <= 9:
        return str(b)
    elif b <= 35:
        return chr(ord('A') + b - 10)
    else:
        return 'Z'

def solve():
    try:
        data = sys.stdin.read().splitlines()
    except:
        return

    if not data:
        return

    h = int(data[0])
    w = int(data[1])
    grid = data[2:]

    sources = []
    for r in range(h):
        for c in range(w):
            char = grid[r][c]
            if char != '.':
                radius = char_to_radius(char)
                if radius > 0:
                    sources.append((r, c, radius))

    total_brightness = [[0 for _ in range(w)] for _ in range(h)]

    for target_r in range(h):
        for target_c in range(w):
            current_brightness = 0
            
            for source_r, source_c, radius in sources:
                d_sq = (source_r - target_r)**2 + (source_c - target_c)**2
                d = int(round(math.sqrt(d_sq)))
                
                brightness = radius - d
                
                if brightness > 0:
                    current_brightness += brightness
            
            total_brightness[target_r][target_c] = current_brightness

    output = []
    for r in range(h):
        row_output = ""
        for c in range(w):
            b = total_brightness[r][c]
            row_output += brightness_to_char(b)
        output.append(row_output)

    sys.stdout.write('\n'.join(output) + '\n')

solve()