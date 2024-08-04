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

def show_computer_board():
    """ 
    Display the computer's board with hidden positons
    """
    print("\nComputer's Board")
    for row in range(5):
        print(hidden_computer_board[row])
    print('------------------------------------')

def is_valid_position(pos, size=10):
    """ 
    Check if the given position is valid within the board size
    """
    if len(pos) != 2:
        return False
    if pos[0] not in 'ABCDE' or not pos[1].isdigit():
        return False
    if int(pos[1]) < 1 or int(pos[1]) > size:
        return False
    return True

# Create the boards for player and computer
player_board = create_board(5, 10)
computer_board = create_board(5, 10)
hidden_computer_board = create_board(5, 10)

# Place the ships for the player and computer
for i in range(5):
    player_valid = False
    computer_valid = False

    while not player_valid:
        xy = input(f'Enter the position for your {i+1}• ship (A1 to E10): ').upper()
        if is_valid_position(xy) and xy not in player_positions:
            x = 'ABCDE'.index(xy[0])
            y = int(xy[1]) - 1
            player_board[x][y] = 1
            player_positions.append(xy)
            player_valid = True
        else:
            print("Invalid or occupied postion, try again.")
    
    while not computer_valid:
        x = randint(0, 4)
        y = randint(0, 4)
        xy = f'{chr(x + ord("A"))}{y + 1}'
        if xy not in computer_positions:
            computer_board[x][y] = 1
            computer_positions.append(xy)
            computer_valid = True

show_computer_board()
show_player_board()
