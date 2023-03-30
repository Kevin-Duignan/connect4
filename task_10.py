import random

import random


def end_of_game(board):  # Question 6
    """
    Checks if the game has ended with a winner
    or a draw.

    :param board: The game board, 2D list of 6 rows x 7 columns.
    :return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
    """
    # Implement your solution below

    # creating another board that has its rows filled with the columns of the original board
    vert_board = []

    def vert_row(board, board_column_index):
        verti_row = []
        for row in board:
            verti_row += [row[board_column_index]]
        return verti_row

    for i in range(len(board[0])):
        vert_board += [vert_row(board, i)]

    # creating another board that has its rows filled with the diagonals of the original board
    def diagonal_row(board, row_index, column_index):
        diag_row = []
        for row in board:
            if row_index <= len(board) - 1 and column_index <= len(board[0]) - 1:
                diag_row += [board[row_index][column_index]]
                column_index += 1
                row_index += 1
            else:
                break
        return diag_row

    def diagonal_board(board):
        diag_board = []
        column_index = 0
        row_index = len(board)
        for i in range(12):
            if row_index >= 1:
                row_index -= 1
            elif column_index <= 6:
                column_index += 1
            diag_board += [diagonal_row(board, row_index, column_index)]
        return diag_board

    reversed_board = []
    for i in board:
        reversed_board += [i[::-1]]

    # function to check the status of game by verifying spliced lists of all rows of the boards
    def check_game_status(board):
        str_board = []
        for row in board:
            str_row = ""
            for value in row:
                str_row += str(value)
            str_board += [str_row]
        game_status = 0
        for row in str_board:
            if "0" in row:
                game_can_continue = 0
            if "1111" in row:
                game_status = 1
            if "2222" in row:
                game_status = 2
        return game_status

    game_can_continue = -1
    for row in board:
        if 0 in row:
            game_can_continue = 0
    if check_game_status(board) != 0:
        return check_game_status(board)
    elif check_game_status(vert_board) != 0:
        return check_game_status(vert_board)
    elif check_game_status(diagonal_board(board)) != 0:
        return check_game_status(diagonal_board(board))
    elif check_game_status(diagonal_board(reversed_board)) != 0:
        return check_game_status(diagonal_board(reversed_board))
    else:
        if game_can_continue == 0:
            return 0
        else:
            return 3


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

    def duplicate_board(board):
        new_brd = []
        for row in board:
            new_brd += [row[:]]
        return new_brd

    player_move = -1
    opponent_move = -1

    for i in range(7):
        new_board = duplicate_board(board)
        if drop_piece(new_board, player, i + 1) == True:
            new_board = duplicate_board(board)
            row_index = 6
            for row in new_board:
                row_index -= 1
                if new_board[row_index][i] == 0:
                    new_board[row_index][i] = player
                    if end_of_game(new_board) == player:
                        new_board = duplicate_board(board)
                        drop_piece(board, player, i + 1)
                        return i + 1

                    else:
                        new_board = duplicate_board(board)
                        new_board[row_index][i] = opponent
                        if end_of_game(new_board) == opponent:
                            if opponent_move == -1:
                                opponent_move = i + 1

    cpu_move = -1
    cpu_move = opponent_move

    while cpu_move == -1:
        rand = random.randrange(1, 8)
        if drop_piece(board, player, rand) == True:
            cpu_move = rand
            return rand

    return cpu_move


board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0],
    [1, 1, 0, 2, 0, 0, 0],
    [1, 1, 0, 2, 2, 0, 2],
]
