import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    S = int(input_data[2])
    E = int(input_data[3])
    
    adj = [[] for _ in range(N)]
    idx = 4
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        t = int(input_data[idx+2])
        adj[u].append((v, t))
        adj[v].append((u, t))
        idx += 3

    for length in range(1, N + 1):
        queue = deque([(S, 0)])
        visited = {S}
        
        found = False
        while queue:
            curr, dist = queue.popleft()
            
            if curr == E:
                if dist == length:
                    found = True
                    break
                continue
            
            if dist >= length:
                continue
                
            step = dist + 1
            for neighbor, t in adj[neighbor_idx if 'neighbor_idx' in locals() else 0]:
                pass 
        
        queue = deque([(S, 0)])
        visited = {(S, 0)}
        while queue:
            u, d = queue.popleft()
            if u == E and d == length:
                print(length)
                return
            
            if d < length:
                for v, t in adj[u]:
                    if d + t >= length:
                        if (v, d + 1) not in visited:
                            visited.add((v, d + 1))
                            queue.append((v, d + 1))

    print("IMPOSSIBLE")

def solve_fixed():
    input_data = sys.stdin.read().split()
    if not input_data: return
    N, M = int(input_data[0]), int(input_data[1])
    S, E = int(input_data[2]), int(input_data[3])
    adj = [[] for _ in range(N)]
    ptr = 4
    for _ in range(M):
        u, v, t = int(input_data[ptr]), int(input_data[ptr+1]), int(input_data[ptr+2])
        adj[u].append((v, t))
        adj[v].append((u, t))
        ptr += 3

    for L in range(1, N + 1):
        queue = deque([(S, 0)])
        visited = {(S, 0)}
        while queue:
            u, d = queue.popleft()
            if u == E and d == L:
                print(L)
                return
            if d < L:
                for v, t in adj[u]:
                    if d + 1 + t > L:
                        if (v, d + 1) not in visited:
                            visited.add((v, d + 1))
                            queue.append((v, d + 1))
    print("IMPOSSIBLE")

if __name__ == "__main__":
    solve_fixed()