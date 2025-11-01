from itertools import combinations

l, w = map(int, input().split())
grid = [list(input()) for _ in range(w)]
dir_map = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
reflect = {
    '/': {'N':'E', 'E':'N', 'S':'W', 'W':'S'},
    '\\': {'N':'W', 'W':'N', 'S':'E', 'E':'S'}
}

mirrors = [(r,c) for r in range(w) for c in range(l) if grid[r][c] in '/\\']
for r in range(w):
    for c in range(l):
        if grid[r][c]=='L':
            lr, lc = r, c
        elif grid[r][c]=='T':
            tr, tc = r, c
dir0 = input()

def simulate(flip_set):
    r, c = lr, lc
    d = dir0
    visited = set()
    while 0<=r<w and 0<=c<l:
        if (r,c,d) in visited:
            return False
        visited.add((r,c,d))
        if (r,c)==(tr,tc):
            return True
        ch = grid[r][c]
        if (r,c) in flip_set:
            ch = '/' if ch=='\\' else '\\'
        if ch in '/\\':
            d = reflect[ch][d]
        elif ch=='#':
            return False
        r += dir_map[d][0]
        c += dir_map[d][1]
    return False

for k in range(len(mirrors)+1):
    for combo in combinations(mirrors, k):
        if simulate(set(combo)):
            for r,c in sorted(combo, key=lambda x:(x[0], x[1])):
                print(c, r)
            exit()
