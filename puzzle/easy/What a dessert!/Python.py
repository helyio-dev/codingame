import sys

input_data = sys.stdin.read().split()
if input_data:
    e, f, s, b = map(int, input_data)

    recipes = [
        ("Cake", 3, 180, 100, 100),
        ("Cookie", 1, 100, 150, 50),
        ("Muffin", 2, 150, 100, 150)
    ]

    best_count = -1
    best_name = ""

    for name, re, rf, rs, rb in recipes:
        count = min(e // re, f // rf, s // rs, b // rb)
        
        if count > best_count:
            best_count = count
            best_name = name
        elif count == best_count:
            pass

    print(f"{best_count} {best_name}")