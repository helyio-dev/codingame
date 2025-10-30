a, b = map(int, input().split())
x, y = a, b
while b != 0:
    q = a // b
    r = a % b
    print(f"{a}={b}*{q}+{r}")
    a, b = b, r
print(f"GCD({x},{y})={a}")
