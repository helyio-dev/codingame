from sys import stdin

def read_compressed():
    data = list(map(int, stdin.readline().split()))
    runs = []
    i = 0
    while i < len(data):
        count = data[i]
        val = data[i+1]
        runs.append([count, val])
        i += 2
    return runs

A = read_compressed()
B = read_compressed()

i = j = 0
dot = 0

while i < len(A) and j < len(B):
    count = min(A[i][0], B[j][0])
    dot += count * A[i][1] * B[j][1]
    A[i][0] -= count
    B[j][0] -= count
    if A[i][0] == 0:
        i += 1
    if B[j][0] == 0:
        j += 1

print(dot)
