from random import randint
from colorama import Fore, Style, init

init()

# Initialization of variables
PLAYER_SCORE = 5
COMPUTER_SCORE = 5
TURN = 0
PLAYER_POSITIONS = []
COMPUTER_POSITIONS = []
PLAYER_GUESSES = []  # To track player's guesses
COMPUTER_GUESSES = []  # To track computer's guesses

BOARD_SIZE = 5
ROWS = 'ABCDE'

# PEP8: Constants use uppercase, and line lengths are limited to 79 characters

def create_board(size):
    """Create an empty game board."""
    return [['O'] * size for _ in range(size)]  # 'O' for unguessed positions


def display_board(board, is_player=True):
    """
    Display the board with row and column labels.
    is_player: If True, shows player's board; otherwise shows the computer's.
    """
    print("  1  2  3  4  5")
    for i, row in enumerate(board):
        row_label = ROWS[i]
        print(f"{row_label} {'  '.join(row)}")


def is_valid_position(pos, guesses, size=BOARD_SIZE):
    """
    Check if a given position is valid.
    - Ensures it's within the board's range.
    - Ensures it's not a repeated guess.
    """
    if len(pos) != 2:
        return False
    if pos[0] not in ROWS or not pos[1].isdigit():
        return False
    if int(pos[1]) < 1 or int(pos[1]) > size:
        return False
    if pos in guesses:
        return False  # Already guessed this position
    return True


def setup_board(board, player=False):
    """
    Place 5 ships randomly on the board for the player or the computer.
    """
    positions = []
    for i in range(5):
        valid = False
        while not valid:
            if player:
                pos = input(f'Enter the position for your {i+1}º ship (A1 to E5): ').upper()
            else:
                x = randint(0, 4)
                y = randint(0, 4)
                pos = f'{ROWS[x]}{y+1}'

            if is_valid_position(pos, positions):
                x = ROWS.index(pos[0])
                y = int(pos[1]) - 1
                board[x][y] = 'S'  # 'S' for ship
                positions.append(pos)
                valid = True
            elif player:
                print(Fore.RED + "Invalid or occupied position, try again." + Style.RESET_ALL)
    return positions


def update_guess_board(board, guess, hit):
    """Update the guess board with 'X' for hit and 'M' for miss."""
    x = ROWS.index(guess[0])
    y = int(guess[1]) - 1
    board[x][y] = 'X' if hit else 'M'  # 'M' for miss


def main_game_loop(player_board, computer_board, hidden_computer_board):
    """
    Main game loop for the battleship game.
    - Prevents repeated guesses.
    - Differentiates between hit/miss/unguessed.
    """
    global TURN, PLAYER_SCORE, COMPUTER_SCORE
    while PLAYER_SCORE > 0 and COMPUTER_SCORE > 0:
        if TURN % 2 == 0:  # Player's turn
            attack_pos = input(
                Fore.YELLOW + f'{player_name}, enter position to attack (A1 to E5): ' + Style.RESET_ALL
            ).upper()

            if is_valid_position(attack_pos, PLAYER_GUESSES):
                PLAYER_GUESSES.append(attack_pos)
                x = ROWS.index(attack_pos[0])
                y = int(attack_pos[1]) - 1

                if computer_board[x][y] == 'S':  # Ship hit
                    update_guess_board(hidden_computer_board, attack_pos, hit=True)
                    COMPUTER_SCORE -= 1
                    print(Fore.GREEN + "You hit a ship!" + Style.RESET_ALL)
                else:
                    update_guess_board(hidden_computer_board, attack_pos, hit=False)
                    print(Fore.RED + "You missed!" + Style.RESET_ALL)
                TURN += 1
            else:
                print(Fore.RED + "Invalid or repeated position, try again." + Style.RESET_ALL)
        else:  # Computer's turn
            while True:
                x = randint(0, 4)
                y = randint(0, 4)
                attack_pos = f'{ROWS[x]}{y+1}'

                if attack_pos not in COMPUTER_GUESSES:
                    COMPUTER_GUESSES.append(attack_pos)

                    if player_board[x][y] == 'S':  # Ship hit
                        player_board[x][y] = 'X'
                        PLAYER_SCORE -= 1
                        print(Fore.RED + f"The computer hit your ship at {attack_pos}!" + Style.RESET_ALL)
                    else:
                        player_board[x][y] = 'M'
                        print(f"The computer missed at {attack_pos}.")
                    TURN += 1
                    break

        display_board(hidden_computer_board, is_player=False)
        display_board(player_board)

        print(Fore.MAGENTA + f"{player_name}'s Remaining Ships: {PLAYER_SCORE}" + Style.RESET_ALL)
        print(Fore.BLUE + f"Computer's Remaining Ships: {COMPUTER_SCORE}" + Style.RESET_ALL)

    if PLAYER_SCORE == 0:
        print(f"{player_name}, you lost! The computer destroyed all your ships.")
    else:
        print(f"Congratulations, {player_name}! You destroyed all the computer's ships.")


# Get the player's name with validation
def get_player_name():
    """Ask for the player's name and ensure it is not left blank."""
    while True:
        name = input("Please enter your name: ").strip()
        if name:
            return name
        else:
            print(Fore.RED + "Name cannot be blank, please enter a valid name." + Style.RESET_ALL)


# Introduction and game setup
print("Welcome to the Battleship Game!")
print("You will place 5 ships on a 5x5 board.")
print("Try to destroy all the computer's ships before it destroys yours.")

player_name = get_player_name()

# Create boards
player_board = create_board(BOARD_SIZE)
computer_board = create_board(BOARD_SIZE)
hidden_computer_board = create_board(BOARD_SIZE)

# Setup boards
PLAYER_POSITIONS = setup_board(player_board, player=True)
COMPUTER_POSITIONS = setup_board(computer_board)

# Show initial boards
display_board(hidden_computer_board, is_player=False)
display_board(player_board)

# Start the main game loop
main_game_loop(player_board, computer_board, hidden_computer_board)
