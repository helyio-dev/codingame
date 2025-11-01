H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]
arrows = {'^', 'v', '<', '>'}
pos = []

for i in range(H):
    for j in range(W):
        if grid[i][j] in arrows:
            pos.append((i, j, grid[i][j]))

steps = 0
while pos:
    steps += 1
    new_pos = {}
    for i, j, d in pos:
        if d == '^':
            ni, nj = (i-1)%H, j
        elif d == 'v':
            ni, nj = (i+1)%H, j
        elif d == '<':
            ni, nj = i, (j-1)%W
        else:
            ni, nj = i, (j+1)%W
        if (ni, nj) in new_pos:
            new_pos[(ni, nj)].append(d)
        else:
            new_pos[(ni, nj)] = [d]
    pos = [(i,j,d[0]) for (i,j), d in new_pos.items() if len(d) == 1]

print(steps)
