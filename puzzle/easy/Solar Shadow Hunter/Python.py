import sys

def solve():
    line1 = sys.stdin.readline().split()
    if not line1: return
    w, h = map(int, line1)
    k = int(sys.stdin.readline())
    grid = [sys.stdin.readline().strip() for _ in range(h)]

    shaded = [[False for _ in range(w)] for _ in range(h)]

    for r in range(h):
        for c in range(w):
            char = grid[r][c]
            if char.isdigit():
                height = int(char)
                shadow_length = height * k
                for i in range(1, shadow_length + 1):
                    target_r = r - i
                    if target_r >= 0:
                        shaded[target_r][c] = True
                    else:
                        break

    total_power = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 'P' and not shaded[r][c]:
                total_power += 100

    print(total_power)

solve()