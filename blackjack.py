import random
from tokenize import Number
# Write your blackjack game here.
class Game:

    def __init__ (self, deck, card, points):
        self.deck = deck
        self.card = card
        self.points = int(points)
    
    def remove_card(self, item):
        if item in self.deck:
            self.deck.remove(item)



class Deck:
    def __init__ (self, suits, ranks):
        self.suits = suits
        self.ranks = ranks
        self.deck = []
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(f"{suit}{rank}") 


class Card:
    possible = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']

    def __init__(self, array):
        self.card = array[random.choice(range(0,len(array)))]
        self.value = 0
        # need to assign value to each card
        for value in Card.possible:
            if self.card[2] == 'A':
                self.value = [1, 11] #have dealer ask question then it picks 
            elif self.card[2] == 'J' or self.card[2] == 'Q' or self.card[2] == 'K':
                self.value = 10
            else:
                self.value = self.card[2:len(self.card)]


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
d = Dealer('Yes')

x = 0
overallScore = 0
while x < 2:
    c = Card(standard.deck)
    test = Game(standard.deck,c.card, c.value)
    print(test.points)
    overallScore += test.points
    x += 1


# p1 = Player()
# p2 = Player()


print(overallScore)
# print(len(test.deck))
# test.remove_card(c.card)
# print(len(test.deck))
# print(standard.deck)
print('indiv card')
print(c.card)
print('card points')
print(c.value)
# print('dealer choose hit')
# print(d.action)
# print('see if Game returns values from classes')
# print(test.card)
# print('see if player name is inputed')
# print(p1.name)
# print(p2.name)
# print(Player.player_count)

