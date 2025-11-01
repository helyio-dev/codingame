x,y=map(int,input().split())
u,v=map(int,input().split())
dx=min((u-x)%200,(x-u)%200)
dy=min((v-y)%150,(y-v)%150)
d=min(dx,dy)
t=d*0.5+(dx-d)*0.3+(dy-d)*0.4
print(round(t,1))
