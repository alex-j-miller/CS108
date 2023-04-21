''' Final Project - GUI

Presents the GUI to the user

@author: Alex Miller (ajm94)
@date: Fall, 2021
'''
from uno import *
from guizero import *
from time import sleep

app = App(title='UNO', layout='grid', height= 300, width= 650, bg= 'white')
game = Uno()

class GUI:
    def __init__(self):
        """Initializes the GUI"""
        
        self.box = Box(app, grid= [1,2], layout='grid')
        
        self.p2 = Text(app, text=f'Player 2: {len(game.p2_hand)} cards', grid= [0,0])
        self.p3 = Text(app, text=f'Player 3: {len(game.p3_hand)} cards', grid= [1,0])
        self.p4 = Text(app, text=f'Player 4: {len(game.p4_hand)} cards', grid= [2,0])
        self.top_card = Text(app, text=game.top_card, grid=[1,1])
        PushButton(app, text='Draw', grid= [0,1], command= self.player_turn, args= [None, True])
        self.print_cards(game.p1_hand)
        self.turn = 0
        self.turns = [0,1,2,3]
        self.reverse = False
        
        
    
    def player_turn(self, card, draw):
        """Let's the player take a turn then does the other turns"""
        if not draw:
            if game.check_playable(card, game.top_card):
                self.play_card(card)
            else:
                self.draw_card()
        else:
            self.draw_card()
        
        if game.top_card.num == '+':
            if game.top_card.color == 'W':
                game.draw_card(game.p2_hand)
                game.draw_card(game.p2_hand)
                game.draw_card(game.p2_hand)
                game.draw_card(game.p2_hand)
            else:
                game.draw_card(game.p2_hand)
                game.draw_card(game.p2_hand)
            
        game.ai_turn(game.p2_hand)
        self.p2.destroy()
        self.p2 = Text(app, text=f'Player 2: {len(game.p2_hand)} cards', grid= [0,0])
        self.top_card.destroy()
        self.top_card = Text(app, text=game.top_card, grid=[1,1])
        
        if game.top_card.num == '+':
            if game.top_card.color == 'W':
                game.draw_card(game.p3_hand)
                game.draw_card(game.p3_hand)
                game.draw_card(game.p3_hand)
                game.draw_card(game.p3_hand)
            else:
                game.draw_card(game.p3_hand)
                game.draw_card(game.p3_hand)

        game.ai_turn(game.p3_hand)
        self.p3.destroy()
        self.p3 = Text(app, text=f'Player 3: {len(game.p3_hand)} cards', grid= [1,0])
        self.top_card.destroy()
        self.top_card = Text(app, text=game.top_card, grid=[1,1])
        
        if game.top_card.num == '+':
            if game.top_card.color == 'W':
                game.draw_card(game.p4_hand)
                game.draw_card(game.p4_hand)
                game.draw_card(game.p4_hand)
                game.draw_card(game.p4_hand)
            else:
                game.draw_card(game.p4_hand)
                game.draw_card(game.p4_hand)

        game.ai_turn(game.p4_hand)
        self.p4.destroy()
        self.p4 = Text(app, text=f'Player 4: {len(game.p4_hand)} cards', grid= [2,0])
        self.top_card.destroy()
        self.top_card = Text(app, text=game.top_card, grid=[1,1])
        
        if game.top_card.num == '+':
            if game.top_card.color == 'W':
                game.draw_card(game.p1_hand)
                game.draw_card(game.p1_hand)
                game.draw_card(game.p1_hand)
                game.draw_card(game.p1_hand)
            else:
                game.draw_card(game.p1_hand)
                game.draw_card(game.p1_hand)
        
        
        
    
    def play_card(self, card):
        """Plays the card the in received"""
        if game.check_playable(card, game.top_card):
            game.play_card(card, game.p1_hand)
            self.top_card.destroy()
            self.top_card = Text(app, text=game.top_card, grid=[1,1])
        self.print_cards(game.p1_hand)
        
    
    def print_cards(self, hand):
        """Prints the players cards"""
        self.box.destroy()
        self.box = Box(app, grid= [1,2], layout='grid')
        i = 0
        for card in hand:
            PushButton(self.box,
                       text=card,
                       grid=[i%5,i//5],
                       command= self.player_turn,
                       args= [card, False]
                       )
            i += 1
    def draw_card(self):
        """Makes the player draw a card"""
        game.draw_card(game.p1_hand)
        self.print_cards(game.p1_hand)

gui = GUI()
app.display()