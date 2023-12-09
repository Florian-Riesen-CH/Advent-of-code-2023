import re

f = open("input.txt", "r")
maxRow = 139
maxLine = 139
lignes = f.readlines()
f.close
f = open("input.txt", "r")
somme = 0
keyValue = dict()

for indexLine, line in enumerate(f):
    number=''
    for indexChar, char in enumerate(line):
        if (char.isdigit()):
            number += char
        if (not char.isdigit()) and number != '':
            xStart = indexLine
            xEnd = indexLine
            yStart = indexChar-len(number)
            yEnd = indexChar-1
            
            xStartRange = xStart -1
            yStartRange = yStart - 1
            xEndRange = xEnd + 1
            yEndRange = yEnd + 1
            
            if xStartRange < 0:
                xStartRange = 0
            if yStartRange < 0:
                yStartRange = 0
            if xEndRange > maxRow:
                xEndRange = maxRow
            if yEnd > maxLine:
                yEnd = maxLine
            
            
            fianal = number
            number = ''
            
            positionStar = []
            for x in range(xStartRange, xEndRange+1):
                for y in range(yStartRange, yEndRange+1):
                    char = lignes[x][y]
                    if char == '*':
                        location = ''+str(x)+':'+str(y)
                        for key, val in keyValue.items():
                            if location in val:
                                print(fianal, ' * ', key, ' = ',int(fianal) * int(key))
                                total = int(fianal) * int(key)
                                somme += total
                        positionStar.append(location)
                        
            if fianal in keyValue:
                for pos in positionStar:
                    keyValue.get(fianal).append(pos)
            else:
                keyValue[fianal]  =  positionStar     

print(keyValue['106'])
print(keyValue['133'])
print(somme)