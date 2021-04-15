#!/usr/bin/env python
# coding: utf-8

# # Buildning luffarschack with functions

# In[1]:


print("|  |")
print(" " + board[1] " ")





# In[ ]:


def display_board(board):
    
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


# In[ ]:


display_board(["O", "X", "X", "O", "O", "X", "X", "X", "O", "O"])


# In[ ]:


def player_input():
    """function takes player input and assigns marker as X or O"""
    marker=""
    
    while not (marker =="X" or marker =="O"):
        marker = input("player 1: Would you like to be X or O").upper()
        
    if marker =="X":
        return ("X", "O")
    else:
        return ("O", "X")


# In[ ]:


player_input()


# In[ ]:


def place_marker(board, marker, position):
    """"takes the board object, a marker X or O and take position (1-9) and assigns it to the board"""
    
    board[position] = marker


# In[ ]:


test_board = ["O", "X", "X", "X", "O", "X", "X", "X", "O", "O"]

place_marker(test_board, ")", 5)


# In[ ]:


display_board(test_board)


# In[ ]:


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark)) 







# In[ ]:


win_check(test_board, "X")


# In[ ]:


import random as rd

def choose_first():
    if rd.randint(0,1) == 0:
        return "player2"
    else:
        return "player1"


# In[ ]:


def space_check(board, position):
    """return a bool indicating wether a space on the board is available"""
    return board[position] == " "


# In[ ]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
    


# In[ ]:


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("choose your next move: (1,9) "))
        
    return position


# In[ ]:


def replay():
    return input("would you like to play again? Enter Yes or No").lower().stratswith("y")


# In[71]:


print("welcome to another fucking life deciding game")

while True:

    # resetting the board
    theboard = [" "] *10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + "will go first")
    
    play_game = input("Are you ready to rumble? Enter Yes or No.")
    
    if play_game.lower()[0] == "y":
        game_on = True
    else:
        game_on = False
        
    while game_on:
    
        if turn == "player1":
            
            
            
            #player1 1st turn
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player1_marker, position)
        
            if win_check(theboard, player1_marker):
                display_board(theboard)
                print("Gratulerar min vän, du vinner")
                game_on = False
                
            else: 
                if full_board_check(theboard):
                    display_board(theboard)
                    print("Spelet är oavgjort")
                    break
                    
                else:
                
                    turn = "player2"
        else:
        #Players2s turn
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player2_marker, position)
        
            if win_check(theboard, player2_marker):
                display_board(theboard)
                print("Gratulerar min vän, du vinner")
                game_on = False
                
            else: 
                if full_board_check(theboard):
                    display_board(theboard)
                    print("Spelet är oavgjort")
                    break
                    
                else:
                    turn = "player1"
                
                
                
    if not replay():
        break
        
        
                

            
        
    
    


# In[ ]:




