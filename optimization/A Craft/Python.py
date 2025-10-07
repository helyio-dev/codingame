g=[input()for _ in range(10)]
print(*[f"{x} {y} {d}" for _ in range(int(input())) for x,y,d in [input().split()] if g[int(y)][int(x)]=='.'])
