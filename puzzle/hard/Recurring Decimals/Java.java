import java.util.*;
class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int remainder = 1;

        StringBuilder res = new StringBuilder();
        HashMap<Integer, Integer> values = new HashMap<>();
        int idx = 0;

        while (remainder != 0){
            if (values.containsKey(remainder)){
                res.insert((int)values.get(remainder), '(');
                res.append(')');
                break;
            }
            values.put(remainder, idx);

            remainder *= 10;
            int value = remainder / n;
            res.append(String.valueOf(value));
            remainder = remainder % n;

            idx += 1;
        }
        System.out.println("0."+res.toString());
        in.close();
    }
}