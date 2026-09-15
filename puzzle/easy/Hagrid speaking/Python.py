import re

def apply_case(original, replacement):
    result = []
    n = len(original)
    last_upper = original[-1].isupper()
    for i, ch in enumerate(replacement):
        if i < n:
            upper = original[i].isupper()
        else:
            upper = last_upper
        if ch.isalpha():
            result.append(ch.upper() if upper else ch.lower())
        else:
            result.append(ch)
    return ''.join(result)

def transform_word(word):
    lower = word.lower()
    mapping = {'you': 'yeh', 'to': 'ter', 'and': "an'", 'me': 'meh'}
    if lower in mapping:
        return apply_case(word, mapping[lower])
    if len(word) > 2:
        chars = list(word)
        if chars[-1].lower() in ('f', 't', 'd', 'g'):
            chars[-1] = "'"
        if chars[0].lower() == 'h':
            chars[0] = "'"
        return ''.join(chars)
    return word

WORD_RE = re.compile(r"[A-Za-z]+(?:['\-][A-Za-z]+)*")

def transform_text(text):
    def repl(m):
        w = m.group(0)
        if "'" in w or '-' in w:
            return w
        return transform_word(w)
    return WORD_RE.sub(repl, text)

def contains_hagrid(text):
    tokens = WORD_RE.findall(text)
    return "Hagrid" in tokens

def process_line(line):
    if line.count('"') == 2:
        i1 = line.index('"')
        i2 = line.index('"', i1 + 1)
        before = line[:i1]
        quoted = line[i1 + 1:i2]
        after = line[i2 + 1:]
        outside = before + after
        if contains_hagrid(outside):
            quoted = transform_text(quoted)
        return before + '"' + quoted + '"' + after
    return line

def main():
    n = int(input())
    for _ in range(n):
        line = input()
        print(process_line(line))

if __name__ == "__main__":
    main()