#include <stdio.h>
#include <string.h>

typedef struct {
    char name[10];
    int life;
    int punch;
    int kick;
    char special[30];
} Champ;

int main(){
    Champ champs[]={
        {"KEN",25,6,5,"3*rage"},
        {"RYU",25,4,5,"4*rage"},
        {"TANK",50,2,2,"2*rage"},
        {"VLAD",30,3,3,"2*(rage+opp_rage)"},
        {"JADE",20,2,7,"hits*rage"},
        {"ANNA",18,9,1,"dmg_taken*rage"},
        {"JUN",60,2,1,"rage"}
    };
    char c1[10],c2[10];
    int n;
    scanf("%s %s",c1,c2);
    scanf("%d",&n);
    Champ *a=NULL,*b=NULL;
    for(int i=0;i<7;i++){
        if(!strcmp(champs[i].name,c1))a=&champs[i];
        if(!strcmp(champs[i].name,c2))b=&champs[i];
    }
    int life1=a->life,life2=b->life,rage1=0,rage2=0,h1=0,h2=0,dmg1=0,dmg2=0;
    for(int i=0;i<n;i++){
        char dir[3],atk[10];
        scanf("%s %s",dir,atk);
        int *r1,*r2,*h,*d1,*d2,*L1,*L2;
        Champ *A,*B;
        if(dir[0]=='>'){A=a;B=b;L1=&life1;L2=&life2;r1=&rage1;r2=&rage2;h=&h1;d1=&dmg1;d2=&dmg2;}
        else{A=b;B=a;L1=&life2;L2=&life1;r1=&rage2;r2=&rage1;h=&h2;d1=&dmg2;d2=&dmg1;}
        int d=0;
        if(!strcmp(atk,"PUNCH"))d=A->punch;
        else if(!strcmp(atk,"KICK"))d=A->kick;
        else{
            if(!strcmp(A->name,"VLAD")){d=2*((*r1)+(*r2));*r2=0;}
            else if(!strcmp(A->name,"JADE"))d=(*h)*(*r1);
            else if(!strcmp(A->name,"ANNA"))d=(*d1)*(*r1);
            else if(!strcmp(A->name,"JUN")){d=*r1;*L1+=*r1;}
            else if(!strcmp(A->name,"KEN"))d=3*(*r1);
            else if(!strcmp(A->name,"RYU"))d=4*(*r1);
            else if(!strcmp(A->name,"TANK"))d=2*(*r1);
            *r1=0;
        }
        *L2-=d;
        *d2+=d;
        (*r2)++;
        (*h)++;
        if(life1<=0||life2<=0)break;
    }
    if(life1>life2)printf("%s beats %s in %d hits\n",a->name,b->name,h1);
    else printf("%s beats %s in %d hits\n",b->name,a->name,h2);
    return 0;
}
