import java.util.Scanner;

class Solution {

    private static long[] houses;
    private static long[] sumForIndexes;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();

        houses = new long[N];
        for (int i = 0; i < N; i++) {
            houses[i] = in.nextLong();
        }

        sumForIndexes = new long[N];

        long res = Math.max(calcMaxFromIndex(0), calcMaxFromIndex(1));
        System.out.println(res);
    }

    static long calcMaxFromIndex(int index) {
        if (index >= houses.length) {
            return 0;
        }

        if (sumForIndexes[index] != 0) {
            return sumForIndexes[index];
        }

        long right2 = Math.max(calcMaxFromIndex(index + 2), calcMaxFromIndex(index + 3));

        sumForIndexes[index] = (houses[index] > 0 ? houses[index] : 0) + (right2 > 0 ? right2 : 0);

        return sumForIndexes[index];
    }
}