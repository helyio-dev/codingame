#include <stdio.h>
#include <stdlib.h>

int W,H,sr,sc,N;

int path_length(char **grid){
    int r=sr,c=sc,steps=0;
    int visited[20][20]={0};
    while(1){
        if(r<0 || r>=H || c<0 || c>=W) return -1;
        if(visited[r][c]) return -1;
        visited[r][c]=1;
        char cell=grid[r][c];
        if(cell=='T') return steps+1;
        if(cell=='#' || cell=='.') return -1;
        steps++;
        if(cell=='^') r--;
        else if(cell=='v') r++;
        else if(cell=='<') c--;
        else if(cell=='>') c++;
        else return -1;
    }
}

int main(){
    scanf("%d %d",&W,&H);
    scanf("%d %d",&sr,&sc);
    scanf("%d",&N);
    char ***maps=malloc(N * sizeof(char**));
    for(int i=0;i<N;i++){
        maps[i]=malloc(H*sizeof(char*));
        for(int j=0;j<H;j++){
            maps[i][j]=malloc((W+1)*sizeof(char));
            scanf("%s",maps[i][j]);
        }
    }

    int best_len=1000,best_idx=-1;
    for(int i=0;i<N;i++){
        int l=path_length(maps[i]);
        if(l!=-1 && l<best_len){
            best_len=l;
            best_idx=i;
        }
    }

    if(best_idx==-1) printf("TRAP\n");
    else printf("%d\n",best_idx);

    for(int i=0;i<N;i++){
        for(int j=0;j<H;j++) free(maps[i][j]);
        free(maps[i]);
    }
    free(maps);
    return 0;
}
