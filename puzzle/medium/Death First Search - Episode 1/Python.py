import sys
import math

n, l, e = [int(i) for i in input().split()]

links = {i: set() for i in range(n)}
for _ in range(l):
    n1, n2 = [int(j) for j in input().split()]
    links[n1].add(n2)
    links[n2].add(n1)

gateways = set()
for _ in range(e):
    ei = int(input())
    gateways.add(ei)

while True:
    si = int(input())  

    found = False
    for neighbor in links[si]:
        if neighbor in gateways:
            print(f"{si} {neighbor}")
            found = True
            break

    if not found:
        for gw in gateways:
            for neighbor in links[gw]:
                print(f"{neighbor} {gw}")
                found = True
                break
            if found:
                break
