import std;

void main()
{
    while (1) {
        string enemy1 = readln.chomp;
        int dist1 = readln.chomp.to!int;
        string enemy2 = readln.chomp;
        int dist2 = readln.chomp.to!int;

        if (dist1 < dist2) {
            writeln(enemy1);
        } else {
            writeln(enemy2);
        }
    }
}
