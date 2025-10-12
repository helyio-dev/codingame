#include <stdio.h>
#include <string.h>

void solve() {
    char queen_color_str[6];
    char board[8][9];
    char queen_color;
    char opponent_color;
    int qr = -1, qc = -1;
    int controlled_squares = 0;

    if (scanf("%s", queen_color_str) != 1) return;

    if (strcmp(queen_color_str, "white") == 0) {
        queen_color = 'w';
        opponent_color = 'b';
    } else {
        queen_color = 'b';
        opponent_color = 'w';
    }

    for (int i = 0; i < 8; i++) {
        if (scanf("%s", board[i]) != 1) return;
        for (int j = 0; j < 8; j++) {
            if (board[i][j] == 'Q') {
                qr = i;
                qc = j;
            }
        }
    }

    if (qr == -1) {
        printf("0\n");
        return;
    }

    int directions[16] = {-1, 0, 1, 0, 0, -1, 0, 1, -1, -1, -1, 1, 1, -1, 1, 1};

    for (int i = 0; i < 8; i++) {
        int dr = directions[2 * i];
        int dc = directions[2 * i + 1];
        
        int r = qr;
        int c = qc;
        
        while (1) {
            r += dr;
            c += dc;
            
            if (!(r >= 0 && r < 8 && c >= 0 && c < 8)) {
                break;
            }
            
            char piece = board[r][c];
            
            if (piece == '.') {
                controlled_squares++;
                continue;
            }

            if (piece == queen_color || piece == 'Q') {
                break;
            }
            
            if (piece == opponent_color) {
                controlled_squares++;
                break;
            }
        }
    }

    printf("%d\n", controlled_squares);
}

int main() {
    solve();
    return 0;
}