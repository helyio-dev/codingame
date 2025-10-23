#include <stdio.h>
#include <string.h>

int main(){
    int w,h; long long n;
    scanf("%d %d",&w,&h);
    scanf("%lld",&n);
    char grid[10][21];
    for(int i=0;i<h;i++) scanf("%s",grid[i]);
    int dirs[4][2]={{0,-1},{1,0},{0,1},{-1,0}};
    int x,y,d=0;
    for(y=0;y<h;y++){
        char *p=strchr(grid[y],'O');
        if(p){x=p-grid[y];break;}
    }
    typedef struct{int x,y,d; long long step;} State;
    State seen[800]; int seen_count=0;
    long long steps=0;
    while(steps<n){
        int found=0;
        for(int i=0;i<seen_count;i++)
            if(seen[i].x==x && seen[i].y==y && seen[i].d==d){
                long long cycle=steps-seen[i].step;
                long long rem=(n-steps)%cycle;
                x=seen[i].x; y=seen[i].y; d=seen[i].d;
                n=steps+rem;
                found=1;
                break;
            }
        if(!found){
            seen[seen_count].x=x; seen[seen_count].y=y; seen[seen_count].d=d; seen[seen_count].step=steps;
            seen_count++;
        }
        int nx=x+dirs[d][0],ny=y+dirs[d][1];
        while(grid[ny][nx]=='#') d=(d+1)%4,nx=x+dirs[d][0],ny=y+dirs[d][1];
        x=nx;y=ny;
        steps++;
    }
    printf("%d %d\n",x,y);
    return 0;
}
