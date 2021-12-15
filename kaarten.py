import random
Kleuren = ["klaveren", "ruiten", "schoppen", "harten"]
Kaarten = ["boer", "vrouw", "heer", "aas", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
DeckList = []

for x in range(1,8):
    Deck = random.choice(Kleuren) +  ' ' + random.choice(Kaarten)
    print(f'Kaart {x}: {Deck}')


for x in range(47):
    Deck1 = random.choice(Deck)
    DeckList.append(Deck1)


print(DeckList)
