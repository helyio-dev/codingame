W,H=map(int,input().split())
x,y=map(int,input().split())
grid=[list(input()) for _ in range(H)]

dir_map={'^':(0,-1),'>':(1,0),'v':(0,1),'<':(-1,0)}
rotate={'^':'>','>':'v','v':'<','<':'^'}

def rotate_arrow(cx,cy,first):
    rotations=0
    while 0<=cx<W and 0<=cy<H:
        rotations+=1
        grid[cy][cx]=rotate[grid[cy][cx]]
        dx,dy=dir_map[grid[cy][cx]]
        cx,cy=cx+dx,cy+dy
        if (cx,cy)==first or not (0<=cx<W and 0<=cy<H):
            break
    return rotations

print(rotate_arrow(x,y,(x,y)))
