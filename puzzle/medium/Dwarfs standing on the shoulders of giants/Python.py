import sys
import math
from collections import defaultdict

n = int(input())
influences = defaultdict(list)
nodes = set()

for _ in range(n):
    x, y = [int(j) for j in input().split()]
    influences[x].append(y)
    nodes.add(x)
    nodes.add(y)

max_length = 0
memo = {}

def dfs(person):
    if person in memo:
        return memo[person]
    max_depth = 0
    for neighbor in influences[person]:
        depth = dfs(neighbor)
        if depth > max_depth:
            max_depth = depth
    memo[person] = max_depth + 1
    return memo[person]

for person in nodes:
    if person not in memo:
        dfs(person)

if memo:
    print(max(memo.values()))
else:
    print(0)