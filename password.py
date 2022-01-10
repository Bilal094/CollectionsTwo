import random 
from random import choice, shuffle
# Assignments
Hoofdletter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Kleineletter = "abcdefghijklmnopqrstuvwxyz"
Cijfer = "1234567890"
Symbolen = ["@", "#", "$", "%", "&", "_", "?"]

def generator():
    a = random.randint(2,6)
    b = random.randint(4,7)
    Wachtwoord = []


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


W = generator()
shuffle(W)
if W[0] and W[-1] in Symbolen:
    while W[0] and W[-1] in Symbolen:
        shuffle(W)
        print(W)
        break
else:
    print(W)






