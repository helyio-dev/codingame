import sys
from collections import deque

def solve():
    data = sys.stdin.read().splitlines()
    if not data: return
    
    try:
        w, h = map(int, data[0].split())
        energy_limit = int(data[1])
        grid = data[2:]
    except: return

    start_pos = None
    ghosts = []
    fruit_map = {}
    fruit_values = {'*': 5, '.': 1, ')': 3}
    
    for r in range(h):
        for c in range(w):
            char = grid[r][c]
            if char == 'P': start_pos = (r, c)
            elif char == 'G': ghosts.append((r, c))
            elif char in fruit_values:
                fruit_map[(r, c)] = (1 << len(fruit_map), fruit_values[char])

    danger = set()
    for gr, gc in ghosts:
        danger.add((gr, gc))
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            danger.add(((gr+dr)%h, (gc+dc)%w))

    if start_pos in danger:
        print(0)
        return

    # queue stores (r, c, energy_left, current_score, eaten_mask)
    # On utilise un dictionnaire pour le pruning: (r, c, eaten_mask) -> max_energy_left
    queue = deque([(start_pos[0], start_pos[1], energy_limit, 0, 0)])
    visited = {}
    max_total_score = 0

    while queue:
        r, c, e, score, mask = queue.popleft()
        
        if score > max_total_score:
            max_total_score = score
            
        if e <= 0:
            continue

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = (r+dr)%h, (c+dc)%w
            
            if grid[nr][nc] == '#' or (nr, nc) in danger:
                continue
                
            cost = 3 if (abs(nr-r) > 1 or abs(nc-c) > 1) else 1
            new_e = e - cost
            
            if new_e >= 0:
                new_mask = mask
                new_score = score
                if (nr, nc) in fruit_map:
                    f_bit, f_val = fruit_map[(nr, nc)]
                    if not (mask & f_bit):
                        new_mask |= f_bit
                        new_score += f_val
                
                state = (nr, nc, new_mask)
                if visited.get(state, -1) < new_e:
                    visited[state] = new_e
                    queue.append((nr, nc, new_e, new_score, new_mask))

    print(max_total_score)

solve()