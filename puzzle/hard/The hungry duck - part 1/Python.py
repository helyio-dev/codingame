from collections import deque

food = []
w, h = [int(i) for i in input().split()]
for i in range(h):
    food.append([*map(int,input().split())])

queue = deque([[0,0, 0]])
max_score = 0
while queue:
    i, j, score = queue.popleft()
    score += food[i][j]
    if score > max_score:
        max_score = score

    if i+1 < h:
        queue.append([i+1,j,score])
    if j+1 < w:
        queue.append([i,j+1,score])

print(max_score)