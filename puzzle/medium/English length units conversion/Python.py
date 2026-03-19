conversions = {}
start, end = input().split(" in ")
n = int(input())
sn = n
s = start
for i in range(n):
    a, b = input().split(" = ")
    a,*unit1 = a.split(" ")
    b,*unit2 = b.split(" ")
    unit1 = " ".join(unit1)
    unit2 = " ".join(unit2)

    if unit1 not in conversions:
        conversions[unit1] = []
    conversions[unit1] += [[int(a),int(b),unit2]]

    if unit2 not in conversions:
        conversions[unit2] = []
    conversions[unit2] += [[int(b),int(a),unit1]]

route = [[]]
goal = [end]
def search(unit, path):
    if unit == goal[0]:
        route[0] = path
        return
    for (_,_,child) in conversions[unit]:
        if child not in path:
            search(child, path+[child])
search(start, [])

for u in route[0]:
    for (a,b,unit) in conversions[start]:
        if unit == u:            
            sn *= a
            n = n*b   
            start = u
            break

for i in range(min(n,sn),1,-1):
    if n % i == 0 and sn % i == 0:
        n //= i
        sn //= i
        break

print(sn, s, "=", n, end)