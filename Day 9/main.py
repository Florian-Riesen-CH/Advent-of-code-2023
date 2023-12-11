f = open('inputFinal.txt', 'r')
lines = f.readlines()

def defineEquart(numeros, listIteration):
    nextRange = list()
    for i in range(1, len(numeros)):
        nextRange.append(int(numeros[i])-int(numeros[i-1]))
    listIteration.append(nextRange)
    if max(nextRange) == 0 and min(nextRange) == 0:
        return
    else :
        defineEquart(nextRange, listIteration)
allIteration = list()        
for line in lines:
    numeros = line.replace('\n', '').split(' ')
    numeros = [int(x) for x in numeros]
    listIteration = list()
    listIteration.append(numeros)
    defineEquart(numeros, listIteration)
    allIteration.append(listIteration)
    

for iteration in allIteration:
    iteration.reverse()
    sum = 0
    for line in iteration:
        lastValue = line[0]
        sum = lastValue - sum
        line.insert(0,sum)


total = 0
for iteration in allIteration:
    iteration.reverse()
    calcul = iteration[0][0]
    total += calcul
    
print(total)