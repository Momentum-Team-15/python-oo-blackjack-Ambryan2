import random
from tokenize import Number
# Write your blackjack game here.
class Game:
    def __init__ (self, deck, card, points):
        self.deck = deck
        self.card = card
        # need to put rules in here

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
        # need to assign value to each card
        self.value = 10


class Dealer:
    def __init__(self, choice):
        self.choice = choice
        if choice.upper() == 'YES':
            self.action = 0
        else:
            self.action = 1


class Player:
    player_count = 1

    def __init__(self):
        self.name = input(f"Player {Player.player_count} enter your name: ")
        Player.player_count += 1

standard = Deck(['❤️', '♦️', '♠️', '♣️'],['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'])
c = Card(standard.deck)
d = Dealer('Yes')
test = Game(standard.deck,c.card, 5)
p1 = Player()
p2 = Player()

print(standard.deck)
print('indiv card')
print(c.card)
print('card points')
print(c.value)
print('dealer choose hit')
print(d.action)
print('see if Game returns values from classes')
print(test.card)
print('see if player name is inputed')
print(p1.name)
print(p2.name)
print(Player.player_count)

