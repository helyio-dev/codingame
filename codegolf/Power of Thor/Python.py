a,b,x,y=map(int,input().split())
while 1:
 p=('S'*(y<b)+'N'*(y>b)+('E'*(x<a)+'W'*(x>a)))
 y+=y<b;y-=y>b;x+=x<a;x-=x>a
 print(p)
