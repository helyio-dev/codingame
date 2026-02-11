import sys

def solve():
    turns = int(sys.stdin.readline())
    
    def parse_ai():
        line = sys.stdin.readline().split()
        n, name = int(line[0]), line[1]
        strat = [sys.stdin.readline().split() for _ in range(n)]
        return {"name": name, "strat": strat, "history": [], "score": 0}

    ai1 = parse_ai()
    ai2 = parse_ai()
    
    lcg_state = 12

    def get_rand():
        nonlocal lcg_state
        lcg_state = (137 * lcg_state + 187) % 256
        return "C" if bin(lcg_state).count('1') % 2 == 1 else "D"

    def evaluate(me, opp, turn_idx):
        for cmd in me["strat"]:
            res = False
            action = cmd[-1]
            
            if cmd[0] == "*":
                res = True
            elif cmd[0] == "START":
                if turn_idx == 0: res = True
            elif cmd[0] == "ME" and cmd[1] == "WIN":
                if me["score"] > opp["score"]: res = True
            elif turn_idx > 0:
                if cmd[1] == "-1":
                    target = me if cmd[0] == "ME" else opp
                    if target["history"][-1] == cmd[2]: res = True
                elif cmd[1] == "MAX":
                    target = me if cmd[0] == "ME" else opp
                    if target["history"].count(cmd[2]) > len(target["history"]) / 2: res = True
                elif cmd[1] == "LAST":
                    target = me if cmd[0] == "ME" else opp
                    n_last = int(cmd[2])
                    relevant = target["history"][-n_last:]
                    if relevant.count(cmd[3]) > len(relevant) / 2: res = True
            
            if res:
                return get_rand() if action == "RAND" else action
        return "C"

    for i in range(turns):
        act1 = evaluate(ai1, ai2, i)
        act2 = evaluate(ai2, ai1, i)
        
        ai1["history"].append(act1)
        ai2["history"].append(act2)
        
        if act1 == "C" and act2 == "C":
            ai1["score"] += 2
            ai2["score"] += 2
        elif act1 == "D" and act2 == "D":
            ai1["score"] += 1
            ai2["score"] += 1
        elif act1 == "D" and act2 == "C":
            ai1["score"] += 3
            ai2["score"] += 0
        else:
            ai1["score"] += 0
            ai2["score"] += 3

    if ai1["score"] > ai2["score"]:
        print(ai1["name"])
    elif ai2["score"] > ai1["score"]:
        print(ai2["name"])
    else:
        print("DRAW")

solve()