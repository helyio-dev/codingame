import sys
import math

n = int(input())
values = list(map(int, input().split()))

max_price = values[0]
max_loss = 0

for price in values[1:]:
    if price > max_price:
        max_price = price
    else:
        loss = price - max_price
        if loss < max_loss:
            max_loss = loss

print(max_loss)
