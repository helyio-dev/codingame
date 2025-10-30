from collections import defaultdict

M, N, P = map(int, input().split())
countA, countB = map(int, input().split())

A = defaultdict(list)
for _ in range(countA):
    i, j, v = input().split()
    A[int(i)].append((int(j), float(v)))

B = defaultdict(list)
for _ in range(countB):
    j, k, v = input().split()
    B[int(j)].append((int(k), float(v)))

C = defaultdict(float)

for i in A:
    for j, va in A[i]:
        if j in B:
            for k, vb in B[j]:
                C[(i, k)] += va * vb

for (i, k) in sorted(C):
    if C[(i, k)] != 0:
        print(i, k, C[(i, k)])
