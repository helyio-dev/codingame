using System;

class Program{
    static bool PointInTriangle(int px,int py,int[] t){
        int Sign(int x1,int y1,int x2,int y2,int x3,int y3){
            return (x1-x3)*(y2-y3)-(x2-x3)*(y1-y3);
        }
        int d1=Sign(px,py,t[0],t[1],t[2],t[3]);
        int d2=Sign(px,py,t[2],t[3],t[4],t[5]);
        int d3=Sign(px,py,t[4],t[5],t[0],t[1]);
        bool has_neg=(d1<0)||(d2<0)||(d3<0);
        bool has_pos=(d1>0)||(d2>0)||(d3>0);
        return !(has_neg && has_pos);
    }

    static void Main(){
        var parts=Console.ReadLine().Split();
        int HI=int.Parse(parts[0]), WI=int.Parse(parts[1]);
        string style=Console.ReadLine();
        int howManyTriangles=int.Parse(Console.ReadLine());
        int[][] triangles=new int[howManyTriangles][];
        for(int i=0;i<howManyTriangles;i++){
            triangles[i]=Array.ConvertAll(Console.ReadLine().Split(),int.Parse);
        }
        char[,] grid=new char[HI,WI];
        for(int y=0;y<HI;y++)
            for(int x=0;x<WI;x++)
                grid[y,x]='*';

        foreach(var t in triangles){
            int minX=Math.Max(0, Math.Min(t[0], Math.Min(t[2], t[4])));
            int maxX=Math.Min(WI-1, Math.Max(t[0], Math.Max(t[2], t[4])));
            int minY=Math.Max(0, Math.Min(t[1], Math.Min(t[3], t[5])));
            int maxY=Math.Min(HI-1, Math.Max(t[1], Math.Max(t[3], t[5])));
            for(int y=minY;y<=maxY;y++)
                for(int x=minX;x<=maxX;x++)
                    if(PointInTriangle(x,y,t))
                        grid[y,x]=(grid[y,x]=='*')?' ':'*';
        }

        for(int y=0;y<HI;y++){
            for(int x=0;x<WI;x++){
                Console.Write(grid[y,x]);
                if(style=="expanded" && x!=WI-1) Console.Write(" ");
            }
            Console.WriteLine();
        }
    }
}
