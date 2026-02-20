import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    next(it)
    w = int(next(it))
    h = int(next(it))
    next(it)
    target_w = int(next(it))
    next(it)
    
    pixels = []
    for _ in range(h):
        row = []
        for _ in range(w):
            row.append(int(next(it)))
        pixels.append(row)

    current_w = w
    while current_w > target_w:
        energy = [[0] * current_w for _ in range(h)]
        for y in range(h):
            for x in range(current_w):
                dx = 0
                if 0 < x < current_w - 1:
                    dx = abs(pixels[y][x+1] - pixels[y][x-1])
                dy = 0
                if 0 < y < h - 1:
                    dy = abs(pixels[y+1][x] - pixels[y-1][x])
                energy[y][x] = dx + dy

        dp = [[0] * current_w for _ in range(h)]
        for x in range(current_w):
            dp[0][x] = energy[0][x]

        for y in range(1, h):
            for x in range(current_w):
                prev_min = dp[y-1][x]
                if x > 0:
                    prev_min = min(prev_min, dp[y-1][x-1])
                if x < current_w - 1:
                    prev_min = min(prev_min, dp[y-1][x+1])
                dp[y][x] = energy[y][x] + prev_min

        min_energy_dp = min(dp[h-1])
        best_x = -1
        for x in range(current_w):
            if dp[h-1][x] == min_energy_dp:
                best_x = x
                break
        
        path = [0] * h
        path[h-1] = best_x
        total_energy = energy[h-1][best_x]
        
        curr_x = best_x
        for y in range(h-2, -1, -1):
            next_x = -1
            min_prev_val = float('inf')
            
            for dx in [-1, 0, 1]:
                tx = curr_x + dx
                if 0 <= tx < current_w:
                    if dp[y][tx] < min_prev_val:
                        min_prev_val = dp[y][tx]
                        next_x = tx
            
            curr_x = next_x
            path[y] = curr_x
            total_energy += energy[y][curr_x]

        print(total_energy)
        for y in range(h):
            pixels[y].pop(path[y])
        
        current_w -= 1

if __name__ == "__main__":
    solve()