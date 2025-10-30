n = int(input())
edges = []
nodes = set()
for _ in range(n):
    a, _, b = input().split()
    edges.append((a, b))
    nodes.update([a, b])

g = {x: [] for x in nodes}
for a, b in edges:
    g[a].append(b)

visited = {}
def dfs(u):
    visited[u] = 1
    for v in g[u]:
        if v not in visited:
            if dfs(v):
                return True
        elif visited[v] == 1:
            return True
    visited[u] = 2
    return False

res = "consistent"
for u in nodes:
    if u not in visited:
        if dfs(u):
            res = "contradiction"
            break
print(res)
