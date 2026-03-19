cars = {}
speeding = []

l = int(input())
n = int(input())

for i in range(n):
    reg, dist, time = input().split(" ")
    dist, time = map(int, [dist,time])
    
    if reg in cars:
        dist2, time2 = cars[reg]

        speed = (dist - dist2) / ((time-time2) / 3600.0)
        if speed > l:
            speeding.append(reg + " " + str(dist))
    cars[reg] = [dist, time]

if speeding:
    print(*speeding ,sep = "\n")
else:
    print("OK")