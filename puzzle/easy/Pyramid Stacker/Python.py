import sys

n, h = map(int, sys.stdin.readline().split())
cubes = sys.stdin.readline().strip()

layers = []
idx = 0

for i in range(h, 0, -1):
    layer_size = i * i
    current_layer_cubes = cubes[idx : idx + layer_size]
    idx += layer_size
    
    grid = [['' for _ in range(i)] for _ in range(i)]
    for k, char in enumerate(current_layer_cubes):
        r, c = divmod(k, i)
        grid[r][c] = char
    
    front_view = []
    if current_layer_cubes:
        for col in range(i):
            visible_char = ""
            for row in range(i - 1, -1, -1):
                if grid[row][col] != '':
                    visible_char = grid[row][col]
                    break
            front_view.append(visible_char if visible_char != "" else " ")
    
    layers.append((i, front_view))

layers.reverse()

for i, (size, view) in enumerate(layers):
    indent = " " * (h - size)
    if not view:
        print("")
        continue
    
    row_str = indent + " ".join(view)
    print(row_str.rstrip())