using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{
    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        int remainder = 1;

        string res = "";
        int idx = 0;
        Dictionary<int, int> values = new Dictionary<int, int>();
        
        while (remainder != 0){
            if (values.ContainsKey(remainder)){
                string left = res[0..values[remainder]];
                string right = res[values[remainder]..res.Length];
                res = left + "(" + right + ")";
                break;
            }
            values[remainder] = idx;

            remainder *= 10;
            int val = remainder / n;
            res += val.ToString();
            remainder = remainder % n;
            
            idx += 1;
        }
        Console.WriteLine("0."+res);
    }
}