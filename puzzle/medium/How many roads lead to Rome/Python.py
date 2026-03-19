from collections import defaultdict, deque

graph = defaultdict(list)
n = int(input())
for i in range(n):
    f, to = map(int,input().split())
    graph[f].append(to)
    graph[to].append(f)

queue = deque([[1,[1]]])
paths = set()
while queue:
    node, path = queue.popleft()
    if node == 100:
        paths.add(tuple(path))

    for children in graph[node]:
        if children not in path:
            queue.append([children, path+[children]])

print(len(paths))