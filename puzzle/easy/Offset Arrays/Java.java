import java.util.*;

class Solution {
    static class ArrayDef {
        int start;
        int[] values;
        ArrayDef(int start, int[] values) {
            this.start = start;
            this.values = values;
        }
        int get(int index) {
            return values[index - start];
        }
    }

    static Map<String, ArrayDef> arrays = new HashMap<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        for (int k = 0; k < n; k++) {
            String line = sc.nextLine();
            String[] parts = line.split("=");
            String left = parts[0].trim();
            String right = parts[1].trim();
            int lbr = left.indexOf('[');
            int rbr = left.indexOf(']');
            String name = left.substring(0, lbr);
            String[] bounds = left.substring(lbr + 1, rbr).split("\\.\\.");
            int start = Integer.parseInt(bounds[0]);
            String[] vals = right.split(" ");
            int[] values = new int[vals.length];
            for (int i = 0; i < vals.length; i++) values[i] = Integer.parseInt(vals[i]);
            arrays.put(name, new ArrayDef(start, values));
        }
        String query = sc.nextLine().trim();
        System.out.println(evaluate(query));
    }

    static int evaluate(String expr) {
        while (expr.contains("[")) {
            int lastOpen = expr.lastIndexOf('[');
            int close = expr.indexOf(']', lastOpen);
            String indexPart = expr.substring(lastOpen + 1, close);
            int index = evaluate(indexPart);
            int start = lastOpen;
            while (start > 0 && Character.isLetter(expr.charAt(start - 1))) start--;
            String name = expr.substring(start, lastOpen);
            int val = arrays.get(name).get(index);
            expr = expr.substring(0, start) + val + expr.substring(close + 1);
        }
        return Integer.parseInt(expr);
    }
}
