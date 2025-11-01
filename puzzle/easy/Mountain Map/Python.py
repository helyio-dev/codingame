n = int(input())
heights = list(map(int, input().split()))
total_width = sum(heights) * 2
total_height = max(heights)

canvas = [[' ']*total_width for _ in range(total_height)]
pos = 0

for h in heights:
    row, col = total_height-1, pos
    for i in range(h):
        canvas[row-i][col+i] = '/'
    for i in range(h):
        canvas[row-h+1+i][col+h+i] = '\\'
    pos += 2*h

for line in canvas:
    print(''.join(line).rstrip())
