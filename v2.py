import random

from blackjack import Deck

class Game:
    possible_numbers = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']

    def __init__(self, deck, player):
        self.deck = deck
        self.card = deck[random.choice(range(0,len(deck)))]
        self.points = 0
        for value in Game.possible_numbers:
            if self.card[2] == 'A':
                answer = int(input(f"Do you want ace to be 1 or 11? "))
                if answer == 1:
                    self.points = 1
                else:
                    self.points = 11
            elif self.card[2] == 'J' or self.card[2] == 'Q' or self.card[2] == 'K':
                self.points = 10
            else:
                self.points = self.card[2:len(self.card)]
        self.player = player
        self.p_points = 0
        self.p_points += self.points
    
    def draw_card(self, item):
        if item in self.deck:
            self.deck.remove(item)
# makes deck
suits = ['❤️', '♦️', '♠️', '♣️']
ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
deck = []
for symbol in suits:
    for rank in ranks:
        deck.append(f"{symbol}{rank}")
print(deck) 