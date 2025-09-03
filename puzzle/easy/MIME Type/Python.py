import sys

n = int(input())
q = int(input())
mime_types = {}

for i in range(n):
    ext, mt = input().split()
    mime_types[ext.lower()] = mt

for i in range(q):
    fname = input()
    last_dot_index = fname.rfind('.')
    
    if last_dot_index == -1:
        print("UNKNOWN")
    else:
        ext = fname[last_dot_index + 1:].lower()
        print(mime_types.get(ext, "UNKNOWN"))
