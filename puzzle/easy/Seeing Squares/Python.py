R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]

def is_square(r, c, h):
    w = 2 * h - 1
    if r + h - 1 >= R or c + w - 1 >= C:
        return False
    if grid[r][c] != '+' or grid[r][c + w - 1] != '+' or grid[r + h - 1][c] != '+' or grid[r + h - 1][c + w - 1] != '+':
        return False
    for j in range(c + 1, c + w - 1):
        if grid[r][j] not in '-+' or grid[r + h - 1][j] not in '-+':
            return False
    for i in range(r + 1, r + h - 1):
        if grid[i][c] not in '|+' or grid[i][c + w - 1] not in '|+':
            return False
    return True

count = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == '+':
            for h in range(2, R - r + 1):
                if is_square(r, c, h):
                    count += 1

print(count)
