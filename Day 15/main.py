array = open("input.txt", 'r').read().split(',')
dico = {i: {} for i in range(256)}


def calcul_hash(str):
    value = 0
    for letter in str:
        value += ord(letter)
        value *= 17
        value = value % 256
    return value


for stentence in array:
    if '=' in stentence:
        label = stentence.split('=')[0]
        box = calcul_hash(label)
        focal = int(stentence.split('=')[1])
        if box in dico.keys():
            dico[box][label] = focal
        else :
            dico[box] = {label:focal}
    elif '-' in stentence:
        label = stentence.split('-')[0]
        box = calcul_hash(label)
        if label in dico[box].keys():
            del dico[box][label]
    
print(dico)

somme = 0
for (box, labels) in dico.items():
    emplacement = 1
    for (label, focal) in labels.items():
        somme += (1 + box) * emplacement * focal
        emplacement += 1
print(somme)