# Kevin
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


if __name__ == "__main__":
    # Enter test code below
    print(create_board())
