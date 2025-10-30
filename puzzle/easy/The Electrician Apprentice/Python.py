def eval_series(switches, states):
    return all(states.get(s, False) for s in switches)

def eval_parallel(switches, states):
    return any(states.get(s, False) for s in switches)

C = int(input())
circuits = []
for _ in range(C):
    line = input().split()
    equipment = line[0]
    wiring = []
    i = 1
    while i < len(line):
        if line[i] in ('-', '='):
            kind = line[i]
            i += 1
            switches = []
            while i < len(line) and line[i] not in ('-', '='):
                switches.append(line[i])
                i += 1
            wiring.append((kind, switches))
        else:
            i += 1
    circuits.append((equipment, wiring))

A = int(input())
switch_states = {}
for _ in range(A):
    sw = input()
    switch_states[sw] = not switch_states.get(sw, False)

results = []
for equipment, wiring in circuits:
    on = True
    for kind, switches in wiring:
        if kind == '-':
            on = on and eval_series(switches, switch_states)
        elif kind == '=':
            on = on and eval_parallel(switches, switch_states)
    results.append(f"{equipment} is {'ON' if on else 'OFF'}")

print("\n".join(results))
