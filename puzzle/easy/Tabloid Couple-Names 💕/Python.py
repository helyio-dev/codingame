import sys
import math

def merge(a, b):
    A = a.lower()
    B = b.lower()
    res = {}
    max_overlap = 0

    for i in range(len(A)):
        for j in range(len(B)):
            k = 0
            while i + k < len(A) and j + k < len(B) and A[i + k] == B[j + k]:
                k += 1
            if k > 0:
                left = a[:i]
                mid = a[i:i+k]
                right = b[j+k:]
                if left and right:
                    name = left + mid + right
                    if len(name) >= min(len(a), len(b)) and name.lower() != A and name.lower() != B:
                        if k > max_overlap:
                            max_overlap = k
                            res = {}
                        if k == max_overlap:
                            res[name.lower()] = name
    return max_overlap, res

def solve(a, b):
    k1, r1 = merge(a, b)
    k2, r2 = merge(b, a)

    max_overlap = max(k1, k2)
    res = {}

    if k1 == max_overlap:
        res.update(r1)
    if k2 == max_overlap:
        res.update(r2)

    if max_overlap == 0:
        return ["NONE"]

    out = sorted([v.capitalize() for v in res.values()])
    return out if out else ["NONE"]

n = int(input())
for _ in range(n):
    s = input().split()
    a = s[0]
    b = s[2]
    ans = solve(a, b)
    print(f"{a} plus {b} = {' '.join(ans)}")