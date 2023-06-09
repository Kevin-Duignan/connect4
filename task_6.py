# Rohit original
# Kevin re-implementation


def end_of_game(board):
    """
    Checks if the game has ended with a winner
    or a draw.

    :param board: The game board, 2D list of 6 rows x 7 columns.
    :return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
    """

    # * Win Check
    def win(string):
        if "1111" in string:
            return 1
        elif "2222" in string:
            return 2

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
                    diagonal_str += str(board[i][j])
                    i += 1
                    j -= 1
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
        return 3  # All slots are filled so draw
    else:
        return 0  # There are empty slots left so keep playing
