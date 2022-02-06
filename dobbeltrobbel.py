# Import ---
import random, time
from random import choice
from time import sleep
# Assignments ---
Red2 = -2
Blue2 = -2
redDice = [1, 2, 3, 4, 5, 6]
blueDice = [1, 2, 3, 4, 5, 6]
whiteDice = [1, 1, 1, 2, 2, 3]
redScore = [Red2, '', '', '', '', '', '', '', '']
blueScore = ['', '', '', '', '', '', '', '', Blue2]
whiteScore = ['','','','','']
# Functions ---

def error():
    print('Type a.u.b een gegeven keuze')

def numberComparison(red, blue):
    if red == blue:
        return 'even'
    elif red > blue:
        return 'blue'
    elif red < blue:
        return 'red'

def checkIfPositionTrue(number, position, list):
    if list[position] == "":
        index = position
        while True:
            index += 1
            if list[index] != "":
                if number > list[index] or number == list[index]:
                    while True:
                        index -= 1
                        if list[index] != "":
                            if number < list[index] or number == list[index]:
                                return True
                            else:
                                return False
                else:       
                    return False

# Code start ---
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
        print('rood')

    elif nC == 'blue':
        print('blauw')
