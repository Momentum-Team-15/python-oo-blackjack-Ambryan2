import random

class Game:
    # p_points = 0

    def __init__(self, deck, player):
        self.deck = deck
        self.card = deck[random.choice(range(0,len(deck)))]
        self.points = 0

        self.player = player
        # self.p_points += self.points
    
    # note need to draw card first when calling
    def draw_card(self, item, all_cards):
        self.card = all_cards[random.choice(range(0,len(all_cards)))]
        if self.card[2] == 'A':
            self.points = 0
            answer = int(input(f"Do you want ace to be 1 or 11? "))
            self.points = answer
        elif self.card[2] == 'J' or self.card[2] == 'Q' or self.card[2] == 'K':
            self.points = 0
            self.points = 10
        else:
            self.points = 0
            self.points = self.card[2:len(self.card)]
        if item in self.deck:
            self.deck.remove(item)
        
# makes deck
suits = ['❤️', '♦️', '♠️', '♣️']
ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
deck = []
for symbol in suits:
    for rank in ranks:
        deck.append(f"{symbol}{rank}")
# card = deck[random.choice(range(0,len(deck)))]

player_1 = "Dealer"
d_score = 0
player_2 = "Player"
p_score = 0

dealer = Game(deck, player_1)
player = Game(deck, player_2)


# this order prints the card and the points with card including ace
dealer.draw_card(dealer.card, dealer.deck)
print(dealer.card + "this is card wanted to add")
print(len(dealer.deck))
d_score += int(dealer.points)
print(f"{d_score} this is wanted score from card")

dealer.draw_card(dealer.card, dealer.deck)
print(dealer.card + "This is card wanted to add")
d_score += int(dealer.points)
print(f"{d_score} this is wanted score")
# dealer.draw_card(dealer.card, dealer.deck)
print(len(dealer.deck))

print(f"{len(player.deck)} this is length of player deck")
# print(dealer.points)
# print(dealer.player)
