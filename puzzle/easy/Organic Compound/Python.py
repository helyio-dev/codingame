import sys
import re

def parse_atoms(formula):
    counts = {'C': 0, 'H': 0, 'O': 0}
    matches = re.findall(r'([CHCO])(\d*)', formula)
    for element, count in matches:
        counts[element] += int(count) if count else 1
    return counts

def solve():
    formula = sys.stdin.readline().strip()
    
    counts = parse_atoms(formula)
    n = counts['C']
    h = counts['H']
    o = counts['O']
    
    prefixes = {
        1: "meth", 2: "eth", 3: "prop", 4: "but", 5: "pent",
        6: "hex", 7: "hept", 8: "oct", 9: "non", 10: "dec"
    }
    
    if n not in prefixes:
        print("OTHERS")
        return

    res = "OTHERS"
    prefix = prefixes[n]

    if o == 0:
        if h == 2 * n + 2:
            res = prefix + "ane"
        elif h == 2 * n and n > 1:
            res = prefix + "ene"
            
    elif o == 1:
        if formula.endswith("OH") and h == 2 * n + 2:
            res = prefix + "anol"
        elif formula.endswith("CHO") and h == 2 * n:
            res = prefix + "anal"
        elif "-CO-" in formula.replace("CO", "-CO-") and h == 2 * n and n >= 3:
            if formula.count("O") == 1 and not (formula.endswith("CO") or formula.startswith("CO")):
                 res = prefix + "anone"
            
    elif o == 2:
        if formula.endswith("COOH") and h == 2 * n:
            res = prefix + "anoic acid"

    print(res)

solve()