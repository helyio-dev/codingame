using System;
using System.Collections.Generic;

class Program{
    static void Main(){
        var wh=Console.ReadLine().Split(); int w=int.Parse(wh[0]),h=int.Parse(wh[1]);
        long n=long.Parse(Console.ReadLine());
        char[][] grid=new char[h][];
        for(int i=0;i<h;i++) grid[i]=Console.ReadLine().ToCharArray();
        int[,] dirs={{0,-1},{1,0},{0,1},{-1,0}};
        int x=0,y=0,d=0;
        for(y=0;y<h;y++)
            for(x=0;x<w;x++)
                if(grid[y][x]=='O') goto start;
        start:;
        var seen=new Dictionary<(int,int,int), (long,int,int)>();
        long steps=0;
        while(steps<n){
            var state=(x,y,d);
            if(seen.ContainsKey(state)){
                var cycle=steps-seen[state].Item1;
                long rem=(n-steps)%cycle;
                (x,y,d)=(seen[state].Item2,seen[state].Item3,d);
                n=steps+rem;
            }else seen[state]=(steps,x,y);
            int nx=x+dirs[d,0],ny=y+dirs[d,1];
            while(grid[ny][nx]=='#') {d=(d+1)%4; nx=x+dirs[d,0]; ny=y+dirs[d,1];}
            x=nx;y=ny;steps++;
        }
        Console.WriteLine($"{x} {y}");
    }
}
