#include <stdio.h>
#include <stdint.h>

int H,W,N;
typedef uint64_t u64;

int base[4][2]={{0,0},{0,1},{1,0},{2,0}};
int Ls[8][4][2];
int L_count=0;

void generate_Ls(){
    for(int flip=0;flip<2;flip++){
        int f=flip? -1:1;
        for(int rot=0;rot<4;rot++){
            int shape[4][2];
            for(int i=0;i<4;i++){
                int x=base[i][0], y=base[i][1];
                for(int r=0;r<rot;r++){
                    int tmp=x;x=y;y=-tmp;
                }
                shape[i][0]=x*f;
                shape[i][1]=y;
            }
            int minx=shape[0][0], miny=shape[0][1];
            for(int i=1;i<4;i++){
                if(shape[i][0]<minx) minx=shape[i][0];
                if(shape[i][1]<miny) miny=shape[i][1];
            }
            int ok=1;
            for(int i=0;i<L_count;i++){
                int same=1;
                for(int j=0;j<4;j++){
                    if(shape[j][0]!=Ls[i][j][0] || shape[j][1]!=Ls[i][j][1]){
                        same=0; break;
                    }
                }
                if(same){ok=0; break;}
            }
            if(ok){
                for(int i=0;i<4;i++){
                    Ls[L_count][i][0]=shape[i][0]-minx;
                    Ls[L_count][i][1]=shape[i][1]-miny;
                }
                L_count++;
            }
        }
    }
}

u64 bitmask(int L[4][2], int x0, int y0){
    u64 mask=0;
    for(int i=0;i<4;i++){
        int xi=x0+L[i][0], yi=y0+L[i][1];
        if(xi<0 || xi>=H || yi<0 || yi>=W) return 0;
        mask|=1ULL<<(xi*W+yi);
    }
    return mask;
}

u64 comb(int n,int k){
    if(k>n) return 0;
    if(k==0 || k==n) return 1;
    u64 res=1;
    for(int i=1;i<=k;i++){
        res=res*(n-i+1)/i;
    }
    return res;
}

int main(){
    scanf("%d %d %d",&H,&W,&N);
    generate_Ls();
    u64 fits_masks[512]; // suffisant pour H,W≤8
    int total_masks=0;
    for(int i=0;i<L_count;i++){
        for(int x0=0;x0<H;x0++){
            for(int y0=0;y0<W;y0++){
                u64 m=bitmask(Ls[i],x0,y0);
                if(m){
                    fits_masks[total_masks++]=m;
                }
            }
        }
    }
    u64 configs=0;
    for(int i=0;i<total_masks;i++){
        for(int j=0;j<total_masks;j++){
            if(fits_masks[i]&fits_masks[j]) continue;
            int free=H*W - __builtin_popcountll(fits_masks[i]|fits_masks[j]);
            if(free>=N) configs+=comb(free,N);
        }
    }
    printf("%llu\n",configs);
    return 0;
}
