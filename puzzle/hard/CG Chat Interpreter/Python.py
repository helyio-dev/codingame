import sys, re
from collections import defaultdict

ASSIGN_KW = {"youre", "your", "ur"}
OUTPUT_KW = {"tell", "telling"}

def get_top(stacks, nick):
    st = stacks[nick]
    return st[-1] if st else 0

def parse_primary(tokens, i, speaker, context, stacks, good_nouns, bad_nouns):
    if i >= len(tokens):
        return None
    typ, w = tokens[i]
    if typ == "M":
        return (get_top(stacks, w), i + 1)
    if w == "me":
        return (get_top(stacks, speaker), i + 1)
    if w in ("you", "u"):
        ctx = context.get(speaker)
        return (get_top(stacks, ctx) if ctx else 0, i + 1)
    if w in ("a", "an"):
        j = i + 1
        mult = 1
        while j < len(tokens) and tokens[j][0] == "W" and tokens[j][1] not in good_nouns and tokens[j][1] not in bad_nouns:
            mult *= 2
            j += 1
        if j < len(tokens) and tokens[j][0] == "W" and (tokens[j][1] in good_nouns or tokens[j][1] in bad_nouns):
            sign = 1 if tokens[j][1] in good_nouns else -1
            return (mult * sign, j + 1)
        return None
    return None

def parse_constant(tokens, i, speaker, context, stacks, good_nouns, bad_nouns):
    res = parse_primary(tokens, i, speaker, context, stacks, good_nouns, bad_nouns)
    if res is None:
        return None
    val, j = res
    while True:
        if j < len(tokens) and tokens[j] == ("W", "squared"):
            val = val * val
            j += 1
            continue
        if j < len(tokens) and tokens[j] == ("W", "and"):
            res2 = parse_constant(tokens, j + 1, speaker, context, stacks, good_nouns, bad_nouns)
            if res2 is not None:
                v2, j2 = res2
                if j2 < len(tokens) and tokens[j2] == ("W", "too"):
                    val = val + v2
                    j = j2 + 1
                    continue
        if j + 1 < len(tokens) and tokens[j] == ("W", "but") and tokens[j + 1] == ("W", "not"):
            res2 = parse_constant(tokens, j + 2, speaker, context, stacks, good_nouns, bad_nouns)
            if res2 is not None:
                v2, j2 = res2
                if j2 < len(tokens) and tokens[j2] == ("W", "though"):
                    val = val - v2
                    j = j2 + 1
                    continue
        if j < len(tokens) and tokens[j] == ("W", "by"):
            res2 = parse_constant(tokens, j + 1, speaker, context, stacks, good_nouns, bad_nouns)
            if res2 is not None:
                v2, j2 = res2
                if j2 < len(tokens) and tokens[j2] == ("W", "multiplied"):
                    val = val * v2
                    j = j2 + 1
                    continue
        break
    return val, j

def tokenize(rest):
    tokens = []
    for t in rest.split():
        if len(t) >= 3 and t[0] == "*" and t[-1] == "*" and t.count("*") == 2:
            inner = t[1:-1]
            if inner:
                tokens.append(("M", inner))
                continue
        ct = t.strip("*")
        if ct:
            tokens.append(("W", ct))
    return tokens

def process_line(line, context, stacks, good_nouns, bad_nouns, output):
    cleaned = re.sub(r"[^A-Za-z0-9\s<>*]", "", line).lower()
    m = re.match(r"^\s*<([a-z0-9]+)>\s*(.*)$", cleaned)
    if not m:
        return
    speaker = m.group(1)
    rest = m.group(2)
    tokens = tokenize(rest)
    start = 0
    if tokens and tokens[0][0] == "M":
        context[speaker] = tokens[0][1]
        start = 1
    cmd = None
    cmd_idx = None
    i = start
    while i < len(tokens):
        typ, w = tokens[i]
        if typ == "W":
            if w in ASSIGN_KW or w in OUTPUT_KW or w in ("listen", "forget", "flip"):
                cmd = w
                cmd_idx = i
                break
        i += 1
    consumed = None
    if cmd is not None and context.get(speaker) is not None:
        ctx = context[speaker]
        if cmd in ASSIGN_KW:
            k = cmd_idx + 1
            found = None
            while k < len(tokens):
                res = parse_constant(tokens, k, speaker, context, stacks, good_nouns, bad_nouns)
                if res is not None:
                    found = (k, res[0], res[1])
                    break
                k += 1
            if found is not None:
                cstart, val, cend = found
                stacks[ctx].append(val)
                consumed = (cstart, cend)
        elif cmd in OUTPUT_KW:
            st = stacks[ctx]
            if st:
                output.append(str(st.pop()))
            else:
                output.append("0")
        elif cmd == "listen":
            st = stacks[ctx]
            if st:
                st.append(st[-1])
        elif cmd == "forget":
            st = stacks[ctx]
            if st:
                st.pop()
        elif cmd == "flip":
            st = stacks[ctx]
            if len(st) >= 2:
                st[-1], st[-2] = st[-2], st[-1]
    for idx in range(len(tokens)):
        if idx == 0 and start == 1:
            continue
        if consumed is not None and consumed[0] <= idx < consumed[1]:
            continue
        typ, w = tokens[idx]
        if typ == "M":
            context[speaker] = w

def main():
    data = sys.stdin.read().split("\n")
    idx = 0
    numGood, numBad = map(int, data[idx].split())
    idx += 1
    good_line = data[idx] if idx < len(data) else ""
    idx += 1
    bad_line = data[idx] if idx < len(data) else ""
    idx += 1
    numLines = int(data[idx])
    idx += 1
    lines = data[idx: idx + numLines]

    def normw(s):
        return re.sub(r"[^a-z0-9]", "", s.lower())

    good_nouns = set(normw(w) for w in good_line.split())
    bad_nouns = set(normw(w) for w in bad_line.split())

    context = {}
    stacks = defaultdict(list)
    output = []

    for line in lines:
        process_line(line, context, stacks, good_nouns, bad_nouns, output)

    print("".join(output))

if __name__ == "__main__":
    main()