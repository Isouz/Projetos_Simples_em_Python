#################
## TIC TAC TOE ##
#################

import os
from time import sleep


def print_board(board):
       print('=' * 14)
       print()
       print(f"  {board[0]} | {board[1]} | {board[2]} ")
       print(" ---+---+---")
       print(f"  {board[3]} | {board[4]} | {board[5]} ")
       print(" ---+---+---")
       print(f"  {board[6]} | {board[7]} | {board[8]} ")
       print()
       print('=' * 14)
       print()


def valid_input():  
    while True:
        try:
            num = int(input('Position: '))
            if num < 1 or num > 9:
                print('out of range')
                print()
                sleep(1)
            elif num in played:
                print('already played')
                sleep(1)
            else:
                return num
        except:
            print('Not a number')
            print()
            sleep(1)


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
       

def victory_animation(player):
    for num in range(3):
        clear()
        print_board(board)
        print(f"{green}--- Player {player} won! ---{clear_color}")
        sleep(0.5)
        clear()
        print_board(board)
        sleep(0.5)
    print(f"{green}--- Player {player} won! ---")
    print(f'''
  ._==_==_=_. 
.-\:       /-. 
| (|:.     |) | 
 '-|:.     |-'
   \::.    /
    '::. .' 
      ) ( 
    _.' '._ 
   `"""""""` 
    {clear_color}''')
 
    
def check_victory(board, player):
    # check rows
    for num in [0, 3, 6]:
        if board[num] == player and board[num + 1] == player and board[num + 2] == player:
            victory_animation(player)
            sleep(2)
            return True
         
    # check columns
    for num in range(3):
        if  board[num] == player and  board[num + 3] == player and  board[num + 6] == player:
            victory_animation(player)
            sleep(2)
            return True
        
    # check diagonals
    if board[0] == player and board[4] == player and board[8] == player:
         victory_animation(player)
         sleep(2)
         return True
    elif board[2] == player and board[4] == player and board[6] == player:
         victory_animation(player)
         sleep(2)
         return True
    else:
         return False


def draw_animation(board, player):
    for num in range(3):
        clear()
        print_board(board)
        sleep(0.5)
        print(f"""{yellow}
 ____                     
|  _ \ _ __ __ ___      __
| | | | '__/ _` \ \ /\ / /
| |_| | | | (_| |\ V  V / 
|____/|_|  \__,_| \_/\_/  
        {clear_color}""")
        sleep(0.5)
    
    
# cores
green = '\033[32m'
yellow = '\033[33m'
clear_color = '\033[m'

stop_match = False   
current_player = 'X'  

played = []
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']   
ex_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# main looping
while stop_match == False:  
    clear()
    
    print('Type the position to play:')
    print_board(ex_board)
    
    print(f'{yellow}>> Player: {clear_color}{current_player}')
    print_board(board)
    
    if ' ' not in board:
        draw_animation(board, current_player)
        break
    
    position = valid_input()
    played.append(position)
    board[position - 1] = current_player
    ex_board[position -1] = ' '
    
    stop_match = check_victory(board, current_player)
    
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'            
           

# Developed by Igor Souza - GitHub: github.com/isouz
