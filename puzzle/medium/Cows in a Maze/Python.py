cows = []
maze = []
c, h, w = [int(i) for i in input().split()]
for i in range(c):
    cow = int(input())
    cows.append(cow)
for i in range(h):
    maze.append([])
    for j in input().split():
        square = int(j)
        maze[-1].append(square)

passed = [0]
def dfs(y,x, worth, visited):
    if y==0 and x==0:
        passed[0] += 1
        return True

    visited.add((y,x))
    for dy,dx in [[0,1],[-1,0],[0,-1],[1,0]]:
        ny ,nx = y+dy, x+dx
        if 0 <= ny < h and 0 <= nx < w and maze[ny][nx] <= worth and (ny,nx) not in visited:
            if dfs(ny, nx, worth, visited):
                return True
    visited.remove((y,x))

for i,cow in enumerate(sorted(cows), start = 0):
    if cow >= maze[-1][-1]:
        res = dfs(h-1,h-1,cow, set())
        if res:
            passed = [len(cows) - i]
            break

print(*passed)