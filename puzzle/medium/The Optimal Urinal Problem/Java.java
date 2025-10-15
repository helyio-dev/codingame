import java.util.*;

class Solution {
    static int N;
    static int[] memoTwo;
    static boolean[] seenTwo;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        in.close();

        N = n;
        memoTwo = new int[N + 1];
        seenTwo = new boolean[N + 1];

        int bestCount = 0;
        int bestIdx = 1;

        for (int i = 1; i <= n; i++) {
            int leftLen = i - 2;
            int rightLen = n - i - 1;
            int total = 1 + fOne(leftLen) + fOne(rightLen);
            if (total > bestCount) {
                bestCount = total;
                bestIdx = i;
            }
        }

        System.out.println(bestCount + " " + bestIdx);
    }

    static int fOne(int L) {
        if (L <= 0) return 0;
        return 1 + fTwo(L - 2);
    }

    static int fTwo(int L) {
        if (L <= 0) return 0;
        if (seenTwo[L]) return memoTwo[L];

        int res;
        if (L % 2 == 1) {
            int p = (L + 1) / 2;
            int left = p - 2;
            int right = L - p - 1;
            res = 1 + fTwo(left) + fTwo(right);
        } else {
            int p1 = L / 2;
            int left1 = p1 - 2;
            int right1 = L - p1 - 1;
            int a = fTwo(left1) + fTwo(right1);

            int p2 = p1 + 1;
            int left2 = p2 - 2;
            int right2 = L - p2 - 1;
            int b = fTwo(left2) + fTwo(right2);

            res = 1 + Math.max(a, b);
        }

        seenTwo[L] = true;
        memoTwo[L] = res;
        return res;
    }
}
