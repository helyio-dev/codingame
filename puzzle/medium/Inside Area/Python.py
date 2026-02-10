import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0])
    x, y = 0, 0
    vertices = [(0, 0)]
    perimeter = 0
    
    for i in range(1, n + 1):
        direction, step = input_data[i].split()
        step = int(step)
        perimeter += step
        
        if direction == '^':
            y += step
        elif direction == 'v':
            y -= step
        elif direction == '>':
            x += step
        elif direction == '<':
            x -= step
            
        vertices.append((x, y))
    
    shoelace = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[i+1]
        shoelace += (x1 * y2 - x2 * y1)
    
    area_inner = abs(shoelace) // 2
    
    total_area = area_inner + (perimeter // 2) + 1
    print(total_area)

solve()