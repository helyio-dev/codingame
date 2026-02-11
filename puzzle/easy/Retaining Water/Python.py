import heapq

def solve():
    n = int(input())
    grid = [[ord(c) - ord('A') + 1 for c in input()] for _ in range(n)]
    
    visited = [[False] * n for _ in range(n)]
    heap = []
    
    for r in range(n):
        for c in range(n):
            if r == 0 or r == n - 1 or c == 0 or c == n - 1:
                heapq.heappush(heap, (grid[r][c], r, c))
                visited[r][c] = True
                
    water_volume = 0
    
    while heap:
        height, r, c = heapq.heappop(heap)
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                
                if grid[nr][nc] < height:
                    water_volume += height - grid[nr][nc]
                    heapq.heappush(heap, (height, nr, nc))
                else:
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))
                
    print(water_volume)

solve()