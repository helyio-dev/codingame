n = int(input())
for _ in range(n):
    row, col, isWhite = map(int, input().split())
    if row < 8 or col < 8:
        print(0)
        continue
    h = row - 7
    w = col - 7
    total = h * w
    if isWhite == 0:
        total //= 2
    else:
        total = (total + 1) // 2
    print(total)
