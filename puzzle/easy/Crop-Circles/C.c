#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define WIDTH 19
#define HEIGHT 25
#define CROP_PLANTED "{}"
#define CROP_MOWED "  "

void apply_circle(char field[HEIGHT][WIDTH * 2 + 1], int cx, int cy, int d, int operation) {
    long long d_sq = (long long)d * d;

    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            long long dx = (long long)x - cx;
            long long dy = (long long)y - cy;
            
            if (4 * (dx * dx + dy * dy) <= d_sq) {
                char *target = field[y] + x * 2;
                
                if (operation == 0) {
                    memcpy(target, CROP_MOWED, 2);
                } else if (operation == 1) {
                    memcpy(target, CROP_PLANTED, 2);
                } else if (operation == 2) {
                    if (target[0] == '{') {
                        memcpy(target, CROP_MOWED, 2);
                    } else {
                        memcpy(target, CROP_PLANTED, 2);
                    }
                }
            }
        }
    }
}

int get_coord(char c) {
    return c - 'a';
}

int main() {
    char input[2048];
    if (scanf("%[^\n]", input) != 1) {
        return 0;
    }

    char field[HEIGHT][WIDTH * 2 + 1];
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            memcpy(field[i] + j * 2, CROP_PLANTED, 2);
        }
        field[i][WIDTH * 2] = '\0';
    }

    char *token = strtok(input, " ");
    while (token != NULL) {
        int op = 0;
        int start = 0;

        if (strncmp(token, "PLANTMOW", 8) == 0) {
            op = 2;
            start = 8;
        } else if (strncmp(token, "PLANT", 5) == 0) {
            op = 1;
            start = 5;
        } else {
            op = 0;
            start = 0;
        }

        char x_char = token[start];
        char y_char = token[start + 1];
        int d;
        sscanf(token + start + 2, "%d", &d);

        int cx = get_coord(x_char);
        int cy = get_coord(y_char);

        apply_circle(field, cx, cy, d, op);

        token = strtok(NULL, " ");
    }

    for (int i = 0; i < HEIGHT; i++) {
        printf("%s\n", field[i]);
    }

    return 0;
}