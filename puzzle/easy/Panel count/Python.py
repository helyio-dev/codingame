P = int(input())
properties = [input().strip() for _ in range(P)]

N = int(input())
persons = []
for _ in range(N):
    parts = input().strip().split()
    name = parts[0]
    prop_values = parts[1:]
    person_dict = dict(zip(properties, prop_values))
    persons.append(person_dict)

F = int(input())
formulas = [input().strip() for _ in range(F)]

for formula in formulas:
    conditions = [cond.strip() for cond in formula.split("AND")]
    cond_pairs = [cond.split("=") for cond in conditions]
    cond_pairs = [(p.strip(), v.strip()) for p, v in cond_pairs]
    
    count = 0
    for person in persons:
        if all(person.get(p) == v for p, v in cond_pairs):
            count += 1
    print(count)
