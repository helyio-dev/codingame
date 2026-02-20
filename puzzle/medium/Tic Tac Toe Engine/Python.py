import sys

def check_winner(board):
    lines = []
    for i in range(3):
        lines.append(board[i*3:(i+1)*3])
        lines.append(board[i::3])
    lines.append(board[0::4])
    lines.append(board[2:7:2])
    
    for line in lines:
        if line[0] != '.' and line[0] == line[1] == line[2]:
            return line[0]
    if '.' not in board:
        return 'Draw'
    return None

def minimax(board, player, engine, depth):
    winner = check_winner(board)
    if winner == engine:
        return 10 - depth
    if winner == ('O' if engine == 'X' else 'X'):
        return depth - 10
    if winner == 'Draw':
        return 0

    scores = []
    opponent = 'O' if player == 'X' else 'X'
    
    for i in range(9):
        if board[i] == '.':
            next_board = list(board)
            next_board[i] = player
            score = minimax("".join(next_board), opponent, engine, depth + 1)
            scores.append(score)
            
    return max(scores) if player == engine else min(scores)

def solve():
    engine = sys.stdin.readline().strip()
    board_str = "".join([sys.stdin.readline().strip() for _ in range(3)])
    
    if check_winner(board_str):
        for i in range(0, 9, 3):
            print(board_str[i:i+3])
        return

    cell_values = [8, 4, 7, 3, 9, 2, 6, 1, 5]
    best_score = -float('inf')
    best_move = -1
    
    opponent = 'O' if engine == 'X' else 'X'
    
    for i in range(9):
        if board_str[i] == '.':
            temp_board = list(board_str)
            temp_board[i] = engine
            score = minimax("".join(temp_board), opponent, engine, 1)
            
            if score > best_score:
                best_score = score
                best_move = i
            elif score == best_score:
                if cell_values[i] > cell_values[best_move]:
                    best_move = i
                    
    final_board = list(board_str)
    if best_move != -1:
        final_board[best_move] = engine
        
    res = "".join(final_board)
    for i in range(0, 9, 3):
        print(res[i:i+3])

if __name__ == "__main__":
    solve()