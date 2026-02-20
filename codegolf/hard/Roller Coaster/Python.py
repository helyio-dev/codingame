import sys
(L,C,N),*P=[[*map(int,l.split())]for l in sys.stdin]
P=[p[0]for p in P];i=r=0;G=[0]*N;S=[0]*N;T=sum(P)
for j in range(N):
 s,k=0,j
 while s+P[k%N]<=L and s<T:s+=P[k%N];k+=1
 G[j],S[j]=s,k%N
for _ in' '*C:r+=G[i];i=S[i]
print(r)