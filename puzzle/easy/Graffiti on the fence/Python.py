L = int(input())
N = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(N)]
intervals.sort()
merged = []
for st, ed in intervals:
    if not merged or st > merged[-1][1]:
        merged.append([st, ed])
    else:
        merged[-1][1] = max(merged[-1][1], ed)
unpainted = []
prev = 0
for st, ed in merged:
    if prev < st:
        unpainted.append((prev, st))
    prev = ed
if prev < L:
    unpainted.append((prev, L))
if not unpainted:
    print("All painted")
else:
    for st, ed in unpainted:
        print(st, ed)
