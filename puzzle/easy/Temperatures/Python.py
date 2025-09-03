import sys
import math

n = int(input())
closest_temp = None

for i in input().split():
    t = int(i)
    if closest_temp is None or abs(t) < abs(closest_temp) or (abs(t) == abs(closest_temp) and t > closest_temp):
        closest_temp = t

if closest_temp is None:
    print(0)
else:
    print(closest_temp)
