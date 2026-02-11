import sys

def solve():
    mode = sys.stdin.readline().strip()
    
    n1 = int(sys.stdin.readline())
    v1 = [sys.stdin.readline().strip() for _ in range(n1)]
    
    n2 = int(sys.stdin.readline())
    v2 = [sys.stdin.readline().strip() for _ in range(n2)]
    
    diffs = []
    
    if mode == "BY_NUMBER":
        matched_v1 = set()
        matched_v2 = set()
        
        for i in range(min(n1, n2)):
            if v1[i] != v2[i]:
                diffs.append(f"CHANGE: {v1[i]} ---> {v2[i]}")
            matched_v1.add(i)
            matched_v2.add(i)
            
        for i in range(n1):
            if i not in matched_v1:
                diffs.append(f"DELETE: {v1[i]}")
        for i in range(n2):
            if i not in matched_v2:
                diffs.append(f"ADD: {v2[i]}")
                
    else:
        v1_map = {content: i + 1 for i, content in enumerate(v1)}
        v2_map = {content: i + 1 for i, content in enumerate(v2)}
        
        v1_set = set(v1)
        v2_set = set(v2)
        
        common = v1_set.intersection(v2_set)
        for content in common:
            if v1_map[content] != v2_map[content]:
                diffs.append(f"MOVE: {content} @:{v1_map[content]} >>> @:{v2_map[content]}")
        
        for content in v1:
            if content not in v2_set:
                diffs.append(f"DELETE: {content}")
        for content in v2:
            if content not in v1_set:
                diffs.append(f"ADD: {content}")

    if not diffs:
        print("No Diffs")
    else:
        for d in sorted(diffs):
            print(d)

solve()