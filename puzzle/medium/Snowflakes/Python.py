import sys

def get_shapes():
    line1 = sys.stdin.readline().split()
    if not line1: return
    h, w = map(int, line1)
    grid = [sys.stdin.readline().strip() for _ in range(h)]
    
    visited = [[False for _ in range(w)] for _ in range(h)]
    snowflakes = []

    for r in range(h):
        for c in range(w):
            if grid[r][c] == '*' and not visited[r][c]:
                shape = []
                stack = [(r, c)]
                visited[r][c] = True
                while stack:
                    curr_r, curr_c = stack.pop()
                    shape.append((curr_r, curr_c))
                    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == '*' and not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                snowflakes.append(shape)
    return snowflakes

def normalize(shape):
    min_r = min(r for r, c in shape)
    min_c = min(c for r, c in shape)
    base_shape = sorted((r - min_r, c - min_c) for r, c in shape)
    
    variants = []
    curr = base_shape
    for _ in range(4):
        curr = sorted((c, -r) for r, c in curr)
        mr = min(r for r, c in curr)
        mc = min(c for r, c in curr)
        variants.append(tuple(sorted((r - mr, c - mc) for r, c in curr)))
        
        flipped = sorted((r, -c) for r, c in curr)
        mr = min(r for r, c in flipped)
        mc = min(c for r, c in flipped)
        variants.append(tuple(sorted((r - mr, c - mc) for r, c in flipped)))
        
    return min(variants)

def solve():
    snowflakes = get_shapes()
    if snowflakes is None: return
    
    total_count = len(snowflakes)
    unique_shapes = set()
    
    for s in snowflakes:
        unique_shapes.add(normalize(s))
        
    print(total_count)
    print(len(unique_shapes))

if __name__ == "__main__":
    solve()