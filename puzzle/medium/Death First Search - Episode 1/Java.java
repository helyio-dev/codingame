import java.util.*;

class Player {

    static class Node {
        int id;
        List<Node> neighbors = new ArrayList<>();
        boolean isGateway = false;
        Node(int id) { this.id = id; }
    }

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int L = in.nextInt();
        int E = in.nextInt();

        Node[] nodes = new Node[N];
        for (int i = 0; i < N; i++) nodes[i] = new Node(i);

        for (int i = 0; i < L; i++) {
            int N1 = in.nextInt();
            int N2 = in.nextInt();
            nodes[N1].neighbors.add(nodes[N2]);
            nodes[N2].neighbors.add(nodes[N1]);
        }

        for (int i = 0; i < E; i++) nodes[in.nextInt()].isGateway = true;

        while (true) {
            int SI = in.nextInt();
            boolean cut = false;
            for (Node neighbor : nodes[SI].neighbors) {
                if (neighbor.isGateway) {
                    System.out.println(SI + " " + neighbor.id);
                    nodes[SI].neighbors.remove(neighbor);
                    neighbor.neighbors.remove(nodes[SI]);
                    cut = true;
                    break;
                }
            }
            if (!cut) {
                outer: for (Node node : nodes) {
                    for (Node neighbor : node.neighbors) {
                        if (neighbor.isGateway) {
                            System.out.println(node.id + " " + neighbor.id);
                            node.neighbors.remove(neighbor);
                            neighbor.neighbors.remove(node);
                            break outer;
                        }
                    }
                }
            }
        }
    }
}
