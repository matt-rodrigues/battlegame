# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint

# Initialization of variables
player_score = 5
computer_score = 5
turn = 5
player_positions =[]
computer_positions = []

def create_board(rows, colus):
    """
    Creating a game board with the given numbers of rows and columns
    """
    board = []
    for i in range(rows):
        board.append(cols * [0])
    return board

def show_player_board():
    """
    Display the player's board
    """
    print("\nPlayer's Board")
    for row in range(5):
        print(player_board[row])
    