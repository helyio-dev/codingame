import java.util.Scanner;

class Player {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int nbFloors = in.nextInt(); 
        int width = in.nextInt(); 
        int nbRounds = in.nextInt(); 
        int exitFloor = in.nextInt(); 
        int exitPos = in.nextInt(); 
        int nbTotalClones = in.nextInt(); 
        int nbAdditionalElevators = in.nextInt(); 
        int nbElevators = in.nextInt(); 
        int[] floors = new int[nbElevators+1];
        floors[exitFloor] = exitPos;
        for (int i = 0; i < nbElevators; i++) {
            floors[in.nextInt()] = in.nextInt();
        }

        while (true) {
            int floor = in.nextInt(); 
            int pos = in.nextInt(); 
            int dir = in.next().compareTo("NONE");

            boolean block = (floor >= 0) && (dir < 1 ? pos < floors[floor] : dir > 1 && pos > floors[floor]);

            System.out.println(block  ? "BLOCK" : "WAIT");
        }
    }
}