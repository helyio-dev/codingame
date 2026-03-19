def number_to_column(value):
    if value==0:print("A");quit()

    column_name = ""

    while value > 0:
        value -= 1
        rem = value % 26
        column_name += chr(ord("A") + rem)
        value //= 26
    return column_name


def column_to_number(column):
    total = 0
    for i,j in enumerate(column):
        total += (ord(j)-ord("A")+1) * (26 ** i)
    return total

conversions = []
n = int(input())
for label in input().split():
    conversion = None
    if label.isnumeric():
        conversion = number_to_column(int(label))[::-1]
    else:
        conversion = column_to_number(label[::-1])
    
    conversions.append(conversion)

print(*conversions)