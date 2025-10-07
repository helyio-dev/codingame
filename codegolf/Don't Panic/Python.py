r=input;*_,a,b,_,_,n=map(int,r().split());e={a:b}
for _ in[0]*n:x,y=r().split();e[x]=int(y)
while 1:f,p,d=r().split();p=int(p);t=e.get(f,b);print("BLOCK"if(p>t and d>'Q'or p<t and d<'M')else"WAIT")