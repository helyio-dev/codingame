username = input().strip()
s = sum(ord(c) for c in username)
l = len(username)
seed = (s * l) ^ 20480
seg1 = seed & 0xFFFF
seg2 = (seed >> 16) & 0xFFFF
seg3 = (ord(username[0]) + ord(username[-1])) * l
seg4 = (seg1 + seg2 + seg3) % 65536
key = '-'.join(f"{x:04X}" for x in [seg1, seg2, seg3 & 0xFFFF, seg4])
print(key)
