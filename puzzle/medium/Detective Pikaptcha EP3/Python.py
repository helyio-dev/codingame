width, height = [int(i) for i in input().split()]
grid = []
start_square = [-1,-1]
chars = {"<":0,"^":1,">":2,"v":3,"#":0}
direction = 0
for i in range(height):
    grid.append([])
    for j,char in enumerate(input()):
        grid[-1].append(0 if char not in chars else char)
        if char in chars and char != "#":
            start_square = [i,j]
            direction = chars[char]
            grid[i][j] = 0

side = 1 if input() == "L" else -1

directions = {0:[0,-1],1:[-1,0],2:[0,1],3:[1,0]}

previous_square = [-1,-1]
i = start_square[0]
j = start_square[1]
chars = {0:"<",1:"^",2:">",3:"v"}
while previous_square != start_square:

    start_direction = direction
    loop = 0
    while loop<4:
        y , x = directions[direction]
        iy = i+y
        jx = j+x
        
        wrap = False
        if iy < 0:
            iy = height-1
            wrap = True
        elif iy>=len(grid):
            iy = 0
            wrap=True
        
        if wrap:
            if width % 2 == 1:
                middle = width/2
                jx = abs(middle-jx)
                if jx < middle:
                    jx = width - jx
            else:
                middles = [width//2-1,width//2]
                if jx <= middles[0]:
                    jx = width - abs(middles[1]-jx)
                else:
                    jx = middles[0] - (width-1-jx)
        jx = jx%width
        if grid[iy][jx] == "#":
            direction = (direction+side)%4
        else:
            break  
        loop+=1
    if loop==4:break

    i = iy
    j = (jx)%width
    grid[i][j] += 1 
    previous_square = [i,j]
    direction = (direction+(side*-1))%4

for row in grid:
    print("".join([str(i) for i in row]))