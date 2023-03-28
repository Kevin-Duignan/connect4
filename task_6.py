# Rohit
def end_of_game(board):  # Question 6 - Rohit
    """
    Checks if the game has ended with a winner
    or a draw.

    :param board: The game board, 2D list of 6 rows x 7 columns.
    :return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
    """
    # Containing strings of each row in original board
    row_board = []
    # Containing strings of each column in a row
    column_board = []
    
    # * Rows -> List of Strings
    for row in board:
        row_board.append("".join([str(i) for i in row])) # Can't append elements of instant int
            
    # * Columns -> List of Strings
    for i in range(len(board[0])): # Length of each row in original board
        column_string = ""
        # Concatenate elements of ith index from each row into a string
        for row in board:
            column_string+= str(row[i])
        column_board.append(column_string)
            
    print(row_board)
    print(column_board)
            
            
    


board = [
    [1, 2, 1, 1, 2, 2, 0],
    [2, 1, 2, 2, 1, 2, 2],
    [2, 1, 1, 2, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 1, 1, 1, 2],
    [2, 2, 2, 1, 2, 1, 2]]

print(end_of_game(board))
