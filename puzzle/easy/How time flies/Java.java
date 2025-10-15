import java.time.*;
import java.time.format.DateTimeFormatter;
import java.util.*;

class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd.MM.yyyy");
        LocalDate begin = LocalDate.parse(in.nextLine(), fmt);
        LocalDate end = LocalDate.parse(in.nextLine(), fmt);

        Period p = Period.between(begin, end);
        long totalDays = Duration.between(begin.atStartOfDay(), end.atStartOfDay()).toDays();

        StringBuilder sb = new StringBuilder();
        if (p.getYears() > 0) sb.append(p.getYears()).append(" year").append(p.getYears() > 1 ? "s" : "");
        if (p.getMonths() > 0) {
            if (sb.length() > 0) sb.append(", ");
            sb.append(p.getMonths()).append(" month").append(p.getMonths() > 1 ? "s" : "");
        }
        if (sb.length() > 0) sb.append(", ");
        sb.append("total ").append(totalDays).append(" days");

        System.out.println(sb.toString());
    }
}
