from collections import deque

def main():
    H, W = map(int, input().split())
    grid = [[int(ch) for ch in input().strip()] for _ in range(H)]
    R, C = map(int, input().split())

    overloaded = set()
    queue = deque()
    queue.append((R, C))

    while queue:
        r, c = queue.popleft()
        if (r, c) in overloaded:
            continue
        grid[r][c] += 1
        if grid[r][c] > 9:
            grid[r][c] = 0
            overloaded.add((r, c))
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < H and 0 <= nc < W and (nr, nc) not in overloaded:
                        queue.append((nr, nc))

    for row in grid:
        print(''.join(str(x) for x in row))

if __name__ == "__main__":
    main()