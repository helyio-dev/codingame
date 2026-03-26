import java.util.*;

class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        char[] num = in.nextLine().toCharArray();
        int neven = 0;
        for (char c : num)
            neven += (c % 2 == 0) ? 1 : 0;

        char[] evens = new char[neven];
        char[] odds = new char[num.length - neven];

        int ievens = 0, iodds = 0;
        for (char c : num) {
            if (c % 2 == 0)
                evens[ievens++] = c;
            else
                odds[iodds++] = c;
        }

        for (int ie = 0, io = 0; ie + io < num.length;) {
            if (ie == evens.length) {
                System.out.print(odds[io++]);
                continue;
            }
            if (io == odds.length) {
                System.out.print(evens[ie++]);
                continue;
            }
            if (evens[ie] > odds[io])
                System.out.print(evens[ie++]);
            else
                System.out.print(odds[io++]);
        }
        System.out.println();
    }
}