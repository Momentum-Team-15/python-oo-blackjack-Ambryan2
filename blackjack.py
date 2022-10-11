# import random
# from tokenize import Number
# from tracemalloc import start
# # Write your blackjack game here.
# class Game:
#     start = []
#     def __init__ (self, deck, card, points):
#         self.deck = deck
#         self.card = card
#         self.points = 0
#         # self.points = points
#         if points == [1,11]:
#             answer = int(input(f"Do you want ace to be 1 or 11? "))
#             if answer == 1:
#                 self.points = 1
#             else:
#                 self.points = 11
#         else:
#             self.points += int(points)

#     def remove_card(self, item):
#         if item in self.deck:
#             self.deck.remove(item)

# class Deck:
#     def __init__ (self, suits, ranks):
#         self.suits = suits
#         self.ranks = ranks
#         self.deck = []
#         for suit in self.suits:
#             for rank in self.ranks:
#                 self.deck.append(f"{suit}{rank}") 

# class Card:
#     possible = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']

#     def __init__(self, array):
#         self.card = array[random.choice(range(0,len(array)))]
#         self.value = 0
#         # need to assign value to each card
#         for value in Card.possible:
#             if self.card[2] == 'A':
#                 self.value = [1,11] #have dealer ask question then it picks 
#             elif self.card[2] == 'J' or self.card[2] == 'Q' or self.card[2] == 'K':
#                 self.value = 10
#             else:
#                 self.value = self.card[2:len(self.card)]

# class Player:
#     player_count = 1

#     def __init__(self):
#         self.name = input(f"Player {Player.player_count} enter your name: ")
#         Player.player_count += 1

# # this is the beginning of the game

# standard = Deck(['❤️', '♦️', '♠️', '♣️'],['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'])

# # this is first card in deck
# c = Card(standard.deck)
# blackjack = Game(standard.deck,c.card, c.value)

# # deal cards to each player
# player_cards = []
# player_points = 0
# dealer_cards = []
# dealer_points = 0
# count = 0

# while len(player_cards) < 2:
#     player_cards.append(blackjack.card)
#     player_points += blackjack.points
#     blackjack.remove_card(c.card)
#     c = Card(standard.deck)
#     blackjack = Game(standard.deck,c.card, c.value)

# while len(dealer_cards) < 2:
#     dealer_cards.append(blackjack.card)
#     dealer_points += blackjack.points
#     blackjack.remove_card(c.card)
#     c = Card(standard.deck)
#     blackjack = Game(standard.deck,c.card, c.value)


# print(f"Players cards: {' '.join(player_cards)} which equals {player_points}\nDealer Cards: {' '.join(dealer_cards)} which equals {dealer_points}")

# # This is for the dealer's turn if points less than 17
# if dealer_points < 17:
#     print(f"Dealer now plays ...")
#     while dealer_points < 17:
#         dealer_cards.append(blackjack.card)
#         dealer_points += blackjack.points
#         blackjack.remove_card(c.card)
#         c = Card(standard.deck)
#         blackjack = Game(standard.deck,c.card, c.value)
#     print(f"Dealer cards are {' '.join(dealer_cards)} and points are {dealer_points}")

# # while loop that ask if player wants to hit unless they decide not
# ask = ''
# while ask != "no" and player_points < 22:
#     print(f"Your points are {player_points}")
#     ask = input("Do you want to continue? ").lower()
#     if ask == 'yes':
#         player_cards.append(blackjack.card)
#         player_points += blackjack.points
#         blackjack.remove_card(c.card)
#         c = Card(standard.deck)
#         blackjack = Game(standard.deck,c.card, c.value)

# if player_points > 21:
#     print('Busted')
# elif player_points < 21 and player_points > dealer_points:
#     print('You Won!!!')
# elif dealer_points > 21 and player_points < 21:
#     print('You Won!!')
# else:
#     print('You lost')
