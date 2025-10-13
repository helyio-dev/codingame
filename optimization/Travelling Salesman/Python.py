import sys
import math
import time

start_time = time.time()

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

def dist(a, b):
    dx = points[a][0] - points[b][0]
    dy = points[a][1] - points[b][1]
    return math.hypot(dx, dy)

visited = [False]*N
path = [0]
visited[0] = True
current = 0

for _ in range(N-1):
    next_point = -1
    min_d = float('inf')
    for i in range(N):
        if not visited[i]:
            d = dist(current, i)
            if d < min_d:
                min_d = d
                next_point = i
    path.append(next_point)
    visited[next_point] = True
    current = next_point

path.append(0)

def path_length(p):
    total = 0
    for i in range(len(p)-1):
        total += dist(p[i], p[i+1])
    return total

improved = True
while improved and time.time() - start_time < 4.8:  
    improved = False
    for i in range(1, N-1):
        for j in range(i+1, N):
            if time.time() - start_time > 4.8:
                break
            a, b = path[i-1], path[i]
            c, d = path[j], path[(j+1)%len(path)]
            if dist(a,b)+dist(c,d) > dist(a,c)+dist(b,d):
                path[i:j+1] = reversed(path[i:j+1])
                improved = True

print(' '.join(map(str, path)))
