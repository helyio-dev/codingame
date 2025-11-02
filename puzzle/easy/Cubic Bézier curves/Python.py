import math

def interp(p, q, t):
    return (p[0]*(1-t) + q[0]*t, p[1]*(1-t) + q[1]*t)

width, height = map(int, input().split())
steps = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
C = tuple(map(int, input().split()))
D = tuple(map(int, input().split()))

curve_points = set()
for s in range(steps):
    t = s / (steps - 1)
    AB = interp(A, B, t)
    BC = interp(B, C, t)
    CD = interp(C, D, t)
    ABC = interp(AB, BC, t)
    BCD = interp(BC, CD, t)
    P = interp(ABC, BCD, t)
    x = int(P[0] + 0.5)
    y = int(P[1] + 0.5)
    curve_points.add((x, y))

canvas = [["." if x == 0 else " " for x in range(width)] for y in range(height)]
for x, y in curve_points:
    if 0 <= x < width and 0 <= y < height:
        canvas[y][x] = "#"

for row in reversed(canvas):
    line = "".join(row).rstrip()
    print(line)
