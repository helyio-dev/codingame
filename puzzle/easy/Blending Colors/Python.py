import math

S, P = map(int, input().split())
shapes = []
for _ in range(S):
    data = input().split()
    name = data[0]
    x0, y0, length = map(int, data[1:4])
    R, G, B = map(int, data[4:7])
    shapes.append((name, x0, y0, length, R, G, B))

points = [tuple(map(int, input().split())) for _ in range(P)]

def round_up(x):
    return int(x + 0.5)

for px, py in points:
    on_border = False
    inside_colors = []
    for shape in shapes:
        name, x0, y0, length, R, G, B = shape
        if name == "SQUARE":
            x1, y1 = x0, y0
            x2, y2 = x0 + length, y0 + length
            if (px == x1 or px == x2) and y1 <= py <= y2 or (py == y1 or py == y2) and x1 <= px <= x2:
                on_border = True
                break
            if x1 < px < x2 and y1 < py < y2:
                inside_colors.append((R, G, B))
        else:
            dx = px - x0
            dy = py - y0
            dist_sq = dx*dx + dy*dy
            r_sq = length*length
            if dist_sq == r_sq:
                on_border = True
                break
            if dist_sq < r_sq:
                inside_colors.append((R, G, B))
    if on_border:
        print("(0, 0, 0)")
    elif inside_colors:
        R_avg = round_up(sum(c[0] for c in inside_colors)/len(inside_colors))
        G_avg = round_up(sum(c[1] for c in inside_colors)/len(inside_colors))
        B_avg = round_up(sum(c[2] for c in inside_colors)/len(inside_colors))
        print(f"({R_avg}, {G_avg}, {B_avg})")
    else:
        print("(255, 255, 255)")
