import random

class Game:
    def __init__(self, deck, player):
        self.deck = deck
        self.points = 0
        self.player = player
        self.hand = []
        self.score = 0

    # note need to draw card first when calling
    def draw_card(self): #, item, all_cards):
        self.card = self.deck[random.choice(range(0,len(self.deck)))]
        self.hand.append(self.card)
        if self.card[3] == 'A':
            print(self.hand)
            answer = int(input(f"{self.player} do you want ace to be 1 or 11? "))
            self.points = answer
        elif self.card[3] == 'J' or self.card[3] == 'Q' or self.card[3] == 'K':
            self.points = 10
        else:
            self.points = int(self.card[3:len(self.card)])
        self.score += self.points
        if self.card in self.deck:
            self.deck.remove(self.card)

class Deck:
    def __init__(self,suits, ranks):
        self.deck = []
        for symbol in suits:
            for rank in ranks:
                self.deck.append(f"{symbol}{rank}")
game = input('Do you want to play blackjack (yes or no): ').lower()

player_1 = "Dealer"
p1_wins = 0

player_2 = input("What is your name: ")
p2_wins = 0


while game != 'no':
# makes deck
    deck = Deck(['♥️ ', '♦️ ', '♠️ ', '♣️ '],['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'])
    new_deck = deck.deck

    # this puts these players in the game
    dealer = Game(new_deck, player_1)
    player = Game(new_deck, player_2)

    # give player two cards
    while len(dealer.hand) < 2 or len(dealer.hand) < 2:
        dealer.draw_card()
        player.draw_card()

    #prints cards that were given
    print(f"Dealer hand {dealer.hand}: Score = {dealer.score}")
    print(f"{player.player} hand {player.hand} Score = {player.score}") 
    # print(len(dealer.deck))

    #Dealer plays if score less than 17 based on rules
    if dealer.score < 17:
        print("Dealer gets to play")
        while dealer.score < 17:
            dealer.draw_card()
        print(f"Dealer hand {dealer.hand}: Score = {dealer.score}")

    # player gets to play now if the so choose
    answer = ''
    while answer != 'NO' and player.score < 21:
        answer = input(f"{player.player} do you want another card (yes or no): ").upper()
        if answer == 'YES':
            player.draw_card()
            print(f"Player hand {player.hand} Score = {player.score}") 

    # determines the outcome
    if player.score > 21:
        print('You lost because you busted!')
        p1_wins += 1
    elif (player.score <= 21 and player.score > dealer.score) or (dealer.score > 21 and player.score <= 21):
        print('You Won!!!')
        p2_wins += 1
    elif dealer.score == player.score:
        print('Tie Game')
    else:
        print('You lost')
        p1_wins += 1
    print()
    print(f"Dealer has won {p1_wins}\nYou have won {p2_wins}")
    print()
    game = input('Do you want to continue playing (yes or no): ').lower()
