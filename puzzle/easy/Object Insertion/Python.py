a, b = map(int, input().split())
obj = [input() for _ in range(a)]
c, d = map(int, input().split())
grid = [list(input()) for _ in range(c)]

positions = []

for i in range(c - a + 1):
    for j in range(d - b + 1):
        can_place = True
        for x in range(a):
            for y in range(b):
                if obj[x][y] == '*' and grid[i+x][j+y] != '.':
                    can_place = False
                    break
            if not can_place:
                break
        if can_place:
            positions.append((i,j))

print(len(positions))

if len(positions) == 1:
    i,j = positions[0]
    result = [row[:] for row in grid]
    for x in range(a):
        for y in range(b):
            if obj[x][y] == '*':
                result[i+x][j+y] = '*'
    for row in result:
        print(''.join(row))
