import random, time
from random import choice
from time import sleep
# Assignments ---

BlauwDobbelsteen = [1, 2, 3, 4, 5, 6]
RoodDobbelsteen = [1, 2, 3, 4, 5, 6]
WitDobbelsteen = [1, 1, 1, 2, 2, 3]
RoodMin2 = -2
BlauwMin2 = -2
RoodScoreBladList = [RoodMin2, " ", " ", " ", " ", " ", " ", " ", " ", " "]
BlauwScoreBladList = [" ", " ", " ", " ", " ", " ", " ", " ", " ", BlauwMin2]
WitScoreBladList = [" ", " ", " ", " ", " "]
ScoreBladPositieListRood = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
ScoreBladPositieListBlauw = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
ScoreBladRoodCheck = [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ScoreBladBlauwCheck = [0, 0, 0, 0, 0, 0, 0, 0, 0, -2]
maximumEnMinimum = []
ScoreRood = ''
ScoreBlauw = ''
ScoreWit = ''
ScorePositieBlauw = ''
ScorePositieRood = ''

for x in RoodScoreBladList:
    ScoreRood += '['+str(x)+'] ' 
for y in BlauwScoreBladList:
    ScoreBlauw += '['+str(y)+'] '
for z in WitScoreBladList:
    ScoreWit += '['+str(z)+'] '
for a in ScoreBladPositieListBlauw:
    ScorePositieBlauw += ' '+str(a)+'  '
for a in ScoreBladPositieListRood:
    ScorePositieRood += ' '+str(a)+'  '

# User Defined Functions ---
def error():
    print('Type a.u.b een gegeven keuze')

def positionError():
    print('Jouw getal is kleiner dan de getallen ernaast/groter dan de getallen ervoor! Je moet het op volgorde invullen.')

def scoreBlad():
    print('------------------------ Score blad ------------------------')
    print('Rood =  '+ ScoreRood)
    print('Positie =    '+ ScorePositieRood)
    print('Blauw =   '+ ScoreBlauw)
    print('Positie = '+ ScorePositieBlauw)
    print('Wit = ' + ScoreWit)

def valueIdentical():
        print('De rode en blauwe dobbelsteen hebben dezelfde waarden')
        sleep(1)
        scoreBlad()
        positionQuestionIdentical = input('In welk scoreblad wil jij jouw getal invullen? A) blauw, B) rood ').upper()

def determineScoreList(rollednumber, dice, color):
    print(f'Je hebt gekozen voor {rollednumber}')
    sleep(1)
    print(f'De {color} dobbelsteen heeft het laagst gerolde waarde ({dice})')
    sleep(1)
    print(f'Kies de positie in de {color} scoreblad waar jij je nummer in wilt vullen.')

def numberCompare(choice):
        if maximumEnMinimum[0] < maximumEnMinimum[1]:
            determineScoreList(choice, RoodNummer, 'rode')
        elif maximumEnMinimum[0] > maximumEnMinimum[1]:
            determineScoreList(choice, BlauwNummer, 'blauwe')

def checkPosition(rollednumber, scorelist, scoreposition):

    if scorelist[scoreposition] == " ":
        index = scoreposition
        while True:
            index += 1
            if list[index] != " ":
                if rollednumber >= scorelist[index]:
                    index = scoreposition
                    while True:
                        index -= 1
                        if list[index] != " ":
                            if rollednumber <= scorelist[index]:
                                return True
                            else:
                                return False
                else:
                    return False
    else:
        return False
        
# Code start ---
DobbelHerhalen = True
while DobbelHerhalen:
    Dobbel = input(f'Type \'1\' om te dobbelen met de 3 dobbelstenen ')
    if Dobbel == '1':
        RoodNummer = choice(RoodDobbelsteen)
        BlauwNummer = choice(BlauwDobbelsteen)
        WitNummer = choice(WitDobbelsteen)
        print(f'Rode dobbelsteen resultaat: {RoodNummer}')
        print(f'Blauwe dobbelsteen resultaat: {BlauwNummer}')
        print(f'Witte dobbelsteen resultaat: {WitNummer}')
        DobbelHerhalen = False
    else:
        error()
        DobbelHerhalen = True
print()

sleep(2)
TotaalA = BlauwNummer + RoodNummer + WitNummer
TotaalB = BlauwNummer + RoodNummer - WitNummer
TotaalC = BlauwNummer + RoodNummer
maximumEnMinimum.append(RoodNummer)
maximumEnMinimum.append(BlauwNummer)
maximumEnMinimum.append(WitNummer)
maxValue = max(maximumEnMinimum)
minValue = min(maximumEnMinimum)
TotaalD = maxValue - minValue
print('Welk getal wil je in de scoreblad zetten? ')
print(f'A) Blauw + rood + wit = {BlauwNummer} + {RoodNummer} + {WitNummer} = {TotaalA}')
print(f'B) Blauw + rood - wit = {BlauwNummer} + {RoodNummer} - {WitNummer} = {TotaalB}')
print(f'C) Blauw + rood = {BlauwNummer} + {RoodNummer} = {TotaalC}')
print(f'D) Hoogst gerolde dobbelsteen - laagst gerolde dobbelsteen = {maxValue} - {minValue} = {TotaalD}')

berekeningKeuze = input('').upper()
if berekeningKeuze == 'A':
    if maximumEnMinimum[0] == maximumEnMinimum[1]:
        valueIdentical()
    else:
        numberCompare(TotaalA)
        sleep(1)
        scoreBlad()

elif berekeningKeuze == 'B':
    if maximumEnMinimum[0] == maximumEnMinimum[1]:
        valueIdentical()
    else:
        numberCompare(TotaalB)
        sleep(1)
        scoreBlad()

elif berekeningKeuze == 'C':
    if maximumEnMinimum[0] == maximumEnMinimum[1]:
        valueIdentical()
    else:
        numberCompare(TotaalC)
        sleep(1)
        scoreBlad()