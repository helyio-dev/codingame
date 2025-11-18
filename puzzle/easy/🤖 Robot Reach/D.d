import std;

int sumDigits(int n) {
    return n.to!string.map!(c => c - '0').sum;
}

void main()
{
    int R = readln.chomp.to!int;
    int C = readln.chomp.to!int;
    int T = readln.chomp.to!int;

    auto visited = new bool[][](R, C);
    Tuple!(int, int)[] queue;
    int count = 0;

    if (sumDigits(0) + sumDigits(0) <= T) {
        queue ~= tuple(0, 0);
        visited[0][0] = true;
        count++;
    }

    auto dirs = [tuple(0,1), tuple(1,0), tuple(0,-1), tuple(-1,0)];

    while (!queue.empty) {
        auto pos = queue.front;
        queue = queue[1..$];
        int x = pos[0], y = pos[1];

        foreach (dir; dirs) {
            int nx = x + dir[0], ny = y + dir[1];
            if (nx >= 0 && nx < R && ny >= 0 && ny < C && !visited[nx][ny]) {
                if (sumDigits(nx) + sumDigits(ny) <= T) {
                    visited[nx][ny] = true;
                    queue ~= tuple(nx, ny);
                    count++;
                }
            }
        }
    }

    writeln(count);
}