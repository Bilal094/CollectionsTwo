import random 
from random import choice, shuffle
# Assignments
Hoofdletter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Kleineletter = "abcdefghijklmnopqrstuvwxyz"
Cijfer = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
Symbolen = ["@", "#", "$", "%", "&", "_", "?"]
Wachtwoord = []
# Code start
def generator():
    a = random.randint(2,6)
    b = random.randint(4,7)

    for x in range(a):
        Hoofd = choice(Hoofdletter)
        Wachtwoord.append(Hoofd)

    for y in range(b):
        Getal = choice(Cijfer)
        Wachtwoord.append(Getal)

    for z in range(3):
        Symbool = choice(Symbolen)
        Wachtwoord.append(Symbool)

    i = x + y + 5
    lengte = 24 - i

    for k in range(lengte):
        Klein = choice(Kleineletter)
        Wachtwoord.append(Klein)
    
    return Wachtwoord

generator()

shuffle(Wachtwoord)
if Wachtwoord[0] in Symbolen or Wachtwoord[-1] in Symbolen or Wachtwoord[0] in Cijfer or Wachtwoord[1] in Cijfer or Wachtwoord[2] in Cijfer:
    while Wachtwoord[0] in Symbolen or Wachtwoord[-1] in Symbolen or Wachtwoord[0] in Cijfer or Wachtwoord[1] in Cijfer or Wachtwoord[2] in Cijfer:
        print('Re-shuffle...')
        shuffle(Wachtwoord)
        print(''.join(Wachtwoord))
else:
    print(''.join(Wachtwoord))