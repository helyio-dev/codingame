import sys
import math

message = input()

binary_str = ''.join(format(ord(c), '07b') for c in message)
result = []
i = 0

while i < len(binary_str):
    current_bit = binary_str[i]
    count = 1
    while i + count < len(binary_str) and binary_str[i + count] == current_bit:
        count += 1
    
    prefix = '0' if current_bit == '1' else '00'
    result.append(f"{prefix} {'0' * count}")
    i += count

print(' '.join(result))
