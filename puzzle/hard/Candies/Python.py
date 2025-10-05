n, k = [int(i) for i in input().split()]

ways = []
def search(remaining, path):

    if remaining == 0:
        ways.append(path)

    for j in range(1,k+1):
        if remaining - j >= 0:
            search(remaining-j, path+(str(j),))
search(n,())

ways = sorted(ways)
for way in ways:
    print(" ".join([str(i) for i in way]))