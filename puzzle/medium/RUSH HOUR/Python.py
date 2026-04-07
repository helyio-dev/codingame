import sys
from collections import deque

def solve():
    n = int(input())
    initial_cars = []
    for _ in range(n):
        car_data = input().split()
        initial_cars.append((int(car_data[0]), int(car_data[1]), int(car_data[2]), int(car_data[3]), car_data[4]))

    initial_state = tuple(sorted((c[0], c[1], c[2], c[3], c[4]) for c in initial_cars))
    
    queue = deque([(initial_state, [])])
    visited = {initial_state}

    while queue:
        current_state, path = queue.popleft()

        red_car = next(c for c in current_state if c[0] == 0)
        if red_car[1] == 4:
            for move in path:
                print(move)
            return

        grid = [[-1 for _ in range(6)] for _ in range(6)]
        for cid, cx, cy, clen, caxis in current_state:
            for i in range(clen):
                if caxis == 'H':
                    grid[cy][cx + i] = cid
                else:
                    grid[cy + i][cx] = cid

        for i, car in enumerate(current_state):
            cid, cx, cy, clen, caxis = car
            
            if caxis == 'H':
                if cx > 0 and grid[cy][cx - 1] == -1:
                    new_car = (cid, cx - 1, cy, clen, caxis)
                    new_state = list(current_state)
                    new_state[i] = new_car
                    new_state_t = tuple(sorted(new_state))
                    if new_state_t not in visited:
                        visited.add(new_state_t)
                        queue.append((new_state_t, path + [f"{cid} LEFT"]))
                
                if cx + clen < 6 and grid[cy][cx + clen] == -1:
                    new_car = (cid, cx + 1, cy, clen, caxis)
                    new_state = list(current_state)
                    new_state[i] = new_car
                    new_state_t = tuple(sorted(new_state))
                    if new_state_t not in visited:
                        visited.add(new_state_t)
                        queue.append((new_state_t, path + [f"{cid} RIGHT"]))
            else:
                if cy > 0 and grid[cy - 1][cx] == -1:
                    new_car = (cid, cx, cy - 1, clen, caxis)
                    new_state = list(current_state)
                    new_state[i] = new_car
                    new_state_t = tuple(sorted(new_state))
                    if new_state_t not in visited:
                        visited.add(new_state_t)
                        queue.append((new_state_t, path + [f"{cid} UP"]))
                
                if cy + clen < 6 and grid[cy + clen][cx] == -1:
                    new_car = (cid, cx, cy + 1, clen, caxis)
                    new_state = list(current_state)
                    new_state[i] = new_car
                    new_state_t = tuple(sorted(new_state))
                    if new_state_t not in visited:
                        visited.add(new_state_t)
                        queue.append((new_state_t, path + [f"{cid} DOWN"]))

solve()