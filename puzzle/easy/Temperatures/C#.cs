using System;

class Solution
{
  static void Main(string[] args)
  {
    int n = int.Parse(Console.ReadLine()); 
    int minT = 5526;
    string[] inputs = Console.ReadLine().Split(' ');
    for (int i = 0; i < n; i++)
    {
      int t = int.Parse(inputs[i]); 
      if (Math.Abs(t) < Math.Abs(minT) || Math.Abs(t) == Math.Abs(minT) && t > minT)
      {
        minT = t;
      }
    }

    if (n == 0)
    {
      Console.WriteLine(0);
    }
    else
    {
      Console.WriteLine(minT);
    }
  }
}