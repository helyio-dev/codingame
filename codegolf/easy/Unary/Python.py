s=input();b=''.join(f'{ord(c):07b}'for c in s);r='';i=0
while i<len(b):j=i;exec("while j<len(b)and b[j]==b[i]:j+=1");r+=('0 'if b[i]>'0'else'00 ')+ '0'*(j-i)+' ';i=j
print(r[:-1])