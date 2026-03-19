people = {}
c = int(input())
for i in range(c):
    people[input()] = i+1

votes = []
v = int(input())
for i in range(v):
    vote = list(map(int,input().split()))
    votes += [vote]

eliminated = []
for i in range(c): 
    round_votes = {people[name]:[0,name] for i,name in enumerate(people.keys(),1) if name not in eliminated}
    for j in range(v): 
        for vote in votes:
            for val in vote:
                if val in round_votes:
                    round_votes[val][0] += 1
                    break
    
    round_votes = sorted(round_votes.values(),key = lambda x: x[0])
    eliminated += [round_votes[0][1]]

eliminated[-1] = "winner:"+eliminated[-1]
for name in eliminated:
    print(name)