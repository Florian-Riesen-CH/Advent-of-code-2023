
import math

listInput = [[57726992,291117211762026]]
sizeInput = list()
for input in listInput:
    time = input[0]
    record = input[1]
    winner = list()
    for i in range(0, time+1):
        distance = time - i
        distanceParcouru = distance * i
        if distanceParcouru > record:
            winner.append(i)

    sizeInput.append(len(winner))

result = math.prod(sizeInput)
print(result)