import sys
import time
sys.setrecursionlimit(10000)
lines = open('input.txt','r').readlines()
allowBot = ['|','L', 'J']
allowTop = ['|','7', 'F']
allowRight = ['-','J', '7']
allowleft = ['-','L', 'F']

maxheigh = len(lines)
maxline = len(lines[0])


def find_s_position():
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if lines[x][y] == 'S':
                return (x,y)

def calcul_next_step(x,y,locationFrom):
    actualValue = lines[x][y]
    #allPath.append((x,y))
    
    if locationFrom == 'bot':
        if actualValue == '|':
            return(x-1,y,'bot',)
        elif actualValue == 'F':
            return(x,y+1,'left')
        elif actualValue == '7':
            return(x,y-1,'right')
    
    if locationFrom == 'top':
        if actualValue == '|':
            return(x+1,y,'top')
        elif actualValue == 'L':
            return(x,y+1,'left')
        elif actualValue == 'J':
            return(x,y-1,'right')
        
     
    if locationFrom == 'right':
        if actualValue == '-':
            return(x,y-1,'right')
        elif actualValue == 'L':
            return(x-1,y,'bot')
        elif actualValue == 'F':
            return(x+1,y,'top')
            
    if locationFrom == 'left':
        if actualValue == '-':
            return(x,y+1,'left')
        elif actualValue == 'J':
            return(x-1,y,'bot')
        elif actualValue == '7':
            return(x+1,y,'top')        
    
def displayPath(lines,allPath, isolatedPos):
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if (x,y) in allPath:
                print("\033[34m.\033[0m", end='')
            else:
                if(x,y) in isolatedPos:
                    print("\033[33m.\033[0m", end='')
                else:    
                    print("\033[31m.\033[0m", end='')
        print()

def checkIfSurrond(x,y,allPath):
    Flagbot = False
    custo_x = x
    while custo_x < maxheigh:
        custo_x += 1
        if (custo_x,y) in allPath:
            Flagbot = True
            break
    if Flagbot == False:
        return False    
    
    
    Flagtop = False
    custo_x = x
    while custo_x > 0:
        custo_x -= 1
        if (custo_x,y) in allPath:
            Flagtop = True
            break
    if Flagtop == False:
        return False    
        
    Flagright = False
    custo_y = y
    while custo_y < maxline:
        custo_y += 1
        if (x,custo_y) in allPath:
            Flagright = True
            break
    if Flagright == False:
        return False    
    
    flagLeft = False
    custo_y = y
    while custo_y > 0:
        custo_y -= 1
        if (x,custo_y) in allPath:
            flagLeft = True
            break
    if flagLeft == False:
        return False    
    
    if Flagbot and Flagtop and Flagright and flagLeft:
        return True
    else:
        return False
    
allPossibiliy =[]    
allPath =[]
notInPath = []
isolatedPos = []
signe = ''

for x in range(len(lines)):
    for y in range(len(lines[x])):
        allPossibiliy.append((x,y))

#displayPath(lines, allPath, isolatedPos)

(x,y) = find_s_position()
print('x: ', x, ' y: ',y)
allPath.append((x,y))
allPath.append((x-1,y))
(x,y,locationFrom)=calcul_next_step(x-1, y,'bot') 
allPath.append((x,y))


while signe != 'S':
    (x,y,locationFrom)=calcul_next_step(x, y,locationFrom)
    signe = lines[x][y]
    allPath.append((x,y))


#displayPath(lines, allPath, isolatedPos)


notInPath = set(allPossibiliy) - set(allPath)

count=0
for i in notInPath:
    if checkIfSurrond(i[0],i[1],allPath):
        isolatedPos.append((i[0],i[1]))
        count += 1

displayPath(lines, allPath, isolatedPos)
        
print(count)


