h=int(input())
w=int(input())
n=int(input())
seat_map={}
for _ in range(n):
    name,seat=input().split(',')
    row=int(seat[:-1])-1
    col=ord(seat[-1])-65
    seat_map[(row,col)]=name
boarded=set()
left= [(r,c) for r in range(h) for c in range(w//2)]
right=[(r,c) for r in range(h) for c in range(w//2,w)]
group=0
while len(boarded)<n:
    grp=[]
    if group%2==0:
        for r in reversed(range(h)):
            for c in range(w//2):
                if (r,c) in seat_map and seat_map[(r,c)] not in boarded:
                    grp.append(seat_map[(r,c)])
                    boarded.add(seat_map[(r,c)])
                    break
    else:
        for r in reversed(range(h)):
            for c in reversed(range(w//2,w)):
                if (r,c) in seat_map and seat_map[(r,c)] not in boarded:
                    grp.append(seat_map[(r,c)])
                    boarded.add(seat_map[(r,c)])
                    break
    if grp:print("Now boarding: "+','.join(grp))
    group+=1
