# Kevin
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


def create_board():

    # Implement your solution below
    board_row = 6
    board_col = 7
    board = [[0 for i in range(board_col)] for i in range(board_row)]
    return board


if __name__ == "__main__":
    # Enter test code below
    board = create_board()
    drop_piece(board, 1, 3)
    for row in board:
        print(row)
