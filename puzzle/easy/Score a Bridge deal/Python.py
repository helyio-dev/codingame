nbTests = int(input())

def contract_value(level, suit):
    if suit in ["C", "D"]:
        return 20 * level
    elif suit in ["H", "S"]:
        return 30 * level
    else:
        return 40 + 30 * (level - 1)

def overtrick_value(over, suit, dbl, vul):
    if dbl == 1:
        return over * (20 if suit in ["C","D"] else 30)
    elif dbl == 2:
        return over * (100 if not vul else 200)
    else:
        return over * (200 if not vul else 400)

def undertrick_penalty(under, dbl, vul):
    if dbl == 1:
        return under * (100 if vul else 50) * -1
    elif dbl == 2:
        if not vul:
            if under == 1: return -100
            if under == 2: return -300
            if under == 3: return -500
            return -500 - 300*(under-3)
        else:
            if under == 1: return -200
            return -200 - 300*(under-1)
    else:
        if not vul:
            if under == 1: return -200
            if under == 2: return -600
            if under == 3: return -1000
            return -1000 - 600*(under-3)
        else:
            if under == 1: return -400
            return -400 - 600*(under-1)

for _ in range(nbTests):
    line = input().split()
    if line[1] == "Pass":
        print(0)
        continue
    
    vul = line[0] == "V"
    contract = line[1]
    level = int(contract[0])
    dbl = 1
    if contract.endswith("XX"):
        dbl = 4
        suit = contract[1:-2]
    elif contract.endswith("X"):
        dbl = 2
        suit = contract[1:-1]
    else:
        suit = contract[1:]
    
    tricks_won = int(line[2])
    contracted_tricks = level + 6
    overtricks = tricks_won - contracted_tricks
    
    if overtricks >= 0:
        base = contract_value(level, suit) * dbl
        score = base
        if base >= 100:
            score += 500 if vul else 300
        else:
            score += 50
        if level == 6:
            score += 750 if vul else 500
        elif level == 7:
            score += 1500 if vul else 1000
        if dbl > 1:
            score += 50 if dbl == 2 else 100
        if overtricks > 0:
            score += overtrick_value(overtricks, suit, dbl, vul)
    else:
        score = undertrick_penalty(-overtricks, dbl, vul)
    
    print(score)
