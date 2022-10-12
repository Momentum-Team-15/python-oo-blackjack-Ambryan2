import random

class Game:
    def __init__(self, deck, player):
        self.deck = deck
        self.points = 0
        self.player = player
        self.hand = []
        self.score = 0
        self.win = 0
    # note need to draw card first when calling
    def draw_card(self): #, item, all_cards):
        self.card = self.deck[random.choice(range(0,len(self.deck)))]
        self.hand.append(self.card)
        # if self.card[3] == 'A':
        #     print(self.hand)
        #     answer = int(input(f"{self.player} do you want ace to be 1 or 11? "))
        #     self.points = answer
        # elif self.card[3] == 'J' or self.card[3] == 'Q' or self.card[3] == 'K':
        #     self.points = 10
        # else:
        #     self.points = int(self.card[3:len(self.card)])
        # self.score += self.points
        if self.card in self.deck:
            self.deck.remove(self.card)
    
    def calculate_score(self):
        self.score = 0
        for card in self.hand:
            if card[3] == 'A':
                print(self.hand)
                answer = int(input(f"{self.player} do you want ace to be 1 or 11? "))
                self.points = answer
            elif card[3] == 'J' or card[3] == 'Q' or card[3] == 'K':
                self.points = 10
            else:
                self.points = int(card[3:len(card)])
            self.score += self.points

    def deal_two(self):
        while len(self.hand) < 2:
            self.draw_card()

    def play_turn(self):
        answer = ''
        while answer != 'NO' and self.score < 21 and dealer.score <= 21:
            answer = input(f"{self.player} do you want another card (yes or no): ").upper()
            if answer == 'YES':
                self.draw_card()
                self.calculate_score()
                print(f"Your hand is {self.hand} Score = {self.score}") 
    
    def determine_winner(self, dealer):
        if self.score > 21:
            print('You lost because you busted!')
            bot.won_game() 
        elif (self.score <= 21 and self.score > dealer.score) or (dealer.score > 21 and self.score <= 21):
            print('You Won!!!')
            you.won_game()
            self.win = 1
        elif dealer.score == self.score:
            print('Tie Game')
        else:
            print('You lost')
            bot.won_game()

class Deck:
    def __init__(self,suits, ranks):
        self.deck = []
        for symbol in suits:
            for rank in ranks:
                self.deck.append(f"{symbol}{rank}")

class Player:
    def __init__(self, name = 'Dealer'):
        self.name = name
        self.money = 0
        self.wins = 0
    
    def ask_name(self):
        name = input('New player what is your name? ')
        self.name = name
        print(f"Nice to meet you {self.name}!")
    # probably put these in Game class
    def won_game(self):
        self.wins += 1

    def lost_bet(self):
        print('Better luck next time')
        self.money -= 10
    
    def won_bet(self):
        print('You got lucky this time')
        self.money += 15
    
game = input('Do you want to play blackjack (yes or no): ').lower()

bot = Player() 
you = Player()
you.ask_name()
# print(f"Nice to meet you {you.name}!")
print()
while game != 'no':
# makes deck
    deck = Deck(['♥️ ', '♦️ ', '♠️ ', '♣️ '],['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'])
    new_deck = deck.deck

    # the_gambler ='no'
    # this puts these players in the game
    dealer = Game(new_deck, bot.name)
    player = Game(new_deck, you.name)

    # give player two cards
    dealer.draw_card()
    dealer.calculate_score()
    player.deal_two()
    player.calculate_score()

    #prints cards that were given
    print(f"Dealer hand {dealer.hand} ?: Score = {dealer.score}")
    print(f"{player.player} hand {player.hand} Score = {player.score}") 

    # print()
    # print("Before we begin why don't we make this a little more interesting...")
    # the_gambler = input("Want to bet $10 for a chance to get $15, yes or no? ").lower()
    print()
    print("Before we begin why don't we make this a little more interesting...")
    the_gambler = input("Want to bet $10 for a chance to get $15, yes or no? ").lower()

    #Dealer plays if score less than 17 based on rules
    if dealer.score < 17:
        while dealer.score < 17:
            dealer.draw_card()
            dealer.calculate_score()
    
    print()
    # player gets to play now if they so choose
    player.play_turn()

    print(f"Dealer hand {dealer.hand}: Score = {dealer.score}")
    print()
    print(f"{player.player} hand {player.hand} Score = {player.score}") 
    print()
    # determines the outcome
    player.determine_winner(dealer)
    if the_gambler == 'yes':
        if player.win == 1:
            you.won_bet()
        else:
            you.lost_bet()
    if you.money > -30:   
        print(f"Your money ${you.money}")
        print()
        print(f"Dealer has won {bot.wins}\nYou have won {you.wins}")
        print()
        game = input('Do you want to continue playing (yes or no): ').lower()
    else:
        print("\n You owe too much money! Get out of the Casino!!!")
        game = 'no'

