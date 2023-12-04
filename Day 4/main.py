f = open("input.txt", "r")
listInput = f.readlines()
nbCarte = 6
dicoCount = {n:1 for n in range(1,nbCarte+1)}
dicoPresence = dict()
def nbCartesWin(row):
    pts = 0
    guess = row.split(':')[1].split('|')[0].strip().split(' ')
    answers = row.split('|')[1].strip().replace('  ',' ').split(' ')

    matches = set(guess) & set(answers)
    
    return len(matches)


def calculNumber(index):
    val = dicoPresence[index]
    if len(val) == 0:
        return   
    for i in val:
        dicoCount[i] += 1
        calculNumber(i)


for row in listInput:
    print(row)
    index = int(row.split(':')[0].split("Card ")[1].strip())
    nbwin = nbCartesWin(row)
    listNumber = list()
    for i in range(index+1, index+nbwin+1):
        listNumber.append(i)
    dicoPresence[index] = listNumber
    
totalScore = 0
for index, value in dicoPresence.items():
    print(index,': ',value)
    

print(dicoCount)
for i in range(1, nbCarte+1):
    calculNumber(i)

print(dicoCount)

for i in dicoCount.values():
    totalScore+=i

print("total: ",totalScore)

