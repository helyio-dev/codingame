import math
wife = input()
husband = input()

width = math.lcm(len(wife),len(husband))

wife = wife * (width//len(wife))
husband = husband * (width//len(husband))

print(wife)
for char1, char2 in zip(husband, wife):
    print(char1 + " "*(width-2) + char2)
print(husband)