L,S,N=map(int,input().split())
code=''.join(input() for _ in range(L))
inp=[int(input()) for _ in range(N)]
tape=[0]*S
ptr=0
ip=0
out=[]
code=list(filter(lambda c:c in '><+-.,[]',code))
stack=[]
jmp={}
for i,c in enumerate(code):
    if c=='[':stack.append(i)
    if c==']':
        if not stack:print('SYNTAX ERROR');exit()
        j=stack.pop()
        jmp[i]=j;jmp[j]=i
if stack:print('SYNTAX ERROR');exit()
inp_idx=0
while ip<len(code):
    c=code[ip]
    if c=='>':
        ptr+=1
        if ptr>=S:print('POINTER OUT OF BOUNDS');exit()
    elif c=='<':
        ptr-=1
        if ptr<0:print('POINTER OUT OF BOUNDS');exit()
    elif c=='+':
        tape[ptr]+=1
        if tape[ptr]>255:print('INCORRECT VALUE');exit()
    elif c=='-':
        tape[ptr]-=1
        if tape[ptr]<0:print('INCORRECT VALUE');exit()
    elif c=='.':
        out.append(chr(tape[ptr]))
    elif c==',':
        if inp_idx>=len(inp):tape[ptr]=0
        else:
            tape[ptr]=inp[inp_idx];inp_idx+=1
            if tape[ptr]<0 or tape[ptr]>255:print('INCORRECT VALUE');exit()
    elif c=='[':
        if tape[ptr]==0:ip=jmp[ip]
    elif c==']':
        if tape[ptr]!=0:ip=jmp[ip]
    ip+=1
print(''.join(out))
