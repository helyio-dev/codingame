score = int(input())
darts = int(input())

singles = [(f"S{x}", x) for x in range(1, 21)] + [("S25", 25)]
doubles = [(f"D{x}", 2*x) for x in range(1, 21)] + [("D25", 50)]
trebles = [(f"T{x}", 3*x) for x in range(1, 21)]
segments = singles + doubles + trebles

routes = set()

def dfs(route, total):
    if total > score or len(route) > darts:
        return
    if total == score and len(route) <= darts and route[-1][0].startswith("D"):
        routes.add(tuple(route))
        return
    for s in segments:
        dfs(route + [s], total + s[1])

dfs([], 0)

unique_routes = set()
for r in routes:
    if len(r) >= 2 and r[-1] == r[-2]:
        key = r[:-2] + tuple(sorted(r[-2:]))  # identiques => même route
        unique_routes.add(key)
    else:
        unique_routes.add(r)

print(len(unique_routes))
