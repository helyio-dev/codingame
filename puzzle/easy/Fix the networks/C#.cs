using System;
using System.Text;
using System.Linq;

public class CidrFixer
{
    private static uint IpToUint(string ipAddr)
    {
        string[] parts = ipAddr.Split('.');
        uint result = 0;
        result |= uint.Parse(parts[0]) << 24;
        result |= uint.Parse(parts[1]) << 16;
        result |= uint.Parse(parts[2]) << 8;
        result |= uint.Parse(parts[3]);
        return result;
    }

    private static int CountTrailingZeros(uint n)
    {
        if (n == 0) return 32;
        int count = 0;
        while ((n & 1) == 0)
        {
            n >>= 1;
            count++;
        }
        return count;
    }

    public static void Main()
    {
        int M;
        if (!int.TryParse(Console.ReadLine(), out M)) return;

        for (int i = 0; i < M; i++)
        {
            string line = Console.ReadLine();
            if (string.IsNullOrWhiteSpace(line)) continue;

            string[] ipCidr = line.Split('/');
            string ipAddr = ipCidr[0];
            int S = int.Parse(ipCidr[1]);

            uint A = IpToUint(ipAddr);
            int V = 32 - S;
            ulong N = 1UL << V;
            
            bool isValid = false;
            if (V == 32)
            {
                if (A == 0)
                {
                    isValid = true;
                }
            }
            else
            {
                uint mask = (1U << V) - 1;
                if ((A & mask) == 0)
                {
                    isValid = true;
                }
            }

            if (isValid)
            {
                Console.WriteLine($"valid {N}");
            }
            else
            {
                int T = CountTrailingZeros(A);
                int SNew = 32 - T;
                ulong NNew = 1UL << T;
                
                Console.WriteLine($"invalid {ipAddr}/{SNew} {NNew}");
            }
        }
    }
}