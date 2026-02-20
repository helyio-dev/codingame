import sys

def solve():
    raw = sys.stdin.read().split()
    if not raw: return
    
    grid = [0] * 256
    rows = [0] * 16
    cols = [0] * 16
    boxes = [0] * 16
    empty_cells = []
    
    chars = "ABCDEFGHIJKLMNOP"
    mapping = {c: i for i, c in enumerate(chars)}
    rev = {i: c for i, c in enumerate(chars)}
    
    for r in range(16):
        row_str = raw[r]
        for c in range(16):
            idx = (r << 4) | c
            if row_str[c] != '.':
                v = mapping[row_str[c]]
                m = 1 << v
                grid[idx] = v
                rows[r] |= m
                cols[c] |= m
                boxes[((r >> 2) << 2) | (c >> 2)] |= m
            else:
                grid[idx] = -1
                empty_cells.append(idx)

    def backtrack():
        if not empty_cells:
            return True

        best_idx_in_list = 0
        min_ops = 17
        best_m = 0
        
        for i in range(len(empty_cells)):
            idx = empty_cells[i]
            r, c = idx >> 4, idx & 15
            m = 65535 ^ (rows[r] | cols[c] | boxes[((r >> 2) << 2) | (c >> 2)])
            
            count = bin(m).count('1')
            if count < min_ops:
                min_ops = count
                best_idx_in_list = i
                best_m = m
                if count <= 1: break
        
        if min_ops == 0: return False
        
        idx = empty_cells.pop(best_idx_in_list)
        r, c = idx >> 4, idx & 15
        b = ((r >> 2) << 2) | (c >> 2)
        
        m = best_m
        while m:
            lsb = m & -m
            v = lsb.bit_length() - 1
            
            grid[idx] = v
            rows[r] |= lsb
            cols[c] |= lsb
            boxes[b] |= lsb
            
            if backtrack(): return True
            
            rows[r] ^= lsb
            cols[c] ^= lsb
            boxes[b] ^= lsb
            m ^= lsb
            
        grid[idx] = -1
        empty_cells.append(idx)
        last_idx = len(empty_cells) - 1
        empty_cells[best_idx_in_list], empty_cells[last_idx] = empty_cells[last_idx], empty_cells[best_idx_in_list]
        
        return False

    if backtrack():
        for i in range(0, 256, 16):
            print("".join(rev[grid[j]] for j in range(i, i + 16)))

solve()