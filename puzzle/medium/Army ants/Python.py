n1,n2=map(int,input().split())
s1=input()[::-1]
s2=input()
t=int(input())
a=list(s1+s2)
for _ in range(t):
 i=0
 while i<len(a)-1:
  if a[i] in s1 and a[i+1] in s2:
   a[i],a[i+1]=a[i+1],a[i]
   i+=1
  i+=1
print("".join(a))