"""
Creating a cli version of the tic-tac-toe game
"""
from os import system


# r1 , r2 and r3 are the position on the board

r1 = ['1', '2', '3']
r2 = ['6', '5', '4']
r3 = ['7', '8', '9']



player1 = input('Player 1 0 >> ') or None
player2 = input('Player 2 X >> ') or None

# To set the current player
play = player1

# Check what's being played
played = {
    player1 :[],
    player2 :[]
}
# This is to prevent duplicate entries
banned = []

# Maps the numbers to positions
positions = {
    1:'r1',
    2:'r1',
    3:'r1',
    4:'r2',
    5:'r2',
    6:'r2',
    7:'r3',
    8:'r3',
    9:'r3'
}

          
# Row checks for horizontal wins
def row(lst, which_player):
    won = 0
    for first in lst:
        if first == players.get(which_player):
            won += 1
        else:
            break
    if won == 3:
        return True
    return None

# Checks vertical wins
def top_down(which_player):
    won = 0
    value = players.get(which_player)
    positions = list(zip(r1,r2,r3))
    for position in positions:
        for pos in position:
            if pos == value:
                won +=1
            else:
                break
    if won == 3:
        return True
    return None

# checks diagonals
def diagonals(which_player):
    value = players.get(which_player)
    if value == r2[1]:
        while True:
            if r1[0] == value and r3[2] == value and r2[1] == value:
                print('1st', r1[0] == value and r3[2] == value and r2[1] == value)
                print(r1[2] == value and r3[0] == value and r2[1] == value)
                return True
            if r1[2] == value and r3[0] == value and r2[1] == value:
                print('2nd')
                return True
            break
        return None
    else:
        return None
    
# Main check win function.
def check_win(which_player):
    if len(played.get(which_player)) >= 3:
        print(top_down(which_player), 'top down')
        while True:
            if row(r1, which_player) or row(r2, which_player) or row(r3, which_player):
                print('row')
                return True
            if top_down(which_player):
                print('top down')
                return True
            if diagonals(which_player):
                print('diagonals')
                return True
            else:
                return None

# change the current player to the next
def change_player():
    global play
    if play == player1:
        play = player2
    else:
        play = player1
def clear_terminal():
    # Clear the terminal to print the new board
    system('cls')



while True:
    board = f'''
        ___________________
        |  {r1[0]}  |  {r1[1]}  |  {r1[2]}  |
        ___________________
        |  {r2[0]}  |  {r2[1]}  |  {r2[2]}  |
        ___________________
        |  {r3[0]}  |  {r3[1]}  |  {r3[2]}  |
        ___________________
    '''
    print(board)

    # Players characters
    players = {
        player1: '0',
        player2: 'X',
    }

    # prevents empty usernames

    if player1 and player2 is not None:
        place= int(input(f'Enter Number {play} >> '))

        # prevent a word from being chosen twice
        if place not in banned:
            banned.append(place)
        
        # first row positions
            if positions.get(place) == 'r1':
                r1[r1.index(str(place))] = players.get(play)
                played[play].append(f'r1[{place}]')
                change_player()

        # second row positions 
            if positions.get(place) == 'r2':
                r2[r2.index(str(place))] = players.get(play)
                played[play].append(f'r2[{place}]')
                change_player()
        
        # third row positions
            if positions.get(place) == 'r3':
                r3[r3.index(str(place))] = players.get(play)
                played[play].append(f'r3[{place}]')
                change_player()

        # You can only win when there's 5 or more plays, so it starts checking wins after the 5 plays
            if len(played.get(player1)) + len(played.get(player2)) >= 5:

                clear_terminal()
                board = f'''
                    ___________________
                    |  {r1[0]}  |  {r1[1]}  |  {r1[2]}  |
                    ___________________
                    |  {r2[0]}  |  {r2[1]}  |  {r2[2]}  |
                    ___________________
                    |  {r3[0]}  |  {r3[1]}  |  {r3[2]}  |
                    ___________________
                '''
                if check_win(player2):
                    print(f'{player2},won')
                    print(board)
                    break
                if check_win(player1):
                    print(f'{player1} won') 
                    print(board)
                    break
            if len(played.get(player1)) + len(played.get(player2)) == 9:
                clear_terminal()
                print('This is a draw')
                break
              
        else:
            print('Place is already filled')
    # clear_terminal()
    



