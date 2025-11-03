w,h=map(int,input().split())
s=''.join(input() for _ in range(h))
n=int(input())
def parse(t):
    t=t.replace(' ','').split(',')
    r=set()
    for x in t:
        if '-' in x:
            a,b=x.split('-')
            r.update(chr(c) for c in range(ord(a),ord(b)+1))
        else:r.add(x)
    return r
for _ in range(n):
    want=parse(input())
    need=len(want)
    cnt={}
    have=0
    res=(0,len(s)-1)
    l=0
    for r,ch in enumerate(s):
        if ch in want:
            cnt[ch]=cnt.get(ch,0)+1
            if cnt[ch]==1:have+=1
        while have==need:
            if r-l<res[1]-res[0]:
                res=(l,r)
            lc=s[l]
            if lc in cnt:
                cnt[lc]-=1
                if cnt[lc]==0:have-=1
            l+=1
    print(res[0],res[1])
