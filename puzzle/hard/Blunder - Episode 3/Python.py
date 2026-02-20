import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    points = []
    idx = 1
    for _ in range(N):
        points.append((float(input_data[idx]), float(input_data[idx+1])))
        idx += 2

    def get_log_f(name, n):
        if name == "O(1)": return 0.0
        if name == "O(log n)": return math.log(math.log(n)) if n > 1.1 else -10.0
        if name == "O(n)": return math.log(n)
        if name == "O(n log n)": return math.log(n) + math.log(math.log(n)) if n > 1.1 else math.log(n)
        if name == "O(n^2)": return 2.0 * math.log(n)
        if name == "O(n^2 log n)": return 2.0 * math.log(n) + (math.log(math.log(n)) if n > 1.1 else 0)
        if name == "O(n^3)": return 3.0 * math.log(n)
        if name == "O(2^n)": return n * math.log(2.0)
        return 0.0

    complexities = ["O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n^2)", "O(n^2 log n)", "O(n^3)", "O(2^n)"]
    
    best_name = ""
    min_variance = float('inf')

    for name in complexities:
        log_ratios = []
        for n, t in points:
            if t <= 0: t = 0.000001
            log_f = get_log_f(name, n)
            log_ratios.append(math.log(t) - log_f)
        
        avg_log_ratio = sum(log_ratios) / N
        variance = sum((lr - avg_log_ratio)**2 for lr in log_ratios) / N
        
        if variance < min_variance:
            min_variance = variance
            best_name = name

    print(best_name)

solve()