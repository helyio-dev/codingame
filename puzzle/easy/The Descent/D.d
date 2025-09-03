import std;

void main()
{
    while (1) {
        int maxH = -1;
        int mountainToFire = 0;
        
        for (int i = 0; i < 8; i++) {
            int mountainH = readln.chomp.to!int;
            if (mountainH > maxH) {
                maxH = mountainH;
                mountainToFire = i;
            }
        }
        writeln(mountainToFire);
    }
}
