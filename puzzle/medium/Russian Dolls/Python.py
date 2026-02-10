import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    try:
        n_line = input_data[0].strip()
        if not n_line:
            return
        n_cases = int(n_line)
    except ValueError:
        return

    for i in range(1, n_cases + 1):
        if i >= len(input_data):
            break
            
        test_case = input_data[i].strip()
        if not test_case:
            print("-1")
            continue

        parts = test_case.split()
        
        try:
            tokens = []
            for p in parts:
                val = int(p)
                if val == 0:
                    raise ValueError
                tokens.append(val)
        except ValueError:
            print("-1")
            continue

        stack = []
        solid_count = 0
        valid = True
        processed_count = 0
        
        for val in tokens:
            processed_count += 1
            if val < 0:
                stack.append([abs(val), 0])
            else:
                if not stack or stack[-1][0] != val:
                    valid = False
                    break
                
                doll_size, children_sum = stack.pop()
                
                if children_sum >= doll_size:
                    valid = False
                    break
                
                if children_sum == 0:
                    solid_count += 1
                
                if stack:
                    stack[-1][1] += doll_size
                else:
                    if processed_count < len(tokens):
                        valid = False
                        break

        if valid and not stack and processed_count == len(tokens):
            print(solid_count)
        else:
            print("-1")

solve()