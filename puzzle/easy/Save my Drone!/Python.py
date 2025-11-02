X=int(input())
Y=int(input())
R=int(input())
grid=[input() for _ in range(Y)]
if R: grid=[row[::-1] for row in grid[::-1]]
tiles={'#':'Block','^':'Thruster','@':'Gyroscope','+':'Fuel','$':'Core'}
seq=[tiles[c] for row in grid for c in row if c in tiles]
if not seq: print("Nothing")
else:
 r=[]
 c=1
 for i in range(1,len(seq)+1):
  if i<len(seq) and seq[i]==seq[i-1]: c+=1
  else:
   r.append(f"{c} {seq[i-1]}{'s'*(c>1)}")
   c=1
 print(", ".join(r))
