import math

inputs = input().split()
n = int(inputs[0])
k = int(inputs[1]) 
out = {}
primes = [int(i) for i in input().split()]

out = 0
for p in primes:
    out+=n//p


def comb(arr , i):
    if i<len(primes):
        if arr != []:
            combs.append(arr+[primes[i]])
        comb(arr+[primes[i]] , i+1)
        comb(arr , i+1)

combs = []
comb([],i:=0)

clashes = 0
for combination in combs:
    if len(combination)%2==0:
        clashes += n // math.prod(combination)
    else:
        clashes -= (n // math.prod(combination))

print(out-clashes)