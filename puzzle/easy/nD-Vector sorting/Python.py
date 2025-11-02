D = int(input())
N = int(input())
perm = [int(x)-1 for x in input().split()]
vectors = [list(map(int, input().split())) for _ in range(N)]
indexed = list(enumerate(vectors, 1))
indexed.sort(key=lambda x: [x[1][i] for i in perm])
print(" ".join(str(i) for i, _ in indexed))
