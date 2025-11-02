#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> dy = {0, 1, 0, -1};
vector<int> dx = {1, 0, -1, 0};
vector<char> dn = {'-', '|', '-', '|'};
vector<char> tail = {'>', 'v', '<', '^'};

int dfs(vector<string> &map, int y, int x)
{
    char curr = map[y][x];
    map[y][x] = '.';

    if (curr == 'v' || curr == '<' || curr == '>' || curr == '^')
    {
        return 1;
    }

    for (int d = 0; d < 4; d++)
    {
        int _y = y + dy[d];
        int _x = x + dx[d];

        if (!(_y >= 0 && _y < map.size() && _x >= 0 && _x < map[0].size()))
        {
            continue;
        }

        char next = map[_y][_x];

        if ((curr == '*' || curr == 'o') && next == dn[d])
        {
            return dfs(map, _y, _x) + 1;
        }
        if (curr == dn[d] && (next == dn[d] || next == '*' || next == 'o' || next == tail[d]))
        {
            return dfs(map, _y, _x) + 1;
        }
    }

    return -1;
}

int main()
{
    int n;
    int m;
    cin >> n >> m;
    cin.ignore();

    vector<string> map; 

    for (int i = 0; i < n; i++)
    {
        string t;
        getline(cin, t);

        map.push_back(t);
    }

    int maxSize = 0; 
    int count = 0;  

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (map[i][j] == 'o')
            {
                int result = dfs(map, i, j);

                if (result > maxSize)
                {
                    maxSize = result;
                    count = 1;
                }
                else if (result == maxSize)
                {
                    count++;
                }
            }
        }
    }

    cout << maxSize << endl << count << endl;
}