I=input;R,C,A=map(int,I().split());E=0
while 1:
 y,x=map(int,I().split());m=[I()for _ in' '*R];E|=m[y][x]=='C';q=[(y,x,[])];s={(y,x)};z=0
 for i,j,p in q:
  c=m[i][j]
  if(E and'T'==c)or(not E and'C'==c):z=p;break
  for d,r,k in zip("UP DOWN LEFT RIGHT".split(),(-1,1,0,0),(0,0,-1,1)):
   n,o=i+r,j+k
   if R>n>=0<=o<C and'#'!=m[n][o]and(n,o)not in s and(not E or'?'!=m[n][o]):s|={(n,o)};q+=[(n,o,p+[d])]
 print((z or[p for i,j,p in q if'?'==m[i][j]][0])[0])