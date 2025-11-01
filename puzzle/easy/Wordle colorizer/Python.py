a=input()
n=int(input())
for _ in range(n):
    t=list(input())
    r=['X']*5
    used=[0]*5
    for i in range(5):
        if t[i]==a[i]:
            r[i]='#'
            used[i]=1
    for i in range(5):
        if r[i]=='X' and t[i] in a:
            for j in range(5):
                if not used[j] and a[j]==t[i]:
                    r[i]='O'
                    used[j]=1
                    break
    print(''.join(r))
