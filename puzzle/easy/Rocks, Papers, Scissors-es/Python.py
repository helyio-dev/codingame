n = int(input())
moves = [input().strip() for _ in range(n)]

beat = {'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper': 'Rock'}
options = ['Rock', 'Paper', 'Scissors']

max_wins = -1
best_move = ''
best_start = 0

for start in range(n):
    for my_move in options:

        if moves[start] != beat[my_move]:
            continue
        wins = 1
        idx = (start + 1) % n
        while idx != start:
            if moves[idx] == beat[my_move]:
                wins += 1
            elif moves[idx] == my_move:
                pass  
            else:
                break 
            idx = (idx + 1) % n
        if wins > max_wins or (wins == max_wins and start < best_start):
            max_wins = wins
            best_move = my_move
            best_start = start

print(best_move)
print(best_start)
