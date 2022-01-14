import random 
from random import choice
# Assignments
Blauw = [1, 2, 3, 4, 5, 6]
Rood = [1, 2, 3, 4, 5, 6]
Wit = [1, 1, 1, 2, 2, 3]
BlauwScore = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
RoodScore = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def scoreBlad(puntBlauw, puntRood):
    if puntBlauw == 0 or puntRood == 0:
        print()
    else:
        pass 
    print('---------------------------------- Score blad ----------------------------------')
    print('|                                                                             |')
    print(f'| Blauw: [-2] [{None}] [{None}] [{None}] [{None}] [{None}] [{None}] [{None}] [{None}] [{None}]  |')
    print(f'| Rood:  [{None}] [{None}] [{None}] [{None}] [{None}] [{None}] [{None}] [{None}] [{None}] [-2]  |')
    print(f'| Wit:                  [{None}] [{None}] [{None}] [{None}] [{None}]                    |')


scoreBlad(0,0)