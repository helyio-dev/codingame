n_imp = int(input())
imports = [input().split()[1] for _ in range(n_imp)]
n_dep = int(input())
dependencies = {}
all_libs = set(imports)
for _ in range(n_dep):
    line = input()
    parts = line.split(' requires ')
    lib = parts[0].strip()
    reqs = [x.strip() for x in parts[1].split(',')]
    dependencies[lib] = reqs
    all_libs.update(reqs)
imported = set()
error_found = False
for lib in imports:
    reqs = dependencies.get(lib, [])
    for r in reqs:
        if r not in imported:
            print(f"Import error: tried to import {lib} but {r} is required.")
            error_found = True
            break
    if error_found:
        break
    imported.add(lib)
if not error_found:
    print("Compiled successfully!")
    exit()
from collections import defaultdict, deque
graph = defaultdict(list)
in_deg = defaultdict(int)
for lib in all_libs:
    in_deg[lib] = 0
for lib, reqs in dependencies.items():
    for r in reqs:
        graph[r].append(lib)
        in_deg[lib] += 1
temp_deg = dict(in_deg)
available = [l for l in all_libs if temp_deg[l] == 0]
order = []
while available:
    node = min(available)
    order.append(node)
    available.remove(node)
    for neigh in graph[node]:
        temp_deg[neigh] -= 1
        if temp_deg[neigh] == 0:
            available.append(neigh)
if len(order) != len(all_libs):
    print("Fatal error: interdependencies.")
else:
    print("Suggest to change import order:")
    for lib in order:
        if lib in imports:
            print(f"import {lib}")
