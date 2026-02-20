import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    gears = []
    idx = 1
    for _ in range(n):
        gears.append((int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])))
        idx += 3

    directions = {}
    directions[0] = 1 
    
    stack = [0]
    blocked = False
    
    while stack:
        curr = stack.pop()
        cx, cy, cr = gears[curr]
        
        for i in range(n):
            nx, ny, nr = gears[i]
            if (cx - nx)**2 + (cy - ny)**2 == (cr + nr)**2:
                new_dir = -directions[curr]
                if i in directions:
                    if directions[i] != new_dir:
                        blocked = True
                else:
                    directions[i] = new_dir
                    stack.append(i)
        if blocked: break

    if blocked or (n - 1 not in directions):
        print("NOT MOVING")
    else:
        print("CW" if directions[n-1] == 1 else "CCW")

if __name__ == "__main__":
    solve()