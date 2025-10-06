s = input()

def palindrome(i,j):
    while i >= 0 and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i+1:j]

strs = []
maxVal = 1
for i in range(len(s)):
    odd = palindrome(i,i)
    even = palindrome(i,i+1)
    odd_length = len(odd)
    even_length = len(even)

    if even_length > maxVal  or maxVal < odd_length:
        strs = []
    maxVal = max(maxVal , odd_length ,even_length)

    if maxVal == odd_length:
        strs.append(odd)
    if maxVal==even_length:
        strs.append(even)

for i in strs:
    print(i)