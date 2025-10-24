N=int(input())
a=[input() for _ in range(N)]
M=2*N-1
b=[[' ']*M for _ in range(M)]
h={'(':')','{':'}','[':']','<':'>'}
h_rev={v:k for k,v in h.items()}
v={'^':'v','v':'^','A':'V','V':'A','w':'m','m':'w','W':'M','M':'W','u':'n','n':'u'}
slash={'/':'\\','\\':'/'}
for i in range(N):
    for j in range(N):
        c=a[i][j]
        b[i][j]=c
        if c in slash: b[i][M-1-j]=slash[c]
        elif c in h: b[i][M-1-j]=h[c]
        elif c in h_rev: b[i][M-1-j]=h_rev[c]
        else: b[i][M-1-j]=c
        if c in slash: b[M-1-i][j]=slash[c]
        else: b[M-1-i][j]=v[c] if c in v else c
        if b[i][M-1-j] in slash: b[M-1-i][M-1-j]=slash[b[i][M-1-j]]
        else: b[M-1-i][M-1-j]=v[b[i][M-1-j]] if b[i][M-1-j] in v else b[i][M-1-j]
l='+'+'-'*M+'+'+'-'*M+'+'
print(l)
for r in range(M):
    print('|'+"".join(b[r])+'|'+"".join(b[r])+'|')
print(l)
for r in range(M):
    print('|'+"".join(b[r])+'|'+"".join(b[r])+'|')
print(l)
