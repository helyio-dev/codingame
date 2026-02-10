import 'dart:io';

bool isAnagram(String w1, String w2) {
  String s1 = w1.toLowerCase();
  String s2 = w2.toLowerCase();
  if (s1 == s2) return false;
  
  List<String> chars1 = s1.split('')..sort();
  List<String> chars2 = s2.split('')..sort();
  
  return chars1.join() == chars2.join();
}

void main() {
  String? w = stdin.readLineSync();
  String? s = stdin.readLineSync();

  if (w == null || s == null) return;

  RegExp regExp = RegExp(r'[a-zA-Z]+');
  List<String> words = regExp.allMatches(s).map((m) => m.group(0)!).toList();

  int keyIndex = -1;
  for (int i = 0; i < words.length; i++) {
    if (isAnagram(w, words[i])) {
      keyIndex = i;
      break;
    }
  }

  if (keyIndex == -1) {
    print("IMPOSSIBLE");
  } else {
    List<String> before = words.sublist(0, keyIndex);
    List<String> after = words.sublist(keyIndex + 1);

    int d1 = keyIndex % 10;
    int d2 = after.length % 10;
    int d3 = before.join('').length % 10;
    int d4 = after.join('').length % 10;

    print("$d1.$d2.$d3.$d4");
  }
}