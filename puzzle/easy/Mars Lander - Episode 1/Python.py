import sys
import math
surface_n = int(input())
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]
while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    thrust = 4 if v_speed < -35 else 3
    
    print("0", min(thrust, fuel))