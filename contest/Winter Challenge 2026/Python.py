import sys

my_id = int(input())
line2 = input().split()
width, height = (int(line2[0]), int(line2[1])) if len(line2) >= 2 else (int(line2[0]), int(input()))
grid = [input() for _ in range(height)]
platforms = {(c, r) for r in range(height) for c in range(width) if grid[r][c] == '#'}
my_snake_count = int(input())
my_ids = [int(input()) for _ in range(my_snake_count)]
opp_ids = [int(input()) for _ in range(my_snake_count)]

def get_flood_fill(start, occupied, limit=15):
    q = [start]
    visited = {start}
    count = 0
    while q and count < limit:
        curr = q.pop(0)
        count += 1
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = curr[0]+dx, curr[1]+dy
            if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in occupied and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))
    return count

while True:
    try:
        ps_line = input().split()
        if not ps_line: break
        power_sources = {tuple(map(int, input().split())) for _ in range(int(ps_line[0]))}
        
        snakes = {}
        sc_line = input().split()
        if not sc_line: break
        for _ in range(int(sc_line[0])):
            parts = input().split()
            sid, body_raw = int(parts[0]), parts[1].split(':')
            snakes[sid] = [tuple(map(int, p.split(','))) for p in body_raw]

        occupied = platforms.copy()
        for s in snakes.values():
            for part in s: occupied.add(part)

        actions = []
        for sid in my_ids:
            if sid not in snakes: continue
            head = snakes[sid][0]
            best_move, max_score = "UP", -10**9

            for m_name, dx, dy in [("UP", 0, -1), ("DOWN", 0, 1), ("LEFT", -1, 0), ("RIGHT", 1, 0)]:
                nx, ny = head[0] + dx, head[1] + dy
                
                if not (0 <= nx < width and 0 <= ny < height) or (nx, ny) in occupied:
                    continue

                score = 0
                if (nx, ny) in power_sources: score += 1500

                dist_to_ps = min([abs(nx-px) + abs(ny-py) for px, py in power_sources], default=20)
                score -= dist_to_ps * 20

                space = get_flood_fill((nx, ny), occupied)
                score += space * 50

                new_body = [(nx, ny)] + snakes[sid][:-1]
                stable = False
                for bx, by in new_body:
                    if (bx, by+1) in platforms or any((bx, by+1) in s and sid != s_id for s_id, s in snakes.items()):
                        stable = True; break
                
                if not stable:
                    fall_y = ny
                    while fall_y < height and (nx, fall_y + 1) not in occupied:
                        fall_y += 1
                    if fall_y >= height: score -= 5000
                    else: score -= 800

                for oid in opp_ids:
                    if oid in snakes:
                        o_head = snakes[oid][0]
                        if abs(nx-o_head[0]) + abs(ny-o_head[1]) <= 2:
                            score -= 300

                if score > max_score:
                    max_score, best_move = score, m_name

            actions.append(f"{sid} {best_move}")
        print(";".join(actions) if actions else "WAIT")
    except EOFError: break