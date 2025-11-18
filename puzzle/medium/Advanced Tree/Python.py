def print_tree(m, flags,  level, stats, pref):
    if flags['limit'] > 0 and level >= flags['limit']:
        return []
    ls = []
    k = sorted(list(m.keys()), key=lambda x: (x[1:] if x[0]=='.' else x).lower())
    hidden = flags['hidden']
    dirs = flags['dirs']
    for i in range(len(k)-1, -1, -1):
        x = k[i]
        if (x[0] == '.' and not hidden) or (dirs and not m[x]):
            del k[i]
    for i in k:
        if m[i]:stats['dir'] += 1
        else: stats['file'] += 1
        p = '|   '
        if i == k[-1]:
            last = '`' 
            p = '    '
        else:
            last = '|'
        ls.append(pref + last + '-- ' + i)
        ls.extend(print_tree(m[i], flags, level+1, stats, pref+p))
    return ls

s = input()

f = input().split(',')
flags = {'limit':-1}
flags['hidden'] = '-a' in f
flags['dirs'] = '-d' in f
for i in f:
    if i.startswith('-L '):
        flags['limit'] = int(i[3:])

m = {}
for i in range(int(input())):
    line = input()
    c = m
    for x in line.split('/'):
      c.setdefault(x, {})
      c = c[x]

error = False
for i in s.split('/'):
    if not i in m and '.' in m:
        m = m['.']
    if not i in m:
        error = True
        break
    else:
        m = m[i]

stats = {'dir':0, 'file':0}
if error or not m:
    print(s, '[error opening dir]')
else:    
    ls = [s]
    ls.extend(print_tree(m, flags, 0, stats, ''))
    print('\n'.join(ls))

di = stats['dir']
fl = stats['file']
st = '\n' + str(di) + ' director' + ('y' if di==1 else 'ies') 
if not flags['dirs']:
    st += ', ' + str(fl) + ' file' + ('' if fl==1 else 's')
print(st)
