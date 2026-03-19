clues = []
sizes = []
n = int(input())
for i in range(n):
    clue = input()
    clues.append(clue)
    if len(clue) not in sizes:
        sizes.append(len(clue))

grid = []
s = ""
h, w = [int(i) for i in input().split()]
for i in range(h):
    line = input()
    s+=line
    grid.append(list(line))

for i in range(len(s)):
    for size in sizes:
        new_i = i//w
        new_j = i%w
        if s[i:i+size] in clues or s[i:i+size][::-1] in clues:
            word = s[i:i+size]
            reversed_word = s[i:i+size][::-1]
            grid[new_i][i%w:i%w+size] = " "*len(word)
        
        if s[i:i+(w*size):w] in clues or s[i:i+(w*size):w][::-1] in clues:
            for char in s[i:i+(w*size):w]:
                grid[new_i%w][new_j] = " "
                new_i += 1
        
        if s[i:i+(w*size):w+1] in clues or s[i:i+(w*size):w+1][::-1] in clues:
            for char in s[i:i+(w*size):w+1]:
                grid[new_i%w][new_j%w] = " "
                new_i += 1
                new_j += 1
        
        if s[i:i+((w-1)*size):w-1] in clues or s[i:i+((w-1)*size):w-1][::-1] in clues:
            for char in s[i:i+((w-1)*size):w-1]:
                grid[new_i%w][new_j%w] = " "
                new_i += 1
                new_j -= 1

print("".join([char for char in "".join(["".join(row) for row in grid]) if char != " "]))