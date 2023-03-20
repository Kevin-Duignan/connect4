def end_of_game(board):  # Question 6 - Rohit
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
        diag_row = ([3] * len(board))
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
                if 0 in row[splice_int1:(splice_int1 + 4)] and 1 not in row[
                                                                        splice_int1:(splice_int1 + 4)] and 2 not in row[
                                                                                                                    splice_int1:(
                                                                                                                            splice_int1 + 4)] and 3 not in row[
                                                                                                                                                           splice_int1:(
                                                                                                                                                                   splice_int1 + 4)]:
                    game_can_continue = 0
                if 0 in row[splice_int1:(splice_int1 + 4)] or 3 in row[splice_int1:(splice_int1 + 4)]:
                    splice_int1 += 1
                    pass
                elif 1 in row[splice_int1:(splice_int1 + 4)] and 2 in row[splice_int1:(splice_int1 + 4)]:
                    splice_int1 += 1
                    pass
                else:
                    game_status = row[splice_int1:(splice_int1 + 4)][0]
        return ([game_status, game_can_continue])

    # check horizontal wins
    # print(check_game_status(board, 4))

    # check vertical wins
    # print(check_game_status(vert_board, 3))

    # check diagonal wins
    # forwards_diagonal
    # print(check_game_status(diagonal_board(board), 3))

    # backwards_diagonal
    # print(check_game_status(diagonal_board(reversed_board), 3))

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
        if check_game_status(board, 4)[1] == 0 and check_game_status(vert_board, 3)[1] == 0 and \
                check_game_status(diagonal_board(board), 3)[1] == 0 and \
                check_game_status(diagonal_board(reversed_board), 3)[0] == 0:
            pass
        else:
            final_result = 3

    return final_result
