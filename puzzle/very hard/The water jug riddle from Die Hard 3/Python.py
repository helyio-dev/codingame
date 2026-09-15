from collections import deque

target = int(input())
containers_count = int(input())
buckets = []
for i in range(containers_count):
    buckets.append(int(input()))

queue = deque([((0,) * len(buckets), 0)])
seen = {(0,) * len(buckets)}
while queue:
    state, moves = queue.popleft()
    if target in state:
        print(moves)
        break

    for i, capacity in enumerate(buckets):
        new_state = list(state)
        new_state[i] = capacity
        new_state = tuple(new_state)

        if new_state not in seen:
            seen.add(new_state)
            queue.append((new_state, moves + 1))

        new_state = list(state)
        new_state[i] = 0
        new_state = tuple(new_state)
        if new_state not in seen:
            seen.add(new_state)
            queue.append((new_state, moves + 1))

        for j, capacity_j in enumerate(buckets):
            if i == j:
                continue
            amount = min(state[i], capacity_j - state[j])
            new_state = list(state)
            new_state[i] -= amount
            new_state[j] += amount
            new_state = tuple(new_state)
            if new_state not in seen:
                seen.add(new_state)
                queue.append((new_state, moves + 1))