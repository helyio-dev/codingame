from itertools import combinations

m = int(input())
n = int(input())
bars = list(map(int, input().split()))

best_sum = -1
best_subset = []

for r in range(1, n+1):
    for comb in combinations(bars, r):
        s = sum(comb)
        if s <= m:
            if s > best_sum or (s == best_sum and len(comb) < len(best_subset)) or (s == best_sum and len(comb) == len(best_subset) and comb < tuple(best_subset)):
                best_sum = s
                best_subset = list(comb)

print(*sorted(best_subset))
