using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

public class Zeckendorf
{
    public static void Main()
    {
        long N;
        if (!long.TryParse(Console.ReadLine(), out N)) return;

        if (N <= 0) return;

        List<long> fib = new List<long>();
        fib.Add(1);
        fib.Add(2);
        
        while (true)
        {
            long nextFib = fib[fib.Count - 1] + fib[fib.Count - 2];
            if (nextFib > N)
            {
                break;
            }
            fib.Add(nextFib);
        }

        List<string> representation = new List<string>();
        
        for (int i = fib.Count - 1; i >= 0; i--)
        {
            long f = fib[i];
            if (N >= f)
            {
                representation.Add(f.ToString());
                N -= f;
            }
        }

        Console.WriteLine(string.Join("+", representation));
    }
}