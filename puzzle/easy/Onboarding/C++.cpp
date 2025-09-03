#include <iostream>
#include <string>
#include <vector>

int main()
{
    while (1) {
        std::string enemy1;
        std::cin >> enemy1;
        int dist1;
        std::cin >> dist1;
        std::string enemy2;
        std::cin >> enemy2;
        int dist2;
        std::cin >> dist2;

        if (dist1 < dist2) {
            std::cout << enemy1 << std::endl;
        } else {
            std::cout << enemy2 << std::endl;
        }
    }

    return 0;
}
