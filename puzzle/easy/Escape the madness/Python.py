import sys
import re

s = sys.stdin.readline()
if not s:
    sys.exit()
t = s.rstrip('\r\n')

tri = {
    '??=': '#', '??/': '\\', "??'": '^', '??(': '[',
    '??)': ']', '??!': '|', '??-': '~'
}
for k, v in tri.items():
    t = t.replace(k, v)

i = 0
r2 = []
h = "0123456789abcdefABCDEF"
while i < len(t):
    if t[i] == '\\' and i + 1 < len(t):
        if t[i+1] == 'U' and i + 9 < len(t) and all(c in h for c in t[i+2:i+10]):
            r2.append(chr(int(t[i+2:i+10], 16)))
            i += 10
        elif t[i+1] == 'u' and i + 5 < len(t) and all(c in h for c in t[i+2:i+6]):
            r2.append(chr(int(t[i+2:i+6], 16)))
            i += 6
        elif t[i+1] == 'x' and i + 3 < len(t) and all(c in h for c in t[i+2:i+4]):
            r2.append(chr(int(t[i+2:i+4], 16)))
            i += 4
        else:
            r2.append(t[i+1])
            i += 2
    else:
        r2.append(t[i])
        i += 1
t = "".join(r2)

def sub_h(m):
    c = m.group(1)
    if c.startswith('#'):
        return chr(int(c[1:]))
    d = {'amp': '&', 'lt': '<', 'gt': '>', 'bsol': '\\'}
    return d.get(c, m.group(0))

t = re.sub(r'&(#?[a-zA-Z0-9]+);', sub_h, t)
print(t)