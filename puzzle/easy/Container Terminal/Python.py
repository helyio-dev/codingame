N = int(input())
for _ in range(N):
    line = input().strip()
    stacks = []
    for c in line:
        placed = False
        for i in range(len(stacks)):
            if stacks[i][-1] >= c:
                stacks[i].append(c)
                placed = True
                break
        if not placed:
            stacks.append([c])
    print(len(stacks))
