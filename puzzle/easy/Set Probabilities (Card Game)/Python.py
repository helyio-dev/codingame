import sys

def solve():
    line1 = sys.stdin.readline()
    if not line1:
        return
    n = int(line1.strip())
    
    features = [
        ["1", "2", "3"],
        ["OUTLINED", "STRIPED", "SOLID"],
        ["RED", "GREEN", "PURPLE"],
        ["DIAMOND", "OVAL", "SQUIGGLE"]
    ]
    
    table_cards = []
    for _ in range(n):
        parts = sys.stdin.readline().split()
        card = []
        for i in range(4):
            card.append(features[i].index(parts[i]))
        table_cards.append(tuple(card))

    def is_set(c1, c2, c3):
        for i in range(4):
            if (c1[i] + c2[i] + c3[i]) % 3 != 0:
                return False
        return True

    def get_needed(c1, c2):
        needed = []
        for i in range(4):
            val = (3 - (c1[i] + c2[i]) % 3) % 3
            needed.append(val)
        return tuple(needed)

    has_set_already = False
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if is_set(table_cards[i], table_cards[j], table_cards[k]):
                    has_set_already = True
                    break
            if has_set_already: break
        if has_set_already: break

    if has_set_already:
        print("1.0000")
        return

    needed_cards = set()
    for i in range(n):
        for j in range(i + 1, n):
            needed_cards.add(get_needed(table_cards[i], table_cards[j]))

    deck_size = 81 - n
    count_success = 0
    for card in needed_cards:
        if card not in table_cards:
            count_success += 1
            
    prob = count_success / deck_size
    print(f"{prob:.4f}")

solve()