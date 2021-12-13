Boodschappen = {}
Loop = True

while Loop == True:
    Vraag = input('Wat wil je toevoegen in je boodschappenlijstje? Type \'stop\' als je klaar bent/wilt stoppen ').lower()
    if Vraag == 'stop':
        Loop = False
        print('Boodschappenlijstje = ' + str(Boodschappen))
    else:    
        Aantal = int(input('Aantal '+ Vraag +': '))
        for x in range(Aantal):
            if Vraag in Boodschappen.keys():
                Boodschappen[Vraag] += 1 
            else:
                Boodschappen[Vraag] = 1