import sys
import re

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    
    it = iter(lines)
    
    try:
        n = int(next(it))
    except (StopIteration, ValueError):
        return

    cyborg_names = [next(it) for _ in range(n)]
    
    m = int(next(it))
    mayhem_info = {}
    for _ in range(m):
        line = next(it)
        match = re.search(r"Mayhem's (\w+) is (?:a |an )?\"?([^\"]+)\"?", line, re.IGNORECASE)
        if match:
            attr, val = match.groups()
            mayhem_info[attr.lower()] = val
            
    c = int(next(it))
    cyborgs = {name: {} for name in cyborg_names}
    for _ in range(c):
        line = next(it)
        for name in cyborg_names:
            if line.startswith(name):
                pattern = f"{re.escape(name)}'s (\\w+) is (?:a |an )?\"?([^\"]+)\"?"
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    attr, val = match.groups()
                    cyborgs[name][attr.lower()] = val
                break

    possible_mayhems = []

    for name in cyborg_names:
        data = cyborgs[name]
        is_match = True
        
        for attr, m_val in mayhem_info.items():
            if attr == "word":
                if "catchphrase" in data:
                    if not re.search(r'\b' + re.escape(m_val) + r'\b', data["catchphrase"]):
                        is_match = False
                else:
                    pass
            else:
                if attr in data:
                    if data[attr] != m_val:
                        is_match = False
            
            if not is_match:
                break
        
        if is_match:
            possible_mayhems.append(name)

    if len(possible_mayhems) == 0:
        print("MISSING")
    elif len(possible_mayhems) > 1:
        print("INDETERMINATE")
    else:
        print(possible_mayhems[0])

if __name__ == "__main__":
    solve()