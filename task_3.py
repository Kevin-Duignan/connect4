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
		print("|", end = "")
		for col in range(board_col):
			if board[row][col] == 1:
				print(" X |", end = "")
			elif board[row][col] == 2:
				print(" O |", end = "")
			elif board[row][col] == 0:
				print("   |", end = "")
		print("\n --- --- --- --- --- --- ---")
	print("=============================")

		
	

def create_board():

    # Implement your solution below
    board_row = 6
    board_col = 7
    board = [[0 for i in range(board_col)] for i in range(board_row)]
    return board


if __name__ == "__main__":
	# Enter test code below
	board = create_board()
	board[5][0], board[5][1] = 1, 2 # place a 1 in bottom left cell and a 2 in the cell directly to the right
	print_board(board)