from collections import deque

valid = set([i for i in "[]{}()<>"])
swapper = {"{":"}", "[":"]", "(":")", "<":">"}

n = int(input())
for i in range(n):
    expression = input()
    brackets = deque([])
    for char in expression:
        if char in valid:
            char = swapper[char] if char in swapper else char
            brackets.append(char)
            while len(brackets) > 1 and brackets[-1] == brackets[-2]:
                brackets.pop()
                brackets.pop()

    if not brackets:
        print("true")
    else:
        print("false")