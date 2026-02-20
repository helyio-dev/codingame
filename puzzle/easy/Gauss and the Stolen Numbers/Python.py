import sys

def solve():
    line1 = sys.stdin.readline()
    if not line1:
        return
    n = int(line1.strip())
    s_rem = int(sys.stdin.readline().strip())
    q_rem = int(sys.stdin.readline().strip())

    total_s = n * (n + 1) // 2
    total_q = n * (n + 1) * (2 * n + 1) // 6

    sum_missing = total_s - s_rem
    sum_sq_missing = total_q - q_rem

    prod_missing = (sum_missing**2 - sum_sq_missing) // 2

    delta = int((sum_missing**2 - 4 * prod_missing)**0.5 + 0.5)
    
    x = (sum_missing - delta) // 2
    y = (sum_missing + delta) // 2

    print(f"{x} {y}")

if __name__ == "__main__":
    solve()