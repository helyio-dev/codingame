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
        string[] inputs = Console.ReadLine().Split(' ');
        int lightX = int.Parse(inputs[0]);
        int lightY = int.Parse(inputs[1]);
        int x = int.Parse(inputs[2]);
        int y = int.Parse(inputs[3]); 

        while (true)
        {
            int remainingTurns = int.Parse(Console.ReadLine()); 
            var move = new StringBuilder();

            if (y < lightY)
            {
              move.Append('S');
              y++;
            }
            else if (y > lightY)
            {
              move.Append('N');
              y--;
            }

            if (x < lightX)
            {
              move.Append('E');
              x++;
            }
            else if (x > lightX)
            {
              move.Append('W');
              x--;
            }

            Console.WriteLine(move.ToString());
        }
    }
}