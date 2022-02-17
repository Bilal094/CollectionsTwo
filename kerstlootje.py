import random
namesWithDuplicates = []
names = []
main = True

while True:
    question = input('Type de namen van de deelnemers. Type \'1\' als je klaar bent. Type \'stop\' als je wilt stoppen ').lower()
    namesWithDuplicates.append(question)

    if question == 'stop':
        break

    if '1' in namesWithDuplicates:
        namesWithDuplicates.remove('1')

    if question == '1':
        if len(names) > 1:
            lootLoop = True
            while lootLoop:
                loot1 = random.choice(names)
                loot2 = random.choice(names)
                if loot1 != loot2:
                    print(f'{loot1} voor {loot2}')
                    main = False
                    lootLoop = False
        else:
            print('Je moet meer dan 1 deelnemer toevoegen!')

    for x in namesWithDuplicates:
        if x not in names:
            names.append(x)
            namesWithDuplicates.clear()
        else:
            print('Deze deelnemer is al opgegeven!')
            namesWithDuplicates.clear()