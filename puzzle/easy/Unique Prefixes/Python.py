n = int(input())
words = [input().strip() for _ in range(n)]
unique_words = list(dict.fromkeys(words))
prefixes = {}

for w in unique_words:
    for i in range(1, len(w) + 1):
        pref = w[:i]
        if all((other == w) or not other.startswith(pref) for other in unique_words):
            prefixes[w] = pref
            break
    if w not in prefixes:
        prefixes[w] = w

for w in words:
    print(prefixes[w])
