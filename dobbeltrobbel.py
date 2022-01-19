import random, time
from random import choice
from time import sleep
# Assignments
BlauwDobbelsteen = [1, 2, 3, 4, 5, 6]
RoodDobbelsteen = [1, 2, 3, 4, 5, 6]
WitDobbelsteen = [1, 1, 1, 2, 2, 3]
RoodMin2 = -2
BlauwMin2 = -2
RoodScoreBlad = [RoodMin2, " ", " ", " ", " ", " ", " ", " ", " ", " "]
BlauwScoreBlad = [" ", " ", " ", " ", " ", " ", " ", " ", " ", BlauwMin2]
WitScoreBlad = [" ", " ", " ", " ", " "]
Herhalen = 0
Ronde = 0
maximumEnMinimum = []
ScoreRood = ''
ScoreBlauw = ''
ScoreWit = ''

for x in RoodScoreBlad:
    ScoreRood += '['+str(x)+'] ' 
for y in BlauwScoreBlad:
    ScoreBlauw += '['+str(y)+'] '
for z in WitScoreBlad:
    ScoreWit += '['+str(z)+'] '
    
def error():
    print('Type a.u.b een gegeven keuze')

def dobbelVraag():
    global RoodNummer, BlauwNummer, WitNummer
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

def scoreBlad():
    print('------------------------ Score blad ------------------------')
    print('Rood = '+ ScoreRood)
    print('Blauw = '+ ScoreBlauw)
    print('Wit = ' + ScoreWit)

# Code start ---
dobbelVraag()
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
    maximumEnMinimum.pop(2)
    if 