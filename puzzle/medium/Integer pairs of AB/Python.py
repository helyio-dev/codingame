n=int(input())
m=n
f=1
c=0
while m%2==0:
    c+=1
    m//=2
f*=2*c+1
i=3
while i*i<=m:
    c=0
    while m%i==0:
        c+=1
        m//=i
    f*=2*c+1
    i+=2
if m>1:f*=3
print(2*f-1)
