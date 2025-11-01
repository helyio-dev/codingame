n=int(input())
k=int(input())

count=0
factor=1
while factor<=n:
    higher=n//(factor*10)
    digit=(n//factor)%10
    lower=n%factor
    if k==0:
        if higher!=0:
            count+= (higher-1)*factor + min(max(lower+1,0), factor)
    else:
        if digit>k:
            count+= (higher+1)*factor
        elif digit==k:
            count+= higher*factor + lower+1
        else:
            count+= higher*factor
    factor*=10
print(count)
