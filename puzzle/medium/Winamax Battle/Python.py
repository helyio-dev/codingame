import sys

order = {str(i): i for i in range(2, 11)}
order.update({"J":11, "Q":12, "K":13, "A":14})

n = int(input())
p1 = [input() for _ in range(n)]
m = int(input())
p2 = [input() for _ in range(m)]

turns = 0

while p1 and p2:
    turns += 1
    pile1 = []
    pile2 = []

    def battle():
        if len(p1) < 4 or len(p2) < 4:
            print("PAT")
            sys.exit()
        for _ in range(3):
            pile1.append(p1.pop(0))
            pile2.append(p2.pop(0))

    while True:
        if not p1 or not p2:
            break
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        pile1.append(c1)
        pile2.append(c2)
        v1 = order[c1[:-1]]
        v2 = order[c2[:-1]]
        if v1 > v2:
            p1.extend(pile1 + pile2)
            break
        elif v1 < v2:
            p2.extend(pile1 + pile2)
            break
        else:
            if len(p1) < 3 or len(p2) < 3:
                print("PAT")
                sys.exit()
            battle()

if not p2:
    print("1", turns)
elif not p1:
    print("2", turns)
else:
    print("PAT")
