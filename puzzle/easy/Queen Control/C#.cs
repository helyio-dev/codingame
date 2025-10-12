using System;
using System.Text;

public class Solution
{
    public static void Main(string[] args)
    {
        Solve();
    }

    private static void Solve()
    {
        string queenColorStr = Console.ReadLine();
        string[] board = new string[8];
        
        for (int i = 0; i < 8; i++)
        {
            board[i] = Console.ReadLine();
        }

        char queenColor;
        char opponentColor;

        if (queenColorStr == "white")
        {
            queenColor = 'w';
            opponentColor = 'b';
        }
        else
        {
            queenColor = 'b';
            opponentColor = 'w';
        }

        int qr = -1;
        int qc = -1;

        for (int r = 0; r < 8; r++)
        {
            for (int c = 0; c < 8; c++)
            {
                if (board[r][c] == 'Q')
                {
                    qr = r;
                    qc = c;
                    goto QueenFound;
                }
            }
        }

    QueenFound:
        
        if (qr == -1)
        {
            Console.WriteLine(0);
            return;
        }

        int controlledSquares = 0;

        int[] dr = {-1, 1, 0, 0, -1, -1, 1, 1};
        int[] dc = {0, 0, -1, 1, -1, 1, -1, 1};

        for (int i = 0; i < 8; i++)
        {
            int r = qr;
            int c = qc;
            int currentDr = dr[i];
            int currentDc = dc[i];

            while (true)
            {
                r += currentDr;
                c += currentDc;

                if (!(r >= 0 && r < 8 && c >= 0 && c < 8))
                {
                    break;
                }

                char piece = board[r][c];

                if (piece == '.')
                {
                    controlledSquares++;
                    continue;
                }

                if (piece == queenColor || piece == 'Q')
                {
                    break;
                }

                if (piece == opponentColor)
                {
                    controlledSquares++;
                    break;
                }
            }
        }

        Console.WriteLine(controlledSquares);
    }
}