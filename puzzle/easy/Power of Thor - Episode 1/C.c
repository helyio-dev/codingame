#include <stdio.h>

int main() {
  int lightX; 
  int lightY; 
  int x; 
  int y; 
  scanf("%d%d%d%d", &lightX, &lightY, &x, &y);

  while (1) {

    if (y > lightY) {
      printf("N");
      y--;
    } else if (y < lightY) {
      printf("S");
      y++;
    }

    if (x > lightX) {
      printf("W");
      x--;
    } else if (x < lightX) {
      printf("E");
      x++;
    }

    printf("\n");
  }

  return 0;
}