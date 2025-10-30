N = int(input())
spiral = [[0]*N for _ in range(N)]
num = 1
top, left = 0, 0
bottom, right = N-1, N-1

while top <= bottom and left <= right:
    for j in range(left, right+1):
        spiral[top][j] = num
        num += 1
    top += 1
    for i in range(top, bottom+1):
        spiral[i][right] = num
        num += 1
    right -= 1
    for j in range(right, left-1, -1):
        spiral[bottom][j] = num
        num += 1
    bottom -= 1
    for i in range(bottom, top-1, -1):
        spiral[i][left] = num
        num += 1
    left += 1

S = 0
for i in range(N):
    S += spiral[i][i] + spiral[i][N-1-i]
if N % 2 == 1:
    S -= spiral[N//2][N//2]

print(S)
