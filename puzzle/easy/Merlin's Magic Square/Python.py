import sys

def solve():
    lines = sys.stdin.readlines()
    
    raw_initial_state = [line.strip() for line in lines[:3]]
    lizzo_moves = lines[3].strip()
    
    I = []
    for row in raw_initial_state:
        I.extend([1 if c == '*' else 0 for c in row.split()])

    F_solved = [1, 1, 1, 1, 0, 1, 1, 1, 1]
    
    EFFECT_MAP = {
        1: [1, 1, 0, 1, 1, 0, 0, 0, 0],
        2: [1, 1, 1, 0, 0, 0, 0, 0, 0],
        3: [0, 1, 1, 0, 1, 1, 0, 0, 0],
        4: [1, 0, 0, 1, 0, 0, 1, 0, 0],
        5: [0, 1, 0, 1, 1, 1, 0, 1, 0],
        6: [0, 0, 1, 0, 0, 1, 0, 0, 1],
        7: [0, 0, 0, 1, 1, 0, 1, 1, 0],
        8: [0, 0, 0, 0, 0, 0, 1, 1, 1],
        9: [0, 0, 0, 0, 1, 1, 0, 1, 1]
    }

    xor_states = lambda state1, state2: [s1 ^ s2 for s1, s2 in zip(state1, state2)]

    L_effect = [0] * 9
    for move in lizzo_moves:
        button = int(move)
        L_effect = xor_states(L_effect, EFFECT_MAP[button])

    S_Lizzo = xor_states(I, L_effect)

    R = xor_states(S_Lizzo, F_solved)

    for button, effect in EFFECT_MAP.items():
        if effect == R:
            print(button)
            break

if __name__ == "__main__":
    solve()