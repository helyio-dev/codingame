from collections import defaultdict
from collections import deque

graph = defaultdict(list)

start = input()
end = input()
n = int(input())
for i in range(n):
    station_1, station_2 = input().split()
    graph[station_1].append(station_2)
    graph[station_2].append(station_1)

queue = deque([[start,[start]]])
while queue:
    current_station, path = queue.popleft()

    if current_station == end:
        print(" > ".join(path))
        break

    for con in graph[current_station]:
        if con not in path:
            queue.append([con, path+[con]])