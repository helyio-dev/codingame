import sys

def solve():
    line1 = sys.stdin.readline()
    if not line1: return
    radius = int(line1.strip())
    center = sys.stdin.readline().strip()
    
    dp = [0] * (radius + 1)
    dp[0] = 1
    
    for char in center:
        pos = ord(char) - ord('a')
        
        dist_counts = {}
        for i in range(26):
            d = abs(i - pos)
            if d <= radius:
                dist_counts[d] = dist_counts.get(d, 0) + 1
        
        new_dp = [0] * (radius + 1)
        for d, count in dist_counts.items():
            for r in range(radius - d + 1):
                if dp[r] > 0:
                    new_dp[r + d] += dp[r] * count
        dp = new_dp
        
    print(sum(dp))

if __name__ == "__main__":
    solve()