import sys
from collections import Counter

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    try:
        n = int(input_data[0].strip())
    except:
        return
    
    drugs = [input_data[i+1].strip() for i in range(n)]
    cnts = [Counter(d.lower()) for d in drugs]
    adj = [0] * n
    
    for i in range(n):
        for j in range(n):
            if i == j: continue
            c1, c2 = cnts[i], cnts[j]
            common = 0
            for char in c1:
                if char in c2:
                    common += min(c1[char], c2[char])
            if common < 3:
                adj[i] |= (1 << j)

    ans = 0

    def bk(r_cnt, p, x):
        nonlocal ans
        if not p:
            if not x:
                if r_cnt > ans:
                    ans = r_cnt
            return
        
        if r_cnt + bin(p).count('1') <= ans:
            return

        u = (p | x).bit_length() - 1
        cand = p & ~adj[u]
        
        while cand:
            v = cand.bit_length() - 1
            bk(r_cnt + 1, p & adj[v], x & adj[v])
            p &= ~(1 << v)
            x |= (1 << v)
            cand &= ~(1 << v)

    bk(0, (1 << n) - 1, 0)
    print(ans)

if __name__ == "__main__":
    solve()