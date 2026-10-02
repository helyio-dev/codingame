import sys
from itertools import combinations

def main():
    data = sys.stdin.read().split('\n')
    h, w = map(int, data[0].split())
    grid = []
    for i in range(h):
        line = data[1 + i] if 1 + i < len(data) else ''
        grid.append(line.ljust(w))
    comp = [[False] * w for _ in range(h)]
    gates = []
    switches = []
    led = None
    for r in range(h):
        c = 0
        while c < w:
            if grid[r][c] == '[':
                e = grid[r].find(']', c)
                if e == -1:
                    c += 1
                    continue
                sc = None
                for k in range(c + 1, e):
                    if grid[r][k] != ' ':
                        sc = k
                        break
                for k in range(c, e + 1):
                    comp[r][k] = True
                ch = grid[r][sc]
                if ch == '@':
                    led = (r, c, e)
                elif ch in '<>':
                    switches.append((r, c, e, sc, ch))
                else:
                    gates.append((r, c, e, sc, ch))
                c = e + 1
            else:
                c += 1
    vert = set('|+01')
    horiz = set('-+')
    wid = [[-1] * w for _ in range(h)]
    n_w = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] != ' ' and not comp[r][c] and wid[r][c] == -1:
                stack = [(r, c)]
                wid[r][c] = n_w
                while stack:
                    y, x = stack.pop()
                    ch = grid[y][x]
                    cand = []
                    if ch in vert:
                        cand.append((y - 1, x, 'v'))
                        cand.append((y + 1, x, 'v'))
                    if ch in horiz:
                        cand.append((y, x - 1, 'h'))
                        cand.append((y, x + 1, 'h'))
                    for ny, nx, t in cand:
                        if 0 <= ny < h and 0 <= nx < w and not comp[ny][nx] and grid[ny][nx] != ' ' and wid[ny][nx] == -1:
                            nch = grid[ny][nx]
                            if (t == 'v' and nch in vert) or (t == 'h' and nch in horiz):
                                wid[ny][nx] = n_w
                                stack.append((ny, nx))
                n_w += 1
    source_of = {}
    n_in = 0
    in_vals = []
    for c in range(w):
        if grid[h - 1][c] in '01' and not comp[h - 1][c]:
            source_of[wid[h - 1][c]] = ('I', n_in)
            in_vals.append(int(grid[h - 1][c]))
            n_in += 1
    for i, (r, c, e, sc, ch) in enumerate(gates):
        if r - 1 >= 0 and wid[r - 1][sc] != -1:
            source_of[wid[r - 1][sc]] = ('G', i)
    for i, (r, c, e, sc, ch) in enumerate(switches):
        cols = [k for k in range(c + 1, e) if r - 1 >= 0 and grid[r - 1][k] == '|' and not comp[r - 1][k]]
        if cols:
            source_of[wid[r - 1][min(cols)]] = ('SL', i)
            source_of[wid[r - 1][max(cols)]] = ('SR', i)

    def pins_below(r, c, e):
        res = []
        if r + 1 < h:
            for k in range(c + 1, e):
                if grid[r + 1][k] == '|' and not comp[r + 1][k]:
                    res.append(source_of.get(wid[r + 1][k]))
        return res

    gin = [pins_below(r, c, e) for (r, c, e, sc, ch) in gates]
    sin = []
    for (r, c, e, sc, ch) in switches:
        p = pins_below(r, c, e)
        sin.append(p[0] if p else None)
    lin = pins_below(*led)
    order = []
    visited = set()
    sys.setrecursionlimit(10000)

    def visit(key):
        if key is None or key in visited:
            return
        visited.add(key)
        t = key[0]
        if t == 'G':
            for k in gin[key[1]]:
                visit(k)
        elif t in ('SL', 'SR'):
            visit(sin[key[1]])
        order.append(key)

    for k in lin:
        visit(k)
    ns = len(switches)
    sw_init = [1 if s[4] == '<' else 0 for s in switches]
    total = ns + n_in

    def evaluate(tog):
        ins = in_vals[:]
        sw = sw_init[:]
        for t in tog:
            if t < ns:
                sw[t] ^= 1
            else:
                ins[t - ns] ^= 1
        val = {None: 0}
        for key in order:
            t = key[0]
            i = key[1]
            if t == 'I':
                val[key] = ins[i]
            elif t == 'SL':
                val[key] = val[sin[i]] if sw[i] == 1 else 0
            elif t == 'SR':
                val[key] = val[sin[i]] if sw[i] == 0 else 0
            else:
                ch = gates[i][4]
                vs = [val[k] for k in gin[i]]
                a = vs[0] if vs else 0
                b = vs[1] if len(vs) > 1 else 0
                if ch == '~':
                    v = 1 - a
                elif ch == '&':
                    v = a & b
                elif ch == '|':
                    v = a | b
                elif ch == '+':
                    v = a ^ b
                elif ch == '^':
                    v = 1 - (a & b)
                elif ch == '-':
                    v = 1 - (a | b)
                else:
                    v = 1 - (a ^ b)
                val[key] = v
        if not lin:
            return False
        for k in lin:
            if val[k] != 1:
                return False
        return True

    names = ['K%d' % (i + 1) for i in range(ns)] + ['I%d' % (i + 1) for i in range(n_in)]
    for size in range(total + 1):
        for comb in combinations(range(total), size):
            if evaluate(comb):
                for t in comb:
                    print(names[t])
                return

main()