import sys

def is_triple(n):
    b = bin(n)[2:]
    return "111" in b or "000" in b

def solve():
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line.strip())
    
    curr = n + 1
    while True:
        b = bin(curr)[2:]
        
        pos0 = b.find("000")
        pos1 = b.find("111")
        
        if pos0 == -1 and pos1 == -1:
            print(curr)
            break
            
        pos = min(p for p in [pos0, pos1] if p != -1)
        
        prefix = b[:pos+3]
        incremented = bin(int(prefix, 2) + 1)[2:]
        
        if len(incremented) > len(prefix):
            new_b = incremented + "0" * (len(b) - len(prefix))
        else:
            new_b = incremented + "0" * (len(b) - len(prefix))
            
        curr = int(new_b, 2)

solve()