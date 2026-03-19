from math import floor
import heapq

heap = []
k = int(input())
n = int(input())
for i in range(n):
    value, rate = [int(j) for j in input().split()]
    heap += [[-value ,-rate]]
heapq.heapify(heap)

replenish = []

resources = 0
for i in range(k):
    value,rate = heapq.heappop(heap) if heap else [0,-100]

    resources += value * -1

    if replenish and replenish[0][0] == i:
        _,replenished_value, replenished_rate = heapq.heappop(replenish)
        heapq.heappush(heap, [replenished_value, replenished_rate])

    if value != 0:
        heapq.heappush(replenish, [i+3, -floor(abs(value)*-rate/100),rate])

print(resources)