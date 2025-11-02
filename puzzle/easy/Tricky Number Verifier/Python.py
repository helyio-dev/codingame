from datetime import datetime
n=int(input())
for _ in range(n):
    s=input().strip()
    if len(s)!=10 or not s.isdigit() or s[0]=='0':print("INVALID SYNTAX");continue
    LLL,chk,bday=s[:3],int(s[3]),s[4:]
    d,m,y=int(bday[:2]),int(bday[2:4]),int(bday[4:])
    y+=2000
    try:datetime(y,m,d)
    except:print("INVALID DATE");continue
    def calc(l):
        f=[3,7,9,5,8,4,2,1,6]
        v=list(map(int,l[:3]+l[4:]))
        s=sum(a*b for a,b in zip(v,f))
        x=s%11
        if x==10:return calc(str(int(l[:3])+1).zfill(3)+l[3:])
        return x,int(l[:3])+ (1 if x==10 else 0)
    x,_=calc(s)
    if x==chk:print("OK")
    else:
        L=int(LLL)
        while True:
            v=list(map(int,str(L).zfill(3)+bday))
            s2=sum(a*b for a,b in zip(v,[3,7,9,5,8,4,2,1,6]))
            x2=s2%11
            if x2==10:L+=1;continue
            print(f"{str(L).zfill(3)}{x2}{bday}")
            break
