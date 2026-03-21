import sys

prog = input().split()
prog = [int(x, 16) for x in prog]

r = [0, 0, 0, 0]
i = 0

while i < len(prog):
    op = prog[i]

    if op == 0xFF:
        break

    if op == 0x01:
        x = prog[i+1]
        v = prog[i+2]
        r[x] = v % 256
        i += 3
    elif op == 0x02:
        x = prog[i+1]
        y = prog[i+2]
        r[x] = (r[x] + r[y]) % 256
        i += 3
    elif op == 0x03:
        x = prog[i+1]
        y = prog[i+2]
        r[x] = (r[x] - r[y]) % 256
        i += 3
    elif op == 0x04:
        x = prog[i+1]
        y = prog[i+2]
        r[x] = (r[x] * r[y]) % 256
        i += 3
    elif op == 0x05:
        x = prog[i+1]
        r[x] = (r[x] + 1) % 256
        i += 2
    elif op == 0x06:
        x = prog[i+1]
        r[x] = (r[x] - 1) % 256
        i += 2

for v in r:
    print(v)