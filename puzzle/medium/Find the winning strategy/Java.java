import java.util.Scanner;

class Player {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int rows = in.nextInt(); 
        in.nextInt(); 

        int[][] grid = new int[rows][2];

        while (true) {
            int nimSum = 0;
            for (int i = 0; i < rows; i++) {
                int xPlayer = in.nextInt();
                int xBoss = in.nextInt(); 

                int nimber = xBoss - xPlayer - 1;
                nimSum ^= nimber;

                grid[i] = new int[]{xPlayer, nimber};
            }

            for (int i = 0; i < rows; i++) {
                int test = grid[i][1] ^ nimSum;
                if (test <= grid[i][1]) {
                    System.out.println(i + " " + (grid[i][0] + (grid[i][1] - test)));
                    break;
                }
            }
        }
    }
}