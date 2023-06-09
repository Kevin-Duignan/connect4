def validate_input(prompt, valid_inputs):
    """
    Repeatedly ask user for input until they enter an input
    within a set valid of options.

    :param prompt: The prompt to display to the user, string.
    :param valid_inputs: The range of values to accept, list
    :return: The user's input, string.
    """
    # Implement your solution below
    print(prompt, end="")
    enter = input()
    if enter in valid_inputs:
        return enter
    else:
        print("Invalid input, please try again.")
        return validate_input(prompt, valid_inputs)


# Copy and paste create_board here
def create_board():
    """
    Returns a 2D list of 6 rows and 7 columns to represent
    the game board. Default cell value is 0.

    :return: A 2D list of 6x7 dimensions.
    """
    # Implement your solution below
    board_row = 6
    board_col = 7
    board = [[0 for i in range(board_col)] for i in range(board_row)]
    return board


# Copy and paste print_board here
def print_board(board):
    """
    Prints the game board to the console.

    :param board: The game board, 2D list of 6x7 dimensions.
    :return: None
    """
    # Implement your solution below
    board_row = 6
    board_col = 7
    print("========== Connect4 =========")
    print("Player 1: X       Player 2: O\n")
    print("  1   2   3   4   5   6   7")
    print(" --- --- --- --- --- --- ---")
    for row in range(board_row):
        print("|", end="")
        for col in range(board_col):
            if board[row][col] == 1:
                print(" X |", end="")
            elif board[row][col] == 2:
                print(" O |", end="")
            elif board[row][col] == 0:
                print("   |", end="")
        print("\n --- --- --- --- --- --- ---")
    print("=============================")


# Copy and paste drop_piece here
def drop_piece(board, player, column):
    """
    Drops a piece into the game board in the given column.
    Please note that this function expects the column index
    to start at 1.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player dropping the piece, int.
    :param column: The index of column to drop the piece into, int.
    :return: True if piece was successfully dropped, False if not.
    """
    # Iterate through each row from bottom up
    if 1 <= column <= 7:
        for row in reversed(board):
            # Drop player token in the lowest free space
            if row[column - 1] == 0:
                row[column - 1] = player
                return True

    # If all spaces are filled (no 0s)
    return False


# Copy and paste execute_player_turn here
def execute_player_turn(player, board):  # Task 5
    """
    Prompts user for a legal move given the current game board
    and executes the move.

    :return: Column that the piece was dropped into, int.
    """
    while True:
        column = int(
            input(
                f"Player {player}, please enter the column you would like to drop your piece into: "
            )
        )
        # drop_piece returns true if there is space
        if drop_piece(board, player, column):
            return column
        else:
            print("Invalid turn, please try again.")


# Copy and paste end_of_game here
def end_of_game(board):
    """
    Checks if the game has ended with a winner
    or a draw.

    :param board: The game board, 2D list of 6 rows x 7 columns.
    :return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
    """
    # Implement your solution below

    # creating another board that has its rows filled with the columns of the original board
    vert_board = [0] * len(board[0])

    def verti_row(board, board_column_index):
        vert_row = [0] * len(board)
        row_column_index = -1
        for row in board:
            row_column_index += 1
            vert_row[row_column_index] = row[board_column_index]
        return vert_row

    column_index = -1
    for i in vert_board:
        column_index += 1
        vert_board[column_index] = verti_row(board, column_index)

    # creating another board that has its rows filled with the diagonals of the original board
    def diagonal_row(board, row_index, column_index):
        diag_row = [3] * len(board)
        diag_index = -1
        for row in board:
            if row_index <= len(board) - 1 and column_index <= len(board[0]) - 1:
                diag_index += 1
                diag_row[diag_index] = board[row_index][column_index]
                column_index += 1
                row_index += 1
            else:
                break
        return diag_row

    def diagonal_board(board):
        diag_board = [0] * (len(board) + (len(board[0]) - 1))
        column_index = 0
        row_index = len(board)
        for i in range(len(board) + (len(board[0]) - 1)):
            if row_index >= 1:
                row_index -= 1
            elif column_index <= (len(board[0]) - 1):
                column_index += 1
            diag_board[i] = diagonal_row(board, row_index, column_index)
        return diag_board

    reversed_board = [0] * len(board)
    index = 0
    for i in board:
        reversed_board[index] = i[::-1]
        index += 1

    # function to check the status of game by verifying spliced lists of all rows of the boards
    def check_game_status(board, possibilities):
        game_status = 0
        game_can_continue = -1
        for row in board:
            splice_int1 = 0
            for i in range(possibilities):
                if (
                    0 in row[splice_int1 : (splice_int1 + 4)]
                    and 1 not in row[splice_int1 : (splice_int1 + 4)]
                    and 2 not in row[splice_int1 : (splice_int1 + 4)]
                    and 3 not in row[splice_int1 : (splice_int1 + 4)]
                ):
                    game_can_continue = 0
                if (
                    0 in row[splice_int1 : (splice_int1 + 4)]
                    or 3 in row[splice_int1 : (splice_int1 + 4)]
                ):
                    splice_int1 += 1
                    pass
                elif (
                    1 in row[splice_int1 : (splice_int1 + 4)]
                    and 2 in row[splice_int1 : (splice_int1 + 4)]
                ):
                    splice_int1 += 1
                    pass
                else:
                    game_status = row[splice_int1 : (splice_int1 + 4)][0]
        return [game_status, game_can_continue]

        # function to check the status of game by verifying spliced lists of all rows of the boards

    def check_game_status(board, possibilities):
        game_status = 0
        game_can_continue = -1
        for row in board:
            splice_int1 = 0
            for i in range(possibilities):
                if 0 in row[splice_int1 : (splice_int1 + 4)]:
                    game_can_continue = 0
                if (
                    0 in row[splice_int1 : (splice_int1 + 4)]
                    or 3 in row[splice_int1 : (splice_int1 + 4)]
                ):
                    splice_int1 += 1
                    pass
                elif (
                    1 in row[splice_int1 : (splice_int1 + 4)]
                    and 2 in row[splice_int1 : (splice_int1 + 4)]
                ):
                    splice_int1 += 1
                    pass
                else:
                    game_status = row[splice_int1 : (splice_int1 + 4)][0]
        return [game_status, game_can_continue]

    # computing final status of game
    final_result = 0
    if check_game_status(board, 4)[0] != 0:
        final_result = check_game_status(board, 4)[0]
    elif check_game_status(vert_board, 3)[0] != 0:
        final_result = check_game_status(vert_board, 3)[0]
    elif check_game_status(diagonal_board(board), 3)[0] != 0:
        final_result = check_game_status(diagonal_board(board), 3)[0]
    elif check_game_status(diagonal_board(reversed_board), 3)[0] != 0:
        final_result = check_game_status(diagonal_board(reversed_board), 3)[0]
    else:
        if (
            check_game_status(board, 4)[1] == 0
            and check_game_status(vert_board, 3)[1] == 0
            and check_game_status(diagonal_board(board), 3)[1] == 0
            and check_game_status(diagonal_board(reversed_board), 3)[0] == 0
        ):
            pass
        else:
            final_result = 3

    return final_result


# Copy and paste local_2_player_game here
def local_2_player_game():
    """
    Defines the main application loop.
    User chooses a type of game to play or to exit.

    :return: None
    """
    # Implement your solution below

    turn_counter = 0

    # Do While
    while True:
        clear_screen()
        print_board(board)
        # If start of game
        if turn_counter == 0:
            # Player 1 starts
            print("Your turn to start, Player 1!")
            move = execute_player_turn(1, board)
            turn_counter += 1
            game_status = end_of_game(board)

        # Else if in the middle of a game
        elif game_status == 0:
            # Compute player turn
            player = (turn_counter % 2) + 1  # Even turn is p1, odd turn is p2
            previous_player = ((turn_counter - 1) % 2) + 1  # Last turn

            # Previous move and prompt for next move
            print(f"Player {previous_player}'s turn was column {move}.")
            move = execute_player_turn(player, board)

            turn_counter += 1
            game_status = end_of_game(board)

        # If game is over
        else:
            break

    # When game has ended
    if game_status == 3:
        print("It's a draw!")
    else:
        # execute_player_turn returns player number if that player wins
        print(f"Player {game_status} wins!")


def print_rules():
    """
    Prints the rules of the game.
    :return: None
    """
    print("================= Rules =================")
    print("Connect 4 is a two-player game where the")
    print("objective is to get four of your pieces")
    print("in a row either horizontally, vertically")
    print("or diagonally. The game is played on a")
    print("6x7 grid. The first player to get four")
    print("pieces in a row wins the game. If the")
    print("grid is filled and no player has won,")
    print("the game is a draw.")
    print("=========================================")


def clear_screen():
    """
    Clears the terminal for Windows and Linux/MacOS.
    :return: None
    """
    import os

    os.system("cls" if os.name == "nt" else "clear")


def main():
    """
        Defines the main application loop.
    User chooses a type of game to play or to exit.
        :return: None
    """
    clear_screen()
    # Implement your solution below
    print("=============== Main Menu ===============")
    print("Welcome to Connect 4!")
    print("1. View Rules")
    print("2. Play a local 2 player game")
    print("3. Play a game against the computer")
    print("4. Exit")
    print("=========================================")

    user_input = validate_input(
        "Please select an option (1, 2, 3, 4): ", ["1", "2", "3", "4"]
    )

    if user_input == "1":
        clear_screen()
        print_rules()
        home_input = validate_input(
            "Please select an option (home, exit): ", ["home", "exit"]
        )
        if home_input == "home":
            main()
        elif home_input == "exit":
            exit()
    elif user_input == "2":
        clear_screen()
        local_2_player_game()
    elif user_input == "3":
        clear_screen()
        # TODO: game_against_cpu()
    elif user_input == "4":
        clear_screen()
        exit()


board = board = [[0 for i in range(7)] for i in range(6)]
main()
