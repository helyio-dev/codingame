import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    height = int(input_data[0])
    increments = []
    idx = 1
    for i in range(height):
        increments.append([int(d) for d in input_data[idx]])
        idx += 1
        
    prizes = []
    for i in range(height + 1):
        prizes.append(int(input_data[idx]))
        idx += 1

    dp = [{} for _ in range(height)]
    
    dp[0][0] = increments[0][0]
    
    for r in range(1, height):
        for c, current_sum in dp[r-1].items():
            for move in [0, 1]:
                nc = c + move
                val = current_sum + increments[r][nc]
                if nc not in dp[r]:
                    dp[r][nc] = val
                else:
                    dp[r][nc] = max(dp[r][nc], val)
                    
    max_jackpot = 0
    final_row = dp[height - 1]
    
    for c, total_sum in final_row.items():
        for move in [0, 1]:
            prize_idx = c + move
            jackpot = total_sum * prizes[prize_idx]
            if jackpot > max_jackpot:
                max_jackpot = jackpot
                
    print(max_jackpot)

if __name__ == "__main__":
    solve()