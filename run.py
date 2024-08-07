from random import randint
from colorama import Fore, Style, init

init() 

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
    print(f"\n{player_name}'s Board")
    for row in player_board:
        print(row)


def show_computer_board():
    """
    Display the computer's board with hidden positions.
    """
    print("\nComputer's Board")
    for row in hidden_computer_board:
        print(row)
    print('------------------------------------')


def is_valid_position(pos, size=5):
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


def setup_boards():
    """
    Set up boards for the player and computer by placing ships.
    """
    global player_board, computer_board, hidden_computer_board

    player_board = create_board(board_size)
    computer_board = create_board(board_size)
    hidden_computer_board = create_board(board_size)

    for i in range(5):
        player_valid = False
        computer_valid = False

        while not player_valid:
            xy = input(f'Enter the position for your {i+1}º ship (A1 to E{board_size}): ').upper()
            if is_valid_position(xy, board_size) and xy not in player_positions:
                x = 'ABCDE'.index(xy[0])
                y = int(xy[1]) - 1
                player_board[x][y] = 1
                player_positions.append(xy)
                player_valid = True
            else:
                print("Invalid or occupied position, try again.")

        while not computer_valid:
            x = randint(0, 4)
            y = randint(0, 4)
            xy = f'{chr(x + ord("A"))}{y + 1}'
            if xy not in computer_positions:
                computer_board[x][y] = 1
                computer_positions.append(xy)
                computer_valid = True


def main_game_loop():
    """
    Main game loop for the battleship game
    """
    global turn, player_score, computer_score

    while True:
        if player_score == 0 or computer_score == 0:
            break
        else:
            if turn % 2 == 0:  # Player attacks
                attack_pos = input(
                    f'Enter the position you want to attack (A1 to E{board_size}), {player_name}: '
                ).upper()
                if is_valid_position(attack_pos, board_size):
                    x = 'ABCDE'.index(attack_pos[0])
                    y = int(attack_pos[1]) - 1
                    if computer_board[x][y] == 1:
                        hidden_computer_board[x][y] = 'X'
                        computer_score -= 1
                        print(Fore.GREEN + 'You hit a ship!' + Style.RESET_ALL)
                    else:
                        print(Fore.RED + 'You missed!' + Style.RESET_ALL)
                    turn += 1
                else:
                    print('Invalid position, try again.')
            else:  # Computer attacks
                x = randint(0, 4)
                y = randint(0, 4)  # Correct range for the board
                attack_pos = f'{chr(x + ord("A"))}{y + 1}'
                if player_board[x][y] == 1:
                    player_board[x][y] = 'X'
                    player_score -= 1
                    print(Fore.RED + f"The computer hit your ship at {attack_pos}!" + Style.RESET_ALL)
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


# Introduction
print("Welcome to the Battleship Game!")
print("You will place 5 ships on a 5x5 board.")
print("Each ship occupies one cell on the board.")
print("You will take turns with the computer to attack each other's ships.")
print("The goal is to destroy all of the opponent's ships.")

# Get the player's name
player_name = input("Please enter your name: ")

# Board size
board_size = 5

# Setup boards with ships
setup_boards()

# Show initial boards
show_computer_board()
show_player_board()

# Start the main game loop
main_game_loop()
