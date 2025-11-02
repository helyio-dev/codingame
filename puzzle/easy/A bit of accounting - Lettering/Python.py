from itertools import combinations

N = int(input())
M = int(input())
invoices = [int(input()) for _ in range(N)]
payments = [int(input()) for _ in range(M)]

used = [False] * N
letter = ord('A')

for p in payments:
    found = False
    for i, inv in enumerate(invoices):
        if not used[i] and inv == p:
            print(f"{chr(letter)} {p} - {inv}")
            used[i] = True
            found = True
            break
    if found:
        letter += 1
        continue
    indices = [i for i, u in enumerate(used) if not u]
    for r in range(2, len(indices)+1):
        for combo in combinations(indices, r):
            if sum(invoices[i] for i in combo) == p:
                matched = [invoices[i] for i in combo]
                print(f"{chr(letter)} {p} - {' '.join(map(str, matched))}")
                for i in combo:
                    used[i] = True
                found = True
                break
        if found:
            break
    letter += 1
