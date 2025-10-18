possible_answers_list = []

for i in range(0,9999):
    possible_answers_list.append("%04d" % i)

def is_rule_applicable(source, guess, bulls, cows):
    true_bulls = 0
    true_cows = 0
    source_bulls = list(source)
    guess_bulls = list(guess)
    source_cows = list(source)
    guess_cows = list(guess)
    for index, char in enumerate(source_bulls):
        if char == guess_bulls[index]:
            true_bulls += 1
            source_cows.pop(index - true_bulls + 1)
            guess_cows.pop(index - true_bulls + 1)
    if true_bulls != bulls:
        return False

    for char in source_cows:
        if char in guess_cows:
            true_cows += 1

    if true_cows != cows:
        return False

    return True

n = int(input())
for i in range(n):
    guess, bulls, cows = input().split()
    bulls = int(bulls)
    cows = int(cows)

    possible_answers_list = [x for x in possible_answers_list if is_rule_applicable(x, guess, bulls, cows)]


print(possible_answers_list[0])