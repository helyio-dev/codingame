import 'dart:io';
import 'dart:math';

String readLineSync() {
  String? s = stdin.readLineSync();
  return s == null ? '' : s;
}

void main() {
    while (true) {
        String enemy1 = readLineSync();
        int dist1 = int.parse(readLineSync());
        String enemy2 = readLineSync();
        int dist2 = int.parse(readLineSync());

        if (dist1 < dist2) {
            print(enemy1);
        } else {
            print(enemy2);
        }
    }
}
