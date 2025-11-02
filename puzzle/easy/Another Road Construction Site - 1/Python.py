roadLength = int(input())
zoneQuantity = int(input())
zones = [tuple(map(int, input().split())) for _ in range(zoneQuantity)]
zones.sort()
time = 0
prev = 0
for km, speed in zones:
    time += (km - prev) / 130 * 60
    prev = km
time += (roadLength - prev) / 130 * 60
actual = 0
prev = 0
for km, speed in zones:
    actual += (km - prev) / 130 * 60
    prev = km
    start = km
    next_speed = speed
    if zones.index((km, speed)) + 1 < len(zones):
        end = zones[zones.index((km, speed))+1][0]
    else:
        end = roadLength
    actual += (end - start) / next_speed * 60
    prev = end
print(round(actual - (roadLength / 130 * 60)))
