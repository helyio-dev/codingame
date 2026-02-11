import sys
import math

def solve():
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line.strip())
    
    for _ in range(n):
        coords = sys.stdin.readline().split()
        if not coords:
            break
        x = int(coords[0])
        y = int(coords[1])
        
        common = math.gcd(x, y)
        result = x + y - common
        print(result)

solve()