n = int(input())

cache = {}
def search(height, next_step):
    if height == n:
        return 1

    if height > n:
        return 0
    
    if (height,next_step) in cache:
        return cache[(height,next_step)]

    ways = 0
    for i in range(next_step+1, n-height+1):
        ways += search(height+i, i)

    cache[(height,next_step)] = ways
    return ways

ways = search(0,0)

print(ways - 1)