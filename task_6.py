# Rohit
def end_of_game(board):  # Question 6 - Rohit
    """
    Checks if the game has ended with a winner
    or a draw.

    :param board: The game board, 2D list of 6 rows x 7 columns.
    :return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
    """
      
    # # * Rows -> List of Strings
    # for row in board:
    #     row_str = "".join([str(i) for i in row])
        
    #     # Check if row has a win
    #     if "1111" in row_str:
    #         return 1
    #     elif "2222" in row_str:
    #         return 2
            
    # # * Columns -> List of Strings
    # for i in range(len(board[0])): # Length of each row in original board
    #     column_string = ""
    #     # Concatenate elements of ith index from each row into a string
    #     for row in board:
    #         column_string += str(row[i])
        
    #     # Check if column has a win
    #     if "1111" in column_string:
    #         return 1
    #     elif "2222" in column_string:
    #         return 2
        
    

    # * Keep Playing or Draw
    for row in board:
        if 0 in row:
            return 0 # Still empty slots left
    else:
        return 3 # All slots are filled and no win     
    


board = [
    [1, 2, 1, 1, 2, 2, 1],
    [2, 1, 2, 2, 1, 2, 2],
    [2, 1, 1, 2, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 1, 1, 1, 2],
    [2, 2, 2, 1, 2, 1, 2]]

print(end_of_game(board))
