n = int(input())
steps = 0
while n > 0:
    if n % 2 == 0:
        n //= 2
    elif n == 3 or n % 4 == 1:
        n -= 1
    else:
        n += 1
    steps += 1
print(steps)
