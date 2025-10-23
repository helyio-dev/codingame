#include <stdio.h>
#include <string.h>

int beats(char a,char b){
    if(a==b) return 0;
    if(a=='C' && (b=='P'||b=='L')) return 1;
    if(a=='P' && (b=='R'||b=='S')) return 1;
    if(a=='R' && (b=='C'||b=='L')) return 1;
    if(a=='L' && (b=='S'||b=='P')) return 1;
    if(a=='S' && (b=='C'||b=='R')) return 1;
    return 0;
}

int main(){
    int n;
    scanf("%d",&n);
    int num[n],op[n][10],op_count[n];
    char sign[n];
    for(int i=0;i<n;i++){
        scanf("%d %c",&num[i],&sign[i]);
        op_count[i]=0;
    }

    int round=n;
    int idx[n];
    for(int i=0;i<n;i++) idx[i]=i;

    while(round>1){
        int next_idx[round/2],k=0;
        for(int i=0;i<round;i+=2){
            int i1=idx[i],i2=idx[i+1];
            int w,l;
            if(beats(sign[i1],sign[i2])){w=i1;l=i2;}
            else if(beats(sign[i2],sign[i1])){w=i2;l=i1;}
            else w=(num[i1]<num[i2]?i1:i2), l=(w==i1?i2:i1);
            op[w][op_count[w]++]=num[l];
            next_idx[k++]=w;
        }
        for(int i=0;i<k;i++) idx[i]=next_idx[i];
        round/=2;
    }

    int winner=idx[0];
    printf("%d\n",num[winner]);
    for(int i=0;i<op_count[winner];i++){
        if(i) printf(" ");
        printf("%d",op[winner][i]);
    }
    printf("\n");
    return 0;
}
