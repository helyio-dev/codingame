#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 10

int main() {
    int h;
    if (scanf("%d", &h) != 1) return 1;

    int c;
    while ((c = getchar()) != '\n' && c != EOF);

    int w = 0;
    char line[MAX_SIZE * 6];
    int grid[MAX_SIZE][MAX_SIZE];
    
    int row = 0;
    while (row < h) {
        if (fgets(line, sizeof(line), stdin) == NULL) {
            row++; 
            continue;
        }
        
        if (row == 0) {
            char temp_line[sizeof(line)];
            strcpy(temp_line, line);
            
            char *temp_token = strtok(temp_line, " \n\r");
            while (temp_token != NULL) {
                w++;
                temp_token = strtok(NULL, " \n\r");
            }
        }
        
        char *token = strtok(line, " \n\r");
        int col = 0;
        
        while (token != NULL) {
            if (sscanf(token, "%d", &grid[row][col]) == 1) {
                col++;
            }
            token = strtok(NULL, " \n\r");
        }
        row++;
    }

    char peaks_str[1000] = "";
    char valleys_str[1000] = "";
    int peak_count = 0;
    int valley_count = 0;

    int dr[] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int dc[] = {-1, 0, 1, -1, 1, -1, 0, 1};

    for (int r = 0; r < h; r++) {
        for (int c = 0; c < w; c++) {
            int current_val = grid[r][c];
            int is_peak = 1;
            int is_valley = 1;

            for (int i = 0; i < 8; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (nr >= 0 && nr < h && nc >= 0 && nc < w) {
                    int neighbor_val = grid[nr][nc];

                    if (current_val <= neighbor_val) {
                        is_peak = 0;
                    }

                    if (current_val >= neighbor_val) {
                        is_valley = 0;
                    }

                    if (is_peak == 0 && is_valley == 0) {
                        break;
                    }
                }
            }

            if (is_peak) {
                char coord_str[20];
                snprintf(coord_str, sizeof(coord_str), "(%d, %d)", c, r);
                
                if (peak_count > 0) {
                    strcat(peaks_str, ", ");
                }
                strcat(peaks_str, coord_str);
                peak_count++;
            }
            
            if (is_valley) {
                char coord_str[20];
                snprintf(coord_str, sizeof(coord_str), "(%d, %d)", c, r);
                
                if (valley_count > 0) {
                    strcat(valleys_str, ", ");
                }
                strcat(valleys_str, coord_str);
                valley_count++;
            }
        }
    }

    if (peak_count == 0) {
        printf("NONE\n");
    } else {
        printf("%s\n", peaks_str);
    }

    if (valley_count == 0) {
        printf("NONE\n");
    } else {
        printf("%s\n", valleys_str);
    }

    return 0;
}