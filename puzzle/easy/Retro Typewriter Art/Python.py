import re

def g(s):
    if s == "nl":
        return "\n"
    
    replacements = {"sp": " ", "bS": "\\", "sQ": "'"}
    
    for key, value in replacements.items():
        if key in s:
            s = s.replace(key, value)
    
    if s.isdigit(): 
        if len(s) > 1:
            count = int(s[:-1])
            char = s[-1]
        else:
            count = int(s)
            char = s
    else:
        match = re.match(r"(\d+)(.*)", s)
        if match:
            count = int(match.group(1))
            char = match.group(2)
        else:
            return ""

    return char * count

def f():
    recipe = input()
    chunks = recipe.split(" ")
    
    result = ""
    for chunk in chunks:
        if chunk == "nl":
            print(result)
            result = ""
        else:
            result += g(chunk)
            
    if result:
        print(result)

f()