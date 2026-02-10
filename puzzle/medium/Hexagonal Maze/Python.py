import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    w, h = map(int, input_data[0].split())
    grid = [list(row) for row in input_data[1:]]
    
    start = None
    end = None
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)

    def get_neighbors(r, c):
        res = []
        if r % 2 == 0:
            dirs = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)]
        else:
            dirs = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]
        
        for dr, dc in dirs:
            nr = (r + dr) % h
            nc = (c + dc) % w
            res.append((nr, nc))
        return res

    queue = deque([start])
    parent = {start: None}
    
    found = False
    while queue:
        curr = queue.popleft()
        if curr == end:
            found = True
            break
            
        for neighbor in get_neighbors(*curr):
            if neighbor not in parent and grid[neighbor[0]][neighbor[1]] != '#':
                parent[neighbor] = curr
                queue.append(neighbor)
        if found:
            break

    curr = parent[end]
    while curr and curr != start:
        grid[curr[0]][curr[1]] = '.'
        curr = parent[curr]

    for row in grid:
        print("".join(row))

solve()