n = int(input())

def value(s):
    try:return float(s)
    except:return sum([ord(c) for c in s])

arr = [value(input()) for i in range(n)]
temp = sorted(arr)

pos = {}
for i in range(len(arr)):
    pos[arr[i]] = i

swaps = 0
for i in range(len(arr)):
    if temp[i] != arr[i]:
        ind = pos[temp[i]]
        arr[i], arr[ind] = arr[ind], arr[i]

        pos[arr[i]] = i
        pos[arr[ind]] = ind

        swaps += 1

if len(set(arr)) == len(arr):
    print(swaps)
else:print(-1)