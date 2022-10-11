import random

class Game:
    def __init__(self, deck, player):
        self.deck = deck
        self.card = deck[random.choice(range(0,len(deck)))]
        self.points = 0
        self.player = player
        self.hand = []

    # note need to draw card first when calling
    def draw_card(self, item, all_cards):
        self.card = all_cards[random.choice(range(0,len(all_cards)))]
        self.hand.append(self.card)
        if self.card[3] == 'A':
            self.points = 0
            print(self.hand)
            answer = int(input(f"{self.player} do you want ace to be 1 or 11? "))
            self.points = answer
        elif self.card[3] == 'J' or self.card[3] == 'Q' or self.card[3] == 'K':
            self.points = 0
            self.points = 10
        else:
            self.points = 0
            self.points = int(self.card[3:len(self.card)])
        if item in self.deck:
            self.deck.remove(item)
        
# makes deck
suits = ['❤️ ', '♦️ ', '♠️ ', '♣️ ']
ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
deck = []
for symbol in suits:
    for rank in ranks:
        deck.append(f"{symbol}{rank}")
# Players involved
player_1 = "Dealer"
d_score = 0
player_2 = "Player"
p_score = 0

dealer = Game(deck, player_1)
player = Game(deck, player_2)

# give player two cards
while len(dealer.hand) < 2 or len(dealer.hand) < 2:
    dealer.draw_card(dealer.card, dealer.deck)
    d_score += dealer.points 
    player.draw_card(player.card, player.deck)
    p_score += player.points 

#prints cards that were given
print(f"Dealer hand {dealer.hand}: Score = {d_score}")
print(f"Player hand {player.hand} Score = {p_score}") 
print(len(dealer.deck))

#Dealer plays if score less than 17 based on rules
if d_score < 17:
    print("Dealer gets to play")
    while d_score < 17:
        dealer.draw_card(dealer.card, dealer.deck)
        d_score += dealer.points 
    print(f"Dealer hand {dealer.hand}: Score = {d_score}")

# player gets to play now if the so choose
answer = ''
while answer != 'NO' and p_score < 21:
    answer = input(f"{player.player} do you want to play (yes or no): ").upper()
    if answer == 'YES':
        player.draw_card(player.card, player.deck)
        p_score += player.points 
        print(f"Player hand {player.hand} Score = {p_score}") 

# determines the outcome
if p_score > 21:
    print('You lost because you busted!')
elif (p_score <= 21 and p_score > d_score) or (d_score > 21 and p_score < 21):
    print('You Won!!!')
elif d_score == p_score:
    print('Tie Game')
else:
    print('You lost')
