from copy import deepcopy

def dmgCalc(grid, x, y):
    damage = 0
    h = len(grid)
    w = len(grid[0])

    for i in range(x - 1, max(-1, x - 4), -1):
        if grid[y][i] == '#':
            break
        elif grid[y][i] == '@':
            damage += 1

    for i in range(x + 1, min(w, x + 4)):
        if grid[y][i] == '#':
            break
        elif grid[y][i] == '@':
            damage += 1

    for i in range(y - 1, max(-1, y - 4), -1):
        if grid[i][x] == '#':
            break
        elif grid[i][x] == '@':
            damage += 1

    for i in range(y + 1, min(h, y + 4)):
        if grid[i][x] == '#':
            break
        elif grid[i][x] == '@':
            damage += 1

    return damage


def dstroy(grid, x, y):
    h = len(grid)
    w = len(grid[0])

    for i in range(x - 1, max(-1, x - 4), -1):
        if grid[y][i] == '#':
            break
        elif grid[y][i] == '@':
            grid[y][i] = '.'

    for i in range(x + 1, min(w, x + 4)):
        if grid[y][i] == '#':
            break
        elif grid[y][i] == '@':
            grid[y][i] = '.'

    for i in range(y - 1, max(-1, y - 4), -1):
        if grid[i][x] == '#':
            break
        elif grid[i][x] == '@':
            grid[i][x] = '.'

    for i in range(y + 1, min(h, y + 4)):
        if grid[i][x] == '#':
            break
        elif grid[i][x] == '@':
            grid[i][x] = '.'


def getTargets(grid):
    count = 0
    for row in grid:
        count += row.count('@')
    return count


def winnable(grid, x, y, bombs):
    grid = deepcopy(grid)
    dstroy(grid, x, y)

    maxDamage = 0

    for yy in range(len(grid)):
        for xx in range(len(grid[0])):
            if grid[yy][xx] == '.':
                damage = dmgCalc(grid, xx, yy)
                if damage > maxDamage:
                    maxDamage = damage

    return maxDamage * bombs >= getTargets(grid)


w, h = map(int, input().split())

grid = [list(input()) for _ in range(h)]
res = deepcopy(grid)

bombsPlaced = {}

while True:
    rounds, bombs = map(int, input().split())

    expired = []

    for pos in bombsPlaced:
        bombsPlaced[pos] -= 1
        if bombsPlaced[pos] == 0:
            dstroy(grid, pos[0], pos[1])
            expired.append(pos)

    for pos in expired:
        del bombsPlaced[pos]

    maxDamage = 0
    bombPos = None

    for x in range(w):
        for y in range(h):
            if res[y][x] == '.':
                damage = dmgCalc(res, x, y)
                if damage > maxDamage and winnable(res, x, y, bombs - 1):
                    maxDamage = damage
                    bombPos = (x, y)

    if maxDamage == 0:
        print("WAIT")
        continue

    x, y = bombPos

    if grid[y][x] == '.' and (x, y) not in bombsPlaced:
        dstroy(res, x, y)
        bombsPlaced[(x, y)] = 3
        print(x, y)
    else:
        print("WAIT")