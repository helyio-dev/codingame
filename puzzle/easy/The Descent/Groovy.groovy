import java.util.Scanner

def input = new Scanner(System.in);

// game loop
while (true) {
    def maxH = -1
    def mountainToFire = 0
    for (i = 0; i < 8; ++i) {
        def mountainH = input.nextInt()
        if (mountainH > maxH) {
            maxH = mountainH
            mountainToFire = i
        }
    }
    println mountainToFire
}
