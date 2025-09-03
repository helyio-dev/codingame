import sys

def solve():
    l, h = map(int, sys.stdin.readline().split())
    mayan_numerals = {}
    
    # Store Mayan numeral representations
    for i in range(20):
        mayan_numerals[i] = []
    
    numeral_lines = [sys.stdin.readline().rstrip() for _ in range(h)]
    
    for i in range(h):
        for j in range(20):
            mayan_numerals[j].append(numeral_lines[i][j * l : (j + 1) * l])
    
    # Function to get the value of a Mayan section
    def get_mayan_value(section_lines):
        for i in range(20):
            if mayan_numerals[i] == section_lines:
                return i
        return -1  # Should not happen with valid input

    def read_mayan_number():
        s = int(sys.stdin.readline())
        sections = []
        for _ in range(s // h):
            section_lines = [sys.stdin.readline().rstrip() for _ in range(h)]
            sections.append(section_lines)
        
        value = 0
        power_of_20 = 1
        for i in range(len(sections) - 1, -1, -1):
            numeral_value = get_mayan_value(sections[i])
            value += numeral_value * power_of_20
            power_of_20 *= 20
        return value

    num1 = read_mayan_number()
    num2 = read_mayan_number()
    operation = sys.stdin.readline().rstrip()

    result = 0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 // num2
    
    # Convert result back to Mayan
    if result == 0:
        sections = [0]
    else:
        sections = []
        while result > 0:
            sections.append(result % 20)
            result //= 20
        sections.reverse()
    
    for section_val in sections:
        for line in mayan_numerals[section_val]:
            print(line)

solve()