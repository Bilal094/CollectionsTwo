# Import ---
import random, time
from random import choice
from time import sleep
# Assignments ---
game = True
Red2 = -2
Blue2 = -2
redDice = [1, 2, 3, 4, 5, 6]
blueDice = [1, 2, 3, 4, 5, 6]
whiteDice = [1, 1, 1, 2, 2, 3]
redScore = [Red2, '', '', '', '', '', '', '', '', '']
blueScore = ['', '', '', '', '', '', '', '', '', Blue2]
whiteScore = []
highAndLow = []
total1 = []
# Functions ---

def positionError():
    print('De gekozen positie is niet geldig')

def error():
    print('Type a.u.b een gegeven keuze')

def numberComparison(red, blue):
    if red == blue:
        return 'even'
    elif red < blue:
        return 'blue'
    elif red > blue:
        return 'red'

def evenNumbers():
    print('De rode en blauwe dobbelstenen hebben dezelfde waarden')
    sleep(1)
    print('Je mag kiezen in welke van de 2 lijsten je kunt invullen')
    print()
    print(f'A) Rood ({redScore})')
    print(f'B) Blauw ({blueScore})')

def checkPositionRight(number, position, List):
    global isValidR, isValidL
    isValidR = False

    if List == blueScore:
        index = int(position)
        if List[index] == '':
            while index < len(List) - 1:
                index += 1
                if List[index] != '':
                    if number >= List[index]:
                        isValidR = True
                        return isValidR
                    else:
                        return isValidR
                elif List[index] == len(List) - 1:
                    isValidR = True
                    return isValidR
        return isValidR

    if List[int(position)] == '':
        index = int(position)
        if index == 9:
            isValidR = True
            return isValidR
        while index < len(List) - 1:
            index += 1
            if List[index] != '':
                if number <= List[index]:
                    isValidR = True
                break
            elif index == len(List) - 1:
                isValidR = True
    return isValidR

def checkPositionLeft(number, position, List):
    isValidL = False

    if List == blueScore:
        index = int(position)
        if List[index] == '':
            while index < len(List) - 1:
                if index == 0:
                    isValidR = True
                    return isValidR
                index -= 1
                if List[index] != '':
                    if number <= List[index]:
                        isValidL = True
                        return isValidL
                    else:
                        return isValidL
        return isValidL

    if List[int(position)] == '':
        index = int(position)
        while index <= len(List) - 1:
            index -= 1
            if List[index] != '':
                if number >= List[index]:
                    isValidL = True
                break
            elif index == len(List) - 1:
                isValidL = True
    return isValidL

def numberPlacement(total, List):
        positionBool = True
        while positionBool:
            positionChoice = input('Kies waar jij je nummer wilt zetten (0 - 9) of type \'end\' wanneer je jouw nummer nergens in kunt vullen ')
            if positionChoice == 'end':
                break
            pCR = checkPositionRight(total, positionChoice, List)
            pCL = checkPositionLeft(total, positionChoice, List)
            if pCR == True and pCL == True:
                List[int(positionChoice)] = total
                positionBool = False
            elif pCR == False and pCL == True or pCR == True and pCL == False or pCR == False and pCL == False:
                positionError()

def Main(total, option):
    print(f'Je hebt gekozen voor optie {option} ({total})')
    sleep(1)
    nC = numberComparison(redNumber, blueNumber)
    if nC == 'red':
        print('De rode dobbelsteen heeft het hoogst gerold')
        sleep(1)
        print(redScore)
        numberPlacement(total, redScore)

    elif nC == 'blue':
        print('De blauwe dobbelsteen heeft het hoogst gerold')
        sleep(1)
        print(blueScore)
        numberPlacement(total, blueScore)

    elif nC == 'even':
        evenNumbers()
        scoreChoice = input('').upper()
        if scoreChoice == 'A':
            print(redScore)
            numberPlacement(total, redScore)
        elif scoreChoice == 'B':
            print(blueScore)
            numberPlacement(total, blueScore)

def pointCalculate(List1, List2, List3):
    print()
    print('De witte lijst is gevuld/je hebt er voor gekozen om te stoppen')
    sleep(1)
    emptySpot = 0
    for i in List1:
        if i == '':
            emptySpot += 1
    for i in List2:
        if i == '':
            emptySpot += 1

    # Subtotal 1
    List1 = [x if x != '' else 0 for x in List1]
    List2 = [x if x != '' else 0 for x in List2]
    for x in range(10):
        y = List1[x] * List2[x]
        total1.append(y)
    Sum = sum(total1)

    # Subtotal 2
    sumWhite = sum(whiteScore)
    total2 = sumWhite * emptySpot

    total3 = Sum - total2

    print(f'Jouw eindscore is {total3}')
# Code start ---
print('Dobbeltrobbel werkt alsvolgt:')
sleep(1)
print('Je typt op \'1\' om te dobbelen')
sleep(1)
print('Het hoogst gerolde waarde van de rode/blauwe dobbelsteen bepaalt in welk scoreblad jij jouw nummer in moet vullen')
sleep(1.5)
print('Bijvoorbeeld, als de rode dobbelsteen het hoogst heeft gerold, moet je in de rode scoreblad gaan vullen')
sleep(1.5)
print('Wanneer de rode en blauwe dobbelsteen hetzefde hebben gerold, dan mag jij kiezen in welk scoreblad jij jouw nummer invult')
sleep(1.5)
print('De index van de rode en blauwe scoreblad begint bij 0. Bij de blauwe scoreblad is het index hetzelfde maar omgekeerd')
sleep(1.5)
print('Stel dat jij de nummer 2 naast -2 wilt zetten (in de blauwe scoreblad!), dan moet je kiezen voor positie 8, niet 1')
sleep(1.5)
print('Jouw nummer moet wel op een correcte positie gezet worden.\nHet volgende nummer mag niet kleiner zijn en de nummers ervoor mogen niet groter zijn dan de nummer die jij hebt')
sleep(1.5)
print('Dezelfde nummers mogen elkaar wel opvolgen')
sleep(1.5)
print('Wanneer jij jouw nummer nergens in kunt vullen, type dan \'end\'')
sleep(1)
print('Het spel stopt als jij \'stop\' typet of wanneer de witte scoreblad vol is. De witte scoreblad wordt gevuld wanneer jij optie c of d kiest, vervolgens wordt jouw score berekend')
sleep(1)
print('Succes!')
while game:

    if len(whiteScore) == 5:
        pointCalculate(redScore, blueScore, whiteScore)
        game = False
        break

    while True:
        print('De stand van zaken')
        print(f'Rood = {redScore}')
        print(f'Blauw = {blueScore}')
        print(f'Wit = {whiteScore}')
        question1 = input('Type \'1\' om te dobbelen. Type \'stop\' als je wilt stoppen ')
        if question1 == '1':
            redNumber = choice(redDice)
            blueNumber = choice(blueDice)
            whiteNumber = choice(whiteDice)
            break
        elif question1 == 'stop':
            pointCalculate(redScore, blueScore, whiteScore)
            game = False
            break
        else:
            error()
    
    if game == False:
        break
    elif len(whiteScore) == 5:
        pointCalculate(redScore, blueScore, whiteScore)
        break

    print(f'Je gedobbelde waarden zijn {redNumber} (rood), {blueNumber} (blauw), {whiteNumber} (wit). Je kunt uit de volgende berekeningen kiezen:')

    totalA = redNumber + blueNumber + whiteNumber
    totalB = redNumber + blueNumber - whiteNumber
    totalC = redNumber + blueNumber
    highAndLow.append(redNumber)
    highAndLow.append(blueNumber)
    highestNumber = max(highAndLow)
    lowestNumber = min(highAndLow)
    totalD = highestNumber - lowestNumber

    print(f'A) {redNumber} + {blueNumber} + {whiteNumber} = {totalA}')
    print(f'B) {redNumber} + {blueNumber} - {whiteNumber} = {totalB}')
    print(f'C) {redNumber} + {blueNumber} = {totalC}')
    print(f'D) {highestNumber} - {lowestNumber} = {totalD}')

    print()
    while True:
        numberChoice = input('').upper()
        if numberChoice == 'A':
            Main(totalA, 'A')
            break
        elif numberChoice == 'B':
            Main(totalB, 'B')
            break
        elif numberChoice == 'C':
            Main(totalC, 'C')
            whiteScore.append(whiteNumber)
            break
        elif numberChoice == 'D':
            Main(totalD, 'D')
            whiteScore.append(whiteNumber)
            break
        else:
            error()