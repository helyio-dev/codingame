import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;

class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int tributes = in.nextInt();
        in.nextLine();

        Map<String, Tribute> map = new LinkedHashMap<>();
        for (int i = 0; i < tributes; i++) {
            String name = in.nextLine();
            map.put(name, new Tribute(name));
        }
        int turns = in.nextInt();
        in.nextLine();

        for (int i = 0; i < turns; i++) {
            String line = in.nextLine();
            String[] parts = line.split(" killed ");
            String killerName = parts[0];
            String[] victims = parts[1].split(", ");

            for (String victimName : victims) {
                Tribute killer = map.get(killerName);
                killer.killed.add(victimName);

                Tribute victim = map.get(victimName);
                victim.killer = killerName;
            }
        }

        AtomicInteger idx = new AtomicInteger();
        map.values().stream()
                .sorted(Comparator.comparing(t -> t.name))
                .forEach(t -> {
                    if (idx.getAndIncrement() > 0) System.out.println();
                    System.out.println("Name: " + t.name);
                    t.killed.sort(String::compareTo);
                    System.out.println("Killed: " + (t.killed.isEmpty() ? "None" : String.join(", ", t.killed)));
                    System.out.println("Killer: " + (t.killer.isEmpty() ? "Winner" : t.killer));
                });
    }
}

class Tribute {
    String name;
    String killer = "";
    List<String> killed = new ArrayList<>();

    public Tribute(String name) {
        this.name = name;
    }
}
