b=[list(input()) for _ in range(8)]
cols,diag1,diag2=set(),set(),set()
for r in range(8):
    for c in range(8):
        if b[r][c]=='Q':
            cols.add(c)
            diag1.add(r-c)
            diag2.add(r+c)
def solve(r):
    if r==8:return True
    if 'Q' in b[r]:
        return solve(r+1)
    for c in range(8):
        if c not in cols and r-c not in diag1 and r+c not in diag2:
            b[r][c]='Q'
            cols.add(c);diag1.add(r-c);diag2.add(r+c)
            if solve(r+1):return True
            b[r][c]='.';cols.remove(c);diag1.remove(r-c);diag2.remove(r+c)
solve(0)
for row in b:print(''.join(row))
