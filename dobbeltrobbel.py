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
        print('Rood en blauw zijn gelijk aan elkaar, dus je kunt kiezen waar jij jouw gekozen getalin wilt vullen')
    elif red > blue:
        print('Je hebt het hoogst gerold met de rode dobbelsteen, dus je vult jouw gekozen getal in de blauwe rij')
    elif red < blue:
        print('Je hebt het hoogst gerold met de blauwe dobbelsteen, dus je vult jouw gekozen getal in de rode rij')

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
    numberComparison(redNumber, blueNumber)
