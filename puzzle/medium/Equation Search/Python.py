import sys

def solve():
    n_in = sys.stdin.readline()
    if not n_in: return
    n = int(n_in)
    right_sides = sorted(list(map(int, sys.stdin.readline().split())))
    counts = list(map(int, sys.stdin.readline().split()))
    
    possible_eqs_by_rhs = {}
    for rs in right_sides:
        eqs = []
        for a in range(1, 10):
            for b in range(a, 10):
                if a + b == rs:
                    eqs.append((a, "+", b))
                if a * b == rs:
                    eqs.append((a, "x", b))
        possible_eqs_by_rhs[rs] = eqs

    solutions = []
    current_solution = {}
    current_counts = [0] * 9

    def backtrack(rhs_idx):
        if rhs_idx == n:
            if all(current_counts[i] == counts[i] for i in range(9)):
                solutions.append(dict(current_solution))
            return

        target_rs = right_sides[rhs_idx]
        for a, op, b in possible_eqs_by_rhs[target_rs]:
            if current_counts[a-1] + 1 > counts[a-1]: continue
            current_counts[a-1] += 1
            
            if current_counts[b-1] + 1 > counts[b-1]:
                current_counts[a-1] -= 1
                continue
            
            current_counts[b-1] += 1
            current_solution[target_rs] = (a, op, b)
            
            backtrack(rhs_idx + 1)
            
            current_counts[b-1] -= 1
            current_counts[a-1] -= 1

    backtrack(0)

    print(len(solutions))
    if len(solutions) == 1:
        sol = solutions[0]
        for rs in right_sides:
            a, op, b = sol[rs]
            print(f"{a} {op} {b} = {rs}")

if __name__ == "__main__":
    solve()