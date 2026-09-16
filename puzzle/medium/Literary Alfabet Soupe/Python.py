languages = [
    "Danish",
    "English",
    "Estonian",
    "Finnish",
    "French",
    "German",
    "Irish",
    "Italian",
    "Portuguese",
    "Spanish",
    "Swedish",
    "Turkish",
    "Welsh"
]

exclusions = {
    "Danish": "qz",
    "English": "",
    "Estonian": "cfqwxy",
    "Finnish": "bfqwx",
    "French": "",
    "German": "",
    "Irish": "jkqvwxyz",
    "Italian": "jkwxy",
    "Portuguese": "kw",
    "Spanish": "kw",
    "Swedish": "qw",
    "Turkish": "qwx",
    "Welsh": "jkqvxz"
}

inclusions = {
    "Danish": "æåø",
    "English": "",
    "Estonian": "šžõäöü",
    "Finnish": "äö",
    "French": "çœëïüàèùâêîôûé",
    "German": "ßäöü",
    "Irish": "áéíóú",
    "Italian": "àèìòùé",
    "Portuguese": "çãõàâêôáéíóú",
    "Spanish": "ñüáéíóú",
    "Swedish": "åäö",
    "Turkish": "ğçşİıöü",
    "Welsh": "ŵŷâêîôû"
}

texts = [input().lower() for _ in range(13)]

def compatible(text, language):
    exc = set(exclusions[language])
    inc = set(inclusions[language])

    for c in text:
        if c.isalpha():
            if c in exc:
                return False
            if c not in "abcdefghijklmnopqrstuvwxyz" and c not in inc:
                return False
    return True

possible = [
    [language for language in languages if compatible(text, language)]
    for text in texts
]

def solve(i, used, result):
    if i == 13:
        return result

    choices = [
        language for language in possible[i]
        if language not in used
    ]

    if not choices:
        return None

    choices.sort(key=lambda language: sum(
        language in possible[j]
        for j in range(i + 1, 13)
    ))

    for language in choices:
        new_result = result + [language]
        answer = solve(i + 1, used | {language}, new_result)
        if answer is not None:
            return answer

    return None

answer = solve(0, set(), [])

for language in answer:
    print(language)