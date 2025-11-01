n=int(input())
trie={}
for _ in range(n):
    code,c= input().split()
    node=trie
    for b in code:
        if b not in node:
            node[b]={}
        node=node[b]
    node['val']=chr(int(c))
s=input()
res=[]
i=0
while i<len(s):
    node=trie
    j=i
    while j<len(s) and s[j] in node:
        node=node[s[j]]
        j+=1
        if 'val' in node:
            res.append(node['val'])
            i=j
            break
    else:
        print(f"DECODE FAIL AT INDEX {i}")
        exit()
print(''.join(res))
