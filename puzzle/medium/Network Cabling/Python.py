import sys

def solve():
    n = int(sys.stdin.readline())
    
    x_coords = []
    y_coords = []
    
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        x_coords.append(x)
        y_coords.append(y)
        
    x_min = min(x_coords)
    x_max = max(x_coords)
    
    cable_principal_length = x_max - x_min
    
    y_coords.sort()
    
    median_y = y_coords[n // 2]
    
    cable_dedicated_length = 0
    for y in y_coords:
        cable_dedicated_length += abs(y - median_y)
        
    total_length = cable_principal_length + cable_dedicated_length
    
    print(total_length)

solve()