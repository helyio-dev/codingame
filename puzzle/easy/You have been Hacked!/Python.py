n = int(input())
companies = []
protection = {}

for _ in range(n):
    name, p = input().split(":")
    companies.append(name)
    protection[name] = int(p)

a = int(input())
attacks = {}

for _ in range(a):
    name, attack_type, strength = input().split(":")
    if name not in attacks:
        attacks[name] = {}
    attacks[name].setdefault(attack_type, 0)
    attacks[name][attack_type] += int(strength)

for name in companies:
    p = protection[name]
    limits = {
        "ps": 10000 if p >= 7 else 0,
        "bf": float("inf") if p >= 7 else 5000 if p >= 5 else 500,
        "mi": float("inf") if p >= 7 else 3000 if p >= 5 else 1000
    }

    status = "Hacked"

    for attack_type in ("ps", "bf", "mi"):
        total = attacks[name][attack_type]
        if total < limits[attack_type]:
            status = "Blocked"
            break

    print(f"{name}:{status}")
