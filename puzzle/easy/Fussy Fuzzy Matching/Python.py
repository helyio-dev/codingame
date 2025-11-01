import re

letterCase = input().strip() == "true"
letterFuzz = int(input())
numberFuzz = int(input())
otherFuzz = input().strip() == "true"
template = input().strip()
n = int(input())
candidates = [input().strip() for _ in range(n)]

def tokenize(s):
    return re.findall(r'[A-Za-z]+|\d+|[^A-Za-z0-9]', s)

def letter_match(a, b):
    if not letterCase:
        a, b = a.lower(), b.lower()
    if len(a) != len(b):
        return False
    for ca, cb in zip(a, b):
        if abs(ord(ca) - ord(cb)) > letterFuzz:
            return False
    return True

def number_match(a, b):
    return abs(int(a) - int(b)) <= numberFuzz

def other_match(a, b):
    if otherFuzz:
        return a == b
    return not a.isalnum() and not b.isalnum()

for cand in candidates:
    t_parts = tokenize(template)
    c_parts = tokenize(cand)
    if len(t_parts) != len(c_parts):
        print("false")
        continue
    ok = True
    for ta, ca in zip(t_parts, c_parts):
        if ta.isalpha() and ca.isalpha():
            if not letter_match(ta, ca):
                ok = False
                break
        elif ta.isdigit() and ca.isdigit():
            if not number_match(ta, ca):
                ok = False
                break
        elif not ta.isalnum() and not ca.isalnum():
            if not other_match(ta, ca):
                ok = False
                break
        else:
            ok = False
            break
    print("true" if ok else "false")
