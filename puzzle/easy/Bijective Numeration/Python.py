def decimary_to_decimal(s):
    result = 0
    for ch in s:
        if ch == 'A':
            digit = 10
        else:
            digit = int(ch)
        result = result * 10 + digit
    return result

def decimal_to_decimary(n):
    if n == 0:
        return ''
    digits = []
    while n > 0:
        rem = n % 10
        if rem == 0:
            rem = 10
            n -= 10
        if rem == 10:
            digits.append('A')
        else:
            digits.append(str(rem))
        n //= 10
    return ''.join(digits[::-1])

count = int(input())
nums = input().split()
total = sum(decimary_to_decimal(x) for x in nums)
print(decimal_to_decimary(total))
