def replace(old, new, str):
    while old in str:
        str = str.replace(old, new)
    return str

intext = input()

intext = replace(" ,", ", ", intext)
intext = replace(" .", ". ", intext)

intext = replace("..", ".", intext)
intext = replace(",,", ",", intext)

intext = intext.replace(",", ", ")
intext = intext.replace(".", ". ")

intext = intext.strip()

intext = replace("  ", " ", intext)

intext = intext.lower()

intext = intext[0].upper() + intext[1:]

pos = 0
found = True
while found:
    beginSent = intext.find(". ", pos)
    if beginSent == -1:
        found = False
        continue
    pos = beginSent + 2
    if pos < len(intext):
        intext = intext[0:pos] + intext[pos].upper() + intext[pos+1:]


print(intext)