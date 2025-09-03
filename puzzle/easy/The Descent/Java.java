import java.util.*;
import java.io.*;
import java.math.*;

class Player {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);

        while (true) {
            int maxH = -1;
            int mountainToFire = 0;

            for (int i = 0; i < 8; i++) {
                int mountainH = in.nextInt();
                if (mountainH > maxH) {
                    maxH = mountainH;
                    mountainToFire = i;
                }
            }

            System.out.println(mountainToFire);
        }
    }
}
