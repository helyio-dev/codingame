import sys
import re

def solve():
    word_to_match = sys.stdin.readline().strip().lower()
    sentence = sys.stdin.readline().strip()

    def is_anagram(w1, w2):
        w1, w2 = w1.lower(), w2.lower()
        if w1 == w2:
            return False
        return sorted(w1) == sorted(w2)

    words_data = []
    for match in re.finditer(r'[a-zA-Z]+', sentence):
        words_data.append({
            'word': match.group(),
            'start': match.start(),
            'end': match.end()
        })

    key_index = -1
    for i, data in enumerate(words_data):
        if is_anagram(word_to_match, data['word']):
            key_index = i
            break

    if key_index == -1:
        print("IMPOSSIBLE")
        return

    key_data = words_data[key_index]

    d1 = key_index % 10

    d2 = (len(words_data) - 1 - key_index) % 10

    letters_before = sum(len(w['word']) for w in words_data[:key_index])
    d3 = letters_before % 10

    letters_after = sum(len(w['word']) for w in words_data[key_index+1:])
    d4 = letters_after % 10

    print(f"{d1}.{d2}.{d3}.{d4}")

solve()