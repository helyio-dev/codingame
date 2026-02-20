import sys
from math import gcd

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    counts = {}
    for i in range(1, n + 1):
        v = int(input_data[i])
        counts[v] = counts.get(v, 0) + 1
    
    freqs = list(counts.values())
    g_all = freqs[0]
    for f in freqs[1:]:
        g_all = gcd(g_all, f)
    
    mod = 10**9 + 7
    
    fact = [1] * (n + 1)
    inv = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i-1] * i) % mod
        
    inv[n] = pow(fact[n], mod - 2, mod)
    for i in range(n - 1, -1, -1):
        inv[i] = (inv[i+1] * (i+1)) % mod

    def phi(m):
        res = m
        p = 2
        temp = m
        while p * p <= temp:
            if temp % p == 0:
                while temp % p == 0:
                    temp //= p
                res -= res // p
            p += 1
        if temp > 1:
            res -= res // temp
        return res

    total = 0
    for d in range(1, g_all + 1):
        if g_all % d == 0:
            num = fact[n // d]
            den = 1
            for f in freqs:
                den = (den * inv[f // d]) % mod
            
            term = (num * den) % mod
            total = (total + phi(d) * term) % mod
            
    print((total * pow(n, mod - 2, mod)) % mod)

if __name__ == "__main__":
    solve()