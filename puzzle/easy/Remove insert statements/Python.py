import sys
import re

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0])
    lines = input_data[1:n+1]
    
    in_function = 0
    full_script = []
    
    for line in lines:
        stripped = line.strip().upper()
        
        if stripped.startswith("BEGIN"):
            in_function += 1
            full_script.append((line, True))
            continue
        
        if stripped.startswith("END") and not any(stripped.startswith(k) for k in ["END IF", "END LOOP"]):
            full_script.append((line, True))
            in_function = max(0, in_function - 1)
            continue
            
        full_script.append((line, in_function > 0))

    output = []
    current_insert_buffer = []
    in_insert_to_delete = False

    for line_text, is_inside_func in full_script:
        if is_inside_func:
            output.append(line_text)
            continue

        parts = line_text.split('--', 1)
        code = parts[0]
        comment = "--" + parts[1] if len(parts) > 1 else ""
        
        segments = re.split(r'(;)', code)
        
        line_to_print = ""
        for i in range(0, len(segments), 2):
            stmt_part = segments[i]
            sep = segments[i+1] if i+1 < len(segments) else ""
            
            combined = stmt_part + sep
            
            if not in_insert_to_delete:
                if re.match(r'^\s*INSERT\b', stmt_part, re.IGNORECASE):
                    in_insert_to_delete = True
                    if sep == ";":
                        in_insert_to_delete = False
                else:
                    line_to_print += combined
            else:
                if sep == ";":
                    in_insert_to_delete = False
        
        final = line_to_print + comment
        if final.strip() or comment:
            output.append(final)
        elif line_text.strip() == "":
            output.append("")

    for l in output:
        print(l)

solve()