keys = input()
left, right = [], []

for k in keys:
    if k == '<':
        if left: right.append(left.pop())
    elif k == '>':
        if right: left.append(right.pop())
    elif k == '-':
        if left: left.pop()
    else:
        left.append(k)

print(''.join(left + right[::-1]))
