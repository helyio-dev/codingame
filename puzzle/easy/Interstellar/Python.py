import re, math
from math import gcd
from functools import reduce

def parse_vector(v):
    v = v.replace(' ','')
    comps = {'i':0,'j':0,'k':0}
    for m in re.finditer(r'([+-]?)(\d*)([ijk])', v):
        sign = -1 if m.group(1)=='-' else 1
        num = int(m.group(2)) if m.group(2) else 1
        comps[m.group(3)] = sign*num
    return comps

def simplify_vector(d):
    vals = [d['i'],d['j'],d['k']]
    non_zero = [abs(x) for x in vals if x!=0]
    if not non_zero:
        return '0'
    g = reduce(gcd, non_zero)
    vals = [x//g for x in vals]
    result = ''
    for idx, c in enumerate(['i','j','k']):
        val = vals[idx]
        if val==0:
            continue
        sign = '+' if val>0 else '-'
        if not result and val>0:
            sign=''
        v = abs(val)
        result += f'{sign}{v if v!=1 else ""}{c}'
    return result

ship = parse_vector(input())
wormhole = parse_vector(input())
dir_vec = {k: wormhole[k]-ship[k] for k in 'ijk'}
print(f"Direction: {simplify_vector(dir_vec)}")
dist = math.sqrt(sum((wormhole[k]-ship[k])**2 for k in 'ijk'))
print(f"Distance: {dist:.2f}")
