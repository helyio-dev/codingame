import sys

def solve():
    n = int(sys.stdin.readline())
    dictionary = [sys.stdin.readline().strip() for _ in range(n)]
    letters = sys.stdin.readline().strip()

    scores = {
        'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1, 't': 1, 'l': 1, 's': 1, 'u': 1,
        'd': 2, 'g': 2,
        'b': 3, 'c': 3, 'm': 3, 'p': 3,
        'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
        'k': 5,
        'j': 8, 'x': 8,
        'q': 10, 'z': 10
    }

    available_counts = {}
    for char in letters:
        available_counts[char] = available_counts.get(char, 0) + 1

    max_score = -1
    best_word = ""

    for word in dictionary:
        word_counts = {}
        is_possible = True
        for char in word:
            word_counts[char] = word_counts.get(char, 0) + 1
        
        for char, count in word_counts.items():
            if available_counts.get(char, 0) < count:
                is_possible = False
                break
        
        if is_possible:
            current_score = 0
            for char in word:
                current_score += scores.get(char, 0)
            
            if current_score > max_score:
                max_score = current_score
                best_word = word

    print(best_word)

solve()
