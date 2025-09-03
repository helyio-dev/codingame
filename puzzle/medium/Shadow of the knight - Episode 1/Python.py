import sys

w, h = [int(i) for i in input().split()]
n = int(input())
x0, y0 = [int(i) for i in input().split()]

x_min, x_max = 0, w - 1
y_min, y_max = 0, h - 1

while True:
    bomb_dir = input()
    
    if 'U' in bomb_dir:
        y_max = y0 - 1
    elif 'D' in bomb_dir:
        y_min = y0 + 1
    if 'L' in bomb_dir:
        x_max = x0 - 1
    elif 'R' in bomb_dir:
        x_min = x0 + 1
    
    x0 = (x_min + x_max) // 2
    y0 = (y_min + y_max) // 2
    
    print(f"{x0} {y0}")
