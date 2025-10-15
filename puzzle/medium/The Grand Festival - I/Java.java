import java.util.Scanner;

class Solution {

    static int R;
    static int[] prizes;
    static int[][] sumForIndexes;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        R = in.nextInt();

        sumForIndexes = new int[N][R];

        prizes = new int[N];
        for (int i = 0; i < N; i++) {
            prizes[i] = in.nextInt();
        }

        int res = Math.max(calcMaxFromIndex(0, R), calcMaxFromIndex(1, R));
        System.out.println(res);
    }

    static int calcMaxFromIndex(int index, int nbDays) {
        nbDays--;

        if (index >= prizes.length) {
            return 0;
        }

        if (sumForIndexes[index][nbDays] != 0) {
            return sumForIndexes[index][nbDays];
        }

        if (nbDays > 0) {
            sumForIndexes[index][nbDays] = prizes[index] + Math.max(calcMaxFromIndex(index + 1, nbDays), calcMaxFromIndex(index + 2, R));
        } else {
            sumForIndexes[index][nbDays] = prizes[index] + Math.max(calcMaxFromIndex(index + 2, R), calcMaxFromIndex(index + 3, R));
        }

        return sumForIndexes[index][nbDays];
    }
}