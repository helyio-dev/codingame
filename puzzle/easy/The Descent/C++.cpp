#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    while (1) {
        int max_h = -1;
        int mountain_to_fire = 0;

        for (int i = 0; i < 8; i++) {
            int mountain_h;
            cin >> mountain_h;
            if (mountain_h > max_h) {
                max_h = mountain_h;
                mountain_to_fire = i;
            }
        }
        cout << mountain_to_fire << endl;
    }
}
