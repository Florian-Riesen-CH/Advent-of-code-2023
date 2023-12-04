import re

def extract_numbers(text):
    number_words = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    numbers = []
    n = len(text)
    i = 0

    while i < n:
        if text[i].isdigit():
            numbers.append(int(text[i]))
            i += 1
        else:
            found = False
            for j in range(i + 1, n + 1):
                word = text[i:j]
                if word in number_words:
                    numbers.append(number_words[word])
                    found = True
            if found:
                i += 1  # Avancer d'un caractère si un mot numérique est trouvé
            else:
                i += 1  # Avancer d'un caractère si aucun mot numérique n'est trouvé

    return numbers


f = open("input.txt", "r")
somme = 0
for x in f:
    newVal = extract_numbers(x)
    print(x,' - ', newVal[0], newVal[-1], ' sum: ', str(newVal[0])+ str(newVal[-1]))
    somme += int( str(newVal[0])+ str(newVal[-1]))

print('---------------------')
print(somme)

