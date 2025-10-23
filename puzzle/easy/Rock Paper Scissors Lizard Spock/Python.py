def beats(a,b):
    win={'C':['P','L'],'P':['R','S'],'R':['C','L'],'L':['S','P'],'S':['C','R']}
    return a!=b and b in win[a]

n=int(input())
players=[tuple(input().split()) for _ in range(n)]
players=[(int(num),sign) for num,sign in players]
opponents={p[0]:[] for p in players}

while len(players)>1:
    next_round=[]
    for i in range(0,len(players),2):
        p1,p2=players[i],players[i+1]
        num1,num2=p1[0],p2[0]
        s1,s2=p1[1],p2[1]
        if beats(s1,s2):
            winner,num_w,opp= p1,num1,num2
        elif beats(s2,s1):
            winner,num_w,opp= p2,num2,num1
        else:
            winner,num_w,opp= (p1 if num1<num2 else p2),(num1 if num1<num2 else num2),(num2 if num1<num2 else num1)
        opponents[num_w].append(opp)
        next_round.append(winner)
    players=next_round

winner=players[0][0]
print(winner)
print(' '.join(map(str,opponents[winner])))
