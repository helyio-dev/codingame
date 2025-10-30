wallyWidth, wallyHeight = map(int, input().split())
wally = [input() for _ in range(wallyHeight)]
pictureWidth, pictureHeight = map(int, input().split())
picture = [input() for _ in range(pictureHeight)]

for y in range(pictureHeight - wallyHeight + 1):
    for x in range(pictureWidth - wallyWidth + 1):
        match = True
        for dy in range(wallyHeight):
            for dx in range(wallyWidth):
                if wally[dy][dx] != ' ' and wally[dy][dx] != picture[y+dy][x+dx]:
                    match = False
                    break
            if not match:
                break
        if match:
            print(x, y)
            exit()
