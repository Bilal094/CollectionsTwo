import random
# Assignments
Hoofdletter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Kleineletter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Cijfer = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
Symbolen = ["@", "#", "$", "%", "&", "_", "?"]
Wachtwoord = []
HoofdIndex = random.randrange(2,6)
KleinIndex = random.randrange(8)
CijferIndex = random.randrange(4,7)
SymbolenIndex = random.randint(3)

# Code start
# for m in range(1):
for x in range(HoofdIndex):
    x = random.choice(Hoofdletter)
    Wachtwoord.append(x)
    
for y in range(KleinIndex):
    y = random.choice(Kleineletter)
    Wachtwoord.append(y)

for z in range(CijferIndex):
    z = random.choice(Cijfer)
    Wachtwoord.append(z)

for i in range(SymbolenIndex):
    i = random.choice(Symbolen)
    Wachtwoord.append(i)



random.shuffle(Wachtwoord)
print(Wachtwoord)

