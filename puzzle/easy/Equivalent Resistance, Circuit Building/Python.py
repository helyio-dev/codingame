N = int(input())
resistors = {}
for _ in range(N):
    name, val = input().split()
    resistors[name] = float(val)
expr = input().split()

def evaluate(tokens):
    stack = []
    for token in tokens:
        if token in '([':
            stack.append(token)
        elif token in ')]':
            temp = []
            while stack and isinstance(stack[-1], float):
                temp.append(stack.pop())
            temp.reverse()
            start = stack.pop()
            if start == '(':
                stack.append(sum(temp))
            else:
                stack.append(1/sum(1/x for x in temp))
        else:
            stack.append(resistors[token])
    return stack[0]

print(round(evaluate(expr)*10)/10)
