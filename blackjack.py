
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
        print("Hidden Card")
        print(f'{self.dealer.hand[1]}\n')

        print("The player's cards are : ")
        for card in self.player.hand:
            print(card)
        print(f'Your total :{self.calculate_hand(self.player)}\n')

        self.player_turn()
        self.dealer_turn()
        self.scoring()

    def deal_card(self, participant):
        card = self.deck.cards.pop()
        participant.hand.append(card)

    def calculate_hand(self, participant):
        total_points = 0
        for card in participant.hand:
            total_points += card.value
        return total_points

    def player_turn(self):
        hit_stay = input("Would you like to hit? 'Y' or 'N': ").upper()
        print('\n')
        if hit_stay == 'Y':
            self.deal_card(self.player)
            for card in self.player.hand:
                print(card)
            print(f'Your total: {self.calculate_hand(self.player)}\n')
            if self.calculate_hand(self.player) > 21:
                print('Bust, you lose')
                exit()
            self.player_turn()
        elif hit_stay == 'N':
            for card in self.player.hand:
                print(card)
            print(f'Your final score: {self.calculate_hand(self.player)}\n')
        else:
            self.player_turn()

    def dealer_turn(self):
        while self.calculate_hand(self.dealer) < 17:
            print('----------------------------------')
            self.deal_card(self.dealer)
            print('Dealer hits\n')
            for card in self.dealer.hand:
                print(card)
            print(f"Dealer's hand and total {self.calculate_hand(self.dealer)}")
        if self.calculate_hand(self.dealer) > 21:
            print('----------------------------------')
            print(f'Dealer bust on {self.calculate_hand(self.dealer)}')
            exit()
        if self.calculate_hand(self.dealer) >= 17 and self.calculate_hand(self.dealer) <= 21:
            print('----------------------------------')
            for card in self.dealer.hand:
                print(card)
            print(f"Dealer's final hand and score: {self.calculate_hand(self.dealer)}")

    def scoring(self):
        if self.calculate_hand(self.player) > self.calculate_hand(self.dealer):
            print('\nYou win')
        elif self.calculate_hand(self.player) == self.calculate_hand(self.dealer):
            print('\nTie game')
        else:
            print('\nYou lose')

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

Game()