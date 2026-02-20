import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    w, h = int(data[0]), int(data[1])
    grid = []
    idx = 2
    num_positions = {}
    for r in range(h):
        row = []
        for c in range(w):
            val = int(data[idx]); idx += 1
            row.append(val)
            if val > 0: num_positions[(r, c)] = val
        grid.append(row)

    rects_by_num = {}
    for (nr, nc), area in num_positions.items():
        possible = []
        for rh in range(1, area + 1):
            if area % rh == 0:
                rw = area // rh
                for top in range(max(0, nr - rh + 1), min(h - rh, nr) + 1):
                    for left in range(max(0, nc - rw + 1), min(w - rw, nc) + 1):
                        bottom, right = top + rh - 1, left + rw - 1
                        ok = True
                        for (orr, occ) in num_positions:
                            if (orr, occ) != (nr, nc):
                                if top <= orr <= bottom and left <= occ <= right:
                                    ok = False; break
                        if ok:
                            cells = tuple((r, c) for r in range(top, bottom + 1) for c in range(left, right + 1))
                            possible.append(cells)
        rects_by_num[(nr, nc)] = possible

    solutions = []
    occupied = [[False] * w for _ in range(h)]
    current_rects = [None] * len(num_positions)
    num_list = list(num_positions.keys())
    num_to_idx = {pos: i for i, pos in enumerate(num_list)}

    def backtrack(n_idx):
        if n_idx == len(num_list):
            res = [[''] * w for _ in range(h)]
            temp_occupied = [[-1] * w for _ in range(h)]
            for i, cells in enumerate(current_rects):
                for r, c in cells: temp_occupied[r][c] = i
            
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            mapping = {}
            char_idx = 0
            for r in range(h):
                for c in range(w):
                    rid = temp_occupied[r][c]
                    if rid not in mapping:
                        mapping[rid] = alphabet[char_idx]
                        char_idx += 1
                    res[r][c] = mapping[rid]
            solutions.append("".join("".join(row) for row in res))
            return

        best_n_idx = -1
        min_p = float('inf')
        
        for i in range(n_idx, len(num_list)):
            pos = num_list[i]
            count = 0
            for rect in rects_by_num[pos]:
                if all(not occupied[r][c] for r, c in rect):
                    count += 1
            if count == 0: return 
            if count < min_p:
                min_p = count
                best_n_idx = i
                if count == 1: break
        
        num_list[n_idx], num_list[best_n_idx] = num_list[best_n_idx], num_list[n_idx]
        pos = num_list[n_idx]
        
        for rect in rects_by_num[pos]:
            if all(not occupied[r][c] for r, c in rect):
                for r, c in rect: occupied[r][c] = True
                current_rects[num_to_idx[pos]] = rect
                backtrack(n_idx + 1)
                for r, c in rect: occupied[r][c] = False
        
        num_list[n_idx], num_list[best_n_idx] = num_list[best_n_idx], num_list[n_idx]

    backtrack(0)
    print(len(solutions))
    if solutions:
        solutions.sort()
        s = solutions[0]
        for i in range(h): print(s[i*w : (i+1)*w])

solve()