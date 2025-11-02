import math

N = int(input())
spheres = [list(map(float, input().split())) for _ in range(N)]

for i in range(N):
    x1, y1, z1, r1 = spheres[i]
    max_r = float('inf')
    for j in range(N):
        if i == j:
            continue
        x2, y2, z2, r2 = spheres[j]
        d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
        max_r = min(max_r, d - r2)
    spheres[i][3] = max_r

total = sum(r**3 for _,_,_,r in spheres)
print(round(total))
