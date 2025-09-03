import java.util.Scanner

def input = new Scanner(System.in);

while (true) {
    def enemy1 = input.next();
    def dist1 = input.nextInt();
    def enemy2 = input.next();
    def dist2 = input.nextInt();

    if (dist1 < dist2) {
        println enemy1
    } else {
        println enemy2
    }
}
