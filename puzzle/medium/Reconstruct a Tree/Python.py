import sys

def solve():
    line1 = sys.stdin.readline().split()
    if not line1: return
    code = [int(x) for x in line1]
    root = int(sys.stdin.readline())
    
    n = len(code) + 2
    adj = {i: [] for i in range(1, n + 1)}
    degree = {i: 1 for i in range(1, n + 1)}
    for x in code:
        degree[x] += 1
    
    p_copy = list(code)
    for x in p_copy:
        for y in range(1, n + 1):
            if degree[y] == 1:
                adj[x].append(y)
                adj[y].append(x)
                degree[x] -= 1
                degree[y] -= 1
                break
    
    u, v = [i for i in range(1, n + 1) if degree[i] == 1]
    adj[u].append(v)
    adj[v].append(u)
    
    def build_format(u, p):
        children = sorted([v for v in adj[u] if v != p])
        if not children:
            return f"({u})"
        res = f"({u}"
        for child in children:
            res += " " + build_format(child, u)
        return res + ")"
    
    print(build_format(root, -1))

solve()