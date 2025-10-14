#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char direction[6];
    int howManyArrows;
    int heightOfArrows;
    int strokeThicknessOfArrows;
    int spacingBetweenArrows;
    int additionalIndentOfEachLine;

    char allInput[100];
    if (fgets(allInput, sizeof(allInput), stdin) == NULL) {
        return 1;
    }

    if (sscanf(allInput, "%s %d %d %d %d %d",
               direction,
               &howManyArrows,
               &heightOfArrows,
               &strokeThicknessOfArrows,
               &spacingBetweenArrows,
               &additionalIndentOfEachLine) != 6) {
        return 1;
    }

    char arrowChar = (strcmp(direction, "left") == 0) ? '<' : '>';

    int centerRow = heightOfArrows / 2;
    int maxIndent = centerRow * additionalIndentOfEachLine;
    
    int useLiteralLogic = (strcmp(direction, "left") == 0); 

    for (int i = 0; i < heightOfArrows; i++) {
        int distFromCenter = (i > centerRow) ? (i - centerRow) : (centerRow - i);
        
        int currentIndent;
        
        if (useLiteralLogic) {
            currentIndent = distFromCenter * additionalIndentOfEachLine;
        } else {
            currentIndent = maxIndent - (distFromCenter * additionalIndentOfEachLine);
        }

        for (int j = 0; j < currentIndent; j++) {
            printf(" ");
        }

        for (int a = 0; a < howManyArrows; a++) {
            for (int t = 0; t < strokeThicknessOfArrows; t++) {
                printf("%c", arrowChar);
            }

            if (a < howManyArrows - 1) {
                for (int s = 0; s < spacingBetweenArrows; s++) {
                    printf(" ");
                }
            }
        }

        printf("\n");
    }

    return 0;
}