c=int(input())
p=int(input())
items=[]
for _ in range(c):
    cat,size,price=input().split()
    items.append([cat,size,int(price)])
for _ in range(p):
    cat,size=input().split()
    match=[x for x in items if x[0]==cat and x[1]==size]
    if not match:
        print("NONE")
    else:
        m=min(match,key=lambda x:x[2])
        print(m[2])
        items.remove(m)
