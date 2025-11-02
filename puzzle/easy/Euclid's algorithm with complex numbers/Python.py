xa, ya = map(int, input().split())
xb, yb = map(int, input().split())

a = complex(xa, ya)
b = complex(xb, yb)

orig_a, orig_b = a, b

def closest_int(x):
    if x - int(x) == 0.5:
        return int(x) + 1
    if x - int(x) == -0.5:
        return int(x)
    return int(round(x))

while b != 0:
    c = a / b
    cx = closest_int(c.real)
    cy = closest_int(c.imag)
    q = complex(cx, cy)
    r = a - q * b
    print(f"{a} = {b} * {q} + {r}")
    a, b = b, r

print(f"GCD({orig_a}, {orig_b}) = {a}")
