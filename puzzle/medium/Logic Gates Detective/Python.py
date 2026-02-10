import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines: return

    obs_parts = lines[0].split()
    vals = {}
    for obs in obs_parts:
        name, val = obs.split(':')
        vals[name] = int(val)

    targets = lines[1].split()
    n_rules = int(lines[2])
    rules = []
    nodes = set(vals.keys())
    for i in range(3, 3 + n_rules):
        parts = lines[i].split()
        a, op, b, _, c = parts
        rules.append((a, op, b, c))
        nodes.update([a, b, c])

    def get_deductions(v):
        changed = True
        while changed:
            changed = False
            for a, op, b, c in rules:
                if a in v and b in v and c not in v:
                    if op == 'or': res = v[a] | v[b]
                    elif op == 'and': res = v[a] & v[b]
                    elif op == 'xor': res = v[a] ^ v[b]
                    v[c], changed = res, True
                if c in v:
                    if op == 'and':
                        if v[c] == 1:
                            if a not in v: v[a], changed = 1, True
                            if b not in v: v[b], changed = 1, True
                        elif a in v and v[a] == 1 and b not in v: v[b], changed = 0, True
                        elif b in v and v[b] == 1 and a not in v: v[a], changed = 0, True
                    elif op == 'or':
                        if v[c] == 0:
                            if a not in v: v[a], changed = 0, True
                            if b not in v: v[b], changed = 0, True
                        elif a in v and v[a] == 0 and b not in v: v[b], changed = 1, True
                        elif b in v and v[b] == 0 and a not in v: v[a], changed = 1, True
                    elif op == 'xor':
                        if a in v and b not in v: v[b], changed = v[a] ^ v[c], True
                        elif b in v and a not in v: v[a], changed = v[b] ^ v[c], True
        return v

    def is_consistent(v):
        for a, op, b, c in rules:
            if a in v and b in v and c in v:
                if op == 'or' and v[c] != (v[a] | v[b]): return False
                if op == 'and' and v[c] != (v[a] & v[b]): return False
                if op == 'xor' and v[c] != (v[a] ^ v[b]): return False
        return True

    def backtrack(v):
        v = get_deductions(v)
        if not is_consistent(v): return None
        if len(v) == len(nodes): return v
        
        curr_nodes = sorted([n for n in nodes if n not in v])
        nxt = curr_nodes[0]
        for val in [0, 1]:
            v_copy = v.copy()
            v_copy[nxt] = val
            res = backtrack(v_copy)
            if res: return res
        return None

    final_vals = backtrack(vals)
    print("".join(str(final_vals[t]) for t in targets))

solve()