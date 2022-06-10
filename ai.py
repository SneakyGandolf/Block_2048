#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Artificial Intelligence for Block-2048


author: J. Hollingsworth, D. Hutchings, and Caelin Bahner

"""

import random

# Validation Functions #

# return True if board has the same number of columns in every row
def is_rectangle(board):
    row_1 = len(board[0])
    for i in board:
        if len(i) != row_1:
            return False
    return True

# return True if every number in board is a power of 2 up to 2048 inclusive
def is_2048_data(board):
    for i in board:
        for j in i:
            if j != 0 and j != 2 and j != 4 and j != 8 and j != 16 and j != 32 and j != 64 and j != 128 and j != 256 and j != 512 and j != 1024 and j != 2048:           
                return False 
    return True

# return True if there are no zeroes below non-zeroes in a column
def no_holes(board):
    for i,x in enumerate(board):
        if i == (len(board)-1):
            break     
        for j,y in enumerate(x):
            if board[i][j] == 0 and board[i+1][j] > 0:
                return False
    return True

# return True if there are no numbers adjacent that are the same
def matches_resolved(board):
    for i,x in enumerate(board):
        if i == (len(board)-1):
            break     
        for j,y in enumerate(x):
            if board[i][j] != 0 and board[i+1][j] != 0 and board[i][j] == board[i+1][j]:
                return False
            if j == (len(x)-1):
                break  
            if board[i][j] != 0 and board[i][j+1] != 0 and board[i][j] == board[i][j+1]:   
                return False
            if board[i+1][j] != 0 and board[i+1][j+1] != 0 and board[i+1][j] == board[i+1][j+1]:   
                return False
    return True



# AI Functions #

# return the value of the topmost block in the given column
def get_topmost_block(col, board):
    if board[-1][col] != 0:
        return -1
    j = len(board)-1
    for i in range(len(board)):    
        if board[j][col] != 0:
            return board[j][col] 
        j -= 1
    return 0

# play in a random column
def play_randomly(board):
    return random.randint(0,len(board[0])-1)


# play in a random column (avoid playing in a full column)
def play_randomly_avoid_full_columns(board):

        i = 0
        while i == 0:
            col = random.randint(0, len(board[0])-1)
            if board[-1][col] == 0:
               return col


# play in a column where the topmost block will match if possible,
# otherwise play in a random column (avoid playing in a full column)
def play_vertical_stack_matcher(block, board):
    
    
    for i in range(len(board[0])):
        if block == get_topmost_block(i,board):
            return i 
    return play_randomly_avoid_full_columns(board)



# play in a column where the topmost block will match,
# if no match possible, play in a column that will
#         stack a lower number on top of a higher number
# otherwise play in a random column (avoid playing in a full column)
def play_intelligent_vertical_stack_matcher(block, board):

    for i in range(len(board[0])):
        if block == get_topmost_block(i,board):
            return i 
    for i in range(len(board[0])):    
        if block < get_topmost_block(i,board):
            return i 
        
    return play_randomly_avoid_full_columns(board)
            
def get_left_value(block,col,board):
    desired_sqre = get_topmost_block(col+1,board)
    j = len(board)-1
    col = len(board[0])-1
    for i in range(len(board[0])):    
        if board[j-1][col+1] == block:
            return True
        j -= 1
        return False
def get_right_value(block,board):    
    j = len(board)-1
    col = len(board[0])-1
    for i in range(len(board[0])):
#        if board[j][col] == board[-1][col] or board[j][col] == board[j][-1]:
        if board[j+1][col+1] == block:
            return True
        j -= 1
        col -= 1
        return False
        

#AI that plays better than play_intelligent_vertical_stack_matcher()
def play_my_awesome_logic(block,board):
    for i in range(len(board[0])):
        if block == get_topmost_block(i,board):
            return i 
    for i in range(len(board[0])):    
        if block < get_topmost_block(i,board):
            return i 
#ai looks horizontally to determine matches not only above    
    for i in range(len(board[0])):
        if get_right_value(block, board) == True or get_left_value(block, board) == True:
            return i
    return play_randomly_avoid_full_columns(board)

#NOTE: My ai looks horizontally to determine if there is a potential match not only vertically. 
    

# play interactively -- this code is complete -- no changes needed
def play_console_control(block, board):
    num_cols = len(board[0])
    col = int(input("Drop " + str(block) + " in which column: "))

    # ask again if given an invalid column
    while col < 0 or col >= num_cols:
        col = int(input("Drop " + str(block) + " in which column: "))

    return col



def strategy(block, on_deck, board):
    # input()  # uncomment this line to pause the game after every block drop (debugging)
    #return play_console_control(block, board)    # interactive
    #return play_randomly(board)
    #return play_randomly_avoid_full_columns(board)
    #return play_vertical_stack_matcher(block, board)
    return play_intelligent_vertical_stack_matcher(block, board)
    #return play_my_awesome_logic(block, on_deck, board)


if __name__ == "__main__":
    import block_2048
    block_2048.main()
