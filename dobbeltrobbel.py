# Import ---
from ast import ListComp
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
# Functions ---
def positionError():
    print('De gekozen positie is niet geldig')
def error():
    print('Type a.u.b een gegeven keuze')

def numberComparison(red, blue):
    if red == blue:
        return 'even'
    elif red > blue:
        return 'blue'
    elif red < blue:
        return 'red'


def checkPositionRight(number, position, List):
    global isValidR, isValidL
    if List == blueScore:
        List.reverse()
    isValidR = False
    if List[int(position)] == '':
        index = int(position)
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
    if List == blueScore:
        List.reverse()
    isValidL = False
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

    print(f'A) {redNumber} + {blueNumber} + {whiteNumber} = {totalA}')
    print(f'B) {redNumber} + {blueNumber} - {whiteNumber} = {totalB}')

    print()
    numberChoice = input('').upper()
    if numberChoice == 'A':
        print(f'Je hebt gekozen voor optie A ({totalA})')
        sleep(1)
        nC = numberComparison(redNumber, blueNumber)
        if nC == 'red':
            print('De rode dobbelsteen heeft het laagst gerold')
            sleep(1)
            print(redScore)

            positionBoolR = True
            while positionBoolR:
                positionChoice = input('Kies waar jij je nummer wilt zetten (0 - 9) of type \'end\' wanneer je jouw nummer nergens in kunt vullen ')
                if positionChoice == 'end':
                    break

                pCR = checkPositionRight(totalA, positionChoice, redScore)
                pCL = checkPositionLeft(totalA, positionChoice, redScore)
                if pCR == True and pCL == True:
                    redScore[int(positionChoice)] = totalA
                    positionBoolR = False
                elif pCR == False and pCL == False:
                    positionError()

        elif nC == 'blue':
            print('De blauwe dobbelsteen heeft het laagst gerold')
            sleep(1)
            print(blueScore)

            positionBoolB = True
            while positionBoolB:
                positionChoice = input('Kies waar jij je nummer wilt zetten (0 - 9) (Omgekeerd!) of type \'end\' wanneer je jouw nummer nergens in kunt vullen ')
                if positionChoice == 'end':
                    break

                pCR = checkPositionRight(totalA, positionChoice, blueScore)
                pCL = checkPositionLeft(totalA, positionChoice, blueScore)
                if pCR == True and pCL == True:
                    blueScore[int(positionChoice)] = totalA
                    positionBoolB = False
                elif pCR == False and pCL == False:
                    positionError()

    elif numberChoice == 'B':

        print(f'Je hebt gekozen voor optie B ({totalB})')
        sleep(1)
        nC = numberComparison(redNumber, blueNumber)
        if nC == 'red':
            print('De rode dobbelsteen heeft het laagst gerold')
            sleep(1)
            print(redScore)

            positionBoolR = True
            while positionBoolR:
                positionChoice = input('Kies waar jij je nummer wilt zetten (0 - 9) of type \'end\' wanneer je jouw nummer nergens in kunt vullen ')
                if positionChoice == 'end':
                    break

                pCR = checkPositionRight(totalB, positionChoice, redScore)
                pCL = checkPositionLeft(totalB, positionChoice, redScore)
                if pCR == True and pCL == True:
                    redScore[int(positionChoice)] = totalB
                    positionBoolR = False
                elif pCR == False and pCL == False:
                    positionError()

        elif nC == 'blue':
            print('De blauwe dobbelsteen heeft het laagst gerold')
            sleep(1)
            print(blueScore)

            positionBoolB = True
            while positionBoolB:
                positionChoice = input('Kies waar jij je nummer wilt zetten (0 - 9) (Omgekeerd!) of type \'end\' wanneer je jouw nummer nergens in kunt vullen ')
                if positionChoice == 'end':
                    break

                pCR = checkPositionRight(totalB, positionChoice, blueScore)
                pCL = checkPositionLeft(totalB, positionChoice, blueScore)
                if pCR == True and pCL == True:
                    blueScore[int(positionChoice)] = totalB
                    positionBoolB = False
                elif pCR == False and pCL == False:
                    positionError()
    game += 1