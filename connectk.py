import os
import random

# Configuration dictionary for each new game of connect4/connectk
CONFIG = {
    "game": "",  # ["connect4", "connectk"]
    "rows": 0,
    "columns": 0,
    "win_pieces": 0,  # How many pieces need to be connected in order to win
    "human_players": 0,  # No. of human players
    "cpu_players": 0,  # No. of CPUs
    "total_players": 0,
    "cpu_levels": [],  # List of length cpu_players with a difficulty in ["easy", "medium", "hard"] for each cpu
    "first_turn": [],  # ["humans", "cpus", "mix"]
}


def clear_screen():
    # Command for clearing the terminal line
    os.system("cls" if os.name == "nt" else "clear")


def validate_input(prompt, valid_inputs):
    """
    Repeatedly ask user for input until they enter an input
    within a set valid of options.

    :param prompt: The prompt to display to the user, string.
    :param valid_inputs: The range of values to accept, list
    :return: The user's input, string.
    """
    while True:

        user_input = input(prompt)
        if user_input in valid_inputs:
            return user_input
        else:
            print("Invalid inputs, please try again.")
            pass


def print_rules(game):
    """
    Prints the rules of the game.

    :param game: The type of game selected: "connect4" or "connectk"
    :return: None
    """
    if game == "connect4":
        print("================= Rules =================")
        print("Connect 4 is a two-player game where the")
        print("objective is to get four of your pieces")
        print("in a row either horizontally, vertically")
        print("or diagonally. The game is played on a")
        print("6x7 grid. The first player to get four")
        print("pieces in a row wins the game. If the")
        print("grid is filled and no player has won,")
        print("the game is a draw.")
        print("========================================")
    elif game == "connectk":
        print("================= Rules ======================")
        print("** Please read the rules of Connect 4 first **")
        print("Connect K runs on the same basis of connect 4,")
        print("but you get to choose how hard the game is!")
        print("You can choose the:")
        print("- The number of rows of the game board")
        print("- The number of columns of the game board")
        print("- The number of pieces that need to be")
        print("  connected in order to win")
        print("- The number of human players")
        print("- The number and level of CPU players")
        print("=============================================")


def create_board(rows, columns):

    """
    Returns a 2D list of {rows} rows and {columns} columns to represent
    the game board. Default cell value is 0.

    :param rows: The configured number of rows
    :param columns: The configured number of columns
    :return: A 2D list of 6x7 dimensions.
    """
    board = [
        [0 for _ in range(columns)] for _ in range(rows)
    ]  # List of lists filled with 0
    return board


def print_board(board, config):
    """
    Prints the game board to the console.

    :param board: The game board, 2D list of column x row dimensions.
    :param config: The configuration dictionary of the current game.
    :return: None
    """
    rows = config["rows"]
    columns = config["columns"]

    if config["game"] == "connect4":  # 6x7 board
        # Board layout
        print("========== Connect4 =========")
        print("Player 1: X       Player 2: O\n")
        print("  1   2   3   4   5   6   7")
        print(" --- --- --- --- --- --- ---")
        for row in range(rows):
            print("|", end="")
            for col in range(columns):
                if board[row][col] == 1:
                    print(" X |", end="")
                elif board[row][col] == 2:
                    print(" O |", end="")
                elif board[row][col] == 0:
                    print("   |", end="")
            print("\n --- --- --- --- --- --- ---")
        print("=============================")

    else:  # Connect K
        # To keep alignment
        game_name = " ConnectK " if columns % 2 == 1 else " Connect K "
        # Double line is used to compute length of all other lines
        double_line = ""
        player_count = config["human_players"] + config["cpu_players"]
        player_symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(columns):
            if i == 0 and columns % 2 == 1:
                double_line += "====="
            else:
                double_line += "===="
        double_line += "="
        # Always even so always return an int
        partial_line = double_line[: int((len(double_line) / 2) - (len(game_name) / 2))]
        player_line = "| Players: "

        # Use alphabetical letters as symbols for first 26 players and use the player number for the rest
        for i in range(player_count):
            if i < 26:
                player_line += player_symbols[i]
            else:
                player_line += i

            # Add commas if not last player
            if i != player_count - 1:
                player_line += ", "
            else:
                for i in range(len(player_line), len(double_line)):
                    if i == len(double_line) - 1:
                        player_line += "|"
                    else:
                        player_line += " "

        single_line = double_line.replace("=", "-")

        # Start with two spaces to account for left line going down
        column_numbers = "  "
        column = 1
        for i in range(len(double_line)):
            if column > columns:
                break
            elif i % 4 == 0:  # Spacing between numbers necessary
                column_numbers += str(column)
                column += 1
            elif column <= 9:
                column_numbers += " "
            else:  # Double digits
                if (i + 1) % 4 == 0:
                    # Remove last space to account for extra digit
                    continue
                else:
                    column_numbers += " "

        dotted_line = ""
        for i in range(
            len(double_line) - 1
        ):  # -1 because last column should always be 0
            if i == 0 or i % 4 == 0:
                dotted_line += " "
            else:
                dotted_line += "-"

        print(partial_line, end="")
        print(game_name, end="")
        print(partial_line)

        print(player_line)
        print(single_line)
        print(column_numbers)
        print(dotted_line)
        for row in range(rows):
            print("|", end="")
            for column in range(columns):
                if board[row][column] == 0:
                    print("   |", end="")
                elif board[row][column] <= 26:
                    print(f" {player_symbols[board[row][column] - 1]} |", end="")
                else:
                    print(f" {board[row][column]}|", end="")
            print("\n" + dotted_line)
        print(double_line)


def drop_piece(board, player, column):
    """
    Drops a piece into the game board in the given column.
    Please note that this function expects the column index
    to start at 1.

    :param board: The game board, 2D list of rows x columns dimensions.
    :param player: The player dropping the piece, int.
    :param column: The index of column to drop the piece into, int.
    :return: True if piece was successfully dropped, False if not.
    """
    # Iterate through board from bottom up
    if 1 <= column <= len(board[0]):
        for row in reversed(board):
            # Drop player piece in the lowest free space
            if row[column - 1] == 0:  # Column is 1 indexed
                row[column - 1] = player
                return True
    # If all spaces are filled
    return False


def execute_player_turn(player, board):
    """
    Prompts user for a legal move given the current game board
    and executes the move.

    :return: Column that the piece was dropped into, int.
    """
    while True:
        column = int(
            validate_input(
                f"Player {player}, please enter the column that you would like to drop your piece into: ",
                [str(i) for i in range(1, len(board[0]) + 1)],
            )
        )
        if drop_piece(board, player, column):
            return column
        else:
            print("Invalid move, try again.")

def end_of_game(board, config):
    """
    Checks if the game has ended with a winner
    or a draw.

    :param board: The game board, 2D list of a rows x b columns.
    :return: 0 if game is not over, the turn of the player that wins, or 101 if it's a draw.
    """

    # * Win Check
    def win(string):
        if config["game"] == "connect":
            if "1111" in string:
                return 1
            elif "2222" in string:
                return 2
        win_string = ""
        for player in range(1, config["total_players"] + 1):
            for _ in range(config["columns"]):
                if len(win_string) < config["win_pieces"]:
                    win_string += str(player)
            if win_string in string:
                return player

    # * Rows -> Strings
    for row in board:
        row_str = "".join([str(i) for i in row])
        # If there's a win return the winner
        exists = win(row_str)
        if exists:
            return exists

    # To check for draw further down
    filled_slots = True
    # * Columns -> Strings
    for i in range(len(board[0])):  # Length of each row in original board
        column_str = ""
        # Concatenate elements of ith index from each row into a string
        for row in board:
            column_str += str(row[i])
            # If empty spaces then won't be a draw
            if row[i] == 0:
                filled_slots = False
        exists = win(column_str)
        if exists:
            return exists

    # * Diagonals -> Strings
    if config["game"] == "connect4":
        def diagonal_check(board):
            for col in range(3, len(board[0])):  # 3-6
                # Second half from right-most column down
                if col == 6:
                    for row in range(3):  # 0-2
                        diagonal_str = ""
                        i = row
                        j = col
                        while i < col and j >= row:
                            diagonal_str += str(board[i][j])
                            i += 1
                            j -= 1
                        exists = win(diagonal_str)
                        if exists:
                            return exists
                # First half from left most relevant column
                else:
                    diagonal_str = ""
                    row = 0
                    i = row
                    j = col
                    # Do this until row and column number are switched
                    while i <= col and j >= row:
                        try:
                            diagonal_str += str(board[i][j])
                        except IndexError:
                            pass
                        j -= 1
                        i += 1
                    exists = win(diagonal_str)
                    if exists:
                        return exists

        # Diagonal /
        exists = diagonal_check(board)
        if exists:
            return exists  # Returning the value from win() to main
        # Diagonal \
        flipped_board = [row for row in reversed(board)]
        exists = diagonal_check(flipped_board)
        if exists:
            return exists

    # * Keep Playing or Draw
    if filled_slots:
        return 101  # All slots are filled so draw
    else:
        return 0  # There are empty slots left so keep playing

def cpu_player_easy(board, player, config):
    """
    Executes a move for the CPU on easy difficulty. This function
    plays a randomly selected column.

    :param board: The game board, 2D list of RxC dimensions.
    :param player: The player whose turn it is, integer value between 2 and 100.
    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below
    while True:
        random_column = random.randint(1, config["columns"])
        if drop_piece(board, player, random_column):
            return random_column


def cpu_player_medium(board, cpu_player, config):
    """
    Executes a move for the CPU on medium difficulty.
    It first checks for an immediate win and plays that move if possible.
    If no immediate win is possible, it checks for an immediate win
    for the opponent and blocks that move. If neither of these are
    possible, it plays a random move.

    :param board: The game board, 2D list of RxC dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """

    # Check for any possibility of win
    for col_index in range(len(board[0])):
        cpu_move = col_index + 1
        new_board = [row[:] for row in board]
        if drop_piece(new_board, cpu_player, cpu_move):  # Simulate drop for self
            if end_of_game(new_board, config) == cpu_player:
                drop_piece(board, cpu_player, cpu_move)  # Do a real drop
                return cpu_move

    # Check for any possibility of loss
    for opponent in range(1, config["total_players"] + 1):
        for col_index in range(len(board[0])):
            opponent_move = col_index + 1
            new_board = [row[:] for row in board]
            if drop_piece(
                new_board, opponent, opponent_move
            ):  # Simulate drop for opponent
                if (
                    end_of_game(new_board, config) == opponent
                ):  # If that drop wins for the opponent
                    cpu_move = opponent_move
                    drop_piece(
                        board, cpu_player, cpu_move
                    )  # Block that drop with cpu move
                    return cpu_move

    # If no move to block or win
    while True:
        cpu_move = random.randrange(1, config["columns"])  # random place to drop
        if drop_piece(board, cpu_player, cpu_move):
            return cpu_move


def cpu_player_hard(board, player, config):
    # Configure cpu hard to be the same as cpu medium for now
    return cpu_player_medium(board, player, config)

def run_game(board, config):
    """
    Executes the logic needed to run a game of ConnectK
    """

    if config["game"] == "connect4":
        exists_cpu = False
        if config["cpu_players"] == 1: # Human vs CPU
            exists_cpu = True
            difficulty = config["cpu_levels"][0]
            if config["first_turn"] == "humans":
                human = 1
                cpu = 2
            elif config["first_turn"] == "cpus":
                cpu = 1
                human = 2
            else:
                human = random.randint(1, 2)
                cpu = 2 if human == 1 else 1

        while True:
            clear_screen()
            game_status = end_of_game(board, config)
            if game_status == 0:
                for turn in range(1, 3):
                    print_board(board, config)
                    if not exists_cpu:
                        print(f"Your move, Player {turn}!")
                        move = execute_player_turn(turn, board)
                    else: # exists_cpu == True
                        if turn == human:
                            print("Your move, Player!")
                            move = execute_player_turn(turn, board)
                        elif turn == cpu:
                            if difficulty == "easy":
                                print( 
                                    f"It's Player {turn}'s turn, this one might get lucky..."
                                )
                                move = cpu_player_easy(board, turn, config)
                            elif difficulty == "medium":
                                print(
                                    f"It's Player {turn}'s turn, don't underestimate them!"
                                )
                                move = cpu_player_medium(board, turn, config)
                            elif difficulty == "hard":
                                print(
                                    f"It's Player {turn}'s turn, think you can beat them? Think again"
                                )
                                move = cpu_player_hard(board, turn, config)
                    
                    print(f"Player {turn}'s move is {move}")
            # If game is over
            else:
                break
        if game_status == "101":
            print("It's a draw!")
        else:
            print(f"Player {game_status} wins!")
            
    elif config["game"] == "connectk":
        # Order of players and player type
        order = {}

        if config["first_turn"] == "humans":
            for turn in range(1, config["total_players"] + 1):
                if turn <= config["human_players"]:  # Turns starting at 1
                    order[turn] = "human"
                else:  # For cpu turns
                    cpu_turn = (
                        turn - config["human_players"] - 1
                    )  # Starting from 0 to compute difficulty for each cpu
                    order[turn] = config["cpu_levels"][cpu_turn]
        elif config["first_turn"] == "cpus":
            for turn in range(1, config["total_players"] + 1):
                if turn <= config["cpu_players"]:
                    order[turn] = config["cpu_levels"][
                        turn - 1
                    ]  # Each turn that is a cpu will have a difficulty attached to it
                else:  # Human cpus
                    order[turn] = "human"
        else:  # Randomized order
            cpu_turn = 0
            human_turn = 0
            for turn in range(1, config["total_players"] + 1):
                is_human_turn = random.choice([True, False])
                if is_human_turn and human_turn < config["human_players"]:
                    order[turn] = "human"
                    human_turn += 1
                elif cpu_turn < config["cpu_players"]:  # CPU turn
                    order[turn] = config["cpu_levels"][cpu_turn]
                    cpu_turn += 1
                else:  # Human turn anyway if cpus all cpus are assigned a turn
                    order[turn] = "human"
                    cpu_turn += 1

        # Go through order
        while True:
            clear_screen()
            game_status = end_of_game(board, config)
            if game_status == 0:
                for turn in range(1, config["total_players"]):
                    print_board(board, config)
                    if order[turn] == "human":
                        print(f"Your move, Player {turn}!")
                        move = execute_player_turn(turn, board)
                    elif order[turn] == "easy":
                        print(
                            f"It's Player {turn}'s turn, this one might get lucky..."
                        )
                        move = cpu_player_easy(board, turn, config)
                    elif order[turn] == "medium":
                        print(
                            f"It's Player {turn}'s turn, don't underestimate them!"
                        )
                        move = cpu_player_medium(board, turn, config)
                    else:  # cpu hard
                        print(
                            f"It's Player {turn}'s turn, think you can beat them? Think again"
                        )
                        move = cpu_player_hard(board, turn, config)
                    print(f"Player {turn}'s move was {move}")
            else:
                break
        if game_status == 101:
            print("It's a draw!")
        else:
            print(f"Player {game_status} wins!")



def connectk_inputs():

    connectk_config = CONFIG
    connectk_config["game"] += "connectk"

    print("=============== Connect K ===============")
    print("1. View Rules")
    print("2. Play Connect K")
    print("3. Exit")
    print("=========================================")
    connectk_option = validate_input(
        "Please select an option [1, 2, 3]: ", ["1", "2", "3"]
    )
    clear_screen()

    if connectk_option == "1":  # Rules
        print_rules(connectk_config["game"])
        home_input = validate_input(
            "Please select an option [home, exit]: ", ["home", "exit"]
        )
        if home_input == "home":  # Back to main menu
            main()
        else:  # Exit
            clear_screen()
            exit()

    elif connectk_option == "2":  # Configure game
        connectk_config["rows"] = int(
            validate_input(
                "Input the number of rows for your board (max 100, min 2): ",
                [str(i) for i in range(2, 101)],
            )
        )
        connectk_config["columns"] = int(
            validate_input(
                "Input the number of columns for your board (max 100, min 2): ",
                [str(i) for i in range(2, 101)],
            )
        )
        # Calculate the maximum value a user can input while still making the game valid
        max_input = max(connectk_config["rows"], connectk_config["columns"])
        connectk_config["win_pieces"] = int(
            validate_input(
                "Input the number of connected pieces needed to win (can't be larger than row and column number): ",
                [
                    str(i) for i in range(1, max_input + 1)
                ],  # Valid inputs between 1 and the larger of row and column number
            )
        )
        connectk_config["human_players"] = int(
            validate_input(
                "Input the number of human players (total players can't be larger than row and column number, or lower than 2): ",
                [str(i) for i in range(0, max_input + 1)],
            )
        )
        if connectk_config["human_players"] == 0:
            min_cpus = 2
        elif connectk_config["human_players"] == 1:
            min_cpus = 1
        else:
            min_cpus = 0
        connectk_config["cpu_players"] = int(
            validate_input(
                "Input the number of CPU players (total players can't be larger than row and column number, or lower than 2): ",
                [
                    str(i)
                    for i in range(
                        min_cpus, max_input - connectk_config["human_players"] + 1
                    )
                ],  # CPU players + human players cannot exceed max input
            )
        )
        connectk_config["total_players"] = (
            connectk_config["cpu_players"] + connectk_config["human_players"]
        )
        for i in range(connectk_config["cpu_players"]):
            level = validate_input(
                f"Input the difficulty level for CPU no. {i + 1} from [easy, medium, hard]: ",
                ["easy", "medium", "hard"],
            )
            connectk_config["cpu_levels"].append(level)
        connectk_config["first_turn"] = validate_input(
            "Input which player type you want to begin the game from [humans, cpus, randomized]: ",
            ["humans", "cpus", "randomized"],
        )
    else:  # Exit
        clear_screen()
        exit()
    return connectk_config


def connect4_inputs():

    connect4_config = CONFIG
    connect4_config["game"] += "connect4"
    connect4_config["rows"] = 7
    connect4_config["columns"] = 6
    connect4_config["win_pieces"] = 4
    connect4_config["total_players"] = 2

    print("=============== Connect 4 ===============")
    print("1. View Rules")
    print("2. Play a local 2 player game")
    print("3. Play a game against the computer")
    print("4. Exit")
    print("=========================================")

    connect4_option = validate_input(
        "Please select an option [1, 2, 3, 4]: ", ["1", "2", "3", "4"]
    )
    clear_screen()
    if connect4_option == "1":  # Rules
        print_rules("4")
        home_input = validate_input(
            "Please select an option [home, exit]: ", ["home", "exit"]
        )
        if home_input == "home":  # Back to main menu
            main()
        else:  # Exit
            clear_screen()
            exit()
    elif connect4_option == "2":  # Local game
        connect4_config["human_players"] = 2
        connect4_config["cpu_players"] = 0
    elif connect4_option == "3":  # Human vs CPU
        connect4_config["human_players"] = 1
        connect4_config["cpu_players"] = 1
        difficulty = validate_input(
            "Please select a difficulty from [easy, medium, hard]: ",
            ["easy", "medium", "hard"],
        )
        connect4_config["cpu_levels"].append(difficulty)
        connect4_config["first_turn"] = validate_input(
            "Please choose which player type will go first from [humans, cpus, randomized]: ",
            ["humans, cpus, randomized"],
        )

    else:  # Exit
        clear_screen()
        exit()
    return connect4_config


def main():
    """
    Start program, displays menu which leads to other functions.

    :return: config dict
    """
    clear_screen()

    print("============= Main Menu =============")
    print("1. Connect K")
    print("2. Connect 4")
    print("3. Exit")
    print("=====================================")

    menu_option = validate_input("Please select an option [1, 2, 3]: ", ["1", "2", "3"])
    clear_screen()
    if menu_option == "1":
        connectk_config = connectk_inputs()
        board = create_board(connectk_config["rows"], connectk_config["columns"])
        run_game(board, connectk_config)
    elif menu_option == "2":
        connect4_config = connect4_inputs()
        board = create_board(connect4_config["rows"], connect4_config["columns"])
        run_game(board, connect4_config)
    else:
        clear_screen()
        exit()

if __name__ == "__main__":
    main()