import sys

def solve():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
    except ValueError:
        return

    adj = {}
    nodes = set()
    
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        nodes.add(a)
        nodes.add(b)
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)

    if not nodes:
        print("false")
        return

    start_node = next(iter(nodes))
    visited = set()
    stack = [start_node]
    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.add(curr)
            if curr in adj:
                for neighbor in adj[curr]:
                    stack.append(neighbor)
    
    if visited != nodes:
        print("false")
        return

    odd_degree_count = 0
    for node in nodes:
        if len(adj[node]) % 2 != 0:
            odd_degree_count += 1

    if odd_degree_count == 0 or odd_degree_count == 2:
        print("true")
    else:
        print("false")

solve()