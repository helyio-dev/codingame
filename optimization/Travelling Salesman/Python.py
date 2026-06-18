import sys
import time

start_time = time.time()

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

dist_matrix = [[0.0] * N for _ in range(N)]
for i in range(N):
    xi, yi = points[i]
    for j in range(i + 1, N):
        xj, yj = points[j]
        d = ((xi - xj) ** 2 + (yi - yj) ** 2) ** 0.5
        dist_matrix[i][j] = dist_matrix[j][i] = d

visited = [False] * N
visited[0] = True
path = [0]
current = 0

for _ in range(N - 1):
    next_point = -1
    min_dist = float('inf')
    for x in range(N):
        if not visited[x] and dist_matrix[current][x] < min_dist:
            min_dist = dist_matrix[current][x]
            next_point = x
    visited[next_point] = True
    path.append(next_point)
    current = next_point

path.append(0)

improved = True
while improved:
    improved = False
    
    if (time.time() - start_time) > 4.8:
        break
        
    for i in range(1, N - 1):
        a = path[i - 1]
        b = path[i]
        
        for j in range(i + 1, N):
            c = path[j]
            d = path[j + 1] 
            
            if (dist_matrix[a][c] + dist_matrix[b][d]) < (dist_matrix[a][b] + dist_matrix[c][d]):
                path[i:j + 1] = path[j:i - 1:-1]
                improved = True
                break 
        if improved:
            break

print(' '.join(map(str, path)))