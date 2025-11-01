L = int(input())
N = int(input())
positions = list(map(int, input().split()))
max_time = 0
for p in positions:
    max_time = max(max_time, max(p, L - p))
print(round(max_time))
