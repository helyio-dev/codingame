import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    sr, sc = int(input_data[1]) - 1, int(input_data[2]) - 1
    gr, gc = int(input_data[3]) - 1, int(input_data[4]) - 1
    grid = input_data[5:]

    if grid[sr][sc] != grid[gr][gc]:
        return

    if abs(sr - gr) + abs(sc - gc) == 1:
        print(2)
        return

    queue = deque([(sr, sc, gr, gc, 2)])
    visited = {(sr, sc, gr, gc)}

    while queue:
        r1, c1, r2, c2, d = queue.popleft()
        
        for dr1, dc1 in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr1, nc1 = r1 + dr1, c1 + dc1
            if 0 <= nr1 < n and 0 <= nc1 < n:
                for dr2, dc2 in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr2, nc2 = r2 + dr2, c2 + dc2
                    if 0 <= nr2 < n and 0 <= nc2 < n:
                        if grid[nr1][nc1] == grid[nr2][nc2]:
                            
                            if (nr1, nc1) == (nr2, nc2):
                                print(d + 1)
                                return
                            
                            if abs(nr1 - nr2) + abs(nc1 - nc2) == 1:
                                print(d + 2)
                                return
                                
                            state = (nr1, nc1, nr2, nc2)
                            if state not in visited:
                                visited.add(state)
                                queue.append((nr1, nc1, nr2, nc2, d + 2))

if __name__ == "__main__":
    solve()