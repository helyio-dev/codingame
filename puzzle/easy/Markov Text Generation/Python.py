text=input().split()
d=int(input())
l=int(input())
seed=input().split()
chain={}
for i in range(len(text)-d):
    key=' '.join(text[i:i+d])
    chain.setdefault(key,[]).append(text[i+d])
r=0
out=seed[:]
while len(out)<l:
    key=' '.join(out[-d:])
    if key not in chain:break
    opts=chain[key]
    r+=7
    out.append(opts[r%len(opts)])
print(' '.join(out[:l]))
