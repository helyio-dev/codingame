import sys

width = int(input())
height = int(input())
grid = [input() for _ in range(height)]

for y in range(height):
    for x in range(width):
        if grid[y][x] == '0':
            right_x, right_y = -1, -1
            down_x, down_y = -1, -1
            
            for nx in range(x + 1, width):
                if grid[y][nx] == '0':
                    right_x, right_y = nx, y
                    break
            
            for ny in range(y + 1, height):
                if grid[ny][x] == '0':
                    down_x, down_y = x, ny
                    break
            
            print(f"{x} {y} {right_x} {right_y} {down_x} {down_y}")
