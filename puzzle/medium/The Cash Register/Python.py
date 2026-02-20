import sys
from collections import deque

def solve():
    reg_line = sys.stdin.readline()
    if not reg_line: return
    coins = sorted([int(c) for c in reg_line.split()], reverse=True)
    
    goal_line = sys.stdin.readline()
    if not goal_line: return
    goal = int(goal_line)

    if goal == 0:
        print(0)
        return

    queue = deque([(0, [])])
    visited = {0}

    while queue:
        current_sum, current_coins = queue.popleft()

        for coin in coins:
            next_sum = current_sum + coin
            
            if next_sum == goal:
                res = current_coins + [coin]
                print(*(sorted(res, reverse=True)))
                return
            
            if next_sum < goal and next_sum not in visited:
                visited.add(next_sum)
                queue.append((next_sum, current_coins + [coin]))

    print("IMPOSSIBLE")

if __name__ == "__main__":
    solve()