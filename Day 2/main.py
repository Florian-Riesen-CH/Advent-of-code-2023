import re

f = open("input.txt", "r")
max_red = 12
max_green = 13
max_blue = 14
total = 0
for x in f:
    cpt_blue = 0
    cpt_red = 0
    cpt_green = 0
    tirages = x.split(':')[1]
    tirageSplit = tirages.split(';')
    tirageNo = int(x.split(':')[0].replace('Game ',''))
    print(tirageNo)
    isok = True
    for tirage in tirageSplit:
        for i in tirage.split(','):
            value = int(re.search(r'\d+', i).group())
            if 'green' in i:
                if value > cpt_green:
                    cpt_green = value
            if 'blue' in i:
                if value > cpt_blue:
                    cpt_blue = value
            if 'red' in i:
                if value > cpt_red:
                    cpt_red = value
    
    print(' red:', cpt_red, ' green:',cpt_green, ' blue:', cpt_blue)
    total += cpt_red*cpt_green*cpt_blue
     
        
print(total)  
        
        