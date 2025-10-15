import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int K = in.nextInt();
        List<Integer> s = new ArrayList<>();
        for (int i = 0; i < K; i++) {
            float A = in.nextFloat();

            int val = 1;
            double fact = 0; 
            while (val * Math.log(A) > fact) {
                fact += Math.log(++val); 
            }

            s.add(val);
        }

        System.out.println(s.stream().map(String::valueOf).collect(Collectors.joining(" ")));
    }
}