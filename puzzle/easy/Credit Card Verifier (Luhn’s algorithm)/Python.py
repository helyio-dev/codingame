import sys
import math

def quersum(number) -> int:
    res = 0
    for digit in str(number):
        res += int(digit)
    return res

n = int(input())
for i in range(n):
    card = input()

    card = card.replace(' ', '')
    cardRevert = card[::-1]

    sum = 0
    isOdd = True
    for number in cardRevert:
        if isOdd:
            sum += int(number)
        else:
            sum += quersum(2 * int(number))
            
        isOdd = not isOdd

    if sum % 10 == 0:
        print("YES")
    else:
        print("NO")