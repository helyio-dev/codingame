using System;
using System.Collections.Generic;

class Solution
{
    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        char[,] grid = new char[n, n];
        
        for (int i = 0; i < n; i++)
        {
            string line = Console.ReadLine();
            for (int j = 0; j < n; j++)
            {
                grid[i, j] = line[j];
            }
        }

        int[,] dirs = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
        char[,] result = new char[n, n];
        bool foundPath = false;
        
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                result[i, j] = '-';

        for (int i = 0; i < n && !foundPath; i++)
        {
            for (int j = 0; j < n && !foundPath; j++)
            {
                if (grid[i, j] == 'a')
                {
                    var q = new Queue<(int, int, char)>();
                    q.Enqueue((i, j, 'a'));
                    result[i, j] = 'a';
                    char[,] currentResult = new char[n, n];
                    Array.Copy(result, currentResult, n * n);

                    while (q.Count > 0)
                    {
                        var (x, y, current) = q.Dequeue();
                        for (int d = 0; d < 4; d++)
                        {
                            int nx = x + dirs[d, 0];
                            int ny = y + dirs[d, 1];
                            if (nx >= 0 && nx < n && ny >= 0 && ny < n &&
                                currentResult[nx, ny] == '-' && grid[nx, ny] == current + 1)
                            {
                                currentResult[nx, ny] = (char)(current + 1);
                                if (current + 1 == 'z')
                                {
                                    foundPath = true;
                                    result = currentResult;
                                    break;
                                }
                                q.Enqueue((nx, ny, (char)(current + 1)));
                            }
                        }
                        if (foundPath) break;
                    }
                    if (!foundPath)
                    {
                        for (int x = 0; x < n; x++)
                            for (int y = 0; y < n; y++)
                                if (currentResult[x, y] != '-')
                                    result[x, y] = '-';
                    }
                }
            }
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
                Console.Write(result[i, j]);
            Console.WriteLine();
        }
    }
}
