import java.text.DecimalFormat;
import java.math.RoundingMode;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Solution {

    static Map<Integer, Integer> total = new HashMap<>();
    static Map<Integer, Integer> dices = new HashMap<>();
    static List<String> exprList = new ArrayList<>();

    static final String DICE = "DICE";

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String expr = in.nextLine();

        Matcher m = Pattern.compile("d[0-9]+").matcher(expr);

        int lastIndex = 0;
        while (m.find()) {
            String str = expr.substring(lastIndex, m.start());
            exprList.add(str);
            exprList.add(DICE);
            dices.put(exprList.size() - 1, Integer.parseInt(m.group().substring(1)));
            lastIndex = m.end();
        }
        if (lastIndex != expr.length()) exprList.add(expr.substring(lastIndex));

        evaluate("", exprList, 0);

        int nbCombination = total.values().stream().mapToInt(i -> i).sum();

        DecimalFormat format = new DecimalFormat("##.00");
        format.setRoundingMode(RoundingMode.HALF_UP);

        total.entrySet().stream()
                .sorted(Map.Entry.comparingByKey())
                .forEach(e -> System.out.println(e.getKey() + " " + format.format(e.getValue() * 100d / nbCombination)));
    }

    private static void evaluate(String eval, List<String> exprList, int index) {
        if (index >= exprList.size()) {
            int val = evalExpr(eval);
            total.put(val, total.getOrDefault(val, 0) + 1);
            return;
        }

        if (exprList.get(index).equals(DICE)) {
            for (int diceValue = 1; diceValue <= dices.get(index); diceValue++) {
                evaluate(eval + diceValue, exprList, index + 1);
            }
        } else {
            evaluate(eval + exprList.get(index), exprList, index + 1);
        }
    }

    private static int evalExpr(String expr) {
        return new Object() {
            int pos = -1, ch;

            void nextChar() { ch = (++pos < expr.length()) ? expr.charAt(pos) : -1; }
            boolean eat(int charToEat) {
                while (ch == ' ') nextChar();
                if (ch == charToEat) { nextChar(); return true; }
                return false;
            }

            int parse() {
                nextChar();
                int x = parseComparison();
                if (pos < expr.length()) throw new RuntimeException("Unexpected: " + (char)ch);
                return x;
            }

            int parseComparison() {
                int x = parseExpression();
                for (;;) {
                    if (eat('>')) {
                        if (eat('=')) x = (x >= parseExpression()) ? 1 : 0;
                        else x = (x > parseExpression()) ? 1 : 0;
                    } else if (eat('<')) {
                        if (eat('=')) x = (x <= parseExpression()) ? 1 : 0;
                        else x = (x < parseExpression()) ? 1 : 0;
                    } else if (eat('=')) {
                        if (eat('=')) x = (x == parseExpression()) ? 1 : 0;
                        else throw new RuntimeException("Unexpected '='");
                    } else if (eat('!')) {
                        if (eat('=')) x = (x != parseExpression()) ? 1 : 0;
                        else throw new RuntimeException("Unexpected '!'");
                    } else return x;
                }
            }

            int parseExpression() {
                int x = parseTerm();
                for (;;) {
                    if (eat('+')) x += parseTerm();
                    else if (eat('-')) x -= parseTerm();
                    else return x;
                }
            }

            int parseTerm() {
                int x = parseFactor();
                for (;;) {
                    if (eat('*')) x *= parseFactor();
                    else if (eat('/')) x /= parseFactor();
                    else return x;
                }
            }

            int parseFactor() {
                if (eat('+')) return parseFactor();
                if (eat('-')) return -parseFactor();

                int startPos = this.pos;
                if (ch >= '0' && ch <= '9') {
                    while (ch >= '0' && ch <= '9') nextChar();
                    return Integer.parseInt(expr.substring(startPos, this.pos));
                } else if (eat('(')) {
                    int x = parseComparison();
                    eat(')');
                    return x;
                }
                throw new RuntimeException("Unexpected: " + (char)ch);
            }
        }.parse();
    }
}
