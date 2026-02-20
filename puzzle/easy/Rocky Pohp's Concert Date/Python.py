import sys
import math

def get_factors(n):
    for i in range(int(math.sqrt(n)), 0, -1):
        if n % i == 0:
            return i, n // i
    return 1, n

def solve():
    s_n = sys.stdin.read().strip()
    length = len(s_n)
    
    for i in range(1, length):
        part1 = s_n[:i]
        part2 = s_n[i:]
        
        if (part1.startswith('0') and len(part1) > 1) or (part2.startswith('0') and len(part2) > 1):
            continue
            
        a, b = int(part1), int(part2)
        product = a * b
        
        f1, f2 = get_factors(product)
        if (f1 == a and f2 == b) or (f1 == b and f2 == a):
            date_str = str(product).zfill(8)
            
            day = date_str[-2:]
            month = date_str[-4:-2]
            year = date_str[:-4]
            
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                print(f"{year.zfill(4)}-{month}-{day}")
                return

solve()