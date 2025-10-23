c1,c2=input().split()
n=int(input())
stats={'KEN':[25,6,5,'3*rage'],'RYU':[25,4,5,'4*rage'],'TANK':[50,2,2,'2*rage'],
       'VLAD':[30,3,3,'2*(rage+opp_rage)'],'JADE':[20,2,7,'hits*rage'],
       'ANNA':[18,9,1,'dmg_taken*rage'],'JUN':[60,2,1,'rage']}
life={c1:stats[c1][0],c2:stats[c2][0]}
rage={c1:0,c2:0}
hits={c1:0,c2:0}
dmg_taken={c1:0,c2:0}

def deal(a,b,move):
    ra,rb=rage[a],rage[b]
    da,db,sp=stats[a][1],stats[a][2],stats[a][3]
    if move=='PUNCH':d=da
    elif move=='KICK':d=db
    else:
        if a=='VLAD':d=2*(ra+rb);rage[b]=0
        elif a=='JADE':d=hits[a]*ra
        elif a=='ANNA':d=dmg_taken[a]*ra
        elif a=='JUN':d=ra;life[a]+=ra
        else:d=eval(sp,{},{"rage":ra})
        rage[a]=0
    life[b]-=d
    dmg_taken[b]+=d
    rage[b]+=1
    hits[a]+=1

for _ in range(n):
    d,atk=input().split()
    if d=='>':deal(c1,c2,atk)
    else:deal(c2,c1,atk)
    if life[c1]<=0 or life[c2]<=0:break

if life[c1]>life[c2]:
    print(f"{c1} beats {c2} in {hits[c1]} hits")
else:
    print(f"{c2} beats {c1} in {hits[c2]} hits")
