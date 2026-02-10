import sys

def solve():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    
    invoices = []
    for _ in range(n):
        invoices.append(int(sys.stdin.readline()))
        
    payments = []
    for _ in range(m):
        payments.append(int(sys.stdin.readline()))

    def find_combination(target, available_invoices):
        def backtrack(remaining, start, path):
            if remaining == 0:
                return path
            if remaining < 0:
                return None
            
            for i in range(start, len(available_invoices)):
                res = backtrack(remaining - available_invoices[i], i + 1, path + [available_invoices[i]])
                if res is not None:
                    return res
            return None
        
        return backtrack(target, 0, [])

    current_invoices = list(invoices)
    for i in range(m):
        payment = payments[i]
        letter = chr(65 + i)
        
        match = find_combination(payment, current_invoices)
        
        if match:
            for val in match:
                current_invoices.remove(val)
            
            match_str = " ".join(map(str, match))
            print(f"{letter} {payment} - {match_str}")

solve()