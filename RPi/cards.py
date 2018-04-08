# Card Deck Creator
# By Ethan Crooks
# Work in progress, to be used with card games such as poker or higher or lower

import random

def deckgenerator():
    deck = []
    suitdict = {1: 's', 2: 'c', 3: 'h', 4: 'd'}
    numberdict = {1:'A',2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:'J',12:'Q',13:'K'}
    for suit in range(1,5):
        for number in range(1,14):
            cardsuit = suitdict[suit]
            cardnumber = numberdict[number]
            card = str(cardnumber) + str(cardsuit)
            deck.append(card)
    return deck

print(deckgenerator())
