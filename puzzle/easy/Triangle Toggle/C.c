#include <stdio.h>

int sign(int x1,int y1,int x2,int y2,int x3,int y3){
    return (x1-x3)*(y2-y3)-(x2-x3)*(y1-y3);
}

int pointInTriangle(int px,int py,int *t){
    int d1=sign(px,py,t[0],t[1],t[2],t[3]);
    int d2=sign(px,py,t[2],t[3],t[4],t[5]);
    int d3=sign(px,py,t[4],t[5],t[0],t[1]);
    int has_neg=(d1<0)||(d2<0)||(d3<0);
    int has_pos=(d1>0)||(d2>0)||(d3>0);
    return !(has_neg && has_pos);
}

int main(){
    int HI,WI,howManyTriangles;
    scanf("%d %d",&HI,&WI);
    char style[10];
    scanf("%s",style);
    scanf("%d",&howManyTriangles);
    int triangles[10][6];
    for(int i=0;i<howManyTriangles;i++)
        for(int j=0;j<6;j++)
            scanf("%d",&triangles[i][j]);
    char grid[50][50];
    for(int y=0;y<HI;y++)
        for(int x=0;x<WI;x++)
            grid[y][x]='*';
    for(int i=0;i<howManyTriangles;i++){
        int *t=triangles[i];
        int minX=t[0]<t[2]? (t[0]<t[4]?t[0]:t[4]) : (t[2]<t[4]?t[2]:t[4]);
        int maxX=t[0]>t[2]? (t[0]>t[4]?t[0]:t[4]) : (t[2]>t[4]?t[2]:t[4]);
        int minY=t[1]<t[3]? (t[1]<t[5]?t[1]:t[5]) : (t[3]<t[5]?t[3]:t[5]);
        int maxY=t[1]>t[3]? (t[1]>t[5]?t[1]:t[5]) : (t[3]>t[5]?t[3]:t[5]);
        if(minX<0) minX=0;
        if(minY<0) minY=0;
        if(maxX>=WI) maxX=WI-1;
        if(maxY>=HI) maxY=HI-1;
        for(int y=minY;y<=maxY;y++)
            for(int x=minX;x<=maxX;x++)
                if(pointInTriangle(x,y,t))
                    grid[y][x]=(grid[y][x]=='*')?' ':'*';
    }
    for(int y=0;y<HI;y++){
        for(int x=0;x<WI;x++){
            printf("%c",grid[y][x]);
            if(style[0]=='e' && x!=WI-1) printf(" ");
        }
        printf("\n");
    }
    return 0;
}
