''' Final Project - Uno

Runs the CLI for Uno

@author: Alex Miller (ajm94)
@date: Fall, 2021
'''

from uno import *

def check_command(command):
    """Check the command and runs the right code"""
    if command[0] == 'p':
        n = int(command[2:(len(command))])
        if game.check_playable(game.p1_hand[n], game.top_card):
            game.play_card(game.p1_hand[n], game.p1_hand)
        else:
            print(f'{game.p1_hand[n]} is not playable.')
            player_turn()
        
    if command == 'd':
        game.draw_card(game.p1_hand)

def player_turn():
    """Lets the player take their turn"""
    card_count = f'Player 1 - {len(game.p1_hand)}\nPlayer 2 - {len(game.p2_hand)}\nPlayer 3 - {len(game.p3_hand)}\nPlayer 4 - {len(game.p4_hand)}'
    
    i = 0
    while i < 10:
        print()
        i += 1
    
    print(turn)
    print(card_count)
    print()

    print(f'Top card - {game.top_card}\n')

    string = ''
    for card in game.player_cards(game.p1_hand):
        string += card + ' | '
    print(string)
    print()
    print(MENU)
    check_command(input('Command: '))
    
def check_win(x):
    """Checks to see if a player has won"""
    if x == '':
        x = game.check_win(x)

def take_turn(x):
    """Sees which player's turn it is and then runs their turn"""
    if x == 0:
        player_turn()
        check_win(message)
    elif x == 1:
        game.ai_turn(game.p2_hand)
        check_win(message)
    elif x == 2:
        game.ai_turn(game.p3_hand)
        check_win(message)
    elif x == 3:
        game.ai_turn(game.p4_hand)
        check_win(message)
    
game = Uno()
message = ''
turn = 0
reverse = False
MENU = 'p (card position) - Play card in the input\'s position\nd - Draw card'


while True:
    take_turn(turn)
    if game.top_card.num == 'R':
        if reverse:
            reverse = False
        else:
            reverse = True
    elif game.top_card.num == 'S':
        if reverse:
            turn = abs((turn - 1) % 4)
        else:
            turn = (turn + 1) % 4
    elif game.top_card.num == '+':
        if reverse:
            turn = abs((turn - 1) % 4)
        else:
            turn = (turn + 1) % 4
        if game.top_card.color == 'W':
            if turn == 0:
                game.draw_card(p1_hand)
                game.draw_card(p1_hand)
                game.draw_card(p1_hand)
                game.draw_card(p1_hand)
            elif turn == 1:
                game.draw_card(game.p2_hand)
                game.draw_card(game.p2_hand)
                game.draw_card(game.p2_hand)
                game.draw_card(game.p2_hand)
            elif turn == 2:
                game.draw_card(game.p3_hand)
                game.draw_card(game.p3_hand)
                game.draw_card(game.p3_hand)
                game.draw_card(game.p3_hand)
            elif turn == 3:
                game.draw_card(game.p4_hand)
                game.draw_card(game.p4_hand)
                game.draw_card(game.p4_hand)
                game.draw_card(game.p4_hand)

        else:
            if turn == 0:
                game.draw_card(p1_hand)
                game.draw_card(p1_hand)
            elif turn == 1:
                game.draw_card(game.p2_hand)
                game.draw_card(game.p2_hand)
            elif turn == 2:
                game.draw_card(game.p3_hand)
                game.draw_card(game.p3_hand)
            elif turn == 3:
                game.draw_card(game.p4_hand)
                game.draw_card(game.p4_hand)
    
    
    if reverse:
        turn = abs((turn - 1) % 4)
    else:
        turn = (turn + 1) % 4