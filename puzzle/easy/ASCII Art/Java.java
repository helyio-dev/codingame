import java.util.Scanner;

public class Solution
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        
        int L = Integer.parseInt(scanner.nextLine());
        int H = Integer.parseInt(scanner.nextLine());
        String T = scanner.nextLine().toUpperCase();
        
        final int unknownCharIndex = 'Z' - 'A' + 1;
        
        for (int i = 0; i < H; i++)
        {
            String asciiLine = scanner.nextLine();
            
            for (int j = 0; j < T.length(); j++)
            {
                int charIndex = T.charAt(j) - 'A';
                int letterIndex = Character.isLetter(T.charAt(j)) ? charIndex : unknownCharIndex;
                
                String asciiPart = asciiLine.substring(letterIndex * L, (letterIndex + 1) * L);
                
                System.out.print(asciiPart);
            }
            
            System.out.println();
        }
    }
}