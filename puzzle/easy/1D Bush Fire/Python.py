N = int(input())
for _ in range(N):
    line = input().strip()
    i = 0
    drops = 0
    while i < len(line):
        if line[i] == 'f':
            drops += 1
            i += 3
        else:
            i += 1
    print(drops)
