import 'dart:io';

int sumDigits(int n) {
  return n.toString().split('').map((c) => int.parse(c)).reduce((a, b) => a + b);
}

void main() {
  int R = int.parse(stdin.readLineSync()!);
  int C = int.parse(stdin.readLineSync()!);
  int T = int.parse(stdin.readLineSync()!);

  List<List<bool>> visited = List.generate(R, (_) => List.filled(C, false));
  List<List<int>> queue = [];
  int count = 0;

  if (sumDigits(0) + sumDigits(0) <= T) {
    queue.add([0, 0]);
    visited[0][0] = true;
    count = 1;
  }

  List<List<int>> directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];

  while (queue.isNotEmpty) {
    List<int> cell = queue.removeAt(0);
    int x = cell[0], y = cell[1];

    for (List<int> dir in directions) {
      int nx = x + dir[0];
      int ny = y + dir[1];

      if (nx >= 0 && nx < R && ny >= 0 && ny < C && !visited[nx][ny]) {
        if (sumDigits(nx) + sumDigits(ny) <= T) {
          visited[nx][ny] = true;
          queue.add([nx, ny]);
          count++;
        }
      }
    }
  }

  print(count);
}