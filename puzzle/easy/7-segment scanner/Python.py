segments = {
    " _ | ||_|": "0",
    "     |  |": "1",
    " _  _||_ ": "2",
    " _  _| _|": "3",
    "   |_|  |": "4",
    " _ |_  _|": "5",
    " _ |_ |_|": "6",
    " _   |  |": "7",
    " _ |_||_|": "8",
    " _ |_| _|": "9"
}

lines = [input() for _ in range(3)]
n = len(lines[0]) // 3
res = ""
for i in range(n):
    seg = lines[0][3*i:3*i+3] + lines[1][3*i:3*i+3] + lines[2][3*i:3*i+3]
    res += segments.get(seg, "?")
print(res)
