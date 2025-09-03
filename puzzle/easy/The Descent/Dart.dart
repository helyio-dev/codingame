import 'dart:io';
import 'dart:math';

String readLineSync() {
  String? s = stdin.readLineSync();
  return s == null ? '' : s;
}

void main() {
    while (true) {
        int maxH = -1;
        int mountainToFire = 0;

        for (int i = 0; i < 8; i++) {
            int mountainH = int.parse(readLineSync());
            if (mountainH > maxH) {
                maxH = mountainH;
                mountainToFire = i;
            }
        }
        print(mountainToFire);
    }
}
