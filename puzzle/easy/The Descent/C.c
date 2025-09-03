#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    while (1) {
        int max_h = -1;
        int mountain_to_fire = 0;

        for (int i = 0; i < 8; i++) {
            int mountain_h;
            scanf("%d", &mountain_h);
            if (mountain_h > max_h) {
                max_h = mountain_h;
                mountain_to_fire = i;
            }
        }
        printf("%d\n", mountain_to_fire);
    }
    return 0;
}
