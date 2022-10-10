import random
from tokenize import Number
# Write your blackjack game here.
class Game:
    pass

class Deck:
    def __init__ (self, suits, ranks):
        self.suits = suits
        self.ranks = ranks
        self.deck = []
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(f"{suit}{rank}")    

class Card:
    def __init__(self, array):
        self.card = array[random.choice(range(0,len(array)))]
        self.value = 10

class Dealer:
    pass

class Player:
    pass

t = Deck(['❤️', '♦️', '♠️', '♣️'],['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'])
c = Card(t.deck)
print(t.deck)
print()
print(c.card)
print()
print(c.value)
