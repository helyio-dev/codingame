import sys

r, s = [int(i) for i in input().split()]
removed = set()
for _ in range(r):
    desc = input().strip()
    ranks = set()
    suits = set()
    for c in desc:
        if c in '23456789TJQKA':
            ranks.add(c)
        elif c in 'CDHS':
            suits.add(c)
    if not ranks: ranks = set('23456789TJQKA')
    if not suits: suits = set('CDHS')
    for rank in ranks:
        for suit in suits:
            removed.add(rank + suit)

sought = set()
for _ in range(s):
    desc = input().strip()
    ranks = set()
    suits = set()
    for c in desc:
        if c in '23456789TJQKA':
            ranks.add(c)
        elif c in 'CDHS':
            suits.add(c)
    if not ranks: ranks = set('23456789TJQKA')
    if not suits: suits = set('CDHS')
    for rank in ranks:
        for suit in suits:
            sought.add(rank + suit)

remaining = 52 - len(removed)
matches = len(sought - removed)
odds = (matches / remaining) * 100 if remaining else 0

print(f"{int(round(odds))}%")
