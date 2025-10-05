from collections import deque

food = []
w, h = [int(i) for i in input().split()]
for i in range(h):
    food.append([*map(int,input().split())])

queue = deque([[0,0, 0]])
max_score = 0
seen = {}
while queue:
    i, j, score = queue.popleft()
    score += food[i][j]
    
    if (i,j) in seen and score <= seen[(i,j)]:
        continue
    seen[(i,j)] = score

    if score > max_score:
        max_score = score

    if i+1 < h:
        queue.append([i+1,j,score])
    if j+1 < w:
        queue.append([i,j+1,score])

print(max_score)