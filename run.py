# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint
from colorama import Fore, Style, init 

#Initialize colorama
innit()

# Initialization of variables
player_score = 5
computer_score = 5
turn = 0  # The turn should start from 0
player_positions = []
computer_positions = []

def create_board(size):
    """
    Create a game board with the given number of rows and columns.
    """
    board = []
    for _ in range(size):
        board.append([0] * size)
    return board

def show_player_board():
    """
    Display the player's board.
    """
    print("\n{player_name}'s Board")
    for row in player_board:
        print(row)

def show_computer_board():
    """ 
    Display the computer's board with hidden positions.
    """
    print("\nComputer's Board")
    for row in range(5):
        print(hidden_computer_board[row])
    print('------------------------------------')

def is_valid_position(pos, size=10):
    """ 
    Check if the given position is valid within the board size.
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
        xy = input(f'Enter the position for your {i+1}º ship (A1 to E10): ').upper()
        if is_valid_position(xy) and xy not in player_positions:
            x = 'ABCDE'.index(xy[0])
            y = int(xy[1]) - 1
            player_board[x][y] = 1
            player_positions.append(xy)
            player_valid = True
        else:
            print("Invalid or occupied position, try again.")
    
    while not computer_valid:
        x = randint(0, 4)
        y = randint(0, 9)  # Correct range for the board
        xy = f'{chr(x + ord("A"))}{y + 1}'
        if xy not in computer_positions:
            computer_board[x][y] = 1
            computer_positions.append(xy)
            computer_valid = True

show_computer_board()
show_player_board()

# Main game loop
while True:
    if player_score == 0 or computer_score == 0:
        break
    else:
        if turn % 2 == 0:  # Player attacks
            attack_pos = input(
                'Enter the position you want to attack (A1 to E10): '
            ).upper()
            if is_valid_position(attack_pos):
                x = 'ABCDE'.index(attack_pos[0])
                y = int(attack_pos[1]) - 1
                if computer_board[x][y] == 1:
                    hidden_computer_board[x][y] = 'x'
                    computer_score -= 1
                    print('You hit a ship!')
                else:
                    print('You missed!')
                turn += 1
            else:
                print('Invalid position, try again.')
        else:  # Computer attacks
            x = randint(0, 4)
            y = randint(0, 9)  # Correct range for the board
            attack_pos = f'{chr(x + ord("A"))}{y + 1}'
            if player_board[x][y] == 1:
                player_board[x][y] = 'x'
                player_score -= 1
                print(f"The computer hit your ship at {attack_pos}!")
            else:
                print(f"The computer missed at {attack_pos}!")
            turn += 1
        
        show_computer_board()
        show_player_board()
        print("Player's Remaining Ships:", player_score)
        print("Computer's Remaining Ships:", computer_score)
    
if player_score == 0:
    print("You lost, the computer destroyed all your ships.")
else:
    print("Congratulations, you destroyed all the computer's ships.")
