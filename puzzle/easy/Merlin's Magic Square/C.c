#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void xor_states(int *state1, const int *state2, int size) {
    for (int i = 0; i < size; i++) {
        state1[i] ^= state2[i];
    }
}

int main() {
    int I[9];
    char line[50];
    
    int I_idx = 0;
    for (int r = 0; r < 3; r++) {
        if (fgets(line, sizeof(line), stdin) == NULL) return 1;
        char *token = strtok(line, " \n\r");
        while (token != NULL) {
            I[I_idx++] = (token[0] == '*') ? 1 : 0;
            token = strtok(NULL, " \n\r");
        }
    }

    if (fgets(line, sizeof(line), stdin) == NULL) return 1;
    char *lizzo_moves = line;
    
    const int F_solved[] = {1, 1, 1, 1, 0, 1, 1, 1, 1};

    const int EFFECT_MAP[10][9] = {
        {0, 0, 0, 0, 0, 0, 0, 0, 0}, 
        {1, 1, 0, 1, 1, 0, 0, 0, 0}, 
        {1, 1, 1, 0, 0, 0, 0, 0, 0}, 
        {0, 1, 1, 0, 1, 1, 0, 0, 0}, 
        {1, 0, 0, 1, 0, 0, 1, 0, 0}, 
        {0, 1, 0, 1, 1, 1, 0, 1, 0}, 
        {0, 0, 1, 0, 0, 1, 0, 0, 1}, 
        {0, 0, 0, 1, 1, 0, 1, 1, 0}, 
        {0, 0, 0, 0, 0, 0, 1, 1, 1}, 
        {0, 0, 0, 0, 1, 1, 0, 1, 1}  
    };

    int L_effect[9] = {0};
    for (int k = 0; lizzo_moves[k] != '\0' && lizzo_moves[k] != '\n' && lizzo_moves[k] != '\r'; k++) {
        int button = lizzo_moves[k] - '0';
        if (button >= 1 && button <= 9) {
            xor_states(L_effect, EFFECT_MAP[button], 9);
        }
    }

    int S_Lizzo[9];
    memcpy(S_Lizzo, I, sizeof(I));
    xor_states(S_Lizzo, L_effect, 9);

    int R[9];
    memcpy(R, F_solved, sizeof(R));
    xor_states(R, S_Lizzo, 9);

    for (int button = 1; button <= 9; button++) {
        int match = 1;
        for (int j = 0; j < 9; j++) {
            if (EFFECT_MAP[button][j] != R[j]) {
                match = 0;
                break;
            }
        }
        if (match) {
            printf("%d\n", button);
            break;
        }
    }

    return 0;
}