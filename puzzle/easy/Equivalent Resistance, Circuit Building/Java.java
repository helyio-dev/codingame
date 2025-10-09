import java.util.*;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());
        Map<String, Double> resistors = new HashMap<>();
        for (int i = 0; i < N; i++) {
            String[] parts = sc.nextLine().split(" ");
            resistors.put(parts[0], Double.parseDouble(parts[1]));
        }
        String[] expr = sc.nextLine().split(" ");

        Stack<Object> stack = new Stack<>();
        for (String token : expr) {
            if (token.equals("(") || token.equals("[")) {
                stack.push(token);
            } else if (token.equals(")") || token.equals("]")) {
                List<Double> temp = new ArrayList<>();
                while (!stack.isEmpty() && stack.peek() instanceof Double) {
                    temp.add(0, (Double) stack.pop());
                }
                String start = (String) stack.pop();
                double result;
                if (start.equals("(")) {
                    result = 0;
                    for (double v : temp) result += v;
                } else {
                    result = 0;
                    for (double v : temp) result += 1.0 / v;
                    result = 1.0 / result;
                }
                stack.push(result);
            } else {
                stack.push(resistors.get(token));
            }
        }
        double res = (Double) stack.pop();
        System.out.printf("%.1f%n", res);
    }
}
