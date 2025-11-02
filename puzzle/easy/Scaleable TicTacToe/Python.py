n, g = map(int, input().split())
b = [list(input()) for _ in range(n)]
def check():
    for i in range(n):
        for j in range(n):
            if b[i][j] == ' ': continue
            p = b[i][j]
            if j + g <= n and all(b[i][j+k]==p for k in range(g)):
                for k in range(g): b[i][j+k] = '-'
                return p
            if i + g <= n and all(b[i+k][j]==p for k in range(g)):
                for k in range(g): b[i+k][j] = '|'
                return p
            if i + g <= n and j + g <= n and all(b[i+k][j+k]==p for k in range(g)):
                for k in range(g): b[i+k][j+k] = '\\'
                return p
            if i + g <= n and j - g + 1 >= 0 and all(b[i+k][j-k]==p for k in range(g)):
                for k in range(g): b[i+k][j-k] = '/'
                return p
    return None
winner = check()
for row in b: print(''.join(row))
if winner: print(f"The winner is {winner}.")
elif any(' ' in row for row in b): print("The game isn't over yet!")
else: print("The game ended in a draw!")
