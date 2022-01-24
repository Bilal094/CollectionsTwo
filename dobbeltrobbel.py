import random, time
from random import choice
from time import sleep
# Assignments
BlauwDobbelsteen = [1, 2, 3, 4, 5, 6]
RoodDobbelsteen = [1, 2, 3, 4, 5, 6]
WitDobbelsteen = [1, 1, 1, 2, 2, 3]
RoodMin2 = -2
BlauwMin2 = -2
RoodScoreBladList = [RoodMin2, " ", " ", " ", " ", " ", " ", " ", " ", " "]
BlauwScoreBladList = [" ", " ", " ", " ", " ", " ", " ", " ", " ", BlauwMin2]
WitScoreBladList = [" ", " ", " ", " ", " "]
ScoreBladPositieListRood = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
ScoreBladPositieListBlauw = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
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

    
def error():
    print('Type a.u.b een gegeven keuze')

def positieError():
    print('Jouw getal is groter dan de getallen ernaast! Je moet het op volgorde invullen.')

def waardenIdentiek(keuze):
        print(f'Je hebt gekozen voor het getal {keuze}')
        sleep(1)
        print('De gerolde waarden van de rode en de blauwe dobbelsteen zijn gelijk aan elkaar')
        sleep(1)
        print('Je mag kiezen in welk scoreblad je jouw getal wilt invullen')

def berekeningAenB():
    if maximumEnMinimum[0] < maximumEnMinimum[1]:
        print(f'De rode dobbelsteen ({RoodNummer}) heeft het laagst gerolde waarde, dus vul je getal in de rode scoreblad!')
    elif maximumEnMinimum[1] < maximumEnMinimum[0]:
        print(f'De blauwe dobbelsteen ({BlauwNummer}) heeft het laagst gerolde waarde, dus vul je getal in de blauwe scoreblad!')
    else:
        error()

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
    print('Rood =  '+ ScoreRood)
    print('Positie =    '+ ScorePositieRood)
    print('Blauw =   '+ ScoreBlauw)
    print('Positie = '+ ScorePositieBlauw)
    print('Wit = ' + ScoreWit)

def positieKeuze(keuze):
    global ScoreKeuze
    print(f'Je hebt gekozen voor het getal {keuze}')
    sleep(1)
    maximumEnMinimum.pop(2)
    berekeningAenB()
    sleep(1.5)
    scoreBlad()
    HerhalenScore = True
    if maximumEnMinimum[0] > maximumEnMinimum[1]:
        print()
        ScoreKeuzeBlauw = input('Type het nummer waar jij je getal in wilt vullen (Blauw) ')
        if ScoreKeuzeBlauw in ScoreBladPositieListBlauw:
            while HerhalenScore:

                if ScoreKeuzeBlauw == "1":
                    HerhalenScore = False
                    HerhalenScoreBlad = True
                    while HerhalenScoreBlad:
                        if berekeningKeuze == "A" and TotaalA > ScoreBladBlauwCheck[2]:
                            BlauwScoreBladList[0] = TotaalA
                            break
                        elif berekeningKeuze == "B" and TotaalB > ScoreBladBlauwCheck[2]:
                            BlauwScoreBladList[0] = TotaalB
                            break
                        else:
                           positieError()
                           HerhalenScoreBlad = True
                           

                else:
                    error()
                    HerhalenScore = True


    elif maximumEnMinimum[0] < maximumEnMinimum[1]:
        print()
        ScoreKeuzeRood = input('Type het nummer waar jij je getal in wilt vullen (Rood) ')
        if ScoreKeuzeRood in ScoreBladPositieListRood:
            while HerhalenScore:

                if ScoreKeuzeRood == "1":
                    HerhalenScore = False
                    HerhalenScoreBlad = True
                    while HerhalenScoreBlad:
                        if berekeningKeuze == "A" and TotaalA > ScoreBladRoodCheck[2]:
                            RoodScoreBladList[0] = TotaalA
                            break
                        elif berekeningKeuze == "B" and TotaalB > ScoreBladRoodCheck[2]:
                            RoodScoreBladList[0] = TotaalB
                            break
                        else:
                           positieError()
                           HerhalenScoreBlad = True
        return BlauwScoreBladList, RoodScoreBladList


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

    if maximumEnMinimum[0] == maximumEnMinimum[1]:
        waardenIdentiek(TotaalA)
        scoreBlad()
        ScoreKeuzeIdentiek = input('Type het nummer waar jij je getal in wilt vullen ')
    else:
        if maximumEnMinimum[0] > maximumEnMinimum[1]:
            positieKeuze(TotaalA)
        elif maximumEnMinimum[1] > maximumEnMinimum[0]:
            positieKeuze(TotaalA)
            
elif berekeningKeuze == 'B':
    
    if maximumEnMinimum[0] == maximumEnMinimum[1]:
        waardenIdentiek(TotaalB)
        scoreBlad()
        ScoreKeuzeIdentiek = input('Type het nummer waar jij je getal in wilt vullen ')
    else:
        if maximumEnMinimum[0] > maximumEnMinimum[1]:
            positieKeuze(TotaalB)
        elif maximumEnMinimum[1] > maximumEnMinimum[0]:
            positieKeuze(TotaalB)
else:
    error()
scoreBlad()
