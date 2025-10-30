N = int(input())
groups = [input().split(", ") for _ in range(N)]

def is_joey(kangaroo, joey):
    it = iter(kangaroo)
    return all(c in it for c in joey)

kangaroos = {}

for group in groups:
    for word in group:
        joeys = sorted([w for w in group if w != word and is_joey(word, w)])
        if joeys:
            kangaroos[word] = joeys

if not kangaroos:
    print("NONE")
else:
    for k in sorted(kangaroos):
        print(f"{k}: {', '.join(kangaroos[k])}")
