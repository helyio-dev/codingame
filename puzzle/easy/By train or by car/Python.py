import math

start, end = input().split()
n = int(input())
graph = {}
for _ in range(n):
    a,b,d = input().split()
    graph[a] = (b,float(d))

path = [start]
distances = []
while path[-1] != end:
    nxt, d = graph[path[-1]]
    path.append(nxt)
    distances.append(d)

def train_time(distances):
    t = 35  
    for i,d in enumerate(distances):
        first = min(3,d)
        last = min(3,d-first)
        main = max(0,d-first-last)
        t += first*60/50 + main*60/284 + last*60/50
        if i < len(distances)-1:
            t += 8 
    t += 30  
    return t

def car_time(distances):
    t = 0
    for d in distances:
        first = min(7,d)
        last = min(7,d-first)
        main = max(0,d-first-last)
        t += first*60/50 + main*60/105 + last*60/50
    return t

tt = train_time(distances)
tc = car_time(distances)

if tt < tc:
    print(f'TRAIN {int(tt//60)}:{int(tt%60):02}')
else:
    print(f'CAR {int(tc//60)}:{int(tc%60):02}')
