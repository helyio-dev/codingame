import java.util.*;

class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(); 
        int a = in.nextInt();
        int b = in.nextInt(); 
        int k = in.nextInt(); 
        int m = in.nextInt();

        Set<Integer> visited = new HashSet<>();
        visited.add(k);
        if (k < m)
            while (Math.abs(k + a - m) < Math.abs(k - m) && k + a >= 1 && k + a <= n)
                visited.add(k += a);
        else if (k > m)
            while (Math.abs(k - b - m) < Math.abs(k - m) && k - b >= 1 && k - b <= n)
                visited.add(k -= b);
        while (k != m) {
            if (k + a <= n && k < m) {
                k += a;
            } else if (k - b >= 1 && k > m) {
                k -= b;
            } else {
                if (k + a <= n) k += a;
                else if (k - b >= 1) k -= b;
            }
            if (!visited.add(k)) {
                System.out.println("IMPOSSIBLE");
                return;
            }
        }
        System.out.println(visited.size() - 1);
    }
}