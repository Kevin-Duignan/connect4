import random


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


# Copy and paste any code from previous tasks here


def cpu_player_medium(board, player):
    """
    Executes a move for the CPU on medium difficulty.
    It first checks for an immediate win and plays that move if possible.
    If no immediate win is possible, it checks for an immediate win
    for the opponent and blocks that move. If neither of these are
    possible, it plays a random move.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """

    opponent = 0
    if player == 1:
        opponent = 2
    else:
        opponent = 1
    opponent_move = -1

#simulate dropping both player and cpu piece in each available column and use end_of_game function to check if that position will produce a win
    for i in range(7):#7 possible moves/columns to check for immediate wins
        duplicate_board = [row[:] for row in board]#duplicate board
        row_index = 6
        for row in duplicate_board:
            row_index -= 1
            if duplicate_board[row_index][i] == 0:
                duplicate_board[row_index][i] = player#simulate drop_piece for cpu to check for immediate win
                if end_of_game(duplicate_board) == player:
                    duplicate_board = [row[:] for row in board]
                    drop_piece(board, player, i + 1)
                    return i + 1 #return move as taking an immediate win for cpu is higher priority than possibly blocking opponent move

                else:#simulate drop_piece for opponent to check if there are any immediate wins for them to block by cpu
                    duplicate_board = [row[:] for row in board]
                    duplicate_board[row_index][i] = opponent
                    if end_of_game(duplicate_board) == opponent:
                        if opponent_move == -1:
                            opponent_move = i + 1#dont return column move as there could still be an immediate win for cpu

    cpu_move = -1
    cpu_move = opponent_move#if there was immediate block, value of -1 would change

#if no immediate blocks or immediate wins available, output a random availiable column move
    while cpu_move == -1:
        rand = random.randrange(1, 8)
        if drop_piece(board, player, rand) == True:
            cpu_move = rand
            return rand
#if cpu_move exists(meaning there was an immediate block available to prevent opponent win)
    drop_piece(board, player, cpu_move)
    return cpu_move


board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0],
    [1, 1, 0, 2, 0, 0, 0],
    [1, 1, 0, 2, 2, 0, 2],
]

print(end_of_game(board))
