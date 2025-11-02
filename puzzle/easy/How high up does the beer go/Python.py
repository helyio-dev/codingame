import math

bottomRadius, topRadius, glassHeight, beerVol = map(float, input().split())

def frustum_volume(h):
    r = bottomRadius + (topRadius - bottomRadius) * (h / glassHeight)
    return (math.pi * h * (bottomRadius**2 + bottomRadius*r + r**2)) / 3

low, high = 0, glassHeight
while high - low > 1e-6:
    mid = (low + high) / 2
    if frustum_volume(mid) < beerVol:
        low = mid
    else:
        high = mid

print(round((low + high) / 2, 1))
