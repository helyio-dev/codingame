using System;
using System.Collections.Generic;

class Program{
    static int H,W,N;
    static List<int[,]> Ls=new List<int[,]>();

    static void GenerateLs(){
        int[,] baseL={{0,0},{0,1},{1,0},{2,0}};
        for(int flip=1;flip>=-1;flip-=2){
            for(int rot=0;rot<4;rot++){
                int[,] shape=new int[4,2];
                for(int i=0;i<4;i++){
                    int x=baseL[i,0], y=baseL[i,1];
                    for(int r=0;r<rot;r++){
                        int tmp=x;x=y;y=-tmp;
                    }
                    shape[i,0]=x*flip;
                    shape[i,1]=y;
                }
                int minx=int.MaxValue, miny=int.MaxValue;
                for(int i=0;i<4;i++){
                    if(shape[i,0]<minx) minx=shape[i,0];
                    if(shape[i,1]<miny) miny=shape[i,1];
                }
                for(int i=0;i<4;i++){
                    shape[i,0]-=minx;
                    shape[i,1]-=miny;
                }
                bool exists=false;
                foreach(var L in Ls){
                    bool same=true;
                    for(int i=0;i<4;i++){
                        if(L[i,0]!=shape[i,0] || L[i,1]!=shape[i,1]) {same=false; break;}
                    }
                    if(same){exists=true; break;}
                }
                if(!exists) Ls.Add(shape);
            }
        }
    }

    static ulong Bitmask(int[,] L,int x0,int y0){
        ulong mask=0;
        for(int i=0;i<4;i++){
            int xi=x0+L[i,0], yi=y0+L[i,1];
            if(xi<0||xi>=H||yi<0||yi>=W) return 0;
            mask|=1UL<<(xi*W+yi);
        }
        return mask;
    }

    static ulong Comb(int n,int k){
        if(k>n) return 0;
        if(k==0 || k==n) return 1;
        ulong res=1;
        for(int i=1;i<=k;i++) res=res*(ulong)(n-i+1)/(ulong)i;
        return res;
    }

    static void Main(){
        var parts=Console.ReadLine().Split();
        H=int.Parse(parts[0]);
        W=int.Parse(parts[1]);
        N=int.Parse(parts[2]);

        GenerateLs();
        List<ulong> masks=new List<ulong>();
        foreach(var L in Ls)
            for(int x0=0;x0<H;x0++)
                for(int y0=0;y0<W;y0++){
                    ulong m=Bitmask(L,x0,y0);
                    if(m!=0) masks.Add(m);
                }

        ulong configs=0;
        foreach(var r in masks){
            foreach(var b in masks){
                if((r & b)!=0) continue;
                int free=H*W - CountBits(r|b);
                if(free>=N) configs+=Comb(free,N);
            }
        }
        Console.WriteLine(configs);
    }

    static int CountBits(ulong n){
        int c=0;
        while(n>0){n&=n-1;c++;}
        return c;
    }
}
