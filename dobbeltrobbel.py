# Import ---
import random, time
from random import choice
from time import sleep
# Assignments ---
game = 0
Red2 = -2
Blue2 = -2
redDice = [1, 2, 3, 4, 5, 6]
blueDice = [1, 2, 3, 4, 5, 6]
whiteDice = [1, 1, 1, 2, 2, 3]
redScore = [Red2, '', '', '', '', '', '', '', '', '']
blueScore = ['', '', '', '', '', '', '', '', '', Blue2]
whiteScore = ['','','','','']
highAndLow = []
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
        while index < len(List) - 1:
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
            elif pCR == False and pCL == False:
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

# Code start ---

while game < 10:
    while True:
        question1 = input('Type \'1\' om te dobbelen ')
        if question1 == '1':
            redNumber = choice(redDice)
            blueNumber = choice(blueDice)
            whiteNumber = choice(whiteDice)
            break
        else:
            error()

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
            break
        elif numberChoice == 'D':
            Main(totalD, 'D')
            break
        else:
            error()

    game += 1