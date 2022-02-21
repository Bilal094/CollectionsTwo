import random
from random import shuffle, choice
namesWithDuplicates = []
namesparticipants = []
namesinhat = []
usedNames = []
main = True
lootLoop = True

while True:
    question = input('Type de namen van de deelnemers. Type \'1\' als je klaar bent. Type \'stop\' als je wilt stoppen ').lower()
    namesWithDuplicates.append(question)

    if question == 'stop':
        break

    if '1' in namesWithDuplicates:
        namesWithDuplicates.remove('1')

    if question == '1':
        if len(namesparticipants) > 1:
            lootLoop = True
            break
        else:
            print('Je moet meer dan 1 deelnemer toevoegen!')

    for x in namesWithDuplicates:
        if x not in namesparticipants:
            namesparticipants.append(x)
            namesWithDuplicates.clear()
        else:
            print('Deze deelnemer is al opgegeven!')
            namesWithDuplicates.clear()

if lootLoop == True:
    namesinhat = namesparticipants.copy()
    while lootLoop:
        shuffle(namesparticipants)
        shuffle(namesinhat)
        while True:
            loot1 = choice(namesparticipants)
            loot2 = choice(namesinhat)
            if len(namesinhat) == 2:
                if loot1 == loot2:
                    newloot1 = choice(usedNames)
                    namesparticipants.append(newloot1)
            if loot1 != loot2:
                print(f'{loot1} heeft een lootje van {loot2}')
                usedNames.append(loot1)
                namesparticipants.remove(loot1)
                namesinhat.remove(loot2)
                break
        if len(namesinhat) == 0:
            lootLoop = False
            break