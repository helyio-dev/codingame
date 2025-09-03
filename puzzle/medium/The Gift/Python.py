import sys

def solve():
    n = int(sys.stdin.readline())
    c = int(sys.stdin.readline())
    budgets = []
    for _ in range(n):
        budgets.append(int(sys.stdin.readline()))

    total_budget = sum(budgets)
    if total_budget < c:
        print("IMPOSSIBLE")
        return

    budgets.sort()
    contributions = [0] * n
    remaining_cost = c

    for i in range(n):
        fair_share = remaining_cost // (n - i)
        contribution = min(fair_share, budgets[i])
        contributions[i] = contribution
        remaining_cost -= contribution

    for contribution in contributions:
        print(contribution)

solve()