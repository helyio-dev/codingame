import java.util.Scanner;

class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long r1 = in.nextLong();
        long r2 = in.nextLong();

        boolean found = false;
        while (!found) {
            if (r1 < r2) {
                r1 = nextRiver(r1);
            } else if (r2 < r1) {
                r2 = nextRiver(r2);
            } else {
                found = true;
            }
        }

        System.out.println(r1);
    }

    private static long nextRiver(long n) {
        long s = n;
        while (s > 0) {
            n = n + (s % 10);
            s = s / 10;
        }
        return n;
    }
}