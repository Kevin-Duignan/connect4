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
	board_row = 6
	board_col = 7
	board = [[0 for i in range(board_col)] for i in range(board_row)]
	return board

# Copy and paste print_board here
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

# Copy and paste execute_player_turn here
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

# Copy and paste end_of_game here
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

#Don't forget to include any helper functions you may have created


def clear_screen():
	"""
	Clears the terminal for Windows and Linux/MacOS.

	:return: None
	"""
	import os
	os.system('cls' if os.name == 'nt' else 'clear')
	

def local_2_player_game():
	"""
	Runs a local 2 player game of Connect 4.

	:return: None
	"""
	# Implement your solution below
	raise NotImplementedError


if __name__ == "__main__":
	# Enter test code below
	local_2_player_game()