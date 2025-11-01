N = int(input())
V = int(input())
M = int(input())

children = {}
has_parent = set()

for _ in range(M):
    P, L, R = map(int, input().split())
    children[P] = (L, R)
    has_parent.add(L)
    has_parent.add(R)

root = next(i for i in range(1, N+1) if i not in has_parent)

if V == root:
    print("Root")
else:
    path = []
    def dfs(node):
        if node == V:
            return True
        if node in children:
            L, R = children[node]
            path.append("Left")
            if dfs(L):
                return True
            path.pop()
            path.append("Right")
            if dfs(R):
                return True
            path.pop()
        return False

    dfs(root)
    print(" ".join(path))
