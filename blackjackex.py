
import random

SUITS = ['♥️', '♠️', '♦️', '♣️']
RANK_VALUE = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player()
        self.dealer = Dealer()

        self.deal_card(self.dealer)
        self.deal_card(self.dealer)
        self.deal_card(self.player)
        self.deal_card(self.player)

        print("The dealer's cards are : ")
        print("Hidden")
        print(f'{self.dealer.hand[1]}\n')

        # print(f'Dealer total: {self.calculate_hand(self.dealer)}\n')

        print("The player's cards are : ")
        for card in self.player.hand:
            print(card)
        print(f'Your total :{self.calculate_hand(self.player)}\n')

        # print(f'Cards remaining: {len(self.deck.cards)}')

    def deal_card(self, participant):
        card = self.deck.cards.pop()
        participant.hand.append(card)

    def calculate_hand(self, participant):
        total_points = 0
        for card in participant.hand:
            total_points += card.value
        return total_points




class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank_value in RANK_VALUE.items():
                new_card = Card(suit, rank_value[0], rank_value[1])
                self.cards.append(new_card)
                
    def shuffle(self):
        random.shuffle(self.cards)

class Player:
    def __init__(self):
        self.hand = []


class Dealer:
    def __init__(self):
        self.hand = []


new_game = Game()

if new_game.calculate_hand(new_game.dealer) == 21:
    print('Dealer has BlackJack!')
    if new_game.calculate_hand(new_game.player) == 21:
        print('Push')

elif new_game.calculate_hand(new_game.player) == 21:
    print('You have BlackJack!')

while new_game.calculate_hand(new_game.dealer) < 17:
    print('Dealer hits\n')
    new_game.deal_card(new_game.dealer)
    print('Hidden')
    for card in new_game.dealer.hand[1:]:
        print(card)
    print('\n')
    if new_game.calculate_hand(new_game.dealer) > 21:
        print(f'Dealer bust {new_game.calculate_hand(new_game.dealer)}')
        for card in new_game.dealer.hand:
            print(card)
        exit()

    elif new_game.calculate_hand(new_game.dealer) == 21:
        print('Dealer has 21')

def hit():
    hit_stay = input("Would you like to hit? 'Y' or 'N': ").upper()
    print('\n')
    if hit_stay == 'Y':
        new_game.deal_card(new_game.player)
        for card in new_game.player.hand:
            print(card)
        print(f'Your total: {new_game.calculate_hand(new_game.player)}\n')
        if new_game.calculate_hand(new_game.player) > 21:
            print('Bust, you lose')
            exit()
        hit()
    elif hit_stay == 'N':
        for card in new_game.player.hand:
            print(card)
        print(f'Your total: {new_game.calculate_hand(new_game.player)}\n')
        for card in new_game.dealer.hand:
            print(card)
        print(f'Dealer total {new_game.calculate_hand(new_game.dealer)}')
        if new_game.calculate_hand(new_game.player) > new_game.calculate_hand(new_game.dealer):
            print('\nYou win')
        elif new_game.calculate_hand(new_game.player) == new_game.calculate_hand(new_game.dealer):
            print('\nTie game')
        else:
            print('\nYou lose')
    else:
        hit()

hit()