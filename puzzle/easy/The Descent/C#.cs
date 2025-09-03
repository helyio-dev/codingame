using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Player
{
    static void Main(string[] args)
    {
        while (true)
        {
            int maxH = -1;
            int mountainToFire = 0;

            for (int i = 0; i < 8; i++)
            {
                int mountainH = int.Parse(Console.ReadLine());
                if (mountainH > maxH)
                {
                    maxH = mountainH;
                    mountainToFire = i;
                }
            }

            Console.WriteLine(mountainToFire);
        }
    }
}
