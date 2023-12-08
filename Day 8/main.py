import re
import sys
import math

f = open("input.txt", "r")
lines = f.readlines()
orders = [*lines[0][0:len(lines[0])-1]]
datas = lines[2:len(lines)]
steps = 0
sys.setrecursionlimit(10000000)

cleanData = {}

def calculStepValue(steps):
    reste = steps % len(orders)
    return orders[reste]
    
#AAA -> BBB -> AAA -> BBB -> AAA -> BBB -> ZZZ
#     L  ->  L  ->  R  ->  L  ->  L  ->  R
def calculPath(index: str, steps):
    if index[2] == 'Z':
        print('Index ',index,' trouvé en ', steps, ' steps')
        return steps
    #
    #next_order = calculStepValue(steps)
    stepOrder = calculStepValue(steps)
    #print(index, ' -> ', stepOrder, ' Steps:', steps)
    steps += 1
    if stepOrder == 'R':
        return calculPath(cleanData[index][1],steps)
    elif stepOrder == 'L':
        return calculPath(cleanData[index][0],steps)

def getDatasEndByA():
    cleanDataByA = {}
    for data in datas:
        allPath = re.findall('[A-Z0-9]{3}', data)
        if [*allPath[0]][2] == 'A':
            cleanDataByA[allPath[0]] = allPath[1:3]
    return cleanDataByA

for data in datas:
    allPath = re.findall('[A-Z0-9]{3}', data)
    cleanData[allPath[0]] = allPath[1:3]

cleanDataByA = getDatasEndByA()
answer = []
for key in cleanDataByA.keys():
    answer.append(calculPath(key, 0))


ppmc = math.lcm(*answer)
print(ppmc)