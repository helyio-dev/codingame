valueToReach = int(input())
N = int(input())
counts = list(map(int, input().split()))
values = list(map(int, input().split()))

coins = sorted(zip(values, counts))  
total_money = sum(v*c for v,c in coins)
if total_money < valueToReach:
    print(-1)
else:
    remaining = valueToReach
    grab = 0
    for v, c in coins:
        take = min(c, (remaining + v - 1) // v)  
        remaining -= take * v
        grab += take
        if remaining <= 0:
            break
    print(grab)
