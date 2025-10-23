using System;
using System.Collections.Generic;

class Program{
    static bool Beats(char a,char b){
        return (a=='C'&&(b=='P'||b=='L'))||
               (a=='P'&&(b=='R'||b=='S'))||
               (a=='R'&&(b=='C'||b=='L'))||
               (a=='L'&&(b=='S'||b=='P'))||
               (a=='S'&&(b=='C'||b=='R'));
    }

    static void Main(){
        int n=int.Parse(Console.ReadLine());
        int[] num=new int[n];
        char[] sign=new char[n];
        List<int>[] op=new List<int>[n];
        for(int i=0;i<n;i++){
            var parts=Console.ReadLine().Split();
            num[i]=int.Parse(parts[0]);
            sign[i]=parts[1][0];
            op[i]=new List<int>();
        }

        int[] idx=new int[n];
        for(int i=0;i<n;i++) idx[i]=i;
        int round=n;
        while(round>1){
            int k=0;
            int[] next_idx=new int[round/2];
            for(int i=0;i<round;i+=2){
                int i1=idx[i],i2=idx[i+1];
                int w,l;
                if(Beats(sign[i1],sign[i2])){w=i1;l=i2;}
                else if(Beats(sign[i2],sign[i1])){w=i2;l=i1;}
                else{w=(num[i1]<num[i2]?i1:i2); l=(w==i1?i2:i1);}
                op[w].Add(num[l]);
                next_idx[k++]=w;
            }
            for(int i=0;i<k;i++) idx[i]=next_idx[i];
            round/=2;
        }

        int winner=idx[0];
        Console.WriteLine(num[winner]);
        Console.WriteLine(string.Join(" ",op[winner]));
    }
}
