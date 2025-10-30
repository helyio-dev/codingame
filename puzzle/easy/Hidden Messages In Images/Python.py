w, h = map(int, input().split())
pixels = []
for _ in range(h):
    pixels.extend(map(int, input().split()))

bits = [str(p % 2) for p in pixels]
message = ''

for i in range(0, len(bits), 8):
    byte = bits[i:i+8]
    message += chr(int(''.join(byte), 2))

print(message)
