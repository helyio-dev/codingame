import sys
import math

input = sys.stdin.readline

def solve(a):
    a = sorted(a)
    n = len(a)

    d = [[2.0 * math.sqrt(a[i] * a[j]) for j in range(n)] for i in range(n)]

    best = float("inf")

    def greedy(order):
        pos = [0.0] * n
        left = 0.0
        right = 0.0

        for k in range(1, n):
            x = 0.0
            r = a[order[k]]

            for j in range(k):
                v = pos[j] + d[order[k]][order[j]]
                if v > x:
                    x = v

            pos[k] = x
            right = max(right, x + r)
            left = min(left, x - r)

        return right - left

    order = list(range(n))
    used = [False] * n
    pos = [0.0] * n

    def dfs(k, left, right):
        nonlocal best

        if k == n:
            w = right - left
            if w < best:
                best = w
            return

        previous = -1

        candidates = []

        for i in range(n):
            if used[i] or a[i] == previous:
                continue

            previous = a[i]

            if k == 0:
                x = 0.0
                nl = -a[i]
                nr = a[i]
            else:
                x = 0.0
                for j in range(k):
                    v = pos[j] + d[i][order[j]]
                    if v > x:
                        x = v

                nl = min(left, x - a[i])
                nr = max(right, x + a[i])

            w = nr - nl
            candidates.append((w, i, x, nl, nr))

        candidates.sort()

        for w, i, x, nl, nr in candidates:
            if w >= best:
                continue

            order[k] = i
            pos[k] = x
            used[i] = True

            dfs(k + 1, nl, nr)

            used[i] = False

    for first in range(n):
        used[first] = True
        order[0] = first
        pos[0] = 0.0
        dfs(1, -a[first], a[first])
        used[first] = False

    return best

t = int(input())

for _ in range(t):
    data = list(map(int, input().split()))
    m = data[0]
    radii = data[1:m + 1]
    print(f"{solve(radii):.3f}")