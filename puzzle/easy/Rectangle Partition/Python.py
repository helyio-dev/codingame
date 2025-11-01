w, h, cx, cy = map(int, input().split())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))

xs = [0] + xs + [w]
ys = [0] + ys + [h]

xpos = []
for i in range(len(xs)):
    for j in range(i + 1, len(xs)):
        xpos.append(xs[j] - xs[i])
ypos = []
for i in range(len(ys)):
    for j in range(i + 1, len(ys)):
        ypos.append(ys[j] - ys[i])

count = 0
xpos.sort()
ypos.sort()

from collections import Counter
cx = Counter(xpos)
cy = Counter(ypos)

for size in cx:
    if size in cy:
        count += cx[size] * cy[size]

print(count)
