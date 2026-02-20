import sys
from collections import deque

def parse_tile(t):
    return (int(t[:-1]), t[-1])

def format_tile(t):
    return f"{t[0]}{t[1]}"

def is_run(tiles):
    if len(tiles) < 3: return False
    c = tiles[0][1]
    v_prev = tiles[0][0]
    for i in range(1, len(tiles)):
        if tiles[i][1] != c or tiles[i][0] != v_prev + 1: return False
        v_prev = tiles[i][0]
    return True

def is_set(tiles):
    if not (3 <= len(tiles) <= 4): return False
    v = tiles[0][0]
    colors = set()
    for t in tiles:
        if t[0] != v or t[1] in colors: return False
        colors.add(t[1])
    return True

def is_valid(tiles):
    return is_run(tiles) or is_set(tiles)

def sort_tiles(tiles):
    if not tiles: return []
    if all(t[0] == tiles[0][0] for t in tiles):
        order = {'B': 0, 'G': 1, 'R': 2, 'Y': 3}
        return sorted(tiles, key=lambda x: order[x[1]])
    return sorted(tiles)

def solve():
    goal_str = sys.stdin.readline().strip()
    goal_tile = parse_tile(goal_str)
    n_rows = int(sys.stdin.readline())
    initial_rows = {}
    max_rid = 0
    for _ in range(n_rows):
        line = sys.stdin.readline().split()
        rid = int(line[0])
        tiles = tuple(sort_tiles([parse_tile(t) for t in line[1:]]))
        initial_rows[rid] = tiles
        max_rid = max(max_rid, rid)

    queue = deque([(initial_rows, [], max_rid, None)])
    visited = set()

    while queue:
        rows, actions, m_rid, carry = queue.popleft()
        state = (tuple(sorted(rows.items())), carry)
        if state in visited: continue
        visited.add(state)

        if len(actions) >= 7: continue

        if carry is None:
            for rid in sorted(rows.keys()):
                new_tiles = sort_tiles(list(rows[rid]) + [goal_tile])
                if is_valid(new_tiles):
                    res_rows = rows.copy()
                    res_rows[rid] = tuple(new_tiles)
                    for a in actions: print(a)
                    print(f"PUT {goal_str} {rid}")
                    for r in sorted(res_rows.keys()):
                        print(f"{r} {' '.join(format_tile(t) for t in res_rows[r])}")
                    return
                
                for split_idx in range(1, len(new_tiles)):
                    p1, p2 = new_tiles[:split_idx], new_tiles[split_idx:]
                    if is_valid(p1) and is_valid(p2):
                        res_rows = rows.copy()
                        res_rows[rid] = tuple(p1)
                        res_rows[m_rid + 1] = tuple(p2)
                        for a in actions: print(a)
                        print(f"PUT {goal_str} {rid}")
                        for r in sorted(res_rows.keys()):
                            print(f"{r} {' '.join(format_tile(t) for t in res_rows[r])}")
                        return

            rids = sorted(rows.keys())
            for i in range(len(rids)):
                for j in range(i + 1, len(rids)):
                    r1, r2 = rids[i], rids[j]
                    combined = sort_tiles(list(rows[r1]) + list(rows[r2]))
                    if is_run(combined):
                        nr = rows.copy()
                        nr[r1] = tuple(combined)
                        del nr[r2]
                        queue.append((nr, actions + [f"COMBINE {r1} {r2}"], m_rid, None))

            for rid in sorted(rows.keys()):
                tiles = rows[rid]
                for i in range(len(tiles)):
                    t = tiles[i]
                    rem = list(tiles[:i] + tiles[i+1:])
                    if not rem:
                        nr = rows.copy()
                        del nr[rid]
                        queue.append((nr, actions + [f"TAKE {format_tile(t)} {rid}"], m_rid, t))
                    elif is_valid(rem):
                        nr = rows.copy()
                        nr[rid] = tuple(rem)
                        queue.append((nr, actions + [f"TAKE {format_tile(t)} {rid}"], m_rid, t))
                    else:
                        for s in range(1, len(rem)):
                            p1, p2 = rem[:s], rem[s:]
                            if is_valid(p1) and is_valid(p2):
                                nr = rows.copy()
                                nr[rid] = tuple(p1)
                                nr[m_rid + 1] = tuple(p2)
                                queue.append((nr, actions + [f"TAKE {format_tile(t)} {rid}"], m_rid + 1, t))
                                break
        else:
            for rid in sorted(rows.keys()):
                new_tiles = sort_tiles(list(rows[rid]) + [carry])
                if is_valid(new_tiles):
                    nr = rows.copy()
                    nr[rid] = tuple(new_tiles)
                    queue.append((nr, actions + [f"PUT {format_tile(carry)} {rid}"], m_rid, None))
                else:
                    for s in range(1, len(new_tiles)):
                        p1, p2 = new_tiles[:s], new_tiles[s:]
                        if is_valid(p1) and is_valid(p2):
                            nr = rows.copy()
                            nr[rid] = tuple(p1)
                            nr[m_rid + 1] = tuple(p2)
                            queue.append((nr, actions + [f"PUT {format_tile(carry)} {rid}"], m_rid + 1, None))
                            break

if __name__ == "__main__":
    solve()