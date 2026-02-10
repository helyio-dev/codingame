import sys

def solve():
    input_data = sys.stdin.readline().strip()
    if not input_data:
        return
    
    parts = input_data.split(',')
    name = parts[0]
    rarity = parts[1]
    attrs = [a.replace(':', ' ') for a in parts[2:]]

    display_name = f"-{name}-"
    
    content_widths = [len(display_name), len(rarity)]
    content_widths.extend([len(a) for a in attrs])
    max_w = max(content_widths)

    def get_centered(text, target_w):
        diff = target_w - len(text)
        left = (diff + 1) // 2
        right = diff // 2
        return " " * left + text + " " * right

    if rarity == "Common":
        print("#" * (max_w + 4))
        print(f"# {get_centered(display_name, max_w)} #")
        print(f"# {get_centered(rarity, max_w)} #")
        for a in attrs:
            print(f"# {a.ljust(max_w)} #")
        print("#" * (max_w + 4))

    elif rarity == "Rare":
        print("/" + "#" * (max_w + 2) + "\\")
        print(f"# {get_centered(display_name, max_w)} #")
        print(f"# {get_centered(rarity, max_w)} #")
        for a in attrs:
            print(f"# {a.ljust(max_w)} #")
        print("\\" + "#" * (max_w + 2) + "/")

    elif rarity == "Epic":
        print("/" + "-" * (max_w + 2) + "\\")
        print(f"| {get_centered(display_name, max_w)} |")
        print(f"| {get_centered(rarity, max_w)} |")
        for a in attrs:
            print(f"| {a.ljust(max_w)} |")
        print("\\" + "_" * (max_w + 2) + "/")

    elif rarity == "Legendary":
        inner_w = max_w + 2
        center_char = "_" if inner_w % 2 != 0 else "__"
        num_dashes = (inner_w - len(center_char) - 2) // 2
        
        top = "X" + "-" * num_dashes + "\\" + center_char + "/" + "-" * num_dashes + "X"
        print(top)
        print(f"[ {get_centered(display_name, max_w)} ]")
        print(f"| {get_centered(rarity, max_w)} |")
        for a in attrs:
            print(f"| {a.ljust(max_w)} |")
        print("X" + "_" * (max_w + 2) + "X")

solve()