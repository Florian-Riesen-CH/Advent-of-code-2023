cartes : dict = {'A':12, 'K':11, 'Q':10, 'J':-1, 'T':8, '9':7, '8':6, '7':5, '6':4, '5':3, '4':2, '3':1, '2':0}
ranking = list()
from collections import Counter
import functools

def defineRank(hand: str):
    handClean = hand
    nbJ = hand.count('J')
    hand = hand.replace('J','')
    if hand == '':
        hand = 'AAAAA'
    handCartes = [*hand]
    cardScore = 0
    score = Counter(handCartes)
    scoreSort = sorted(score.items(), key=functools.cmp_to_key(mycmpcard))
    maxval = next(iter(scoreSort))
    handClean = handClean.replace('J', maxval[0])

    print(handClean)
    score = Counter(handClean)
    match(len(score)):
        case 1:
            cardScore = 6
        case 2:
            if 4 in score.values():
                cardScore = 5
            else: 
                cardScore = 4
        case 3:
            if 3 in score.values():
                cardScore = 3
            else: 
                cardScore = 2
        case 4:
            cardScore = 1
        case 5:
            cardScore = 0
    return cardScore

def mycmpcard(a, b): 
    if a[1] > b[1]:
        return - 1
    elif a[1] < b[1]:
        return 1
    else:
        if cartes.get(a[0]) > cartes.get(b[0]):   
            return -1
        elif cartes.get(a[0]) < cartes.get(b[0]):  
            return 1 
        else:
            return 0

def mycmp(a, b): 
    card_a = [*a[0]]
    card_b = [*b[0]]
    score_a = a[2]
    score_b = b[2]

    if score_a > score_b:
        return 1
    elif score_a < score_b:
        return -1
    else:
        for i in range(len(card_a)):
            if cartes.get(card_a[i]) > cartes.get(card_b[i]):   
                return 1
            elif cartes.get(card_a[i]) < cartes.get(card_b[i]):  
                return -1 

def readFile():
    f = open("input.txt", "r")
    listInput = f.readlines()
    for line in listInput:
        carte = list()
        cardValue = line.split(' ')[0]
        if cardValue == 'JJJJJ':
            cardValue = 'AAAAA'
        carte.append(cardValue)
        carte.append(line.split(' ')[1].replace('\n',''))
        carte.append(defineRank(line.split(' ')[0]))
        ranking.append(carte)
    ranking.sort(key=lambda x: x[2])
    ranking.reverse()

def calculScore():
    total = 0
    for i in range(len(ranking)):
        print((i+1), '*', int(ranking[i][1]))
        total += (i+1) * int(ranking[i][1])
    return total

readFile()
ranking = sorted(ranking, key=functools.cmp_to_key(mycmp))
print(calculScore())
