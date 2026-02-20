import sys

def solve():
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line)
    target = 50 - n
    
    dp = [0] * (target + 1)
    dp[0] = 1
    
    for i in range(1, target + 1):
        for score in range(1, 13):
            if i >= score:
                options = 2 if score > 1 else 1
                dp[i] += dp[i - score] * options
                
    print(dp[target])

solve()