import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if len(lines) < 3: return
    
    top = int(lines[0].strip())
    mid = [int(c) for c in lines[1].strip()]
    bottom = int(lines[2].strip())
    
    front, right, back, left = mid
    
    if top + bottom != 7 or front + back != 7 or right + left != 7:
        print("degenerate")
        return

    adj = {
        1: [2, 3, 5, 4],
        2: [1, 4, 6, 3],
        3: [1, 2, 6, 5],
        4: [1, 5, 6, 2],
        5: [1, 3, 6, 4],
        6: [2, 4, 5, 3]
    }
    
    neighbors = adj[top]
    idx_front = neighbors.index(front)
    if neighbors[(idx_front + 1) % 4] == right:
        print("right-handed")
    else:
        print("left-handed")

solve()