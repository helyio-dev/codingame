import sys
import math

r = int(input())
l = int(input())

sequence = [str(r)]
for _ in range(l - 1):
    current = sequence[-1].split()
    next_seq = []
    i = 0
    while i < len(current):
        count = 1
        while i + count < len(current) and current[i] == current[i + count]:
            count += 1
        next_seq.extend([str(count), current[i]])
        i += count
    sequence.append(' '.join(next_seq))
print(sequence[l - 1])
