n,k=map(int,input().split())
def shape(seq):
    if not seq:return ''
    root=seq[0]
    left=[x for x in seq[1:] if x<root]
    right=[x for x in seq[1:] if x>root]
    return '('+shape(left)+')('+shape(right)+')'
shapes=set()
for _ in range(n):
    lst=list(map(int,input().split()))
    shapes.add(shape(lst))
print(len(shapes))
