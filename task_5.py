# Copy and paste validate_input here
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
    return [[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]


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
    for row in reversed(board):
        # Drop player token in the lowest free space
        # Array index start at 0, but humans count from 1, so minus one from input column account for that
        if row[column - 1] == 0:
            row[column - 1] = player
            return True

    # If all spaces are filled (no 0s)
    return False


def execute_player_turn(player, board):  # Task 5
    """
    Prompts user for a legal move given the current game board
    and executes the move.

    :return: Column that the piece was dropped into, int.
    """
    while True:
        column = int(input(f"Player {player}, please enter the column you would like to drop your piece into: "))
        # drop_piece returns true if there is space
        if drop_piece(board, player, column):
            return column
        else:
            print("That column is full, please try again.")


if __name__ == "__main__":
    # Enter test code below
    board = create_board()
    move = execute_player_turn(1, board)
    print(move)
