import random
Kleuren = ["klaveren", "ruiten", "schoppen", "harten"]
Kaarten = ["boer", "vrouw", "heer", "aas", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
DeckList = []

for x in Kleuren:
    for y in Kaarten:
        Deck = x + ' ' + y
        DeckList.append(Deck)

for z in range(2):
    DeckList.append('joker')

random.shuffle(DeckList)
for u in range(1,8):
    Kaarten7 = DeckList.pop()
    print(f'Kaart {u}: {Kaarten7}')

print()
print('Deck (47 kaarten) =', DeckList)