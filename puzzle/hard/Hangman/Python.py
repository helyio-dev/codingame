word = input()
chars = input().split(" ")
output = ["_" if char.isalpha() else " " for char in word]

hangman="""+--+   +--+   +--+   +--+   +--+   +--+   +--+ 
|      |  o   |  o   |  o   |  o   |  o   |  o 
|      |      |  |   | /|   | /|\\  | /|\\  | /|\\
|\\     |\\     |\\     |\\     |\\     |\\/    |\\/ \\""".split("\n")

hm = 0
i = 0
while i < len(chars) and hm < 7:
    if chars[i] not in word or chars[i] in output:
        hm+=1
    for idx,char in enumerate(word):
        if char == chars[i] or char.lower() in chars[i]:
            output[idx] = char
    i+=1

for row in hangman:
    print(row[(7*hm) : 7*hm+5].strip())
print(*output,sep="")