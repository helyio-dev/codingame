using System;
using System.Collections.Generic;

class Program{
    class Champ{
        public string Name;
        public int Life, Punch, Kick;
        public Champ(string n,int l,int p,int k){Name=n;Life=l;Punch=p;Kick=k;}
    }

    static void Main(){
        var champs=new Dictionary<string,Champ>{
            {"KEN",new Champ("KEN",25,6,5)},
            {"RYU",new Champ("RYU",25,4,5)},
            {"TANK",new Champ("TANK",50,2,2)},
            {"VLAD",new Champ("VLAD",30,3,3)},
            {"JADE",new Champ("JADE",20,2,7)},
            {"ANNA",new Champ("ANNA",18,9,1)},
            {"JUN",new Champ("JUN",60,2,1)}
        };

        var parts=Console.ReadLine().Split();
        string c1=parts[0], c2=parts[1];
        int n=int.Parse(Console.ReadLine());

        int life1=champs[c1].Life, life2=champs[c2].Life;
        int rage1=0,rage2=0,h1=0,h2=0,dmg1=0,dmg2=0;

        for(int i=0;i<n;i++){
            var line=Console.ReadLine().Split();
            string dir=line[0], atk=line[1];
            bool first=dir==">";
            string A=first?c1:c2, B=first?c2:c1;
            ref int lifeA=ref (first?ref life1:ref life2);
            ref int lifeB=ref (first?ref life2:ref life1);
            ref int rageA=ref (first?ref rage1:ref rage2);
            ref int rageB=ref (first?ref rage2:ref rage1);
            ref int hA=ref (first?ref h1:ref h2);
            ref int dmgA=ref (first?ref dmg1:ref dmg2);
            ref int dmgB=ref (first?ref dmg2:ref dmg1);
            int d=0;
            if(atk=="PUNCH")d=champs[A].Punch;
            else if(atk=="KICK")d=champs[A].Kick;
            else{
                if(A=="VLAD"){d=2*(rageA+rageB);rageB=0;}
                else if(A=="JADE")d=hA*rageA;
                else if(A=="ANNA")d=dmgA*rageA;
                else if(A=="JUN"){d=rageA;lifeA+=rageA;}
                else if(A=="KEN")d=3*rageA;
                else if(A=="RYU")d=4*rageA;
                else if(A=="TANK")d=2*rageA;
                rageA=0;
            }
            lifeB-=d;dmgB+=d;rageB++;hA++;
            if(life1<=0||life2<=0)break;
        }

        if(life1>life2)Console.WriteLine($"{c1} beats {c2} in {h1} hits");
        else Console.WriteLine($"{c2} beats {c1} in {h2} hits");
    }
}
