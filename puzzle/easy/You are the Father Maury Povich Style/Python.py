mother_line = input().split(":", 1)[1].strip().split()
child_line = input().split(":", 1)[1].strip().split()
n = int(input())
for _ in range(n):
    line = input()
    name, chroms = line.split(":", 1)
    name = name.strip()
    chroms = chroms.strip().split()
    ok = True
    for mc, cc, fc in zip(mother_line, child_line, chroms):
        if not (cc[0] in mc and cc[1] in fc or cc[1] in mc and cc[0] in fc):
            ok = False
            break
    if ok:
        print(f"{name}, you are the father!")
        break
