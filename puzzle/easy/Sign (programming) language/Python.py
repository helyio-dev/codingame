import sys
import re

p = sys.stdin.readline().strip()

reg = 0
counting = False
inst_count = 0

i = 0
while i < len(p):
    match = None
    
    if p[i] == '$':
        if not counting:
            counting = True
            inst_count = 0
        else:
            reg += inst_count
            counting = False
        i += 1
        continue

    if p[i:i+3] == '/*$':
        if counting: inst_count += 1
        i += 3
        continue

    m_add = re.match(r'/\$([^/]*)/', p[i:])
    if m_add:
        n = len(m_add.group(1))
        reg += n
        if counting: inst_count += 1
        i += m_add.end()
        continue

    m_sub = re.match(r'//([^/]*)/', p[i:])
    if m_sub:
        n = len(m_sub.group(1))
        reg -= n
        if counting: inst_count += 1
        i += m_sub.end()
        continue

    m_mul_neg = re.match(r'/\*/([^/]*)/', p[i:])
    if m_mul_neg:
        n = len(m_mul_neg.group(1))
        reg *= (-n)
        if counting: inst_count += 1
        i += m_mul_neg.end()
        continue

    m_mul_pos = re.match(r'/\*\*([^/]*)/', p[i:])
    if m_mul_pos:
        n = len(m_mul_pos.group(1))
        reg *= (n + 1)
        if counting: inst_count += 1
        i += m_mul_pos.end()
        continue

    i += 1

print(reg)