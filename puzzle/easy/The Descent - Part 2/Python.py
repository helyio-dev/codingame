import sys

def solve():
    line1 = sys.stdin.readline().split()
    if not line1: return
    w, h = map(int, line1)
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    a, b = map(int, sys.stdin.readline().split())
    t = int(sys.stdin.readline())

    def get_min_shots(sw, sh):
        if sw > w or sh > h:
            return float('inf')
        
        min_total = float('inf')
        for r in range(h - sh + 1):
            for c in range(w - sw + 1):
                cells = []
                for i in range(r, r + sh):
                    for j in range(c, c + sw):
                        cells.append(grid[i][j])
                
                for target in range(min(cells) + 1):
                    current_shots = sum(val - target for val in cells)
                    if current_shots < min_total:
                        min_total = current_shots
        return min_total

    res_a_b = get_min_shots(a, b)
    res_b_a = get_min_shots(b, a)
    
    final_min = min(res_a_b, res_b_a)
    
    if final_min <= t:
        print(final_min)
    else:
        print("Not Possible")

solve()