def h(c):
    if '0' <= c <= '9':
        return int(c)
    elif 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 10
    return 0

def g(v):
    if 0 <= v <= 9:
        return str(v)
    elif 10 <= v <= 35:
        return chr(ord('A') + v - 10)
    else:
        return 'Z'

def f():
    l = int(input())
    w = int(input())
    d = int(input())
    n = int(input())
    
    grid = [input() for _ in range(n)]
    
    sources = []
    
    for z in range(d):
        for y in range(w):
            for x in range(l):
                char = grid[z * (w + 1) + y][x]
                if char != '.':
                    radius = h(char)
                    sources.append((x, y, z, radius))
    
    output_grid = []
    
    for z_target in range(d):
        for y_target in range(w):
            row = ""
            for x_target in range(l):
                total_brightness = 0
                for x_source, y_source, z_source, radius in sources:
                    distance = ((x_target - x_source)**2 + (y_target - y_source)**2 + (z_target - z_source)**2)**0.5
                    brightness = radius - round(distance)
                    if brightness > 0:
                        total_brightness += brightness
                row += g(total_brightness)
            output_grid.append(row)
        if z_target < d - 1:
            output_grid.append("")

    for line in output_grid:
        print(line)

f()