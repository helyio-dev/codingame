from collections import deque
route = input()

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direction_chars = ["N", "E", "S", "W"]

invalid = set()
i = j = 0
for char in route:
    dy, dx = {"N": (1, 0), "E": (0, 1), "S": (-1, 0), "W": (0, -1)}[char]
    ni, nj = i + dy, j + dx
    invalid.add(((i, j), (ni, nj)))
    invalid.add(((ni, nj), (i, j)))
    i, j = ni, nj

start = (i, j)
goal = (0, 0)
max_dist = len(route) + 2

queue = deque([(start, [])])
seen = {start: 0}
results = []
found_depth = None

while queue:
    (i, j), path = queue.popleft()

    if found_depth is not None and len(path) > found_depth:
        break

    if (i, j) == goal:
        found_depth = len(path)
        results.append("".join(path))
        continue

    for idx, (dy, dx) in enumerate(directions):
        ni, nj = i + dy, j + dx
        next_pos = (ni, nj)
        if ((i, j), next_pos) in invalid:
            continue
        if abs(ni) + abs(nj) >= max_dist:
            continue
        if next_pos in seen and seen[next_pos] < len(path) + 1:
            continue
        seen[next_pos] = len(path) + 1
        queue.append((next_pos, path + [direction_chars[idx]]))

results.sort()
for r in results:
    print(r)