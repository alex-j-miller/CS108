''' Final Project - Uno

Runs the game for Uno

@author: Alex Miller (ajm94)
@date: Fall, 2021
'''

from cards import *
from random import *

class Uno:
    
    def __init__(self):
        """Constructs the UNO game"""
        
        self.cards = self.get_cards()
        self.unused_cards = self.cards
        
        self.p1_hand = []
        self.p2_hand = []
        self.p3_hand = []
        self.p4_hand = []
        
        self.give_cards(self.p1_hand)
        self.give_cards(self.p2_hand)
        self.give_cards(self.p3_hand)
        self.give_cards(self.p4_hand)
        
        self.first_card()
        self.current_player = 1
        
    def get_cards(self):
        """Get cards from cards.txt"""
        cards = []
        f = open('cards.txt', 'r')
        for line in f:
            cards.append(Card(line[0], line[1]))
        f.close()
        return cards
    
    def give_cards(self, hand):
        """Give cards to player's hand"""
        i = 0
        while i < 7:
            n = randrange(0, len(self.unused_cards))
            hand.append(self.unused_cards[n])
            self.unused_cards.remove(self.unused_cards[n])
            i += 1
            
    def draw_card(self, hand):
        """Player draws a card"""
        n = randrange(0, len(self.unused_cards))
        hand.append(self.unused_cards[n])
        self.unused_cards.remove(self.unused_cards[n])
        
    def player_cards(self, hand):
        """Returns the player's cards as a list"""
        cards = []
        for card in hand:
            cards.append(str(card))
        return cards
    
    def first_card(self):
        """Picks the first card for the game"""
        n = randrange(0, len(self.unused_cards))
        x = self.unused_cards[n]
        self.unused_cards.remove(self.unused_cards[n])
        self.top_card = x
    
    def check_playable(self, hand1, hand2):
        """Check to see if a card is playable"""
        return hand1.color == hand2.color or hand1.num == hand2.num or hand1.color == 'W' or hand2.color == 'W'

    def play_card(self, card, hand):
        """Plays the a card"""
        if self.check_playable(card, self.top_card):
            hand.remove(card)
            self.top_card = card
    
    def ai_turn(self, hand):
        """Let's the 'AI' take their turn"""
        play = None
        for card in hand:
            if self.check_playable(card, self.top_card):
                play = card
        if play == None:
            self.draw_card(hand)
        else:
            self.play_card(play, hand)
    
    def check_win(self, x):
        """Checks to see if the game is won"""
        if x == '':
            if len(self.p1_hand) == 0:
                return 'Player 1 has won'
            elif len(self.p2_hand) == 0:
                return 'Player 2 has won'
            elif len(self.p3_hand) == 0:
                return 'Player 3 has won'
            elif len(self.p4_hand) == 0:
                return 'Player 4 has won'
            else:
                return False
            
