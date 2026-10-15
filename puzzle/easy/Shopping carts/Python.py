n = int(input())
carts = list(map(int, input().split()))
actions = input().strip()

for action in actions:
    if action == 'T':
        if max(carts) == 0:
            print("IMPOSSIBLE")
            break
        i = carts.index(max(carts))
        carts[i] -= 1
    else:
        m = min(carts)
        i = len(carts) - 1 - carts[::-1].index(m)
        carts[i] += 1
else:
    print(*carts)