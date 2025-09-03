import sys
import math
import heapq

class Heap(object):

    def __init__(self):
        self._heap = []

    def push(self, priority, item):
        assert priority >= 0
        heapq.heappush(self._heap, (priority, item))

    def pop(self):

        item = heapq.heappop(self._heap)[1] 
        return item

    def __len__(self):
        return len(self._heap)

    def __iter__(self):
        return self

    def next(self):
        try:
            return self.pop()
        except IndexError:
            raise StopIteration

def distr(s1, s2):
    x = (stops[s2][2]-stops[s1][2])*math.cos( math.radians((stops[s1][1]+stops[s2][1])/2) )
    y = (stops[s2][1]-stops[s1][1])
    return math.sqrt(x*x+y*y)*6371

stops = {}
graph = {}
dist = {}
v = {}


s = input()
s=s[9:]
e = input()
e=e[9:]
n = int(input())

for i in range(n):
    stop = input().split(",")
    stop[0] = stop[0][9:]
    stops[stop[0]] = [stop[1].strip("\""), float(stop[3]), float(stop[4])]
    dist[stop[0]] = 1000000000000
    v[stop[0]] = 0

m = int(input())
for i in range(m):
    s1,s2 = input().split();
    s1=s1[9:]
    s2=s2[9:]
    if s1 not in graph:
        graph[s1] = []
    graph[s1].append( [s2, distr(s1,s2)])

parent = {}
minheap = Heap()
parent[s] = 'NULL'
dist[s] = 0
minheap.push(0, s)
u = s

pos = 1

while u != e :
    v[u] = 1
    dest = graph[u]
    for i in dest:
        if v[i[0]] == 0 and dist[u]+i[1] < dist[i[0]]:
            parent[i[0]] = u
            dist[i[0]] = dist[u]+i[1]
            minheap.push(dist[i[0]], i[0])
    if len(minheap)==0:
        pos=0
        break
    else:
        u = minheap.pop()

if pos==1:
    revstops = []
    while u!='NULL':
        revstops.append(stops[u][0])
        u = parent[u]

    revstops = revstops[::-1]

    for i in revstops:
        print(i)
else:
    print("IMPOSSIBLE")