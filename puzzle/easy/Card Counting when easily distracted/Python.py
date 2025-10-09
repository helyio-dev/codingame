s = input().strip()
b = int(input())
valid = set("A23456789TJQK")
values = {**{str(i): i for i in range(2, 10)}, **dict.fromkeys("TJQK", 10), "A": 1}
deck = {c: 4 for c in values}

for part in s.split('.'):
    if part and all(ch in valid for ch in part):
        for ch in part:
            if deck[ch] > 0:
                deck[ch] -= 1

total = sum(deck.values())
below = sum(v for c, v in deck.items() if values[c] < b)
count_below = sum(deck[c] for c in deck if values[c] < b)
print(f"{round(count_below / total * 100)}%")
