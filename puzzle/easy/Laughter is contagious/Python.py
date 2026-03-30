import sys

row = sys.stdin.readline().strip()
if row:
    p = [row[i:i+2] for i in range(0, len(row), 2)]
    n = len(p)

    def is_lol(s): return s.isupper()
    def is_might(s): return s[0].isupper() and s[1].islower()
    def is_sullen(s): return s.islower()

    lols = {s.upper() for s in p if is_lol(s)}
    for i in range(n):
        if p[i].upper() in lols:
            p[i] = p[i].upper()

    res = p[:]
    for i in range(n):
        if is_might(p[i]):
            sullen_count = 0
            if i > 0 and is_sullen(p[i-1]): sullen_count += 1
            if i < n - 1 and is_sullen(p[i+1]): sullen_count += 1
            
            if sullen_count <= 1:
                targets = []
                for d in range(1, 4):
                    if i - d >= 0 and is_lol(p[i-d]): targets.append(i-d)
                    if i + d < n and is_lol(p[i+d]): targets.append(i+d)
                    if targets: break
                
                if len(targets) == 1:
                    res[i] = p[targets[0]]
                elif len(targets) == 2:
                    res[i] = p[targets[0]][1] + p[targets[1]][0]

    print("".join(res))