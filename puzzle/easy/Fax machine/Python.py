w=int(input())
h=int(input())
a=list(map(int,input().split()))
p=[]
c='*'
for n in a:
    p+=[c]*n
    c=' ' if c=='*' else '*'
for i in range(h):
    row=''.join(p[i*w:(i+1)*w])
    print(f'|{row}|')
